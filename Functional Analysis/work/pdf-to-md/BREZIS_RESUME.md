# Brezis PDF → Markdown 재개 메모

- 마지막 갱신: 2026-09-30 17:10 JST경
- 원본: `../../source/Brezis.pdf` (614 PDF pages)
- 최종 출력: `../../md/Brezis/`
- 현재 실행 중인 변환·검수 작업: 없음

## 1. 현재 완료 상태

### 로컬 CPU 변환

- PDF 1–167쪽은 모두 MinerU CPU 변환과 page Markdown materialize가 완료됐다.
- 전체 체크포인트 기준으로는 172쪽이 완료돼 있다.
  - 연속 완료: 1–167
  - 기존 파일럿으로 별도 완료: 195, 215, 277, 308, 339
- `chunks/brezis/p0136-p0167/` 변환은 완료됐다(32쪽, 583.81초). `complete.json`과 `page-0136.md`–`page-0167.md`를 검증했다.
- `materialize_pages.py Brezis`의 마지막 결과는 `materialized_pages=172`였다.

### 원본 이미지 대조가 완전히 끝난 페이지

- 1–44
- 46–53
- 78–82
- 104–107
- 원본에서 확인된 빈 페이지: 3, 7, 11, 15, 45, 103, 195, 215, 277, 339, 363

완전히 교정된 페이지만 `reviewed/brezis/`에 둔다. 현재 이 폴더에는 61개 page 파일이 있고, 그중 4개는 3·7·11·15쪽의 zero-byte 빈 페이지 파일이다. 조립 manifest 기준 실제 `subagent_visual_reviewed` 본문 페이지는 57쪽이다.

### 미완성 교정본

미완성 파일은 삭제하지 않고 `review-staging/brezis/`로 옮겼다. 이 폴더의 파일을 조립 완료본으로 취급하면 안 된다.

- 54–69: 주요 수식·번호 오류는 일부 고쳤지만 OCR typography/text 잔여 오류가 있어 원본과 다시 끝까지 대조해야 한다.
- 70–77: 거의 raw OCR 초안 상태다. 특히 70–71쪽의 Chapter 3 제목, $\Phi$/집합족 기호와 각주, 72–73쪽의 norm·proposition·proof 문구, 74쪽 각주, 77쪽 weak-* 표기를 교정해야 한다.
- 83–102: 원본 이미지는 열어 보았지만 파일은 OCR 초안만 배치한 상태다. 모두 다시 대조해야 한다.
- 80쪽은 검수 완료 상태이며 잘못 들어간 U+0014 제어문자를 `(3′)`로 고쳤다. 이 파일은 `reviewed/brezis/`에 남아 있다.
- 104–135 이미지는 한 번 열람했지만 실제 교정 완료 파일은 104–107뿐이다. 108–135는 처음부터 page별 교정을 진행한다.

staging 파일을 검수 완료했을 때만 해당 파일을 `reviewed/brezis/`로 이동한다.

### 현재 부분 조립본

- `../../md/Brezis/`는 140/614쪽 부분 조립본이다.
- 18개 content Markdown 파일과 `README.md`, `review/page-manifest.csv`, `review/validation.json`이 생성돼 있다.
- manifest 상태:
  - `subagent_visual_reviewed`: 57
  - `source_blank_page`: 10
  - `unreviewed_ocr_draft`: 72
  - `ai_review_passed`: 1 (파일럿 308쪽)
- validation의 문제 2개는 부분 조립이라 당연히 생기는 `page_coverage`와 `page_anchors`뿐이다. 깨진 링크는 현재 없다.
- 이 부분 조립본은 진행 상황 확인용이며 최종본이 아니다.

## 2. 실행 환경

- 이 PC에서는 GPU를 사용할 수 없다 (`torch.cuda.is_available() == False`, `nvidia-smi` 없음).
- CPU MinerU 변환은 실제로 성공했다.
- `.venv`에 잠금 파일 기준 의존성이 설치돼 있다.
- MinerU 모델은 `.mineru/`에 내려받아져 있다(약 793 MB).
- `.env`와 `OPENAI_API_KEY`는 없다.
  - 로컬 `run_all.py`, `materialize_pages.py`, 조립·검증에는 문제가 없다.
  - `run_api_pass.py`와 `run_repairs.py`는 실행하지 않는다.
  - 이미지 검수는 Codex subagent로 계속한다.

## 3. CPU 변환 재개 명령

작업 폴더로 이동한다.

```bash
cd "/home/moon/workspace/math_stat_ai/Functional Analysis/work/pdf-to-md"
```

중간 세션 종료 시 재처리 손실을 줄이기 위해 다음에는 chunk size 16을 권장한다.

```bash
SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
MINERU_HOME="$PWD/.mineru" \
HF_HOME="$PWD/.huggingface" \
MODELSCOPE_HOME="$PWD/.modelscope" \
MODELSCOPE_CACHE="$PWD/.modelscope/cache" \
MINERU_MODEL_SOURCE=huggingface \
.venv/bin/python run_all.py Brezis --chunk-size 16
```

`run_all.py`는 완료된 개별 페이지를 모두 인식하도록 수정돼 있다. 재개하면 1–167과 파일럿 5쪽을 건너뛰고 168쪽부터 시작한다. 장시간 Codex 실행 세션이 종료되더라도 같은 명령을 다시 실행하면 된다.

새 chunk가 완료될 때마다 다음을 실행해 page draft를 만든다.

```bash
.venv/bin/python materialize_pages.py Brezis
```

## 4. subagent 검수 재개 순서

한 CPU OCR worker와 최대 3개 검수 subagent를 병렬로 사용한다. 같은 page 파일을 두 agent가 동시에 고치지 않는다.

1. `review-staging/brezis/page-0054.md`–`page-0077.md`를 원본과 끝까지 대조한다.
2. `review-staging/brezis/page-0083.md`–`page-0102.md`를 원본과 끝까지 대조한다.
3. raw page draft 108–135를 대조해 새 `reviewed/brezis/page-XXXX.md`를 만든다.
4. 이후 CPU 체크포인트가 완료되는 순서대로 서로 겹치지 않는 범위를 agent에 할당한다.
5. 195·215·277·339는 검증된 빈 페이지이므로 별도 전사가 필요 없다. 308은 파일럿 AI pass가 있지만 최종 기준상 다시 원본 대조한다.

각 agent 지시에는 다음 기준을 넣는다.

- PDF 렌더 이미지를 권위 있는 원본으로 사용하고 page draft는 보조 자료로만 사용한다.
- 모든 비어 있지 않은 페이지를 실제로 열어 본다.
- running header와 folio는 제거한다.
- prose, heading, theorem/proof/exercise 번호, 모든 수식·식 번호, 각주, caption/figure를 원문 순서대로 보존한다.
- 인라인 수식은 `$...$`, 독립 수식은 `$$...$$`를 사용한다.
- 원문 오탈자를 임의로 고치지 않는다.
- 조립기가 넣는 page anchor는 page 파일에 넣지 않는다.
- 진짜 원본 판독 불가가 아니면 `[UNCLEAR]`를 남기지 않는다.
- 완전 교정 전에는 `reviewed/brezis/`로 승격하지 않는다.

## 5. 자동 검사

검수 파일을 승격하기 전에 최소한 다음을 확인한다.

- 제어문자 없음
- 홀수 개의 비이스케이프 `$` 없음
- `\begin{...}` / `\end{...}` 불일치 없음
- `[UNCLEAR:]` 없음(원본 자체가 판독 불가인 경우는 별도 기록)
- figure 링크는 raw chunk 상대 경로를 직접 넣지 말고 `[FIGURE: 설명]` marker를 사용한다. `assemble_book.py`가 최종 `assets/` 링크로 바꾼다.

## 6. 전권 완료 후 실행

전 페이지 CPU draft와 시각 검수가 끝난 다음에만 `--allow-partial` 없이 최종 조립한다.

```bash
.venv/bin/python materialize_pages.py Brezis
.venv/bin/python assemble_book.py Brezis
.venv/bin/python update_inventory.py Brezis
.venv/bin/python validate_book.py Brezis
```

최종 완료 조건:

- manifest 614쪽, 중복·누락 없음
- 모든 비빈 페이지가 `subagent_visual_reviewed`
- 11개 실제 빈 페이지가 `source_blank_page`
- validation `problem_count=0`
- README의 18개 장·부속 링크와 모든 asset 링크가 정상
- `unreviewed_ocr_draft`, `[UNCLEAR]`, 제어문자, 깨진 수식 구분자 없음

## 7. 이번에 반영한 파이프라인 수정

- `run_all.py`: 1쪽 파일럿을 포함해 이미 완료된 page를 재처리하지 않도록 변경
- `assemble_book.py`: 검증된 빈 페이지 처리, `reviewed/brezis/` 우선 사용, 정확한 review status·source path 기록
- `update_inventory.py`: 장 첫 페이지가 이전 장의 마지막 section으로 잘못 분류되던 문제 수정
- `.gitignore`: `.modelscope/` cache 제외
- raw OCR, API 파일럿, Conway 관련 기존 변경은 건드리지 않음
