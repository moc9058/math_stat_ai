"""Summarize model-review findings; malformed JSON remains visible as an issue."""

from __future__ import annotations

import json

from run_pilot import HERE, SAMPLES


def main() -> None:
    rows = []
    for book, pages in SAMPLES.items():
        for page in pages:
            path = HERE / "pilot" / f"{book.lower()}-p{page:03}-gpt-6-luna-review.json"
            outer = json.loads(path.read_text(encoding="utf-8"))
            try:
                inner = json.loads(outer["review"])
            except json.JSONDecodeError:
                inner = None
            rows.append({
                "book": book,
                "pdf_page": page,
                "valid_review_json": inner is not None,
                "safe_to_accept": inner.get("safe_to_accept") if inner else None,
                "error_count": len(inner.get("errors", [])) if inner else None,
                "uncertain_regions": len(inner.get("uncertain_regions", [])) if inner else None,
            })
    summary = {
        "pages": len(rows),
        "valid_review_json": sum(x["valid_review_json"] for x in rows),
        "safe_to_accept_true": sum(x["safe_to_accept"] is True for x in rows),
        "explicit_errors": sum(x["error_count"] or 0 for x in rows),
        "rows": rows,
    }
    (HERE / "pilot" / "review-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
