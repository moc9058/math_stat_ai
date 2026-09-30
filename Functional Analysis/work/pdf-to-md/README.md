# Functional analysis PDF conversion

Inputs are `../../source/Brezis.pdf` and `../../source/Conway.pdf`.
Book outputs are written to `../../md/Brezis/` and `../../md/Conway/`.
The repository root `.env` provides `OPENAI_API_KEY` for the API correction and
review pass; the key is excluded from Git.

From this directory in PowerShell:

```powershell
$env:UV_CACHE_DIR = (Join-Path (Get-Location) '.uv-cache')
$env:UV_PYTHON_INSTALL_DIR = (Join-Path (Get-Location) '.uv-python')
uv sync --locked --python 3.12
$env:MINERU_HOME = (Join-Path (Get-Location) '.mineru')
$env:HF_HOME = (Join-Path (Get-Location) '.huggingface')
& '.venv\Scripts\python.exe' inventory.py
& '.venv\Scripts\python.exe' run_all.py Conway --chunk-size 8
& '.venv\Scripts\python.exe' run_all.py Brezis --chunk-size 8
& '.venv\Scripts\python.exe' materialize_pages.py Conway
& '.venv\Scripts\python.exe' materialize_pages.py Brezis
& '.venv\Scripts\python.exe' run_api_pass.py Conway --workers 2
& '.venv\Scripts\python.exe' run_api_pass.py Brezis --workers 2
& '.venv\Scripts\python.exe' run_repairs.py Conway --workers 2
& '.venv\Scripts\python.exe' run_repairs.py Brezis --workers 2
& '.venv\Scripts\python.exe' assemble_book.py Conway
& '.venv\Scripts\python.exe' assemble_book.py Brezis
& '.venv\Scripts\python.exe' update_inventory.py Conway
& '.venv\Scripts\python.exe' update_inventory.py Brezis
& '.venv\Scripts\python.exe' validate_book.py Conway
& '.venv\Scripts\python.exe' validate_book.py Brezis
& '.venv\Scripts\python.exe' usage_report.py
```

`run_all.py` skips completed page ranges. `run_api_pass.py --follow` watches
for new completed OCR chunks and materializes page drafts before each API
pass. The Sol transcription and independent Astra review are saved for each
page with token counts. A model's `safe_to_accept` flag is recorded as
`ai_review_passed`; it is not represented as human visual verification.
Reviewer suggestions are not applied automatically because they can be
incorrect. Pages marked `needs_further_review`, `api_failed`, or containing
`[UNCLEAR: ...]` need resolution against the PDF image. The assembled book
retains its PDF page anchors, linked extracted figures, and a review manifest.
`run_repairs.py` makes one further image-based correction and independent
review. Remaining `needs_manual_review` pages require direct image inspection.

The 24-page pilot report is at `pilot/PILOT_REPORT.md`. OCR checkpoints and
API usage logs are kept in this work directory. No script deletes or rewrites
the source PDFs.

## Visual review without an API key

All Conway pages have been reviewed by AI against the original PDF page images,
and all flagged review items have been resolved. Review records are available
in `../../md/Conway/review/` and the per-page status files. Apparent source typos
are preserved and documented.

Use a uv-managed virtual environment for all Python dependencies. For this
image-review workflow, only PyMuPDF is needed; no API key or OCR model is required.
From this directory on Linux, with `uv` available:

```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python 'pymupdf==1.28.2'
uv run --no-sync python validate_book.py Conway
```

The PyMuPDF version above matches `uv.lock`. The full OCR/API workflow still
uses `uv sync --locked` as documented above.
