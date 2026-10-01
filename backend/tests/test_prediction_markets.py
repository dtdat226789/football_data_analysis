"""Tests for the derived prediction markets (backend/apps/markets.py).

Three layers:

  * invariants  — every derived family must be internally consistent
                  (over+under=1, BTTS yes+no=1, handicap win+push+lose=1,
                  correct score sums to 1, 1X2 sums to 1). A derivation bug
                  shows up as a broken total before it shows up as a number
                  that looks plausible.
  * fidelity    — the reconstruction is only worth trusting because it
                  reproduces the probabilities dc_v2 already publishes. Checked
                  against every collected block, with a tolerance wide enough
                  to survive upstream changing slightly and tight enough to
                  catch a genuine modelling mistake.
  * selection   — the "flexible rate" behaviour that picks which markets
                  become chips.

Nothing here touches the API, the database or the network.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from apps.markets import (  # noqa: E402
    DEFAULT_RHO,
    FULL_TIME,
    FULL_TIME_LINES,
    HALF_TIME,
    HALF_TO_FULL,
    MARKET_CEILING,
    MARKET_LIMIT,
    MARKET_THRESHOLD,
    PROVENANCE_MODEL,
    PROVENANCE_MODELLED,
    _over_probabilities,
    fit_rho,
    fixture_markets,
    handicap_settlement,
    market_detail,
    markets_from_prediction,
    score_grid,
    select_markets,
)

ROOT = Path(__file__).resolve().parents[2]
FIXTURES_DIR = ROOT / "data" / "raw" / "fixtures"

# Rows are rounded to 4dp on the way out, so complements can disagree by up to
# one unit in the last place of each of the two rounded values.
TOL = 2e-4

LAM_HOME = 1.204
LAM_AWAY = 1.6137
LAM_HT = 0.9329

# A real dc_v2 `raw` block, copied from the eng1 fixtures dump, so the fidelity
# checks run against the numbers the feed actually publishes.
PUBLISHED = {
    "home": 0.2846, "away": 0.4687, "btts_yes": 0.561,
    "over_0.5": 0.9399, "over_1.5": 0.7723, "over_2.5": 0.5348,
    "over_3.5": 0.312, "over_4.5": 0.1551,
    "ht_over_0.5": 0.6079, "ht_over_1.5": 0.2383,
    "expected_ht_goals": 0.9329,
    "expected_away_goals": 1.6137, "expected_home_goals": 1.204,
}


def raw_block(**overrides) -> dict:
    """Lambdas only, with no published O/U lines.

    With nothing to fit against the correction falls back to the placeholder, so
    this is the deterministic form for structural tests. Fidelity tests use
    `published_block` instead.
    """
    block = {
        "expected_home_goals": LAM_HOME,
        "expected_away_goals": LAM_AWAY,
        "expected_ht_goals": LAM_HT,
    }
    block.update(overrides)
    return block


def published_block(**overrides) -> dict:
    """The real block, published lines and all, so the correction gets solved."""
    block = dict(PUBLISHED)
    block.update(overrides)
    return block


def by_key(markets: list[dict]) -> dict[str, dict]:
    return {market["key"]: market for market in markets}


def probability(markets: list[dict], key: str) -> float:
    return by_key(markets)[key]["probability"]


# --------------------------------------------------------------------------
# the grid
# --------------------------------------------------------------------------

def test_grid_is_a_distribution():
    grid = score_grid(LAM_HOME, LAM_AWAY)
    assert grid is not None
    assert math.isclose(sum(map(sum, grid)), 1.0, abs_tol=1e-12)
    assert all(value >= 0.0 for row in grid for value in row)


def test_grid_is_cached_on_rounded_parameters():
    assert score_grid(1.2040, 1.6137) is score_grid(1.204, 1.6137)
    assert score_grid(1.204, 1.6137) is not score_grid(1.9, 1.6137)


@pytest.mark.parametrize("lam", [None, 0, -1.0, "1.2", True, float("nan"), float("inf")])
def test_grid_refuses_unusable_lambdas(lam):
    """A missing or nonsensical lambda yields no grid, never a zero-filled one."""
    assert score_grid(lam, 1.5) is None
    assert score_grid(1.5, lam) is None


def test_extreme_rho_correction_does_not_produce_negative_cells():
    """A rho that would drive the 0-0 cell negative falls back to plain Poisson."""
    grid = score_grid(4.0, 4.0, rho=0.4)
    assert grid is not None
    assert all(value >= 0.0 for row in grid for value in row)
    assert math.isclose(sum(map(sum, grid)), 1.0, abs_tol=1e-12)


# --------------------------------------------------------------------------
# invariants
# --------------------------------------------------------------------------

def test_result_probabilities_sum_to_one():
    markets = fixture_markets(raw_block())
    result = by_key(markets)
    total = sum(result[f"ft.result.{side}"]["probability"] for side in ("home", "draw", "away"))
    assert math.isclose(total, 1.0, abs_tol=TOL)


def test_double_chance_is_the_sum_of_its_parts():
    markets = fixture_markets(raw_block())
    result = by_key(markets)
    home = result["ft.result.home"]["probability"]
    away = result["ft.result.away"]["probability"]
    draw = result["ft.result.draw"]["probability"]
    assert math.isclose(
        result["ft.double_chance.home_or_draw"]["probability"], home + draw, abs_tol=TOL
    )
    assert math.isclose(
        result["ft.double_chance.draw_or_away"]["probability"], draw + away, abs_tol=TOL
    )
    assert math.isclose(
        result["ft.double_chance.home_or_away"]["probability"], home + away, abs_tol=TOL
    )


@pytest.mark.parametrize("line", [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
def test_over_and_under_are_complementary(line):
    markets = fixture_markets(raw_block())
    result = by_key(markets)
    over = result[f"ft.totals.over_{line}"]["probability"]
    under = result[f"ft.totals.under_{line}"]["probability"]
    assert math.isclose(over + under, 1.0, abs_tol=TOL)
    assert 0.0 <= over <= 1.0


def test_btts_sides_are_complementary():
    markets = fixture_markets(raw_block())
    result = by_key(markets)
    assert math.isclose(
        result["ft.btts.yes"]["probability"] + result["ft.btts.no"]["probability"],
        1.0, abs_tol=TOL,
    )


def test_team_totals_complement_and_never_exceed_match_totals():
    markets = fixture_markets(raw_block())
    result = by_key(markets)
    for side in ("home", "away"):
        for line in (0.5, 1.5, 2.5, 3.5):
            over = result[f"ft.team_total.{side}.over_{line}"]["probability"]
            under = result[f"ft.team_total.{side}.under_{line}"]["probability"]
            assert math.isclose(over + under, 1.0, abs_tol=TOL)
    # A team cannot score more often than the match produces that many goals.
    assert result["ft.team_total.home.over_1.5"]["probability"] <= \
        result["ft.totals.over_1.5"]["probability"] + TOL


def test_correct_score_rows_sum_to_at_most_one():
    markets = fixture_markets(raw_block())
    total = sum(
        market["probability"] for market in markets if market["family"] == "correct_score"
    )
    assert 0.0 < total <= 1.0 + TOL
    # Ordered most likely first, and every row is a real scoreline.
    scores = [market["probability"] for market in markets if market["family"] == "correct_score"]
    assert scores == sorted(scores, reverse=True)
    for market in markets:
        if market["family"] == "correct_score":
            home, away = market["label"].split("-")
            assert home.isdigit() and away.isdigit()


def test_ht_ft_combinations_sum_to_one():
    """Nine combinations covering every outcome pair must total 1."""
    markets = fixture_markets(raw_block())
    total = sum(market["probability"] for market in markets if market["family"] == "ht_ft")
    assert math.isclose(total, 1.0, abs_tol=4 * TOL)
    assert len([market for market in markets if market["family"] == "ht_ft"]) == 9


def test_ht_ft_is_the_product_of_the_two_marginals():
    markets = fixture_markets(raw_block())
    result = by_key(markets)
    for ht_side in ("home", "draw", "away"):
        for ft_side in ("home", "draw", "away"):
            expected = (
                result[f"ht.result.{ht_side}"]["probability"]
                * result[f"ft.result.{ft_side}"]["probability"]
            )
            assert math.isclose(
                result[f"ht_ft.{ht_side}.{ft_side}"]["probability"], expected, abs_tol=4 * TOL
            )


# --------------------------------------------------------------------------
# Asian handicap settlement
# --------------------------------------------------------------------------

def test_half_goal_lines_never_push():
    grid = score_grid(LAM_HOME, LAM_AWAY)
    for line in (-1.5, -0.5, 0.5, 1.5):
        win, push, lose = handicap_settlement(grid, line)
        assert push == 0.0
        assert math.isclose(win + lose, 1.0, abs_tol=1e-12)


def test_whole_goal_line_pushes_exactly_on_the_draw_margin():
    """Home -1 must push on a one-goal margin and nothing else."""
    grid = score_grid(LAM_HOME, LAM_AWAY)
    win, push, lose = handicap_settlement(grid, -1.0)
    one_goal = math.fsum(grid[i][j] for i in range(len(grid)) for j in range(len(grid)) if i - j == 1)
    assert math.isclose(push, one_goal, abs_tol=1e-12)

    level = math.fsum(grid[i][j] for i in range(len(grid)) for j in range(len(grid)) if i == j)
    _, level_push, _ = handicap_settlement(grid, 0.0)
    assert math.isclose(level_push, level, abs_tol=1e-12)


def test_quarter_line_is_the_mean_of_its_two_half_stakes():
    """-0.25 is half of -0.5 and half of 0.0, so it pushes half the time 0.0 does."""
    grid = score_grid(LAM_HOME, LAM_AWAY)
    minus_half = handicap_settlement(grid, -0.5)
    level = handicap_settlement(grid, 0.0)
    quarter = handicap_settlement(grid, -0.25)

    for expected, actual in zip(
        [minus_half[0], level[0]], [quarter[0], quarter[0]]
    ):
        assert math.isclose(actual, expected, abs_tol=1e-12)

    assert math.isclose(quarter[1], 0.5 * level[1], abs_tol=1e-12)
    assert math.isclose(
        quarter[1], 0.5 * 0.0 + 0.5 * level[1], abs_tol=1e-12
    ), "the half-stake on -0.5 can never push"


def test_quarter_line_away_side_is_a_mirrored_decomposition():
    grid = score_grid(LAM_HOME, LAM_AWAY)
    assert math.isclose(
        handicap_settlement(grid, 0.25)[1],
        0.5 * handicap_settlement(grid, 0.0)[1] + 0.5 * handicap_settlement(grid, 0.5)[1],
        abs_tol=1e-12,
    )


@pytest.mark.parametrize("line", [-1.5, -1.25, -1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5])
def test_handicap_outcomes_always_total_one(line):
    grid = score_grid(LAM_HOME, LAM_AWAY)
    win, push, lose = handicap_settlement(grid, line)
    assert math.isclose(win + push + lose, 1.0, abs_tol=1e-12)
    assert win >= 0.0 and push >= 0.0 and lose >= 0.0


def test_handicap_zero_line_pushes_on_a_draw():
    grid = score_grid(LAM_HOME, LAM_AWAY)
    _, push, _ = handicap_settlement(grid, 0.0)
    assert push > 0.15, "a bivariate Poisson on these lambdas draws about a quarter of matches"


def test_handicap_rows_carry_push_and_complement_across_sides():
    markets = fixture_markets(raw_block())
    result = by_key(markets)
    for line in (-1.0, -0.5, 0.0, 0.5, 1.0):
        home = result[f"ft.asian_handicap.{line}_home"]
        away = result[f"ft.asian_handicap.{line}_away"]
        assert "push" in home
        assert math.isclose(
            home["probability"] + home["push"] + away["probability"], 1.0, abs_tol=2 * TOL
        )
        # The two sides are quoted on opposite lines, as a bettor would write them.
        assert home["label"] == f"Home {line:+g}"
        assert away["label"] == f"Away {-line:+g}"


# --------------------------------------------------------------------------
# fidelity against what dc_v2 already publishes
# --------------------------------------------------------------------------

def test_reconstruction_reproduces_published_probabilities():
    """The whole justification for deriving markets: it agrees with the feed.

    Solving the draw correction from the published O/U lines brings the
    reconstruction onto the feed's own numbers, so the markets dc_v2 never
    published are consistent with the ones it did. If dc_v2 ever changes its
    goal model this fails, which is the point.
    """
    markets = by_key(fixture_markets(published_block()))
    for derived_key, published_key in (
        ("ft.result.home", "home"),
        ("ft.result.away", "away"),
        ("ft.btts.yes", "btts_yes"),
        ("ft.totals.over_1.5", "over_1.5"),
        ("ft.totals.over_2.5", "over_2.5"),
        ("ft.totals.over_3.5", "over_3.5"),
        ("ht.totals.over_0.5", "ht_over_0.5"),
        ("ht.totals.over_1.5", "ht_over_1.5"),
    ):
        derived = markets[derived_key]["probability"]
        expected = PUBLISHED[published_key]
        assert abs(derived - expected) <= 0.001, f"{derived_key}: {derived} vs {expected}"


def test_draw_is_the_remainder_of_the_published_home_and_away():
    markets = by_key(fixture_markets(published_block()))
    remainder = 1 - PUBLISHED["home"] - PUBLISHED["away"]
    assert math.isclose(markets["ft.result.draw"]["probability"], remainder, abs_tol=0.001)


def test_solving_the_correction_beats_the_published_placeholder():
    """Why `fit_rho` exists: the published `xi` is a placeholder, not the model."""
    block = published_block()
    solved = fit_rho(block, LAM_HOME, LAM_AWAY)
    placeholder = score_grid(LAM_HOME, LAM_AWAY, DEFAULT_RHO)

    def worst_on_published_lines(grid) -> float:
        over = _over_probabilities(grid, FULL_TIME_LINES)
        return max(
            abs(over[index] - PUBLISHED[f"over_{line:g}"])
            for index, line in enumerate(FULL_TIME_LINES)
        )

    assert worst_on_published_lines(score_grid(LAM_HOME, LAM_AWAY, solved)) < \
        worst_on_published_lines(placeholder)


def test_placeholder_is_used_when_too_few_lines_to_identify_the_correction():
    assert fit_rho(raw_block(), LAM_HOME, LAM_AWAY) == DEFAULT_RHO
    assert fit_rho({"over_0.5": 0.9}, LAM_HOME, LAM_AWAY) == DEFAULT_RHO
    assert fit_rho(published_block(), None, LAM_AWAY) == DEFAULT_RHO
    assert fit_rho(published_block(), 0.0, LAM_AWAY) == DEFAULT_RHO


def test_the_published_xi_is_never_used_as_a_correction():
    """Every collected block publishes xi=0.0019, so passing it through would
    silently make the same wrong assumption everywhere. The correction is solved
    for from the O/U lines instead."""
    solved = fit_rho(published_block(), LAM_HOME, LAM_AWAY)
    assert solved != DEFAULT_RHO


def test_fit_rho_keeps_every_corrected_cell_positive():
    """The search must not land somewhere the model is undefined."""
    for lam_h, lam_a in ((0.4, 0.5), (1.0, 1.04), (4.07, 2.68), (3.0, 3.0)):
        block = published_block(expected_home_goals=lam_h, expected_away_goals=lam_a)
        grid = score_grid(lam_h, lam_a, fit_rho(block, lam_h, lam_a))
        assert grid
        assert all(value >= 0.0 for row in grid for value in row)
        assert math.isclose(sum(map(sum, grid)), 1.0, abs_tol=1e-12)


def test_fidelity_holds_across_every_collected_block():
    """Run the same check over the real dump, not just one fixture.

    Asserted as a distribution rather than a single worst case, because the
    dump is re-fetched and its shape changes. Mean and p99 are held tight, so
    systematic drift fails immediately; a small share of individual checks is
    allowed above 0.75pp because a handful of upstream blocks publish O/U lines
    that their own expected goals cannot produce.

    Two blocks in the current dump are like that, and no model can fix them:
    wfrance1 "Lyon W vs Toulouse W" and wsweden "Hacken W vs Uppsala W", both
    publishing expected home goals of 6.8 and 6.0. Their O/U lines imply a
    total-goals mean of 7.13 and 6.35 while the published lambdas sum to 7.29
    and 6.44, so the lines are not jointly satisfiable by any Poisson -- let
    alone a Poisson plus one Dixon-Coles parameter. Both are far past 0.75pp on
    the upper totals lines and are the entire tail of the distribution.
    """
    if not FIXTURES_DIR.is_dir():
        pytest.skip("no collected fixtures on this machine")

    errors: list[float] = []
    for path in sorted(FIXTURES_DIR.glob("*.json")):
        if path.name == "manifest.json":
            continue
        try:
            payload = json.loads(path.read_bytes())
        except (OSError, ValueError):
            continue
        for match in payload.get("matches") or []:
            published = ((match.get("model_predictions") or {}).get("dc_v2") or {}).get("raw") or {}
            if not published:
                continue
            markets = by_key(fixture_markets(published))
            if not markets:
                continue
            for derived_key, published_key in (
                ("ft.result.home", "home"),
                ("ft.result.away", "away"),
                ("ft.btts.yes", "btts_yes"),
                ("ft.totals.over_1.5", "over_1.5"),
                ("ft.totals.over_2.5", "over_2.5"),
                ("ft.totals.over_3.5", "over_3.5"),
            ):
                if not isinstance(published.get(published_key), (int, float)):
                    continue
                errors.append(abs(markets[derived_key]["probability"] - published[published_key]))

    assert errors, "no dc_v2 blocks found to check fidelity against"
    errors.sort()
    checked = len(errors)
    mean = sum(errors) / checked
    p99 = errors[int(checked * 0.99)]
    outliers = sum(1 for e in errors if e > 0.0075)

    assert mean <= 0.001, f"mean reconstruction error {mean:.5f} exceeds 0.001 over {checked} checks"
    assert p99 <= 0.005, f"p99 reconstruction error {p99:.5f} exceeds 0.005 over {checked} checks"
    assert outliers / checked <= 0.01, (
        f"{outliers} of {checked} checks exceed 0.0075 "
        f"({100 * outliers / checked:.2f}%, worst {errors[-1]:.4f}); more than 1% means the "
        f"correction has stopped tracking the published lines"
    )


def test_derived_rows_are_cached_but_handed_out_as_copies():
    """The list feed re-derives the same fixtures every request, so the result is
    cached; callers still get their own dicts and cannot poison the cache."""
    first = fixture_markets(published_block())
    second = fixture_markets(published_block())
    assert first == second
    assert first[0] is not second[0]
    first[0]["probability"] = 0.1234
    assert fixture_markets(published_block())[0]["probability"] != 0.1234


# --------------------------------------------------------------------------
# provenance
# --------------------------------------------------------------------------

def test_full_time_markets_are_model_and_half_time_are_modelled():
    markets = fixture_markets(raw_block())
    for market in markets:
        if market["scope"] == FULL_TIME:
            assert market["provenance"] == PROVENANCE_MODEL, market["key"]
        else:
            assert market["provenance"] == PROVENANCE_MODELLED, market["key"]


def test_half_time_markets_are_dropped_when_no_ht_lambda_is_published():
    """No assumption available means no half-time rows, not invented ones."""
    markets = fixture_markets(raw_block(expected_ht_goals=None))
    assert markets, "full-time markets should still be produced"
    assert all(market["scope"] == FULL_TIME for market in markets)
    assert not [market for market in markets if market["family"] == "ht_ft"]


def test_ht_markets_need_both_lambdas():
    markets = fixture_markets(raw_block(expected_away_goals=None))
    assert markets == []


# --------------------------------------------------------------------------
# chip selection — the "flexible rate" behaviour
# --------------------------------------------------------------------------

def selected_for(**overrides) -> list[dict]:
    return select_markets(fixture_markets(raw_block(**overrides)))


def test_selection_respects_threshold_ceiling_and_cap():
    selected = selected_for()
    assert len(selected) <= MARKET_LIMIT
    for market in selected:
        assert MARKET_THRESHOLD <= market["probability"] <= MARKET_CEILING


def test_selection_excludes_near_certain_and_coin_flip_markets():
    """A chip must be decisive but still in play.

    Long shots are decisive and useless (half-time under 6.5 is ~99.99% on most
    fixtures); anything near even is not a view at all.
    """
    selected = selected_for()
    for market in selected:
        assert market["probability"] < 0.999
        assert abs(market["probability"] - 0.5) > 0.05


def test_selection_only_uses_mainstream_markets():
    """No long lines, no team totals, no correct score in a one-line summary."""
    for market in selected_for():
        assert market["promotable"] is True
        if market["family"] == "totals":
            assert market["line"] in (1.5, 2.5, 3.5)
        if market["family"] == "asian_handicap":
            assert market["line"] in (-1.0, -0.5, 0.0, 0.5, 1.0)
        assert market["family"] not in ("team_total", "correct_score")


def test_measured_markets_outrank_assumed_ones():
    """Provenance is ranked ahead of decisiveness, so a 94% assumption never
    displaces a 61% measurement."""
    for block in (raw_block(), published_block()):
        selected = select_markets(fixture_markets(block))
        seen_modelled = False
        for market in selected:
            if market["provenance"] == PROVENANCE_MODELLED:
                seen_modelled = True
            else:
                assert not seen_modelled, "a model row appeared after a modelled row"


def test_modelled_chips_only_appear_once_measured_markets_run_out():
    """Half-time rows may fill leftover slots, but never displace a full-time one."""
    high = published_block(
        expected_home_goals=1.9, expected_away_goals=0.4, expected_ht_goals=1.1,
    )
    selected = select_markets(fixture_markets(high))
    assert selected
    full_time_count = sum(1 for market in selected if market["scope"] == FULL_TIME)
    assert full_time_count == len(selected) or full_time_count >= MARKET_LIMIT - 2


def test_selection_collapses_markets_rounding_to_the_same_percentage():
    """AH -0.5 and AH -1 are near-identical bets at this scale; one slot only."""
    selected = selected_for()
    seen = set()
    for market in selected:
        identity = (market["family"], market["scope"], round(market["probability"] * 100))
        assert identity not in seen, f"{market['label']} duplicates an earlier chip"
        seen.add(identity)


def test_selection_is_deterministic():
    markets = fixture_markets(raw_block())
    first = [market["key"] for market in select_markets(markets)]
    second = [market["key"] for market in select_markets(list(reversed(markets)))]
    assert first == second


def test_selection_tolerates_missing_and_malformed_rows():
    assert select_markets([]) == []
    assert select_markets(None) == []
    assert select_markets([{"label": "x", "probability": None}]) == []
    assert select_markets([{"label": "x", "probability": "0.9"}]) == []
    assert select_markets([{"label": "x", "probability": 0.9, "promotable": False}]) == []
    assert select_markets("not a list") == []


def test_selection_respects_a_custom_threshold_and_limit():
    markets = fixture_markets(raw_block())
    assert len(select_markets(markets, limit=2)) == 2
    assert len(select_markets(markets, limit=0)) == 0
    loose = select_markets(markets, threshold=0.0, ceiling=1.0, limit=3)
    assert len(loose) == 3
    for market in select_markets(markets, threshold=0.9):
        assert market["probability"] >= 0.9


def test_a_ceiling_below_the_threshold_is_raised_to_it():
    """Misconfiguration must not silently return nothing."""
    markets = fixture_markets(raw_block())
    assert select_markets(markets, threshold=0.9, ceiling=0.1) == \
        select_markets(markets, threshold=0.9, ceiling=0.9)


def test_btts_yes_becomes_a_chip_when_the_model_expects_goals():
    """The behaviour the feature was asked for: a decisive O/U line surfaces."""
    high_scoring = fixture_markets(raw_block(
        expected_home_goals=2.4, expected_away_goals=2.1, expected_ht_goals=1.6,
    ))
    selected = select_markets(high_scoring)
    labels = {market["label"] for market in selected}
    assert "O1.5" in labels
    assert all(market["scope"] == FULL_TIME for market in selected)


def test_low_scoring_fixture_promotes_under_lines():
    markets = fixture_markets(raw_block(
        expected_home_goals=0.7, expected_away_goals=0.8, expected_ht_goals=0.5,
    ))
    labels = {market["label"] for market in select_markets(markets)}
    assert "U2.5" in labels or "U1.5" in labels


# --------------------------------------------------------------------------
# the served shape
# --------------------------------------------------------------------------

def test_markets_from_prediction_returns_markets_and_selection():
    out = markets_from_prediction({"raw": raw_block(), "xi": DEFAULT_RHO})
    assert set(out) == {"markets", "selected"}
    assert out["markets"] and out["selected"]
    assert len(out["selected"]) <= MARKET_LIMIT


def test_markets_from_prediction_ignores_the_placeholder_xi():
    """Every block publishes xi=0.0019, so honouring it would make the same
    wrong assumption everywhere. The correction is solved for instead, which is
    why the served markets are closer to the feed than that placeholder gives."""
    served = markets_from_prediction({"raw": published_block(), "xi": DEFAULT_RHO})
    assert served == markets_from_prediction({"raw": published_block()})

    placeholder = {
        market["key"]: market["probability"]
        for market in fixture_markets(published_block(), rho=DEFAULT_RHO)
    }
    actual = {market["key"]: market["probability"] for market in served["markets"]}
    assert abs(actual["ft.result.home"] - PUBLISHED["home"]) < \
        abs(placeholder["ft.result.home"] - PUBLISHED["home"])


def test_markets_from_prediction_on_a_block_without_lambdas():
    out = markets_from_prediction({"raw": {"home": 0.3, "away": 0.4}})
    assert out == {"markets": [], "selected": []}


@pytest.mark.parametrize("preds", [None, {}, "nope", {"raw": None}, {"raw": "nope"}])
def test_markets_from_prediction_tolerates_junk(preds):
    assert markets_from_prediction(preds) == {"markets": [], "selected": []}


def test_no_prediction_is_invented_for_a_missing_prediction_block():
    assert markets_from_prediction({}) == {"markets": [], "selected": []}
    assert fixture_markets({}) == []
    assert fixture_markets(None) == []


def test_every_served_row_has_the_shape_the_table_relies_on():
    required = {"key", "family", "label", "scope", "line", "selection", "probability", "provenance", "promotable"}
    for market in fixture_markets(raw_block()):
        assert required <= set(market)
        assert market["scope"] in (FULL_TIME, HALF_TIME, HALF_TO_FULL)
        assert market["provenance"] in (PROVENANCE_MODEL, PROVENANCE_MODELLED)
        assert 0.0 <= market["probability"] <= 1.0
        assert market["key"].count(".") >= 1
    keys = [market["key"] for market in fixture_markets(raw_block())]
    assert len(keys) == len(set(keys)), "market keys must be unique"


# ---------------------------------------------------------------------------
# market_detail — the explanation behind one derived market
# ---------------------------------------------------------------------------


def explain(raw: dict, key: str) -> dict | None:
    """The explanation the API serves for `key` on a fixture built from `raw`."""
    rows = by_key(fixture_markets(raw))
    assert key in rows, key
    return market_detail(raw, rows[key])


def test_every_derived_market_has_an_explanation():
    """No market may be listed without a mechanism behind it."""
    for row in fixture_markets(published_block()):
        detail = market_detail(published_block(), row)
        assert detail is not None, row["key"]


def test_explanation_reproduces_the_row_it_explains():
    """The number in the table and the number in the modal must not disagree."""
    for row in fixture_markets(published_block()):
        detail = market_detail(published_block(), row)
        if detail is None or detail.get("factors"):
            continue
        assert detail["settlement"]["win"] == pytest.approx(row["probability"], abs=TOL)
        if isinstance(row.get("push"), (int, float)) and row["push"] > 0:
            assert detail["settlement"]["push"] == pytest.approx(row["push"], abs=TOL)


def test_a_result_market_lists_exactly_the_scorelines_on_its_side():
    detail = explain(published_block(), "ft.result.home")
    for cell in detail["cells"]:
        assert cell["home_goals"] > cell["away_goals"]
    assert detail["paying_cells"] == len(detail["cells"])
    assert detail["settlement"]["push"] == 0.0
    # A result cannot refund, so every listed cell is a clean win.
    assert {cell["outcome"] for cell in detail["cells"]} == {"win"}


def test_a_correct_score_market_names_exactly_one_scoreline():
    detail = explain(published_block(), "ft.correct_score.2-1")
    assert len(detail["cells"]) == 1
    assert detail["cells"][0]["score"] == "2-1"
    assert detail["paying_cells"] == 1


def test_a_totals_market_only_lists_scorelines_over_the_line():
    detail = explain(published_block(), "ft.totals.over_2.5")
    for cell in detail["cells"]:
        assert cell["home_goals"] + cell["away_goals"] > 2.5


def test_cells_are_ordered_by_how_likely_they_are():
    detail = explain(published_block(), "ft.totals.over_2.5")
    probabilities = [cell["probability"] for cell in detail["cells"]]
    assert probabilities == sorted(probabilities, reverse=True)


def test_shares_are_a_split_of_each_paying_outcome():
    """A share is a share of something, so each outcome's shares must add up."""
    detail = explain(published_block(), "ft.asian_handicap.-1.0_home")
    for outcome in ("win", "push"):
        total = sum(
            cell["share"]
            for cell in detail["cells"]
            if outcome in cell["outcome"].split("+")
        )
        assert total == pytest.approx(1.0, abs=0.01), outcome


def test_a_quarter_line_splits_a_draw_between_push_and_lose():
    detail = explain(published_block(), "ft.asian_handicap.-0.25_home")
    draws = [c for c in detail["cells"] if c["home_goals"] == c["away_goals"]]
    assert draws
    # Half the stake is refunded and half is lost, so neither side is a clean win.
    assert {c["outcome"] for c in draws} == {"push+lose"}


def test_the_away_side_of_a_handicap_is_the_mirror_of_the_home_side():
    home = explain(published_block(), "ft.asian_handicap.-0.5_home")
    away = explain(published_block(), "ft.asian_handicap.-0.5_away")
    assert home["settlement"]["lose"] == pytest.approx(away["settlement"]["win"], abs=TOL)
    assert home["settlement"]["win"] == pytest.approx(away["settlement"]["lose"], abs=TOL)
    # Home -0.5 can never refund, so both sides settle on the same scorelines.
    assert home["paying_cells"] + away["paying_cells"] == home["grid_cells"]


def test_a_whole_handicap_line_pushes_on_the_exact_scoreline():
    detail = explain(published_block(), "ft.asian_handicap.-1.0_home")
    pushes = [c for c in detail["cells"] if c["outcome"] == "push"]
    # Handing over exactly one goal: the one-goal scorelines refund and nothing
    # else does, because every other margin settles cleanly.
    assert pushes
    assert {c["home_goals"] - c["away_goals"] for c in pushes} == {1}
    assert detail["settlement"]["push"] > 0
    # The push is every one-goal result, and those are the only pushed cells.
    one_goal = {c["score"] for c in detail["cells"] if c["home_goals"] - c["away_goals"] == 1}
    assert {c["score"] for c in pushes} == one_goal


def test_half_time_full_time_explains_itself_with_factors_not_scorelines():
    detail = explain(published_block(), "ht_ft.home.home")
    assert detail["cells"] == []
    assert detail["paying_cells"] == 0
    assert detail["factors"]["half_time_side"] == "home"
    assert detail["factors"]["full_time_side"] == "home"
    # Quoted at the win probability, which is the product of the two splits.
    expected = (
        detail["factors"]["half_time"]["home"] * detail["factors"]["full_time"]["home"]
    )
    assert detail["settlement"]["win"] == pytest.approx(expected, abs=TOL)


def test_an_unexplainable_row_returns_none_rather_than_guessing():
    """A row the grid cannot rebuild must be refused, not approximated."""
    assert market_detail(published_block(), {"family": "made_up", "scope": FULL_TIME}) is None
    assert market_detail(published_block(), {"family": "totals", "scope": FULL_TIME, "line": "nonsense"}) is None


def test_no_explanation_without_usable_lambdas():
    """The same rule as the menu: a block with no goals serves no markets."""
    raw = published_block()
    for key in ("expected_home_goals", "expected_away_goals"):
        raw.pop(key)
    assert market_detail(raw, {"family": "result", "scope": FULL_TIME, "selection": "home"}) is None
