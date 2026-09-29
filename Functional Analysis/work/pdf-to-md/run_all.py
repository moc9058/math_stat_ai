"""Resumable single-worker OCR over a complete book in bounded chunks."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
TOTAL = {"Brezis": 614, "Conway": 416}


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("book", choices=TOTAL)
    cli.add_argument("--chunk-size", type=int, default=8)
    args = cli.parse_args()
    if args.chunk_size < 1 or args.chunk_size > 32:
        cli.error("chunk size must be 1..32")
    for first in range(1, TOTAL[args.book] + 1, args.chunk_size):
        last = min(first + args.chunk_size - 1, TOTAL[args.book])
        marker = HERE / "chunks" / args.book.lower() / f"p{first:04}-p{last:04}" / "complete.json"
        if marker.exists():
            print(f"skip {args.book} {first}-{last}", flush=True)
            continue
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
