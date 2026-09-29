"""Check assembled book coverage, local links, and common Markdown math defects."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TOTAL = {"Brezis": 614, "Conway": 416}


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("book", choices=TOTAL)
    args = cli.parse_args()
    folder = ROOT / "md" / args.book
    manifest = list(csv.DictReader((folder / "review/page-manifest.csv").open(encoding="utf-8", newline="")))
    numbers = [int(row["pdf_page"]) for row in manifest]
    problems = []
    if numbers != list(range(1, TOTAL[args.book] + 1)):
        problems.append({"kind": "page_coverage", "missing": sorted(set(range(1, TOTAL[args.book] + 1)) - set(numbers)),
                         "duplicates": sorted({n for n in numbers if numbers.count(n) > 1})})
    seen_anchors = []
    for path in folder.glob("*.md"):
        body = path.read_text(encoding="utf-8")
        seen_anchors += [int(n) for n in re.findall(r'<a id="pdf-page-(\d+)"></a>', body)]
        for part in re.split(r'(?=<a id="pdf-page-\d+"></a>)', body):
            anchor = re.search(r'pdf-page-(\d+)', part)
            if not anchor:
                continue
            page = int(anchor.group(1))
            if len(re.findall(r'(?<!\\)\$', part)) % 2:
                problems.append({"kind": "unbalanced_dollar", "pdf_page": page})
            starts = re.findall(r'\\begin\{([^}]+)\}', part)
            ends = re.findall(r'\\end\{([^}]+)\}', part)
            if sorted(starts) != sorted(ends):
                problems.append({"kind": "latex_environment", "pdf_page": page,
                                 "begins": starts, "ends": ends})
        for target in re.findall(r'!?(?:\[[^\]]*\])\(([^)]+)\)', body):
            if target.startswith(("http://", "https://", "#", "data:")):
                continue
            if not any(char in target for char in ("/", ".", "#")):
                continue  # Math such as [U_y f](t) is not a Markdown file link.
            if not (path.parent / target.split("#", 1)[0]).exists():
                problems.append({"kind": "broken_link", "file": path.name, "target": target})
        if "[UNCLEAR:" in body:
            problems.append({"kind": "unclear_marker", "file": path.name,
                             "count": body.count("[UNCLEAR:")})
        if "[FIGURE:" in body:
            problems.append({"kind": "unlinked_figure", "file": path.name,
                             "count": body.count("[FIGURE:")})
    if sorted(seen_anchors) != list(range(1, TOTAL[args.book] + 1)):
        problems.append({"kind": "page_anchors", "count": len(seen_anchors)})
    statuses = {}
    for row in manifest:
        statuses[row["status"]] = statuses.get(row["status"], 0) + 1
    report = {"book": args.book, "expected_pages": TOTAL[args.book], "manifest_pages": len(manifest),
              "statuses": statuses, "problems": problems}
    target = folder / "review/validation.json"
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"book": args.book, "manifest_pages": len(manifest),
                      "statuses": statuses, "problem_count": len(problems)}, indent=2))


if __name__ == "__main__":
    main()
