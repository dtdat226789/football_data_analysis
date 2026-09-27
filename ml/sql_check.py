"""Independent SQL-level consistency check for the materialized dataset.

This is a *reference* verification that does not reuse the Python build logic
at all: it runs plain SQL against PostgreSQL and compares a few invariants to
the materialized CSV/JSON rows. Crossing the Python and SQL implementations
catches both implementation bugs and accidental data drift.

Checks:
  1. row count matches the DB's completed-match count for the league
  2. api_id set matches the DB exactly
  3. for each materialized row, the DB has the same home/away score
  4. DB-level sanity: no row is self-aware (a team cannot play itself)

The league must be the one the dataset was built for: comparing e.g. a Spain
dataset against the `premier` rows would report a mismatch every time. The
season scope mirrors `load_matches` (complete seasons only) so the two sides
count the same rows.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend" / "scripts"))
sys.path.insert(0, str(ROOT))

import psycopg2.extras  # noqa: E402

from ml import db  # noqa: E402

DB_ROWS_QUERY = """
SELECT m.api_id, m.home_score, m.away_score
FROM matches m
JOIN league_seasons ls ON ls.id = m.league_season_id
JOIN leagues l ON l.id = ls.league_id
WHERE l.api_key = %s AND ls.season_state = 'complete'
"""


def run(rows: list[dict], league: str | None = None) -> dict:
    league = league or db.LEAGUE
    expected_ids = {r["api_id"] for r in rows}
    conn = db.get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(DB_ROWS_QUERY, (league,))
            db_rows = cur.fetchall()
    finally:
        conn.close()

    db_ids = {r["api_id"] for r in db_rows}
    by_id = {r["api_id"]: (r["home_score"], r["away_score"]) for r in db_rows}
    problems: list[str] = []
    if expected_ids != db_ids:
        problems.append(
            f"api_id mismatch: only_in_dataset={len(expected_ids - db_ids)} "
            f"only_in_db={len(db_ids - expected_ids)}"
        )
    if len(rows) != len(db_rows):
        problems.append(f"row count mismatch: dataset={len(rows)} db={len(db_rows)}")
    bad_scores = [
        r["api_id"]
        for r in rows
        if by_id.get(r["api_id"]) != (r["home_score"], r["away_score"])
    ]
    if bad_scores:
        problems.append(f"score mismatch for api_ids: {bad_scores[:10]}")
    if any(r["home_team_id"] == r["away_team_id"] for r in rows):
        problems.append("a team appears as both home and away in the same row")
    return {
        "ok": not problems,
        "problems": problems,
        "db_rows": len(db_rows),
        "league": league,
    }


def main(argv: list[str] | None = None) -> int:
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "dataset",
        nargs="?",
        default="ml/datasets/match_result_dataset.json",
        help="path to the materialized dataset JSON",
    )
    parser.add_argument(
        "--league",
        default=db.LEAGUE,
        help="league the dataset was built for (must match, or the check is meaningless)",
    )
    args = parser.parse_args(argv)
    rows = json.loads(Path(args.dataset).read_text())
    report = run(rows, args.league)
    print(json.dumps(report, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())