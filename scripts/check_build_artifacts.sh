#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

missing=0
for path in data/raw/fixtures data/analysis; do
  if [ ! -d "$path" ]; then
    echo "error: missing directory $path" >&2
    missing=1
  fi
done

for path in data/raw/league_teams.json ml/datasets/match_result_dataset.json ml/datasets/match_predictions.json; do
  if [ ! -s "$path" ]; then
    echo "error: missing or empty file $path" >&2
    missing=1
  fi
done

if [ "$missing" -ne 0 ]; then
  echo "Generate the missing artifacts with 'bash scripts/generate_ml_artifacts.sh' and 'bash scripts/refresh_data.sh' before building." >&2
  exit 1
fi

for path in data/raw/fixtures data/analysis; do
  if [ -z "$(find "$path" -mindepth 1 -maxdepth 1 -print -quit)" ]; then
    echo "warning: $path is empty; the image will contain no data from it until a refresh runs." >&2
  fi
done

python3 - <<'PY'
import json
from pathlib import Path

for rel in (
    "data/raw/league_teams.json",
    "ml/datasets/match_result_dataset.json",
    "ml/datasets/match_predictions.json",
):
    json.loads(Path(rel).read_text(encoding="utf-8"))

preds = json.loads(Path("ml/datasets/match_predictions.json").read_text(encoding="utf-8"))
if not preds.get("model_id") or not preds.get("matches"):
    raise SystemExit("ml/datasets/match_predictions.json has no model_id or matches")
print("build artifacts OK")
PY
