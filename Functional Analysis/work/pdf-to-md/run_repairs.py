"""Run one bounded image-based repair and independent review for flagged pages."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def repair(book: str, number: int) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, "repair_page.py", book, str(number)],
                          cwd=HERE, capture_output=True, text=True)
    if proc.returncode:
        return number, "repair_failed: " + (proc.stdout + proc.stderr)[-400:].replace("\n", " ")
    status_path = HERE / "api" / book.lower() / f"{book.lower()}-p{number:04}-status.json"
    return number, json.loads(status_path.read_text(encoding="utf-8"))["status"]


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("book", choices=["Brezis", "Conway"])
    cli.add_argument("--workers", type=int, default=2)
    args = cli.parse_args()
    if not 1 <= args.workers <= 4:
        cli.error("workers must be 1..4")
    directory = HERE / "api" / args.book.lower()
    pages = []
    for status_path in directory.glob("*-status.json"):
        status = json.loads(status_path.read_text(encoding="utf-8"))
        if status["status"] == "needs_further_review":
            pages.append(status["pdf_page"])
    print(f"flagged={len(pages)}", flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for number, outcome in pool.map(lambda n: repair(args.book, n), sorted(pages)):
            print(f"page={number} status={outcome}", flush=True)


if __name__ == "__main__":
    main()
