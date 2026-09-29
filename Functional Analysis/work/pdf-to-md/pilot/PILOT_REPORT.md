# 24-page conversion pilot

The local MinerU basic pipeline processed 12 sampled PDF pages from each book. All
24 pages have bounded OCR checkpoints and one-page Markdown drafts. An independent
Luna image review was requested for every sampled page. Twenty-three review
responses were valid JSON; one (Brezis PDF page 308) requires a new review.

| Item | Brezis | Conway |
| --- | ---: | ---: |
| PDF pages | 614 | 416 |
| Sampled pages | 12 | 12 |
| Median local CPU OCR time per sampled page | 12.2 s | 63.1 s |

Across the 23 usable Luna reviews, the reviewer marked only seven pages safe to
accept and identified 86 explicit issues. These are model judgments, not completed
human visual verification. Conway's mathematical notation is the main weakness of
the local OCR draft. Sol image transcription of Conway PDF page 21 passed an
independent Astra review; the same procedure on page 209 still had one equation
symbol error. The paid transcription therefore also needs review.

The 24 Luna review calls used 68,897 input and 13,458 output tokens in total.
Using the published model rates at the time of this pilot, their estimated API
cost was about USD 0.014. API usage is recorded separately from local OCR and
Codex session usage. The full-book cost estimate must be revised after the
chosen correction and review workflow is measured on longer contiguous ranges.

The source PDFs remain intact. OCR drafts are stored in `chunks/` with
`complete.json` checkpoints and page numbers from the original PDFs. The next
gate is a CUDA backend test on the 6 GB RTX 3060; if incompatible or unstable,
the CPU checkpoint pipeline remains available.
