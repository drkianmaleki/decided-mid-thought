# AI Safety 01

This project measures where in its chain of thought a reasoning model commits to
an answer on underspecified famous problems (a bat-and-ball variant), on
Qwen 3.6 27B (thinking) via OpenRouter with the DeepInfra backend pinned.
Pre-registered hypotheses and planning documents are in [docs/](docs/).

## Setup

- Python 3.12
- `pip install openai python-dotenv`
- Copy `.env.example` to `.env` and fill in both keys.

## Reproduction

Main sweep:

```
python scripts/sweep_2x2.py items/items_batball.csv -n 50
```

Baselines:

```
python scripts/baseline_levels.py -n 20 --workers 5
```

**Warning:** results depend on provider routing (DeepInfra pinned, no
fallbacks — `screen_items.py` additionally allows fallback to Nebius/Novita/Io
Net), `temperature=1.0`, and `model=qwen/qwen3.6-27b`. Per-sample cost was
~$0.04–0.05. Changing any of these will not reproduce the recorded
distributions.

## Data

See [runs/README.md](runs/README.md) for the file-to-script mapping and the
jsonl/csv data dictionary.

## Status

Pre-registration frozen 2026-08-22 (see [docs/](docs/)). Resampling
experiments next.
