"""Aggregate recorded OpenAI API tokens and an explicitly estimated cost."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
# USD per million input/output tokens, checked against official model pages
# during the pilot on 2026-09-28. This is an estimate, not a billing record.
RATES = {"gpt-6-luna": (0.10, 0.50), "gpt-6-sol": (2.00, 10.00),
         "gpt-6-astra": (10.00, 50.00)}


def main() -> None:
    totals = defaultdict(lambda: {"calls": 0, "input_tokens": 0, "output_tokens": 0})
    for folder in (HERE / "pilot", HERE / "api"):
        if not folder.exists():
            continue
        for path in folder.rglob("*.json"):
            try:
                record = json.loads(path.read_text(encoding="utf-8"))
            except (ValueError, OSError):
                continue
            model = record.get("model") if isinstance(record, dict) else None
            if model not in RATES or "input_tokens" not in record or "output_tokens" not in record:
                continue
            book = record.get("book", "unknown")
            key = (book, model)
            totals[key]["calls"] += 1
            totals[key]["input_tokens"] += record["input_tokens"]
            totals[key]["output_tokens"] += record["output_tokens"]
    lines = ["# Recorded OpenAI API usage", "", "Estimates use published model rates checked 2026-09-28; actual billing may differ.", "",
             "| Book | Model | Calls | Input tokens | Output tokens | Estimated USD |",
             "| --- | --- | ---: | ---: | ---: | ---: |"]
    grand = 0.0
    for (book, model), entry in sorted(totals.items()):
        input_rate, output_rate = RATES[model]
        estimate = (entry["input_tokens"] * input_rate + entry["output_tokens"] * output_rate) / 1_000_000
        grand += estimate
        lines.append(f"| {book} | {model} | {entry['calls']} | {entry['input_tokens']:,} | {entry['output_tokens']:,} | ${estimate:.4f} |")
    lines += ["", f"**Total estimated API cost:** ${grand:.4f}", "",
              "Source: https://developers.openai.com/api/docs/models", ""]
    target = HERE / "api-usage-report.md"
    target.write_text("\n".join(lines), encoding="utf-8")
    print(f"calls={sum(v['calls'] for v in totals.values())} estimated_usd={grand:.4f}")


if __name__ == "__main__":
    main()
