"""Snapshot table row counts and detect data loss between two snapshots."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from db_common import get_conn

TABLES = (
    "countries",
    "goal_timing",
    "league_seasons",
    "leagues",
    "match_predictions",
    "matches",
    "projections",
    "raw_payloads",
    "seasons",
    "standings",
    "team_aliases",
    "team_league_seasons",
    "team_seasons",
    "teams",
    "track_accuracy",
    "track_daily",
    "track_market_stats",
    "track_picks",
    "track_record",
    "track_summary",
)


def snapshot_counts(conn) -> dict[str, int]:
    counts: dict[str, int] = {}
    with conn.cursor() as cur:
        for table in TABLES:
            cur.execute("SELECT to_regclass(%s)", (table,))
            if cur.fetchone()[0] is None:
                continue
            cur.execute(f'SELECT count(*) FROM "{table}"')
            counts[table] = int(cur.fetchone()[0])
    return counts


def compare_counts(before: dict[str, int], after: dict[str, int]) -> list[str]:
    issues: list[str] = []
    for table in sorted(set(before) | set(after)):
        previous = int(before.get(table, 0))
        current = int(after.get(table, 0))
        if current < previous:
            issues.append(f"{table}: {previous} -> {current}")
    return issues


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--snapshot", metavar="PATH", help="write current table counts to PATH")
    mode.add_argument("--before", metavar="PATH", help="snapshot taken before a destructive change")
    parser.add_argument("--after", metavar="PATH", help="snapshot taken after the change")
    args = parser.parse_args(argv)
    if args.before and not args.after:
        parser.error("--before requires --after")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.snapshot:
        conn = get_conn()
        try:
            payload = {"counts": snapshot_counts(conn)}
        finally:
            conn.close()
        Path(args.snapshot).write_text(
            json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8"
        )
        print(f"row counts written to {args.snapshot}")
        return 0

    before = json.loads(Path(args.before).read_text(encoding="utf-8"))["counts"]
    after = json.loads(Path(args.after).read_text(encoding="utf-8"))["counts"]
    issues = compare_counts(before, after)
    if issues:
        for issue in issues:
            print(f"DATA LOSS {issue}")
        return 1
    print(f"row counts preserved across {len(before)} table(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
