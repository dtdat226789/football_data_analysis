"""DB-free tests for ml/sql_check.py using a stubbed connection.

The check exists to catch disagreement between the Python feature build and
PostgreSQL, so what matters is that it queries the *right* league and season
scope. These tests pin both without needing a live database.
"""
from __future__ import annotations

import json

import pytest

from ml import db
from ml.sql_check import DB_ROWS_QUERY, main, run


class _StubCursor:
    def __init__(self, rows):
        self._rows = rows
        self.executed: list[tuple[str, object]] = []

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def execute(self, sql, params=None):
        self.executed.append((sql, params))

    def fetchall(self):
        return self._rows


class _StubConn:
    def __init__(self, rows):
        self._rows = rows
        self.closed = False
        self.executed: list[tuple[str, object]] = []

    def cursor(self, cursor_factory=None):
        conn = self

        class _C(_StubCursor):
            def execute(self, sql, params=None):
                conn.executed.append((sql, params))
                super().execute(sql, params)

        return _C(self._rows)

    def close(self):
        self.closed = True


@pytest.fixture
def stub_db(monkeypatch):
    def install(rows):
        conn = _StubConn(rows)
        monkeypatch.setattr(db, "get_conn", lambda: conn)
        return conn

    return install


def _dataset_row(api_id, home_score, away_score, home_id=1, away_id=2):
    return {
        "api_id": api_id,
        "home_score": home_score,
        "away_score": away_score,
        "home_team_id": home_id,
        "away_team_id": away_id,
    }


def _db_row(api_id, home_score, away_score):
    return {"api_id": api_id, "home_score": home_score, "away_score": away_score}


def test_run_defaults_to_the_module_league(stub_db):
    conn = stub_db([_db_row(1, 2, 0)])
    run([_dataset_row(1, 2, 0)])
    sql, params = conn.executed[0]
    assert sql == DB_ROWS_QUERY
    assert params == (db.LEAGUE,)


def test_run_queries_the_requested_league(stub_db):
    # Regression: run() ignored the league and always compared against
    # db.LEAGUE, so a --league spain1 build could never pass.
    conn = stub_db([_db_row(1, 2, 0)])
    report = run([_dataset_row(1, 2, 0)], "spain1")
    assert conn.executed[0][1] == ("spain1",)
    assert report["league"] == "spain1"
    assert report["ok"] is True


def test_db_query_is_scoped_to_complete_seasons():
    # Must mirror load_matches, or the two sides count different rows.
    assert "ls.season_state = 'complete'" in DB_ROWS_QUERY


def test_run_reports_api_id_mismatch(stub_db):
    stub_db([_db_row(1, 2, 0), _db_row(2, 0, 1)])
    report = run([_dataset_row(1, 2, 0)])
    assert report["ok"] is False
    assert any("api_id mismatch" in p for p in report["problems"])


def test_run_reports_score_mismatch(stub_db):
    stub_db([_db_row(1, 5, 0)])
    report = run([_dataset_row(1, 2, 0)])
    assert report["ok"] is False
    assert any("score mismatch" in p for p in report["problems"])


def test_run_reports_row_count_mismatch(stub_db):
    # A season-scope disagreement surfaces as a count mismatch alongside the id
    # mismatch, which is why both are reported.
    stub_db([_db_row(1, 2, 0), _db_row(2, 1, 1)])
    report = run([_dataset_row(1, 2, 0), _dataset_row(2, 1, 1), _dataset_row(3, 0, 1)])
    assert report["ok"] is False
    assert report["db_rows"] == 2
    assert any("row count mismatch" in p for p in report["problems"])
    assert any("api_id mismatch" in p for p in report["problems"])


def test_run_reports_self_aware_row(stub_db):
    stub_db([_db_row(1, 2, 0)])
    report = run([_dataset_row(1, 2, 0, home_id=7, away_id=7)])
    assert report["ok"] is False
    assert any("both home and away" in p for p in report["problems"])


def test_run_passes_on_matching_data(stub_db):
    stub_db([_db_row(1, 2, 0), _db_row(2, 1, 1)])
    report = run([_dataset_row(1, 2, 0), _dataset_row(2, 1, 1)])
    assert report == {"ok": True, "problems": [], "db_rows": 2, "league": db.LEAGUE}


def test_run_closes_the_connection(stub_db):
    conn = stub_db([_db_row(1, 2, 0)])
    run([_dataset_row(1, 2, 0)])
    assert conn.closed is True


def test_main_passes_league_through(tmp_path, monkeypatch, stub_db, capsys):
    captured = {}

    def fake_run(rows, league=None):
        captured["league"] = league
        return {"ok": True, "problems": [], "db_rows": len(rows), "league": league}

    monkeypatch.setattr("ml.sql_check.run", fake_run)
    path = tmp_path / "ds.json"
    path.write_text(json.dumps([_dataset_row(1, 2, 0)]))
    assert main([str(path), "--league", "spain1"]) == 0
    assert captured["league"] == "spain1"
    assert json.loads(capsys.readouterr().out)["league"] == "spain1"


def test_main_returns_nonzero_when_the_check_fails(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(
        "ml.sql_check.run",
        lambda rows, league=None: {"ok": False, "problems": ["boom"], "db_rows": 0, "league": league},
    )
    path = tmp_path / "ds.json"
    path.write_text(json.dumps([_dataset_row(1, 2, 0)]))
    assert main([str(path)]) == 1
