"""Unit tests for the POC raw-data collector (no network access)."""
from __future__ import annotations

import time
from pathlib import Path

import pytest

from scripts.collect_raw_data import collect_file, collect_league


@pytest.fixture(autouse=True)
def _stub_time(monkeypatch):
    monkeypatch.setattr(time, "sleep", lambda *_: None)


@pytest.fixture()
def stub_get(monkeypatch):
    def _set(content=b'{"ok": true}', failures=None):
        state = {"failures": dict(failures or {}), "calls": []}

        def fake_get_raw(client, url, params=None, max_retries=3):
            state["calls"].append((url, params))
            key = url
            remaining = state["failures"].get(key, 0)
            if remaining:
                state["failures"][key] = remaining - 1
                return None
            return content

        monkeypatch.setattr("scripts.collect_raw_data.get_raw", fake_get_raw)
        return state

    return _set


def test_collect_file_writes_raw_bytes(tmp_path, stub_get):
    stub_get(b"\x00\x01raw-payload")
    out = tmp_path / "league" / "season" / "results.json"
    collect_file(object(), "/leagues/x/results/", {"season": "2020-2021"}, out, False, 0.0)
    assert out.read_bytes() == b"\x00\x01raw-payload"


def test_collect_file_skips_existing(tmp_path, stub_get):
    out = tmp_path / "results.json"
    out.write_text("old")
    state = stub_get(b"new")
    collect_file(object(), "/leagues/x/results/", None, out, False, 0.0)
    assert out.read_text() == "old"
    assert state["calls"] == []


def test_collect_file_overwrite_redownloads(tmp_path, stub_get):
    out = tmp_path / "results.json"
    out.write_text("old")
    state = stub_get(b"new")
    collect_file(object(), "/leagues/x/results/", None, out, True, 0.0)
    assert out.read_bytes() == b"new"
    assert len(state["calls"]) == 1


def test_collect_file_skips_on_unavailable(tmp_path, stub_get):
    out = tmp_path / "results.json"
    state = stub_get(failures={"/leagues/x/results/": 1})
    collect_file(object(), "/leagues/x/results/", None, out, False, 0.0)
    assert not out.exists()


def test_collect_league_layout(tmp_path, stub_get, monkeypatch):
    stub_get(b"{}")
    monkeypatch.setattr("scripts.collect_raw_data.OUTPUT_DIR", tmp_path)
    collect_league(object(), "premier", ["2020-2021", "2021-2022"], ["classic", "luck"], False, 0.0)

    expected = [
        tmp_path / "premier" / "leagues.json",
        tmp_path / "premier" / "2020-2021" / "teams.json",
        tmp_path / "premier" / "2020-2021" / "results.json",
        tmp_path / "premier" / "2020-2021" / "table_classic.json",
        tmp_path / "premier" / "2020-2021" / "table_luck.json",
        tmp_path / "premier" / "2021-2022" / "teams.json",
        tmp_path / "premier" / "2021-2022" / "results.json",
        tmp_path / "premier" / "2021-2022" / "table_classic.json",
        tmp_path / "premier" / "2021-2022" / "table_luck.json",
    ]
    written = sorted(p for p in tmp_path.rglob("*.json"))
    assert written == sorted(expected)