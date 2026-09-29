"""Write one unreviewed Markdown draft per completed OCR page."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

from mineru.parser import ParseResult


HERE = Path(__file__).resolve().parent


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("book", choices=["Brezis", "Conway"])
    args = cli.parse_args()
    source = HERE / "chunks" / args.book.lower()
    count = 0
    for chunk in sorted(source.glob("p*-p*")):
        if not (chunk / "complete.json").exists():
            continue
        data = json.loads((chunk / "middle_json.json").read_text(encoding="utf-8"))
        for page in data["pages"]:
            page_number = page["page_idx"] + 1
            single = copy.deepcopy(data)
            single["pages"] = [page]
            markdown = ParseResult.from_dict(single).markdown().strip()
            markdown = f"<!-- PDF page {page_number}; unreviewed OCR draft -->\n\n" + markdown + "\n"
            path = chunk / f"page-{page_number:04}.md"
            path.write_text(markdown, encoding="utf-8")
            count += 1
    print(f"book={args.book} materialized_pages={count}")


if __name__ == "__main__":
    main()
