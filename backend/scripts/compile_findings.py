"""Module 7 - Consolidated findings report.

Aggregates the JSON reports produced by `profile_database.py` and analysis
modules 1-6 into a single findings report under data/analysis/:

    findings.json    # machine-readable report
    findings.md      # human-readable summary

Sections:
    1. Sources                (which module reports were found / read)
    2. Key findings           (curated facts extracted from every module)
    3. Cross-module headline stats
    4. Module comparison      (report sections + file size per module)
    5. Notable anomalies      (echoed from database_profile.json warnings)
    6. Methodology            (scope + leakage-safe note)

Reads the sibling JSON files in the out-dir only; never queries the database.
Missing or invalid module reports are skipped safely with `exists: False`.

Usage:
    python backend/scripts/compile_findings.py
    python backend/scripts/compile_findings.py --league spain1
    python backend/scripts/compile_findings.py --out-dir data/analysis --out-stem my_findings
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from analysis_common import (
    parse_args,
    args_to_config,
    report_metadata,
    write_report,
    rel_to_root,
    fmt_md_table,
    render_report_header,
)

STEM = "findings"
SCRIPT_NAME = "backend/scripts/compile_findings.py"

SOURCE_STEMS = [
    "database_profile",
    "matches_analysis",
    "goals_analysis",
    "teams_analysis",
    "season_trends",
    "scoreline_analysis",
    "relationships",
]

SECTION_EXCLUDE = {"report_name", "script", "generated_at", "config", "league", "meta"}

METHODOLOGY_NOTE = (
    "Exploratory-data-analysis only: SQL + Python over the analytics database; "
    "relationship statistics use leakage-safe pre-match features and imply "
    "no predictive power."
)

HT_FLOW_LABEL = {"home": "home lead at HT", "draw": "level at HT", "away": "away lead at HT"}
FT_FLOW_LABEL = {"home": "home win", "draw": "draw", "away": "away win"}


# ── small formatting helpers ─────────────────────────────────────────────────
def _n(value: float | None, ndigits: int = 1) -> str:
    if value is None:
        return "-"
    return f"{value:.{ndigits}f}"


def _int(value) -> str:
    if value is None:
        return "n/a"
    return str(value)


def _val(value, suffix: str = "") -> str:
    if value is None:
        return "-"
    return f"{value}{suffix}"


def _first(values: list) -> object:
    for v in values:
        if v is not None:
            return v
    return None


def _pick(data: dict, *path) -> object:
    cur = data
    for key in path:
        if isinstance(cur, dict):
            cur = cur.get(key)
        elif isinstance(cur, list) and isinstance(key, int) and 0 <= key < len(cur):
            cur = cur[key]
        else:
            return None
    return cur


# ── source loading (robust, never raises) ───────────────────────────────────
def load_source(out_dir: Path, stem: str) -> dict | None:
    path = out_dir / f"{stem}.json"
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def build_sources(out_dir: Path) -> list[dict]:
    sources: list[dict] = []
    for stem in SOURCE_STEMS:
        path = out_dir / f"{stem}.json"
        exists = path.is_file()
        sources.append({
            "report_name": stem,
            "path": rel_to_root(path),
            "exists": exists,
            "loaded": False,
            "size_kb": round(path.stat().st_size / 1024, 2) if exists else None,
        })
    return sources


# ── per-module finding extractors (pure) ─────────────────────────────────────
def _matches_findings(m: dict | None) -> list[dict]:
    out: list[dict] = []
    if not isinstance(m, dict):
        return out
    ov = m.get("overall") or {}
    n = ov.get("n_matches")
    if n is not None:
        out.append({
            "source": "matches_analysis",
            "finding": "Outcome split across all seasons",
            "detail": (f"{n} matches: home wins {_n(ov.get('home_win_pct'))}%, "
                       f"draws {_n(ov.get('draw_pct'))}%, away wins "
                       f"{_n(ov.get('away_win_pct'))}% "
                       f"({_int(ov.get('home_wins'))}H / {_int(ov.get('draws'))}D / "
                       f"{_int(ov.get('away_wins'))}A)"),
            "importance": "medium",
        })
    cb = m.get("comebacks") or {}
    home_cb = (cb.get("home") or {}).get("count")
    away_cb = (cb.get("away") or {}).get("count")
    if home_cb is not None or away_cb is not None:
        out.append({
            "source": "matches_analysis",
            "finding": "Comeback wins",
            "detail": (f"{_int(home_cb)} home and {_int(away_cb)} away comebacks "
                       "(trailing at HT but winning at FT)"),
            "importance": "medium",
        })
    flow = _most_common_ht_ft(m.get("ht_ft_matrix"))
    if flow:
        out.append({
            "source": "matches_analysis",
            "finding": "Most common HT/FT flow",
            "detail": f"{flow['label']} occurred {flow['count']} times",
            "importance": "low",
        })
    return out


def _most_common_ht_ft(mx: dict | None) -> dict | None:
    if not isinstance(mx, dict):
        return None
    best: tuple[tuple[str, str], int] | None = None
    counts = mx.get("counts") or {}
    for ht in mx.get("ht_states") or []:
        for ft in mx.get("ft_outcomes") or []:
            count = counts.get(ht, {}).get(ft) if isinstance(counts.get(ht), dict) else None
            if count is None:
                continue
            if best is None or count > best[1]:
                best = ((ht, ft), count)
    if best is None:
        return None
    (ht, ft), count = best
    return {"label": f"{HT_FLOW_LABEL.get(ht, ht)} -> {FT_FLOW_LABEL.get(ft, ft)}",
            "count": count}


def _goals_findings(g: dict | None) -> list[dict]:
    out: list[dict] = []
    if not isinstance(g, dict):
        return out
    gs = g.get("goal_share") or {}
    dist = g.get("goals_distribution") or {}
    total = gs.get("total_goals")
    n = dist.get("n_matches")
    if total is not None and isinstance(n, (int, float)) and n:
        out.append({
            "source": "goals_analysis",
            "finding": "Average goals per match",
            "detail": f"{n} matches produced {total} goals (avg {total / n:.3f} per match)",
            "importance": "medium",
        })
    if gs.get("home_pct") is not None:
        ratio = _n(gs.get("home_away_ratio"), 2)
        out.append({
            "source": "goals_analysis",
            "finding": "Home goal share",
            "detail": (f"home {_n(gs.get('home_pct'))}% vs away {_n(gs.get('away_pct'))}% "
                       f"of {_int(gs.get('total_goals'))} goals in total "
                       f"(home/away ratio {ratio})"),
            "importance": "medium",
        })
    btts = (g.get("btts") or {}).get("overall") or {}
    if btts.get("pct") is not None:
        out.append({
            "source": "goals_analysis",
            "finding": "Both teams to score",
            "detail": f"{_int(btts.get('count'))} of {_int(btts.get('n_matches'))} "
                      f"matches ({_n(btts.get('pct'))}%)",
            "importance": "medium",
        })
    bucket = _most_common_fg_bucket(g.get("first_goal_timing"))
    if bucket:
        out.append({
            "source": "goals_analysis",
            "finding": "Most common first-goal bucket",
            "detail": (f"minute {bucket['bucket']} (first goal in {bucket['count']} "
                       f"scoring matches, {_n(bucket['pct'], 1)}% of scoring)"),
            "importance": "low",
        })
    summary = (g.get("first_goal_timing") or {}).get("summary")
    if isinstance(summary, dict) and summary.get("mean") is not None:
        out.append({
            "source": "goals_analysis",
            "finding": "Average first goal minute",
            "detail": f"mean {_n(summary.get('mean'), 2)}, median {_n(summary.get('p50'), 1)}",
            "importance": "low",
        })
    return out


def _most_common_fg_bucket(fg: dict | None) -> dict | None:
    if not isinstance(fg, dict):
        return None
    best: dict | None = None
    for key, b in (fg.get("buckets") or {}).items():
        if not isinstance(b, dict) or b.get("count") is None:
            continue
        if best is None or b["count"] > best["count"]:
            best = {"bucket": key, "count": b["count"], "pct": b.get("pct_of_scoring")}
    return best


def _teams_findings(t: dict | None) -> list[dict]:
    out: list[dict] = []
    if not isinstance(t, dict):
        return out
    rows = t.get("teams") or []
    if rows:
        top = rows[0]
        out.append({
            "source": "teams_analysis",
            "finding": "Dominant team by lifetime points",
            "detail": (f"{top.get('team')} leads with {_int(top.get('points'))} points "
                       f"across {_int(top.get('seasons_played'))} seasons "
                       f"({_int(top.get('titles'))} title(s), GD {_int(top.get('goal_difference'))})"),
            "importance": "high",
        })
    ct = t.get("consistent_teams") or {}
    n_teams = ct.get("n_teams")
    if n_teams is not None:
        names = [x.get("team") for x in ct.get("teams") or [] if isinstance(x, dict)]
        listed = ", ".join(names[:5]) + ("..." if len(names) > 5 else "")
        out.append({
            "source": "teams_analysis",
            "finding": "Team consistency",
            "detail": (f"{n_teams} teams present in every one of the "
                       f"{_int(ct.get('n_seasons'))} seasons" + (f" ({listed})" if listed else "")),
            "importance": "medium",
        })
    ha = t.get("home_away") or []
    if ha:
        top = ha[0]
        out.append({
            "source": "teams_analysis",
            "finding": "Biggest home advantage",
            "detail": (f"{top.get('team')} earns {_int(top.get('home_advantage'))} more "
                       f"points at home than away "
                       f"({_int((top.get('home') or {}).get('points'))} home vs "
                       f"{_int((top.get('away') or {}).get('points'))} away)"),
            "importance": "medium",
        })
    return out


def _champion_most_titles(champions: list | None) -> tuple[str, int] | None:
    if not isinstance(champions, list):
        return None
    counts = Counter(c.get("champion") for c in champions
                     if isinstance(c, dict) and c.get("champion"))
    if not counts:
        return None
    name, titles = counts.most_common(1)[0]
    return name, titles


def _avg_goal_trend(trends: list | None) -> dict | None:
    if not isinstance(trends, list):
        return None
    values = [x.get("avg_goals") for x in trends
              if isinstance(x, dict) and x.get("avg_goals") is not None]
    if len(values) < 2:
        return None
    half = len(values) // 2
    first = values[:half]
    last = values[len(values) - half:]
    first_m = statistics.fmean(first)
    last_m = statistics.fmean(last)
    delta = round(last_m - first_m, 3)
    if delta > 0.05:
        direction = "up"
    elif delta < -0.05:
        direction = "down"
    else:
        direction = "stable"
    return {
        "direction": direction,
        "delta": delta,
        "first_half_mean": round(first_m, 3),
        "last_half_mean": round(last_m, 3),
        "n_seasons": len(values),
    }


def _view_divergence_extremes(vd: dict | None) -> tuple[dict | None, dict | None]:
    per_season = vd.get("per_season") if isinstance(vd, dict) else None
    vals: list[dict] = []
    if isinstance(per_season, list):
        for entry in per_season:
            if not isinstance(entry, dict):
                continue
            for view in ("luck", "goals"):
                v = entry.get(view)
                if v is not None:
                    vals.append({"season": entry.get("season"), "view": view, "value": v})
    if not vals:
        return None, None
    most = max(vals, key=lambda x: x["value"])
    least = min(vals, key=lambda x: x["value"])
    return most, least


def _trends_findings(tr: dict | None) -> list[dict]:
    out: list[dict] = []
    if not isinstance(tr, dict):
        return out
    champ = _champion_most_titles(tr.get("champions"))
    if champ:
        name, titles = champ
        n_seasons = sum(1 for c in tr.get("champions") or []
                        if isinstance(c, dict) and c.get("champion"))
        out.append({
            "source": "season_trends",
            "finding": "Champion with most titles",
            "detail": f"{name} won {titles} of {n_seasons} championship(s) on record",
            "importance": "high",
        })
    tightest = (tr.get("title_race") or {}).get("tightest") or {}
    if tightest:
        margin = tightest.get("margin")
        pts = f"{margin} pt" if margin == 1 else f"{margin} pts"
        out.append({
            "source": "season_trends",
            "finding": "Tightest title race",
            "detail": (f"{_int(tightest.get('season'))}: {tightest.get('champion')} beat "
                       f"{tightest.get('runner_up')} by {pts}"),
            "importance": "medium",
        })
    trend = _avg_goal_trend(tr.get("league_trends"))
    if trend:
        out.append({
            "source": "season_trends",
            "finding": "Average-goals trend",
            "detail": (f"{trend['direction']} ({trend['delta']:+.3f} per match): "
                       f"first half {trend['first_half_mean']} vs last half "
                       f"{trend['last_half_mean']} across {trend['n_seasons']} seasons"),
            "importance": "medium",
        })
    most, least = _view_divergence_extremes(tr.get("view_divergence"))
    if most:
        out.append({
            "source": "season_trends",
            "finding": "Largest view divergence",
            "detail": (f"{_int(most['season'])} ({most['view']} view, avg abs position "
                       f"diff {most['value']:.3f})"),
            "importance": "low",
        })
    if least and least is not most:
        out.append({
            "source": "season_trends",
            "finding": "Smallest view divergence",
            "detail": (f"{_int(least['season'])} ({least['view']} view, avg abs position "
                       f"diff {least['value']:.3f})"),
            "importance": "low",
        })
    return out


def _scoreline_findings(s: dict | None) -> list[dict]:
    out: list[dict] = []
    if not isinstance(s, dict):
        return out
    freq = s.get("scoreline_frequency") or {}
    top = freq.get("top") or []
    if top:
        e = top[0]
        out.append({
            "source": "scoreline_analysis",
            "finding": "Most common scoreline",
            "detail": f"{e.get('scoreline')} in {_int(e.get('count'))} matches "
                      f"({_n(e.get('pct'))}%)",
            "importance": "medium",
        })
    common = s.get("common_scorelines") or {}
    labels = {"home": "Most common home-win scoreline",
              "draw": "Most common draw scoreline",
              "away": "Most common away-win scoreline"}
    for outcome, label in labels.items():
        entry = common.get(outcome) or {}
        if entry.get("scoreline"):
            out.append({
                "source": "scoreline_analysis",
                "finding": label,
                "detail": f"{entry.get('scoreline')} ({_int(entry.get('count'))} of "
                          f"{_int(entry.get('n_matches'))} {outcome} matches, "
                          f"{_n(entry.get('pct'))}%)",
                "importance": "low",
            })
    ex = s.get("extreme_scorelines") or {}
    if isinstance(ex.get("count"), int):
        out.append({
            "source": "scoreline_analysis",
            "finding": "Extreme scorelines",
            "detail": f"{ex.get('count')} match(es) with >= {ex.get('min_total')} total goals",
            "importance": "low",
        })
    return out


def _relationships_findings(r: dict | None) -> list[dict]:
    out: list[dict] = []
    if not isinstance(r, dict):
        return out
    cm = r.get("correlation_matrix") or []
    if cm:
        top = cm[0]
        corr = top.get("corr_total_goals")
        if corr is not None:
            out.append({
                "source": "relationships",
                "finding": "Strongest correlation with total goals",
                "detail": (f"{top.get('feature')} |corr| = {corr} "
                           f"(n={_int(top.get('n'))} leakage-safe rows)"),
                "importance": "medium",
            })
    fbr = r.get("feature_by_result") or []
    if fbr:
        top = fbr[0]
        if top.get("range") is not None:
            means = top.get("means") or {}
            out.append({
                "source": "relationships",
                "finding": "Most outcome-separating feature",
                "detail": (f"{top.get('feature')} spreads group means over "
                           f"{top.get('range')}: home {_n(means.get('HOME_WIN'), 3)}, "
                           f"draw {_n(means.get('DRAW'), 3)}, "
                           f"away {_n(means.get('AWAY_WIN'), 3)}"),
                "importance": "medium",
            })
    return out


def _profile_findings(p: dict | None) -> list[dict]:
    out: list[dict] = []
    if not isinstance(p, dict):
        return out
    warnings = p.get("warnings")
    if isinstance(warnings, list):
        if warnings:
            codes = sorted({w.get("code") for w in warnings if isinstance(w, dict) and w.get("code")})
            out.append({
                "source": "database_profile",
                "finding": f"Data-quality warnings ({len(warnings)})",
                "detail": "Anomaly codes: " + (", ".join(codes) if codes else "-"),
                "importance": "high",
            })
        else:
            out.append({
                "source": "database_profile",
                "finding": "No data-quality warnings",
                "detail": "All registered seasons and match-level integrity checks passed.",
                "importance": "low",
            })
    ls = (p.get("observed") or {}).get("league_seasons") or {}
    n_reg = ls.get("n_registered")
    n_data = ls.get("n_with_data")
    total_matches = (p.get("calculated") or {}).get("overall") or {}
    n_matches = total_matches.get("n_matches")
    if n_reg is not None or n_matches is not None:
        cvg = "-"
        if isinstance(n_data, (int, float)) and isinstance(n_reg, (int, float)) and n_reg:
            cvg = f"{100.0 * n_data / n_reg:.1f}%"
        out.append({
            "source": "database_profile",
            "finding": "Data coverage",
            "detail": f"{_int(n_data)} of {_int(n_reg)} registered seasons populated "
                      f"({cvg}); {_int(n_matches)} matches observed",
            "importance": "medium",
        })
    return out


# ── synthesis (pure over parsed reports) ─────────────────────────────────────
def extract_findings(reports: dict[str, dict]) -> list[dict]:
    findings: list[dict] = []
    findings += _matches_findings(reports.get("matches_analysis"))
    findings += _goals_findings(reports.get("goals_analysis"))
    findings += _teams_findings(reports.get("teams_analysis"))
    findings += _trends_findings(reports.get("season_trends"))
    findings += _scoreline_findings(reports.get("scoreline_analysis"))
    findings += _relationships_findings(reports.get("relationships"))
    findings += _profile_findings(reports.get("database_profile"))
    for i, f in enumerate(findings, 1):
        f["id"] = f"F{i}"
    return findings


def headline_stats(reports: dict[str, dict]) -> dict:
    matches = reports.get("matches_analysis", {})
    goals = reports.get("goals_analysis", {})
    teams = reports.get("teams_analysis", {})
    trends = reports.get("season_trends", {})
    score = reports.get("scoreline_analysis", {})
    profile = reports.get("database_profile", {})

    n_matches = _first([
        _pick(matches, "overall", "n_matches"),
        _pick(goals, "goals_distribution", "n_matches"),
        _pick(score, "scoreline_frequency", "n_matches"),
        _pick(profile, "calculated", "overall", "n_matches"),
    ])
    if n_matches is None:
        teams_rows = _pick(teams, "teams")
        if isinstance(teams_rows, list) and teams_rows:
            played = sum(t.get("total_matches", 0) for t in teams_rows if isinstance(t, dict))
            if played:
                n_matches = played // 2

    avg_goals = _first([
        _pick(matches, "overall", "avg_goals"),
        _pick(profile, "calculated", "overall", "avg_goals"),
    ])
    if avg_goals is None:
        total = _pick(goals, "goal_share", "total_goals")
        n = _pick(goals, "goals_distribution", "n_matches")
        if isinstance(total, (int, float)) and isinstance(n, (int, float)) and n:
            avg_goals = round(total / n, 3)

    home_pct = _first([_pick(matches, "overall", "home_win_pct"),
                       _pick(profile, "calculated", "overall", "home_win_pct")])
    draw_pct = _first([_pick(matches, "overall", "draw_pct"),
                       _pick(profile, "calculated", "overall", "draw_pct")])
    away_pct = _first([_pick(matches, "overall", "away_win_pct"),
                       _pick(profile, "calculated", "overall", "away_win_pct")])

    most_common_scoreline = _first([
        _pick(score, "scoreline_frequency", "top", 0, "scoreline"),
        _pick(profile, "calculated", "scorelines", "most_common", 0, "scoreline"),
    ])

    dominant_team = None
    teams_rows = _pick(teams, "teams")
    if isinstance(teams_rows, list) and teams_rows:
        dominant_team = teams_rows[0].get("team")

    champion = _champion_most_titles(_pick(trends, "champions"))
    champion_most_titles = champion[0] if champion else None

    btts_rate_pct = _pick(goals, "btts", "overall", "pct")

    return {
        "n_matches": n_matches,
        "avg_goals": avg_goals,
        "home_win_pct": home_pct,
        "draw_pct": draw_pct,
        "away_win_pct": away_pct,
        "most_common_scoreline": most_common_scoreline,
        "dominant_team": dominant_team,
        "champion_most_titles": champion_most_titles,
        "btts_rate_pct": btts_rate_pct,
    }


def build_comparison(sources: list[dict], reports: dict[str, dict]) -> list[dict]:
    rows: list[dict] = []
    for s in sources:
        if not s.get("loaded"):
            continue
        data = reports.get(s["report_name"]) or {}
        rows.append({
            "module": s["report_name"],
            "report_name": data.get("report_name") or s["report_name"],
            "sections": [k for k in data if k not in SECTION_EXCLUDE],
            "size_kb": s.get("size_kb"),
        })
    return rows


def build_anomalies(reports: dict[str, dict]) -> list[dict]:
    profile = reports.get("database_profile")
    warnings = profile.get("warnings") if isinstance(profile, dict) else None
    if not isinstance(warnings, list):
        return []
    return [w for w in warnings if isinstance(w, dict)]


# ── report assembly (I/O allowed here) ───────────────────────────────────────
def build_report(out_dir: Path, cfg: dict) -> dict:
    sources = build_sources(out_dir)
    reports: dict[str, dict] = {}
    for src in sources:
        if src["exists"]:
            data = load_source(out_dir, src["report_name"])
            if data is not None:
                src["loaded"] = True
                reports[src["report_name"]] = data

    report = report_metadata(STEM, SCRIPT_NAME, cfg)
    report["sources"] = sources
    report["coverage"] = {
        "found": sum(1 for s in sources if s["loaded"]),
        "total": len(sources),
        "missing": [s["report_name"] for s in sources if not s["loaded"]],
    }
    report["key_findings"] = extract_findings(reports)
    report["headline_stats"] = headline_stats(reports)
    report["comparison"] = build_comparison(sources, reports)
    report["anomalies"] = build_anomalies(reports)
    report["methodology"] = METHODOLOGY_NOTE
    return report


# ── markdown rendering ───────────────────────────────────────────────────────
def render_markdown(report: dict) -> str:
    lines = render_report_header(report, "Consolidated Findings").splitlines()
    add = lines.append

    add("")
    add("## 1. Sources")
    add(fmt_md_table(
        ["report", "path", "exists", "loaded", "size (KB)"],
        [
            [s["report_name"], s["path"], "yes" if s["exists"] else "no",
             "yes" if s["loaded"] else "no",
             _n(s["size_kb"], 2) if s["size_kb"] is not None else "-"]
            for s in report["sources"]
        ],
    ))
    cov = report["coverage"]
    note = "all reports present" if cov["found"] == cov["total"] else (
        "loaded: " + ("none" if not cov["found"] else ", ".join(
            s["report_name"] for s in report["sources"] if s["loaded"])) +
        " | missing: " + (", ".join(cov["missing"]) if cov["missing"] else "none"))
    add(f"- Coverage: **{cov['found']}** of **{cov['total']}** module reports "
        f"found ({note})")

    add("")
    add("## 2. Key findings")
    findings = report["key_findings"]
    if not findings:
        add("- *No findings extracted (no module reports present).*")
    for f in findings:
        add(f"- **{f['id']}** · `{f['source']}` · *[{f['importance']}]* — "
            f"**{f['finding']}** — {f['detail']}")

    add("")
    add("## 3. Cross-module headline stats")
    hs = report["headline_stats"]
    add(fmt_md_table(
        ["stat", "value"],
        [
            ["Matches analysed", _val(hs.get("n_matches"))],
            ["Average goals per match", _val(hs.get("avg_goals"))],
            ["Home win rate", _val(_n(hs.get("home_win_pct")), "%")],
            ["Draw rate", _val(_n(hs.get("draw_pct")), "%")],
            ["Away win rate", _val(_n(hs.get("away_win_pct")), "%")],
            ["Most common scoreline", _val(hs.get("most_common_scoreline"))],
            ["Dominant team (lifetime points)", _val(hs.get("dominant_team"))],
            ["Champion with most titles", _val(hs.get("champion_most_titles"))],
            ["BTTS rate", _val(_n(hs.get("btts_rate_pct")), "%")],
        ],
    ))

    add("")
    add("## 4. Module comparison")
    cmp_rows = report["comparison"]
    if not cmp_rows:
        add("- *No module reports found in the out-dir.*")
    else:
        add(fmt_md_table(
            ["module", "report_name", "sections present", "size (KB)"],
            [
                [r["module"], r["report_name"], ", ".join(r["sections"]),
                 _n(r["size_kb"], 2) if r["size_kb"] is not None else "-"]
                for r in cmp_rows
            ],
        ))

    add("")
    add("## 5. Notable anomalies")
    anomalies = report["anomalies"]
    if not anomalies:
        add("- No anomalies recorded in `database_profile.json` (`warnings` is empty).")
    else:
        for i, w in enumerate(anomalies, 1):
            code = w.get("code", "-")
            severity = w.get("severity", "-")
            message = w.get("message", "-")
            add(f"- **{i}.** `{code}` *({severity})* — {message}")

    add("")
    add("## 6. Methodology")
    add(f"- {report['methodology']}")

    add("")
    add("---")
    add("*Aggregates `database_profile.json` and the module reports "
       "(modules 1-6). Run `python backend/scripts/compile_findings.py` after "
       "regenerating the module reports to refresh.*")
    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────
def parse_module_args(argv: list[str] | None = None) -> argparse.Namespace:
    return parse_args(
        "Module 7 - Consolidated findings report (aggregates module JSON reports).",
        argv=argv,
    )


def main(argv: list[str] | None = None) -> int:
    args = parse_module_args(argv)
    cfg = args_to_config(args)
    out_dir = Path(cfg["out_dir"])
    report = build_report(out_dir, cfg)

    stem = cfg.get("out_stem") or STEM
    json_path, md_path = write_report(out_dir, stem, report, render_markdown)

    cov = report["coverage"]
    print(f"{STEM}: compiled {len(report['key_findings'])} findings and "
          f"{len(report['comparison'])} module comparisons from "
          f"{cov['found']} of {cov['total']} expected reports, "
          f"{len(report['anomalies'])} anomaly(ies) - "
          f"wrote {json_path} and {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
