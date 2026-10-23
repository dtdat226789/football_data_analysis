"""Tests for the static dashboard builder (backend/scripts/build_dashboard.py).

The Chart.js vendoring path is exercised offline: ``urllib.request.urlopen`` is
monkeypatched so tests never hit the network. Everything else (report loading,
dataset extraction, HTML templating, per-league empty-state) runs headless.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parents[1]
SCRIPTS = BACKEND / "scripts"
for p in (BACKEND, SCRIPTS):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import build_dashboard as bd  # noqa: E402


def sample_reports() -> dict:
    return {
        "matches_analysis": {
            "overall": {"n_matches": 380, "home_wins": 170, "draws": 80,
                        "away_wins": 130, "home_goals": 1200, "away_goals": 900,
                        "home_win_pct": 44.7, "draw_pct": 21.1, "away_win_pct": 34.2},
        },
        "goals_analysis": {
            "goals_per_season": [
                {"season": "2024-2025", "avg_home": 1.5, "avg_away": 1.1, "avg_goals": 2.6},
                {"season": "2025-2026", "avg_home": 1.6, "avg_away": 1.2, "avg_goals": 2.8},
            ],
            "goals_distribution": {"buckets": [
                {"goals": 0, "count": 40}, {"goals": 1, "count": 90}]},
        },
        "scoreline_analysis": {"scoreline_frequency": {"top": [
            {"scoreline": "1-0", "count": 55}, {"scoreline": "2-1", "count": 40}]}},
        "season_trends": {"champions": [
            {"season": "2025-2026", "champion": "Arsenal", "champion_pts": 90}]},
        "teams_analysis": {"teams": [
            {"team": "Arsenal", "points": 90}, {"team": "Liverpool", "points": 85}]},
        "findings": {"key_findings": [
            {"finding": "Home advantage", "detail": "44.7%", "importance": "high"}],
            "generated_at": "2026-01-01T00:00:00Z"},
    }


def write_reports(analysis_dir: Path, league: str, reports: dict) -> Path:
    league_dir = analysis_dir / league
    league_dir.mkdir(parents=True)
    for stem, payload in reports.items():
        (league_dir / f"{stem}.json").write_text(
            json.dumps(payload), encoding="utf-8")
    return league_dir


def offline_urlopen(monkeypatch):
    def _raise(*_a, **_k):
        raise OSError("offline")
    monkeypatch.setattr(bd.urllib.request, "urlopen", _raise)


# ── dataset extraction ──────────────────────────────────────────────────────
def test_extract_full_dataset_set():
    data = bd.extract_chart_data(sample_reports())
    assert data["order"] == ["outcome", "avg_goals", "goals_dist", "scorelines",
                             "champions", "top_teams"]
    assert data["charts"]["outcome"]["values"] == [170, 80, 130]
    assert data["charts"]["avg_goals"]["labels"] == ["2024-2025", "2025-2026"]
    assert data["charts"]["champions"]["names"] == ["Arsenal"]
    assert data["charts"]["top_teams"]["labels"][:2] == ["Arsenal", "Liverpool"]


def test_extract_partial_reports_degrades_gracefully():
    data = bd.extract_chart_data({"matches_analysis": sample_reports()["matches_analysis"]})
    assert data["order"] == ["outcome"]
    assert data["charts"]["outcome"]["values"] == [170, 80, 130]


def test_extract_empty_reports():
    assert bd.extract_chart_data({})["order"] == []


# ── league collection + empty-state ─────────────────────────────────────────
def test_collect_leagues_has_data_flags(tmp_path, monkeypatch):
    monkeypatch.setattr(bd, "LEAGUE_CONFIG", {"premier": {"name": "Premier League",
        "country": "England", "teams": 20, "format": "round-robin"},
        "spain1": {"name": "La Liga", "country": "Spain", "teams": 20, "format": "round-robin"}})
    write_reports(tmp_path, "premier", sample_reports())
    leagues = bd.collect_leagues(bd.LEAGUE_CONFIG, tmp_path, None)
    by_slug = {l["slug"]: l for l in leagues}
    assert by_slug["premier"]["has_data"] is True
    assert by_slug["premier"]["findings"][0]["finding"] == "Home advantage"
    assert by_slug["spain1"]["has_data"] is False
    assert set(by_slug["spain1"]) == {"slug", "name", "country", "teams", "format", "has_data"}


def test_collect_leagues_only_filter(tmp_path, monkeypatch):
    monkeypatch.setattr(bd, "LEAGUE_CONFIG", {"premier": {"name": "P"},
        "spain1": {"name": "S"}})
    write_reports(tmp_path, "premier", sample_reports())
    leagues = bd.collect_leagues(bd.LEAGUE_CONFIG, tmp_path, "premier")
    assert [l["slug"] for l in leagues] == ["premier"]


# ── vendoring ───────────────────────────────────────────────────────────────
def test_vendor_chartjs_reuses_existing_copy(tmp_path, monkeypatch):
    target = tmp_path / "chart.umd.min.js"
    target.write_bytes(b"/*! chart.js */")
    offline_urlopen(monkeypatch)
    result = bd.vendor_chartjs(tmp_path, refresh=False)
    assert result == target


def test_vendor_chartjs_offline_build(tmp_path, monkeypatch):
    offline_urlopen(monkeypatch)
    result = bd.vendor_chartjs(tmp_path, refresh=False)
    assert result is None


def test_vendor_chartjs_rejects_bad_payload(tmp_path, monkeypatch):
    class FakeResp:
        def read(self):
            return b"tiny"
    monkeypatch.setattr(bd.urllib.request, "urlopen", lambda *a, **k: FakeResp())
    assert bd.vendor_chartjs(tmp_path, refresh=True) is None


# ── HTML templating ─────────────────────────────────────────────────────────
def test_build_html_embeds_payload_and_no_markers(tmp_path, monkeypatch):
    monkeypatch.setattr(bd, "LEAGUE_CONFIG", {"premier": {"name": "Premier League"},
        "spain1": {"name": "La Liga"}})
    write_reports(tmp_path, "premier", sample_reports())
    leagues = bd.collect_leagues(bd.LEAGUE_CONFIG, tmp_path, None)
    html = bd.build_html(leagues, vendor_ok=True, analysis_dir=tmp_path, out_dir=tmp_path)
    assert "__DATA_JSON__" not in html and "__VENDOR_SRC__" not in html
    assert "vendor/chart.umd.min.js" in html
    assert "premier" in html and "spain1" in html
    payload = json.loads(html.split("const DATA = ", 1)[1].split(";", 1)[0])
    assert payload["chartjs"] is True
    assert payload["leagues"][0]["has_data"] is True


def test_build_html_offline_degrades(tmp_path, monkeypatch):
    monkeypatch.setattr(bd, "LEAGUE_CONFIG", {"premier": {"name": "P"}})
    write_reports(tmp_path, "premier", sample_reports())
    leagues = bd.collect_leagues(bd.LEAGUE_CONFIG, tmp_path, None)
    html = bd.build_html(leagues, vendor_ok=False, analysis_dir=tmp_path, out_dir=tmp_path)
    assert "Chart.js unavailable" in html
    assert "src=\"\"" in html
    payload = json.loads(html.split("const DATA = ", 1)[1].split(";", 1)[0])
    assert payload["chartjs"] is False


# ── end-to-end (headless) ───────────────────────────────────────────────────
def test_build_dashboard_main_offline(tmp_path, monkeypatch, capsys):
    offline_urlopen(monkeypatch)
    write_reports(tmp_path, "premier", sample_reports())
    out = tmp_path / "out"
    rc = bd.main(["--analysis-dir", str(tmp_path), "--out-dir", str(out)])
    assert rc == 0
    html = (out / "dashboard.html").read_text(encoding="utf-8")
    assert "Chart.js unavailable" in html
    log = capsys.readouterr().out
    assert "leagues with data : 1 (premier)" in log
    assert not (tmp_path / "vendor" / "chart.umd.min.js").exists()
