"""Build the versioned match-result feature dataset from PostgreSQL.

Usage:  python3 ml/build_dataset.py
        python3 ml/build_dataset.py --league premier

Reads the analytics DB via ml.db, computes leakage-safe feature rows, runs the
in-process validation (ml.validation) plus the independent SQL cross-check
(ml.sql_check), then materializes:

  ml/datasets/match_result_dataset.json   lossless canonical artifact
  ml/datasets/match_result_dataset.csv    flat file for notebooks/PCs
  ml/datasets/split_manifest.json         train/holdout split metadata
  ml/datasets/validation_report.json      check results + summary stats

Exit code is 1 when any validation check fails.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ml.features.build_features import (
    ALL_COLUMNS,
    CONTEXT_COLUMNS,
    FEATURE_COLUMNS,
    build_rows,
)
from ml.sql_check import run as run_sql_check
from ml.validation import DEFAULT_HOLDOUT_SEASONS, DEFAULT_TRAIN_SEASONS, check_dataset

ROOT = Path(__file__).resolve().parents[1]
DATASETS_DIR = ROOT / "ml" / "datasets"

DATASET_NAME = "match_result_dataset"
CSV_COLUMNS = CONTEXT_COLUMNS


def materialize(rows: list[dict]) -> tuple[Path, Path]:
    DATASETS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = DATASETS_DIR / f"{DATASET_NAME}.json"
    csv_path = DATASETS_DIR / f"{DATASET_NAME}.csv"
    json_path.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=ALL_COLUMNS)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: ("" if r[k] is None else r[k]) for k in ALL_COLUMNS})
    return json_path, csv_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--league", default="premier", help="league api_key (default premier)")
    args = parser.parse_args(argv)

    from ml import db  # local import keeps the module import-light

    conn = db.get_conn()
    try:
        rows = build_rows(conn, league=args.league)
    finally:
        conn.close()

    report = check_dataset(rows)
    sql_report = run_sql_check(rows)

    json_path, csv_path = materialize(rows)

    manifest = {
        "dataset": DATASET_NAME,
        "league": args.league,
        "rows": len(rows),
        "features": len(FEATURE_COLUMNS),
        "train_seasons": DEFAULT_TRAIN_SEASONS,
        "holdout_seasons": DEFAULT_HOLDOUT_SEASONS,
        "files": {"json": json_path.name, "csv": csv_path.name},
        "columns": ALL_COLUMNS,
    }
    split_meta = {
        "train_seasons": report["stats"].get("train_seasons", []),
        "holdout_seasons": report["stats"].get("holdout_seasons", []),
        "train_rows": report["stats"].get("train_rows", 0),
        "holdout_rows": report["stats"].get("holdout_rows", 0),
    }
    (DATASETS_DIR / "split_manifest.json").write_text(json.dumps(split_meta, indent=2))

    summary = {
        "validation": {"ok": report["ok"], "errors": report["errors"], "warnings": report["warnings"]},
        "sql_check": sql_report,
        "stats": report["stats"],
        "manifest": manifest,
    }
    (DATASETS_DIR / "validation_report.json").write_text(json.dumps(summary, indent=2))

    print(f"rows: {len(rows)}")
    print(f"sql check: {'OK' if sql_report['ok'] else 'FAILED ' + str(sql_report['problems'])}")
    print(f"artifacts: {json_path}, {csv_path}")
    print(f"validation: {'PASS' if report['ok'] else 'FAIL'}")
    for e in report["errors"]:
        print(f"  error: {e}")
    for w in report["warnings"]:
        print(f"  warning: {w}")
    return 0 if report["ok"] and sql_report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())