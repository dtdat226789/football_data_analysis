"""Module 6 - Relationships analysis report.

Explores statistical relationships between leakage-safe pre-match state
(features built by ml.features.build_features.build_rows) and match outcomes.
Every feature is computed strictly from prior matches, so no future result is
ever observed. Produces a report under data/analysis/:

    relationships.json      # machine-readable report
    relationships.md        # human-readable summary
    charts/relationships_*.png   # home-win-rate bar charts per bucket

Sections:
    1. Correlation matrix (features vs home / away / total goals)
    2. Form difference vs outcome
    3. Position difference vs outcome
    4. Rest advantage vs outcome (nulls bucketed separately)
    5. Home team quality tiers vs home win rate
    6. Feature averages by result

Usage:
    python backend/scripts/analyze_relationships.py
    python backend/scripts/analyze_relationships.py --league spain1
    python backend/scripts/analyze_relationships.py --out-dir data/analysis --out-stem my_report
"""
from __future__ import annotations

import argparse
import math
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from analysis_common import (
    ROOT_DIR,
    parse_args,
    args_to_config,
    report_metadata,
    write_report,
    fmt_pct,
    fmt_md_table,
    render_report_header,
    round_pct,
    pearson,
    cross_tab,
    new_figure,
    save_chart,
)
from db_common import get_conn

sys.path.insert(0, str(ROOT_DIR / "ml"))
sys.path.insert(0, str(ROOT_DIR))

from ml.features import build_features  # noqa: E402
from ml.features.build_features import FEATURE_COLUMNS  # noqa: E402

STEM = "relationships"
SCRIPT_NAME = "backend/scripts/analyze_relationships.py"

OUTCOME_KEYS = ("HOME_WIN", "DRAW", "AWAY_WIN")
HOME_OUTCOME = "HOME_WIN"
DRAW_OUTCOME = "DRAW"
AWAY_OUTCOME = "AWAY_WIN"

HOME_QUALITY_SPLIT = 0.5

FORM_EDGES = [-4, -1, 2, 5]
FORM_BUCKETS = ["<-4", "-4..-2", "-1..1", "2..4", ">4"]

POSITION_EDGES = [-5, -1, 2, 6]
POSITION_BUCKETS = ["<=-6", "-5..-2", "-1..1", "2..5", ">=6"]

REST_EDGES = [-1, 0, 1, 3]
REST_BUCKETS = ["<-1", "-1..0", "0", "1..2", ">2"]

NUMERIC_FEATURES = list(FEATURE_COLUMNS)

CORR_TARGETS = ("home_score", "away_score", "total_goals")


# ── pure helpers (unit-testable without a database) ─────────────────────────
def _is_null(value) -> bool:
    if value is None:
        return True
    if isinstance(value, float):
        return math.isnan(value)
    return False


def _safe_bucket(value, edges: list[float], labels: list[str]) -> str:
    """Bucket a numeric value using ascending `edges`; None/NaN -> 'unknown'.

    edges[i] is the upper boundary of labels[i]: a value strictly below
    edges[0] lands in labels[0], a value at/above the final edge lands in
    the last label.
    """
    if _is_null(value):
        return "unknown"
    v = float(value)
    for edge, label in zip(edges, labels):
        if v < edge:
            return label
    return labels[-1]


def _outcome_cross_bins(values: list, outcomes: list[str],
                        labels: list[str]) -> list[dict]:
    """Cross-tab bucketed feature values against outcomes, with pct per bin."""
    tabs = cross_tab(values, outcomes)
    bins: list[dict] = []
    for label in labels:
        cnts = tabs.get(label, {})
        home = cnts.get(HOME_OUTCOME, 0)
        draw = cnts.get(DRAW_OUTCOME, 0)
        away = cnts.get(AWAY_OUTCOME, 0)
        n = home + draw + away
        bins.append({
            "bucket": label,
            "n": n,
            "home_wins": home,
            "draws": draw,
            "away_wins": away,
            "home_pct": round_pct(home, n),
            "draw_pct": round_pct(draw, n),
            "away_pct": round_pct(away, n),
        })
    return bins


# ── section builders ─────────────────────────────────────────────────────────
def build_correlation_matrix(rows: list[dict],
                             targets=CORR_TARGETS) -> list[dict]:
    """Pearson correlation of every numeric feature with score outcomes."""
    entries: list[dict] = []
    for feature in NUMERIC_FEATURES:
        xs: list[float] = []
        home: list[float] = []
        away: list[float] = []
        total: list[float] = []
        for r in rows:
            v = r.get(feature)
            if _is_null(v):
                continue
            hs = r["home_score"]
            as_ = r["away_score"]
            xs.append(float(v))
            home.append(hs)
            away.append(as_)
            total.append(hs + as_)
        entries.append({
            "feature": feature,
            "n": len(xs),
            "corr_home_score": pearson(xs, home),
            "corr_away_score": pearson(xs, away),
            "corr_total_goals": pearson(xs, total),
        })
    entries.sort(
        key=lambda e: abs(e["corr_total_goals"]) if e["corr_total_goals"] is not None else 0.0,
        reverse=True,
    )
    return entries


def build_form_outcome(rows: list[dict]) -> dict:
    values = [r["home_team_points_last_5"] - r["away_team_points_last_5"] for r in rows]
    outcomes = [r["match_result"] for r in rows]
    buckets = [
        _safe_bucket(v, FORM_EDGES, FORM_BUCKETS) if v is not None else "unknown"
        for v in values
    ]
    labels = FORM_BUCKETS + ["unknown"]
    return {
        "feature": "home_team_points_last_5 - away_team_points_last_5",
        "bins": _outcome_cross_bins(buckets, outcomes, labels),
    }


def build_position_outcome(rows: list[dict]) -> dict:
    values = [r["position_difference"] for r in rows]
    outcomes = [r["match_result"] for r in rows]
    buckets = [
        _safe_bucket(v, POSITION_EDGES, POSITION_BUCKETS) if v is not None else "unknown"
        for v in values
    ]
    labels = POSITION_BUCKETS + ["unknown"]
    return {
        "feature": "position_difference (home_position - away_position)",
        "bins": _outcome_cross_bins(buckets, outcomes, labels),
    }


def build_rest_advantage(rows: list[dict]) -> dict:
    values = [r["rest_days_difference"] for r in rows]
    outcomes = [r["match_result"] for r in rows]
    buckets = [_safe_bucket(v, REST_EDGES, REST_BUCKETS) for v in values]
    labels = REST_BUCKETS + ["unknown"]
    return {
        "feature": "rest_days_difference (home_rest_days - away_rest_days)",
        "bins": _outcome_cross_bins(buckets, outcomes, labels),
    }


def _tier_stats(tier: str, label: str, results: list[str]) -> dict:
    n = len(results)
    home = sum(1 for r in results if r == HOME_OUTCOME)
    draw = sum(1 for r in results if r == DRAW_OUTCOME)
    away = sum(1 for r in results if r == AWAY_OUTCOME)
    return {
        "tier": tier,
        "label": label,
        "n": n,
        "home_wins": home,
        "draws": draw,
        "away_wins": away,
        "home_pct": round_pct(home, n),
        "draw_pct": round_pct(draw, n),
        "away_pct": round_pct(away, n),
    }


def _range_label(lo: float | None, hi: float | None) -> str:
    if lo is None and hi is not None:
        return f"< {hi:g}"
    if hi is None and lo is not None:
        return f">= {lo:g}"
    if lo is not None and hi is not None:
        return f"<= {hi:g} (>= {lo:g})"
    return "all"


def build_quality_tiers(rows: list[dict], feature: str, cuts: list[float],
                        labels: list[str]) -> list[dict]:
    """Split matches into len(cuts)+1 value tiers over `feature`.

    Tier i holds rows with cuts[i-1] <= v < cuts[i]; the final tier holds
    rows with v >= cuts[-1]. Rows with a missing value are excluded.
    """
    tiers: dict[str, list[str]] = {label: [] for label in labels}
    for r in rows:
        v = r.get(feature)
        if _is_null(v):
            continue
        v = float(v)
        idx = 0
        for cut in cuts:
            if v < cut:
                break
            idx += 1
        result = r["match_result"]
        tiers[labels[idx]].append(result)
    entries: list[dict] = []
    for i, label in enumerate(labels):
        lo = cuts[i - 1] if i > 0 else None
        hi = cuts[i] if i < len(cuts) else None
        entries.append(_tier_stats(label, _range_label(lo, hi), tiers[label]))
    return entries


def build_home_quality(rows: list[dict],
                       split: float = HOME_QUALITY_SPLIT) -> dict:
    tiers = build_quality_tiers(rows, "home_team_home_win_rate", [split], ["low", "high"])
    gap = None
    low, high = tiers[0], tiers[1]
    if low["home_pct"] is not None and high["home_pct"] is not None:
        gap = round(high["home_pct"] - low["home_pct"], 1)
    return {"feature": "home_team_home_win_rate", "tiers": tiers, "home_win_pct_gap": gap}


def build_feature_by_result(rows: list[dict]) -> list[dict]:
    """Mean of each feature per outcome; sorted by home/draw/away spread."""
    entries: list[dict] = []
    for feature in NUMERIC_FEATURES:
        groups: dict[str, list[float]] = {k: [] for k in OUTCOME_KEYS}
        for r in rows:
            v = r.get(feature)
            if _is_null(v):
                continue
            groups[r["match_result"]].append(float(v))
        means = {k: statistics.fmean(g) for k, g in groups.items() if g}
        rounded = {k: round(m, 3) for k, m in means.items()}
        values = list(means.values())
        spread = (max(values) - min(values)) if len(values) >= 2 else None
        entries.append({
            "feature": feature,
            "n_values": sum(len(g) for g in groups.values()),
            "means": rounded,
            "range": round(spread, 3) if spread is not None else None,
        })
    entries.sort(key=lambda e: e["range"] if e["range"] is not None else -1, reverse=True)
    return entries


# ── report assembly ──────────────────────────────────────────────────────────
def build_report(conn, cfg: dict) -> dict:
    report = report_metadata(STEM, SCRIPT_NAME, cfg)
    try:
        rows = build_features.build_rows(conn, cfg["league"])
    except Exception:
        rows = []

    report["n_matches"] = len(rows)
    report["feature_count"] = len(NUMERIC_FEATURES)
    if not rows:
        report["data_warning"] = (
            f"No matches found for league '{cfg['league']}'; report sections are empty."
        )
    report["correlation_matrix"] = build_correlation_matrix(rows)
    report["form_vs_outcome"] = build_form_outcome(rows)
    report["position_vs_outcome"] = build_position_outcome(rows)
    report["rest_advantage"] = build_rest_advantage(rows)
    report["home_quality"] = build_home_quality(rows)
    report["feature_by_result"] = build_feature_by_result(rows)
    return report


# ── charts ───────────────────────────────────────────────────────────────────
def home_win_pct_bucket_chart(bins: list[dict], feature_label: str, title: str):
    fig, ax = new_figure(w=9, h=5)
    labels = [b["bucket"] for b in bins]
    values = [b["home_pct"] if b["home_pct"] is not None else 0.0 for b in bins]
    ax.bar(labels, values, color="#C44E52")
    ax.set_ylabel("home win %")
    ax.set_xlabel(feature_label)
    ax.set_title(title)
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)
    ax.set_ylim(0, None)
    fig.tight_layout()
    return fig


def build_charts(report: dict, out_dir: Path) -> list[Path]:
    if report["n_matches"] == 0:
        return []
    charts = [
        save_chart(
            out_dir, f"{STEM}_home_win_pct_by_form",
            home_win_pct_bucket_chart(
                report["form_vs_outcome"]["bins"],
                "form difference (home - away, last-5 points)",
                "Home win % by pre-match form difference",
            ),
        ),
        save_chart(
            out_dir, f"{STEM}_home_win_pct_by_position",
            home_win_pct_bucket_chart(
                report["position_vs_outcome"]["bins"],
                "position difference (home - away)",
                "Home win % by pre-match position difference",
            ),
        ),
    ]
    return [c for c in charts if c is not None]


# ── markdown rendering ───────────────────────────────────────────────────────
def _fmt_corr(value: float | None) -> str:
    return f"{value:.3f}" if value is not None else "-"


def _fmt_mean(value: float | None) -> str:
    return f"{value:.3f}" if value is not None else "-"


def _outcome_table(bins: list[dict]) -> str:
    return fmt_md_table(
        ["bucket", "matches", "home", "draw", "away", "home %", "draw %", "away %"],
        [
            [b["bucket"], b["n"], b["home_wins"], b["draws"], b["away_wins"],
             fmt_pct(b["home_pct"]), fmt_pct(b["draw_pct"]), fmt_pct(b["away_pct"])]
            for b in bins
        ],
    )


def render_markdown(report: dict) -> str:
    lines = render_report_header(report, "Relationships Analysis").splitlines()
    add = lines.append

    add("")
    add(f"- Matches analysed: **{report['n_matches']}** "
        f"({report['feature_count']} leakage-safe pre-match features).")
    if report.get("data_warning"):
        add(f"- **Warning:** {report['data_warning']}")

    add("")
    add("## 1. Correlation matrix")
    add("_Pearson correlation of each pre-match feature with observed goals; "
        "sorted by |corr(total goals)|._")
    add("")
    add(fmt_md_table(
        ["feature", "corr(home)", "corr(away)", "corr(total)"],
        [
            [c["feature"],
             _fmt_corr(c["corr_home_score"]),
             _fmt_corr(c["corr_away_score"]),
             _fmt_corr(c["corr_total_goals"])]
            for c in report["correlation_matrix"]
        ],
    ))

    add("")
    add("## 2. Form vs outcome")
    add("_Home win/draw/away % per bucket of `home_team_points_last_5 - "
       "away_team_points_last_5`._")
    add("")
    add(_outcome_table(report["form_vs_outcome"]["bins"]))

    add("")
    add("## 3. Position vs outcome")
    add("_Home win/draw/away % per bucket of `position_difference` "
       "(home position - away position; negative favours the home team)._")
    add("")
    add(_outcome_table(report["position_vs_outcome"]["bins"]))

    add("")
    add("## 4. Rest advantage")
    add("_Home win/draw/away % per bucket of `rest_days_difference` "
       "(home rest - away rest). Matches with unknown rest are bucketed "
       "separately._")
    add("")
    add(_outcome_table(report["rest_advantage"]["bins"]))
    unknown = next((b for b in report["rest_advantage"]["bins"] if b["bucket"] == "unknown"), None)
    if unknown and unknown["n"]:
        add(f"- *{unknown['n']} match(es) had unknown rest difference (missing "
            "rest data on at least one side).*")

    hq = report["home_quality"]
    add("")
    add("## 5. Home team quality")
    add(f"_Home win rate by `home_team_home_win_rate` tier (split at "
        f"{HOME_QUALITY_SPLIT:g})._")
    add("")
    for tier in hq["tiers"]:
        add(f"- `{tier['label']}` tier: **{fmt_pct(tier['home_pct'])}** home win "
            f"({tier['home_wins']}/{tier['n']})")
    if hq["home_win_pct_gap"] is not None:
        add(f"- Home-win gap (>= split minus < split): "
            f"**{hq['home_win_pct_gap']:+.1f} pp**")
    add("")
    add(fmt_md_table(
        ["tier", "label", "matches", "home", "draw", "away", "home %"],
        [
            [t["tier"], t["label"], t["n"], t["home_wins"], t["draws"],
             t["away_wins"], fmt_pct(t["home_pct"])]
            for t in hq["tiers"]
        ],
    ))

    add("")
    add("## 6. Feature averages by result")
    add("_Mean feature value per outcome; `range` is home-minus-away spread of "
        "the group means._")
    add("")
    add(fmt_md_table(
        ["feature", "home mean", "draw mean", "away mean", "range"],
        [
            [e["feature"],
             _fmt_mean(e["means"].get(HOME_OUTCOME)),
             _fmt_mean(e["means"].get(DRAW_OUTCOME)),
             _fmt_mean(e["means"].get(AWAY_OUTCOME)),
             _fmt_mean(e["range"])]
            for e in report["feature_by_result"]
        ],
    ))

    add("")
    add("---")
    add("*All features are leakage-safe pre-match values built by "
       "`ml.features.build_features.build_rows` from strictly prior matches. "
       "Run with `python backend/scripts/analyze_relationships.py` to "
       "regenerate.*")
    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────
def parse_module_args(argv: list[str] | None = None) -> argparse.Namespace:
    return parse_args(
        "Module 6 - Relationships analysis report "
        "(leakage-safe pre-match features vs outcomes).",
        argv=argv,
    )


def main(argv: list[str] | None = None) -> int:
    args = parse_module_args(argv)
    cfg = args_to_config(args)

    conn = get_conn()
    try:
        report = build_report(conn, cfg)
    finally:
        conn.close()

    out_dir = Path(cfg["out_dir"])
    try:
        charts = build_charts(report, out_dir)
    except ImportError:
        charts = []

    stem = cfg.get("out_stem") or STEM
    json_path, md_path = write_report(out_dir, stem, report, render_markdown, charts)

    print(f"{STEM} [{cfg['league']}]: {report['n_matches']} matches, "
          f"{report['feature_count']} features, "
          f"{len(report['correlation_matrix'])} correlations - "
          f"wrote {json_path} and {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
