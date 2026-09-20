"""Module 4 - Season-by-season trends analysis report.

Reads `matches`, `standings` (all views), and `team_seasons` from the Football
Charts analytics database *read-only* and produces a report under data/analysis/:

    season_trends.json    # machine-readable report
    season_trends.md      # human-readable summary
    charts/season_trends_*.png   # champion-points line, avg-goals line

Sections:
    1. Champions per season
    2. Title-race tightness
    3. Points thresholds
    4. Relegation battle
    5. League-level trends
    6. View divergence (classic vs luck/goals)

Every SQL statement is a SELECT; the transaction is rolled back before the
connection closes.

Usage:
    python backend/scripts/analyze_seasons.py
    python backend/scripts/analyze_seasons.py --league spain1
    python backend/scripts/analyze_seasons.py --out-dir data/analysis --out-stem my_report
"""
from __future__ import annotations

import argparse
import sys
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
from db_common import get_conn, LEAGUE, league_meta

STEM = "season_trends"
SCRIPT_NAME = "backend/scripts/analyze_seasons.py"
CLASSIC_VIEW = "classic"
ALT_VIEWS = ["luck", "goals"]

MATCHES_QUERY = """
    SELECT s.name AS season,
           m.home_score,
           m.away_score
    FROM matches m
    JOIN league_seasons ls ON ls.id = m.league_season_id
    JOIN seasons s ON s.id = ls.season_id
    JOIN leagues l ON l.id = ls.league_id
    WHERE l.api_key = %s
    ORDER BY s.start_year, s.name, m.match_date, m.game_index
"""

STANDINGS_ALL_QUERY = """
    SELECT s.name AS season,
           st.team_id,
           st.view,
           st.position,
           st.points,
           st.played,
           st.won,
           st.drawn,
           st.lost,
           st.goals_for,
           st.goals_against,
           st.goal_difference
    FROM standings st
    JOIN league_seasons ls ON ls.id = st.league_season_id
    JOIN seasons s ON s.id = ls.season_id
    JOIN leagues l ON l.id = ls.league_id
    WHERE l.api_key = %s
    ORDER BY s.start_year, s.name, st.view, st.position
"""

TEAM_NAMES_QUERY = """
    SELECT DISTINCT t.id AS team_id,
                    t.canonical_name AS name
    FROM teams t
    JOIN team_seasons ts ON ts.team_id = t.id
    JOIN league_seasons ls ON ls.id = ts.league_season_id
    JOIN leagues l ON l.id = ls.league_id
    WHERE l.api_key = %s
"""


# ── pure helpers (unit-testable without a database) ─────────────────────────
def classify_outcome(home: int, away: int) -> str:
    if home > away:
        return "home"
    if home == away:
        return "draw"
    return "away"


def _season_order(rows: list[dict]) -> list[str]:
    seen: list[str] = []
    for row in rows:
        if row["season"] not in seen:
            seen.append(row["season"])
    return sorted(seen, key=season_sort_key)


def _pos_at(classic_rows: list[dict], season: str, pos: int) -> dict | None:
    for r in classic_rows:
        if r["season"] == season and r["position"] == pos:
            return r
    return None


def build_champions(classic_rows: list[dict],
                    name_map: dict[int, str]) -> list[dict]:
    seasons = _season_order(classic_rows)
    entries: list[dict] = []
    for season in seasons:
        first = _pos_at(classic_rows, season, 1)
        second = _pos_at(classic_rows, season, 2)
        if first is None:
            entries.append({"season": season, "champion": None, "runner_up": None,
                            "margin_pts": None, "champion_pts": None})
            continue
        margin = None
        if second is not None:
            margin = first["points"] - second["points"]
        entries.append({
            "season": season,
            "champion": name_map.get(first["team_id"], f"team_{first['team_id']}"),
            "champion_id": first["team_id"],
            "champion_pts": first["points"],
            "runner_up": name_map.get(second["team_id"], f"team_{second['team_id']}") if second else None,
            "runner_up_id": second["team_id"] if second else None,
            "margin_pts": margin,
        })
    return entries


def build_title_race(champions: list[dict]) -> dict:
    margins = [c for c in champions if c["margin_pts"] is not None]
    tight = [c for c in margins if c["margin_pts"] <= 3]
    tightest = min(margins, key=lambda c: c["margin_pts"]) if margins else None
    return {
        "per_season": [
            {"season": c["season"], "margin": c["margin_pts"],
             "tight": c["margin_pts"] is not None and c["margin_pts"] <= 3}
            for c in margins
        ],
        "tight_race_count": len(tight),
        "total_seasons": len(margins),
        "tightest": {
            "season": tightest["season"],
            "margin": tightest["margin_pts"],
            "champion": tightest["champion"],
            "runner_up": tightest["runner_up"],
        } if tightest else None,
    }


THRESHOLD_POSITIONS = [1, 2, 4, 6]


def build_points_thresholds(classic_rows: list[dict],
                            n_teams: int) -> list[dict]:
    seasons = _season_order(classic_rows)
    positions = list(THRESHOLD_POSITIONS) + [n_teams - 3, n_teams]
    entries: list[dict] = []
    for season in seasons:
        s_rows = [r for r in classic_rows if r["season"] == season]
        pos_map: dict[str, int | None] = {}
        for pos in positions:
            entry = next((r for r in s_rows if r["position"] == pos), None)
            pos_map[str(pos)] = entry["points"] if entry else None
        entries.append({"season": season, "positions": pos_map})
    return entries


def build_relegation_battle(classic_rows: list[dict],
                            n_teams: int) -> list[dict]:
    seasons = _season_order(classic_rows)
    entries: list[dict] = []
    for season in seasons:
        rows = [r for r in classic_rows if r["season"] == season]
        safe_pos = n_teams - 3
        drop_pos = n_teams - 2
        entry_safe = next((r for r in rows if r["position"] == safe_pos), None)
        entry_drop = next((r for r in rows if r["position"] == drop_pos), None)
        pts_safe = entry_safe["points"] if entry_safe else None
        pts_drop = entry_drop["points"] if entry_drop else None
        gap = (pts_safe - pts_drop) if pts_safe is not None and pts_drop is not None else None
        bottom3: list[dict | None] = []
        for pos in range(n_teams - 2, n_teams + 1):
            e = next((r for r in rows if r["position"] == pos), None)
            bottom3.append({"position": pos, "points": e["points"] if e else None})
        bottom3_range = None
        valid = [b for b in bottom3 if b["points"] is not None]
        if len(valid) >= 2:
            bottom3_range = max(b["points"] for b in valid) - min(b["points"] for b in valid)
        entries.append({
            "season": season,
            "safe_position": safe_pos,
            "safe_pts": pts_safe,
            "drop_position": drop_pos,
            "drop_pts": pts_drop,
            "gap": gap,
            "bottom3": bottom3,
            "bottom3_range": bottom3_range,
        })
    return entries


def build_league_trends(match_rows: list[dict],
                        classic_rows: list[dict],
                        n_teams: int) -> list[dict]:
    seasons = _season_order(match_rows)
    entries: list[dict] = []
    for season in seasons:
        matches = [r for r in match_rows if r["season"] == season]
        n = len(matches)
        home_wins = sum(1 for r in matches if r["home_score"] > r["away_score"])
        draws = sum(1 for r in matches if r["home_score"] == r["away_score"])
        away_wins = sum(1 for r in matches if r["home_score"] < r["away_score"])
        goalless = sum(1 for r in matches if r["home_score"] == 0 and r["away_score"] == 0)
        total_goals = sum(r["home_score"] + r["away_score"] for r in matches)
        classic_season = [r for r in classic_rows if r["season"] == season]
        total_points = sum(r["points"] for r in classic_season)
        teams_in = len(classic_season) if classic_season else n_teams
        entries.append({
            "season": season,
            "n_matches": n,
            "total_goals": total_goals,
            "avg_goals": round(total_goals / n, 3) if n else None,
            "home_wins": home_wins,
            "draws": draws,
            "away_wins": away_wins,
            "home_win_pct": round_pct(home_wins, n),
            "draw_pct": round_pct(draws, n),
            "away_win_pct": round_pct(away_wins, n),
            "goalless": goalless,
            "goalless_pct": round_pct(goalless, n),
            "total_points": total_points,
            "avg_points_per_team": round(total_points / teams_in, 2) if teams_in else None,
            "n_teams": teams_in,
        })
    return entries


def build_view_divergence(all_rows: list[dict]) -> dict:
    seasons = _season_order(all_rows)
    per_season: list[dict] = []
    for season in seasons:
        s_rows = [r for r in all_rows if r["season"] == season]
        classic = {r["team_id"]: r["position"] for r in s_rows if r["view"] == CLASSIC_VIEW}
        divergences: dict[str, float | None] = {}
        for view in ALT_VIEWS:
            alt = {r["team_id"]: r["position"] for r in s_rows if r["view"] == view}
            shared = set(classic) & set(alt)
            if shared:
                avg_diff = sum(abs(classic[t] - alt[t]) for t in shared) / len(shared)
                divergences[view] = round(avg_diff, 3)
            else:
                divergences[view] = None
        per_season.append({"season": season, **divergences})
    worst_season: dict | None = None
    worst_val = -1.0
    for entry in per_season:
        for view in ALT_VIEWS:
            val = entry.get(view)
            if val is not None and val > worst_val:
                worst_val = val
                worst_season = {"season": entry["season"], "view": view, "avg_abs_diff": val}
    return {"per_season": per_season, "worst_divergence": worst_season}


# ── query layer (SELECT-only) ───────────────────────────────────────────────
def fetch_matches(cur, league: str) -> list[dict]:
    cur.execute(MATCHES_QUERY, (league,))
    return [dict(r) for r in cur.fetchall()]


def fetch_all_standings(cur, league: str) -> list[dict]:
    cur.execute(STANDINGS_ALL_QUERY, (league,))
    return [dict(r) for r in cur.fetchall()]


def fetch_team_names(cur, league: str) -> dict[int, str]:
    cur.execute(TEAM_NAMES_QUERY, (league,))
    return {r["team_id"]: r["name"] for r in cur.fetchall()}


# ── report assembly ──────────────────────────────────────────────────────────
def build_report(conn, cfg: dict) -> dict:
    meta = league_meta(cfg["league"])
    n_teams = meta.get("teams", 20)
    report = report_metadata(STEM, SCRIPT_NAME, cfg)
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        match_rows = fetch_matches(cur, cfg["league"])
        all_standings = fetch_all_standings(cur, cfg["league"])
        name_map = fetch_team_names(cur, cfg["league"])

    classic_rows = [r for r in all_standings if r["view"] == CLASSIC_VIEW]

    champions = build_champions(classic_rows, name_map)
    report["champions"] = champions
    report["title_race"] = build_title_race(champions)
    report["points_thresholds"] = build_points_thresholds(classic_rows, n_teams)
    report["relegation_battle"] = build_relegation_battle(classic_rows, n_teams)
    report["league_trends"] = build_league_trends(match_rows, classic_rows, n_teams)
    report["view_divergence"] = build_view_divergence(all_standings)
    return report


# ── charts ───────────────────────────────────────────────────────────────────
def champion_points_chart(champions: list[dict]):
    fig, ax = new_figure(w=8, h=5)
    seasons = [c["season"] for c in champions if c["champion_pts"] is not None]
    points = [c["champion_pts"] for c in champions if c["champion_pts"] is not None]
    ax.plot(seasons, points, marker="o", color="#C44E52", linewidth=2)
    ax.set_ylabel("champion points")
    ax.set_xlabel("season")
    ax.set_title("Champion points per season")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.set_ylim(0, None)
    fig.tight_layout()
    return fig


def avg_goals_trend_chart(trends: list[dict]):
    fig, ax = new_figure(w=8, h=5)
    seasons = [t["season"] for t in trends if t["avg_goals"] is not None]
    values = [t["avg_goals"] for t in trends if t["avg_goals"] is not None]
    ax.plot(seasons, values, marker="o", color="#4C72B0", linewidth=2)
    ax.set_ylabel("avg goals per match")
    ax.set_xlabel("season")
    ax.set_title("Average goals per match per season")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.set_ylim(0, None)
    fig.tight_layout()
    return fig


def build_charts(report: dict, out_dir: Path) -> list[Path]:
    charts = [
        save_chart(out_dir, f"{STEM}_champion_points", champion_points_chart(report["champions"])),
        save_chart(out_dir, f"{STEM}_avg_goals", avg_goals_trend_chart(report["league_trends"])),
    ]
    return [c for c in charts if c is not None]


# ── markdown rendering ───────────────────────────────────────────────────────
def render_markdown(report: dict) -> str:
    lines = render_report_header(report, "Season Trends Analysis").splitlines()
    add = lines.append

    ch = report["champions"]
    add("")
    add("## 1. Champions per season")
    add(fmt_md_table(
        ["season", "champion", "pts", "runner-up", "margin"],
        [
            [c["season"],
             c["champion"] if c["champion"] else "-",
             c["champion_pts"] if c["champion_pts"] is not None else "-",
             c["runner_up"] if c["runner_up"] else "-",
             f"{c['margin_pts']} pts" if c["margin_pts"] is not None else "-"]
            for c in ch
        ],
    ))

    tr = report["title_race"]
    add("")
    add("## 2. Title-race tightness")
    add(f"- Tight races (margin <= 3 pts): **{tr['tight_race_count']}** "
        f"of {tr['total_seasons']} seasons")
    if tr["tightest"]:
        t = tr["tightest"]
        add(f"- Tightest race: **{t['season']}** - {t['champion']} beat "
            f"{t['runner_up']} by **{t['margin']}** pts")
    add("")
    add(fmt_md_table(
        ["season", "margin", "tight"],
        [[e["season"],
          f"{e['margin']} pts" if e["margin"] is not None else "-",
          "yes" if e["tight"] else ""]
         for e in tr["per_season"]],
    ))

    add("")
    add("## 3. Points thresholds")
    n = report["league"]["teams"]
    add("_Position-specific points per season. Key: 1 = champion, 2 = runner-up, "
       f"4 = CL line, 6 = Europa, {n - 3} = last safe, {n} = bottom._")
    add("")
    th = report["points_thresholds"]
    if th:
        all_pos_keys = sorted(th[0]["positions"].keys(), key=lambda p: int(p))
        headers = ["season"] + [f"pos {p}" for p in all_pos_keys]
        add(fmt_md_table(
            headers,
            [[t["season"]] + [t["positions"][p] if t["positions"][p] is not None else "-"
                              for p in all_pos_keys]
             for t in th],
        ))

    add("")
    add("## 4. Relegation battle")
    rb = report["relegation_battle"]
    add(fmt_md_table(
        ["season", "safe pos", "safe pts", "drop pos", "drop pts", "gap"],
        [[r["season"], r["safe_position"], r["safe_pts"] if r["safe_pts"] is not None else "-",
          r["drop_position"], r["drop_pts"] if r["drop_pts"] is not None else "-",
          f"{r['gap']} pts" if r["gap"] is not None else "-"]
         for r in rb],
    ))

    add("")
    add("## 5. League-level trends")
    lt = report["league_trends"]
    add(fmt_md_table(
        ["season", "matches", "total goals", "avg goals",
         "home win", "draw", "away win", "goalless", "avg pts/team"],
        [
            [t["season"], t["n_matches"], t["total_goals"],
             t["avg_goals"] if t["avg_goals"] is not None else "-",
             fmt_pct(t["home_win_pct"]), fmt_pct(t["draw_pct"]),
             fmt_pct(t["away_win_pct"]), fmt_pct(t["goalless_pct"]),
             t["avg_points_per_team"] if t["avg_points_per_team"] is not None else "-"]
            for t in lt
        ],
    ))

    add("")
    add("## 6. View divergence")
    vd = report["view_divergence"]
    if vd["worst_divergence"]:
        w = vd["worst_divergence"]
        add(f"- Largest divergence: **{w['season']}** ({w['view']} view, "
            f"avg abs position diff = {w['avg_abs_diff']:.3f})")
    add("")
    add("_Avg absolute position difference between classic view and alternative "
       "view per season._")
    add("")
    add(fmt_md_table(
        ["season", "classic vs luck", "classic vs goals"],
        [[e["season"],
          f"{e['luck']:.3f}" if e.get("luck") is not None else "-",
          f"{e['goals']:.3f}" if e.get("goals") is not None else "-"]
         for e in vd["per_season"]],
    ))

    add("")
    add("---")
    add("*All statistics are computed from PostgreSQL tables (read-only). "
       "Run with `python backend/scripts/analyze_seasons.py` to regenerate.*")
    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────
def parse_module_args(argv: list[str] | None = None) -> argparse.Namespace:
    return parse_args(
        "Module 4 - Season-by-season trends analysis report (read-only queries).",
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

    ch = report["champions"]
    print(f"{STEM} [{cfg['league']}]: {len(ch)} seasons, "
          f"{report['title_race']['tight_race_count']} tight races, "
          f"tightest: "
          f"{report['title_race']['tightest']['season'] if report['title_race']['tightest'] else 'n/a'} "
          f"- wrote {json_path} and {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
