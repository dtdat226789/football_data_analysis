"""Tests for the sample-style dashboard aggregation helpers and API routes."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from apps.routers import kpi  # noqa: E402

ROWS = [
    {
        "season": "2024-2025",
        "team_id": 1,
        "api_name": "Alpha",
        "api_slug": "alpha",
        "position": 1,
        "played": 2,
        "points": 4,
        "goals_for": 5,
        "goals_against": 1,
        "metrics": {"expected_points": 3.8},
    },
    {
        "season": "2024-2025",
        "team_id": 2,
        "api_name": "Beta FC",
        "api_slug": "beta-fc",
        "position": 2,
        "played": 2,
        "points": 1,
        "goals_for": 2,
        "goals_against": 4,
        "metrics": {"expected_points": 2.1},
    },
]

MATCHES = [
    {
        "match_date": "2025-01-01",
        "home_team_id": 1,
        "away_team_id": 2,
        "home_score": 3,
        "away_score": 0,
        "home_team": "Alpha",
        "away_team": "Beta FC",
    },
    {
        "match_date": "2025-01-08",
        "home_team_id": 2,
        "away_team_id": 1,
        "home_score": 1,
        "away_score": 2,
        "home_team": "Beta FC",
        "away_team": "Alpha",
    },
]


def test_ranks_share_ties_and_skip_missing():
    assert kpi.ranks({1: 10, 2: 10, 3: 5, 4: None}) == {1: 1, 2: 1, 3: 3, 4: None}
    assert kpi.ranks({1: 1, 2: 4, 3: None}, lower_is_better=True) == {1: 1, 2: 2, 3: None}


@pytest.mark.parametrize(
    ("name", "expected"),
    [("Liverpool", "LIV"), ("Manchester City", "MC"), ("Manchester Utd", "MU"), (None, "—")],
)
def test_short_label(name, expected):
    assert kpi.short_label(name) == expected


def test_build_team_kpi_groups_ranks_and_table():
    payload = kpi.build_team_kpi(ROWS, MATCHES, team_id=1, n=2)
    assert [g["key"] for g in payload["groups"]] == [key for key, _ in kpi.GROUPS]
    assert all(len(g["tiles"]) == 2 for g in payload["groups"])

    tiles = {tile["key"]: tile for group in payload["groups"] for tile in group["tiles"]}
    assert tiles["pointsPerGame"]["value"] == 2.0
    assert tiles["pointsPerGame"]["rank"] == 1
    assert tiles["goalsAgainstPerGame"]["value"] == 0.5
    assert tiles["goalsAgainstPerGame"]["rank"] == 1
    assert tiles["cleanSheetPct"]["value"] == 50.0
    assert tiles["last5GoalsPerGame"]["value"] == 2.5
    assert tiles["last5GoalsPerGame"]["rank"] is None

    assert [m["opponent"] for m in payload["last_matches"]] == ["Beta FC", "Beta FC"]
    assert payload["last_matches"][0]["result"] == "W"
    assert payload["table"][0]["expected_points"] == 3.8
    assert payload["table"][0]["rating"] == 100.0
    assert payload["table"][1]["rating"] == 0.0
    assert payload["club_rating"]["score"] == 100.0
    assert payload["club_rating"]["rank"] == 1
    assert payload["club_rating"]["rank_total"] == 2
    assert payload["table"][0]["is_selected"] is True


def test_build_team_kpi_handles_one_game_and_empty_data():
    assert len(kpi.build_team_kpi(ROWS, MATCHES, 2, 1)["last_matches"]) == 1
    empty = kpi.build_team_kpi([], [], 9, 5)
    assert empty["last_matches"] == []
    assert empty["table"] == []
    assert empty["club_rating"] is None
    assert all(tile["value"] is None for group in empty["groups"] for tile in group["tiles"])


def test_build_club_payload_cards_timeline_and_ranking():
    teams = [
        {"id": 1, "name": "Alpha", "slug": "alpha"},
        {"id": 2, "name": "Beta FC", "slug": "beta-fc"},
    ]
    payload = kpi.build_club_payload(ROWS, [{"season": "2024-2025"}], teams, 1, "2024-2025")
    assert [card["key"] for card in payload["kpis"]] == [
        "clubRating",
        "totalGoals",
        "goalsPerGame",
        "goalsAgainstPerGame",
        "expectedPoints",
    ]
    assert payload["kpis"][0]["value"] == 100.0
    assert payload["kpis"][0]["rank"] == 1
    assert payload["kpis"][0]["rank_total"] == 2
    assert payload["kpis"][1]["value"] == 5.0
    assert payload["kpis"][4]["value"] == 3.8
    assert payload["timeline"] == [{"season": "2024-2025", "value": 2.5}]
    assert [row["team"] for row in payload["ranking"]] == ["Alpha", "Beta FC"]
    assert [row["rating"] for row in payload["ranking"]] == [100.0, 0.0]
    assert payload["ranking"][0]["is_selected"] is True
    assert payload["team"]["slug"] == "alpha"
    assert payload["attribution"] == kpi.ATTRIBUTION


def test_build_club_payload_without_rows_is_empty():
    payload = kpi.build_club_payload([], [], [], -1, "2024-2025")
    assert payload["kpis"][0] == {"key": "clubRating", "value": None, "rank": None, "rank_total": 0}
    assert payload["kpis"][1]["value"] is None
    assert payload["timeline"] == []
    assert payload["ranking"] == []
    assert payload["team"] == {"slug": None, "name": None}


def _db_reachable() -> bool:
    try:
        from apps.deps import get_conn
    except Exception:
        return False
    try:
        conn = get_conn()
        conn.close()
        return True
    except Exception:
        return False


@pytest.mark.skipif(not _db_reachable(), reason="PostgreSQL not reachable")
def test_team_kpi_endpoint():
    from apps.main import app

    with TestClient(app) as client:
        response = client.get("/api/v1/teams/liverpool/kpi", params={"league": "premier"})
        assert response.status_code == 200
        body = response.json()
        assert body["team"] == "liverpool"
        assert len(body["groups"]) == len(kpi.GROUPS)
        assert isinstance(body["last_matches"], list)
        assert isinstance(body["table"], list)


@pytest.mark.skipif(not _db_reachable(), reason="PostgreSQL not reachable")
def test_club_analysis_endpoint():
    from apps.main import app

    with TestClient(app) as client:
        response = client.get("/api/v1/club-analysis", params={"league": "premier"})
        assert response.status_code == 200
        body = response.json()
        assert body["league"] == "premier"
        assert body["season"]
        assert body["teams"]
        assert isinstance(body["ranking"], list)
