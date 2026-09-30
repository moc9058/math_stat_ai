# Learner background and editorial preferences

Recorded from the learner's own description on 2026-09-30. This profile is
intended to be reused when preparing study editions of other mathematics books.
It is a statement of prior study, not a test of current proficiency.

## Prior knowledge

| Subject | Prior study and present familiarity | How to adapt a study edition |
| --- | --- | --- |
| Linear algebra | Reviewed last year; no additional explanation requested. | Assume standard linear algebra. Explain genuinely infinite-dimensional or analytic issues, not elementary matrix manipulations. |
| Real analysis | Studied Rudin's *Principles of Mathematical Analysis* and the real-analysis portions of *Real and Complex Analysis* about three to four years ago; much has been forgotten, but a reminder should be understandable. | Refresh definitions, hypotheses, convergence results, and proof mechanisms at their first use. Include proofs of added results. Do not confuse previous exposure with current recall. |
| Complex analysis | No previous course or systematic study. Only elementary complex numbers, as encountered in introductory/real analysis, are familiar. | Build the required theory from definitions. Supply detailed proofs and explicit dependencies for holomorphic functions, contour integrals, Cauchy theory, and applications, rather than citing these as familiar facts. |
| Topology | Basic concepts studied about three to four years ago; much has been forgotten. | Reintroduce topology, compactness, products, and continuity. Explain nets and nonmetrizable phenomena carefully; do not silently replace nets with sequences. |

## Persistent preferences for mathematical study editions

- Write all files in English, including explanations, proofs, navigation, and this profile.
- Preserve the source book's chapter-per-file organization and its mathematical text.
- Place prerequisite explanations before their use where practical, with links to shared material when repetition would be excessive.
- Label additions as definitions, lemmas, propositions, theorems, corollaries, or examples as appropriate, and give them unambiguous numbers.
- Keep the original numbering intact. Use a separate namespace for editorial additions so that original cross-references continue to work.
- State the hypotheses needed for limit exchanges, differentiations, compactness arguments, and integral identities; provide proofs, not just names of the results.
- For complex analysis, also explain the real-analysis and topology prerequisites needed to understand its proofs. Keep these prerequisites and the complex-analysis development together in one supplement, ordered from foundations to applications.
- In particular, distinguish pointwise, uniform, locally uniform, almost-everywhere, norm, weak, and strong convergence whenever they enter the argument.
- Do not present added explanations as text authored by the source book's author, or extend source-transcription review claims to newly written mathematics.
- For Conway, append an `Exercise Solutions` section to each chapter as it is completed. Write detailed proofs with necessary background explanations, proceed chapter by chapter, and identify solutions by chapter, section, and exercise number. Keep unfinished chapters explicitly distinguished from completed solution sets.
- Use a uv-managed virtual environment for any Python dependencies or validation scripts.

## Scope of reuse

This profile does not establish prior knowledge of other subjects, nor does it
authorize changes to other books. Update it when the learner reports new study
or different preferences; do not infer mastery merely from completing an edit.
