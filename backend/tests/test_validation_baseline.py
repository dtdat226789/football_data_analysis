"""Tests for the validation baseline gate used by refresh_data.sh."""
from __future__ import annotations

import json

from scripts import validation_baseline as vb


def write_tally(path, rows):
    path.write_text("".join(f"{league} {errors} {warnings}\n" for league, errors, warnings in rows), encoding="utf-8")
    return path


def test_read_tally_marks_untrusted_reports(tmp_path):
    tally = write_tally(tmp_path / "tally.txt", [("premier", 2, 5), ("broken", "-", "-")])
    assert vb.read_tally(tally) == {"premier": (2, 5), "broken": None}


def test_read_baseline_tolerates_missing_and_corrupt_files(tmp_path):
    assert vb.read_baseline(tmp_path / "absent.json") == {}
    broken = tmp_path / "broken.json"
    broken.write_text("not json", encoding="utf-8")
    assert vb.read_baseline(broken) == {}


def test_no_baseline_records_known_backlog_without_blocking(tmp_path):
    result = vb.compare({"premier": (3, 7), "italy1": (0, 2)}, {})
    assert result["blocking"] is False
    assert result["totals"] == {"errors": 3, "warnings": 9}
    assert result["untracked"] == []


def test_regression_blocks_but_improvement_does_not():
    baseline = {"premier": (3, 7), "italy1": (2, 4)}
    worse = vb.compare({"premier": (4, 7), "italy1": (1, 4)}, baseline)
    assert worse["blocking"] is True
    assert worse["worsened"] == [{"league": "premier", "before": 3, "after": 4}]

    better = vb.compare({"premier": (1, 7), "italy1": (2, 4)}, baseline)
    assert better["blocking"] is False
    assert better["improved"] == ["premier"]


def test_new_league_with_errors_blocks_only_after_a_baseline_exists():
    baseline = {"premier": (0, 1)}
    assert vb.compare({"premier": (0, 1), "new": (1, 0)}, {})["blocking"] is False
    result = vb.compare({"premier": (0, 1), "new": (1, 0)}, baseline)
    assert result["blocking"] is True
    assert result["untracked"] == ["new"]


def test_unusable_reports_block():
    result = vb.compare({"premier": None, "italy1": (0, 1)}, {"premier": (0, 1)})
    assert result["blocking"] is True
    assert result["missing"] == ["premier"]


def test_main_updates_baseline_only_on_a_clean_run(tmp_path):
    tally = write_tally(tmp_path / "tally.txt", [("premier", 2, 3)])
    baseline = tmp_path / "baseline.json"
    status = tmp_path / "status.json"

    assert vb.main(["--tally", str(tally), "--baseline", str(baseline), "--status", str(status)]) == 0
    assert json.loads(status.read_text())["blocking"] is False
    assert json.loads(baseline.read_text())["counts"] == {"premier": [2, 3]}

    write_tally(tally, [("premier", 5, 3)])
    assert vb.main(["--tally", str(tally), "--baseline", str(baseline), "--status", str(status)]) == 0
    assert json.loads(status.read_text())["blocking"] is True
    assert json.loads(baseline.read_text())["counts"] == {"premier": [2, 3]}
