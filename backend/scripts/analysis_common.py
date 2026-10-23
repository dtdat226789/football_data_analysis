"""Shared helpers for the Common Data Analysis Framework.

Every analyze_*.py module imports from this file for:
  - argument parsing (--league, --out-dir, --out-stem)
  - report metadata headers
  - markdown table rendering
  - file writing (JSON + MD)
  - chart generation (matplotlib, guarded import)
  - pure math helpers (percentages, percentiles, sorting)
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from db_common import LEAGUE, league_meta  # noqa: E402

VERSION = "1.0.0"


# ── path rendering ───────────────────────────────────────────────────────────
def rel_to_root(path: Path | str) -> str:
    """Render a path repo-relative with POSIX separators, for report output.

    Reports are committed artifacts, so they must not embed machine-specific
    absolute paths. A Windows checkout writes ``E:\\repo\\data\\...`` while a
    WSL checkout of the same tree writes ``/mnt/e/repo/data/...``; embedding
    either one rewrites every generated report whenever the tree moves or is
    cloned on another platform. Paths outside the repo fall back to an absolute
    POSIX path, since there is no meaningful relative form for them.
    """
    resolved = Path(path).resolve()
    try:
        return resolved.relative_to(ROOT_DIR).as_posix()
    except ValueError:
        return resolved.as_posix()


# ── matplotlib (optional) ────────────────────────────────────────────────────
def _has_matplotlib() -> bool:
    try:
        import matplotlib  # noqa: F401
        return True
    except ImportError:
        return False


def save_chart(out_dir: Path, name: str, fig) -> Path | None:
    """Save a matplotlib figure as PNG; return path or None if not possible."""
    if not _has_matplotlib():
        return None
    charts_dir = out_dir / "charts"
    charts_dir.mkdir(parents=True, exist_ok=True)
    path = charts_dir / f"{name}.png"
    fig.savefig(path, dpi=120, bbox_inches="tight")
    import matplotlib.pyplot as plt
    plt.close(fig)
    return path


def new_figure(w: float = 8, h: float = 5):
    """Create a matplotlib figure using the Agg backend (non-interactive)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    return plt.subplots(figsize=(w, h))


# ── argument parsing ─────────────────────────────────────────────────────────
def parse_args(description: str, argv: list[str] | None = None,
               extra: argparse.ArgumentParser | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--league", default=LEAGUE, help="league api_key (default: premier)")
    parser.add_argument("--out-dir", type=Path, default=ROOT_DIR / "data" / "analysis",
                        help="output directory (default: data/analysis)")
    parser.add_argument("--out-stem", type=str, default=None,
                        help="output file stem override (default: derived from module)")
    if extra:
        for action in extra._actions:
            if isinstance(action, argparse._HelpAction):
                continue
            parser._add_action(action)
    return parser.parse_args(argv)


def args_to_config(args: argparse.Namespace) -> dict:
    return {
        "league": args.league,
        "out_dir": rel_to_root(args.out_dir),
        "out_stem": args.out_stem,
    }


# ── report metadata ──────────────────────────────────────────────────────────
def report_metadata(report_name: str, script: str, cfg: dict) -> dict:
    meta = league_meta(cfg["league"])
    return {
        "report_name": report_name,
        "script": {"name": script, "version": VERSION},
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "config": cfg,
        "league": meta,
    }


# ── markdown helpers ─────────────────────────────────────────────────────────
def fmt_pct(value: float | None, ndigits: int = 1) -> str:
    if value is None:
        return "-"
    return f"{value:.{ndigits}f}%"


def fmt_md_table(headers: list[str], rows: list[list]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines)


def render_report_header(report: dict, title: str) -> str:
    meta = report
    lines = [
        f"# {title}",
        f"- Report: `{meta['report_name']}`",
        f"- Generated: {meta['generated_at']}",
        f"- Script: `{meta['script']['name']}` v{meta['script']['version']}",
        f"- League: {meta['league']['name']} ({meta['league']['country']})",
        f"- Scope: league `{meta['config']['league']}`",
        "",
    ]
    return "\n".join(lines)


# ── file output ──────────────────────────────────────────────────────────────
def md_link(target: Path, md_path: Path) -> str:
    """Render a Markdown link target relative to the .md file that embeds it.

    Markdown resolves a relative target against the directory holding the
    document, so a chart at ``<out_dir>/charts/c.png`` referenced from
    ``<out_dir>/report.md`` must be written as ``charts/c.png``. A repo-root
    path would resolve to ``<out_dir>/data/analysis/...`` and 404, and an
    absolute path would tie the committed report to one machine.
    """
    target_resolved = Path(target).resolve()
    try:
        return target_resolved.relative_to(md_path.resolve().parent).as_posix()
    except ValueError:
        return rel_to_root(target_resolved)


def write_report(out_dir: Path, stem: str, report: dict,
                 render_md: callable, charts: list[Path] | None = None) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"{stem}.json"
    md_path = out_dir / f"{stem}.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False, default=str) + "\n")
    md_text = render_md(report)
    if charts:
        chart_section = "\n\n## Charts\n\n"
        for c in charts:
            chart_section += f"![{c.stem}]({md_link(c, md_path)})\n"
        md_text += chart_section
    md_path.write_text(md_text + "\n")
    return json_path, md_path


# ── pure math helpers ────────────────────────────────────────────────────────
def round_pct(count: int, total: int, ndigits: int = 1) -> float | None:
    if total <= 0:
        return None
    return round(100.0 * count / total, ndigits)


def classify_outcome(home: int, away: int) -> str:
    if home > away:
        return "home"
    if home == away:
        return "draw"
    return "away"


def percentile(sorted_values: list[int], q: float) -> int | float | None:
    if not sorted_values:
        return None
    n = len(sorted_values)
    if n == 1:
        return sorted_values[0]
    pos = (n - 1) * q
    lo = int(pos)
    frac = pos - lo
    lo_val = sorted_values[lo]
    hi_val = sorted_values[min(lo + 1, n - 1)]
    return round(lo_val + frac * (hi_val - lo_val), 2)


def summarize_values(values: list[int | float]) -> dict | None:
    if not values:
        return None
    s = sorted(values)
    return {
        "n": len(s),
        "min": s[0],
        "max": s[-1],
        "mean": round(statistics.fmean(s), 2),
        "p25": percentile(s, 0.25),
        "p50": percentile(s, 0.50),
        "p75": percentile(s, 0.75),
    }


def season_sort_key(name: str) -> tuple:
    parts = [p for p in name.split("-") if p.isdigit()]
    if not parts:
        return (0, 0, name)
    start = int(parts[0])
    end = int(parts[-1]) if len(parts) > 1 else start
    return (min(start, end), max(start, end), name)


def pearson(xs: list[float], ys: list[float]) -> float | None:
    """Pearson correlation coefficient (no dependencies beyond stdlib)."""
    n = len(xs)
    if n < 3:
        return None
    mx = statistics.fmean(xs)
    my = statistics.fmean(ys)
    sx = statistics.pstdev(xs)
    sy = statistics.pstdev(ys)
    if sx == 0 or sy == 0:
        return 0.0
    cov = statistics.fmean([(x - mx) * (y - my) for x, y in zip(xs, ys)])
    return round(cov / (sx * sy), 4)


def cross_tab(values1: list[str], values2: list[str]) -> dict[str, dict[str, int]]:
    """Two-way frequency table."""
    tabs: dict[str, dict[str, int]] = {}
    for v1, v2 in zip(values1, values2):
        tabs.setdefault(v1, {})
        tabs[v1][v2] = tabs[v1].get(v2, 0) + 1
    return tabs
