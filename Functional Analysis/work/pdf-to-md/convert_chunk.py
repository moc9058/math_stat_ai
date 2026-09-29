"""Checkpointed local MinerU OCR of a bounded PDF page range."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from mineru.parser import parse
from mineru.parser.writer import FileBasedDataWriter


HERE = Path(__file__).resolve().parent
BOOK_ROOT = HERE.parents[1]


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("book", choices=["Brezis", "Conway"])
    cli.add_argument("first", type=int)
    cli.add_argument("last", type=int)
    args = cli.parse_args()
    if args.first < 1 or args.last < args.first:
        cli.error("invalid page range")
    out = HERE / "chunks" / args.book.lower() / f"p{args.first:04}-p{args.last:04}"
    marker = out / "complete.json"
    if marker.exists():
        print(f"already_complete={marker}")
        return
    out.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    result = parse(
        BOOK_ROOT / "source" / f"{args.book}.pdf",
        tier="basic",
        ocr_mode="auto" if args.book == "Brezis" else "ocr",
        page_range=f"{args.first}-{args.last}",
    )
    got = [page.page_idx + 1 for page in result.pages]
    expected = list(range(args.first, args.last + 1))
    if got != expected:
        raise RuntimeError(f"page mismatch: expected {expected}, got {got}")
    result.save(FileBasedDataWriter(str(out)))
    marker.write_text(
        json.dumps({"book": args.book, "pages": got, "seconds": round(time.perf_counter() - started, 2)}, indent=2),
        encoding="utf-8",
    )
    print(marker.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
