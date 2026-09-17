"""Build the Football Charts database end-to-end (steps 01-06).

Runs the full ordered pipeline:
    00 Reset (drops superseded/current tables) -> 01 Registry -> 02/03 Identity
    -> 04 Matches+Standings -> 05 DB validation -> 06 Index tuning.

Each step is also runnable on its own:
    python backend/scripts/etl_01_registry.py
    python backend/scripts/etl_02_identity.py
    python backend/scripts/etl_03_matches_standings.py
    python backend/scripts/validate_db.py
    python backend/scripts/tune_indexes.py

Usage:
    python backend/scripts/build_database.py
    python backend/scripts/build_database.py --skip-reset   # keep existing table state
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from db_common import SQL_DIR, get_conn

ROOT_DIR = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT_DIR / "backend" / "scripts"

STEPS = [
    "etl_01_registry.py",
    "etl_02_identity.py",
    "etl_03_matches_standings.py",
    "validate_db.py",
    "tune_indexes.py",
]


def reset_database() -> None:
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute((SQL_DIR / "00_reset.sql").read_text())
        conn.commit()
        print("\n=== 00_reset.sql ===")
        print("reset complete")
    finally:
        conn.close()


def run(python: str, script: str) -> int:
    print(f"\n=== {script} ===")
    return subprocess.run([python, str(SCRIPTS / script)]).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the analytics database end-to-end.")
    parser.add_argument("--skip-reset", action="store_true", help="do not run 00_reset.sql")
    args = parser.parse_args()

    python = sys.executable
    if not args.skip_reset:
        reset_database()

    for script in STEPS:
        code = run(python, script)
        if code != 0:
            print(f"FAILED: {script} (exit {code})")
            return 1
    print("\nBuild complete: all steps passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())