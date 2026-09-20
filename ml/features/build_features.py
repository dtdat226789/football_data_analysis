"""Orchestrator: build leakage-safe, pre-match feature rows from PostgreSQL matches.

Pipeline per league season:

  1. All matches of the season are loaded already ordered by
     (match_date, kickoff_time, api_id).
  2. Matches are processed in groups of equal (match_date, kickoff_time).
     Every match in a group is scored using ONLY state built from matches with
     a strictly smaller (match_date, kickoff_time). Results are then applied
     to that state AFTER the whole group is scored.
     -> a match can never observe its own result, a simultaneous result, or
        any future result; it can observe earlier-same-day results, exactly
        like real-world information availability.
  3. State per team (team history of TeamRecords) drives form / venue / rest.
     A running pre-match league table (standings.py) drives group C.

No randomness: identical database content produces byte-identical rows.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR / "backend" / "scripts"))

import psycopg2.extras  # noqa: E402

from ml import db  # noqa: E402
from ml.features import form, home_away, rest, standings  # noqa: E402
from ml.features.records import Match, TeamRecord  # noqa: E402
from ml.features.standings import StandingsRow  # noqa: E402

# Top-level column order of the produced dataset.
CONTEXT_COLUMNS = [
    "api_id",
    "league",
    "season",
    "game_index",
    "home_team_id",
    "home_team",
    "away_team_id",
    "away_team",
    "match_date",
    "home_team_games_before",
    "away_team_games_before",
]

FEATURE_COLUMNS = [
    # A. recent form (last 5 matches, any venue)
    "home_team_points_last_5",
    "away_team_points_last_5",
    "home_team_wins_last_5",
    "away_team_wins_last_5",
    "home_team_goals_scored_last_5",
    "away_team_goals_scored_last_5",
    "home_team_goals_conceded_last_5",
    "away_team_goals_conceded_last_5",
    # B. home / away performance
    "home_team_home_win_rate",
    "home_team_home_goals_avg",
    "home_team_home_conceded_avg",
    "away_team_away_win_rate",
    "away_team_away_goals_avg",
    "away_team_away_conceded_avg",
    # C. pre-match standings context
    "home_position_before_match",
    "away_position_before_match",
    "position_difference",
    "home_points_before_match",
    "away_points_before_match",
    "points_difference",
    # D. rest
    "home_rest_days",
    "away_rest_days",
    "rest_days_difference",
]

OUTCOME_COLUMNS = [
    "home_score",
    "away_score",
    "match_result",
]

# Every column that must hold a concrete value (feature + outcome scores).
MATERIALIZED_COLUMNS = FEATURE_COLUMNS + OUTCOME_COLUMNS[:2]

ALL_COLUMNS = CONTEXT_COLUMNS + FEATURE_COLUMNS + OUTCOME_COLUMNS

MATCH_RESULTS = {"HOME_WIN": "home", "DRAW": "draw", "AWAY_WIN": "away"}


def load_matches(conn, league: str) -> list[Match]:
    """Load every completed match for `league`, ordered deterministically."""
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(
            """
            SELECT m.api_id, m.league_season_id, m.game_index,
                   m.home_team_id, m.away_team_id,
                   s.name AS season, m.match_date, m.kickoff_time,
                   m.home_score, m.away_score,
                   th.api_name AS home_team, ta.api_name AS away_team
            FROM matches m
            JOIN league_seasons ls ON ls.id = m.league_season_id
            JOIN leagues l ON l.id = ls.league_id
            JOIN seasons s ON s.id = ls.season_id
            LEFT JOIN team_seasons th
              ON th.league_season_id = m.league_season_id AND th.team_id = m.home_team_id
            LEFT JOIN team_seasons ta
              ON ta.league_season_id = m.league_season_id AND ta.team_id = m.away_team_id
            WHERE l.api_key = %s
            ORDER BY s.start_year, m.match_date, m.kickoff_time, m.game_index, m.api_id
            """,
            (league,),
        )
        raw = cur.fetchall()
    matches = [
        Match(
            api_id=r["api_id"],
            league_season_id=r["league_season_id"],
            season=r["season"],
            game_index=r["game_index"],
            home_team_id=r["home_team_id"],
            away_team_id=r["away_team_id"],
            home_team=r["home_team"],
            away_team=r["away_team"],
            match_date=r["match_date"],
            kickoff_time=r["kickoff_time"],
            home_score=r["home_score"],
            away_score=r["away_score"],
        )
        for r in raw
    ]
    return matches


def season_names(matches: list[Match]) -> list[str]:
    return sorted({m.season for m in matches}, key=db.parse_season_years)


def feature_block(
    m: Match,
    home_records: list[TeamRecord],
    away_records: list[TeamRecord],
    table: dict[int, StandingsRow],
    roster: set[int],
) -> dict:
    """Compute every feature for one match from prior state only."""
    hf = form.all_family_last(home_records)
    af = form.all_family_last(away_records)
    home_rest = rest.rest_days(home_records, m.match_date)
    away_rest = rest.rest_days(away_records, m.match_date)
    home_pos = standings.position(table, roster, m.home_team_id)
    away_pos = standings.position(table, roster, m.away_team_id)
    home_pts = standings.points_of(table, m.home_team_id)
    away_pts = standings.points_of(table, m.away_team_id)
    return {
        # A.
        "home_team_points_last_5": hf["points_last"],
        "away_team_points_last_5": af["points_last"],
        "home_team_wins_last_5": hf["wins_last"],
        "away_team_wins_last_5": af["wins_last"],
        "home_team_goals_scored_last_5": hf["goals_scored_last"],
        "away_team_goals_scored_last_5": af["goals_scored_last"],
        "home_team_goals_conceded_last_5": hf["goals_conceded_last"],
        "away_team_goals_conceded_last_5": af["goals_conceded_last"],
        # B.
        "home_team_home_win_rate": home_away.win_rate(home_records, is_home=True),
        "home_team_home_goals_avg": home_away.goals_avg(home_records, is_home=True),
        "home_team_home_conceded_avg": home_away.conceded_avg(home_records, is_home=True),
        "away_team_away_win_rate": home_away.win_rate(away_records, is_home=False),
        "away_team_away_goals_avg": home_away.goals_avg(away_records, is_home=False),
        "away_team_away_conceded_avg": home_away.conceded_avg(away_records, is_home=False),
        # C.
        "home_position_before_match": home_pos,
        "away_position_before_match": away_pos,
        "position_difference": home_pos - away_pos,
        "home_points_before_match": home_pts,
        "away_points_before_match": away_pts,
        "points_difference": home_pts - away_pts,
        # D.
        "home_rest_days": home_rest,
        "away_rest_days": away_rest,
        "rest_days_difference": None if home_rest is None or away_rest is None else home_rest - away_rest,
    }


def apply_result(table: dict[int, StandingsRow], team_id: int, rec: TeamRecord) -> None:
    row = table[team_id]
    table[team_id] = StandingsRow(
        played=row.played + 1,
        points=row.points + rec.points,
        goal_difference=row.goal_difference + rec.goals_for - rec.goals_against,
        goals_for=row.goals_for + rec.goals_for,
    )


def process_season(matches: list[Match], league: str = "premier") -> list[dict]:
    """Turn the chronologically-ordered matches of ONE season into feature rows.

    Grouping by (match_date, kickoff_time) guarantees that only strictly
    earlier matches contribute to any feature (see module docstring).
    """
    history: dict[int, list[TeamRecord]] = defaultdict(list)
    table: dict[int, StandingsRow] = defaultdict(StandingsRow)
    roster = {m.home_team_id for m in matches} | {m.away_team_id for m in matches}
    for tid in roster:
        table[tid]  # pre-seed every roster team (deterministic rank)
    if not matches:
        return []

    rows: list[dict] = []
    i, n = 0, len(matches)
    while i < n:
        key = (matches[i].match_date, matches[i].kickoff_time)
        j = i
        while j < n and (matches[j].match_date, matches[j].kickoff_time) == key:
            j += 1
        group = matches[i:j]

        scored = []
        for m in group:
            home_records = history[m.home_team_id]
            away_records = history[m.away_team_id]
            home_before = len(home_records)
            away_before = len(away_records)
            features = feature_block(m, home_records, away_records, table, roster)
            scored.append((m, home_before, away_before, features))

        # Apply results only after the whole group has been scored.
        for m, _, _, _ in scored:
            home_rec, away_rec = m.as_records()
            history[m.home_team_id].append(home_rec)
            history[m.away_team_id].append(away_rec)
            apply_result(table, m.home_team_id, home_rec)
            apply_result(table, m.away_team_id, away_rec)

        for m, home_before, away_before, features in scored:
            if m.home_score > m.away_score:
                result = "HOME_WIN"
            elif m.home_score == m.away_score:
                result = "DRAW"
            else:
                result = "AWAY_WIN"
            rows.append(
                {
                    "api_id": m.api_id,
                    "league": league,
                    "season": m.season,
                    "game_index": m.game_index,
                    "home_team_id": m.home_team_id,
                    "home_team": m.home_team,
                    "away_team_id": m.away_team_id,
                    "away_team": m.away_team,
                    "match_date": m.match_date.isoformat(),
                    "home_team_games_before": home_before,
                    "away_team_games_before": away_before,
                    **features,
                    "home_score": m.home_score,
                    "away_score": m.away_score,
                    "match_result": result,
                }
            )
        i = j
    return rows


def build_rows(conn, league: str = "premier") -> list[dict]:
    """Load all matches from PostgreSQL and produce feature rows for them."""
    matches = load_matches(conn, league)
    rows: list[dict] = []
    for season in season_names(matches):
        rows.extend(process_season([m for m in matches if m.season == season], league=league))
    return rows