"""Module 2 - Goal analysis report.

Reads `matches` (with `league_seasons` / `seasons` / `leagues` context) from the
Football Charts analytics database *read-only* and produces a report under
data/analysis/:

    goals_analysis.json    # machine-readable report
    goals_analysis.md      # human-readable summary
    charts/goals_analysis_*.png   # goals-per-match bar, avg goals per season

Sections:
    1. Goals per match distribution
    2. Goals per match per season
    3. Home vs away goal share
    4. BTTS (Both Teams To Score)
    5. Clean sheets
    6. Scoring intensity (1st half vs 2nd half, second-half-only matches)
    7. First-goal timing buckets

Every SQL statement is a SELECT; the transaction is rolled back before the
connection closes.

Usage:
    python backend/scripts/analyze_goals.py
    python backend/scripts/analyze_goals.py --league spain1
    python backend/scripts/analyze_goals.py --out-dir data/analysis --out-stem my_report
"""
from __future__ import annotations

import argparse
import statistics
import sys
from collections import Counter
from pathlib import Path

import psycopg2.extras

sys.path.insert(0, str(Path(__file__).resolve().parent))

from analysis_common import (
    parse_args,
    args_to_config,
    report_metadata,
    write_report,
    fmt_pct,
    fmt_md_table,
    render_report_header,
    round_pct,
    new_figure,
    save_chart,
)
from db_common import get_conn

STEM = "goals_analysis"
SCRIPT_NAME = "backend/scripts/analyze_goals.py"

FIRST_GOAL_BUCKETS = [
    (1, 15), (16, 30), (31, 45),
    (46, 60), (61, 75), (76, 90), (91, 120),
]

MATCHES_QUERY = """
    SELECT s.name AS season,
           m.home_score,
           m.away_score,
           m.home_ht,
           m.away_ht,
           m.first_goal_time
    FROM matches m
    JOIN league_seasons ls ON ls.id = m.league_season_id
    JOIN seasons s ON s.id = ls.season_id
    JOIN leagues l ON l.id = ls.league_id
    WHERE l.api_key = %s
    ORDER BY s.start_year, s.name, m.match_date, m.game_index
"""


# ── pure helpers (unit-testable without a database) ─────────────────────────
def total_goals(row: dict) -> int:
    return row["home_score"] + row["away_score"]


def ht_total(row: dict) -> int | None:
    """Sum of half-time goals, or None when no HT score was recorded."""
    home_ht, away_ht = row.get("home_ht"), row.get("away_ht")
    if home_ht is None or away_ht is None:
        return None
    return home_ht + away_ht


def second_half_total(row: dict) -> int | None:
    """Full-time goals minus half-time goals, or None when HT is missing."""
    ht = ht_total(row)
    if ht is None:
        return None
    return total_goals(row) - ht


def season_order(rows: list[dict]) -> list[str]:
    order: list[str] = []
    for row in rows:
        if row["season"] not in order:
            order.append(row["season"])
    return order


def per_season_entries(rows: list[dict], stats_fn) -> list[dict]:
    """Apply a per-group stats function and merge each season's name."""
    return [
        {"season": season, **stats_fn([r for r in rows if r["season"] == season])}
        for season in season_order(rows)
    ]


def build_goals_distribution(rows: list[dict]) -> dict:
    counts = Counter(total_goals(r) for r in rows)
    n = len(rows)
    max_goals = max(counts) if counts else 0
    buckets = [
        {
            "goals": g,
            "count": counts.get(g, 0),
            "pct": round_pct(counts.get(g, 0), n),
        }
        for g in range(max_goals + 1)
    ]
    return {"n_matches": n, "max_goals": max_goals, "buckets": buckets}


def group_goal_stats(group: list[dict]) -> dict:
    n = len(group)
    home = sum(r["home_score"] for r in group)
    away = sum(r["away_score"] for r in group)
    total = home + away
    return {
        "n_matches": n,
        "total_goals": total,
        "avg_goals": round(total / n, 3) if n else None,
        "avg_home": round(home / n, 3) if n else None,
        "avg_away": round(away / n, 3) if n else None,
        "home_goals": home,
        "away_goals": away,
    }


def build_goals_per_season(rows: list[dict]) -> list[dict]:
    return per_season_entries(rows, group_goal_stats)


def build_goal_share(rows: list[dict], per_season: list[dict]) -> dict:
    home = sum(r["home_score"] for r in rows)
    away = sum(r["away_score"] for r in rows)
    total = home + away
    return {
        "home_goals": home,
        "away_goals": away,
        "total_goals": total,
        "home_pct": round_pct(home, total),
        "away_pct": round_pct(away, total),
        "home_away_ratio": round(home / away, 3) if away else None,
        "per_season": [
            {
                "season": s["season"],
                "home_goals": s["home_goals"],
                "away_goals": s["away_goals"],
                "total_goals": s["total_goals"],
                "home_pct": round_pct(s["home_goals"], s["total_goals"]),
                "away_pct": round_pct(s["away_goals"], s["total_goals"]),
            }
            for s in per_season
        ],
    }


def btts_stats(group: list[dict]) -> dict:
    n = len(group)
    count = sum(1 for r in group if r["home_score"] >= 1 and r["away_score"] >= 1)
    return {"n_matches": n, "count": count, "pct": round_pct(count, n)}


def build_btts(rows: list[dict]) -> dict:
    return {
        "overall": btts_stats(rows),
        "per_season": per_season_entries(rows, btts_stats),
    }


def clean_sheet_stats(group: list[dict]) -> dict:
    n = len(group)
    home_cs = sum(1 for r in group if r["away_score"] == 0)
    away_cs = sum(1 for r in group if r["home_score"] == 0)
    both = sum(1 for r in group if r["home_score"] == 0 and r["away_score"] == 0)
    any_cs = home_cs + away_cs - both
    return {
        "n_matches": n,
        "home_clean_sheets": home_cs,
        "away_clean_sheets": away_cs,
        "total_clean_sheets": home_cs + away_cs,
        "home_cs_pct": round_pct(home_cs, n),
        "away_cs_pct": round_pct(away_cs, n),
        "matches_with_clean_sheet": any_cs,
        "matches_with_clean_sheet_pct": round_pct(any_cs, n),
        "both_clean_sheet_matches": both,
    }


def build_clean_sheets(rows: list[dict]) -> dict:
    return {
        "overall": clean_sheet_stats(rows),
        "per_season": per_season_entries(rows, clean_sheet_stats),
    }


def scoring_intensity_stats(group: list[dict]) -> dict:
    n = len(group)
    with_ht = [r for r in group if ht_total(r) is not None]
    fh = sum(ht_total(r) for r in with_ht)
    sh = sum(second_half_total(r) for r in with_ht)
    split_total = fh + sh
    second_only = sum(1 for r in group if ht_total(r) == 0 and total_goals(r) >= 1)
    return {
        "n_matches": n,
        "n_with_ht": len(with_ht),
        "first_half_goals": fh,
        "second_half_goals": sh,
        "split_total_goals": split_total,
        "first_half_pct": round_pct(fh, split_total),
        "second_half_pct": round_pct(sh, split_total),
        "avg_first_half": round(fh / len(with_ht), 3) if with_ht else None,
        "avg_second_half": round(sh / len(with_ht), 3) if with_ht else None,
        "second_half_only": {
            "count": second_only,
            "pct": round_pct(second_only, n),
        },
    }


def build_scoring_intensity(rows: list[dict]) -> dict:
    return {
        "overall": scoring_intensity_stats(rows),
        "per_season": per_season_entries(rows, scoring_intensity_stats),
    }


def build_first_goal_timing(rows: list[dict]) -> dict:
    n_total = len(rows)
    times = sorted(r["first_goal_time"] for r in rows if r["first_goal_time"] is not None)
    n_scoring = len(times)
    buckets: dict[str, dict] = {}
    for lo, hi in FIRST_GOAL_BUCKETS:
        key = f"{lo}-{hi}"
        count = sum(1 for t in times if lo <= t <= hi)
        buckets[key] = {
            "count": count,
            "pct_of_matches": round_pct(count, n_total),
            "pct_of_scoring": round_pct(count, n_scoring),
        }
    summary = None
    if times:
        summary = {
            "n": len(times),
            "min": times[0],
            "max": times[-1],
            "mean": round(statistics.fmean(times), 2),
            "p50": statistics.median(times),
        }
    return {
        "n_total": n_total,
        "n_with_first_goal": n_scoring,
        "n_goalless": n_total - n_scoring,
        "unbucketed": n_scoring - sum(b["count"] for b in buckets.values()),
        "buckets": buckets,
        "summary": summary,
    }


# ── query layer (SELECT-only) ───────────────────────────────────────────────
def fetch_matches(cur, league: str) -> list[dict]:
    cur.execute(MATCHES_QUERY, (league,))
    return [dict(r) for r in cur.fetchall()]


# ── report assembly ──────────────────────────────────────────────────────────
def build_report(conn, cfg: dict) -> dict:
    report = report_metadata(STEM, SCRIPT_NAME, cfg)
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        rows = fetch_matches(cur, cfg["league"])

    per_season = build_goals_per_season(rows)

    report["goals_distribution"] = build_goals_distribution(rows)
    report["goals_per_season"] = per_season
    report["goal_share"] = build_goal_share(rows, per_season)
    report["btts"] = build_btts(rows)
    report["clean_sheets"] = build_clean_sheets(rows)
    report["scoring_intensity"] = build_scoring_intensity(rows)
    report["first_goal_timing"] = build_first_goal_timing(rows)
    return report


# ── charts ───────────────────────────────────────────────────────────────────
def goals_distribution_chart(distribution: dict):
    fig, ax = new_figure(w=9, h=5)
    labels = [str(b["goals"]) for b in distribution["buckets"]]
    values = [b["count"] for b in distribution["buckets"]]
    ax.bar(labels, values, color="#4C72B0")
    ax.set_ylabel("matches")
    ax.set_xlabel("total goals per match")
    ax.set_title("Goals per match distribution")
    fig.tight_layout()
    return fig


def avg_goals_season_chart(per_season: list[dict]):
    fig, ax = new_figure(w=8, h=5)
    seasons = [s["season"] for s in per_season]
    home = [s["avg_home"] if s["avg_home"] is not None else 0.0 for s in per_season]
    away = [s["avg_away"] if s["avg_away"] is not None else 0.0 for s in per_season]
    ax.bar(seasons, home, label="home", color="#55A868")
    ax.bar(seasons, away, bottom=home, label="away", color="#4C72B0")
    ax.set_ylabel("avg goals per match")
    ax.set_xlabel("season")
    ax.set_title("Average goals per season (home vs away)")
    ax.legend()
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig


def build_charts(report: dict, out_dir: Path) -> list[Path]:
    charts = [
        save_chart(out_dir, f"{STEM}_distribution", goals_distribution_chart(report["goals_distribution"])),
        save_chart(out_dir, f"{STEM}_avg_per_season", avg_goals_season_chart(report["goals_per_season"])),
    ]
    return [c for c in charts if c is not None]


# ── markdown rendering ───────────────────────────────────────────────────────
def render_markdown(report: dict) -> str:
    lines = render_report_header(report, "Goal Analysis").splitlines()
    add = lines.append

    dist = report["goals_distribution"]
    add("")
    add("## 1. Goals per match distribution")
    add(fmt_md_table(
        ["goals", "matches", "pct"],
        [[g["goals"], g["count"], fmt_pct(g["pct"])] for g in dist["buckets"]],
    ))

    add("")
    add("## 2. Goals per match per season")
    add(fmt_md_table(
        ["season", "matches", "total goals", "avg home", "avg away", "avg total"],
        [
            [s["season"], s["n_matches"], s["total_goals"],
             s["avg_home"] if s["avg_home"] is not None else "-",
             s["avg_away"] if s["avg_away"] is not None else "-",
             s["avg_goals"] if s["avg_goals"] is not None else "-"]
            for s in report["goals_per_season"]
        ],
    ))

    gs = report["goal_share"]
    add("")
    add("## 3. Home vs away goal share")
    add(f"- Home goals: **{gs['home_goals']}** ({fmt_pct(gs['home_pct'])})")
    add(f"- Away goals: **{gs['away_goals']}** ({fmt_pct(gs['away_pct'])})")
    add(f"- Home/away ratio: **{gs['home_away_ratio']}**"
        if gs["home_away_ratio"] is not None else "-")
    add("")
    add(fmt_md_table(
        ["season", "home goals", "away goals", "total", "home pct", "away pct"],
        [
            [s["season"], s["home_goals"], s["away_goals"], s["total_goals"],
             fmt_pct(s["home_pct"]), fmt_pct(s["away_pct"])]
            for s in gs["per_season"]
        ],
    ))

    btts = report["btts"]
    add("")
    add("## 4. BTTS (Both Teams To Score)")
    add(f"- Overall: **{btts['overall']['count']}** of `{btts['overall']['n_matches']}` "
        f"({fmt_pct(btts['overall']['pct'])})")
    add("")
    add(fmt_md_table(
        ["season", "matches", "BTTS", "pct"],
        [[b["season"], b["n_matches"], b["count"], fmt_pct(b["pct"])] for b in btts["per_season"]],
    ))

    cs = report["clean_sheets"]["overall"]
    add("")
    add("## 5. Clean sheets")
    add(f"- Home clean sheets: **{cs['home_clean_sheets']}** ({fmt_pct(cs['home_cs_pct'])})")
    add(f"- Away clean sheets: **{cs['away_clean_sheets']}** ({fmt_pct(cs['away_cs_pct'])})")
    add(f"- Total clean sheets recorded: **{cs['total_clean_sheets']}**")
    add(f"- Matches with at least one clean sheet: **{cs['matches_with_clean_sheet']}** "
        f"({fmt_pct(cs['matches_with_clean_sheet_pct'])})")
    add(f"- Both teams kept clean sheets (0-0): **{cs['both_clean_sheet_matches']}**")
    add("")
    add(fmt_md_table(
        ["season", "matches", "home CS", "away CS", "total CS", "matches w/ CS"],
        [
            [s["season"], s["n_matches"], s["home_clean_sheets"], s["away_clean_sheets"],
             s["total_clean_sheets"],
             f"{s['matches_with_clean_sheet']} ({fmt_pct(s['matches_with_clean_sheet_pct'])})"]
            for s in report["clean_sheets"]["per_season"]
        ],
    ))

    si = report["scoring_intensity"]["overall"]
    add("")
    add("## 6. Scoring intensity")
    add(f"- First-half goals: **{si['first_half_goals']}** ({fmt_pct(si['first_half_pct'])})")
    add(f"- Second-half goals: **{si['second_half_goals']}** ({fmt_pct(si['second_half_pct'])})")
    add(f"- Avg first-half goals per match: **{si['avg_first_half']}**")
    add(f"- Avg second-half goals per match: **{si['avg_second_half']}**")
    add(f"- Second-half-only scoring (HT 0-0, FT goals >= 1): "
        f"**{si['second_half_only']['count']}** ({fmt_pct(si['second_half_only']['pct'])})")
    if si["n_with_ht"] != si["n_matches"]:
        add(f"- *{si['n_matches'] - si['n_with_ht']} match(es) excluded (no HT score recorded).*")
    add("")
    add(fmt_md_table(
        ["season", "matches", "1st half", "2nd half", "1st half pct", "2nd half pct"],
        [
            [s["season"], s["n_matches"], s["first_half_goals"], s["second_half_goals"],
             fmt_pct(s["first_half_pct"]), fmt_pct(s["second_half_pct"])]
            for s in report["scoring_intensity"]["per_season"]
        ],
    ))

    fg = report["first_goal_timing"]
    add("")
    add("## 7. First-goal timing")
    add(f"- Matches with first-goal time recorded: `{fg['n_with_first_goal']}` "
        f"of `{fg['n_total']}` ({fmt_pct(round_pct(fg['n_with_first_goal'], fg['n_total']))})")
    add(f"- Goalless matches: `{fg['n_goalless']}`")
    if fg["summary"]:
        s = fg["summary"]
        add(f"- Min `{s['min']}` | Max `{s['max']}` | Mean `{s['mean']}` | "
            f"Median (p50) `{s['p50']}`")
    add("")
    add(fmt_md_table(
        ["bucket", "count", "% of matches", "% of scoring matches"],
        [
            [key, b["count"], fmt_pct(b["pct_of_matches"]), fmt_pct(b["pct_of_scoring"])]
            for key, b in fg["buckets"].items()
        ],
    ))
    if fg["unbucketed"]:
        add(f"- *{fg['unbucketed']} first-goal time(s) fall outside the 1-120 minute buckets.*")

    add("")
    add("---")
    add("*All statistics are computed from PostgreSQL tables (read-only). "
       "Run with `python backend/scripts/analyze_goals.py` to regenerate.*")
    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────
def parse_module_args(argv: list[str] | None = None) -> argparse.Namespace:
    return parse_args(
        "Module 2 - Goal analysis report (read-only queries).",
        argv=argv,
    )


def main(argv: list[str] | None = None) -> int:
    args = parse_module_args(argv)
    cfg = args_to_config(args)

    conn = get_conn()
    try:
        report = build_report(conn, cfg)
        conn.rollback()
    finally:
        conn.close()

    out_dir = Path(cfg["out_dir"])
    try:
        charts = build_charts(report, out_dir)
    except ImportError:
        charts = []

    stem = cfg.get("out_stem") or STEM
    json_path, md_path = write_report(out_dir, stem, report, render_markdown, charts)

    dist = report["goals_distribution"]
    print(f"{STEM} [{cfg['league']}]: {dist['n_matches']} matches, "
          f"{report['goal_share']['total_goals']} goals across "
          f"{len(report['goals_per_season'])} seasons - "
          f"wrote {json_path} and {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
