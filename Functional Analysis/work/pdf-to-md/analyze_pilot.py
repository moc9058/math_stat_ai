"""Summarize pilot runtime, OCR structure, and API review without declaring accuracy."""

from __future__ import annotations

import csv
import json
import statistics
from pathlib import Path

from run_pilot import HERE, SAMPLES


def main() -> None:
    rows = []
    for book, pages in SAMPLES.items():
        for page in pages:
            chunk = HERE / "chunks" / book.lower() / f"p{page:04}-p{page:04}"
            marker = chunk / "complete.json"
            if not marker.exists():
                continue
            duration = json.loads(marker.read_text(encoding="utf-8"))["seconds"]
            middle = json.loads((chunk / "middle_json.json").read_text(encoding="utf-8"))
            blocks = middle["pages"][0].get("blocks", [])
            md = chunk / f"page-{page:04}.md"
            review = HERE / "pilot" / f"{book.lower()}-p{page:03}-gpt-6-luna-review.json"
            reviewed = json.loads(review.read_text(encoding="utf-8")) if review.exists() else None
            rows.append({
                "book": book,
                "pdf_page": page,
                "seconds": duration,
                "blocks": len(blocks),
                "equation_blocks": sum(b["type"] == "equation" for b in blocks),
                "image_blocks": sum(b["type"] == "image" for b in blocks),
                "markdown_chars": len(md.read_text(encoding="utf-8")) if md.exists() else "",
                "review_model": reviewed["model"] if reviewed else "",
                "review_input_tokens": reviewed["input_tokens"] if reviewed else "",
                "review_output_tokens": reviewed["output_tokens"] if reviewed else "",
                "review_status": "review_pending" if not reviewed else "model_reviewed_needs_visual_confirmation",
            })
    csv_path = HERE / "pilot" / "metrics.csv"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "completed_pages": len(rows),
        "per_book": {
            book: {
                "completed_pages": sum(r["book"] == book for r in rows),
                "median_seconds_per_page": round(statistics.median(r["seconds"] for r in rows if r["book"] == book), 1) if any(r["book"] == book for r in rows) else None,
            }
            for book in SAMPLES
        },
        "api_reviewed_pages": sum(bool(r["review_model"]) for r in rows),
        "api_input_tokens": sum(int(r["review_input_tokens"] or 0) for r in rows),
        "api_output_tokens": sum(int(r["review_output_tokens"] or 0) for r in rows),
    }
    (HERE / "pilot" / "metrics-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
