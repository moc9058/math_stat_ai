"""Read-only structural validation of Conway's background-enriched edition.

Run with this directory's uv-managed .venv/bin/python. No third-party packages.
This checks preservation and syntax, not the truth of mathematical proofs.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
MD = HERE.parents[1] / "md"
ORIGINAL = MD / "1. Conway_original"
STUDY = MD / "2. Conway_added_background"
BLOCK = re.compile(
    r"<!-- BEGIN BACKGROUND ([\w.-]+) -->\n(.*?)"
    r"<!-- END BACKGROUND \1 -->(?:\n\n|\n?$)",
    re.DOTALL,
)
NUMBER = re.compile(r"^### [^\n]*?\b((?:BG-[IVXABC]+|CA)\.(\d+))\b", re.MULTILINE)
SOLUTIONS = re.compile(
    r"<!-- BEGIN SOLUTIONS ([IVX]+) -->\n(.*?)"
    r"<!-- END SOLUTIONS \1 -->\n?", re.DOTALL,
)


def exercise_ids(text: str, chapter: str) -> list[str]:
    """Read numbered exercises within each original section's exercise list."""
    section = None
    in_exercises = False
    result = []
    for line in text.splitlines():
        heading = re.match(r"^#{1,3}\s+§(\d+)\b", line)
        if heading and heading.group(1) != section:
            section = heading.group(1)
            in_exercises = False
        # Some source pages use bold or plain text instead of an ATX heading.
        # Do not match inline references such as "**Exercise 11.**".
        if re.match(r"^\s*(?:#{1,6}\s+)?(?:\*\*)?EXERCISES(?:\*\*)?\s*$", line, re.I):
            in_exercises = True
        numbered = re.match(r"^(\d+)\.\s", line)
        if in_exercises and numbered and section:
            result.append(f"{chapter}.{section}.{numbered.group(1)}")
    return result


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def anchors(text: str) -> set[str]:
    found = set(re.findall(r'<a\s+id="([^"]+)"', text))
    counts: Counter[str] = Counter()
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE):
        heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        suffix = counts[slug]
        counts[slug] += 1
        found.add(slug if suffix == 0 else f"{slug}-{suffix}")
    return found


def main() -> None:
    problems: list[dict] = []
    coverage: list[dict] = []
    source_hashes: dict[str, str] = {}
    page_numbers: list[int] = []
    all_identifiers: list[str] = []
    all_blocks: list[str] = []
    solution_coverage: list[dict] = []
    source_files = sorted(ORIGINAL.rglob("*"))

    for source in source_files:
        if not source.is_file():
            continue
        relative = source.relative_to(ORIGINAL)
        key = relative.as_posix()
        data = source.read_bytes()
        source_hashes[key] = sha(data)
        target = STUDY / relative
        if not target.is_file():
            problems.append({"kind": "missing_source_file", "file": key})
            continue
        if relative == Path("README.md"):
            continue  # The study edition intentionally has a distinct README.
        if source.suffix != ".md":
            if data != target.read_bytes():
                problems.append({"kind": "changed_inherited_asset_or_review", "file": key})
            continue
        original_text = data.decode("utf-8")
        study_text = target.read_text(encoding="utf-8")
        blocks = list(BLOCK.finditer(study_text))
        stripped = SOLUTIONS.sub("", BLOCK.sub("", study_text))
        if stripped != original_text:
            problems.append({"kind": "source_text_not_exactly_preserved", "file": key})
        if "<!-- BEGIN BACKGROUND" in stripped or "<!-- END BACKGROUND" in stripped:
            problems.append({"kind": "unmatched_background_marker", "file": key})
        if "<!-- BEGIN SOLUTIONS" in stripped or "<!-- END SOLUTIONS" in stripped:
            problems.append({"kind": "unmatched_solution_marker", "file": key})
        if key.startswith("chapter-"):
            chapter = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"][int(key[8:10]) - 1]
            expected = exercise_ids(original_text, chapter)
            solution_blocks = list(SOLUTIONS.finditer(study_text))
            actual = re.findall(r"^#### Solution ([IVX]+\.\d+\.\d+)\b", study_text, re.M)
            if solution_blocks:
                if len(solution_blocks) != 1 or solution_blocks[0].group(1) != chapter:
                    problems.append({"kind": "incorrect_solution_block", "file": key})
                if study_text[solution_blocks[-1].end():].strip():
                    problems.append({"kind": "solutions_not_at_chapter_end", "file": key})
                if actual != expected:
                    problems.append({"kind": "solution_numbering_or_coverage", "file": key,
                                     "expected": expected, "actual": actual})
            elif actual:
                problems.append({"kind": "unmarked_solutions", "file": key})
            solution_coverage.append({"file": key, "exercise_count": len(expected),
                                      "solution_count": len(actual),
                                      "status": "written" if solution_blocks and actual == expected else "not_yet_written",
                                      "solution_identifiers": actual})
        original_pages = re.findall(r'<a id="pdf-page-(\d+)"></a>', original_text)
        study_pages = re.findall(r'<a id="pdf-page-(\d+)"></a>', study_text)
        if study_pages != original_pages:
            problems.append({"kind": "changed_page_anchor_order", "file": key})
        page_numbers.extend(map(int, study_pages))
        added = "\n".join(m.group(2) for m in blocks)
        ids = [m.group(1) for m in NUMBER.finditer(added)]
        all_identifiers.extend(ids)
        all_blocks.extend(m.group(1) for m in blocks)
        if key.startswith(("chapter-", "appendix-")):
            if not blocks or not ids:
                problems.append({"kind": "missing_background", "file": key})
            numbers = [int(i.rsplit(".", 1)[1]) for i in ids]
            if numbers != list(range(1, len(numbers) + 1)):
                problems.append({"kind": "nonsequential_numbering", "file": key, "numbers": numbers})
            coverage.append({"file": key, "blocks": len(blocks), "numbered_items": len(ids),
                             "added_words": len(added.split()), "identifiers": ids})

    if sorted(page_numbers) != list(range(1, 417)):
        problems.append({"kind": "page_coverage", "count": len(page_numbers)})

    for path in sorted(STUDY.glob("*.md")):
        body = path.read_text(encoding="utf-8")
        relative = path.name
        explicit = re.findall(r'<a\s+id="([^"]+)"', body)
        for anchor, count in Counter(explicit).items():
            if count > 1:
                problems.append({"kind": "duplicate_anchor", "file": relative, "anchor": anchor})
        if "background-complex-prerequisites.md" in body or re.search(r"\bCP\.\d+", body):
            problems.append({"kind": "obsolete_split_supplement_reference", "file": relative})
        if path.name == "background-complex-analysis.md":
            ids = [m.group(1) for m in NUMBER.finditer(body)]
            all_identifiers.extend(ids)
            if ids != [f"CA.{n}" for n in range(1, len(ids) + 1)]:
                problems.append({"kind": "complex_numbering"})
            for identifier in ids:
                expected = identifier.lower().replace(".", "-")
                if expected not in explicit:
                    problems.append({"kind": "missing_numbered_anchor", "identifier": identifier})
            coverage.append({"file": relative, "blocks": 0, "numbered_items": len(ids),
                             "added_words": len(body.split()), "identifiers": ids})

        # Scan only new prose for math/English checks; existing transcription is preserved.
        pieces = [m.group(2) for m in BLOCK.finditer(body)]
        pieces.extend(m.group(2) for m in SOLUTIONS.finditer(body))
        if not (ORIGINAL / path.name).exists() or path.name == "README.md":
            pieces = [body]
        for n, piece in enumerate(pieces, 1):
            if re.search(r"[\uac00-\ud7af]", piece):
                problems.append({"kind": "non_english_added_prose", "file": relative, "block": n})
            if len(re.findall(r"(?<!\\)\$", piece)) % 2:
                problems.append({"kind": "unbalanced_math_dollars", "file": relative, "block": n})
            envs: list[str] = []
            for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", piece):
                direction, env = match.groups()
                if direction == "begin":
                    envs.append(env)
                elif not envs or envs.pop() != env:
                    problems.append({"kind": "math_environment_mismatch", "file": relative, "block": n})
            if envs:
                problems.append({"kind": "unclosed_math_environment", "file": relative, "block": n})
            if re.search(r"\b(?:TODO|TBD|FIXME)\b", piece):
                problems.append({"kind": "unfinished_marker", "file": relative, "block": n})

        for raw in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", body):
            target = unquote(raw.strip().strip("<>"))
            if target.startswith(("https://", "http://", "data:", "mailto:")):
                continue
            if not target.startswith("#") and not re.search(r"\.(?:md|png|jpg|jpeg|json|csv|pdf)(?:#|$)", target, re.I):
                continue  # Avoid treating a mathematical expression as a link.
            name, _, fragment = target.partition("#")
            linked = (path.parent / name).resolve() if name else path
            if not linked.is_file():
                problems.append({"kind": "broken_local_link", "file": relative, "target": raw})
            elif fragment and linked.suffix == ".md":
                if fragment not in anchors(linked.read_text(encoding="utf-8")):
                    problems.append({"kind": "broken_fragment", "file": relative, "target": raw})

    for kind, values in (("duplicate_number", all_identifiers), ("duplicate_block", all_blocks)):
        for value, count in Counter(values).items():
            if count != 1:
                problems.append({"kind": kind, "identifier": value, "count": count})

    known = set(all_identifiers)
    for path in sorted(STUDY.glob("*.md")):
        for identifier in set(re.findall(r"\bCA\.\d+\b", path.read_text(encoding="utf-8"))):
            if identifier not in known:
                problems.append({"kind": "unknown_complex_result", "file": path.name, "identifier": identifier})

    profile = REPO / "LEARNER_BACKGROUND.md"
    if not profile.is_file():
        problems.append({"kind": "missing_learner_profile"})
    report = {
        "edition": "Conway_added_background",
        "validation_scope": "Structural checks only; not a formal proof verification or new PDF-image review.",
        "source_directory": ORIGINAL.relative_to(REPO).as_posix(),
        "source_files_preserved_except_readme": len(source_hashes) - 1,
        "original_pdf_page_anchors": len(page_numbers),
        "numbered_background_items": len(all_identifiers),
        "coverage": coverage,
        "exercise_solution_coverage": solution_coverage,
        "source_sha256": source_hashes,
        "problems": problems,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    raise SystemExit(bool(problems))


if __name__ == "__main__":
    main()
