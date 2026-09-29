"""Verify reviewer findings against the PDF image, then re-review a revision."""

from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
import time
from pathlib import Path

import pymupdf
from openai import OpenAI

from review_page import api_key

HERE = Path(__file__).resolve().parent
BOOK_ROOT = HERE.parents[1]


def review_data(path: Path) -> dict:
    response = json.loads(path.read_text(encoding="utf-8"))
    raw = response["review"].strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0]
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"safe_to_accept": False, "errors": [], "uncertain_regions": ["invalid reviewer JSON"]}


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("book", choices=["Brezis", "Conway"])
    cli.add_argument("page", type=int)
    args = cli.parse_args()
    out = HERE / "api" / args.book.lower()
    stem = f"{args.book.lower()}-p{args.page:04}"
    status_path = out / f"{stem}-status.json"
    status = json.loads(status_path.read_text(encoding="utf-8"))
    if status["status"] not in ("needs_further_review", "needs_manual_review"):
        print(f"skip {args.book} {args.page}: {status['status']}")
        return
    original = out / f"{stem}-gpt-6-sol-transcription.md"
    first_review = out / f"{stem}-gpt-6-astra-transcription-review.json"
    repaired = out / f"{stem}-gpt-6-astra-repair.md"
    if not repaired.exists():
        pdf = BOOK_ROOT / "source" / f"{args.book}.pdf"
        with pymupdf.open(pdf) as doc:
            image = doc[args.page - 1].get_pixmap(matrix=pymupdf.Matrix(2.5, 2.5), alpha=False).tobytes("jpeg", jpg_quality=90)
        image_url = "data:image/jpeg;base64," + base64.b64encode(image).decode("ascii")
        findings = review_data(first_review)
        prompt = (
            "Recheck a mathematics textbook page transcription against its page image. "
            "The prior reviewer suggestions are hypotheses: some can be false. Verify each against the image. "
            "Return a complete corrected Markdown page preserving the source's exact wording, even typos, "
            "and every math symbol, heading, equation number, figure and exercise in reading order. "
            "Use $...$ and $$...$$ for MathJax. Mark unreadable text [UNCLEAR: reason]. "
            "Return Markdown only, without explanation.\n\n"
            f"PDF page {args.page}\n\nPrior transcription:\n{original.read_text(encoding='utf-8')[:18000]}\n\n"
            f"Reviewer hypotheses:\n{json.dumps(findings, ensure_ascii=False)[:6000]}"
        )
        started = time.perf_counter()
        response = OpenAI(api_key=api_key(), timeout=240).responses.create(
            model="gpt-6-astra", reasoning={"effort": "medium"},
            input=[{"role": "user", "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": image_url, "detail": "original"},
            ]}],
        )
        repaired.write_text(response.output_text.rstrip() + "\n", encoding="utf-8")
        (repaired.with_suffix(".json")).write_text(json.dumps({
            "book": args.book, "pdf_page": args.page, "model": "gpt-6-astra",
            "seconds": round(time.perf_counter() - started, 2),
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
        }, indent=2), encoding="utf-8")
    second_review = out / f"{stem}-gpt-6-astra-transcription-repair-review.json"
    if not second_review.exists():
        command = [sys.executable, "review_page.py", args.book, str(args.page),
                   "--model", "gpt-6-astra", "--candidate-path", str(repaired),
                   "--out-dir", str(out), "--tag", "repair"]
        subprocess.run(command, cwd=HERE, check=True)
    findings = review_data(second_review)
    passed = findings.get("safe_to_accept") is True and not findings.get("errors") and not findings.get("uncertain_regions")
    status["status"] = "ai_repair_passed" if passed else "needs_manual_review"
    status["repair"] = str(repaired.relative_to(HERE))
    status["repair_review"] = str(second_review.relative_to(HERE))
    status["repair_error_count"] = len(findings.get("errors", []))
    status["repair_uncertain_count"] = len(findings.get("uncertain_regions", []))
    status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"page={args.page} status={status['status']}")


if __name__ == "__main__":
    main()
