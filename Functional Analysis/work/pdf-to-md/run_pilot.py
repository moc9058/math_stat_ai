"""Resumable 12-page-per-book OCR pilot with one local OCR worker."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SAMPLES = {
    "Brezis": [1, 8, 12, 16, 21, 45, 103, 195, 215, 277, 308, 339],
    "Conway": [1, 16, 21, 50, 90, 100, 150, 209, 250, 300, 350, 416],
}


def main() -> None:
    for book, pages in SAMPLES.items():
        for page in pages:
            marker = HERE / "chunks" / book.lower() / f"p{page:04}-p{page:04}" / "complete.json"
            if marker.exists():
                print(f"skip {book} {page}: complete", flush=True)
                continue
            print(f"start {book} {page}", flush=True)
            result = subprocess.run([sys.executable, str(HERE / "convert_chunk.py"), book, str(page), str(page)], cwd=HERE)
            if result.returncode:
                print(f"failed {book} {page}: exit {result.returncode}", flush=True)
                raise SystemExit(result.returncode)
    summary = {book: [json.loads((HERE / "chunks" / book.lower() / f"p{p:04}-p{p:04}" / "complete.json").read_text(encoding="utf-8")) for p in pages] for book, pages in SAMPLES.items()}
    (HERE / "pilot" / "checkpoint-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print("pilot_complete=24", flush=True)


if __name__ == "__main__":
    main()
