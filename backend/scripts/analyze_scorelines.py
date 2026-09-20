"""Module 5 - Scoreline analysis report.

Reads `matches` (with `league_seasons` / `seasons` / `leagues` context) from the
Football Charts analytics database *read-only* and produces a report under
data/analysis/:

    scoreline_analysis.json    # machine-readable report
    scoreline_analysis.md      # human-readable summary
    charts/scoreline_analysis_*.png   # top-scorelines bar, total-goal histogram

Sections:
    1. Scoreline frequency (top ~20 across all seasons)
    2. Scoreline frequency per season (top 5 per season)
    3. Total-goal histogram (0..10+ buckets)
    4. Extreme scorelines (>= 7 total goals)
    5. Margin-of-victory distribution (decided matches: 1, 2, 3+)
    6. Margin by outcome (home wins / away wins, listed then aggregated in Python)
    7. Most common exact score by outcome type (home / draw / away)

Every SQL statement is a SELECT; the transaction is rolled back before the
connection closes.

Usage:
    python backend/scripts/analyze_scorelines.py
    python backend/scripts/analyze_scorelines.py --league spain1
    python backend/scripts/analyze_scorelines.py --out-dir data/analysis --out-stem my_report
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
    VERSION,
    parse_args,
    args_to_config,
    report_metadata,
    write_report,
    fmt_pct,
    fmt_md_table,
    render_report_header,
    round_pct,
    season_sort_key,
    new_figure,
    save_chart,
)
from db_common import get_conn, LEAGUE

STEM = "scoreline_analysis"
SCRIPT_NAME = "backend/scripts/analyze_scorelines.py"

TOP_SCORELINES = 20
TOP_PER_SEASON = 5
HISTOGRAM_CAP = 10
MIN_TOTAL_GOALS = 7
MARGIN_CAP = 3
OUTCOMES = ("home", "draw", "away")

MATCHES_QUERY = """
    SELECT s.name AS season,
           m.home_score,
           m.away_score,
           m.match_date
    FROM matches m
    JOIN league_seasons ls ON ls.id = m.league_season_id
    JOIN seasons s ON s.id = ls.season_id
    JOIN leagues l ON l.id = ls.league_id
    WHERE l.api_key = %s
    ORDER BY s.start_year, s.name, m.match_date, m.game_index
"""


# ── pure helpers (unit-testable without a database) ─────────────────────────
def classify_outcome(home: int, away: int) -> str:
    if home > away:
        return "home"
    if home == away:
        return "draw"
    return "away"


def scoreline_key(home: int, away: int) -> str:
    return f"{home}-{away}"


def total_goals(row: dict) -> int:
    return row["home_score"] + row["away_score"]


def goal_margin(row: dict) -> int:
    return abs(row["home_score"] - row["away_score"])


def season_order(rows: list[dict]) -> list[str]:
    seen: list[str] = []
    for row in rows:
        if row["season"] not in seen:
            seen.append(row["season"])
    return sorted(seen, key=season_sort_key)


def _top_scorelines(group: list[dict], top_n: int) -> list[dict]:
    counts = Counter(scoreline_key(r["home_score"], r["away_score"]) for r in group)
    n = len(group)
    return [
        {"scoreline": key, "count": c, "pct": round_pct(c, n)}
        for key, c in counts.most_common(top_n)
    ]


def _margin_distribution(group: list[dict]) -> list[dict]:
    n = len(group)
    capsules = Counter(min(goal_margin(r), MARGIN_CAP) for r in group)
    return [
        {
            "margin": m,
            "label": str(m) if m < MARGIN_CAP else f"{MARGIN_CAP}+",
            "count": capsules.get(m, 0),
            "pct": round_pct(capsules.get(m, 0), n),
        }
        for m in range(1, MARGIN_CAP + 1)
    ]


def build_scoreline_frequency(rows: list[dict], top_n: int = TOP_SCORELINES) -> dict:
    counts = Counter(scoreline_key(r["home_score"], r["away_score"]) for r in rows)
    n = len(rows)
    return {
        "n_matches": n,
        "n_distinct_scorelines": len(counts),
        "top": [{"scoreline": key, "count": c, "pct": round_pct(c, n)}
                for key, c in counts.most_common(top_n)],
    }


def build_scoreline_per_season(rows: list[dict], top_n: int = TOP_PER_SEASON) -> list[dict]:
    return [
        {"season": season, "top": _top_scorelines(
            [r for r in rows if r["season"] == season], top_n)}
        for season in season_order(rows)
    ]


def build_total_goal_histogram(rows: list[dict], cap: int = HISTOGRAM_CAP) -> dict:
    counts = Counter(min(total_goals(r), cap) for r in rows)
    n = len(rows)
    buckets = [
        {
            "goals": g,
            "label": str(g) if g < cap else f"{cap}+",
            "count": counts.get(g, 0),
            "pct": round_pct(counts.get(g, 0), n),
        }
        for g in range(cap + 1)
    ]
    return {"n_matches": n, "cap": cap, "buckets": buckets}


def build_extreme_scorelines(rows: list[dict], min_total: int = MIN_TOTAL_GOALS) -> dict:
    matches = [
        {
            "season": r["season"],
            "home_score": r["home_score"],
            "away_score": r["away_score"],
            "scoreline": scoreline_key(r["home_score"], r["away_score"]),
            "total_goals": total_goals(r),
            "match_date": r.get("match_date"),
        }
        for r in rows if total_goals(r) >= min_total
    ]
    matches.sort(key=lambda m: m["total_goals"], reverse=True)
    return {"min_total": min_total, "count": len(matches), "matches": matches}


def build_margin_distribution(rows: list[dict]) -> dict:
    decided = [r for r in rows if r["home_score"] != r["away_score"]]
    n = len(decided)
    return {
        "n_decided": n,
        "n_draws": len(rows) - n,
        "avg_margin": round(statistics.fmean(goal_margin(r) for r in decided), 2) if decided else None,
        "distribution": _margin_distribution(decided),
    }


def _margin_by_outcome(rows: list[dict], outcome: str) -> dict:
    group = [r for r in rows if classify_outcome(r["home_score"], r["away_score"]) == outcome]
    margins = sorted(goal_margin(r) for r in group)
    return {
        "n_matches": len(group),
        "matches": [
            {
                "season": r["season"],
                "home_score": r["home_score"],
                "away_score": r["away_score"],
                "scoreline": scoreline_key(r["home_score"], r["away_score"]),
                "margin": goal_margin(r),
                "match_date": r.get("match_date"),
            }
            for r in group
        ],
        "distribution": _margin_distribution(group),
        "avg_margin": round(statistics.fmean(margins), 2) if margins else None,
        "max_margin": margins[-1] if margins else None,
    }


def build_margin_by_outcome(rows: list[dict]) -> dict:
    return {outcome: _margin_by_outcome(rows, outcome) for outcome in ("home", "away")}


def build_common_scorelines(rows: list[dict]) -> dict:
    result: dict = {}
    for outcome in OUTCOMES:
        group = [r for r in rows if classify_outcome(r["home_score"], r["away_score"]) == outcome]
        n = len(group)
        counts = Counter(scoreline_key(r["home_score"], r["away_score"]) for r in group)
        entry: dict = {"n_matches": n}
        most = counts.most_common(1)
        if most:
            key, count = most[0]
            entry.update({"scoreline": key, "count": count, "pct": round_pct(count, n)})
        else:
            entry.update({"scoreline": None, "count": 0, "pct": None})
        result[outcome] = entry
    return result


# ── query layer (SELECT-only) ───────────────────────────────────────────────
def fetch_matches(cur, league: str) -> list[dict]:
    cur.execute(MATCHES_QUERY, (league,))
    return [dict(r) for r in cur.fetchall()]


# ── report assembly ──────────────────────────────────────────────────────────
def build_report(conn, cfg: dict) -> dict:
    report = report_metadata(STEM, SCRIPT_NAME, cfg)
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        rows = fetch_matches(cur, cfg["league"])

    report["scoreline_frequency"] = build_scoreline_frequency(rows)
    report["scoreline_per_season"] = build_scoreline_per_season(rows)
    report["total_goal_histogram"] = build_total_goal_histogram(rows)
    report["extreme_scorelines"] = build_extreme_scorelines(rows)
    report["margin_distribution"] = build_margin_distribution(rows)
    report["margin_by_outcome"] = build_margin_by_outcome(rows)
    report["common_scorelines"] = build_common_scorelines(rows)
    return report


# ── charts ───────────────────────────────────────────────────────────────────
def top_scorelines_chart(freq: dict):
    fig, ax = new_figure(w=9, h=5)
    top = freq["top"][:15]
    labels = [t["scoreline"] for t in top]
    values = [t["count"] for t in top]
    ax.bar(labels, values, color="#4C72B0")
    ax.set_ylabel("matches")
    ax.set_xlabel("scoreline (home-away)")
    ax.set_title(f"Top {len(top)} scorelines")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig


def total_goal_histogram_chart(hist: dict):
    fig, ax = new_figure(w=8, h=5)
    labels = [b["label"] for b in hist["buckets"]]
    values = [b["count"] for b in hist["buckets"]]
    ax.bar(labels, values, color="#55A868")
    ax.set_ylabel("matches")
    ax.set_xlabel("total goals per match")
    ax.set_title(f"Total goals per match distribution ({HISTOGRAM_CAP}+ capped)")
    fig.tight_layout()
    return fig


def build_charts(report: dict, out_dir: Path) -> list[Path]:
    charts = [
        save_chart(out_dir, f"{STEM}_top_scorelines", top_scorelines_chart(report["scoreline_frequency"])),
        save_chart(out_dir, f"{STEM}_total_goals", total_goal_histogram_chart(report["total_goal_histogram"])),
    ]
    return [c for c in charts if c is not None]


# ── markdown rendering ───────────────────────────────────────────────────────
def render_markdown(report: dict) -> str:
    lines = render_report_header(report, "Scoreline Analysis").splitlines()
    add = lines.append

    sf = report["scoreline_frequency"]
    add("")
    add("## 1. Scoreline frequency")
    add(f"- Matches analysed: **{sf['n_matches']}** across "
        f"**{len(report['scoreline_per_season'])}** seasons.")
    add(f"- Distinct scorelines seen: **{sf['n_distinct_scorelines']}**.")
    add("")
    add(fmt_md_table(
        ["scoreline", "count", "pct"],
        [[s["scoreline"], s["count"], fmt_pct(s["pct"])] for s in sf["top"]],
    ))

    add("")
    add("## 2. Scoreline frequency per season")
    for entry in report["scoreline_per_season"]:
        add("")
        add(f"### {entry['season']}")
        add(fmt_md_table(
            ["scoreline", "count", "pct"],
            [[s["scoreline"], s["count"], fmt_pct(s["pct"])] for s in entry["top"]],
        ))

    th = report["total_goal_histogram"]
    add("")
    add("## 3. Total-goal histogram")
    add(f"_{HISTOGRAM_CAP}+ groups all matches with {HISTOGRAM_CAP} or more total goals._")
    add("")
    add(fmt_md_table(
        ["total goals", "matches", "pct"],
        [[b["label"], b["count"], fmt_pct(b["pct"])] for b in th["buckets"]],
    ))

    ex = report["extreme_scorelines"]
    add("")
    add("## 4. Extreme scorelines")
    add(f"- Matches with {ex['min_total']}+ total goals: **{ex['count']}**")
    if ex["matches"]:
        add("")
        add(fmt_md_table(
            ["season", "date", "scoreline", "total goals"],
            [
                [m["season"], m["match_date"] or "-", m["scoreline"], m["total_goals"]]
                for m in ex["matches"]
            ],
        ))

    md = report["margin_distribution"]
    add("")
    add("## 5. Margin-of-victory distribution (decided matches)")
    add(f"- Decided matches: **{md['n_decided']}** (draws: **{md['n_draws']}**)")
    add(f"- Average winning margin: **{md['avg_margin']}**" if md["avg_margin"] is not None else "-")
    add("")
    add(fmt_md_table(
        ["margin", "matches", "pct"],
        [[b["label"], b["count"], fmt_pct(b["pct"])] for b in md["distribution"]],
    ))

    add("")
    add("## 6. Margin by outcome")
    for outcome in ("home", "away"):
        body = report["margin_by_outcome"][outcome]
        title = "Home wins" if outcome == "home" else "Away wins"
        add("")
        add(f"### {title}")
        add(f"- Matches: **{body['n_matches']}** | avg margin: **{body['avg_margin']}** | "
            f"max margin: **{body['max_margin']}**")
        add(fmt_md_table(
            ["margin", "matches", "pct"],
            [[b["label"], b["count"], fmt_pct(b["pct"])] for b in body["distribution"]],
        ))
        add(f"- *Full match-by-match list available in `{STEM}.json`.*")

    add("")
    add("## 7. Most common exact score by outcome type")
    rows: list[list] = []
    for outcome in OUTCOMES:
        body = report["common_scorelines"][outcome]
        rows.append([
            outcome,
            body["n_matches"],
            body["scoreline"] if body["scoreline"] else "-",
            body["count"],
            fmt_pct(body["pct"]),
        ])
    add(fmt_md_table(["outcome", "matches", "most common score", "count", "pct"], rows))

    add("")
    add("---")
    add("*All statistics are computed from PostgreSQL tables (read-only). "
       "Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*")
    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────
def parse_module_args(argv: list[str] | None = None) -> argparse.Namespace:
    return parse_args(
        "Module 5 - Scoreline analysis report (read-only queries).",
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

    sf = report["scoreline_frequency"]
    print(f"{STEM} [{cfg['league']}]: {sf['n_matches']} matches, "
          f"{sf['n_distinct_scorelines']} distinct scorelines across "
          f"{len(report['scoreline_per_season'])} seasons, "
          f"{report['extreme_scorelines']['count']} with 7+ goals - "
          f"wrote {json_path} and {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())