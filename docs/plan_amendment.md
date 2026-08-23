# §7 — Pivot log ([DATE])
(Appended to mats12_research_plan.md. Past tense, factual. Numbers over adjectives.)

## 7.1 What was tried and what happened
Between [date] and [date] I screened four item pools for baseline uncertainty on Qwen 3.6 27B (thinking):
- Hand-written closed-world puzzles (food, seating): [20/20] correct; planted opinion cues explicitly
  labeled "distractor" in-trace.
- BBH logical deduction (7-object) and shuffled objects (7-object): [40/40].
- GPQA-Diamond conceptual physics: 23 items x 12, [248/248] valid answers correct, ~$[11.55].
Interpretation: [your one sentence — ceiling is a model finding, not a pipeline failure; cue-based
rationalization has no uncertainty to act on at feasible cost.]

## 7.2 The decision
Per plan §6a this is the pre-authorized instrument fallback, not a project change. Unchanged: [the joint
question, category 0 as null, prefill-and-resample, 2x2 logic, model]. Changed: [item type -> underspecified
famous problems; rationalization axis -> premise leakage (cue lives in weights, not prompt)]. Consequence:
[cue on/off control replaced by famous/literal item pair]. Clock [not reset], because [your reason].
Additional design decision ([date]): outcome measure restructured to trace-primary after the bat-and-ball
2x2 showed answers are elicitation-governed ([one number]); menus retained as [robustness factor / dropped].

## 7.3 Corrections to the standing plan
- Provider: Nebius does not carry Qwen 3.6. Using OpenRouter, DeepInfra pinned, no fallbacks.
  (Io Net: silent drops on long generations. Phala: no separable trace channel.)
- Second model (Nemotron) cut for time; single-model study, listed as limitation.
- Type 2 items promoted to main pool; Riddle Riddle (2606.27103) cited as establishing the item type.
  [Verify the arXiv number and claims against the actual paper before write-up.]
- [Anything else in the old plan now false.]

## 7.4 Clock
Started [date, time]. Logged so far: ~[5] h ([one-line itemization]). Remaining: [11] + 2 (write-up).
Toggl running; screenshot at submission.

## 7.5 Next actions
1. Hypotheses doc written & dated BEFORE the multi-item sweep: [link/filename].
2. Item pool extended to [5-6] items: [list, mark which are Riddle Riddle's and which self-written].
3. Multi-item 2x2 sweep; then judge validation; then targeted resampling per §5 gates.
