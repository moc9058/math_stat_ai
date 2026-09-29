"""Assemble page-preserving OCR drafts into book sections with traceable assets."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOK_ROOT = HERE.parents[1]
TOTAL = {"Brezis": 614, "Conway": 416}
CONWAY_SECTIONS = [
    (1, "front-matter", "Front matter"),
    (16, "chapter-01", "I. Hilbert Spaces"),
    (41, "chapter-02", "II. Operators on Hilbert Space"),
    (78, "chapter-03", "III. Banach Spaces"),
    (114, "chapter-04", "IV. Locally Convex Spaces"),
    (139, "chapter-05", "V. Weak Topologies"),
    (181, "chapter-06", "VI. Linear Operators on a Banach Space"),
    (202, "chapter-07", "VII. Banach Algebras and Spectral Theory for Operators on a Banach Space"),
    (247, "chapter-08", "VIII. C*-Algebras"),
    (270, "chapter-09", "IX. Normal Operators on Hilbert Space"),
    (318, "chapter-10", "X. Unbounded Operators"),
    (362, "chapter-11", "XI. Fredholm Theory"),
    (384, "appendix-a", "Appendix A. Preliminaries"),
    (390, "appendix-b", "Appendix B. The Dual of l1"),
    (393, "appendix-c", "Appendix C. The Dual of C0(X)"),
    (399, "bibliography", "Bibliography"),
    (409, "index", "Index"),
]


def sections(book: str) -> list[tuple[int, str, str]]:
    if book == "Conway":
        return CONWAY_SECTIONS
    toc = json.loads((HERE / "inventory/brezis-pdf-toc.json").read_text(encoding="utf-8"))
    result: list[tuple[int, str, str]] = []
    chapter = 0
    for level, title, page in toc:
        if level != 1:
            continue
        match = re.match(r"^(\d+)\.\s", title)
        if match:
            chapter = int(match.group(1))
            slug = f"chapter-{chapter:02}"
        elif title == "Cover":
            slug = "front-matter"
        elif page < 16:
            continue
        else:
            slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        if result and result[-1][0] == page:
            result[-1] = (page, slug, title)
        else:
            result.append((page, slug, title))
    return result


def source_pages(book: str) -> dict[int, tuple[Path, Path]]:
    candidates: dict[int, tuple[Path, Path]] = {}
    for chunk in sorted((HERE / "chunks" / book.lower()).glob("p*-p*")):
        if not (chunk / "complete.json").exists():
            continue
        for page in chunk.glob("page-*.md"):
            number = int(page.stem.split("-")[-1])
            old = candidates.get(number)
            if old is None or len(list(chunk.glob("page-*.md"))) > len(list(old[1].glob("page-*.md"))):
                candidates[number] = (page, chunk)
    return candidates


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("book", choices=TOTAL)
    cli.add_argument("--allow-partial", action="store_true")
    args = cli.parse_args()
    pages = source_pages(args.book)
    missing = sorted(set(range(1, TOTAL[args.book] + 1)) - set(pages))
    if missing and not args.allow_partial:
        raise SystemExit(f"missing {len(missing)} OCR pages; first: {missing[:12]}")
    destination = BOOK_ROOT / "md" / args.book
    destination.mkdir(parents=True, exist_ok=True)
    assets = destination / "assets"
    assets.mkdir(exist_ok=True)
    boundaries = sections(args.book)
    manifest = []
    for idx, (start, slug, title) in enumerate(boundaries):
        end = boundaries[idx + 1][0] - 1 if idx + 1 < len(boundaries) else TOTAL[args.book]
        sections_text = [f"# {title}\n", "<!-- OCR draft; page images require independent visual review. -->\n"]
        for number in range(start, end + 1):
            if number not in pages:
                if args.allow_partial:
                    continue
                raise AssertionError(number)
            page_path, chunk = pages[number]
            ocr_body = page_path.read_text(encoding="utf-8")
            status_path = HERE / "api" / args.book.lower() / f"{args.book.lower()}-p{number:04}-status.json"
            status = json.loads(status_path.read_text(encoding="utf-8")) if status_path.exists() else None
            transcript = HERE / "api" / args.book.lower() / f"{args.book.lower()}-p{number:04}-gpt-6-sol-transcription.md"
            repair = HERE / "api" / args.book.lower() / f"{args.book.lower()}-p{number:04}-gpt-6-astra-repair.md"
            if repair.exists() and status and status["status"] in ("ai_repair_passed", "reviewer_issue_resolved"):
                transcript = repair
            body = transcript.read_text(encoding="utf-8") if transcript.exists() else ocr_body
            lines = body.splitlines()
            if lines and len(lines[0]) < 160 and re.search(r"\s{8,}\d{1,3}\s*$", lines[0]):
                body = "\n".join(lines[1:]).lstrip()
            image_links = []
            for match in re.finditer(r"images/([^\s)]+)", ocr_body):
                name = match.group(1)
                original = chunk / "images" / name
                target_name = f"p{number:04}-{name}"
                if original.exists():
                    shutil.copy2(original, assets / target_name)
                    image_links.append(f"![](assets/{target_name})")
                    body = body.replace("images/" + name, "assets/" + target_name)
            if transcript.exists() and image_links:
                for link in image_links:
                    body, replaced = re.subn(r"\[FIGURE:[^\]]*\]", link, body, count=1)
                    if not replaced:
                        body += "\n\n" + link
            sections_text.append(f"\n<a id=\"pdf-page-{number}\"></a>\n" + body + "\n")
            manifest.append({"book": args.book, "pdf_page": number, "section": slug,
                             "source_page": str(page_path.relative_to(HERE)),
                             "output_md": f"{slug}.md",
                             "status": status["status"] if status else "unreviewed_ocr_draft"})
        (destination / f"{slug}.md").write_text("\n".join(sections_text), encoding="utf-8")
    review = destination / "review"
    review.mkdir(exist_ok=True)
    with (review / "page-manifest.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(manifest[0]) if manifest else
                                ["book", "pdf_page", "section", "source_page", "output_md", "status"])
        writer.writeheader()
        writer.writerows(sorted(manifest, key=lambda row: row["pdf_page"]))
    links = [f"- [{title}]({slug}.md)" for _, slug, title in boundaries]
    coverage = f"Partial assembly: {len(manifest)} of {TOTAL[args.book]} PDF pages are present.\n\n" if missing else "All PDF pages are present.\n\n"
    (destination / "README.md").write_text(
        f"# {args.book}\n\n{coverage}OCR draft. Every page still requires image-based visual review; "
        f"see [page manifest](review/page-manifest.csv).\n\n" + "\n".join(links) + "\n",
        encoding="utf-8",
    )
    print(f"book={args.book} assembled_pages={len(manifest)} missing={len(missing)} sections={len(boundaries)}")


if __name__ == "__main__":
    main()
