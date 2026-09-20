"""Orchestrator for the Common Data Analysis Framework.

Runs every analysis module (0-7) in dependency order for a given league and
produces all reports under the output directory:

    python backend/scripts/run_analysis.py
    python backend/scripts/run_analysis.py --league premier
    python backend/scripts/run_analysis.py --skip relations --out-dir /tmp/out

Each module is executed as its own subprocess so a failure in one module never
stops the pipeline: the failure is recorded and the remaining modules (and the
final findings compilation) still run. The exit code is 0 only when every
selected module completed successfully.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from analysis_common import ROOT_DIR  # noqa: E402

SCRIPT_DIR = Path(__file__).resolve().parent

MODULES = [
    {"name": "Module 0 - Database profile", "script": "profile_database.py", "stem": "database_profile"},
    {"name": "Module 1 - Match outcomes", "script": "analyze_matches.py", "stem": "matches_analysis"},
    {"name": "Module 2 - Goal analysis", "script": "analyze_goals.py", "stem": "goals_analysis"},
    {"name": "Module 3 - Team analysis", "script": "analyze_teams.py", "stem": "teams_analysis"},
    {"name": "Module 4 - Season trends", "script": "analyze_seasons.py", "stem": "season_trends"},
    {"name": "Module 5 - Scoreline analysis", "script": "analyze_scorelines.py", "stem": "scoreline_analysis"},
    {"name": "Module 6 - Relationships", "script": "analyze_relationships.py", "stem": "relationships"},
    {"name": "Module 7 - Consolidated findings", "script": "compile_findings.py", "stem": "findings"},
]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run all Common Data Analysis Framework modules for a league.")
    parser.add_argument("--league", default="premier", help="league api_key (default: premier)")
    parser.add_argument("--out-dir", type=Path, default=None,
                        help="output directory (default: data/analysis/<league>)")
    parser.add_argument("--skip", nargs="+", default=[],
                        help="module stems to skip")
    parser.add_argument("--only", nargs="+", default=[],
                        help="run only these stems")
    return parser.parse_args(argv)


def selected_modules(skip: list[str], only: list[str]) -> list[dict]:
    if only:
        return [m for m in MODULES if m["stem"] in only]
    if skip:
        return [m for m in MODULES if m["stem"] not in skip]
    return list(MODULES)


def run_module(module: dict, league: str, out_dir: Path) -> tuple[str, bool]:
    script_path = SCRIPT_DIR / module["script"]
    try:
        result = subprocess.run(
            [sys.executable, str(script_path), "--league", league, "--out-dir", str(out_dir)],
            cwd=ROOT_DIR,
            check=False,
        )
        ok = result.returncode == 0
    except OSError as exc:
        print(f"{module['stem']}: failed to launch - {exc}")
        ok = False
    status = "ok" if ok else "failed"
    return status, ok


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    out_dir = args.out_dir.resolve() if args.out_dir is not None else (
        ROOT_DIR / "data" / "analysis" / args.league
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    modules = selected_modules(args.skip, args.only)
    if not modules:
        print("run_analysis: no modules selected")
        return 1

    results: list[dict] = []
    for module in modules:
        print(f"⏺ {module['name']} ...")
        status, ok = run_module(module, args.league, out_dir)
        results.append({"module": module["name"], "stem": module["stem"], "status": status})
        if not ok:
            print(f"  {module['stem']}: FAILED (continuing)")

    print("")
    print("run_analysis summary:")
    print("| module | stem | status |")
    print("|--------|------|--------|")
    for r in results:
        print(f"| {r['module']} | {r['stem']} | {r['status']} |")

    failed = [r["stem"] for r in results if r["status"] != "ok"]
    if failed:
        print(f"run_analysis: {len(failed)} module(s) failed: {', '.join(failed)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())