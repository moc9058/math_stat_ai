"""Resumable single-worker OCR over a complete book in bounded chunks."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
TOTAL = {"Brezis": 614, "Conway": 416}


def completed_pages(book: str) -> set[int]:
    """Return every page covered by a valid completed chunk.

    Pilot runs use one-page chunks while full runs normally use larger chunks.
    Looking at page coverage, rather than only the next chunk's marker, avoids
    repeating those pilot pages.
    """
    completed: set[int] = set()
    for marker in (HERE / "chunks" / book.lower()).glob("p*-p*/complete.json"):
        try:
            import json

            payload = json.loads(marker.read_text(encoding="utf-8"))
            if payload.get("book") == book:
                completed.update(int(page) for page in payload.get("pages", []))
        except (OSError, ValueError, TypeError):
            continue
    return completed


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("book", choices=TOTAL)
    cli.add_argument("--chunk-size", type=int, default=8)
    args = cli.parse_args()
    if args.chunk_size < 1 or args.chunk_size > 32:
        cli.error("chunk size must be 1..32")
    done = completed_pages(args.book)
    pending = [page for page in range(1, TOTAL[args.book] + 1) if page not in done]
    ranges: list[tuple[int, int]] = []
    for page in pending:
        if not ranges or page != ranges[-1][1] + 1 or page - ranges[-1][0] >= args.chunk_size:
            ranges.append((page, page))
        else:
            ranges[-1] = (ranges[-1][0], page)
    print(f"already_complete={len(done)} pending={len(pending)} ranges={len(ranges)}", flush=True)
    for first, last in ranges:
        marker = HERE / "chunks" / args.book.lower() / f"p{first:04}-p{last:04}" / "complete.json"
        print(f"start {args.book} {first}-{last}", flush=True)
        log_path = HERE / "chunks" / args.book.lower() / f"p{first:04}-p{last:04}" / "run.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("w", encoding="utf-8") as log:
            code = subprocess.run(
                [sys.executable, str(HERE / "convert_chunk.py"), args.book, str(first), str(last)],
                cwd=HERE,
                stdout=log,
                stderr=subprocess.STDOUT,
            ).returncode
        if code:
            print(f"failed {args.book} {first}-{last}: exit {code}; log={log_path}", flush=True)
            raise SystemExit(code)
        print(f"done {args.book} {first}-{last}", flush=True)
    print(f"ocr_complete={args.book} pages={TOTAL[args.book]}", flush=True)


if __name__ == "__main__":
    main()
