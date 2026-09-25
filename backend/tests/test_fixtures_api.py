"""Tests for the fixtures API (backend/apps/routers/fixtures.py).

Runs against a temporary fixtures directory (no database, no live server),
so the endpoints are exercised exactly as the dashboard consumes them.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

import apps.common as common  # noqa: E402
from apps import routers  # noqa: E402
from apps.main import app  # noqa: E402

SAMPLE = {
    "league": "primera1",
    "count": 2,
    "matches": [
        {
            "slug": "spain/primera-rfef-group-1/2026-09-26-a-vs-b",
            "home_team": "A", "away_team": "B",
            "match_date": "2026-09-26", "time": "14:30",
            "status": "scheduled", "country": "Spain",
            "model_predictions": {
                "dc_v2": {
                    "calibrated": {"home": 0.52, "away": 0.17, "btts_yes": 0.47,
                                   "over_1.5": 0.70, "over_2.5": 0.44, "over_3.5": 0.24},
                    "raw": {"expected_home_goals": 1.57, "expected_away_goals": 0.84},
                    "computed_at": "2026-09-22T00:00:00+00:00",
                    "data_through": "2026-09-20",
                }
            },
        },
        {
            "slug": "spain/primera-rfef-group-1/2026-09-27-c-vs-d",
            "home_team": "C", "away_team": "D",
            "match_date": "2026-09-27", "time": "16:15",
            "status": "scheduled", "country": "Spain",
            "model_predictions": {
                "dc_v2": {
                    "calibrated": {"home": 0.90, "away": 0.03},
                }
            },
        },
    ],
}


@pytest.fixture()
def fixtures_client(tmp_path, monkeypatch):
    fixtures_dir = tmp_path / "fixtures"
    fixtures_dir.mkdir()
    (fixtures_dir / "primera1.json").write_text(
        json.dumps(SAMPLE), encoding="utf-8"
    )
    ((fixtures_dir / "spain1.json")).write_text(
        json.dumps({
            "league": "spain1", "count": 1,
            "matches": [{
                "slug": "spain/laliga/2026-10-01-e-vs-f",
                "home_team": "E", "away_team": "F",
                "match_date": "2026-10-01", "time": "20:00",
                "status": "scheduled", "country": "Spain",
                "model_predictions": {"dc_v2": {"calibrated": {"home": 0.60, "away": 0.10}}},
            }],
        }),
        encoding="utf-8",
    )
    monkeypatch.setattr(routers.fixtures, "FIXTURES_DIR", fixtures_dir)
    with TestClient(app) as client:
        yield client


def test_merged_sorted_by_confidence(fixtures_client):
    r = fixtures_client.get("/api/v1/fixtures", params={"limit": 10})
    assert r.status_code == 200
    body = r.json()
    assert body["count"] == 3
    confidences = [m["predictions"]["confidence"] for m in body["matches"]]
    assert confidences == sorted(confidences, reverse=True)
    first = body["matches"][0]
    assert first["home_team"] == "C"
    assert first["predictions"]["home"] == 0.90


def test_merged_sorted_by_date(fixtures_client):
    r = fixtures_client.get("/api/v1/fixtures", params={"sort": "date", "limit": 10})
    dates = [m["match_date"] for m in r.json()["matches"]]
    assert dates == sorted(dates)


def test_league_filter(fixtures_client):
    r = fixtures_client.get("/api/v1/fixtures", params={"league": "primera1"})
    assert r.status_code == 200
    body = r.json()
    assert body["count"] == 2
    assert {m["league"] for m in body["matches"]} == {"primera1"}


def test_unknown_league(fixtures_client):
    r = fixtures_client.get("/api/v1/fixtures", params={"league": "nope"})
    assert r.status_code == 404


def test_league_full_payload(fixtures_client):
    r = fixtures_client.get("/api/v1/fixtures/primera1")
    assert r.status_code == 200
    body = r.json()
    assert body["league"] == "primera1"
    assert "model_predictions" in body["matches"][0]


def test_empty_fixtures_dir(tmp_path, monkeypatch):
    import apps.routers.fixtures as fixtures
    monkeypatch.setattr(fixtures, "FIXTURES_DIR", tmp_path / "none")
    with TestClient(app) as client:
        r = client.get("/api/v1/fixtures")
        assert r.status_code == 200
        assert r.json()["matches"] == []