# Conway — Background-Enriched Study Edition

This English-language study edition preserves the original chapter files,
mathematical text, theorem numbers, exercises, page anchors, and illustrations,
and adds prerequisite explanations and proofs near their points of use.
The unchanged source edition is in
[1. Conway_original](<../1. Conway_original/README.md>).

It is tailored to the [learner background profile](../../../LEARNER_BACKGROUND.md):
linear algebra is assumed, real analysis and topology are refreshed, and complex
analysis is introduced without assuming previous study of the subject.

## How to read this edition

Continue through the chapters in the original order. Read each inserted
background block before the original argument that follows it. For longer
shared prerequisites, follow the links to the
[complex-analysis supplement](background-complex-analysis.md) and the appendices.
The [background index and reading guide](background-index.md) lists the added
results by chapter and gives a suggested route through the prerequisites.

Original results retain identifiers such as **1.1** or **VII.3.6**. Added
results use **BG-I.1**, **BG-II.1**, and so forth, with a separate sequence in
each chapter; appendices use **BG-A.1**, **BG-B.1**, and **BG-C.1**.
The unified complex-analysis supplement includes its real-analysis and topology
prerequisites and uses **CA.1–CA.68** in reading order. Its nine internal
chapters follow Brown–Churchill, *Complex Variables and Applications*
(eighth edition); two appendices provide prerequisite refreshers and
the additional tools needed for Conway.
Each definition, theorem, lemma, proposition, corollary, or example is labeled
as added material. HTML comments delimit the inserted blocks for preservation
checks; these comments do not interrupt normal Markdown rendering.

The background additions focus on prerequisites and omitted transitions, not
on replacing the book with a fully axiomatic development. Detailed exercise
solutions are being added separately, chapter by chapter, as described below.
Definitions and explicitly identified foundational inputs are
distinguished from results proved in the additions. Apparent source errors are
left in the original text; explanatory qualifications, where provided, are
clearly separated from that text.

## Exercise solutions

Detailed English solutions are appended under `Exercise Solutions` at the end
of each completed chapter, including proofs and prerequisite explanations.
Identifiers such as `Solution I.3.4` mean Chapter I, §3, Exercise 4; they do not
change the original exercise or theorem numbering. These are newly authored
study solutions, not an official solutions manual or part of the source text.

- [Chapter I solutions](chapter-01.md#exercise-solutions): all 54 numbered
  exercises, including their lettered subparts, have written solutions.
- [Chapter II solutions](chapter-02.md#exercise-solutions): all 97 numbered
  exercises, including the 17 exercises in §7 and their lettered subparts,
  have written responses with detailed proofs. Where an assertion as
  transcribed is false or needs qualification, the response supplies a
  correction, counterexample, or explicit additional hypothesis instead.
- [Chapter III solutions](chapter-03.md#exercise-solutions): all 102 numbered
  exercises, including lettered subparts, have written solutions or explicit
  corrections where the printed assumptions do not suffice.
- [Chapter IV solutions](chapter-04.md#exercise-solutions): all 71 numbered
  exercises, including lettered subparts, have written solutions or explicit
  counterexamples and corrected formulations.
- [Chapter V solutions](chapter-05.md#exercise-solutions): 77 numbered exercises.
- [Chapter VI solutions](chapter-06.md#exercise-solutions): 48 numbered exercises.
- [Chapter VII solutions](chapter-07.md#exercise-solutions): 101 numbered exercises.
- [Chapter VIII solutions](chapter-08.md#exercise-solutions): 54 numbered exercises.
- [Chapter IX solutions](chapter-09.md#exercise-solutions): 127 numbered exercises.
- Chapters X–XI: 103 exercises remain outside the requested scope. Work stops
  after Chapter IX; continue only on a new user request.

The revised inventory recognizes both Markdown headings and bold/plain
exercise headings, as well as repeated section headings across page breaks.
It currently records 834 numbered exercises across the eleven chapters;
lettered subparts are not counted separately. The first nine
chapters cover 731 of these numbered exercises; 103 remain in Chapters X–XI.

The [exercise-solution checkpoint](review/exercise-solutions-checkpoint.json)
records current exercise/solution counts and validation results. Matching
counts check coverage of numbered problems, not the correctness or completeness
of every argument; mathematical content must be assessed separately.

### Resume checkpoint — 2026-10-04

The requested scope is complete through Chapter IX. The latest work appended
407 responses (V: 77; VI: 48; VII: 101; VIII: 54; IX: 127), in English, inside
`BEGIN SOLUTIONS` / `END SOLUTIONS` markers. Chapters X and XI are unchanged.
Resume, only when requested, at Chapter X §1 Exercise 1.

Responses distinguish proofs from corrections to false or insufficiently
qualified assertions. Examples include the Haar-measure convention in VII.1.4,
the Banach-space adjoint issue in VII.6.2, the nonseparable eigenvalue issue in
IX.2.11, and the restricted pushforward measures in IX.10.14. IX.1.3 explicitly
identifies a positive-cone symbol mistranscribed in the exercise, checked
against PDF page 276. The original exercise text is preserved.

Some responses explicitly use additional foundational results rather than
reprove them: VII.2.8 uses Wichmann's bounded local-unit theorem, and VII.6.2
uses the noncomplementability of c0 in l-infinity for its counterexample.
VIII.5.7 points forward to the closed-ideal theorem in Chapter IX. These are
stated dependencies, not claims of fully self-contained proofs.

Validation confirms exact ordered exercise/solution identifiers for V–IX,
local links, markers, and mathematical delimiters. Removing the new solution
blocks recovers the existing Git version of each of these five chapters
exactly. The full-edition validator still reports preexisting source-text
preservation differences in all eleven chapters. The existing regression
suite likewise fails its two Chapter I/II preservation subtests because of
preexisting source/list indentation differences. No new structural problem
was found. The checkpoint records these limitations; structural checks do
not formally verify the mathematical proofs. The older
`background-validation.json` is not refreshed by this checkpoint.

## Contents

- [Front matter](front-matter.md)
- [I. Hilbert Spaces](chapter-01.md)
- [II. Operators on Hilbert Space](chapter-02.md)
- [III. Banach Spaces](chapter-03.md)
- [IV. Locally Convex Spaces](chapter-04.md)
- [V. Weak Topologies](chapter-05.md)
- [VI. Linear Operators on a Banach Space](chapter-06.md)
- [VII. Banach Algebras and Spectral Theory for Operators on a Banach Space](chapter-07.md)
- [VIII. C*-Algebras](chapter-08.md)
- [IX. Normal Operators on Hilbert Space](chapter-09.md)
- [X. Unbounded Operators](chapter-10.md)
- [XI. Fredholm Theory](chapter-11.md)
- [Appendix A. Preliminaries](appendix-a.md)
- [Appendix B. The Dual of l1](appendix-b.md)
- [Appendix C. The Dual of C0(X)](appendix-c.md)
- [Bibliography](bibliography.md)
- [Index](index.md)

## Supplements

- [Complex analysis: definitions, theorems, and proofs](background-complex-analysis.md)
- [Background index and reading guide](background-index.md)
- [Reusable learner background](../../../LEARNER_BACKGROUND.md)

## Provenance and validation

The source transcription underwent AI review and comparison with the original
PDF images. The inherited [page manifest](review/page-manifest.csv) and
[source validation results](review/validation.json) concern that transcription,
not the newly written background explanations or exercise solutions. The inherited visual-review
records remain unchanged.

The [study-edition validation report](review/background-validation.json) separately
checks that removing the marked additions recovers the original chapter and
appendix text exactly, all 416 original PDF page anchors remain, inherited
assets are unchanged, added background numbers are sequential, written solution
numbers match the original exercise lists, local links resolve, and the added
math delimiters are balanced. These are structural checks, not a
formal verification of mathematical correctness or a new PDF-image review.

To rerun the read-only check from the repository root using the existing
uv-managed virtual environment:

```bash
"Functional Analysis/work/pdf-to-md/.venv/bin/python" "Functional Analysis/work/pdf-to-md/validate_conway_study.py"
```

Exercise-inventory regression tests (including bold exercise headings and
repeated section headings across page breaks) can be run with:

```bash
"Functional Analysis/work/pdf-to-md/.venv/bin/python" "Functional Analysis/work/pdf-to-md/test_validate_conway_study.py"
```
