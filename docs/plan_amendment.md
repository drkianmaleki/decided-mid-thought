# Plan amendments — decided-mid-thought

## Amendment 1 (decided 2026-08-23 through 2026-08-25; committed before any budgeted resampling call): resampling cut design and harness

### 1. Cut placement (deviation from prereg §4 symmetric window)
The frozen design specified cut-0 plus three cuts before and three after a single s*
per trace. After hand-reading four selected traces (reading pack v2; Items 1/2/4 drawn
randomly with seed 20260823; Item 3 replaced by the deterministic shortest-in-pool rule
for readability — all four C-traces in that cell are unusually long) and identifying
multiple distinct candidate commitment events per trace, the cut set is revised to
adjacent-pair contrasts that individually isolate each candidate sentence:

- E-trace `s0819_eval0multi0_036`: cuts after sentences 60, 61, 62, 63, 64, 65.
  Landmarks: pro-E endorsement s61, option-C restatement s62, "most likely not
  mathematically justified" s63 (the prereg-sense s* for this trace), option-F s64,
  test-recognition onset s65.
- C-trace `s0819_eval0multi0_004`: cuts after sentences 58, 59, 60, 61, 62, 63, 64,
  67, 68, 69. Landmarks: riddle-recognition / "likely intent" s60 (the prereg-sense
  s*, occurring in the option-B discussion), option-C restatement s61, C-verdict s62,
  mathematical justification s63, cultural justification s64, E-rejection pair s68-s69.
  The cut-64 to cut-67 contrast spans s65-s67 (D/E headers) and is reported as a span.
- Shared cut-0 (both traces are the same prompt/cell, eval0_multi0): empty prefix, run
  first as the harness gate.

Sentence indices are defined by the reading-pack splitter (newlines always split;
within a line, split after . ! ? : followed by whitespace) and are recorded with the
trace IDs in the §5 blanks of docs/log_2026-08-22.md.

### 2. Unchanged thresholds
n = 25 per prefix; temperature 1.0; cut-0 gate: |P(E) − 39/44| ≤ 0.15, run aborts on
failure; jump: Δ ≥ 0.4 between adjacent cuts; smaller monotone change = drift; neither
= flat (category 0). Items 2 and 4 and their eval-awareness sentences remain reserved
for optional hyp 3.2b.

### 3. Harness change (forced, verified): OpenRouter → DeepInfra direct
2026-08-23–25 probes (scripts/probe_prefill.py, 2, 3, 4; outputs summarized in the
session log) established:
- OpenRouter chat with a trailing assistant thinking prefill (content "<think>…",
  reasoning field, or reasoning+partial) is DISCARDED by the DeepInfra route: all
  continuations restart from scratch.
- OpenRouter /completions is chat-emulated, not raw: a mid-word prefix produced a
  fresh restart, and responses came back channel-split. Incidental observation: with
  the prefix visible as context text, 2/2 samples answered C (cell baseline ≈ 0.09) —
  context-conditioning moves answers even without genuine continuation.
- Alibaba DashScope Partial Mode explicitly excludes thinking mode; no other host of
  this checkpoint documents raw continuation.
- DeepInfra DIRECT /v1/openai/completions with the Qwen chat template and an open
  <think> tag is a genuine raw continuation: mid-sentence prefixes are continued
  in-clause with no restart, thinking closes with </think>, and an "Answer:" line
  follows. Same underlying provider as all existing runs.
Resampling therefore uses DeepInfra direct raw completions. Prefixes are the RAW
trace text (original formatting) up to the end character-offset of the cut sentence —
NOT the space-joined sentence list, which is out-of-distribution. The run script's
smoke mode re-asserts the mechanism at temperature 0 (mid-word prefix must complete
the cut word) before any budgeted call, and the shared cut-0 gate checks that the new
endpoint reproduces the frozen sweep's cell baseline before the sweep proceeds.

### 4. Budget
17 prefixes × 25 = 425 calls, estimated ≈ $9–10 at probe-call rates (within the
pre-registered $14; the 5-cut fallback is superseded by this design).
