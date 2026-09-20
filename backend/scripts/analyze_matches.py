"""Module 1 - Match analysis report.

Reads `matches` (with `league_seasons` / `seasons` / `leagues` context and
`team_seasons` names) from the Football Charts analytics database *read-only*
and produces a report under data/analysis/:

    matches_analysis.json    # machine-readable report
    matches_analysis.md      # human-readable summary
    charts/matches_analysis_*.png   # HT/FT matrix bar chart, home win-rate line

Sections:
    1. Overall summary
    2. Per-season breakdown
    3. HT/FT outcome matrix (9-cell contingency)
    4. Comeback matches (trailing at HT, winning at FT, both directions)
    5. HT lead conversion (win / held draw / collapse)
    6. First-goal timing buckets + outcome by bucket
    7. Goalless matches per season

Every SQL statement is a SELECT; the transaction is rolled back before the
connection closes.

Usage:
    python backend/scripts/analyze_matches.py
    python backend/scripts/analyze_matches.py --league spain1
    python backend/scripts/analyze_matches.py --out-dir data/analysis --out-stem my_report
"""
from __future__ import annotations

import argparse
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
    classify_outcome,
    new_figure,
    save_chart,
)
from db_common import get_conn, LEAGUE

STEM = "matches_analysis"
SCRIPT_NAME = "backend/scripts/analyze_matches.py"

OUTCOME_LABELS = ("home", "draw", "away")
FIRST_GOAL_BUCKETS = [
    (1, 15), (16, 30), (31, 45),
    (46, 60), (61, 75), (76, 90), (91, 120),
]

MATCHES_QUERY = """
    SELECT s.name AS season,
           th.api_name AS home_team,
           ta.api_name AS away_team,
           m.home_score,
           m.away_score,
           m.home_ht,
           m.away_ht,
           m.first_goal_time
    FROM matches m
    JOIN league_seasons ls ON ls.id = m.league_season_id
    JOIN seasons s ON s.id = ls.season_id
    JOIN leagues l ON l.id = ls.league_id
    JOIN team_seasons th ON th.league_season_id = ls.id AND th.team_id = m.home_team_id
    JOIN team_seasons ta ON ta.league_season_id = ls.id AND ta.team_id = m.away_team_id
    WHERE l.api_key = %s
    ORDER BY s.start_year, s.name, m.match_date, m.game_index
"""


# ── pure helpers (unit-testable without a database) ─────────────────────────
def ht_outcome(row: dict) -> str | None:
    """Half-time result ('home'/'draw'/'away') or None when missing."""
    home_ht, away_ht = row.get("home_ht"), row.get("away_ht")
    if home_ht is None or away_ht is None:
        return None
    return classify_outcome(home_ht, away_ht)


def ft_outcome(row: dict) -> str:
    return classify_outcome(row["home_score"], row["away_score"])


def first_goal_bucket(minute: int | None) -> str | None:
    if minute is None:
        return None
    for lo, hi in FIRST_GOAL_BUCKETS:
        if lo <= minute <= hi:
            return f"{lo}-{hi}"
    return None


def outcome_distribution(group: list[dict]) -> dict:
    """Counts + percentages of FT outcome within `group`."""
    n = len(group)
    dist = Counter(ft_outcome(r) for r in group)
    return {
        "n_matches": n,
        "home": {"count": dist["home"], "pct": round_pct(dist["home"], n)},
        "draw": {"count": dist["draw"], "pct": round_pct(dist["draw"], n)},
        "away": {"count": dist["away"], "pct": round_pct(dist["away"], n)},
    }


def aggregate_stats(rows: list[dict]) -> dict:
    n = len(rows)
    dist = Counter(ft_outcome(r) for r in rows)
    home_goals = sum(r["home_score"] for r in rows)
    away_goals = sum(r["away_score"] for r in rows)
    goalless = sum(1 for r in rows if r["home_score"] == 0 and r["away_score"] == 0)
    total_goals = home_goals + away_goals
    return {
        "n_matches": n,
        "home_wins": dist["home"],
        "draws": dist["draw"],
        "away_wins": dist["away"],
        "home_win_pct": round_pct(dist["home"], n),
        "draw_pct": round_pct(dist["draw"], n),
        "away_win_pct": round_pct(dist["away"], n),
        "home_goals": home_goals,
        "away_goals": away_goals,
        "total_goals": total_goals,
        "avg_goals": round(total_goals / n, 3) if n else None,
        "goalless": goalless,
        "goalless_pct": round_pct(goalless, n),
    }


def build_ht_ft_matrix(rows: list[dict]) -> dict:
    counts = {ht: {ft: 0 for ft in OUTCOME_LABELS} for ht in OUTCOME_LABELS}
    excluded = 0
    for row in rows:
        ht = ht_outcome(row)
        if ht is None:
            excluded += 1
            continue
        counts[ht][ft_outcome(row)] += 1
    pcts = {
        ht: {
            ft: round_pct(counts[ht][ft], sum(counts[ht].values()))
            for ft in OUTCOME_LABELS
        }
        for ht in OUTCOME_LABELS
    }
    return {
        "ht_states": list(OUTCOME_LABELS),
        "ft_outcomes": list(OUTCOME_LABELS),
        "counts": counts,
        "pcts": pcts,
        "excluded_no_ht": excluded,
    }


def _match_example(row: dict) -> dict:
    return {
        "season": row["season"],
        "home_team": row["home_team"],
        "away_team": row["away_team"],
        "ht_score": f"{row['home_ht']}-{row['away_ht']}",
        "ft_score": f"{row['home_score']}-{row['away_score']}",
    }


def build_comebacks(rows: list[dict]) -> dict:
    total = len(rows)
    home: list[dict] = []
    away: list[dict] = []
    for row in rows:
        ht = ht_outcome(row)
        if ht is None:
            continue
        ft = ft_outcome(row)
        if ht == "away" and ft == "home":
            home.append(_match_example(row))
        elif ht == "home" and ft == "away":
            away.append(_match_example(row))
    return {
        "home": {"count": len(home), "pct": round_pct(len(home), total), "matches": home},
        "away": {"count": len(away), "pct": round_pct(len(away), total), "matches": away},
    }


def build_ht_lead_conversion(rows: list[dict]) -> dict:
    groups = {"home_lead": "home", "ht_draw": "draw", "away_lead": "away"}
    out = {}
    for group_key, ht_state in groups.items():
        out[group_key] = outcome_distribution(
            [r for r in rows if ht_outcome(r) == ht_state]
        )
    out["excluded_no_ht"] = sum(1 for r in rows if ht_outcome(r) is None)
    return out


def build_first_goal_timing(rows: list[dict]) -> dict:
    n_total = len(rows)
    n_with_fgt = sum(1 for r in rows if r["first_goal_time"] is not None)
    buckets: dict[str, dict] = {}
    for lo, hi in FIRST_GOAL_BUCKETS:
        key = f"{lo}-{hi}"
        group = [
            r for r in rows
            if r["first_goal_time"] is not None and lo <= r["first_goal_time"] <= hi
        ]
        dist = outcome_distribution(group)
        buckets[key] = {
            **dist,
            "pct_of_matches": round_pct(dist["n_matches"], n_total),
        }
    return {
        "n_total": n_total,
        "n_with_first_goal": n_with_fgt,
        "n_goalless": n_total - n_with_fgt,
        "unbucketed": n_with_fgt - sum(b["n_matches"] for b in buckets.values()),
        "buckets": buckets,
    }


def build_goalless_section(overall: dict, per_season: list[dict]) -> dict:
    return {
        "overall": {
            "n_matches": overall["n_matches"],
            "count": overall["goalless"],
            "pct": overall["goalless_pct"],
        },
        "per_season": [
            {
                "season": s["season"],
                "n_matches": s["n_matches"],
                "count": s["goalless"],
                "pct": s["goalless_pct"],
            }
            for s in per_season
        ],
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

    order: list[str] = []
    for row in rows:
        if row["season"] not in order:
            order.append(row["season"])

    overall = aggregate_stats(rows)
    per_season = [
        {"season": season, **aggregate_stats([r for r in rows if r["season"] == season])}
        for season in order
    ]

    report["overall"] = overall
    report["per_season"] = per_season
    report["ht_ft_matrix"] = build_ht_ft_matrix(rows)
    report["comebacks"] = build_comebacks(rows)
    report["ht_lead_conversion"] = build_ht_lead_conversion(rows)
    report["first_goal_timing"] = build_first_goal_timing(rows)
    report["goalless"] = build_goalless_section(overall, per_season)
    return report


# ── charts ───────────────────────────────────────────────────────────────────
def ht_ft_matrix_chart(matrix: dict):
    fig, ax = new_figure(w=9, h=5)
    short = {"home": "H", "draw": "D", "away": "A"}
    labels = [
        f"{short[ht]}>{short[ft]}"
        for ht in matrix["ht_states"]
        for ft in matrix["ft_outcomes"]
    ]
    values = [
        matrix["counts"][ht][ft]
        for ht in matrix["ht_states"]
        for ft in matrix["ft_outcomes"]
    ]
    ax.bar(labels, values, color="#4C72B0")
    ax.set_ylabel("matches")
    ax.set_xlabel("HT result -> FT outcome")
    ax.set_title("HT/FT outcome matrix")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig


def home_win_rate_chart(per_season: list[dict]):
    fig, ax = new_figure(w=8, h=5)
    seasons = [s["season"] for s in per_season]
    pcts = [s["home_win_pct"] if s["home_win_pct"] is not None else 0.0 for s in per_season]
    ax.plot(seasons, pcts, marker="o", color="#C44E52")
    ax.set_ylabel("home win rate (%)")
    ax.set_xlabel("season")
    ax.set_title("Home win rate per season")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.set_ylim(0, None)
    fig.tight_layout()
    return fig


def build_charts(report: dict, out_dir: Path) -> list[Path]:
    charts = [
        save_chart(out_dir, f"{STEM}_ht_ft_matrix", ht_ft_matrix_chart(report["ht_ft_matrix"])),
        save_chart(out_dir, f"{STEM}_home_win_rate", home_win_rate_chart(report["per_season"])),
    ]
    return [c for c in charts if c is not None]


# ── markdown rendering ───────────────────────────────────────────────────────
FT_LABEL = {"home": "Home", "draw": "Draw", "away": "Away"}
HT_LABEL = {"home": "HT home lead", "draw": "HT draw", "away": "HT away lead"}


def render_markdown(report: dict) -> str:
    lines = render_report_header(report, "Match Analysis").splitlines()
    add = lines.append

    ov = report["overall"]
    add("")
    add("## 1. Overall summary")
    add(fmt_md_table(
        ["metric", "value"],
        [
            ["Matches", ov["n_matches"]],
            ["Home wins", f"{ov['home_wins']} ({fmt_pct(ov['home_win_pct'])})"],
            ["Draws", f"{ov['draws']} ({fmt_pct(ov['draw_pct'])})"],
            ["Away wins", f"{ov['away_wins']} ({fmt_pct(ov['away_win_pct'])})"],
            ["Total goals", ov["total_goals"]],
            ["Average goals per match",
             f"{ov['avg_goals']:.3f}" if ov["avg_goals"] is not None else "-"],
            ["Goalless matches", f"{ov['goalless']} ({fmt_pct(ov['goalless_pct'])})"],
        ],
    ))

    add("")
    add("## 2. Per-season breakdown")
    add(fmt_md_table(
        ["season", "matches", "home wins", "draws", "away wins",
         "total goals", "avg goals", "goalless"],
        [
            [
                s["season"], s["n_matches"],
                f"{s['home_wins']} ({fmt_pct(s['home_win_pct'])})",
                f"{s['draws']} ({fmt_pct(s['draw_pct'])})",
                f"{s['away_wins']} ({fmt_pct(s['away_win_pct'])})",
                s["total_goals"],
                s["avg_goals"] if s["avg_goals"] is not None else "-",
                f"{s['goalless']} ({fmt_pct(s['goalless_pct'])})",
            ]
            for s in report["per_season"]
        ],
    ))

    mx = report["ht_ft_matrix"]
    add("")
    add("## 3. HT/FT outcome matrix")
    add(fmt_md_table(
        ["HT result \\ FT result"] + [FT_LABEL[ft] for ft in mx["ft_outcomes"]] + ["total"],
        [
            [HT_LABEL[ht]]
            + [f"{mx['counts'][ht][ft]} ({fmt_pct(mx['pcts'][ht][ft])})" for ft in mx["ft_outcomes"]]
            + [sum(mx["counts"][ht].values())]
            for ht in mx["ht_states"]
        ],
    ))
    if mx["excluded_no_ht"]:
        add(f"- *{mx['excluded_no_ht']} match(es) excluded (no HT score recorded).*")

    cb = report["comebacks"]
    add("")
    add("## 4. Comeback matches")
    add(f"- Home comebacks (trailing at HT, won at FT): **{cb['home']['count']}** "
        f"({fmt_pct(cb['home']['pct'])})")
    add(f"- Away comebacks (trailing at HT, won at FT): **{cb['away']['count']}** "
        f"({fmt_pct(cb['away']['pct'])})")
    for side, title in (("home", "Home comebacks"), ("away", "Away comebacks")):
        entry = cb[side]
        if not entry["matches"]:
            continue
        add("")
        add(f"### {title}")
        add(fmt_md_table(
            ["season", "home", "away", "HT", "FT"],
            [
                [m["season"], m["home_team"], m["away_team"], m["ht_score"], m["ft_score"]]
                for m in entry["matches"]
            ],
        ))

    conv = report["ht_lead_conversion"]
    add("")
    add("## 5. HT lead conversion")
    add(fmt_md_table(
        ["HT state", "matches", "converted to win", "held as draw", "collapsed to loss"],
        [
            ["Home lead", conv["home_lead"]["n_matches"],
             f"{conv['home_lead']['home']['count']} ({fmt_pct(conv['home_lead']['home']['pct'])})",
             f"{conv['home_lead']['draw']['count']} ({fmt_pct(conv['home_lead']['draw']['pct'])})",
             f"{conv['home_lead']['away']['count']} ({fmt_pct(conv['home_lead']['away']['pct'])})"],
            ["Away lead", conv["away_lead"]["n_matches"],
             f"{conv['away_lead']['away']['count']} ({fmt_pct(conv['away_lead']['away']['pct'])})",
             f"{conv['away_lead']['draw']['count']} ({fmt_pct(conv['away_lead']['draw']['pct'])})",
             f"{conv['away_lead']['home']['count']} ({fmt_pct(conv['away_lead']['home']['pct'])})"],
        ],
    ))
    add("")
    add("### Matches level at half-time")
    add(fmt_md_table(
        ["FT result", "count", "pct"],
        [
            ["Home win", conv["ht_draw"]["home"]["count"], fmt_pct(conv["ht_draw"]["home"]["pct"])],
            ["Draw", conv["ht_draw"]["draw"]["count"], fmt_pct(conv["ht_draw"]["draw"]["pct"])],
            ["Away win", conv["ht_draw"]["away"]["count"], fmt_pct(conv["ht_draw"]["away"]["pct"])],
        ],
    ))
    if conv["excluded_no_ht"]:
        add(f"- *{conv['excluded_no_ht']} match(es) excluded (no HT score recorded).*")

    fg = report["first_goal_timing"]
    add("")
    add("## 6. First-goal timing")
    add(f"- Matches with a first-goal time recorded: `{fg['n_with_first_goal']}` of "
        f"`{fg['n_total']}` ({fmt_pct(round_pct(fg['n_with_first_goal'], fg['n_total']))})")
    add("")
    add("Outcome distribution by first-goal timing bucket:")
    add(fmt_md_table(
        ["bucket", "matches", "% of matches", "home", "draw", "away"],
        [
            [key,
             b["n_matches"],
             fmt_pct(b["pct_of_matches"]),
             f"{b['home']['count']} ({fmt_pct(b['home']['pct'])})",
             f"{b['draw']['count']} ({fmt_pct(b['draw']['pct'])})",
             f"{b['away']['count']} ({fmt_pct(b['away']['pct'])})"]
            for key, b in fg["buckets"].items()
        ],
    ))
    if fg["unbucketed"]:
        add(f"- *{fg['unbucketed']} first-goal time(s) fall outside the 1-120 minute buckets.*")

    gl = report["goalless"]
    add("")
    add("## 7. Goalless matches")
    add(f"- Overall: **{gl['overall']['count']}** of `{gl['overall']['n_matches']}` "
        f"({fmt_pct(gl['overall']['pct'])})")
    add("")
    add(fmt_md_table(
        ["season", "matches", "goalless", "pct"],
        [[g["season"], g["n_matches"], g["count"], fmt_pct(g["pct"])] for g in gl["per_season"]],
    ))

    add("")
    add("---")
    add("*All statistics are computed from PostgreSQL tables (read-only). "
       "Run with `python backend/scripts/analyze_matches.py` to regenerate.*")
    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────
def parse_module_args(argv: list[str] | None = None) -> argparse.Namespace:
    return parse_args(
        "Module 1 - Match analysis report (read-only queries).",
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

    ov = report["overall"]
    print(f"{STEM} [{cfg['league']}]: {ov['n_matches']} matches, "
          f"{ov['total_goals']} goals (avg {ov['avg_goals']}), "
          f"{ov['goalless']} goalless - wrote {json_path} and {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())