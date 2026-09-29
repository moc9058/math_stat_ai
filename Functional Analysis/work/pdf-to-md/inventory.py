"""Inventory every source PDF page without claiming OCR or transcription accuracy."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import pymupdf


HERE = Path(__file__).resolve().parent
BOOK_ROOT = HERE.parents[1]
SOURCE = BOOK_ROOT / "source"
OUTPUT = HERE / "inventory"


def page_kind(page: pymupdf.Page) -> tuple[str, int, int, int]:
    text = page.get_text("text")
    words = len(page.get_text("words"))
    image_info = page.get_image_info()
    images = len(image_info)
    drawings = len(page.get_drawings())
    page_area = page.rect.width * page.rect.height
    full_page_scan = any(
        pymupdf.Rect(image["bbox"]).intersect(page.rect).get_area() > 0.8 * page_area
        for image in image_info
    )
    if full_page_scan:
        kind = "scan_with_ocr_layer" if words >= 10 else "scan_without_ocr_layer"
    elif words < 10:
        kind = "image_or_sparse"
    elif words < 80:
        kind = "mixed_or_sparse"
    else:
        kind = "text_with_possible_math"
    return kind, words, images, drawings


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    summary = {}
    for book in ("Brezis", "Conway"):
        path = SOURCE / f"{book}.pdf"
        sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
        rows = []
        with pymupdf.open(path) as doc:
            toc = doc.get_toc(simple=True)
            for i, page in enumerate(doc):
                kind, words, images, drawings = page_kind(page)
                rows.append({
                    "book": book,
                    "pdf_page": i + 1,
                    "printed_page": "",
                    "chapter": "",
                    "section": "",
                    "kind": kind,
                    "words": words,
                    "embedded_images": images,
                    "drawings": drawings,
                    "status": "unprocessed",
                    "output_md": "",
                    "review_notes": "",
                })
            summary[book] = {
                "pages": len(doc),
                "sha256": sha256,
                "pdf_toc_entries": len(toc),
                "kind_counts": {kind: sum(r["kind"] == kind for r in rows) for kind in sorted({r["kind"] for r in rows})},
            }
            (OUTPUT / f"{book.lower()}-pdf-toc.json").write_text(
                json.dumps(toc, ensure_ascii=False, indent=2), encoding="utf-8"
            )
        with (OUTPUT / f"{book.lower()}-pages.csv").open("w", newline="", encoding="utf-8-sig") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    (OUTPUT / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
