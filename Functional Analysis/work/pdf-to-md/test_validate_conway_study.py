"""Regression checks for exercise discovery and the marked study additions.

Run with the adjacent uv-managed .venv/bin/python. Standard library only.
These checks do not certify the mathematical proofs.
"""

import re
import unittest
from collections import Counter

from validate_conway_study import BLOCK, ORIGINAL, SOLUTIONS, STUDY, exercise_ids


class ExerciseInventoryTests(unittest.TestCase):
    def test_heading_formats_and_repeated_section_header(self):
        source = """## §1. First section
**Exercise 11.** An inline reference, not a list heading.
1. This is not an exercise.
**Exercises**
1. First exercise.
   (a) A subpart, not another numbered exercise.
## §1. First section
2. Continued after a repeated running heading.
## §2*. Second section
1. Not yet in its exercises.
## EXERCISES
1. Another exercise.
# §3. Third section
Exercises
1. A plain-heading exercise.
"""
        self.assertEqual(exercise_ids(source, "II"),
                         ["II.1.1", "II.1.2", "II.2.1", "II.3.1"])

    def test_chapter_two_includes_bold_section_seven(self):
        ids = exercise_ids((ORIGINAL / "chapter-02.md").read_text(), "II")
        counts = Counter(identifier.split(".")[1] for identifier in ids)
        self.assertEqual(dict(counts),
                         {"1": 13, "2": 16, "3": 12, "4": 14,
                          "5": 5, "6": 6, "7": 17, "8": 14})
        self.assertEqual(len(ids), 97)
        self.assertEqual(len(set(ids)), 97)

    def test_all_source_lists_are_sequential(self):
        chapters = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]
        expected_counts = [54, 97, 102, 71, 77, 48, 101, 54, 127, 62, 41]
        for number, (chapter, count) in enumerate(zip(chapters, expected_counts), 1):
            with self.subTest(chapter=chapter):
                ids = exercise_ids((ORIGINAL / f"chapter-{number:02}.md").read_text(), chapter)
                self.assertEqual(len(ids), count)
                self.assertEqual(len(set(ids)), count)
                sections = {}
                for identifier in ids:
                    _, section, exercise = identifier.split(".")
                    sections.setdefault(section, []).append(int(exercise))
                for numbers in sections.values():
                    self.assertEqual(numbers, list(range(1, len(numbers) + 1)))

    def test_written_chapters_preserve_source_and_cover_lists(self):
        for number, chapter in [(1, "I"), (2, "II")]:
            with self.subTest(chapter=chapter):
                name = f"chapter-{number:02}.md"
                original = (ORIGINAL / name).read_text()
                study = (STUDY / name).read_text()
                blocks = list(SOLUTIONS.finditer(study))
                self.assertEqual(len(blocks), 1)
                self.assertEqual(blocks[0].group(1), chapter)
                self.assertEqual(study[blocks[0].end():].strip(), "")
                self.assertEqual(SOLUTIONS.sub("", BLOCK.sub("", study)), original)
                actual = re.findall(r"^#### Solution ([IVX]+\.\d+\.\d+)\b",
                                    blocks[0].group(2), re.M)
                self.assertEqual(actual, exercise_ids(original, chapter))


if __name__ == "__main__":
    unittest.main()
