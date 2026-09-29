"""Resumable page transcription and independent image review via OpenAI API."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOTAL = {"Brezis": 614, "Conway": 416}


def analyze_review(path: Path) -> dict:
    raw = json.loads(path.read_text(encoding="utf-8"))
    review = raw["review"].strip()
    if review.startswith("```"):
        review = review.split("\n", 1)[1].rsplit("```", 1)[0]
    try:
        parsed = json.loads(review)
    except json.JSONDecodeError:
        return {"safe_to_accept": False, "errors": [], "uncertain_regions": ["review JSON invalid"]}
    return {"safe_to_accept": parsed.get("safe_to_accept") is True,
            "errors": parsed.get("errors", []),
            "uncertain_regions": parsed.get("uncertain_regions", [])}


def process(book: str, number: int, out: Path) -> dict:
    stem = f"{book.lower()}-p{number:04}"
    status_path = out / f"{stem}-status.json"
    if status_path.exists():
        prior = json.loads(status_path.read_text(encoding="utf-8"))
        if prior["status"] != "api_failed" or prior.get("attempts", 0) >= 3:
            return prior
        attempts = prior.get("attempts", 0) + 1
    else:
        attempts = 1
    transcript = out / f"{stem}-gpt-6-sol-transcription.md"
    review = out / f"{stem}-gpt-6-astra-transcription-review.json"
    commands = []
    if not transcript.exists():
        commands.append([sys.executable, "transcribe_page.py", book, str(number), "--model", "gpt-6-sol", "--out-dir", str(out)])
    if not review.exists():
        commands.append([sys.executable, "review_page.py", book, str(number), "--model", "gpt-6-astra",
                         "--candidate-path", str(transcript), "--out-dir", str(out)])
    for command in commands:
        result = subprocess.run(command, cwd=HERE, capture_output=True, text=True)
        if result.returncode:
            failure = {"book": book, "pdf_page": number, "status": "api_failed",
                       "step": command[1], "attempts": attempts,
                       "error": result.stdout[-1000:] + result.stderr[-1000:]}
            status_path.write_text(json.dumps(failure, ensure_ascii=False, indent=2), encoding="utf-8")
            return failure
    findings = analyze_review(review)
    result = {"book": book, "pdf_page": number,
              "status": "ai_review_passed" if findings["safe_to_accept"] and not findings["errors"] and not findings["uncertain_regions"] else "needs_further_review",
              "safe_to_accept": findings["safe_to_accept"],
              "error_count": len(findings["errors"]),
              "uncertain_count": len(findings["uncertain_regions"]),
              "transcription": str(transcript.relative_to(HERE)),
              "review": str(review.relative_to(HERE))}
    status_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("book", choices=TOTAL)
    cli.add_argument("--first", type=int, default=1)
    cli.add_argument("--last", type=int)
    cli.add_argument("--workers", type=int, default=2)
    cli.add_argument("--follow", action="store_true", help="watch for newly completed OCR chunks")
    args = cli.parse_args()
    last = args.last or TOTAL[args.book]
    if args.first < 1 or last > TOTAL[args.book] or args.first > last or not 1 <= args.workers <= 4:
        cli.error("invalid page range or worker count")
    out = HERE / "api" / args.book.lower()
    out.mkdir(parents=True, exist_ok=True)
    idle_rounds = 0
    while True:
        if args.follow:
            subprocess.run([sys.executable, "materialize_pages.py", args.book], cwd=HERE,
                           stdout=subprocess.DEVNULL, check=True)
        available = [n for n in range(args.first, last + 1)
                     if list((HERE / "chunks" / args.book.lower()).glob(f"p*-p*/page-{n:04}.md"))]
        pending = []
        for number in available:
            status_path = out / f"{args.book.lower()}-p{number:04}-status.json"
            if not status_path.exists():
                pending.append(number)
            else:
                previous = json.loads(status_path.read_text(encoding="utf-8"))
                if previous["status"] == "api_failed" and previous.get("attempts", 0) < 3:
                    pending.append(number)
        print(f"available={len(available)} pending={len(pending)} requested={last-args.first+1}", flush=True)
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(process, args.book, n, out): n for n in pending}
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                print(f"page={result['pdf_page']} status={result['status']}", flush=True)
        if not args.follow or len(available) == last - args.first + 1:
            break
        idle_rounds = 0 if pending else idle_rounds + 1
        if idle_rounds >= 60:
            raise SystemExit("no new OCR pages for 20 minutes")
        time.sleep(20)


if __name__ == "__main__":
    main()
