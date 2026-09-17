"""Unit tests for the POC raw-data validator (no network access).

Synthetic datasets are written to a tmp directory and the validator's global
OUTPUT_DIR is pointed at it; ISSUES are cleared per build_report() call.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

import scripts.validate_raw_data as v
from scripts.validate_raw_data import (
    ISSUES,
    SEVERITY_ERROR,
    SEVERITY_PASS,
    SEVERITY_WARNING,
    build_report,
)

LEAGUE = "premier"
SEASONS = ["2020-2021", "2021-2022"]
VIEWS = ["classic", "luck", "goals"]

NAMES = ["Arsenal", "Manchester City", "Liverpool", "Chelsea"]


def team_entry(name, position):
    return {
        "team": name,
        "slug": "-".join(name.lower().split()),
        "position": position,
        "points": (20 - position) * 3,
        "played": 38,
        "logo_url": f"https://x/{name}.png",
    }


def league_entry():
    return {
        "leagues": [
            {"league": "premier", "name": "Premier League", "country": "England",
             "seasons": ["2026-2027", "2025-2026"], "url": "https://x/premier"},
        ],
        "count": 1,
        "season_window": "current + previous season (free tier)",
        "attribution": "Data by football-charts.com",
    }


def match_entry(i, *, score="2:1", ht="1:0", goalless=False, fgt=12, fgte=0, date="2020-09-12", id_offset=0):
    return {
        "id": 1000 + id_offset + i,
        "game_index": i,
        "date": date,
        "time": "15:00:00",
        "homeTeam": NAMES[(i - 1) % 2],
        "awayTeam": NAMES[(i) % 2 + 2] if i % 2 else NAMES[(i - 1) % 2 + 2],
        "score": score,
        "ht_result": ht,
        "first_goal_time": fgt if not goalless else None,
        "first_goal_time_extra": fgte if not goalless else 0,
        "goalless": goalless,
    }


def results_payload(season, matches):
    return {
        "league": LEAGUE,
        "season": season,
        "count": len(matches),
        "matches": matches,
        "attribution": "Data by football-charts.com",
        "current_season": "2026-2027",
        "season_state": "complete",
    }


def teams_payload(season, teams):
    return {
        "league": LEAGUE,
        "season": season,
        "teams": teams,
        "attribution": "Data by football-charts.com",
    }


def table_payload(season, view, rows):
    return {
        "league": LEAGUE,
        "season": season,
        "view": view,
        "table": rows,
        "attribution": "Data by football-charts.com",
        "current_season": "2026-2027",
        "season_state": "complete",
    }


def table_row(name, position):
    return {
        "id": position + 90000,
        "team": name,
        "position": position,
        "played": 38, "won": 20, "drawn": 9, "lost": 9,
        "goals_for": 50, "goals_against": 30, "goal_difference": 20, "points": 69,
    }


def write_run(root: Path, *, n_teams=4, n_matches=4, seasons=SEASONS):
    """Write a minimal-but-valid dataset. Returns per-season team names."""
    (root / LEAGUE).mkdir(parents=True, exist_ok=True)
    (root / LEAGUE / "leagues.json").write_text(json.dumps(league_entry()), encoding="utf-8")
    for season in seasons:
        d = root / LEAGUE / season
        d.mkdir(parents=True, exist_ok=True)
        id_offset = 100000 * (1 + seasons.index(season))
        match_date = f"{int(season.split('-')[0])}-09-12"
        teams = [team_entry(NAMES[i], i + 1) for i in range(n_teams)]
        (d / "teams.json").write_text(json.dumps(teams_payload(season, teams)), encoding="utf-8")
        matches = [match_entry(i, id_offset=id_offset, date=match_date) for i in range(1, n_matches + 1)]
        (d / "results.json").write_text(json.dumps(results_payload(season, matches)), encoding="utf-8")
        for view in VIEWS:
            rows = [table_row(NAMES[i], i + 1) for i in range(n_teams)]
            (d / f"table_{view}.json").write_text(json.dumps(table_payload(season, view, rows)), encoding="utf-8")
    return teams


@pytest.fixture()
def dataset(tmp_path, monkeypatch) -> Path:
    monkeypatch.setattr(v, "OUTPUT_DIR", tmp_path)
    write_run(tmp_path)
    return tmp_path


def codes() -> list[str]:
    return [i["code"] for i in ISSUES]


def run_convenience(seasons=SEASONS, views=VIEWS):
    return build_report(LEAGUE, seasons, views)


def test_valid_dataset_is_clean(dataset):
    report = run_convenience()
    assert report["overall"]["errors"] == 0
    assert "SEASON_NOT_DECLARED" in codes()
    assert "TABLE_ID_SEASON_SCOPED" in codes()
    assert report["checks"]["file_completeness"]["missing_files"] == []
    assert report["checks"]["teams"]["status"] != SEVERITY_ERROR
    assert report["checks"]["results"]["status"] != SEVERITY_ERROR


def test_missing_file_reports_error(dataset):
    (dataset / LEAGUE / "2020-2021" / "results.json").unlink()
    report = run_convenience()
    assert report["checks"]["file_completeness"]["status"] == SEVERITY_ERROR
    issue = [i for i in report["issues"] if i["code"] == "FILE_MISSING"]
    assert len(issue) == 1
    assert issue[0]["season"] == "2020-2021"
    assert "results.json" in issue[0]["file"]


def test_duplicate_match_id_is_error(dataset):
    p = dataset / LEAGUE / "2020-2021" / "results.json"
    data = json.loads(p.read_bytes())
    data["matches"][1]["id"] = data["matches"][0]["id"]
    p.write_text(json.dumps(data), encoding="utf-8")
    run_convenience()
    assert "RESULTS_DUPLICATE_ID" in codes()


def test_invalid_score_is_error(dataset):
    p = dataset / LEAGUE / "2020-2021" / "results.json"
    data = json.loads(p.read_bytes())
    data["matches"][0]["score"] = "abc"
    p.write_text(json.dumps(data), encoding="utf-8")
    run_convenience()
    assert "RESULTS_INVALID_SCORE" in codes()


def test_goalless_score_mismatch_is_error(dataset):
    p = dataset / LEAGUE / "2020-2021" / "results.json"
    data = json.loads(p.read_bytes())
    data["matches"][0]["goalless"] = True
    data["matches"][0]["first_goal_time"] = None
    p.write_text(json.dumps(data), encoding="utf-8")
    run_convenience()
    assert "RESULTS_GOALLESS_SCORE" in codes()


def test_invalid_date_and_time(dataset):
    p = dataset / LEAGUE / "2020-2021" / "results.json"
    data = json.loads(p.read_bytes())
    data["matches"][0]["date"] = "12/09/2020"
    data["matches"][1]["time"] = "15:00"
    p.write_text(json.dumps(data), encoding="utf-8")
    run_convenience()
    assert "RESULTS_INVALID_DATE" in codes()
    assert "RESULTS_INVALID_TIME" in codes()


def test_duplicate_team_names_is_error(dataset):
    p = dataset / LEAGUE / "2020-2021" / "teams.json"
    data = json.loads(p.read_bytes())
    data["teams"][1]["team"] = data["teams"][0]["team"]
    p.write_text(json.dumps(data), encoding="utf-8")
    run_convenience()
    assert "TEAMS_DUPLICATE_NAME" in codes()


def test_team_slug_mismatch_is_warning(dataset):
    p = dataset / LEAGUE / "2020-2021" / "teams.json"
    data = json.loads(p.read_bytes())
    data["teams"][0]["slug"] = "totally-different"
    p.write_text(json.dumps(data), encoding="utf-8")
    run_convenience()
    assert "TEAMS_SLUG_MISMATCH" in codes()


def test_result_team_missing_from_teams_is_warning(dataset):
    p = dataset / LEAGUE / "2020-2021" / "results.json"
    data = json.loads(p.read_bytes())
    data["matches"][0]["homeTeam"] = "Mystery FC"
    p.write_text(json.dumps(data), encoding="utf-8")
    run_convenience()
    assert "RESULTS_TEAM_MISSING_FROM_TEAMS" in codes()


def test_cross_season_id_overlap_is_error(dataset):
    p = dataset / LEAGUE / "2020-2021" / "results.json"
    q = dataset / LEAGUE / "2021-2022" / "results.json"
    a = json.loads(p.read_bytes())
    b = json.loads(q.read_bytes())
    b["matches"][0]["id"] = a["matches"][0]["id"]
    q.write_text(json.dumps(b), encoding="utf-8")
    run_convenience()
    assert "MATCH_ID_CROSS_SEASON_OVERLAP" in codes()


def test_table_position_issue_is_error(dataset):
    p = dataset / LEAGUE / "2020-2021" / "table_classic.json"
    data = json.loads(p.read_bytes())
    data["table"][0]["position"] = 99
    p.write_text(json.dumps(data), encoding="utf-8")
    run_convenience()
    assert "TABLE_POSITION_ISSUE" in codes()


def test_table_team_vs_teams_mismatch_is_warning(dataset):
    p = dataset / LEAGUE / "2020-2021" / "table_classic.json"
    data = json.loads(p.read_bytes())
    data["table"][0]["team"] = "Different FC"
    p.write_text(json.dumps(data), encoding="utf-8")
    run_convenience()
    assert "TABLE_TEAM_VS_TEAMS_MISMATCH" in codes()


def test_team_count_change_is_warning(dataset):
    p = dataset / LEAGUE / "2021-2022" / "teams.json"
    data = json.loads(p.read_bytes())
    data["teams"].pop()
    p.write_text(json.dumps(data), encoding="utf-8")
    run_convenience()
    assert "TEAM_COUNT_CHANGE" in codes()


def test_issues_are_cleared_between_runs(dataset):
    run_convenience()
    first = len(ISSUES)
    run_convenience()
    assert len(ISSUES) == first  # no accumulation


def test_markdown_renders(dataset):
    report = run_convenience()
    md = v.render_markdown(report)
    assert md.startswith("# Football Charts Raw Data")
    assert "## Findings" in md
    assert "SEASON_NOT_DECLARED" in md


def test_report_json_serializable(dataset):
    report = run_convenience()
    json.dumps(report)  # must not raise