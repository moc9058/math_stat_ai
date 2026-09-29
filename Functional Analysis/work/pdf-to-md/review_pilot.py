"""Run bounded page-image review calls for completed OCR pilot pages."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from run_pilot import HERE, SAMPLES


def main() -> None:
    for book, pages in SAMPLES.items():
        for page in pages:
            out = HERE / "pilot" / f"{book.lower()}-p{page:03}-gpt-6-luna-review.json"
            if out.exists():
                print(f"skip {book} {page}: reviewed", flush=True)
                continue
            print(f"review {book} {page}", flush=True)
            code = subprocess.run([sys.executable, str(HERE / "review_page.py"), book, str(page), "--model", "gpt-6-luna"], cwd=HERE).returncode
            if code:
                raise SystemExit(code)
    print("luna_reviews_complete=24", flush=True)


if __name__ == "__main__":
    main()
