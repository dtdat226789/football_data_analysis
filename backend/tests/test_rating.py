from __future__ import annotations

import pytest

from apps.rating import club_ratings


def row(team_id, played, points=None, gf=None, ga=None, metrics=None):
    return {
        "season": "2024-2025",
        "team_id": team_id,
        "played": played,
        "points": points,
        "goals_for": gf,
        "goals_against": ga,
        "metrics": metrics or {},
    }


ROWS = [
    row(1, 10, 24, 20, 10, {"expected_points": 22, "last_5_points": 9}),
    row(2, 10, 12, 12, 18, {"expected_points": 14, "last_5_points": 3}),
    row(3, 5, 6, 5, 10, {"expected_points": 6, "last_5_points": 6}),
    row(4, 10, 4, 8, 25),
    row(5, 0, 0, 0, 0),
]


def test_club_ratings_composite_weights_and_missing_signals():
    ratings = club_ratings(ROWS)

    assert set(ratings) == {1, 2, 3, 4}
    assert ratings[1]["score"] == 100.0
    assert ratings[2]["score"] == pytest.approx(29.2)
    assert ratings[3]["score"] == pytest.approx(28.0)
    assert ratings[4]["score"] == 0.0

    assert ratings[1]["rank"] == 1
    assert ratings[2]["rank"] == 2
    assert ratings[3]["rank"] == 3
    assert ratings[4]["rank"] == 4
    assert all(rating["rank_total"] == 4 for rating in ratings.values())

    assert ratings[2]["signals"]["expected_points_per_game"] == pytest.approx(0.2)
    assert ratings[3]["signals"]["last_5_points_rate"] == pytest.approx(0.5)
    assert ratings[4]["signals"] == {
        "points_per_game": 0.0,
        "goal_difference_per_game": 0.0,
    }


def test_club_ratings_flat_values_are_neutral_and_tied():
    ratings = club_ratings([row(1, 4, 6, 8, 6), row(2, 4, 6, 8, 6)])

    assert all(rating["score"] == 50.0 for rating in ratings.values())
    assert all(rating["rank"] == 1 for rating in ratings.values())
    assert all(rating["rank_total"] == 2 for rating in ratings.values())
    assert ratings[1]["signals"]["points_per_game"] == 0.5


def test_club_ratings_skips_teams_without_matches_or_id():
    ratings = club_ratings([row(1, 2, 6, 5, 2), {"played": 2, "points": 6}, row(2, 0, 0, 0, 0)])

    assert list(ratings) == [1]
    assert ratings[1]["rank_total"] == 1


def test_club_ratings_tolerates_unreadable_inputs():
    ratings = club_ratings([row(1, 1), row(2, 3, "n/a", None, 2, {"expected_points": "n/a"})])

    assert all(rating["score"] == 50.0 for rating in ratings.values())
    assert all(rating["signals"] == {} for rating in ratings.values())
    assert all(rating["rank"] == 1 for rating in ratings.values())


def test_club_ratings_reads_numeric_strings():
    ratings = club_ratings(
        [
            row(10, "3", "6", "6", "3", {"expected_points": "4.5", "last_5_points": "6"}),
            row(11, 3, 3, 3, 6, {"expected_points": 1.5, "last_5_points": 0}),
        ],
    )

    assert ratings[10]["score"] == 100.0
    assert ratings[11]["score"] == 0.0
    assert ratings[10]["signals"]["last_5_points_rate"] == 1.0
