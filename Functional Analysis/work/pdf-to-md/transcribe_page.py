"""Vision-assisted full-page transcription trial, stored separately from reviewed output."""

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
BOOK_ROOT = HERE.parents[1]
ROOT = HERE.parents[2]


def api_key() -> str:
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if line.startswith("OPENAI_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("OPENAI_API_KEY missing")


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("book", choices=["Brezis", "Conway"])
    cli.add_argument("page", type=int)
    cli.add_argument("--model", choices=["gpt-6-sol", "gpt-6-astra"], default="gpt-6-sol")
    cli.add_argument("--out-dir", type=Path, default=HERE / "pilot")
    args = cli.parse_args()
    candidate_path = HERE / "chunks" / args.book.lower() / f"p{args.page:04}-p{args.page:04}" / f"page-{args.page:04}.md"
    if not candidate_path.exists():
        matches = sorted((HERE / "chunks" / args.book.lower()).glob(f"p*-p*/page-{args.page:04}.md"))
        if not matches:
            raise SystemExit(f"OCR page draft missing: {args.book} {args.page}")
        candidate_path = matches[-1]
    candidate = re.sub(r"!\[\]\(data:image/[^)]+\)", "[figure to preserve]", candidate_path.read_text(encoding="utf-8"))
    pdf = BOOK_ROOT / "source" / f"{args.book}.pdf"
    with pymupdf.open(pdf) as doc:
        image = doc[args.page - 1].get_pixmap(matrix=pymupdf.Matrix(2.5, 2.5), alpha=False).tobytes("jpeg", jpg_quality=90)
    image_url = "data:image/jpeg;base64," + base64.b64encode(image).decode("ascii")
    prompt = (
        "Transcribe this entire mathematics textbook page into faithful Markdown with MathJax LaTeX. "
        "Use the page image as the authority and the machine OCR below only as a draft. "
        "Keep every heading, numbered result, proof, equation number, table, exercise, and caption in reading order. "
        "Preserve the author's wording and all meaningful symbols; never invent or silently omit content. "
        "Use $...$ for inline math and $$...$$ for display math. "
        "For a figure, write [FIGURE: describe labels and location] so it can be linked to an extracted asset. "
        "For unreadable text, write [UNCLEAR: brief reason] rather than guessing. "
        "Do not include a repeated running header or footer page number in the body. "
        "Return Markdown only, no code fence or commentary.\n\n"
        f"PDF page: {args.page}\nDraft OCR:\n{candidate[:18000]}"
    )
    started = time.perf_counter()
    try:
        response = OpenAI(api_key=api_key(), timeout=240).responses.create(
            model=args.model,
            reasoning={"effort": "medium"},
            input=[{"role": "user", "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": image_url, "detail": "high"},
            ]}],
        )
    except Exception as exc:
        print("api_error_type=", type(exc).__name__)
        raise SystemExit(1) from None
    args.out_dir.mkdir(parents=True, exist_ok=True)
    out = args.out_dir / f"{args.book.lower()}-p{args.page:04}-{args.model}-transcription.md"
    out.write_text(response.output_text.rstrip() + "\n", encoding="utf-8")
    usage = {
        "book": args.book,
        "pdf_page": args.page,
        "model": args.model,
        "seconds": round(time.perf_counter() - started, 2),
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
    }
    (out.with_suffix(".json")).write_text(json.dumps(usage, indent=2), encoding="utf-8")
    print(json.dumps(usage, indent=2))


if __name__ == "__main__":
    main()
