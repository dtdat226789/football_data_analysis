#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
PYTHON="${PYTHON:-python3}"

"$PYTHON" ml/build_dataset.py
"$PYTHON" ml/train.py

if ! "$PYTHON" ml/evaluate.py --enforce-baseline; then
  "$PYTHON" ml/train.py --force-baseline
  "$PYTHON" ml/evaluate.py --enforce-baseline
fi

"$PYTHON" -m ml.backfill_predictions

"$PYTHON" - <<'PY'
import json
from pathlib import Path

path = Path("ml/datasets/match_predictions.json")
payload = json.loads(path.read_text(encoding="utf-8"))
if not payload.get("model_id") or not payload.get("matches"):
    raise SystemExit(f"{path} has no model_id or matches")
print(f"verified {path}: {payload['n_matches']} matches, model {payload['model_id']}")
PY
