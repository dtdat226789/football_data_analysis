"""Tests for the Analysis API (backend/apps/routers/analysis.py via main.app).

FastAPI TestClient against a temporary ANALYSIS_DIR - no database, no live
http server. The default league also exercises the flat-report fallback and
the backward-compatible unprefixed alias routes.
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
from apps.main import app  # noqa: E402

MODULE_SAMPLE = {"report_name": "x", "league": "premier"}


@pytest.fixture()
def app_client(tmp_path, monkeypatch):
    monkeypatch.setattr(common, "ANALYSIS_DIR", tmp_path)
    with TestClient(app) as client:
        yield client, tmp_path


def make_league_dir(tmp_path, league, modules):
    d = tmp_path / league
    charts = d / "charts"
    charts.mkdir(parents=True)
    for mod in modules:
        (d / f"{mod}.json").write_text(
            json.dumps({"report_name": mod, "league": league}), encoding="utf-8"
        )
    (charts / f"{league}_top.png").write_bytes(b"\x89PNG\r\n\x1a\nfake")
    return d


# ── /health ─────────────────────────────────────────────────────────────────
def test_health(app_client):
    client, _ = app_client
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["n_leagues"] == len(common.league_config())


def test_health_v1_alias(app_client):
    client, _ = app_client
    r = client.get("/api/v1/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


# ── /leagues ────────────────────────────────────────────────────────────────
def test_leagues_lists_config_with_data_flag(app_client):
    client, tmp_path = app_client
    make_league_dir(tmp_path, "premier", ["matches_analysis", "findings"])
    r = client.get("/leagues")
    assert r.status_code == 200
    slugs = {item["slug"]: item for item in r.json()}
    assert set(slugs) >= {"premier", "spain1", "algir1"}
    assert slugs["premier"]["has_data"] is True
    assert slugs["spain1"]["has_data"] is False
    assert slugs["premier"]["matches"] == 380
    assert slugs["germany1"]["teams"] == 18
    assert slugs["belgium1"]["format"] == "playoff"
    assert slugs["scot-premier"]["format"] == "split"


# ── /leagues/{league}/analysis ───────────────────────────────────────────────
def test_analysis_bundle_present_modules(app_client):
    client, tmp_path = app_client
    make_league_dir(tmp_path, "premier", ["matches_analysis", "findings"])
    r = client.get("/leagues/premier/analysis")
    assert r.status_code == 200
    body = r.json()
    assert body["has_data"] is True
    assert body["meta"]["name"] == "Premier League"
    assert set(body["reports"]) == {"matches_analysis", "findings"}
    assert body["reports"]["matches_analysis"]["league"] == "premier"
    assert "database_profile" in body["missing"]
    assert body["charts"] == ["premier_top.png"]


def test_analysis_bundle_no_data_league(app_client):
    client, _ = app_client
    r = client.get("/leagues/spain1/analysis")
    assert r.status_code == 200
    body = r.json()
    assert body["has_data"] is False
    assert body["reports"] == {}
    assert set(body["missing"]) == set(common.MODULE_NAMES)
    assert body["charts"] == []


def test_analysis_unknown_league_404(app_client):
    client, _ = app_client
    assert client.get("/leagues/no-such-slug/analysis").status_code == 404


def test_analysis_flat_default_league_fallback(app_client):
    client, tmp_path = app_client
    # reports living directly under ANALYSIS_DIR (legacy flat premier layout)
    (tmp_path / "matches_analysis.json").write_text(
        json.dumps({"report_name": "matches_analysis"}), encoding="utf-8"
    )
    r = client.get("/leagues/premier/analysis")
    assert r.status_code == 200
    assert r.json()["reports"]["matches_analysis"]["report_name"] == "matches_analysis"


# ── /leagues/{league}/analysis/{module} ─────────────────────────────────────
def test_module_endpoint_ok(app_client):
    client, tmp_path = app_client
    make_league_dir(tmp_path, "premier", ["matches_analysis"])
    r = client.get("/leagues/premier/analysis/matches_analysis")
    assert r.status_code == 200
    assert r.json()["league"] == "premier"


def test_module_endpoint_missing_report_404(app_client):
    client, _ = app_client
    r = client.get("/leagues/premier/analysis/relationships")
    assert r.status_code == 404


def test_module_endpoint_unknown_module_404(app_client):
    client, _ = app_client
    assert client.get("/leagues/premier/analysis/bogus").status_code == 404


def test_module_endpoint_rejects_unknown_league_404(app_client):
    client, _ = app_client
    assert client.get("/leagues/nope/analysis/matches_analysis").status_code == 404


# ── charts ──────────────────────────────────────────────────────────────────
def test_charts_list_and_download(app_client):
    client, tmp_path = app_client
    make_league_dir(tmp_path, "premier", ["matches_analysis"])
    r = client.get("/leagues/premier/charts")
    assert r.status_code == 200
    assert r.json()["charts"] == ["premier_top.png"]

    r = client.get("/leagues/premier/charts/premier_top.png")
    assert r.status_code == 200
    assert r.headers["content-type"] == "image/png"
    assert r.content == b"\x89PNG\r\n\x1a\nfake"


def test_charts_missing_chart_404(app_client):
    client, tmp_path = app_client
    make_league_dir(tmp_path, "premier", ["matches_analysis"])
    r = client.get("/leagues/premier/charts/nope.png")
    assert r.status_code == 404


def test_chart_traversal_escapes_blocked(app_client):
    client, tmp_path = app_client
    make_league_dir(tmp_path, "premier", ["matches_analysis"])
    outside = tmp_path / "escapee.png"
    outside.write_bytes(b"\x89PNG\r\n\x1a\noutside")
    for path in (
        "/api/v1/analysis/premier/charts/..%2Fescapee.png",
        "/api/v1/analysis/premier/charts/..%2F..%2Fescapee.png",
        "/api/v1/analysis/premier/charts/sibling..png",
    ):
        r = client.get(path)
        assert r.status_code == 404, path


def test_chart_v1_ok(app_client):
    client, tmp_path = app_client
    make_league_dir(tmp_path, "premier", ["matches_analysis"])
    r = client.get("/api/v1/analysis/premier/charts/premier_top.png")
    assert r.status_code == 200
    assert r.content == b"\x89PNG\r\n\x1a\nfake"


def test_charts_no_data_league_404(app_client):
    client, _ = app_client
    assert client.get("/leagues/spain1/charts").status_code == 404
