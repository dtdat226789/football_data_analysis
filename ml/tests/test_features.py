"""Synthetic-fixture tests for the leakage-safe feature layer.

Every test is DB-free and network-free. The fixtures are tiny hand-built
seasons so the expected values can be verified by hand.
"""
from __future__ import annotations

from datetime import date, time

import pytest

from ml.features import form, home_away, rest
from ml.features.build_features import OUTCOME_COLUMNS, process_season
from ml.features.records import Match, TeamRecord
from ml.features.standings import StandingsRow, position, strictly_better
from ml.validation import check_dataset

D1 = date(2021, 1, 1)
D2 = date(2021, 1, 8)
D3 = date(2021, 1, 15)


def rec(day, points, win, gf, ga, is_home):
    return TeamRecord(
        api_id=0, match_date=day, kickoff_time=time(15, 0),
        points=points, is_win=win, goals_for=gf, goals_against=ga, is_home=is_home,
    )


def mk(api_id, home, away, hs, as_, day, kickoff=time(15, 0), game_index=1, season="2020-2021"):
    return Match(
        api_id=api_id, league_season_id=1, season=season, game_index=game_index,
        home_team_id=home, away_team_id=away,
        home_team=f"T{home}", away_team=f"T{away}",
        match_date=day, kickoff_time=kickoff, home_score=hs, away_score=as_,
    )


def make_season(season="2020-2021"):
    """Four teams, three matchdays. Returns chronologically ordered matches."""
    return [
        mk(1, 1, 2, 2, 0, D1, game_index=1, season=season),
        mk(2, 3, 4, 1, 1, D1, game_index=2, season=season),
        mk(3, 2, 3, 0, 1, D2, game_index=3, season=season),
        mk(4, 4, 1, 3, 1, D2, game_index=4, season=season),
        mk(5, 1, 3, 1, 0, D3, game_index=5, season=season),
        mk(6, 2, 4, 2, 2, D3, game_index=6, season=season),
    ]


# --------------------------------------------------------------------------
# records / points
# --------------------------------------------------------------------------
def test_as_records_home_win():
    home, away = mk(1, 1, 2, 2, 0, D1).as_records()
    assert (home.points, home.is_win, home.goals_for, home.goals_against) == (3, 1, 2, 0)
    assert (away.points, away.is_win, away.goals_for, away.goals_against) == (0, 0, 0, 2)


def test_as_records_draw():
    home, away = mk(1, 1, 2, 1, 1, D1).as_records()
    assert (home.points, home.is_win) == (1, 1)
    assert (away.points, away.is_win) == (1, 1)


def test_as_records_away_win():
    home, away = mk(1, 1, 2, 0, 3, D1).as_records()
    assert (home.points, home.is_win) == (0, 0)
    assert (away.points, away.is_win) == (3, 1)


# --------------------------------------------------------------------------
# form
# --------------------------------------------------------------------------
def test_form_last_n_and_aggregates():
    records = [rec(D1, 3, 1, 2, 0, True), rec(D2, 0, 0, 1, 3, False), rec(D3, 1, 1, 1, 1, True)]
    assert form.points_last(records) == 4
    assert form.wins_last(records) == 2
    assert form.goals_scored_last(records) == 4
    assert form.goals_conceded_last(records) == 4


def test_form_window_only_last_five():
    records = [rec(D1 + (i * (D3 - D1)) // 6, 3, 1, 1, 0, True) for i in range(7)]
    # 7 records, only last 5 count -> 15 points, 5 wins
    assert form.points_last(records) == 15
    assert form.wins_last(records) == 5


def test_form_empty_is_zero():
    assert (form.points_last([]), form.wins_last([]), form.goals_scored_last([])) == (0, 0, 0)
    assert form.goals_conceded_last([]) == 0


# --------------------------------------------------------------------------
# home / away venue splits
# --------------------------------------------------------------------------
def test_home_away_splits():
    records = [
        rec(D1, 3, 1, 2, 0, True),
        rec(D2, 0, 0, 0, 1, False),
        rec(D3, 3, 1, 4, 1, True),
    ]
    assert home_away.win_rate(records, is_home=True) == 1.0
    assert home_away.goals_avg(records, is_home=True) == 3.0
    assert home_away.conceded_avg(records, is_home=True) == 0.5
    assert home_away.win_rate(records, is_home=False) == 0.0
    assert home_away.goals_avg(records, is_home=False) == 0.0
    assert home_away.conceded_avg(records, is_home=False) == 1.0


def test_home_away_empty_is_zero():
    assert home_away.win_rate([], is_home=True) == 0.0
    assert home_away.goals_avg([], is_home=False) == 0.0


# --------------------------------------------------------------------------
# standings
# --------------------------------------------------------------------------
def test_standings_strictly_better_ordering():
    a = StandingsRow(played=1, points=3, goal_difference=2, goals_for=2)
    b = StandingsRow(played=1, points=3, goal_difference=1, goals_for=5)
    c = StandingsRow(played=1, points=0, goal_difference=-2, goals_for=0)
    assert strictly_better(a, b)          # points tie -> better GD
    assert strictly_better(a, c)
    assert not strictly_better(b, a)
    assert not strictly_better(a, a)


def test_standings_position_with_ties():
    table = {
        1: StandingsRow(1, 3, 2, 2),
        2: StandingsRow(1, 1, 0, 1),
        3: StandingsRow(1, 1, 0, 1),
        4: StandingsRow(1, 0, -2, 0),
    }
    assert position(table, {1, 2, 3, 4}, 1) == 1
    assert position(table, {1, 2, 3, 4}, 2) == 2
    assert position(table, {1, 2, 3, 4}, 3) == 2
    assert position(table, {1, 2, 3, 4}, 4) == 4


# --------------------------------------------------------------------------
# rest
# --------------------------------------------------------------------------
def test_rest_days_none_without_history():
    assert rest.rest_days([], D1) is None


def test_rest_days_diff():
    assert rest.rest_days([rec(D1, 3, 1, 1, 0, True)], D2) == 7


# --------------------------------------------------------------------------
# process_season: temporal / leakage safety
# --------------------------------------------------------------------------
def test_season_openers_have_zero_history():
    rows = process_season(make_season())
    first_two = [r for r in rows if r["api_id"] in (1, 2)]
    for r in first_two:
        assert r["home_team_games_before"] == 0
        assert r["away_team_games_before"] == 0
        assert r["home_rest_days"] is None
        assert r["home_team_points_last_5"] == 0
        assert r["home_position_before_match"] == 1
        assert r["home_points_before_match"] == 0


def test_prematch_standings_and_form_second_matchday():
    rows = {r["api_id"]: r for r in process_season(make_season())}
    # Match 4: T4 (1pt, GD 0 from a draw) hosts T1 (3pts, GD +2 from a win) after matchday 1.
    r = rows[4]
    assert r["home_team_games_before"] == 1
    assert r["home_points_before_match"] == 1
    assert r["home_position_before_match"] == 2
    assert r["away_points_before_match"] == 3
    assert r["away_position_before_match"] == 1
    assert r["position_difference"] == 1
    assert r["points_difference"] == -2
    assert r["home_rest_days"] == 7
    assert r["away_rest_days"] == 7
    # Neither team had played away/home before, so venue stats are 0.
    assert r["away_team_away_win_rate"] == 0.0
    assert r["home_team_home_goals_avg"] == 0.0


def test_no_future_leakage_flipping_last_match():
    base = process_season(make_season())
    changed = make_season()
    changed[-1] = mk(6, 2, 4, 5, 0, D3, game_index=6)
    altered = process_season(changed)
    # Nothing before the last match may change.
    assert base[:-1] == altered[:-1]
    assert base[-1]["match_result"] != altered[-1]["match_result"]


def test_own_result_never_used_as_feature():
    base = process_season(make_season())
    changed = make_season()
    changed[0] = mk(1, 1, 2, 0, 2, D1, game_index=1)  # flip first match home->away win
    altered = process_season(changed)
    keys = [k for k in base[0] if k not in OUTCOME_COLUMNS]
    assert {k: base[0][k] for k in keys} == {k: altered[0][k] for k in keys}
    assert base[0]["match_result"] == "HOME_WIN"
    assert altered[0]["match_result"] == "AWAY_WIN"


def test_deterministic_rebuild():
    assert process_season(make_season()) == process_season(make_season())


def test_validation_passes_on_clean_dataset():
    report = check_dataset(process_season(make_season()))
    assert report["ok"], report["errors"]
    assert report["stats"]["total_rows"] == 6
    assert report["stats"]["train_rows"] == 6


def test_validation_detects_duplicate_api_id():
    rows = process_season(make_season())
    rows[1]["api_id"] = rows[0]["api_id"]
    report = check_dataset(rows)
    assert not report["ok"]
    assert any("duplicate" in e for e in report["errors"])


def test_validation_detects_missing_value():
    rows = process_season(make_season())
    rows[0]["home_team_points_last_5"] = None
    report = check_dataset(rows)
    assert not report["ok"]
    assert any("home_team_points_last_5" in e for e in report["errors"])


def test_validation_detects_out_of_range():
    rows = process_season(make_season())
    rows[0]["home_team_home_win_rate"] = 1.5
    report = check_dataset(rows)
    assert not report["ok"]
    assert any("win rates" in e for e in report["errors"])


def test_validation_allows_rest_nulls_but_flags_them():
    rows = process_season(make_season())
    report = check_dataset(rows)
    assert report["ok"]
    assert any("home_rest_days" in w for w in report["warnings"])
