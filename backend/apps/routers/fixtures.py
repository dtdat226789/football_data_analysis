"""Upcoming fixtures API: serves the fetch_fixtures.py dump as read-only JSON.

Data lives in data/raw/fixtures/*.json (one file per league, produced by
backend/scripts/fetch_fixtures.py). The endpoints never touch the API key or
the database: they are pure file lookups, so a league with no collected
fixtures returns an empty list rather than an error.

Routes:
    GET /api/v1/fixtures            merged, pruned upcoming matches (all leagues)
    GET /api/v1/fixtures/{league}   full stored payload for one league
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Literal

from fastapi import APIRouter

from .. import common
from ..deps import require_league

router = APIRouter(tags=["fixtures"])

FIXTURES_DIR = common.ROOT_DIR / "data" / "raw" / "fixtures"

DEFAULT_LIMIT = 20
MAX_LIMIT = 200


def _load_payload(path: Path) -> dict:
    """Read one fixtures file, tolerating bad/absent files."""
    try:
        payload = json.loads(path.read_bytes())
    except (OSError, ValueError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _prediction_summary(match: dict) -> dict:
    """Compact dc_v2 prediction summary for a fixture."""
    preds = (match.get("model_predictions") or {}).get("dc_v2") or {}
    calibrated = preds.get("calibrated") or {}
    raw = preds.get("raw") or {}
    home = calibrated.get("home")
    away = calibrated.get("away")
    return {
        "home": home,
        "away": away,
        "btts_yes": calibrated.get("btts_yes"),
        "over_1_5": calibrated.get("over_1.5"),
        "over_2_5": calibrated.get("over_2.5"),
        "over_3_5": calibrated.get("over_3.5"),
        "expected_home_goals": raw.get("expected_home_goals"),
        "expected_away_goals": raw.get("expected_away_goals"),
        "confidence": round(max(
            [p for p in (home, away) if isinstance(p, (int, float))],
            default=0.0,
        ), 4),
        "computed_at": preds.get("computed_at"),
        "data_through": preds.get("data_through"),
    }


def _prune(match: dict, league: str) -> dict:
    """Keep the display fields + prediction summary for the merged feed."""
    return {
        "slug": match.get("slug"),
        "league": league,
        "country": match.get("country"),
        "home_team": match.get("home_team"),
        "away_team": match.get("away_team"),
        "match_date": match.get("match_date"),
        "time": match.get("time"),
        "status": match.get("status"),
        "predictions": _prediction_summary(match),
    }


def list_fixture_files() -> list[Path]:
    """Every league fixtures file (ignores the manifest)."""
    if not FIXTURES_DIR.is_dir():
        return []
    return sorted(
        p for p in FIXTURES_DIR.glob("*.json")
        if p.name != "manifest.json"
    )


def league_fixture_file(league: str) -> Path | None:
    """Path to a league's fixtures file, or None when not collected."""
    path = FIXTURES_DIR / f"{league}.json"
    return path if path.exists() else None


def fixture_rows(league: str | None = None) -> list[dict]:
    """Pruned match rows for one league, or for every collected league."""
    if league is not None:
        paths = [league_fixture_file(league)] if league_fixture_file(league) else []
    else:
        paths = list_fixture_files()
    rows: list[dict] = []
    for path in paths:
        lg = path.stem
        payload = _load_payload(path)
        for match in payload.get("matches") or []:
            rows.append(_prune(match, lg))
    return rows


@router.get("/fixtures")
def list_fixtures(
    league: str | None = None,
    sort: Literal["date", "confidence"] = "confidence",
    limit: int = DEFAULT_LIMIT,
) -> dict:
    """Merged upcoming fixtures, pruned, sorted by date or model confidence."""
    limit = min(max(limit, 1), MAX_LIMIT)
    if league is not None:
        require_league(league)
    rows = fixture_rows(league)

    if sort == "confidence":
        rows.sort(key=lambda r: r["predictions"]["confidence"], reverse=True)
    else:
        rows.sort(key=lambda r: (r["match_date"] or "", r["time"] or ""))
    return {
        "count": len(rows),
        "total": len(rows),
        "limit": limit,
        "sort": sort,
        "league": league,
        "matches": rows[:limit],
    }


@router.get("/fixtures/{league}")
def league_fixtures(league: str) -> dict:
    """Full stored fixtures payload for one league (raw model_predictions)."""
    require_league(league)
    path = league_fixture_file(league)
    if path is None:
        return {"league": league, "count": 0, "matches": [], "attribution": "Data by football-charts.com"}
    payload = _load_payload(path)
    payload.setdefault("count", len(payload.get("matches") or []))
    payload.setdefault("league", league)
    return payload