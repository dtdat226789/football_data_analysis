"""Unit tests for the Common Data Analysis Framework (no database, no network).

Covers pure helpers of analysis_common plus the aggregation/bucket logic of
each analyze_*.py module and the findings compiler. Query-layer functions are
thin wrappers around read-only SQL exercised against the live database by
running run_analysis.py directly.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

import scripts.analysis_common as ac
import scripts.analyze_matches as matches
import scripts.analyze_goals as goals
import scripts.analyze_teams as teams
import scripts.analyze_seasons as seasons
import scripts.analyze_scorelines as scorelines
import scripts.analyze_relationships as rels
import scripts.compile_findings as findings


# ── analysis_common ──────────────────────────────────────────────────────────
def test_round_pct():
    assert ac.round_pct(1, 4) == 25.0
    assert ac.round_pct(1, 3) == 33.3
    assert ac.round_pct(0, 0) is None


def test_classify_outcome():
    assert ac.classify_outcome(2, 1) == "home"
    assert ac.classify_outcome(1, 1) == "draw"
    assert ac.classify_outcome(0, 2) == "away"


def test_percentile():
    s = sorted([10, 20, 30, 40])
    assert ac.percentile(s, 0.5) == 25
    assert ac.percentile([7], 0.5) == 7
    assert ac.percentile([], 0.5) is None


def test_summarize_values():
    s = ac.summarize_values([1, 2, 3, 4])
    assert s["n"] == 4
    assert s["min"] == 1
    assert s["max"] == 4
    assert s["mean"] == 2.5
    assert ac.summarize_values([]) is None


def test_pearson():
    assert ac.pearson([1, 2, 3], [2, 4, 6]) == 1.0
    assert ac.pearson([1, 2, 3], [3, 2, 1]) == -1.0
    assert ac.pearson([1, 2], [1, 2]) is None
    assert ac.pearson([1, 1, 1], [1, 2, 3]) == 0.0


def test_cross_tab():
    tab = ac.cross_tab(["a", "a", "b"], ["x", "y", "x"])
    assert tab == {"a": {"x": 1, "y": 1}, "b": {"x": 1}}


def test_season_sort_key():
    names = ["2025-2026", "2020-2021", "2022-2023"]
    assert sorted(names, key=ac.season_sort_key) == ["2020-2021", "2022-2023", "2025-2026"]


def test_report_metadata_config_fields(tmp_path):
    cfg = {"league": "premier", "out_dir": str(tmp_path), "out_stem": None}
    meta = ac.report_metadata("test_report", "test.py", cfg)
    assert meta["report_name"] == "test_report"
    assert meta["league"]["name"] == "Premier League"
    assert meta["config"]["league"] == "premier"
    json.dumps(meta)


def test_args_roundtrip_defaults():
    args = ac.parse_args("desc", ["--out-dir", "/tmp/x"])
    cfg = ac.args_to_config(args)
    assert cfg["league"] == ac.LEAGUE
    assert cfg["out_dir"] == str(Path("/tmp/x").resolve())


def test_args_allow_customisation():
    args = ac.parse_args("desc", ["--league", "spain1", "--out-dir", "/tmp/x", "--out-stem", "y"])
    cfg = ac.args_to_config(args)
    assert cfg["league"] == "spain1"
    assert cfg["out_stem"] == "y"


def test_write_report(tmp_path):
    report = {"x": 1}
    jp, mp = ac.write_report(tmp_path, "test_report", report, lambda r: "**MD**")
    assert jp.exists() and mp.exists()
    assert json.loads(jp.read_text()) == report
    assert "**MD**" in mp.read_text()


def test_write_report_appends_charts(tmp_path):
    report = {"x": 1}
    chart = tmp_path / "charts" / "c.png"
    chart.parent.mkdir(parents=True, exist_ok=True)
    chart.write_bytes(b"png")
    _, mp = ac.write_report(tmp_path, "test_report", report, lambda r: "body", charts=[chart])
    assert "![c](%s)" % chart in mp.read_text()


def test_fmt_md_table_and_pct():
    table = ac.fmt_md_table(["A", "B"], [["x", 1], ["y", 2]])
    assert "| A | B |" in table
    assert "| x | 1 |" in table
    assert ac.fmt_pct(33.333, 1) == "33.3%"
    assert ac.fmt_pct(None) == "-"


# ── module 1: matches ────────────────────────────────────────────────────────
def _row(hs=1, as_=0, hht=0, aht=0, fgt=10, season="2020-2021",
         home="Home", away="Away"):
    return {
        "season": season, "home_team": home, "away_team": away,
        "home_score": hs, "away_score": as_,
        "home_ht": hht, "away_ht": aht, "first_goal_time": fgt,
    }


def test_ht_ft_outcomes():
    assert matches.ht_outcome(_row(hht=1, aht=0)) == "home"
    assert matches.ht_outcome(_row(hht=None, aht=None)) is None
    assert matches.ft_outcome(_row(1, 0)) == "home"
    assert matches.ft_outcome(_row(1, 1)) == "draw"
    assert matches.ft_outcome(_row(0, 1)) == "away"


def test_first_goal_bucket():
    assert matches.first_goal_bucket(15) == "1-15"
    assert matches.first_goal_bucket(16) == "16-30"
    assert matches.first_goal_bucket(120) == "91-120"
    assert matches.first_goal_bucket(None) is None
    assert matches.first_goal_bucket(0) is None


def test_aggregate_stats():
    stats = matches.aggregate_stats([
        _row(1, 0), _row(1, 1), _row(0, 1), _row(0, 0),
    ])
    assert stats["n_matches"] == 4
    assert stats["home_wins"] == 1
    assert stats["draws"] == 2
    assert stats["away_wins"] == 1
    assert stats["avg_goals"] == round(4 / 4, 3)
    assert stats["goalless"] == 1


def test_outcome_distribution():
    d = matches.outcome_distribution([_row(1, 0), _row(1, 1)])
    assert d["n_matches"] == 2
    assert d["home"]["count"] == 1
    assert d["home"]["pct"] == 50.0
    assert d["draw"]["count"] == 1


def test_ht_ft_matrix():
    rows = [
        _row(2, 1, 1, 0),   # HT home, FT home
        _row(1, 2, 1, 0),   # HT home, FT away (collapse)
        _row(1, 1, 0, 0),   # HT draw, FT draw
        _row(hht=None, aht=None),  # no HT -> excluded
    ]
    m = matches.build_ht_ft_matrix(rows)
    assert m["counts"]["home"]["home"] == 1
    assert m["counts"]["home"]["away"] == 1
    assert m["counts"]["draw"]["draw"] == 1
    assert m["excluded_no_ht"] == 1
    assert m["pcts"]["home"]["home"] == 50.0


def test_comebacks():
    rows = [
        _row(2, 1, 0, 1),   # trailing at HT, home win
        _row(0, 2, 1, 0),   # trailing at HT, away win
        _row(1, 0, 1, 0),   # leading at HT, home win (not comeback)
    ]
    cb = matches.build_comebacks(rows)
    assert cb["home"]["count"] == 1
    assert cb["away"]["count"] == 1
    assert cb["home"]["matches"][0]["ft_score"] == "2-1"


def test_ht_lead_conversion():
    rows = [
        _row(2, 0, 1, 0),   # home lead -> home win
        _row(1, 1, 1, 0),   # home lead -> draw
        _row(0, 1, 0, 1),   # away lead -> away win
    ]
    conv = matches.build_ht_lead_conversion(rows)
    assert conv["home_lead"]["home"]["count"] == 1
    assert conv["home_lead"]["draw"]["count"] == 1
    assert conv["away_lead"]["away"]["count"] == 1
    assert conv["excluded_no_ht"] == 0


def test_first_goal_timing_buckets():
    rows = [_row(fgt=10), _row(fgt=40), _row(fgt=100), _row(fgt=None)]
    fg = matches.build_first_goal_timing(rows)
    assert fg["n_total"] == 4
    assert fg["n_with_first_goal"] == 3
    assert fg["buckets"]["1-15"]["n_matches"] == 1
    assert fg["buckets"]["31-45"]["n_matches"] == 1
    assert fg["buckets"]["91-120"]["n_matches"] == 1
    assert fg["unbucketed"] == 0


def test_goalless_section():
    overall = matches.aggregate_stats([_row(0, 0), _row(1, 0)])
    per_season = [{"season": "2020-2021", **overall}]
    gs = matches.build_goalless_section(overall, per_season)
    assert gs["overall"]["count"] == 1
    assert gs["overall"]["pct"] == 50.0
    assert gs["per_season"][0]["season"] == "2020-2021"


# ── module 2: goals ──────────────────────────────────────────────────────────
def test_goals_distribution_and_btts():
    dist = goals.build_goals_distribution([
        _row(1, 0), _row(2, 1), _row(0, 0), _row(1, 1),
    ])
    assert dist["n_matches"] == 4
    by_goals = {b["goals"]: b["count"] for b in dist["buckets"]}
    assert by_goals[0] == 1
    assert by_goals[2] == 1
    assert by_goals[3] == 1
    btts = goals.build_btts([_row(1, 0), _row(2, 1), _row(0, 0), _row(1, 1)])
    assert btts["overall"]["count"] == 2  # 2-1 and 1-1
    assert btts["overall"]["pct"] == 50.0


def test_goal_share_and_clean_sheets():
    rows = [_row(2, 1), _row(0, 0), _row(1, 4)]
    per_season = goals.build_goals_per_season(rows)
    share = goals.build_goal_share(rows, per_season)
    assert share["home_goals"] == 3
    assert share["away_goals"] == 5
    assert share["home_pct"] == round(100 * 3 / 8, 1)
    cs = goals.build_clean_sheets(rows)["overall"]
    assert cs["home_clean_sheets"] == 1   # away scored 0 only in 0-0
    assert cs["away_clean_sheets"] == 1   # home scored 0 only in 0-0


def test_scoring_intensity():
    rows = [
        _row(2, 0, 1, 0),   # HT 1, FT 2
        _row(0, 1, 0, 0),   # HT 0, FT 1 (second-half only)
    ]
    si = goals.build_scoring_intensity(rows)["overall"]
    assert si["first_half_goals"] == 1
    assert si["second_half_goals"] == 2
    assert si["second_half_only"]["count"] == 1


def test_first_goal_timing_goals_module():
    fg = goals.build_first_goal_timing([_row(fgt=10), _row(fgt=100), _row(fgt=None)])
    assert fg["n_with_first_goal"] == 2
    assert fg["n_goalless"] == 1
    assert fg["buckets"]["1-15"]["count"] == 1
    assert fg["buckets"]["91-120"]["count"] == 1
    assert fg["summary"]["p50"] == 55  # median of [10, 100]


def test_goals_section_structure_complete():
    for fn, arg in [
        (goals.build_goals_distribution, []),
        (goals.build_btts, []),
        (goals.build_clean_sheets, []),
        (goals.build_scoring_intensity, []),
        (goals.build_first_goal_timing, []),
    ]:
        assert isinstance(fn(arg), dict)


# ── module 3: teams ──────────────────────────────────────────────────────────
def test_team_aggregation_and_standings():
    rows = [
        {"season": "2020-2021", "home_team_id": 1, "away_team_id": 2,
         "home_score": 2, "away_score": 0},
        {"season": "2020-2021", "home_team_id": 2, "away_team_id": 1,
         "home_score": 1, "away_score": 1},
    ]
    agg = teams.aggregate_team_results(rows)
    assert agg[1]["home"]["points"] == 3
    assert agg[1]["away"]["points"] == 1   # 1-1 away = 1 point
    assert agg[2]["home"]["points"] == 1
    assert agg[2]["away"]["points"] == 0
    standings_rows = [
        {"season": "2020-2021", "view": "classic", "team_id": 1, "position": 1,
         "played": 2, "won": 1, "drawn": 1, "lost": 0, "goals_for": 3,
         "goals_against": 1, "goal_difference": 2, "points": 4},
        {"season": "2020-2021", "view": "classic", "team_id": 2, "position": 2,
         "played": 2, "won": 0, "drawn": 1, "lost": 1, "goals_for": 1,
         "goals_against": 3, "goal_difference": -2, "points": 1},
    ]
    summary = teams.standings_summary(standings_rows)
    assert summary[1]["best_position"] == 1
    assert summary[1]["titles"] == 1
    assert summary[2]["best_position"] == 2


def test_lifetime_and_home_away():
    rows = [
        {"season": "2020-2021", "home_team_id": 1, "away_team_id": 2,
         "home_score": 1, "away_score": 0},
        {"season": "2020-2021", "home_team_id": 2, "away_team_id": 1,
         "home_score": 0, "away_score": 1},
    ]
    agg = teams.aggregate_team_results(rows)
    name_map = {1: {"name": "A", "slug": "a"}, 2: {"name": "B", "slug": "b"}}
    lifetimes = teams.build_lifetime(agg, {}, name_map)
    by_team = {r["team_id"]: r for r in lifetimes}
    assert by_team[1]["total_matches"] == 2
    assert by_team[1]["points"] == 6   # 1-0 home win + 1-0 away win
    assert by_team[1]["goal_difference"] == 2
    ha = teams.build_home_away(agg, name_map)
    assert ha[0]["home_advantage"] == 3 - 3  # both legs won 1-0


def test_top_performers_and_consistency():
    rows = [
        {"season": "2020-2021", "home_team_id": 1, "away_team_id": 2,
         "home_score": 1, "away_score": 0},
    ]
    agg = teams.aggregate_team_results(rows)
    name_map = {1: {"name": "A", "slug": "a"}, 2: {"name": "B", "slug": "b"}}
    standings_sum = teams.standings_summary(
        [{"season": "2020-2021", "view": "classic", "team_id": 1, "position": 1,
          "played": 1, "won": 1, "drawn": 0, "lost": 0, "goals_for": 1,
          "goals_against": 0, "goal_difference": 1, "points": 3}]
    )
    lifetimes = teams.build_lifetime(agg, standings_sum, name_map)
    top = teams.build_top_performers(lifetimes, standings_sum)
    assert top["best_ppg"][0]["team_id"] == 1
    assert top["best_ppg"][0]["value"] == 3.0
    cons = teams.build_consistent_teams(["2020-2021"], standings_sum, name_map)
    assert cons["n_seasons"] == 1
    assert cons["n_teams"] == 1


def test_head_to_head():
    rows = [
        {"season": "2020-2021", "home_team_id": 1, "away_team_id": 2,
         "home_score": 1, "away_score": 0},
        {"season": "2020-2021", "home_team_id": 2, "away_team_id": 1,
         "home_score": 1, "away_score": 1},
        {"season": "2021-2022", "home_team_id": 1, "away_team_id": 3,
         "home_score": 0, "away_score": 1},
    ]
    name_map = {1: {"name": "A", "slug": "a"}, 2: {"name": "B", "slug": "b"},
                3: {"name": "C", "slug": "c"}}
    h2h = teams.build_head_to_head(rows, name_map, top_n=10)
    assert h2h["n_pairs_total"] == 2
    pair = h2h["pairs"][0]
    assert pair["meetings"] == 2
    assert pair["home_wins"] == 1
    assert pair["draws"] == 1
    assert pair["away_wins"] == 0


def test_position_table():
    rows = [{"season": "2020-2021", "view": "classic", "team_id": 1, "position": 2}]
    pt = teams.build_position_table(
        ["2020-2021", "2021-2022"], rows, {1: {"name": "A", "slug": "a"}},
        [{"team_id": 1, "points": 10, "goal_difference": 2}],
    )
    assert pt["seasons"] == ["2020-2021", "2021-2022"]
    assert pt["teams"][0]["positions"] == [2, None]


# ── module 4: seasons ────────────────────────────────────────────────────────
def _classic_row(season, team_id, pos, points, team_name="T"):
    return {"season": season, "view": "classic", "team_id": team_id,
            "position": pos, "played": 2, "won": 1, "drawn": 0, "lost": 1,
            "goals_for": 2, "goals_against": 1, "goal_difference": 1,
            "points": points, "team_name": f"{team_name}{team_id}"}


def test_build_champions_and_title_race():
    rows = [
        _classic_row("2020-2021", 1, 1, 90, "A"), _classic_row("2020-2021", 2, 2, 87, "B"),
        _classic_row("2021-2022", 3, 1, 95, "C"), _classic_row("2021-2022", 4, 2, 80, "D"),
    ]
    champs = seasons.build_champions(rows, name_map={})
    assert champs[0]["champion_id"] == 1
    assert champs[0]["margin_pts"] == 3
    assert champs[1]["margin_pts"] == 15
    race = seasons.build_title_race(champs)
    assert race["tightest"]["season"] == "2020-2021"
    assert race["tight_race_count"] == 1  # margin 3 <= 3


def test_build_points_thresholds():
    rows = [
        _classic_row("2020-2021", 1, 1, 90), _classic_row("2020-2021", 2, 2, 85),
        _classic_row("2020-2021", 3, 4, 70), _classic_row("2020-2021", 4, 20, 30),
    ]
    th = seasons.build_points_thresholds(rows, n_teams=20)
    assert th[0]["season"] == "2020-2021"
    assert th[0]["positions"]["1"] == 90
    assert th[0]["positions"]["20"] == 30


def test_build_league_trends():
    match_rows = [
        {"season": "2020-2021", "home_score": 2, "away_score": 0},
        {"season": "2020-2021", "home_score": 1, "away_score": 1},
        {"season": "2021-2022", "home_score": 0, "away_score": 1},
    ]
    classic_rows = [
        _classic_row("2020-2021", 1, 1, 90), _classic_row("2020-2021", 2, 2, 85),
        _classic_row("2020-2021", 3, 3, 80), _classic_row("2020-2021", 4, 4, 70),
    ]
    trends = seasons.build_league_trends(match_rows, classic_rows, n_teams=20)
    s1 = trends[0]
    assert s1["season"] == "2020-2021"
    assert s1["avg_goals"] == 2.0
    assert s1["home_win_pct"] == 50.0
    assert trends[1]["away_win_pct"] == 100.0


def test_build_view_divergence():
    all_rows = [
        {"season": "2020-2021", "view": "classic", "team_id": 1, "position": 4},
        {"season": "2020-2021", "view": "luck", "team_id": 1, "position": 1},
    ]
    vd = seasons.build_view_divergence(all_rows)
    assert vd["per_season"][0]["luck"] == 3.0
    assert vd["worst_divergence"]["season"] == "2020-2021"


# ── module 5: scorelines ─────────────────────────────────────────────────────
def test_scoreline_frequency():
    rows = [
        {"season": "2020-2021", "home_score": 1, "away_score": 0},
        {"season": "2020-2021", "home_score": 1, "away_score": 1},
        {"season": "2020-2021", "home_score": 1, "away_score": 0},
    ]
    freq = scorelines.build_scoreline_frequency(rows, top_n=2)
    assert freq["n_matches"] == 3
    assert freq["n_distinct_scorelines"] == 2
    assert freq["top"][0]["scoreline"] == "1-0"
    assert freq["top"][0]["count"] == 2


def test_total_goal_histogram():
    rows = [
        {"season": "2020-2021", "home_score": 5, "away_score": 4},   # 9
        {"season": "2020-2021", "home_score": 1, "away_score": 1},   # 2
        {"season": "2020-2021", "home_score": 0, "away_score": 0},   # 0
    ]
    hist = scorelines.build_total_goal_histogram(rows, cap=6)
    by_goals = {b["label"]: b["count"] for b in hist["buckets"]}
    assert by_goals["0"] == 1
    assert by_goals["2"] == 1
    assert by_goals["6+"] == 1


def test_extreme_and_margin():
    rows = [
        {"season": "2020-2021", "home_score": 7, "away_score": 0},
        {"season": "2020-2021", "home_score": 1, "away_score": 2},
    ]
    extreme = scorelines.build_extreme_scorelines(rows, min_total=6)
    assert extreme["count"] == 1
    assert extreme["matches"][0]["scoreline"] == "7-0"
    margin = scorelines.build_margin_distribution(rows)
    assert margin["n_decided"] == 2
    by_label = {b["label"]: b["count"] for b in margin["distribution"]}
    assert by_label["1"] == 1   # away win by 1
    assert by_label["3+"] == 1  # home win by 7 (capped at MARGIN_CAP)


def test_margin_by_outcome_and_common():
    rows = [
        {"season": "2020-2021", "home_score": 1, "away_score": 0},
        {"season": "2020-2021", "home_score": 1, "away_score": 1},
        {"season": "2020-2021", "home_score": 0, "away_score": 2},
    ]
    mbo = scorelines.build_margin_by_outcome(rows)
    assert mbo["home"]["n_matches"] == 1
    assert mbo["home"]["avg_margin"] == 1.0
    common = scorelines.build_common_scorelines(rows)
    assert common["home"]["scoreline"] == "1-0"
    assert common["draw"]["scoreline"] == "1-1"
    assert common["away"]["scoreline"] == "0-2"


# ── module 6: relationships ──────────────────────────────────────────────────
def _frow(values: dict) -> dict:
    base = {
        "home_position_before_match": 10, "away_position_before_match": 10,
        "position_difference": 0, "home_team_points_last_5": 7,
        "away_team_points_last_5": 7, "home_rest_days": 5, "away_rest_days": 5,
        "rest_days_difference": 0, "home_team_home_win_rate": 0.5,
        "home_score": 1, "away_score": 0, "match_result": "HOME_WIN",
    }
    base.update(values)
    return base


def test_safe_bucket_handles_nulls_and_nan():
    for value in (None, float("nan")):
        assert rels._safe_bucket(value, [0.5], ["low", "high"]) == "unknown"
    assert rels._safe_bucket(0, [0.5], ["low", "high"]) == "low"
    assert rels._safe_bucket(1, [0.5], ["low", "high"]) == "high"
    assert rels._safe_bucket(0.49, [0.5], ["low", "high"]) == "low"
    assert rels._safe_bucket(0.5, [0.5], ["low", "high"]) == "high"


def test_correlation_matrix():
    rows = [
        _frow({"position_difference": -5, "home_score": 2, "away_score": 0}),
        _frow({"position_difference": 5, "home_score": 0, "away_score": 2}),
        _frow({"position_difference": 0, "home_score": 1, "away_score": 1}),
    ]
    corr = rels.build_correlation_matrix(rows)
    row = next(x for x in corr if x["feature"] == "position_difference")
    assert row["corr_total_goals"] is not None
    assert -1.0 <= row["corr_total_goals"] <= 1.0
    assert row["n"] == 3


def test_build_position_outcome():
    rows = [
        _frow({"position_difference": -8, "match_result": "HOME_WIN",
               "home_score": 2, "away_score": 0}),
        _frow({"position_difference": 0, "match_result": "HOME_WIN",
               "home_score": 1, "away_score": 0}),
        _frow({"position_difference": 8, "match_result": "AWAY_WIN",
               "home_score": 0, "away_score": 2}),
    ]
    bins = rels.build_position_outcome(rows)["bins"]
    by_bucket = {b["bucket"]: b for b in bins}
    assert by_bucket["<=-6"]["home_wins"] == 1
    assert by_bucket[">=6"]["away_wins"] == 1


def test_rest_and_quality_tiers():
    rows = [
        _frow({"rest_days_difference": None, "match_result": "HOME_WIN"}),
        _frow({"rest_days_difference": 5, "match_result": "AWAY_WIN"}),
    ]
    rest = rels.build_rest_advantage(rows)["bins"]
    by_bucket = {b["bucket"]: b for b in rest}
    assert by_bucket["unknown"]["n"] == 1
    assert by_bucket[">2"]["n"] == 1
    quality = rels.build_home_quality(rows)
    assert quality["home_win_pct_gap"] is None  # all home scores equal -> no gap calc


def test_feature_by_result():
    rows = [
        _frow({"home_team_points_last_5": 10, "match_result": "HOME_WIN"}),
        _frow({"home_team_points_last_5": 2, "match_result": "AWAY_WIN"}),
    ]
    fbr = rels.build_feature_by_result(rows)
    entry = next(x for x in fbr if x["feature"] == "home_team_points_last_5")
    assert entry["means"]["HOME_WIN"] == 10.0
    assert entry["means"]["AWAY_WIN"] == 2.0
    assert entry["range"] == 8.0


def test_relationships_empty_rows():
    for fn in (rels.build_correlation_matrix, rels.build_form_outcome,
               rels.build_position_outcome, rels.build_rest_advantage,
               rels.build_home_quality, rels.build_feature_by_result):
        assert isinstance(fn([]), (dict, list))


# ── module 7: findings ───────────────────────────────────────────────────────
def test_load_source_missing(tmp_path):
    assert findings.load_source(tmp_path, "does_not_exist") is None


def test_build_sources_reports_missing(tmp_path):
    sources = findings.build_sources(tmp_path)
    assert len(sources) == 7
    assert all(not s["exists"] for s in sources)


def test_extract_findings_all_sources_present(tmp_path):
    reports = {
        "matches_analysis": {"overall": {"n_matches": 380, "home_win_pct": 46.1,
                                         "draw_pct": 24.0, "away_win_pct": 29.9,
                                         "avg_goals": 2.7, "home_wins": 175,
                                         "draws": 91, "away_wins": 114},
                             "comebacks": {"home": {"count": 15}, "away": {"count": 9}},
                             "ht_ft_matrix": {"counts": {"home": {"home": 100},
                                                         "away": {"away": 90}},
                                              "ht_states": ["home", "draw", "away"],
                                              "ft_outcomes": ["home", "draw", "away"]}},
        "goals_analysis": {"goals_distribution": {"n_matches": 380},
                           "goal_share": {"total_goals": 1018, "home_pct": 53.2,
                                          "away_pct": 46.8, "home_away_ratio": 1.14,
                                          "home_goals": 542, "away_goals": 476},
                           "btts": {"overall": {"pct": 55.0, "count": 209, "n_matches": 380}},
                           "first_goal_timing": {"buckets": {"1-15": {"count": 90,
                                                                      "pct_of_scoring": 25.0}},
                                                 "summary": {"mean": 31.2, "p50": 30}}},
        "teams_analysis": {"teams": [{"team": "A", "points": 300, "seasons_played": 6,
                                      "titles": 3, "goal_difference": 120},
                                     {"team": "B", "points": 250, "seasons_played": 6,
                                      "titles": 2, "goal_difference": 90}],
                           "consistent_teams": {"n_teams": 13, "n_seasons": 6,
                                                "teams": [{"team": "A"}, {"team": "B"}]},
                           "home_away": [{"team": "A", "home_advantage": 15,
                                          "home": {"points": 200}, "away": {"points": 185}}]},
        "season_trends": {"champions": [{"champion": "A", "season": "2020-2021",
                                         "margin_pts": 5, "champion_pts": 99,
                                         "runner_up": "B", "runner_up_id": 2}],
                          "title_race": {"tightest": {"season": "2020-2021", "margin": 5,
                                                      "champion": "A", "runner_up": "B"}},
                          "league_trends": [{"season": "2020-2021", "avg_goals": 2.6}],
                          "view_divergence": {"per_season": [{"season": "2020-2021",
                                                              "luck": 2.5, "goals": 1.0}]}},
        "scoreline_analysis": {"scoreline_frequency": {"top": [{"scoreline": "1-0",
                                                               "count": 120, "pct": 31.6}]},
                               "common_scorelines": {"home": {"scoreline": "1-0",
                                                              "count": 120, "n_matches": 175,
                                                              "pct": 68.6},
                                                     "draw": {"scoreline": "1-1",
                                                              "count": 30, "n_matches": 91,
                                                              "pct": 33.0},
                                                     "away": {"scoreline": "0-1",
                                                              "count": 60, "n_matches": 114,
                                                              "pct": 52.6}},
                               "extreme_scorelines": {"count": 3, "min_total": 7}},
        "relationships": {"correlation_matrix": [{"feature": "points_difference",
                                                  "corr_total_goals": 0.31, "n": 380}],
                          "feature_by_result": [{"feature": "position_difference",
                                                 "range": 8.0,
                                                 "means": {"HOME_WIN": 5.0, "DRAW": 1.0,
                                                           "AWAY_WIN": -3.0}}]},
        "database_profile": {"warnings": [], "observed": {"tables": {"matches": 2280}},
                             "calculated": {"overall": {"n_matches": 2280,
                                                        "avg_goals": 2.89,
                                                        "home_win_pct": 46.0,
                                                        "draw_pct": 24.0,
                                                        "away_win_pct": 30.0},
                                            "scorelines": {"most_common": [
                                                {"scoreline": "1-1", "count": 300}]}}},
    }
    facts = findings.extract_findings(reports)
    assert facts  # non-empty
    sources = {f["source"] for f in facts}
    assert "matches_analysis" in sources
    assert "scoreline_analysis" in sources
    assert all(f["importance"] in ("high", "medium", "low") for f in facts)
    stats = findings.headline_stats(reports)
    assert stats["n_matches"] == 380
    assert stats["most_common_scoreline"] == "1-0"
    assert stats["dominant_team"] == "A"


def test_extract_findings_with_missing_sources(tmp_path):
    reports = {"matches_analysis": None, "goals_analysis": {}, "teams_analysis": None,
               "season_trends": None, "scoreline_analysis": None,
               "relationships": None, "database_profile": None}
    assert findings.extract_findings(reports) == []