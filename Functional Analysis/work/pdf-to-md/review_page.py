"""Use a bounded OpenAI vision review for a single local OCR sample."""

from __future__ import annotations

import argparse
import base64
import json
import re
import time
from pathlib import Path

import pymupdf
from openai import OpenAI


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def api_key() -> str:
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if line.startswith("OPENAI_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("OPENAI_API_KEY missing")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("book", choices=["Brezis", "Conway"])
    parser.add_argument("page", type=int)
    parser.add_argument("--model", choices=["gpt-6-luna", "gpt-6-sol", "gpt-6-astra"], default="gpt-6-luna")
    parser.add_argument("--candidate-path", type=Path)
    parser.add_argument("--out-dir", type=Path, default=HERE / "pilot")
    parser.add_argument("--tag", default="")
    args = parser.parse_args()
    pdf = HERE.parents[1] / "source" / f"{args.book}.pdf"
    md = args.candidate_path or (HERE / "pilot" / f"{args.book.lower()}-p{args.page:03}.md")
    if not md.exists() and args.candidate_path is None:
        md = HERE / "chunks" / args.book.lower() / f"p{args.page:04}-p{args.page:04}" / f"page-{args.page:04}.md"
    if not md.exists() and args.candidate_path is None:
        matches = sorted((HERE / "chunks" / args.book.lower()).glob(f"p*-p*/page-{args.page:04}.md"))
        if not matches:
            raise SystemExit(f"OCR page draft missing: {args.book} {args.page}")
        md = matches[-1]
    candidate = re.sub(r"!\[\]\(data:image/[^)]+\)", "[inline figure]", md.read_text(encoding="utf-8"))
    with pymupdf.open(pdf) as doc:
        page = doc[args.page - 1]
        image = page.get_pixmap(matrix=pymupdf.Matrix(2.5, 2.5), alpha=False).tobytes("jpeg", jpg_quality=85)
    image_url = "data:image/jpeg;base64," + base64.b64encode(image).decode("ascii")
    prompt = (
        "You are reviewing one page of a mathematics textbook transcription against its page image. "
        "Do not rewrite the entire page. Identify up to 12 concrete transcription errors, especially "
        "missing words, wrong math symbols, equation numbers, theorem labels, and reading order. "
        "For each, give the candidate fragment and a correction only when visible with confidence. "
        "State whether the page is safe to accept without further human review. "
        "Return concise JSON with keys safe_to_accept, errors, uncertain_regions.\n\n"
        f"Candidate Markdown for PDF page {args.page}:\n{candidate[:16000]}"
    )
    started = time.perf_counter()
    try:
        response = OpenAI(api_key=api_key(), timeout=180).responses.create(
            model=args.model,
            reasoning={"effort": "medium" if args.model == "gpt-6-astra" else "low"},
            input=[{"role": "user", "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": image_url, "detail": "original" if args.model == "gpt-6-astra" else "high"},
            ]}],
        )
    except Exception as exc:
        print("api_error_type=", type(exc).__name__)
        raise SystemExit(1) from None
    result = {
        "book": args.book,
        "pdf_page": args.page,
        "model": args.model,
        "seconds": round(time.perf_counter() - started, 2),
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "review": response.output_text,
    }
    suffix = "-transcription" if args.candidate_path else ""
    args.out_dir.mkdir(parents=True, exist_ok=True)
    tag = f"-{args.tag}" if args.tag else ""
    out = args.out_dir / f"{args.book.lower()}-p{args.page:04}-{args.model}{suffix}{tag}-review.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "review"}, indent=2))
    print("review_file=", out)


if __name__ == "__main__":
    main()
