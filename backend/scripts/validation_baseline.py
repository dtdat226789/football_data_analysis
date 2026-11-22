"""Track per-league validation findings and gate refresh on regressions.

The raw-data validator exits non-zero whenever it finds errors, but the
repository carries a known backlog of historical data-quality findings. The
refresh pipeline therefore compares each run against the previous baseline and
only blocks publication when a league got worse or a report was unusable. With
no baseline (a clean CI checkout) the counts are recorded but not treated as a
new regression.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import TypeAlias

Counts: TypeAlias = tuple[int, int] | None


def read_tally(path: Path) -> dict[str, Counts]:
    """Read the `league errors warnings` lines written by the refresh loop."""
    current: dict[str, Counts] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        parts = line.split()
        if len(parts) != 3:
            continue
        league, errors, warnings = parts
        if "-" in (errors, warnings):
            current[league] = None
        else:
            current[league] = (int(errors), int(warnings))
    return current


def read_baseline(path: Path) -> dict[str, Counts]:
    """Read the previous baseline; a missing or corrupt file means 'no baseline'."""
    if not path.exists():
        return {}
    try:
        raw = json.loads(path.read_text(encoding="utf-8")).get("counts", {})
    except (OSError, ValueError, AttributeError, TypeError):
        return {}
    baseline: dict[str, Counts] = {}
    for league, value in raw.items():
        if isinstance(value, (list, tuple)) and len(value) == 2:
            baseline[league] = (int(value[0]), int(value[1]))
        else:
            baseline[league] = None
    return baseline


def compare(current: dict[str, Counts], baseline: dict[str, Counts]) -> dict:
    """Summarise the run and decide whether it should block publication."""
    scored = {league: counts for league, counts in current.items() if counts is not None}
    missing = sorted(league for league, counts in current.items() if counts is None)
    total_errors = sum(counts[0] for counts in scored.values())
    total_warnings = sum(counts[1] for counts in scored.values())

    worsened = [
        {"league": league, "before": baseline[league][0], "after": counts[0]}
        for league, counts in sorted(scored.items())
        if baseline.get(league) is not None and counts[0] > baseline[league][0]  # type: ignore[index]
    ]
    improved = [
        league
        for league, counts in sorted(scored.items())
        if baseline.get(league) is not None and counts[0] < baseline[league][0]  # type: ignore[index]
    ]
    # A league appearing for the first time with errors is a regression only
    # once a baseline exists; the very first run records the known backlog.
    untracked = (
        [league for league, counts in sorted(scored.items()) if league not in baseline and counts[0] > 0]
        if baseline
        else []
    )

    reasons: list[str] = []
    if worsened:
        reasons.append(
            "error count increased for " + ", ".join(item["league"] for item in worsened)
        )
    if untracked:
        reasons.append("new leagues with errors: " + ", ".join(untracked))
    if missing:
        reasons.append("no usable report for " + ", ".join(missing))

    return {
        "totals": {"errors": total_errors, "warnings": total_warnings},
        "scored": len(scored),
        "requested": len(current),
        "worsened": worsened,
        "improved": improved,
        "untracked": untracked,
        "missing": missing,
        "blocking": bool(reasons),
        "reasons": reasons,
    }


def write_baseline(path: Path, current: dict[str, Counts], result: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "counts": {league: list(counts) if counts is not None else None for league, counts in current.items()},
        "totals": result["totals"],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def write_status(path: Path, result: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tally", required=True, metavar="PATH")
    parser.add_argument("--baseline", required=True, metavar="PATH")
    parser.add_argument("--status", required=True, metavar="PATH")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    current = read_tally(Path(args.tally))
    baseline = read_baseline(Path(args.baseline))
    result = compare(current, baseline)

    totals = result["totals"]
    print(
        f"  leagues requested: {result['requested']}  scored: {result['scored']}  "
        f"errors: {totals['errors']}  warnings: {totals['warnings']}"
    )
    if not baseline:
        print("  no baseline yet; recording this run's counts for future comparison")
    else:
        for item in result["worsened"]:
            print(f"    WORSE {item['league']}: {item['before']} -> {item['after']}")
        if result["improved"]:
            print(f"  note: error count decreased for {len(result['improved'])} league(s)")
        if not result["worsened"] and not result["improved"] and not result["untracked"]:
            print("  error counts unchanged since the last run")
    for reason in result["reasons"]:
        print(f"  BLOCKING: {reason}")

    if result["blocking"]:
        print("  baseline not updated because this run is blocked")
    else:
        write_baseline(Path(args.baseline), current, result)
        print(f"  baseline written to {args.baseline}")
    write_status(Path(args.status), result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
