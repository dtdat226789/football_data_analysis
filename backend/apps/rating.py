from __future__ import annotations

import math
from typing import Any, Iterable

WEIGHTS: dict[str, float] = {
    "points_per_game": 0.35,
    "goal_difference_per_game": 0.25,
    "expected_points_per_game": 0.25,
    "last_5_points_rate": 0.15,
}


def _number(value: Any) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _divide(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator is None or denominator == 0:
        return None
    return numerator / denominator


def _raw_signals(row: dict[str, Any]) -> dict[str, float | None]:
    played = _number(row.get("played"))
    if played is None or played <= 0:
        return {}
    metrics = row.get("metrics")
    if not isinstance(metrics, dict):
        metrics = {}
    gf = _number(row.get("goals_for"))
    ga = _number(row.get("goals_against"))
    goal_difference = None if gf is None or ga is None else gf - ga
    recent = min(played, 5)
    return {
        "points_per_game": _divide(_number(row.get("points")), played),
        "goal_difference_per_game": _divide(goal_difference, played),
        "expected_points_per_game": _divide(_number(metrics.get("expected_points")), played),
        "last_5_points_rate": _divide(
            _number(metrics.get("last_5_points")),
            3 * recent,
        ),
    }


def _normalise(values: dict[int, float | None]) -> dict[int, float | None]:
    present = [value for value in values.values() if value is not None]
    if not present:
        return {team_id: None for team_id in values}
    low, high = min(present), max(present)
    flat = high - low <= 1e-12
    result: dict[int, float | None] = {}
    for team_id, value in values.items():
        if value is None:
            result[team_id] = None
        elif flat:
            result[team_id] = 0.5
        else:
            result[team_id] = (value - low) / (high - low)
    return result


def _ranks(scores: dict[int, float]) -> dict[int, int]:
    return {
        team_id: 1 + sum(1 for other in scores.values() if other > score + 1e-9)
        for team_id, score in scores.items()
    }


def club_ratings(rows: Iterable[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    raw: dict[int, dict[str, float | None]] = {}
    for row in rows:
        team_id = row.get("team_id")
        if team_id is None:
            continue
        signals = _raw_signals(row)
        if signals:
            raw[team_id] = signals
    if not raw:
        return {}

    normalised = {
        name: _normalise({team_id: values[name] for team_id, values in raw.items()})
        for name in WEIGHTS
    }

    ratings: dict[int, dict[str, Any]] = {}
    for team_id in raw:
        signals = {
            name: normalised[name][team_id]
            for name in WEIGHTS
            if normalised[name][team_id] is not None
        }
        weight = sum(WEIGHTS[name] for name in signals)
        score = (
            round(100 * sum(WEIGHTS[name] * value for name, value in signals.items()) / weight, 1)
            if weight
            else 50.0
        )
        ratings[team_id] = {
            "score": score,
            "rank": 0,
            "rank_total": len(raw),
            "signals": {name: round(value, 4) for name, value in signals.items()},
        }

    ranks = _ranks({team_id: rating["score"] for team_id, rating in ratings.items()})
    for team_id, rank in ranks.items():
        ratings[team_id]["rank"] = rank
    return ratings
