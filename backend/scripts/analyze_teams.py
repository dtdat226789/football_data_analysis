"""Module 3 - Team analysis report.

Reads `matches`, `team_seasons` / `teams`, and `standings` (classic view) from
the Football Charts analytics database *read-only* and produces a report under
data/analysis/:

    teams_analysis.json    # machine-readable report
    teams_analysis.md      # human-readable summary
    charts/teams_analysis_*.png   # top-points bar, home-advantage bar

Sections:
    1. Team standings (lifetime aggregate)
    2. Home vs away split per team (incl. home advantage)
    3. Top performers (PPG, goals, GD, goals-against rate)
    4. Team consistency (teams present in every season)
    5. Head-to-head dominance (most recurring fixtures)
    6. Position-per-season matrix

Match rows are aggregated in Python; standings supply per-season position and
the defensive (goals-against) rate. Every SQL statement is a SELECT; the
transaction is rolled back before the connection closes.

Usage:
    python backend/scripts/analyze_teams.py
    python backend/scripts/analyze_teams.py --league spain1
    python backend/scripts/analyze_teams.py --out-dir data/analysis --out-stem my_report
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict
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
    classify_outcome,
    season_sort_key,
    new_figure,
    save_chart,
)
from db_common import get_conn

STEM = "teams_analysis"
SCRIPT_NAME = "backend/scripts/analyze_teams.py"
STANDINGS_VIEW = "classic"
TOP_PAIRS = 15
TOP_PERFORMERS_N = 5

TEAM_POINTS = {"wins": 3, "draws": 1, "losses": 0}

TEAMS_QUERY = """
    SELECT DISTINCT t.id AS team_id,
                    t.canonical_name AS name,
                    t.canonical_slug AS slug
    FROM teams t
    JOIN team_seasons ts ON ts.team_id = t.id
    JOIN league_seasons ls ON ls.id = ts.league_season_id
    JOIN leagues l ON l.id = ls.league_id
    WHERE l.api_key = %s
    ORDER BY t.canonical_name
"""

MATCHES_QUERY = """
    SELECT s.name AS season,
           m.home_team_id,
           m.away_team_id,
           m.home_score,
           m.away_score
    FROM matches m
    JOIN league_seasons ls ON ls.id = m.league_season_id
    JOIN seasons s ON s.id = ls.season_id
    JOIN leagues l ON l.id = ls.league_id
    WHERE l.api_key = %s
    ORDER BY s.start_year, s.name, m.match_date, m.game_index
"""

STANDINGS_QUERY = """
    SELECT s.name AS season,
           st.team_id,
           st.position,
           st.played,
           st.goals_for,
           st.goals_against
    FROM standings st
    JOIN league_seasons ls ON ls.id = st.league_season_id
    JOIN seasons s ON s.id = ls.season_id
    JOIN leagues l ON l.id = ls.league_id
    WHERE l.api_key = %s AND st.view = %s
    ORDER BY s.start_year, s.name, st.position
"""


# ── pure helpers (unit-testable without a database) ─────────────────────────
def _empty_side() -> dict:
    return {
        "matches": 0, "wins": 0, "draws": 0, "losses": 0,
        "points": 0, "goals_for": 0, "goals_against": 0,
    }


def _new_team_records() -> dict:
    return {"home": _empty_side(), "away": _empty_side()}


def _team_outcome(outcome: str, is_home: bool) -> str:
    """Match outcome from a single team's perspective ('wins'/'draws'/'losses')."""
    if outcome == "draw":
        return "draws"
    expected = "home" if is_home else "away"
    return "wins" if outcome == expected else "losses"


def _apply_side(side: dict, scored: int, conceded: int, outcome: str) -> None:
    side["matches"] += 1
    side["goals_for"] += scored
    side["goals_against"] += conceded
    side[outcome] += 1
    side["points"] += TEAM_POINTS[outcome]


def aggregate_team_results(matches: list[dict]) -> dict[int, dict]:
    """Per-team home/away tallies derived from match rows."""
    records: dict[int, dict] = {}
    for m in matches:
        hid, aid = m["home_team_id"], m["away_team_id"]
        home = records.setdefault(hid, _new_team_records())
        away = records.setdefault(aid, _new_team_records())
        outcome = classify_outcome(m["home_score"], m["away_score"])
        _apply_side(home["home"], m["home_score"], m["away_score"],
                    _team_outcome(outcome, True))
        _apply_side(away["away"], m["away_score"], m["home_score"],
                    _team_outcome(outcome, False))
    return records


def standings_summary(standings: list[dict]) -> dict[int, dict]:
    """Per-team per-season standings facts (classic view, aggregate)."""
    by_team: dict[int, dict] = {}
    for row in standings:
        tid = row["team_id"]
        entry = by_team.setdefault(
            tid, {"seasons": set(), "positions": [],
                  "played": 0, "goals_for": 0, "goals_against": 0}
        )
        entry["seasons"].add(row["season"])
        entry["positions"].append(row["position"])
        entry["played"] += row["played"]
        entry["goals_for"] += row["goals_for"]
        entry["goals_against"] += row["goals_against"]
    return {
        tid: {
            "seasons_played": len(e["seasons"]),
            "best_position": min(e["positions"]),
            "worst_position": max(e["positions"]),
            "titles": sum(1 for p in e["positions"] if p == 1),
            "played": e["played"],
            "goals_for": e["goals_for"],
            "goals_against": e["goals_against"],
        }
        for tid, e in by_team.items()
    }


def build_lifetime(team_results: dict[int, dict],
                   standings_sum: dict[int, dict],
                   name_map: dict[int, dict]) -> list[dict]:
    ids = set(team_results) | set(standings_sum)
    rows: list[dict] = []
    for tid in ids:
        tr = team_results.get(tid, _new_team_records())
        ss = standings_sum.get(tid)
        points = tr["home"]["points"] + tr["away"]["points"]
        games = tr["home"]["matches"] + tr["away"]["matches"]
        gf = tr["home"]["goals_for"] + tr["away"]["goals_for"]
        ga = tr["home"]["goals_against"] + tr["away"]["goals_against"]
        seasons = ss["seasons_played"] if ss else 0
        rows.append({
            "team_id": tid,
            "team": name_map[tid]["name"],
            "slug": name_map[tid]["slug"],
            "seasons_played": seasons,
            "total_matches": games,
            "wins": tr["home"]["wins"] + tr["away"]["wins"],
            "draws": tr["home"]["draws"] + tr["away"]["draws"],
            "losses": tr["home"]["losses"] + tr["away"]["losses"],
            "points": points,
            "goals_for": gf,
            "goals_against": ga,
            "goal_difference": gf - ga,
            "avg_points_per_season": round(points / seasons, 2) if seasons else None,
            "best_position": ss["best_position"] if ss else None,
            "worst_position": ss["worst_position"] if ss else None,
            "titles": ss["titles"] if ss else 0,
        })
    rows.sort(key=lambda r: (-r["points"], -r["goal_difference"], r["team"]))
    return rows


def build_home_away(team_results: dict[int, dict],
                    name_map: dict[int, dict]) -> list[dict]:
    rows = []
    for tid, rec in team_results.items():
        rows.append({
            "team_id": tid,
            "team": name_map[tid]["name"],
            "home": rec["home"],
            "away": rec["away"],
            "home_advantage": rec["home"]["points"] - rec["away"]["points"],
        })
    rows.sort(key=lambda r: (-r["home_advantage"], -r["home"]["points"], r["team"]))
    return rows


def _top_n(rows: list[dict], getter, reverse: bool = True, n: int = TOP_PERFORMERS_N) -> list[dict]:
    ranked = sorted(rows, key=getter, reverse=reverse)[:n]
    return [
        {"rank": i + 1, "team_id": r["team_id"], "team": r["team"],
         "value": round(getter(r), 3)}
        for i, r in enumerate(ranked)
    ]


def build_top_performers(lifetime: list[dict],
                         standings_sum: dict[int, dict]) -> dict:
    by_id = {r["team_id"]: r for r in lifetime}
    ppg_rows = [r for r in lifetime if r["total_matches"] > 0]
    defence_rows = [
        {"team_id": tid, "team": by_id[tid]["team"],
         "value": round(st["goals_against"] / st["played"], 3)}
        for tid, st in standings_sum.items()
        if st["played"] > 0 and tid in by_id
    ]
    return {
        "best_ppg": _top_n(ppg_rows, lambda r: r["points"] / r["total_matches"]),
        "most_goals_scored": _top_n(lifetime, lambda r: r["goals_for"]),
        "best_goal_difference": _top_n(lifetime, lambda r: r["goal_difference"]),
        "best_defence": _top_n(defence_rows, lambda r: r["value"], reverse=False),
    }


def build_consistent_teams(season_names: list[str],
                           standings_sum: dict[int, dict],
                           name_map: dict[int, dict]) -> dict:
    n = len(season_names)
    present = [
        tid for tid, st in standings_sum.items()
        if st["seasons_played"] == n
    ]
    present.sort(key=lambda tid: name_map[tid]["name"])
    return {
        "n_seasons": n,
        "n_teams": len(present),
        "teams": [{"team_id": tid, "team": name_map[tid]["name"]} for tid in present],
    }


def build_head_to_head(matches: list[dict],
                       name_map: dict[int, dict],
                       top_n: int = TOP_PAIRS) -> dict:
    pairs: dict[tuple[int, int], dict[str, int]] = defaultdict(
        lambda: {"home_wins": 0, "draws": 0, "away_wins": 0}
    )
    for m in matches:
        a, b = sorted((m["home_team_id"], m["away_team_id"]))
        outcome = classify_outcome(m["home_score"], m["away_score"])
        counter = pairs[(a, b)]
        if outcome == "draw":
            counter["draws"] += 1
        else:
            counter[f"{outcome}_wins"] += 1
    items = []
    for (a, b), res in pairs.items():
        meetings = sum(res.values())
        items.append({
            "team_a_id": a,
            "team_b_id": b,
            "team_a": name_map[a]["name"],
            "team_b": name_map[b]["name"],
            "meetings": meetings,
            "home_wins": res["home_wins"],
            "draws": res["draws"],
            "away_wins": res["away_wins"],
            "home_win_pct": round_pct(res["home_wins"], meetings),
            "draw_pct": round_pct(res["draws"], meetings),
            "away_win_pct": round_pct(res["away_wins"], meetings),
        })
    items.sort(key=lambda r: (-r["meetings"], -r["home_wins"], r["team_a"], r["team_b"]))
    return {"n_pairs_total": len(items), "top_n": top_n, "pairs": items[:top_n]}


def build_position_table(season_names: list[str],
                         standings: list[dict],
                         name_map: dict[int, dict],
                         lifetime: list[dict]) -> dict:
    positions = {(row["season"], row["team_id"]): row["position"] for row in standings}
    rank = {r["team_id"]: i for i, r in enumerate(lifetime)}
    team_ids = sorted(
        {row["team_id"] for row in standings},
        key=lambda tid: (rank.get(tid, 10**9), name_map[tid]["name"]),
    )
    return {
        "seasons": season_names,
        "teams": [
            {
                "team_id": tid,
                "team": name_map[tid]["name"],
                "positions": [positions.get((season, tid)) for season in season_names],
            }
            for tid in team_ids
        ],
    }


def ordered_season_names(rows: list[dict]) -> list[str]:
    return sorted({row["season"] for row in rows}, key=season_sort_key)


# ── query layer (SELECT-only) ───────────────────────────────────────────────
def fetch_teams(cur, league: str) -> list[dict]:
    cur.execute(TEAMS_QUERY, (league,))
    return [dict(r) for r in cur.fetchall()]


def fetch_matches(cur, league: str) -> list[dict]:
    cur.execute(MATCHES_QUERY, (league,))
    return [dict(r) for r in cur.fetchall()]


def fetch_standings(cur, league: str) -> list[dict]:
    cur.execute(STANDINGS_QUERY, (league, STANDINGS_VIEW))
    return [dict(r) for r in cur.fetchall()]


# ── report assembly ──────────────────────────────────────────────────────────
def build_report(conn, cfg: dict) -> dict:
    report = report_metadata(STEM, SCRIPT_NAME, cfg)
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        teams = fetch_teams(cur, cfg["league"])
        matches = fetch_matches(cur, cfg["league"])
        standings = fetch_standings(cur, cfg["league"])

    name_map = {t["team_id"]: {"name": t["name"], "slug": t["slug"]} for t in teams}
    season_names = ordered_season_names(standings)
    results = aggregate_team_results(matches)
    ss = standings_summary(standings)
    lifetime = build_lifetime(results, ss, name_map)

    report["teams"] = lifetime
    report["home_away"] = build_home_away(results, name_map)
    report["top_performers"] = build_top_performers(lifetime, ss)
    report["consistent_teams"] = build_consistent_teams(season_names, ss, name_map)
    report["head_to_head"] = build_head_to_head(matches, name_map)
    report["position_table"] = build_position_table(season_names, standings, name_map, lifetime)
    return report


# ── charts ───────────────────────────────────────────────────────────────────
def top_points_chart(teams: list[dict]):
    fig, ax = new_figure(w=9, h=6)
    top = list(reversed(teams[:10]))
    ax.barh([t["team"] for t in top], [t["points"] for t in top], color="#4C72B0")
    ax.set_xlabel("lifetime points")
    ax.set_title("Top 10 teams by lifetime points")
    fig.tight_layout()
    return fig


def home_advantage_chart(home_away: list[dict]):
    fig, ax = new_figure(w=9, h=6)
    rows = list(reversed(sorted(home_away, key=lambda r: r["home_advantage"])))
    ax.barh([r["team"] for r in rows], [r["home_advantage"] for r in rows], color="#55A868")
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("home advantage (home points - away points)")
    ax.set_title("Home advantage per team")
    fig.tight_layout()
    return fig


def build_charts(report: dict, out_dir: Path) -> list[Path]:
    charts = [
        save_chart(out_dir, f"{STEM}_top_points", top_points_chart(report["teams"])),
        save_chart(out_dir, f"{STEM}_home_advantage", home_advantage_chart(report["home_away"])),
    ]
    return [c for c in charts if c is not None]


# ── markdown rendering ───────────────────────────────────────────────────────
def _perf_value(category: str, value) -> str:
    if value is None:
        return "-"
    if category == "best_ppg":
        return f"{value:.2f}"
    if category == "best_defence":
        return f"{value:.3f}"
    return str(value)


def render_markdown(report: dict) -> str:
    lines = render_report_header(report, "Team Analysis").splitlines()
    add = lines.append

    teams = report["teams"]
    seasons = report["position_table"]["seasons"]
    n_matches = sum(t["total_matches"] for t in teams) // 2
    add("")
    add(f"- Teams: **{len(teams)}** | Seasons: **{len(seasons)}** | "
        f"Matches: **{n_matches}**")

    add("")
    add("## 1. Team standings (lifetime)")
    add(fmt_md_table(
        ["team", "seasons", "played", "W", "D", "L", "pts", "GF", "GA", "GD",
         "avg pts/season", "best pos", "worst pos", "titles"],
        [
            [t["team"], t["seasons_played"], t["total_matches"], t["wins"],
             t["draws"], t["losses"], t["points"], t["goals_for"],
             t["goals_against"], t["goal_difference"],
             t["avg_points_per_season"] if t["avg_points_per_season"] is not None else "-",
             t["best_position"] if t["best_position"] is not None else "-",
             t["worst_position"] if t["worst_position"] is not None else "-",
             t["titles"]]
            for t in teams
        ],
    ))

    add("")
    add("## 2. Home vs away split")
    add(fmt_md_table(
        ["team", "home P", "H-W", "H-D", "H-L", "H-pts",
         "away P", "A-W", "A-D", "A-L", "A-pts", "adv"],
        [
            [r["team"],
             r["home"]["matches"], r["home"]["wins"], r["home"]["draws"],
             r["home"]["losses"], r["home"]["points"],
             r["away"]["matches"], r["away"]["wins"], r["away"]["draws"],
             r["away"]["losses"], r["away"]["points"],
             r["home_advantage"]]
            for r in report["home_away"]
        ],
    ))

    tp = report["top_performers"]
    add("")
    add("## 3. Top performers")
    add("### Best points per game (PPG)")
    add(fmt_md_table(
        ["rank", "team", "PPG"],
        [[p["rank"], p["team"], f"{p['value']:.2f}"] for p in tp["best_ppg"]],
    ))
    add("")
    add("### Most goals scored")
    add(fmt_md_table(
        ["rank", "team", "goals"],
        [[p["rank"], p["team"], p["value"]] for p in tp["most_goals_scored"]],
    ))
    add("")
    add("### Best goal difference")
    add(fmt_md_table(
        ["rank", "team", "GD"],
        [[p["rank"], p["team"], p["value"]] for p in tp["best_goal_difference"]],
    ))
    add("")
    add("### Best defence (goals against per match, standings)")
    add(fmt_md_table(
        ["rank", "team", "GA/match"],
        [[p["rank"], p["team"], f"{p['value']:.3f}"] for p in tp["best_defence"]],
    ))

    ct = report["consistent_teams"]
    add("")
    add("## 4. Team consistency")
    add(f"- Teams present in all **{ct['n_seasons']}** seasons: **{ct['n_teams']}**")
    if ct["teams"]:
        add("")
        add(", ".join(t["team"] for t in ct["teams"]))

    h2h = report["head_to_head"]
    add("")
    add("## 5. Head-to-head dominance")
    add(f"- Distinct fixtures: **{h2h['n_pairs_total']}** "
        f"(showing the {h2h['top_n']} most frequent)")
    add("")
    add(fmt_md_table(
        ["fixture", "meetings", "home wins", "draws", "away wins",
         "home pct", "draw pct", "away pct"],
        [
            [f"{p['team_a']} vs {p['team_b']}", p["meetings"],
             p["home_wins"], p["draws"], p["away_wins"],
             fmt_pct(p["home_win_pct"]), fmt_pct(p["draw_pct"]),
             fmt_pct(p["away_win_pct"])]
            for p in h2h["pairs"]
        ],
    ))

    pt = report["position_table"]
    add("")
    add("## 6. Position per season (classic view)")
    add("_Cells show final position; '-' when the team was absent from that season._")
    add("")
    add(fmt_md_table(
        ["team"] + pt["seasons"],
        [
            [t["team"]] + [pos if pos is not None else "-" for pos in t["positions"]]
            for t in pt["teams"]
        ],
    ))

    add("")
    add("---")
    add("*All statistics are computed from PostgreSQL tables (read-only). "
       "Run with `python backend/scripts/analyze_teams.py` to regenerate.*")
    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────
def parse_module_args(argv: list[str] | None = None) -> argparse.Namespace:
    return parse_args(
        "Module 3 - Team analysis report (read-only queries).",
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

    n_matches = sum(t["total_matches"] for t in report["teams"]) // 2
    print(f"{STEM} [{cfg['league']}]: {len(report['teams'])} teams, "
          f"{len(report['position_table']['seasons'])} seasons, "
          f"{n_matches} matches - "
          f"wrote {json_path} and {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
