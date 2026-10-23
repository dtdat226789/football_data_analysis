"""Build the analytics database and run all analysis modules for every league.

Runs backend/scripts/build_database.py and then backend/scripts/run_analysis.py
for each league in data/raw/league_teams.json (leagues with teams > 0). The
first league's database build runs the schema reset; every other league passes
--skip-reset so rows already built for other leagues are preserved. Analysis is
per league and writes reports under data/analysis/<league>/.

Each league runs as its own subprocess so a failure never stops the pipeline:
the league is recorded as failed and the remaining leagues still run. The exit
code is 0 only when every requested league succeeded in every selected stage.

Usage:
    python backend/scripts/build_all_leagues.py
    python backend/scripts/build_all_leagues.py --league spain1 germany1
    python backend/scripts/build_all_leagues.py --db-only
    python backend/scripts/build_all_leagues.py --analysis-only
    python backend/scripts/build_all_leagues.py --skip-reset   # DB already built

Options:
    --league         only process these slugs (repeatable); default: every
                     league in data/raw/league_teams.json with teams > 0.
    --db-only        run the database build stage only (skip analysis).
    --analysis-only  run the analysis stage only (skip database build).
    --include-empty  also process leagues with teams: 0 in the catalog.
    --skip-reset     do not reset the schema on the first database build.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from db_common import RAW_DIR  # noqa: E402

ROOT_DIR = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent

CATALOG_PATH = RAW_DIR / "league_teams.json"

BUILD_SCRIPT = "build_database.py"
ANALYSIS_SCRIPT = "run_analysis.py"


def load_catalog(path: Path) -> dict:
    try:
        return json.loads(path.read_bytes())
    except (OSError, ValueError):
        return {}


def run(python: str, script: str, league: str, extra: list[str]) -> tuple[int]:
    cmd = [python, str(SCRIPT_DIR / script), "--league", league] + extra
    print(f"\n=== {script} (league={league}) ===")
    return subprocess.run(cmd, cwd=ROOT_DIR).returncode


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="build_all_leagues",
        description="Build the analytics database and run analysis for every catalog league.",
    )
    parser.add_argument("--league", action="append", default=None,
                        help="only process these slugs (repeatable); default: all with team data")
    parser.add_argument("--db-only", action="store_true",
                        help="run the database build stage only")
    parser.add_argument("--analysis-only", action="store_true",
                        help="run the analysis stage only")
    parser.add_argument("--include-empty", action="store_true",
                        help="also process leagues with teams: 0 in the catalog")
    parser.add_argument("--skip-reset", action="store_true",
                        help="do not reset the schema on the first database build")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    catalog = load_catalog(CATALOG_PATH)
    if not catalog:
        print(f"ERROR: no catalog at {CATALOG_PATH}")
        return 1

    if args.league:
        slugs = args.league
    else:
        slugs = sorted(
            slug for slug, meta in catalog.items()
            if args.include_empty or int(meta.get("teams", 0)) > 0
        )

    if not slugs:
        print("build_all_leagues: no leagues requested")
        return 1

    if args.db_only and args.analysis_only:
        print("build_all_leagues: --db-only and --analysis-only are mutually exclusive")
        return 1

    results: list[dict] = []
    python = sys.executable
    reset_pending = not args.skip_reset

    for league in slugs:
        entry: dict = {"league": league, "db": "-", "analysis": "-"}
        if league not in catalog:
            print(f"WARN  unknown league '{league}', skipping")
            entry["db"] = "skipped"
            entry["analysis"] = "skipped"
            results.append(entry)
            continue

        if not args.analysis_only:
            db_extra = [] if reset_pending else ["--skip-reset"]
            code = run(python, BUILD_SCRIPT, league, db_extra)
            reset_pending = False
            entry["db"] = "ok" if code == 0 else "failed"

        if not args.db_only:
            code = run(python, ANALYSIS_SCRIPT, league, [])
            entry["analysis"] = "ok" if code == 0 else "failed"

        results.append(entry)

    print("\nbuild_all_leagues summary:")
    print("| league | database | analysis |")
    print("|--------|----------|----------|")
    for r in results:
        print(f"| {r['league']} | {r['db']:8} | {r['analysis']:8} |")

    failed = [
        r["league"]
        for r in results
        if r["db"] == "failed" or r["analysis"] == "failed"
    ]
    if failed:
        print(f"build_all_leagues: {len(failed)} league(s) failed: {', '.join(failed)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
