"""PoC: inspect the raw JSON structure of the Football Charts API.

Fetches a single league + season across the four endpoints that will feed the
data pipeline and prints a field-by-field type/nullability report.

Design decision inputs gathered here:
  - what identifiers exist (league, season, team, match)
  - which fields are nullable / inconsistent
  - season coverage (free tier = current + previous)
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from pathlib import Path

import httpx
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR / "backend"))
load_dotenv(ROOT_DIR / ".env")

from tests.conftest import BASE_URL, API_KEY  # noqa: E402

LEAGUE = "premier"
SEASON = "2025-2026"


def describe(items: list, keys: list[str]) -> dict:
    """For each key, report value type set, null count, and sample values."""
    report: dict = {}
    n = len(items)
    for key in keys:
        types: Counter[str] = Counter()
        null = 0
        missing = 0
        samples: list = []
        for row in items:
            if key not in row:
                missing += 1
                continue
            v = row[key]
            if v is None:
                null += 1
                continue
            types[type(v).__name__] += 1
            if len(samples) < 3:
                samples.append(v)
        report[key] = {
            "types": dict(types),
            "missing": missing,
            "null": null,
            "total": n,
            "samples": samples,
        }
    return report


def sorted_keys(items: list) -> list[str]:
    keys: Counter[str] = Counter()
    for row in items:
        if isinstance(row, dict):
            keys.update(row.keys())
    return [k for k, _ in keys.most_common()]


def main() -> None:
    if not API_KEY:
        raise SystemExit("FOOTBALL_CHARTS_API_KEY not set")

    headers = {"Authorization": f"Bearer {API_KEY}"}
    with httpx.Client(base_url=BASE_URL, headers=headers, timeout=60) as client:
        r = client.get("/leagues/")
        r.raise_for_status()
        leagues = r.json()

        teams_r = client.get(f"/leagues/{LEAGUE}/teams/", params={"season": SEASON})
        teams_r.raise_for_status()
        teams = teams_r.json()

        results_r = client.get(f"/leagues/{LEAGUE}/results/", params={"season": SEASON})
        results_r.raise_for_status()
        results = results_r.json()

        table_r = client.get(
            f"/leagues/{LEAGUE}/table/",
            params={"season": SEASON, "view": "classic"},
        )
        table_r.raise_for_status()
        table = table_r.json()

    out: dict = {
        "meta": {
            "base_url": BASE_URL,
            "league": LEAGUE,
            "season": SEASON,
            "fetched_at": None,
        },
        "leagues": {
            "top_level_keys": sorted_keys([leagues]),
            "count": leagues["count"],
            "season_window": leagues.get("season_window"),
            "league_entry_keys": sorted_keys(leagues["leagues"]),
            "season_coverage": {
                e["league"]: e["seasons"] for e in leagues["leagues"] if e["league"] == LEAGUE
            },
            "premier_sample": [e for e in leagues["leagues"] if e["league"] == LEAGUE],
        },
        "teams": {
            "top_level_keys": sorted_keys([teams]),
            "team_keys": sorted_keys(teams["teams"]),
            "field_report": describe(teams["teams"], sorted_keys(teams["teams"])),
            "n_teams": len(teams["teams"]),
        },
        "results": {
            "top_level_keys": sorted_keys([results]),
            "count": results["count"],
            "match_keys": sorted_keys(results["matches"]),
            "field_report": describe(results["matches"], sorted_keys(results["matches"])),
            "n_matches": len(results["matches"]),
            "sample_match": results["matches"][0] if results["matches"] else None,
        },
        "table": {
            "top_level_keys": sorted_keys([table]),
            "row_keys": sorted_keys(table["table"]),
            "field_report": describe(table["table"], sorted_keys(table["table"])),
            "n_rows": len(table["table"]),
            "sample_row": table["table"][0] if table["table"] else None,
        },
    }

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()