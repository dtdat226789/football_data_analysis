"""Upcoming fixtures API: serves the fetch_fixtures.py dump as read-only JSON.

Data lives in data/raw/fixtures/*.json (one file per league, produced by
backend/scripts/fetch_fixtures.py). The endpoints never touch the API key or
the database: they are pure file lookups, so a league with no collected
fixtures returns an empty list rather than an error.

Route:
    GET /api/v1/fixtures            merged, pruned upcoming matches (all leagues)
    GET /api/v1/fixtures/{league}   full stored payload for one league

Single-fixture detail is the one exception: head-to-head, matchday and form
cannot be answered from a fixtures file, so it additionally reads history from
PostgreSQL through the same read-only cursor the rest of the API uses.

    GET /api/v1/fixtures/{league}/{match_id}

Every DB-derived section is independently optional. A fixture whose teams are
not in the analytics database (a brand-new season, a league never collected)
still serves predictions, form and kickoff metadata from the file dump alone,
and `detail_collected` reports whether the richer /matches/{slug}/ payload from
backend/scripts/fetch_fixture_details.py is on disk.

Predictions carry two things beyond what the feed publishes. `markets` is the
full derived menu — Asian handicaps, correct score, HT/FT, team totals — and
`selected` is the confident subset, both built in apps/markets.py from the
dc_v2 goal parameters and tagged by whether they are model output or a stated
assumption. The list feed carries only `selected`, under `predictions`.
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Literal

from fastapi import APIRouter, HTTPException

from .. import common
from ..deps import fetched_cursor, norm_pagination, require_league, resolve_team_id
from ..markets import market_detail, markets_from_prediction
from .matches import build_pre_match, check_date_window, head_to_head
from .teams import _form_result

router = APIRouter(tags=["fixtures"])

FIXTURES_DIR = common.ROOT_DIR / "data" / "raw" / "fixtures"

DEFAULT_LIMIT = 20
MAX_LIMIT = 200

FORM_LIMIT = 5
H2H_LIMIT = 10

# Goal lines the dc_v2 model reports, e.g. `over_2.5` and `ht_over_1.5`. The
# prefix marks the scope; the remainder is the line the market is quoted at.
_GOAL_LINE = re.compile(r"^(ht_)?over_(\d+(?:\.\d+)?)$")


def details_dir() -> Path:
    """Where per-fixture /matches/{slug}/ payloads live.

    Derived from FIXTURES_DIR on every call rather than captured at import, so
    tests that relocate FIXTURES_DIR relocate the detail files with it.
    """
    return FIXTURES_DIR / "details"


def _load_payload(path: Path) -> dict:
    """Read one fixtures file, tolerating bad/absent files."""
    try:
        payload = json.loads(path.read_bytes())
    except (OSError, ValueError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _as_date(value) -> date | None:
    """Fixture dates arrive as JSON strings; the database hands back `date`.

    Normalising here means every query parameter is the same type and the
    rest-day arithmetic is real date subtraction rather than string subtraction.
    """
    if isinstance(value, date):
        return value
    if isinstance(value, str) and value:
        try:
            return date.fromisoformat(value[:10])
        except ValueError:
            return None
    return None


def _in_window(row: dict, start: date | None, end: date | None) -> bool:
    """Whether a pruned fixture falls inside an optional [start, end] window.

    A row whose date will not parse is kept when there is no lower bound and
    dropped when there is one: the caller asked for a window, and a date-less row
    cannot be shown to be inside it. Silently widening the window to include it
    would be a different answer to the same question.
    """
    match_date = _as_date(row.get("match_date"))
    if match_date is None:
        return start is None and end is None
    if start is not None and match_date < start:
        return False
    if end is not None and match_date > end:
        return False
    return True


def _prediction_summary(match: dict, selected: list | None = None) -> dict:
    """Compact dc_v2 prediction summary for a fixture.

    `selected` is the short list of markets the model is most confident about,
    which is what the list feed renders as chips. It is derived rather than read
    (see apps/markets.py) and stays small so the merged feed does not carry a
    full market table on every row. Callers that already hold the derived
    markets pass `selected` in rather than deriving them twice.
    """
    preds = (match.get("model_predictions") or {}).get("dc_v2") or {}
    calibrated = preds.get("calibrated") or {}
    raw = preds.get("raw") or {}
    if selected is None:
        selected = markets_from_prediction(preds)["selected"]
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
        "selected": selected,
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
        "league_name": common.league_name(league),
        "country": match.get("country"),
        "home_team": match.get("home_team"),
        "away_team": match.get("away_team"),
        "match_date": match.get("match_date"),
        "time": match.get("time"),
        "status": match.get("status"),
        "predictions": _prediction_summary(match),
    }


def list_fixture_files() -> list[Path]:
    """Every league fixtures file (ignores the manifest and details dir)."""
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


def fixture_rows(league: str | None = None, today: date | None = None) -> list[dict]:
    """Pruned match rows for one league, or for every collected league.

    `today` drops anything already played, defaulting to the current date.
    The upstream feed is a snapshot that never flips `status` off "scheduled", so
    a dump collected days ago still describes matches that have since been kicked
    off; the date is the only signal that is actually correct. Rows without a
    parsable date are kept, since dropping them would silently hide a fixture
    rather than merely demote it. Callers that genuinely want the whole stored
    snapshot pass `date.min`.
    """
    if league is not None:
        path = league_fixture_file(league)
        paths = [path] if path else []
    else:
        paths = list_fixture_files()
    cutoff = date.today() if today is None else today
    rows: list[dict] = []
    for path in paths:
        lg = path.stem
        payload = _load_payload(path)
        for match in payload.get("matches") or []:
            row = _prune(match, lg)
            match_date = _as_date(row.get("match_date"))
            if match_date is None or match_date >= cutoff:
                rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# Single-fixture detail
# ---------------------------------------------------------------------------


def slug_tail(slug: str) -> str:
    """Last segment of an upstream slug: `a/b/2026-01-01-x-vs-y` -> `2026-01-01-x-vs-y`.

    Upstream slugs embed slashes, so the tail is what the detail files are named
    after and what a UI puts in a route.
    """
    return (slug or "").rstrip("/").rsplit("/", 1)[-1]


def detail_file(league: str, slug: str) -> Path:
    """Path to a collected /matches/{slug}/ payload for a fixture."""
    return details_dir() / f"{league}__{slug_tail(slug)}.json"


def find_fixture(league: str, match_id: str) -> dict | None:
    """One fixture row from a league's dump, addressed by slug or slug tail.

    Accepts the full upstream slug, the trailing `date-home-vs-away` segment, or
    either with a `.json` suffix, so callers are not forced to know the storage
    convention.
    """
    path = league_fixture_file(league)
    if path is None:
        return None
    wanted = (match_id or "").strip().strip("/")
    if wanted.endswith(".json"):
        wanted = wanted[: -len(".json")]
    tail = slug_tail(wanted)
    for match in _load_payload(path).get("matches") or []:
        slug = match.get("slug") or ""
        if wanted in (slug, slug_tail(slug)):
            return match
    # A bare tail that matches nothing exactly is still worth one look: two
    # fixtures can share a date-and-teams tail across competition rounds.
    if tail and tail != wanted:
        for match in _load_payload(path).get("matches") or []:
            if slug_tail(match.get("slug") or "") == tail:
                return match
    return None


def _load_detail(league: str, slug: str) -> dict:
    """The collected /matches/{slug}/ payload for a fixture, or {}."""
    path = detail_file(league, slug)
    if not path.exists():
        return {}
    payload = _load_payload(path)
    match = payload.get("match")
    return match if isinstance(match, dict) else {}


def _probability_triple(calibrated: dict) -> dict:
    """Home/draw/away from the calibrated block.

    dc_v2 calibrates home and away independently and lets the remainder be the
    draw, so draw is derived rather than read. When the two do not sum to <= 1
    (an unrounded or partially published block) nothing is inferred and draw is
    null, because a negative probability would be worse than a missing one.
    """
    home, away = calibrated.get("home"), calibrated.get("away")
    if not isinstance(home, (int, float)) or not isinstance(away, (int, float)):
        return {"home": home, "draw": None, "away": away}
    total = home + away
    draw = round(1.0 - total, 4) if 0.0 < total <= 1.0 else None
    return {"home": home, "draw": draw, "away": away}


def _goal_lines(raw: dict, calibrated: dict) -> list[dict]:
    """Every over/under line the model priced, full time and half time.

    Both blocks are walked so the table can show the model's uncalibrated and
    calibrated read of the same line side by side.
    """
    lines: list[dict] = []
    for source, block in (("raw", raw), ("calibrated", calibrated)):
        for key, value in block.items():
            match = _GOAL_LINE.match(key or "")
            if not match or not isinstance(value, (int, float)):
                continue
            entry = next((row for row in lines if row["line"] == key), None)
            if entry is None:
                lines.append({
                    "line": key,
                    "scope": "half_time" if match.group(1) else "full_time",
                    "threshold": match.group(2),
                    "raw": None,
                    "calibrated": None,
                })
                entry = lines[-1]
            entry[source] = value
    lines.sort(key=lambda row: (row["scope"] != "full_time", float(row["threshold"])))
    return lines


def predictability(match: dict) -> dict | None:
    """The full dc_v2 block for a fixture, not just the chip summary.

    `summary` is the same object the list feed renders, so a detail view and a
    row in /fixtures never disagree about the headline numbers.

    `markets` is the whole derived menu and `selected` the confident subset. Both
    come from apps/markets.py and are omitted rather than faked when the block
    carries no usable lambdas.
    """
    preds = (match.get("model_predictions") or {}).get("dc_v2") or {}
    if not preds:
        return None
    raw = preds.get("raw") or {}
    calibrated = preds.get("calibrated") or {}
    derived = markets_from_prediction(preds)
    return {
        "model": preds.get("model"),
        # xi is a constant placeholder across every collected block and is not
        # the correction that generated the published probabilities — the real
        # one is solved for from the published O/U lines instead. Kept for
        # reference; apps/markets.py explains why it is not used.
        "xi": preds.get("xi"),
        "sigma": preds.get("sigma"),
        "summary": _prediction_summary(match, selected=derived["selected"]),
        "probabilities": _probability_triple(calibrated),
        "expected_goals": {
            "home": raw.get("expected_home_goals"),
            "away": raw.get("expected_away_goals"),
            "half_time_total": raw.get("expected_ht_goals"),
        },
        "lines": _goal_lines(raw, calibrated),
        "markets": derived["markets"],
        "selected": derived["selected"],
        "ratings": preds.get("ratings") or {},
        "effective_matches": preds.get("effective_matches") or {},
        "gates": preds.get("gates") or {},
        "data_status": preds.get("data_status") or {},
        "data_through": preds.get("data_through"),
        "computed_at": preds.get("computed_at"),
        "raw": raw,
        "calibrated": calibrated,
    }


# Venue-conditioned goal expressions. Selected by a literal, never by input, so
# no user-supplied value reaches the SQL string.
_VENUE_COLUMNS = {
    "home": ("m.home_team_id", "m.home_score", "m.away_score"),
    "away": ("m.away_team_id", "m.away_score", "m.home_score"),
}


def _venue_split(cur, league_season_id: int, team_id: int, venue: str, before_date) -> dict | None:
    """A team's home (or away) record before a date, inside one league season."""
    team_column, goals_for, goals_against = _VENUE_COLUMNS[venue]
    cur.execute(
        f"""
        SELECT count(*) AS played,
               sum(CASE WHEN {goals_for} > {goals_against} THEN 1 ELSE 0 END) AS wins,
               sum(CASE WHEN {goals_for} = {goals_against} THEN 1 ELSE 0 END) AS draws,
               sum(CASE WHEN {goals_for} < {goals_against} THEN 1 ELSE 0 END) AS losses,
               sum({goals_for}) AS goals_for,
               sum({goals_against}) AS goals_against
        FROM matches m
        WHERE m.league_season_id = %s
          AND m.match_date < %s
          AND {team_column} = %s
        """,
        (league_season_id, before_date, team_id),
    )
    row = cur.fetchone()
    if not row or not row["played"]:
        return None
    played = int(row["played"])
    scored = int(row["goals_for"] or 0)
    conceded = int(row["goals_against"] or 0)
    return {
        "played": played,
        "wins": int(row["wins"] or 0),
        "draws": int(row["draws"] or 0),
        "losses": int(row["losses"] or 0),
        "goals_for": scored,
        "goals_against": conceded,
        "win_rate": round(int(row["wins"] or 0) / played, 4),
        "goals_avg": round(scored / played, 3),
        "conceded_avg": round(conceded / played, 3),
    }


def _team_matches_before(
    cur, league_season_id: int, team_id: int, before_date, limit: int
) -> list[dict]:
    """A team's most recent matches before a date, newest first."""
    cur.execute(
        """
        SELECT m.api_id, m.match_date, m.kickoff_time, m.game_index,
               th.api_name AS home_team, ta.api_name AS away_team,
               m.home_score, m.away_score, m.home_team_id, m.away_team_id
        FROM matches m
        JOIN team_seasons th
          ON th.league_season_id = m.league_season_id AND th.team_id = m.home_team_id
        JOIN team_seasons ta
          ON ta.league_season_id = m.league_season_id AND ta.team_id = m.away_team_id
        WHERE m.league_season_id = %s
          AND m.match_date < %s
          AND (m.home_team_id = %s OR m.away_team_id = %s)
        ORDER BY m.match_date DESC, m.kickoff_time DESC, m.game_index DESC
        LIMIT %s
        """,
        (league_season_id, before_date, team_id, team_id, limit),
    )
    return [dict(r) for r in cur.fetchall()]


def _team_context(
    cur, league_season_id: int, team_id: int, side: str, before_date, limit: int
) -> dict:
    """Form, venue split, rest and load for one side of an unplayed fixture.

    The last-`limit` aggregates are computed here rather than in the caller
    because the goals a team scored depend on which side it was playing: summing
    `home_score` blindly would credit an away side with its opponent's goals.
    """
    rows = _team_matches_before(cur, league_season_id, team_id, before_date, limit)
    results = [_form_result(r, team_id) for r in rows]
    scored = sum(
        r["home_score"] if r["home_team_id"] == team_id else r["away_score"] for r in rows
    )
    conceded = sum(
        r["away_score"] if r["home_team_id"] == team_id else r["home_score"] for r in rows
    )
    return {
        "team_id": team_id,
        "venue_side": side,
        "form": results,
        "form_line": [r["team_result"] for r in results],
        "points": sum(r["points"] for r in results),
        "wins": sum(1 for r in results if r["team_result"] == "W"),
        "goals_scored": scored,
        "goals_conceded": conceded,
        "rest_days": (before_date - rows[0]["match_date"]).days if rows else None,
        "games_before": _played_total(cur, league_season_id, team_id, before_date),
        "venue": _venue_split(cur, league_season_id, team_id, side, before_date),
    }


def _played_total(cur, league_season_id: int, team_id: int, before_date) -> int:
    cur.execute(
        """
        SELECT count(*) AS played
        FROM matches m
        WHERE m.league_season_id = %s
          AND m.match_date < %s
          AND (m.home_team_id = %s OR m.away_team_id = %s)
        """,
        (league_season_id, before_date, team_id, team_id),
    )
    row = cur.fetchone()
    return int(row["played"]) if row and row["played"] else 0


def _season_for_date(cur, league: str, match_date) -> dict | None:
    """The league season a fixture belongs to, chosen by date.

    Prefer the registered season whose date window contains the fixture. Fall
    back to the latest season with prior matches only when no window match
    exists.
    """
    from db_common import parse_season_years, season_date_window  # noqa: PLC0415

    cur.execute(
        """
        SELECT ls.id, s.name AS season, ls.season_state, s.start_year, s.end_year
        FROM league_seasons ls
        JOIN seasons s ON s.id = ls.season_id
        JOIN leagues l ON l.id = ls.league_id
        WHERE l.api_key = %s
        ORDER BY s.start_year DESC, s.end_year DESC
        """,
        (league,),
    )
    rows = cur.fetchall() or []
    for r in rows:
        name = r["season"]
        window = season_date_window(name)
        if window and window[0] <= match_date <= window[1]:
            return {"id": r["id"], "season": r["season"], "season_state": r["season_state"]}
    if not rows:
        return None
    for r in rows:
        cur.execute(
            "SELECT 1 FROM matches WHERE league_season_id = %s AND match_date < %s LIMIT 1",
            (r["id"], match_date),
        )
        if cur.fetchone():
            return {"id": r["id"], "season": r["season"], "season_state": r["season_state"]}
    return {"id": rows[0]["id"], "season": rows[0]["season"], "season_state": rows[0]["season_state"]}


def _matchday(cur, league_season_id: int, match_date) -> int | None:
    """League-wide round number for an unplayed fixture.

    `game_index` is unique per league season, so the next round after the last
    match played before the fixture is its matchday. A fixture in round 1 has
    no predecessor, which is the count of 0 plus 1.
    """
    cur.execute(
        """
        SELECT max(game_index) AS last_round
        FROM matches
        WHERE league_season_id = %s AND match_date < %s
        """,
        (league_season_id, match_date),
    )
    row = cur.fetchone()
    if row is None or row["last_round"] is None:
        return 1
    return int(row["last_round"]) + 1


def _standings_row(cur, league_season_id: int, team_id: int) -> dict | None:
    """A team's classic-table row, used as the pre-match table for a fixture."""
    cur.execute(
        """
        SELECT position, played, won, drawn, lost,
               goals_for, goals_against, goal_difference, points
        FROM standings
        WHERE league_season_id = %s AND team_id = %s AND view = 'classic'
        """,
        (league_season_id, team_id),
    )
    row = cur.fetchone()
    return dict(row) if row else None


def _feature_row(
    home: dict, away: dict, standings: dict, matchday: int | None, season: str | None
) -> dict:
    """Assemble a dataset-shaped row so build_pre_match can group it unchanged.

    The keys are the real ml.features.build_features column names, which is what
    lets the fixture detail page reuse the finished-match pre-match panel instead
    of growing a second, near-identical component. The naming is not uniform —
    form and load keep a `_team_` infix while rest and the table do not — so the
    mapping is written out rather than generated.

    The table columns are the current standings for the fixture's season. For a
    match that has not been played that snapshot genuinely is the state before
    it, which is why it is safe to present here and not a peek at the result.
    """
    row: dict = {"season": season, "game_index": matchday}
    for prefix, side in (("home", home), ("away", away)):
        suffix = side.get("venue_side") or prefix
        venue = side.get("venue") or {}
        table = (standings or {}).get(prefix) or {}
        # The panel's caption reads these back, so they travel with the numbers.
        row[f"{prefix}_team"] = side.get("name")
        row[f"{prefix}_team_id"] = side.get("team_id")
        points = side.get("points")
        row[f"{prefix}_team_points_last_5"] = points if points is not None else None
        wins = side.get("wins")
        row[f"{prefix}_team_wins_last_5"] = wins if wins is not None else None
        goals_scored = side.get("goals_scored")
        row[f"{prefix}_team_goals_scored_last_5"] = goals_scored if goals_scored is not None else None
        goals_conceded = side.get("goals_conceded")
        row[f"{prefix}_team_goals_conceded_last_5"] = goals_conceded if goals_conceded is not None else None
        row[f"{prefix}_team_{suffix}_win_rate"] = venue.get("win_rate")
        row[f"{prefix}_team_{suffix}_goals_avg"] = venue.get("goals_avg")
        row[f"{prefix}_team_{suffix}_conceded_avg"] = venue.get("conceded_avg")
        row[f"{prefix}_team_games_before"] = side.get("games_before")
        row[f"{prefix}_rest_days"] = side.get("rest_days")
        row[f"{prefix}_position_before_match"] = table.get("position")
        row[f"{prefix}_points_before_match"] = table.get("points")

    home_rest, away_rest = home.get("rest_days"), away.get("rest_days")
    row["rest_days_difference"] = (
        home_rest - away_rest if home_rest is not None and away_rest is not None else None
    )
    home_row = (standings or {}).get("home") or {}
    away_row = (standings or {}).get("away") or {}
    if home_row and away_row:
        row["position_difference"] = home_row["position"] - away_row["position"]
        row["points_difference"] = home_row["points"] - away_row["points"]
    return row


def _context(cur, league: str, home_name: str, away_name: str, match_date) -> dict:
    """Everything the database knows about an unplayed fixture.

    Returns a dict of independent sections; any of them may be empty when the
    league or the teams are not in the analytics database.
    """
    home_id = resolve_team_id(cur, home_name)
    away_id = resolve_team_id(cur, away_name)
    season = _season_for_date(cur, league, match_date)
    out: dict = {
        "season": season,
        "matchday": None,
        "home_team_id": home_id,
        "away_team_id": away_id,
        "pre_match": None,
        "head_to_head": None,
        "standings": {"home": None, "away": None},
    }
    if season is None:
        return out

    league_season_id = season["id"]
    out["matchday"] = _matchday(cur, league_season_id, match_date)
    out["standings"] = {
        "home": _standings_row(cur, league_season_id, home_id) if home_id else None,
        "away": _standings_row(cur, league_season_id, away_id) if away_id else None,
    }
    if home_id is None or away_id is None:
        return out

    home = _team_context(cur, league_season_id, home_id, "home", match_date, FORM_LIMIT)
    away = _team_context(cur, league_season_id, away_id, "away", match_date, FORM_LIMIT)
    home["name"], away["name"] = home_name, away_name
    out["home"] = home
    out["away"] = away
    out["pre_match"] = build_pre_match(
        _feature_row(home, away, out["standings"], out["matchday"], season["season"])
    )
    out["head_to_head"] = head_to_head(
        cur, home_id, away_id, match_date, limit=H2H_LIMIT
    )
    return out


@router.get("/fixtures")
def list_fixtures(
    league: str | None = None,
    sort: Literal["date", "confidence"] = "confidence",
    limit: int = DEFAULT_LIMIT,
    offset: int = 0,
    from_date: date | None = None,
    to_date: date | None = None,
    min_confidence: float | None = None,
) -> dict:
    """Merged upcoming fixtures, pruned, sorted by date or model confidence.

    Only fixtures that have not been played yet are listed. `first_date` reports
    the soonest one, so a client can tell an empty feed ("nothing left this
    week, re-run fetch_fixtures") from a genuinely broken one.

    Filters apply before paging and `total` counts what survived them, so a
    client can page through exactly what it asked for. `returned` is how many
    came back in this slice: with a limit in play that is smaller than `total`,
    and a UI rendering `total` as a count badge would otherwise claim to be
    showing rows it is not.

    `min_confidence` is the model's strongest side on a fixture, so raising it
    answers "where does the model actually have an opinion" rather than "where
    does it have any opinion at all" — most fixtures sit near 0.35 because
    neither side is favoured, and that is the honest reading, not a near-miss.
    """
    limit, offset = norm_pagination(limit, offset, MAX_LIMIT)
    if league is not None:
        require_league(league)
    rows = fixture_rows(league)

    start, end = _as_date(from_date), _as_date(to_date)
    check_date_window(start, end)
    if start or end:
        rows = [r for r in rows if _in_window(r, start, end)]

    if min_confidence is not None:
        rows = [
            r for r in rows
            if (r["predictions"].get("confidence") or 0.0) >= min_confidence
        ]

    # Date first whenever a date is in play: a paged list sorted by confidence
    # reshuffles between pages, so walking it can show a fixture twice and skip
    # another. Confidence stays the default for the plain view, which is a
    # short "best picks" read rather than a list to walk.
    effective_sort = sort
    if sort == "date" or start or end or min_confidence is not None:
        effective_sort = "date"
        rows.sort(key=lambda r: (r["match_date"] or "", r["time"] or ""))
    else:
        rows.sort(key=lambda r: r["predictions"]["confidence"], reverse=True)

    page = rows[offset:offset + limit]
    dated = sorted({r["match_date"] for r in rows if r.get("match_date")})
    # Counts for the whole filtered set, not the page, so a client grouping rows
    # by day can say "12 shown of 126" instead of implying a day is complete.
    day_counts: dict[str, int] = {}
    for r in rows:
        if r.get("match_date"):
            day_counts[r["match_date"]] = day_counts.get(r["match_date"], 0) + 1
    return {
        "count": len(page),
        "total": len(rows),
        "returned": len(page),
        "limit": limit,
        "offset": offset,
        "has_more": offset + len(page) < len(rows),
        # The order the rows are actually in, which is not always the order that
        # was asked for: a date window or confidence floor forces date order.
        "sort": effective_sort,
        "league": league,
        "league_name": common.league_name(league),
        "min_confidence": min_confidence,
        "from_date": from_date,
        "to_date": to_date,
        "first_date": dated[0] if dated else None,
        "last_date": dated[-1] if dated else None,
        "dates": dated,
        "day_counts": day_counts,
        "matches": page,
    }


@router.get("/fixtures/{league}")
def league_fixtures(league: str) -> dict:
    """Full stored fixtures payload for one league (raw model_predictions)."""
    require_league(league)
    path = league_fixture_file(league)
    if path is None:
        return {
            "league": league,
            "league_name": common.league_name(league),
            "count": 0,
            "matches": [],
            "attribution": "Data by football-charts.com",
        }
    payload = _load_payload(path)
    payload.setdefault("count", len(payload.get("matches") or []))
    payload.setdefault("league", league)
    payload["league_name"] = common.league_name(league)
    return payload


def _market_explanation(match: dict, market_key: str) -> dict | None:
    """The mechanism behind one derived market, or None when it has none.

    A market row is a single number; this is what produces it — how it settles
    across win/push/lose and which scorelines in the 81-cell grid pay it.
    Served per market rather than for all ~159 of them because the full
    explanation of every row would dwarf the fixture it belongs to.

    A key the fixture does not have is a 404, not a null: that means the caller
    asked for something that was never there. A null is reserved for a market
    that does exist but whose number the grid cannot rebuild.
    """
    preds = (match.get("model_predictions") or {}).get("dc_v2") or {}
    rows = {row.get("key"): row for row in markets_from_prediction(preds)["markets"]}
    row = rows.get(market_key)
    if row is None:
        raise HTTPException(status_code=404, detail=f"market '{market_key}' not found")
    return market_detail(preds.get("raw") or {}, row)


@router.get("/fixtures/{league}/{match_id:path}")
def fixture_detail(league: str, match_id: str, market: str | None = None) -> dict:
    """Everything known about one upcoming fixture, before it is played.

    Layered so the page degrades instead of erroring: the fixture row, the
    model's full prediction block and the collected /matches/{slug}/ payload come
    from files, and matchday, form, the pre-match table and head-to-head come
    from the analytics database. The database sections are only meaningful once
    the fixture is inside a collected season, which `season`/`matchday` report
    so a caller can tell derived data from assumed data.

    Passing `market=<key>` returns only the explanation for that one derived
    market, so a reader can drill into a chip without refetching the page.
    """
    require_league(league)
    fixture = find_fixture(league, match_id)
    if fixture is None:
        raise HTTPException(
            status_code=404, detail=f"fixture '{match_id}' not found for league '{league}'"
        )

    slug = fixture.get("slug") or ""

    if market is not None:
        # Before the collected payload is loaded: an explanation is a pure
        # function of the prediction block, so nothing else on the page is
        # needed and the file read would be wasted.
        return {
            "league": league,
            "league_name": common.league_name(league),
            "match_id": slug_tail(slug) or match_id,
            "slug": slug,
            "market_key": market,
            "market": _market_explanation(fixture, market),
        }

    detail = _load_detail(league, slug)
    # A collected payload is the richer copy of the same fixture: prefer it for
    # anything it carries and the fixtures file for anything it does not.
    merged = {**fixture, **detail} if detail else fixture
    match_date = merged.get("match_date")
    match_day = _as_date(match_date)

    context: dict = {}
    if match_day is not None:
        try:
            with fetched_cursor() as cur:
                context = _context(cur, league, merged.get("home_team"), merged.get("away_team"), match_day)
        except (Exception, SystemExit):  # noqa: BLE001
            # A fixture must still render when the analytics database is absent or
            # unreachable: every section derived from it is optional by design.
            # SystemExit is listed because db_common.get_conn() reports a
            # missing DATABASE_URL that way, which is a BaseException and would
            # otherwise escape the request.
            context = {}

    season = context.get("season") or {}
    for side, name in (("home", merged.get("home_team")), ("away", merged.get("away_team"))):
        side_data = context.get(side) or {}
        context[side] = {
            "name": name,
            "team_id": side_data.get("team_id"),
            "logo": merged.get(f"{side}_team_logo"),
            "form": side_data.get("form") or [],
            "form_line": side_data.get("form_line") or [],
            "rest_days": side_data.get("rest_days"),
            "games_before": side_data.get("games_before"),
            "venue": side_data.get("venue"),
        }
    context.pop("season", None)

    return {
        "league": league,
        "league_name": common.league_name(league),
        "match_id": slug_tail(slug) or match_id,
        "slug": slug,
        "country": merged.get("country"),
        # The upstream feed's own spelling, which for a dozen leagues differs
        # from the catalog name; league_name above is the canonical label.
        "real_league_name": merged.get("real_league_name"),
        "status": merged.get("status") or merged.get("match_status"),
        "match_date": match_date,
        # The season comes from the database when the fixture sits inside a
        # collected one, and from the collected detail payload otherwise.
        "season": season.get("season") or merged.get("season"),
        "season_state": season.get("season_state"),
        "matchday": context.get("matchday"),
        "teams": {"home": context["home"], "away": context["away"]},
        "standings": context.get("standings") or {"home": None, "away": None},
        "kickoff": {
            "time": merged.get("time"),
            "match_datetime": merged.get("match_datetime"),
            "label": merged.get("label"),
            "league_phase_status": merged.get("league_phase_status"),
            "portal_link": merged.get("portal_link"),
        },
        "predictability": predictability(fixture),
        "pre_match": context.get("pre_match"),
        "head_to_head": context.get("head_to_head"),
        "detail_collected": bool(detail),
    }
