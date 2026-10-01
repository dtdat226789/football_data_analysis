"""Collect raw API data for every league in the Football Charts catalog.

Runs backend/scripts/collect_raw_data.py once per league using the seasons that
league declares in data/raw/league_teams.json (falling back to the historical
POC seasons when a league has no catalog entry). Leagues with teams: 0 are
skipped unless --include-empty.

Each league runs as its own subprocess so a failure never stops the pipeline:
the league is recorded as failed and the remaining leagues still run. The exit
code is 0 only when every requested league succeeded.

Usage:
    python backend/scripts/collect_all_leagues.py
    python backend/scripts/collect_all_leagues.py --league spain1 germany1
    python backend/scripts/collect_all_leagues.py --league italy1 --season 2025-2026
    python backend/scripts/collect_all_leagues.py --include-empty --overwrite --delay 0.5
    python backend/scripts/collect_all_leagues.py --active-only --overwrite

Overrides:
    --league       only collect these slugs (repeatable); default: every league
                   in data/raw/league_teams.json with teams > 0.
    --season       collect only these seasons for every league (repeatable);
                   default: each league's own catalog-declared seasons.
    --active-only  keep only the seasons that are currently in progress, so a
                   daily refresh stops re-downloading immutable history. If a
                   league declares no in-progress season, its most recent one is
                   collected instead so the run never silently no-ops.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from db_common import (  # noqa: E402
    COLLECTED_SEASONS,
    RAW_DIR,
    _season_sort_key,
    is_season_active,
    league_season_dirs,
)

ROOT_DIR = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent

CATALOG_PATH = RAW_DIR / "league_teams.json"


def load_catalog(path: Path) -> dict:
    try:
        return json.loads(path.read_bytes())
    except (OSError, ValueError):
        return {}


def active_seasons(seasons: list[str], today: date | None = None) -> list[str]:
    """Seasons still in progress, or the newest one when none are.

    Closed seasons are immutable once their window has passed, so a daily
    refresh only needs the live ones. The newest-season fallback guarantees at
    least one season per league rather than an empty (and therefore skipped)
    subprocess call.
    """
    live = [s for s in seasons if is_season_active(s, today)]
    if live:
        return live
    return [max(seasons, key=_season_sort_key)] if seasons else []


def resolve_seasons(
    catalog: dict,
    league: str,
    cli_seasons: list[str],
    *,
    active_only: bool = False,
    today: date | None = None,
) -> list[str]:
    if cli_seasons:
        return cli_seasons
    catalog_seasons = list(catalog.get(league, {}).get("seasons") or [])
    already_collected = league_season_dirs(league)
    seasons = list(dict.fromkeys(catalog_seasons + already_collected)) or list(COLLECTED_SEASONS)
    return active_seasons(seasons, today) if active_only else seasons


def run_collect(
    python: str,
    league: str,
    seasons: list[str],
    flag_args: list[str],
) -> tuple[int]:
    cmd = [python, str(SCRIPT_DIR / "collect_raw_data.py"), "--league", league]
    for season in seasons:
        cmd += ["--season", season]
    for flag in flag_args:
        if flag:
            cmd.append(flag)
    print(f"\n=== collect_raw_data.py (league={league}, seasons={', '.join(seasons)}) ===")
    return subprocess.run(cmd, cwd=ROOT_DIR).returncode


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="collect_all_leagues",
        description="Collect raw API data for every catalog league.",
    )
    parser.add_argument("--league", action="append", default=None,
                        help="only collect these slugs (repeatable); default: all with team data")
    parser.add_argument("--season", action="append", default=None,
                        help="override seasons for every league (repeatable)")
    parser.add_argument("--view", action="append", default=None,
                        help="table view to collect (repeatable); default: classic luck goals")
    parser.add_argument("--overwrite", action="store_true",
                        help="re-download files even if they already exist")
    parser.add_argument("--delay", type=float, default=None,
                        help="seconds between requests (default: 1.0)")
    parser.add_argument("--include-empty", action="store_true",
                        help="also collect leagues with teams: 0 in the catalog")
    parser.add_argument("--active-only", action="store_true",
                        help="collect only seasons currently in progress (daily refresh)")
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
        print("collect_all_leagues: no leagues requested")
        return 1

    flag_args = []
    for view in args.view or []:
        flag_args += ["--view", view]
    if args.overwrite:
        flag_args.append("--overwrite")
    if args.delay is not None:
        flag_args += ["--delay", str(args.delay)]

    results: list[dict] = []
    python = sys.executable
    today = date.today()
    for league in slugs:
        if league not in catalog:
            print(f"WARN  unknown league '{league}', skipping")
            results.append({"league": league, "seasons": [], "status": "skipped"})
            continue
        seasons = resolve_seasons(
            catalog, league, args.season, active_only=args.active_only, today=today
        )
        if not seasons:
            print(f"WARN  no season to collect for '{league}', skipping")
            results.append({"league": league, "seasons": [], "status": "skipped"})
            continue
        code = run_collect(python, league, seasons, flag_args)
        status = "ok" if code == 0 else "failed"
        results.append({"league": league, "seasons": seasons, "status": status})

    print("\ncollect_all_leagues summary:")
    print("| league | seasons | status |")
    print("|--------|---------|--------|")
    for r in results:
        print(f"| {r['league']} | {', '.join(r['seasons']) or '(default)'} | {r['status']} |")

    failed = [r["league"] for r in results if r["status"] == "failed"]
    if failed:
        print(f"collect_all_leagues: {len(failed)} league(s) failed: {', '.join(failed)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())