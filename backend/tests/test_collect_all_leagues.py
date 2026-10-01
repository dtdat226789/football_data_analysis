"""Unit tests for collect_all_leagues season resolution (no network, no subprocess).

The daily refresh re-requests results and tables for every catalog league. Doing
that for every season on disk means re-downloading ~1,000 immutable historical
files each night, so --active-only narrows a run to the seasons still in
progress. These tests pin both the narrowing and the guarantee that a narrowed
run never ends up with nothing to collect.
"""
from __future__ import annotations

from datetime import date
from unittest.mock import Mock

import scripts.collect_all_leagues as cal

TODAY = date(2026, 9, 28)

CATALOG = {
    "premier": {"teams": 20, "seasons": ["2026-2027", "2025-2026"]},
    "germany1": {"teams": 18, "seasons": ["2026-2027", "2025-2026"]},
    "norway": {"teams": 16, "seasons": ["2026", "2025"]},
}


def test_active_seasons_keeps_only_live_seasons():
    assert cal.active_seasons(["2026-2027", "2025-2026"], TODAY) == ["2026-2027"]


def test_active_seasons_handles_calendar_year_labels():
    assert cal.active_seasons(["2026", "2025"], TODAY) == ["2026"]


def test_active_seasons_keeps_overlapping_league_splits():
    # japan1 runs a split season and a calendar-year competition at once.
    assert cal.active_seasons(["2026-2027", "2026"], TODAY) == ["2026-2027", "2026"]


def test_active_seasons_falls_back_to_newest_when_nothing_is_live():
    assert cal.active_seasons(["2020-2021", "2021-2022", "2022-2023"], TODAY) == ["2022-2023"]


def test_active_seasons_empty_input_stays_empty():
    assert cal.active_seasons([], TODAY) == []


def test_resolve_seasons_defaults_to_full_history(monkeypatch):
    monkeypatch.setattr(cal, "league_season_dirs", lambda league: ["2020-2021", "2021-2022"])
    seasons = cal.resolve_seasons(CATALOG, "premier", [], today=TODAY)
    assert seasons[:2] == ["2026-2027", "2025-2026"]
    assert "2020-2021" in seasons


def test_resolve_seasons_active_only_drops_history(monkeypatch):
    monkeypatch.setattr(cal, "league_season_dirs", lambda league: ["2020-2021", "2021-2022", "2022-2023"])
    assert cal.resolve_seasons(CATALOG, "premier", [], active_only=True, today=TODAY) == ["2026-2027"]


def test_resolve_seasons_active_only_uses_already_collected_dirs(monkeypatch):
    # A season that is live but absent from the catalog must still be collected.
    monkeypatch.setattr(cal, "league_season_dirs", lambda league: ["2026-2027", "2025-2026"])
    assert cal.resolve_seasons(CATALOG, "germany1", [], active_only=True, today=TODAY) == ["2026-2027"]


def test_cli_seasons_override_active_only(monkeypatch):
    monkeypatch.setattr(cal, "league_season_dirs", lambda league: [])
    seasons = cal.resolve_seasons(CATALOG, "premier", ["2019-2020"], active_only=True, today=TODAY)
    assert seasons == ["2019-2020"]


def test_league_with_no_seasons_falls_back_to_collected(monkeypatch):
    monkeypatch.setattr(cal, "league_season_dirs", lambda league: [])
    seasons = cal.resolve_seasons({"premier": {"teams": 20}}, "premier", [], today=TODAY)
    assert seasons == list(cal.COLLECTED_SEASONS)


def test_load_catalog_missing_file_is_empty(tmp_path):
    assert cal.load_catalog(tmp_path / "nope.json") == {}


def test_load_catalog_invalid_json_is_empty(tmp_path):
    p = tmp_path / "league_teams.json"
    p.write_text("{not json", encoding="utf-8")
    assert cal.load_catalog(p) == {}


def test_main_skips_league_with_no_resolvable_season(monkeypatch, capsys):
    monkeypatch.setattr(cal, "load_catalog", lambda path: {"premier": {"teams": 20, "seasons": []}})
    monkeypatch.setattr(cal, "league_season_dirs", lambda league: [])
    monkeypatch.setattr(cal, "COLLECTED_SEASONS", [])
    # With no seasons at all the collector must be skipped, not invoked bare --
    # an empty --season list would make collect_raw_data.py fall back to its own
    # six-season default and silently re-download history.
    run_collect = Mock(side_effect=AssertionError("run_collect must not be called"))
    monkeypatch.setattr(cal, "run_collect", run_collect)
    assert cal.main(["--league", "premier"]) == 0
    assert "no season to collect" in capsys.readouterr().out
    run_collect.assert_not_called()


def test_main_reports_failure_exit_code(monkeypatch, capsys):
    monkeypatch.setattr(cal, "load_catalog", lambda path: CATALOG)
    monkeypatch.setattr(cal, "league_season_dirs", lambda league: [])
    monkeypatch.setattr(cal, "run_collect", lambda *a, **k: 1)
    assert cal.main(["--league", "premier"]) == 1
    assert "1 league(s) failed" in capsys.readouterr().out
