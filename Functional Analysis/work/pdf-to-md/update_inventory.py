"""Add verified page mapping and conversion status to the original PDF inventory."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from assemble_book import HERE, TOTAL, sections


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("book", choices=TOTAL)
    args = cli.parse_args()
    book = args.book
    inventory_path = HERE / "inventory" / f"{book.lower()}-pages.csv"
    with inventory_path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    boundaries = sections(book)
    toc = json.loads((HERE / "inventory/brezis-pdf-toc.json").read_text(encoding="utf-8")) if book == "Brezis" else []
    section_boundaries = [(page, title) for level, title, page in toc if level == 2 and page >= 16]
    status_dir = HERE / "api" / book.lower()
    output_dir = HERE.parents[1] / "md" / book
    manifest_path = output_dir / "review/page-manifest.csv"
    manifest = {}
    if manifest_path.exists():
        with manifest_path.open(encoding="utf-8", newline="") as stream:
            manifest = {int(row["pdf_page"]): row for row in csv.DictReader(stream)}
    for row in rows:
        page = int(row["pdf_page"])
        if page >= 16:
            row["printed_page"] = str(page - 15)
        current_index = next((index for index in range(len(boundaries) - 1, -1, -1)
                              if boundaries[index][0] <= page), None)
        current = ((boundaries[current_index][1], boundaries[current_index][2])
                   if current_index is not None else ("", ""))
        chapter = current[1] if current[0].startswith("chapter-") else ""
        row["chapter"] = chapter
        if section_boundaries and chapter:
            chapter_start = boundaries[current_index][0]
            chapter_end = boundaries[current_index + 1][0] if current_index + 1 < len(boundaries) else TOTAL[book] + 1
            row["section"] = next((title for start, title in reversed(section_boundaries)
                                   if chapter_start <= start <= page and start < chapter_end), "")
        else:
            row["section"] = ""
        status_path = status_dir / f"{book.lower()}-p{page:04}-status.json"
        if status_path.exists():
            row["status"] = json.loads(status_path.read_text(encoding="utf-8"))["status"]
        elif page in manifest:
            row["status"] = manifest[page]["status"]
        if page in manifest:
            row["output_md"] = str(output_dir / manifest[page]["output_md"])
            row["review_notes"] = str(status_path) if status_path.exists() else ""
    with inventory_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"book={book} pages={len(rows)} mapped={len(manifest)}")


if __name__ == "__main__":
    main()
