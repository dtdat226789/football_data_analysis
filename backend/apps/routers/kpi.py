"""Sample-style dashboards: team KPIs and club analysis (read-only).

Both endpoints aggregate data that already exists in the analytics database:
classic standings (including xPts in ``metrics``), team membership and match
scores. They deliberately report goals-based proxies rather than pretending to
have xG/PPDA/shot data, which this project does not collect.

The calculation helpers are pure so ranking, rounding and empty-data behaviour
can be tested without PostgreSQL.
"""
from __future__ import annotations

import re
from typing import Any, Iterable

from fastapi import APIRouter, HTTPException

from .. import common
from ..deps import ensure_season, fetched_cursor, require_league, resolve_team_id
from ..rating import club_ratings

router = APIRouter(tags=["kpi"])

ATTRIBUTION = "Data by football-charts.com"

GROUPS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("creativity", ("goalsPerGame", "last5GoalsPerGame")),
    ("territory", ("homeGoalShare", "awayGoalsPerGame")),
    ("control", ("pointsPerGame", "cleanSheetPct")),
    ("attack", ("totalGoals", "homeGoalsPerGame")),
    ("defence", ("goalsAgainstPerGame", "awayGoalsAgainstPerGame")),
)

# key -> (lower is better, participates in league ranking)
TILE_RULES: dict[str, tuple[bool, bool]] = {
    "goalsPerGame": (False, True),
    "last5GoalsPerGame": (False, False),
    "homeGoalShare": (False, True),
    "awayGoalsPerGame": (False, True),
    "pointsPerGame": (False, True),
    "cleanSheetPct": (False, True),
    "totalGoals": (False, True),
    "homeGoalsPerGame": (False, True),
    "goalsAgainstPerGame": (True, True),
    "awayGoalsAgainstPerGame": (True, True),
    "expectedPoints": (False, False),
}


def _round(value: float | None) -> float | None:
    if value is None:
        return None
    try:
        return round(float(value), 2)
    except (TypeError, ValueError):
        return None


def _rate(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or not denominator:
        return None
    return _round(numerator / denominator)


def short_label(name: str | None) -> str:
    """Compact label for tables/bars: initials for multiword names, else 3 letters."""
    words = [w for w in re.split(r"\s+", name or "") if w]
    if not words:
        return "—"
    if len(words) > 1:
        return "".join(w[0] for w in words[:3]).upper()
    return words[0][:3].upper()


def ranks(values: dict[int, float | None], *, lower_is_better: bool = False) -> dict[int, int | None]:
    """Competition ranking: ties share a rank; missing values are unranked."""
    present = [v for v in values.values() if v is not None]
    result: dict[int, int | None] = {}
    for key, value in values.items():
        if value is None:
            result[key] = None
            continue
        if lower_is_better:
            better = sum(1 for other in present if other is not None and other < value - 1e-9)
        else:
            better = sum(1 for other in present if other is not None and other > value + 1e-9)
        result[key] = better + 1
    return result


def _accumulators(rows: Iterable[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    acc: dict[int, dict[str, Any]] = {}
    for row in rows:
        team_id = row["team_id"]
        if team_id in acc:
            continue
        metrics = row.get("metrics") or {}
        played = row.get("played") or 0
        gf = row.get("goals_for") or 0
        ga = row.get("goals_against") or 0
        acc[team_id] = {
            "played": played,
            "points": row.get("points") or 0,
            "gf": gf,
            "ga": ga,
            "expected_points": metrics.get("expected_points"),
            "home_gf": 0,
            "away_gf": 0,
            "home_ga": 0,
            "away_ga": 0,
            "home_played": 0,
            "away_played": 0,
            "clean_sheets": 0,
            "last5_gf": 0,
            "last5_count": 0,
        }
    return acc


def _apply_match(acc: dict[int, dict[str, Any]], match: dict[str, Any]) -> None:
    """Add one finished match to both sides' cumulative totals."""
    home_id, away_id = match["home_team_id"], match["away_team_id"]
    if home_id not in acc or away_id not in acc:
        return
    home_score = match.get("home_score")
    away_score = match.get("away_score")
    if home_score is None or away_score is None:
        return
    for team_id, is_home, gf, ga in (
        (home_id, True, home_score, away_score),
        (away_id, False, away_score, home_score),
    ):
        side = acc[team_id]
        if is_home:
            side["home_gf"] += gf
            side["home_ga"] += ga
            side["home_played"] += 1
        else:
            side["away_gf"] += gf
            side["away_ga"] += ga
            side["away_played"] += 1
        if ga == 0:
            side["clean_sheets"] += 1


def _metric_values(acc: dict[int, dict[str, Any]]) -> dict[str, dict[int, float | None]]:
    values: dict[str, dict[int, float | None]] = {
        key: {} for key in TILE_RULES if key != "expectedPoints"
    }
    for team_id, side in acc.items():
        played = side["played"]
        gf, ga = side["gf"], side["ga"]
        values["goalsPerGame"][team_id] = _rate(gf, played)
        values["last5GoalsPerGame"][team_id] = _rate(side["last5_gf"], side["last5_count"])
        values["homeGoalShare"][team_id] = _rate(100 * side["home_gf"], gf)
        values["awayGoalsPerGame"][team_id] = _rate(side["away_gf"], side["away_played"])
        values["pointsPerGame"][team_id] = _rate(side["points"], played)
        values["cleanSheetPct"][team_id] = _rate(100 * side["clean_sheets"], played)
        values["totalGoals"][team_id] = float(gf) if played else None
        values["homeGoalsPerGame"][team_id] = _rate(side["home_gf"], side["home_played"])
        values["goalsAgainstPerGame"][team_id] = _rate(ga, played)
        values["awayGoalsAgainstPerGame"][team_id] = _rate(side["away_ga"], side["away_played"])
    return values


def _tiles(acc: dict[int, dict[str, Any]], team_id: int) -> list[dict[str, Any]]:
    values = _metric_values(acc)
    ranks_by_key = {
        key: ranks(metric, lower_is_better=TILE_RULES[key][0])
        for key, metric in values.items()
        if TILE_RULES[key][1]
    }
    tiles: list[dict[str, Any]] = []
    for key in TILE_RULES:
        if key == "expectedPoints" or key not in values:
            continue
        tiles.append(
            {
                "key": key,
                "value": values[key].get(team_id),
                "rank": ranks_by_key.get(key, {}).get(team_id),
                "rank_total": len([v for v in values[key].values() if v is not None]),
                "lower_is_better": TILE_RULES[key][0],
            }
        )
    return tiles


def _last_matches(matches: Iterable[dict[str, Any]], team_id: int, n: int) -> list[dict[str, Any]]:
    """Most recent matches first, from the team's point of view."""
    found: list[dict[str, Any]] = []
    for match in reversed(list(matches)):
        home_id, away_id = match["home_team_id"], match["away_team_id"]
        if team_id not in (home_id, away_id):
            continue
        home_score, away_score = match.get("home_score"), match.get("away_score")
        if home_score is None or away_score is None:
            continue
        is_home = home_id == team_id
        gf, ga = (home_score, away_score) if is_home else (away_score, home_score)
        outcome = "W" if gf > ga else "D" if gf == ga else "L"
        found.append(
            {
                "date": str(match.get("match_date") or ""),
                "opponent": match.get("away_team") if is_home else match.get("home_team"),
                "venue": "home" if is_home else "away",
                "score": f"{home_score}–{away_score}",
                "result": outcome,
                "points": 3 if outcome == "W" else 1 if outcome == "D" else 0,
                "goals_for": gf,
                "goals_against": ga,
                "clean_sheet": ga == 0,
            }
        )
        if len(found) >= n:
            break
    return found


def build_team_kpi(
    rows: list[dict[str, Any]],
    matches: list[dict[str, Any]],
    team_id: int,
    n: int,
) -> dict[str, Any]:
    """Assemble the KPI dashboard payload from standings rows and match rows."""
    ratings = club_ratings(rows)
    acc = _accumulators(rows)
    for match in matches:
        _apply_match(acc, match)

    last_matches = _last_matches(matches, team_id, n)
    if team_id in acc:
        acc[team_id]["last5_gf"] = sum(m["goals_for"] for m in last_matches)
        acc[team_id]["last5_count"] = len(last_matches)

    table = [
        {
            "team": row.get("api_name") or "",
            "label": short_label(row.get("api_name")),
            "position": row.get("position"),
            "points": row.get("points") or 0,
            "expected_points": (row.get("metrics") or {}).get("expected_points"),
            "rating": (ratings.get(row["team_id"]) or {}).get("score"),
            "is_selected": row["team_id"] == team_id,
        }
        for row in rows
    ]

    tiles = {tile["key"]: tile for tile in _tiles(acc, team_id)}
    return {
        "club_rating": ratings.get(team_id),
        "last_matches": last_matches,
        "groups": [
            {"key": key, "tiles": [tiles[tile_key] for tile_key in tile_keys]}
            for key, tile_keys in GROUPS
        ],
        "table": table,
    }


def build_club_payload(
    rows: list[dict[str, Any]],
    seasons: list[dict[str, Any]],
    teams: list[dict[str, Any]],
    team_id: int,
    season: str,
) -> dict[str, Any]:
    """Season KPI cards, a goals-per-game timeline and a league-wide ranking."""
    season_rows = [r for r in rows if r["season"] == season]
    selected = next((r for r in season_rows if r["team_id"] == team_id), None)
    ratings = club_ratings(season_rows)
    rating = ratings.get(team_id)

    def metric(row: dict[str, Any] | None, name: str) -> float | None:
        if row is None:
            return None
        if name == "expectedPoints":
            return (row.get("metrics") or {}).get("expected_points")
        if name == "totalGoals":
            return float(row.get("goals_for") or 0) if row.get("played") else None
        if name == "goalsPerGame":
            return _rate(row.get("goals_for") or 0, row.get("played"))
        if name == "goalsAgainstPerGame":
            return _rate(row.get("goals_against") or 0, row.get("played"))
        return None

    kpis = [
        {
            "key": "clubRating",
            "value": rating["score"] if rating else None,
            "rank": rating["rank"] if rating else None,
            "rank_total": rating["rank_total"] if rating else 0,
        },
        *[
            {"key": key, "value": _round(metric(selected, key))}
            for key in ("totalGoals", "goalsPerGame", "goalsAgainstPerGame", "expectedPoints")
        ],
    ]

    season_order = [s["season"] for s in seasons]
    by_season = {
        row["season"]: row for row in rows if row["team_id"] == team_id and row.get("played")
    }
    timeline = [
        {
            "season": name,
            "value": _rate(by_season[name].get("goals_for") or 0, by_season[name].get("played")),
        }
        for name in season_order
        if name in by_season
    ]

    ranking = [
        {
            "team": row.get("api_name") or "",
            "label": short_label(row.get("api_name")),
            "slug": row.get("api_slug"),
            "played": row.get("played") or 0,
            "goals": row.get("goals_for") or 0,
            "goals_per_game": _rate(row.get("goals_for") or 0, row.get("played")),
            "rating": (ratings.get(row["team_id"]) or {}).get("score"),
            "is_selected": row["team_id"] == team_id,
        }
        for row in season_rows
        if row.get("played")
    ]
    ranking.sort(key=lambda r: (r["goals_per_game"] or -1, r["goals"]), reverse=True)

    return {
        "team": {
            "slug": next((t["slug"] for t in teams if t["id"] == team_id), None),
            "name": selected.get("api_name") if selected else None,
        },
        "seasons": seasons,
        "teams": teams,
        "kpis": kpis,
        "timeline": timeline,
        "ranking": ranking,
        "attribution": ATTRIBUTION,
    }


def _resolve_season(cur, league: str, season: str | None) -> str:
    if season is not None:
        ensure_season(cur, league, season)
        return season
    cur.execute(
        """
        SELECT s.name
        FROM league_seasons ls
        JOIN seasons s ON s.id = ls.season_id
        WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
          AND EXISTS (SELECT 1 FROM matches m WHERE m.league_season_id = ls.id)
        ORDER BY (ls.season_state = 'complete') DESC, s.start_year DESC, s.end_year DESC
        LIMIT 1
        """,
        (league,),
    )
    row = cur.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"no collected data for league '{league}'")
    return row[0]


def _require_team_in_league(cur, team_id: int, league: str, slug: str) -> None:
    cur.execute(
        """
        SELECT 1
        FROM team_seasons ts
        JOIN league_seasons ls ON ls.id = ts.league_season_id
        WHERE ts.team_id = %s
          AND ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
        LIMIT 1
        """,
        (team_id, league),
    )
    if cur.fetchone() is None:
        raise HTTPException(
            status_code=404, detail=f"team '{slug}' does not play in league '{league}'"
        )


@router.get("/teams/{slug}/kpi")
def team_kpi(
    slug: str,
    league: str = common.DEFAULT_LEAGUE,
    season: str | None = None,
    n: int = 5,
) -> dict[str, Any]:
    """Last-N games, proxy KPIs with league ranks, and the classic table."""
    require_league(league)
    n = min(max(n, 1), 20)
    with fetched_cursor() as cur:
        team_id = resolve_team_id(cur, slug)
        if team_id is None:
            raise HTTPException(status_code=404, detail=f"team '{slug}' not found")
        _require_team_in_league(cur, team_id, league, slug)
        season = _resolve_season(cur, league, season)
        cur.execute(
            """
            SELECT st.team_id, ts.api_name, ts.api_slug, ts.logo_url,
                   st.position, st.played, st.points, st.goals_for, st.goals_against,
                   st.metrics
            FROM standings st
            JOIN league_seasons ls ON ls.id = st.league_season_id
            JOIN seasons s ON s.id = ls.season_id
            JOIN team_seasons ts
              ON ts.league_season_id = st.league_season_id AND ts.team_id = st.team_id
            WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
              AND s.name = %s AND st.view = 'classic'
            ORDER BY st.position NULLS LAST, st.team_id
            """,
            (league, season),
        )
        rows = [dict(r) for r in cur.fetchall()]
        cur.execute(
            """
            SELECT m.match_date, m.home_team_id, m.away_team_id,
                   m.home_score, m.away_score, th.api_name AS home_team,
                   ta.api_name AS away_team
            FROM matches m
            JOIN league_seasons ls ON ls.id = m.league_season_id
            JOIN seasons s ON s.id = ls.season_id
            JOIN team_seasons th
              ON th.league_season_id = m.league_season_id AND th.team_id = m.home_team_id
            JOIN team_seasons ta
              ON ta.league_season_id = m.league_season_id AND ta.team_id = m.away_team_id
            WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
              AND s.name = %s
            ORDER BY m.match_date, m.kickoff_time, m.game_index
            """,
            (league, season),
        )
        matches = [dict(r) for r in cur.fetchall()]

    payload = build_team_kpi(rows, matches, team_id, n)
    selected = next((r for r in rows if r["team_id"] == team_id), None)
    return {
        "team": slug,
        "team_name": (selected or {}).get("api_name") or slug,
        "logo_url": (selected or {}).get("logo_url"),
        "league": league,
        "league_name": common.league_name(league),
        "season": season,
        "n": n,
        "attribution": ATTRIBUTION,
        **payload,
    }


@router.get("/club-analysis")
def club_analysis(
    league: str = common.DEFAULT_LEAGUE,
    season: str | None = None,
    team: str | None = None,
) -> dict[str, Any]:
    """Club season cards, goals-per-game timeline and league goal ranking."""
    require_league(league)
    with fetched_cursor() as cur:
        season = _resolve_season(cur, league, season)
        cur.execute(
            """
            SELECT DISTINCT ts.team_id AS id, ts.api_name AS name, ts.api_slug AS slug
            FROM team_seasons ts
            JOIN league_seasons ls ON ls.id = ts.league_season_id
            WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
            ORDER BY ts.api_name
            """,
            (league,),
        )
        teams = [dict(r) for r in cur.fetchall()]
        cur.execute(
            """
            SELECT s.name AS season, st.team_id, ts.api_name, ts.api_slug,
                   st.played, st.goals_for, st.goals_against, st.points, st.metrics
            FROM standings st
            JOIN league_seasons ls ON ls.id = st.league_season_id
            JOIN seasons s ON s.id = ls.season_id
            JOIN team_seasons ts
              ON ts.league_season_id = st.league_season_id AND ts.team_id = st.team_id
            WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
              AND st.view = 'classic'
            ORDER BY s.start_year, s.end_year, st.position NULLS LAST
            """,
            (league,),
        )
        rows = [dict(r) for r in cur.fetchall()]

    if team is not None:
        team_id = resolve_team_id_with(teams, team)
        if team_id is None:
            raise HTTPException(status_code=404, detail=f"team '{team}' not found in '{league}'")
    else:
        current = [r for r in rows if r["season"] == season]
        best = max(current, key=lambda r: (r.get("points") or 0, -(r["team_id"])), default=None)
        team_id = best["team_id"] if best else (teams[0]["id"] if teams else -1)

    cur_seasons = [
        {"season": name}
        for name in sorted({r["season"] for r in rows})
    ]
    payload = build_club_payload(rows, cur_seasons, teams, team_id, season)
    payload["league"] = league
    payload["league_name"] = common.league_name(league)
    payload["season"] = season
    return payload


def resolve_team_id_with(teams: list[dict[str, Any]], value: str) -> int | None:
    """Resolve a slug or name against the league's own team list."""
    for row in teams:
        if value in (row.get("slug"), row.get("name")):
            return row["id"]
    return None
