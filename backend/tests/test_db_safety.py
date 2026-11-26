"""Tests for non-destructive database safety helpers."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest

from scripts import build_database
from scripts.build_database import is_local_database
from scripts.compare_row_counts import compare_counts


@pytest.mark.parametrize(
    ("dsn", "expected"),
    [
        ("postgresql://u:p@localhost/db", True),
        ("postgresql://u:p@127.0.0.1:5432/db", True),
        ("postgresql://u:p@[::1]:5432/db", True),
        ("postgresql://u:p@neon.example.com/db", False),
        ("sqlite:///football.db", False),
    ],
)
def test_is_local_database(dsn, expected):
    assert is_local_database(dsn) is expected


def test_compare_counts_ignores_growth_and_new_tables():
    assert compare_counts({"matches": 10}, {"matches": 12, "teams": 20}) == []


def test_compare_counts_reports_data_loss():
    issues = compare_counts(
        {"matches": 10, "teams": 20, "seasons": 3},
        {"matches": 9, "teams": 20, "seasons": 1},
    )
    assert issues == ["matches: 10 -> 9", "seasons: 3 -> 1"]


def test_reset_drops_the_migration_ledger():
    path = Path(__file__).resolve().parents[2] / "sql" / "00_reset.sql"
    block = re.search(r"DROP TABLE IF EXISTS(.*?)CASCADE;", path.read_text(), re.S)
    assert block is not None
    names = {line.strip().rstrip(",") for line in block.group(1).splitlines() if line.strip()}
    assert "schema_migrations" in names


def test_migrations_directory_is_tracked():
    path = Path(__file__).resolve().parents[2] / "sql" / "migrations"
    assert path.is_dir()


@pytest.mark.parametrize("reset", [True, False])
def test_main_always_runs_migrations(monkeypatch, reset):
    calls = []

    def fake_run(cmd, *_args, **_kwargs):
        calls.append(Path(cmd[1]).name)
        return subprocess.CompletedProcess(cmd, 0)

    monkeypatch.setattr(build_database, "reset_database", lambda: calls.append("reset"))
    monkeypatch.setattr(build_database.subprocess, "run", fake_run)

    argv = ["--reset-local"] if reset else []
    assert build_database.main(argv) == 0

    expected = ["reset"] if reset else []
    expected.append("migrate.py")
    expected.extend(Path(step).name for step in build_database.STEPS)
    assert calls == expected
