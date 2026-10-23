"""Matches API: paginated, filterable match feeds from PostgreSQL (read-only)."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from fastapi import APIRouter, HTTPException

from .. import common
from ..deps import (
    ensure_season,
    fetched_cursor,
    norm_pagination,
    require_league,
    resolve_latest_season,
)

router = APIRouter(tags=["matches"])

_MATCH_COLUMNS = """
    s.name AS season, m.game_index, m.match_date, m.kickoff_time,
    th.api_name AS home_team, ta.api_name AS away_team,
    m.home_score, m.away_score, m.home_ht, m.away_ht,
    m.first_goal_time, m.first_goal_time_extra
"""
_MATCH_JOINS = """
    FROM matches m
    JOIN league_seasons ls ON ls.id = m.league_season_id
    JOIN seasons s ON s.id = ls.season_id
    JOIN team_seasons th ON th.league_season_id = m.league_season_id AND th.team_id = m.home_team_id
    JOIN team_seasons ta ON ta.league_season_id = m.league_season_id AND ta.team_id = m.away_team_id
"""


def _resolve_season(cur, league: str, season: str | None) -> str:
    if season is None:
        season = resolve_latest_season(cur, league)
        if season is None:
            raise HTTPException(
                status_code=404,
                detail=f"no collected data for league '{league}'",
            )
    else:
        ensure_season(cur, league, season)
    return season


def check_date_window(from_date: date | None, to_date: date | None) -> None:
    """Reject an inverted date window with a 422.

    FastAPI already rejects a malformed value because these params are typed
    `date`. This covers the other half: `from` after `to` used to pass the
    filters and quietly answer "no matches", which reads as an empty league
    rather than a wrong request.
    """
    if from_date and to_date and from_date > to_date:
        raise HTTPException(
            status_code=422,
            detail=f"from_date {from_date.isoformat()} is after to_date {to_date.isoformat()}",
        )


@router.get("/leagues/{league}/matches")
def list_matches(
    league: str,
    season: str | None = None,
    from_date: date | None = None,
    to_date: date | None = None,
    limit: int = 50,
    offset: int = 0,
) -> dict:
    require_league(league)
    check_date_window(from_date, to_date)
    limit, offset = norm_pagination(limit, offset)
    with fetched_cursor() as cur:
        season = _resolve_season(cur, league, season)
        filters = [
            "ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)",
            "s.name = %s",
        ]
        params: list = [league, season]
        if from_date:
            filters.append("m.match_date >= %s")
            params.append(from_date)
        if to_date:
            filters.append("m.match_date <= %s")
            params.append(to_date)
        where = " AND ".join(filters)

        cur.execute(
            f"SELECT count(*) FROM matches m JOIN league_seasons ls "
            f"ON ls.id = m.league_season_id JOIN seasons s ON s.id = ls.season_id "
            f"WHERE {where}",
            params,
        )
        total = cur.fetchone()[0]
        cur.execute(
            f"SELECT m.api_id, {_MATCH_COLUMNS} {_MATCH_JOINS} "
            f"WHERE {where} ORDER BY m.match_date, m.kickoff_time, m.game_index "
            f"LIMIT %s OFFSET %s",
            params + [limit, offset],
        )
        rows = [dict(r) for r in cur.fetchall()]
    return {
        "league": league,
        "league_name": common.league_name(league),
        "season": season,
        "total": total,
        "limit": limit,
        "offset": offset,
        "matches": rows,
    }


@router.get("/matches/recent")
def recent_matches(
    league: str | None = None,
    from_date: date | None = None,
    to_date: date | None = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """Most recently finished matches across leagues (paginated, read-only).

    Each row carries `country` but not a derived `region`: nothing consuming this
    feed reads one, and the dashboard's own region buckets come from
    `GET /dashboard`, not from these rows. A client that wants the grouping can
    derive it from `country`.
    """
    check_date_window(from_date, to_date)
    limit = min(max(limit, 1), 200)
    offset = max(offset, 0)
    filters: list[str] = ["m.home_score IS NOT NULL"]
    params: list = []
    if league is not None:
        require_league(league)
        filters.append("l.api_key = %s")
        params.append(league)
    if from_date:
        filters.append("m.match_date >= %s")
        params.append(from_date)
    if to_date:
        filters.append("m.match_date <= %s")
        params.append(to_date)
    where = " AND ".join(filters)

    with fetched_cursor() as cur:
        cur.execute(
            f"""
            SELECT count(*)
            FROM matches m
            JOIN league_seasons ls ON ls.id = m.league_season_id
            JOIN leagues l ON l.id = ls.league_id
            WHERE {where}
            """,
            params,
        )
        total = cur.fetchone()[0]
        cur.execute(
            f"""
            SELECT m.api_id, {_MATCH_COLUMNS}, l.api_key AS league,
                   l.name AS league_name, l.country, l.url
            {_MATCH_JOINS}
            JOIN leagues l ON l.id = ls.league_id
            WHERE {where}
            ORDER BY m.match_date DESC, m.kickoff_time DESC, m.game_index DESC
            LIMIT %s OFFSET %s
            """,
            params + [limit, offset],
        )
        rows = [dict(r) for r in cur.fetchall()]
    return {
        "count": len(rows),
        "total": total,
        "limit": limit,
        "offset": offset,
        "league": league,
        "league_name": common.league_name(league),
        "matches": rows,
    }


@router.get("/matches/{api_id}")
def get_match(api_id: int) -> dict:
    with fetched_cursor() as cur:
        cur.execute(
            f"SELECT m.api_id, {_MATCH_COLUMNS}, l.api_key AS league, "
            f"l.name AS league_name, l.country, l.url "
            f"{_MATCH_JOINS} JOIN leagues l ON l.id = ls.league_id "
            f"WHERE m.api_id = %s",
            (api_id,),
        )
        row = cur.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"match {api_id} not found")
    return dict(row)

# ---------------------------------------------------------------------------
# Match insights: pre-match context, model view, head-to-head
# ---------------------------------------------------------------------------
#
# The ML side publishes JSON artifacts rather than letting the API load a model
# (ml/models/ is gitignored, and routers/fixtures.py sets the same precedent by
# reading data/raw/fixtures/*.json). Both files are optional: a checkout without
# a built dataset or a backfilled prediction file still gets head-to-head.

DATASET_JSON = common.ROOT_DIR / "ml" / "datasets" / "match_result_dataset.json"
PREDICTIONS_JSON = common.ROOT_DIR / "ml" / "datasets" / "match_predictions.json"

# Columns surfaced in the UI, grouped for display. Everything here is strictly
# pre-match: nothing in this block may use the final score or the result. Keys
# are the real dataset column names (ml.features.build_features.FEATURE_COLUMNS).
_PRE_MATCH_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {
    "form_last_5": (
        ("home_team_points_last_5", "Home points (last 5)"),
        ("away_team_points_last_5", "Away points (last 5)"),
        ("home_team_wins_last_5", "Home wins (last 5)"),
        ("away_team_wins_last_5", "Away wins (last 5)"),
        ("home_team_goals_scored_last_5", "Home scored (last 5)"),
        ("away_team_goals_scored_last_5", "Away scored (last 5)"),
        ("home_team_goals_conceded_last_5", "Home conceded (last 5)"),
        ("away_team_goals_conceded_last_5", "Away conceded (last 5)"),
    ),
    "venue": (
        ("home_team_home_win_rate", "Home win rate (home games)"),
        ("home_team_home_goals_avg", "Home avg goals (home)"),
        ("home_team_home_conceded_avg", "Home avg conceded (home)"),
        ("away_team_away_win_rate", "Away win rate (away games)"),
        ("away_team_away_goals_avg", "Away avg goals (away)"),
        ("away_team_away_conceded_avg", "Away avg conceded (away)"),
    ),
    "table_before_match": (
        ("home_position_before_match", "Home position"),
        ("away_position_before_match", "Away position"),
        ("position_difference", "Position difference"),
        ("home_points_before_match", "Home points"),
        ("away_points_before_match", "Away points"),
        ("points_difference", "Points difference"),
    ),
    "rest": (
        ("home_rest_days", "Home rest days"),
        ("away_rest_days", "Away rest days"),
        ("rest_days_difference", "Rest difference"),
    ),
    "load": (
        ("home_team_games_before", "Home games before"),
        ("away_team_games_before", "Away games before"),
    ),
}

# Group key -> human title, in display order.
PRE_MATCH_GROUP_LABELS = {
    "form_last_5": "Form (last 5)",
    "venue": "Venue split",
    "table_before_match": "Table before match",
    "rest": "Rest",
    "load": "Workload",
}

H2H_LIMIT = 10


_artifact_cache: dict[Path, object] = {}


def _load_artifact(path: Path):
    """Parse a JSON artifact once per process; None when absent or unreadable.

    Both ML artifacts are large (the dataset is multi-MB, the prediction file
    three-quarters of one) and read-only for the lifetime of the process, so
    re-parsing them per request is pure waste. Keyed by path so each artifact
    gets its own slot. Tests reset this via clear_artifact_cache().
    """
    if path not in _artifact_cache:
        try:
            _artifact_cache[path] = json.loads(path.read_bytes()) if path.exists() else None
        except (json.JSONDecodeError, OSError):
            _artifact_cache[path] = None
    return _artifact_cache[path]


def _load_json_index(path: Path, key: str) -> dict:
    """Load {key: record} from a JSON artifact, or {} if absent/unreadable."""
    payload = _load_artifact(path)
    if not isinstance(payload, dict):
        return {}
    index = payload.get(key)
    return index if isinstance(index, dict) else {}


def clear_artifact_cache() -> None:
    _artifact_cache.clear()


def _dataset_index() -> dict:
    """api_id (str) -> feature row. The dataset file is a top-level list.

    Cached on first use: match detail is one row out of thousands, and
    re-reading a multi-MB artifact per request would be wasteful.
    """
    rows = _load_artifact(DATASET_JSON)
    if not isinstance(rows, list):
        return {}
    return {str(r["api_id"]): r for r in rows if isinstance(r, dict) and "api_id" in r}


def _predictions_meta() -> dict | None:
    """Header fields describing which model produced the stored predictions.

    Read from the same parsed payload as the index, so a match detail costs one
    artifact read in total rather than one per section.
    """
    payload = _load_artifact(PREDICTIONS_JSON)
    if not isinstance(payload, dict):
        return None
    return {
        "model_id": payload.get("model_id"),
        "feature_version": payload.get("feature_version"),
        "holdout_seasons": payload.get("holdout_seasons"),
        "in_sample_warning": payload.get("in_sample_warning"),
    }


def build_pre_match(row: dict | None) -> dict | None:
    """Group a dataset row's pre-match features for display."""
    if not row:
        return None
    groups = {}
    for group, fields in _PRE_MATCH_GROUPS.items():
        values = {}
        for column, label in fields:
            if column in row and row[column] is not None:
                values[column] = {"label": label, "value": row[column]}
        if values:
            groups[group] = values
    return {
        "season": row.get("season"),
        "game_index": row.get("game_index"),
        "home_team": row.get("home_team"),
        "away_team": row.get("away_team"),
        "home_team_id": row.get("home_team_id"),
        "away_team_id": row.get("away_team_id"),
        "group_labels": PRE_MATCH_GROUP_LABELS,
        "groups": groups,
    }


def head_to_head(
    cur,
    home_id: int,
    away_id: int,
    before_date,
    exclude_api_id: int | None = None,
    limit: int = H2H_LIMIT,
) -> dict:
    """Prior meetings between two teams, plus a summary over ALL of them.

    `before_date` bounds the history so a caller describing a future fixture
    never counts meetings that have not happened yet. `exclude_api_id` drops
    the match being described when the caller is looking at a finished one.

    The summary is aggregated separately from the page because the table is
    capped by `limit`: deriving it from the returned rows would under-report
    any pair that has met more than `limit` times.
    """
    limit = max(1, min(int(limit), 25))
    pair = "((m.home_team_id = %s AND m.away_team_id = %s) OR (m.home_team_id = %s AND m.away_team_id = %s))"
    exclude = "m.api_id <> %s AND " if exclude_api_id is not None else ""
    exclude_params: list = [exclude_api_id] if exclude_api_id is not None else []

    cur.execute(
        f"""
        SELECT m.api_id, m.match_date, s.name AS season, m.game_index,
               m.home_score, m.away_score,
               th.api_name AS home_team, ta.api_name AS away_team
        FROM matches m
        JOIN league_seasons ls ON ls.id = m.league_season_id
        JOIN seasons s ON s.id = ls.season_id
        JOIN team_seasons th
          ON th.league_season_id = m.league_season_id AND th.team_id = m.home_team_id
        JOIN team_seasons ta
          ON ta.league_season_id = m.league_season_id AND ta.team_id = m.away_team_id
        WHERE {exclude}m.match_date < %s AND {pair}
        ORDER BY m.match_date DESC, m.api_id DESC
        LIMIT %s
        """,
        exclude_params + [before_date, home_id, away_id, away_id, home_id, limit],
    )
    meetings = [dict(r) for r in cur.fetchall()]

    cur.execute(
        f"""
        SELECT count(*) AS played,
               sum(CASE
                     WHEN m.home_score IS NULL OR m.away_score IS NULL THEN 0
                     WHEN m.home_team_id = %s AND m.home_score > m.away_score THEN 1
                     WHEN m.away_team_id = %s AND m.away_score > m.home_score THEN 1
                     ELSE 0 END) AS home_team_wins,
               sum(CASE
                     WHEN m.home_score IS NULL OR m.away_score IS NULL THEN 0
                     WHEN m.home_score = m.away_score THEN 1
                     ELSE 0 END) AS draws,
               sum(CASE
                     WHEN m.home_score IS NULL OR m.away_score IS NULL THEN 0
                     WHEN m.home_team_id = %s THEN m.home_score
                     ELSE m.away_score END) AS goals_for,
               sum(CASE
                     WHEN m.home_score IS NULL OR m.away_score IS NULL THEN 0
                     WHEN m.home_team_id = %s THEN m.away_score
                     ELSE m.home_score END) AS goals_against
        FROM matches m
        WHERE {exclude}m.match_date < %s AND {pair}
        """,
        [home_id, home_id, home_id, home_id]
        + exclude_params
        + [before_date, home_id, away_id, away_id, home_id],
    )
    agg = cur.fetchone() or {}

    played = int(agg.get("played") or 0)
    summary = None
    if played:
        home_wins = int(agg.get("home_team_wins") or 0)
        draws = int(agg.get("draws") or 0)
        summary = {
            "played": played,
            "home_team_wins": home_wins,
            "draws": draws,
            "away_team_wins": played - home_wins - draws,
            "goals_for": int(agg.get("goals_for") or 0),
            "goals_against": int(agg.get("goals_against") or 0),
        }

    return {
        "limit": limit,
        "summary": summary,
        # True when the table shows only the most recent `limit` meetings, so
        # the UI can say so instead of implying this is the full history.
        "truncated": bool(summary and summary["played"] > len(meetings)),
        "matches": meetings,
    }


@router.get("/matches/{api_id}/insights")
def get_match_insights(api_id: int, limit: int = H2H_LIMIT) -> dict:
    """Pre-match context, the model's stored view, and head-to-head history.

    Every section is independently optional. ``pre_match`` is null for matches
    outside the materialized dataset (an in-progress fixture, say), ``model`` is
    null when no backfill artifact exists, and head-to-head is an empty list for
    a first-ever meeting.
    """
    limit = max(1, min(int(limit), 25))

    with fetched_cursor() as cur:
        cur.execute(
            f"SELECT m.api_id, m.home_team_id, m.away_team_id, "
            f"th.api_name AS home_team, ta.api_name AS away_team, "
            f"s.name AS season, m.match_date, m.game_index, "
            f"m.home_score, m.away_score, l.api_key AS league "
            f"{_MATCH_JOINS} JOIN leagues l ON l.id = ls.league_id "
            f"WHERE m.api_id = %s",
            (api_id,),
        )
        match = cur.fetchone()
        if match is None:
            raise HTTPException(status_code=404, detail=f"match {api_id} not found")

        home_id, away_id = match["home_team_id"], match["away_team_id"]
        h2h = head_to_head(
            cur,
            home_id,
            away_id,
            match["match_date"],
            exclude_api_id=api_id,
            limit=limit,
        )

    model = _load_json_index(PREDICTIONS_JSON, "matches").get(str(api_id))
    model_meta = _predictions_meta()

    return {
        "api_id": api_id,
        "league": match["league"],
        "league_name": common.league_name(match["league"]),
        "match": dict(match),
        "pre_match": build_pre_match(_dataset_index().get(str(api_id))),
        "model": {**model, **({"meta": model_meta} if model_meta else {})}
        if model
        else None,
        "head_to_head": h2h,
    }
