"""Tests for the derived outcome projections (backend/apps/projections.py).

Three layers:

  * invariants  — every derived family must be internally consistent
                  (over/under=1, both teams score yes+no=1, margin win+refund+lose=1,
                  exact score sums to 1, match outcome sums to 1). A derivation bug
                  shows up as a broken total before it shows up as a number
                  that looks plausible.
  * fidelity    — the reconstruction is only worth trusting because it
                  reproduces the probabilities dc_v2 already publishes. Checked
                  against every collected block, with a tolerance wide enough
                  to survive upstream changing slightly and tight enough to
                  catch a genuine modelling mishare.
  * selection   — the "selection" behaviour that picks which projections
                  become highlights.

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

from apps.projections import (  # noqa: E402
    DEFAULT_RHO,
    FULL_TIME,
    FULL_TIME_GOAL_LINES,
    HALF_TIME,
    HALF_TO_FULL,
    HIGHLIGHT_CEILING,
    HIGHLIGHT_LIMIT,
    HIGHLIGHT_THRESHOLD,
    PROVENANCE_EXACT,
    PROVENANCE_ESTIMATED,
    _over_probabilities,
    fit_rho,
    fixture_projections,
    margin_outcomes,
    projection_detail,
    projections_from_prediction,
    score_grid,
    select_highlights,
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
    "home": 0.2846, "away": 0.4687, "both_score_yes": 0.561,
    "over_0.5": 0.9399, "over_1.5": 0.7723, "over_2.5": 0.5348,
    "over_3.5": 0.312, "over_4.5": 0.1551,
    "ht_over_0.5": 0.6079, "ht_over_1.5": 0.2383,
    "expected_ht_goals": 0.9329,
    "expected_away_goals": 1.6137, "expected_home_goals": 1.204,
}


def raw_block(**overrides) -> dict:
    """Lambdas only, with no published goal-total lines.

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


def by_key(projections: list[dict]) -> dict[str, dict]:
    return {projection["key"]: projection for projection in projections}


def probability(projections: list[dict], key: str) -> float:
    return by_key(projections)[key]["probability"]


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
    projections = fixture_projections(raw_block())
    result = by_key(projections)
    total = sum(result[f"ft.outcome.{side}"]["probability"] for side in ("home", "draw", "away"))
    assert math.isclose(total, 1.0, abs_tol=TOL)


def test_paired_outcome_is_the_sum_of_its_parts():
    projections = fixture_projections(raw_block())
    result = by_key(projections)
    home = result["ft.outcome.home"]["probability"]
    away = result["ft.outcome.away"]["probability"]
    draw = result["ft.outcome.draw"]["probability"]
    assert math.isclose(
        result["ft.paired_outcome.home_or_draw"]["probability"], home + draw, abs_tol=TOL
    )
    assert math.isclose(
        result["ft.paired_outcome.draw_or_away"]["probability"], draw + away, abs_tol=TOL
    )
    assert math.isclose(
        result["ft.paired_outcome.home_or_away"]["probability"], home + away, abs_tol=TOL
    )


@pytest.mark.parametrize("line", [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
def test_over_and_under_are_complementary(line):
    projections = fixture_projections(raw_block())
    result = by_key(projections)
    over = result[f"ft.goal_totals.over_{line}"]["probability"]
    under = result[f"ft.goal_totals.under_{line}"]["probability"]
    assert math.isclose(over + under, 1.0, abs_tol=TOL)
    assert 0.0 <= over <= 1.0


def test_both_score_sides_are_complementary():
    projections = fixture_projections(raw_block())
    result = by_key(projections)
    assert math.isclose(
        result["ft.both_score.yes"]["probability"] + result["ft.both_score.no"]["probability"],
        1.0, abs_tol=TOL,
    )


def test_team_totals_complement_and_never_exceed_match_totals():
    projections = fixture_projections(raw_block())
    result = by_key(projections)
    for side in ("home", "away"):
        for line in (0.5, 1.5, 2.5, 3.5):
            over = result[f"ft.team_total.{side}.over_{line}"]["probability"]
            under = result[f"ft.team_total.{side}.under_{line}"]["probability"]
            assert math.isclose(over + under, 1.0, abs_tol=TOL)
    # A team cannot score more often than the match produces that many goals.
    assert result["ft.team_total.home.over_1.5"]["probability"] <= \
        result["ft.goal_totals.over_1.5"]["probability"] + TOL


def test_exact_score_rows_sum_to_at_most_one():
    projections = fixture_projections(raw_block())
    total = sum(
        projection["probability"] for projection in projections if projection["family"] == "exact_score"
    )
    assert 0.0 < total <= 1.0 + TOL
    # Ordered most likely first, and every row is a real scoreline.
    scores = [projection["probability"] for projection in projections if projection["family"] == "exact_score"]
    assert scores == sorted(scores, reverse=True)
    for projection in projections:
        if projection["family"] == "exact_score":
            home, away = projection["label"].split("-")
            assert home.isdigit() and away.isdigit()


def test_half_full_combinations_sum_to_one():
    """Nine combinations covering every outcome pair must total 1."""
    projections = fixture_projections(raw_block())
    total = sum(projection["probability"] for projection in projections if projection["family"] == "half_full")
    assert math.isclose(total, 1.0, abs_tol=4 * TOL)
    assert len([projection for projection in projections if projection["family"] == "half_full"]) == 9


def test_half_full_is_the_product_of_the_two_marginals():
    projections = fixture_projections(raw_block())
    result = by_key(projections)
    for ht_side in ("home", "draw", "away"):
        for ft_side in ("home", "draw", "away"):
            expected = (
                result[f"ht.outcome.{ht_side}"]["probability"]
                * result[f"ft.outcome.{ft_side}"]["probability"]
            )
            assert math.isclose(
                result[f"half_full.{ht_side}.{ft_side}"]["probability"], expected, abs_tol=4 * TOL
            )


# --------------------------------------------------------------------------
# Asian margin outcomes
# --------------------------------------------------------------------------

def test_half_goal_lines_never_refund():
    grid = score_grid(LAM_HOME, LAM_AWAY)
    for line in (-1.5, -0.5, 0.5, 1.5):
        win, refund, lose = margin_outcomes(grid, line)
        assert refund == 0.0
        assert math.isclose(win + lose, 1.0, abs_tol=1e-12)


def test_whole_goal_line_refunds_exactly_on_the_draw_margin():
    """Home -1 must refund on a one-goal margin and nothing else."""
    grid = score_grid(LAM_HOME, LAM_AWAY)
    win, refund, lose = margin_outcomes(grid, -1.0)
    one_goal = math.fsum(grid[i][j] for i in range(len(grid)) for j in range(len(grid)) if i - j == 1)
    assert math.isclose(refund, one_goal, abs_tol=1e-12)

    level = math.fsum(grid[i][j] for i in range(len(grid)) for j in range(len(grid)) if i == j)
    _, level_refund, _ = margin_outcomes(grid, 0.0)
    assert math.isclose(level_refund, level, abs_tol=1e-12)


def test_quarter_line_is_the_mean_of_its_two_half_shares():
    """-0.25 is half of -0.5 and half of 0.0, so it refunds half the time 0.0 does."""
    grid = score_grid(LAM_HOME, LAM_AWAY)
    minus_half = margin_outcomes(grid, -0.5)
    level = margin_outcomes(grid, 0.0)
    quarter = margin_outcomes(grid, -0.25)

    for expected, actual in zip(
        [minus_half[0], level[0]], [quarter[0], quarter[0]]
    ):
        assert math.isclose(actual, expected, abs_tol=1e-12)

    assert math.isclose(quarter[1], 0.5 * level[1], abs_tol=1e-12)
    assert math.isclose(
        quarter[1], 0.5 * 0.0 + 0.5 * level[1], abs_tol=1e-12
    ), "the half-share on -0.5 can never refund"


def test_quarter_line_away_side_is_a_mirrored_decomposition():
    grid = score_grid(LAM_HOME, LAM_AWAY)
    assert math.isclose(
        margin_outcomes(grid, 0.25)[1],
        0.5 * margin_outcomes(grid, 0.0)[1] + 0.5 * margin_outcomes(grid, 0.5)[1],
        abs_tol=1e-12,
    )


@pytest.mark.parametrize("line", [-1.5, -1.25, -1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5])
def test_margin_outcomes_always_total_one(line):
    grid = score_grid(LAM_HOME, LAM_AWAY)
    win, refund, lose = margin_outcomes(grid, line)
    assert math.isclose(win + refund + lose, 1.0, abs_tol=1e-12)
    assert win >= 0.0 and refund >= 0.0 and lose >= 0.0


def test_margin_zero_line_refunds_on_a_draw():
    grid = score_grid(LAM_HOME, LAM_AWAY)
    _, refund, _ = margin_outcomes(grid, 0.0)
    assert refund > 0.15, "a bivariate Poisson on these lambdas draws about a quarter of matches"


def test_margin_rows_carry_refund_and_complement_across_sides():
    projections = fixture_projections(raw_block())
    result = by_key(projections)
    for line in (-1.0, -0.5, 0.0, 0.5, 1.0):
        home = result[f"ft.goal_margin.{line}_home"]
        away = result[f"ft.goal_margin.{line}_away"]
        assert "refund" in home
        assert math.isclose(
            home["probability"] + home["refund"] + away["probability"], 1.0, abs_tol=2 * TOL
        )
        # Both sides are named in plain language rather than by a signed line.
        assert home["label"].startswith("Home ")
        assert away["label"].startswith("Away ")
        assert "Home -" not in home["label"]
        assert "Home +" not in home["label"]


# --------------------------------------------------------------------------
# fidelity against what dc_v2 already publishes
# --------------------------------------------------------------------------

def test_reconstruction_reproduces_published_probabilities():
    """The whole justification for deriving projections: it agrees with the feed.

    Solving the draw correction from the published goal-total lines brings the
    reconstruction onto the feed's own numbers, so the projections dc_v2 never
    published are consistent with the ones it did. If dc_v2 ever changes its
    goal model this fails, which is the point.
    """
    projections = by_key(fixture_projections(published_block()))
    for derived_key, published_key in (
        ("ft.outcome.home", "home"),
        ("ft.outcome.away", "away"),
        ("ft.both_score.yes", "both_score_yes"),
        ("ft.goal_totals.over_1.5", "over_1.5"),
        ("ft.goal_totals.over_2.5", "over_2.5"),
        ("ft.goal_totals.over_3.5", "over_3.5"),
        ("ht.goal_totals.over_0.5", "ht_over_0.5"),
        ("ht.goal_totals.over_1.5", "ht_over_1.5"),
    ):
        derived = projections[derived_key]["probability"]
        expected = PUBLISHED[published_key]
        assert abs(derived - expected) <= 0.001, f"{derived_key}: {derived} vs {expected}"


def test_draw_is_the_remainder_of_the_published_home_and_away():
    projections = by_key(fixture_projections(published_block()))
    remainder = 1 - PUBLISHED["home"] - PUBLISHED["away"]
    assert math.isclose(projections["ft.outcome.draw"]["probability"], remainder, abs_tol=0.001)


def test_solving_the_correction_beats_the_published_placeholder():
    """Why `fit_rho` exists: the published `xi` is a placeholder, not the model."""
    block = published_block()
    solved = fit_rho(block, LAM_HOME, LAM_AWAY)
    placeholder = score_grid(LAM_HOME, LAM_AWAY, DEFAULT_RHO)

    def worst_on_published_lines(grid) -> float:
        over = _over_probabilities(grid, FULL_TIME_GOAL_LINES)
        return max(
            abs(over[index] - PUBLISHED[f"over_{line:g}"])
            for index, line in enumerate(FULL_TIME_GOAL_LINES)
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
    for from the goal-total lines instead."""
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
    allowed above 0.75pp because a handful of upstream blocks publish goal-total lines
    that their own expected goals cannot produce.

    Two blocks in the current dump are like that, and no model can fix them:
    wfrance1 "Lyon W vs Toulouse W" and wsweden "Hacken W vs Uppsala W", both
    publishing expected home goals of 6.8 and 6.0. Their goal-total lines imply a
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
            projections = by_key(fixture_projections(published))
            if not projections:
                continue
            for derived_key, published_key in (
                ("ft.outcome.home", "home"),
                ("ft.outcome.away", "away"),
                ("ft.both_score.yes", "both_score_yes"),
                ("ft.goal_totals.over_1.5", "over_1.5"),
                ("ft.goal_totals.over_2.5", "over_2.5"),
                ("ft.goal_totals.over_3.5", "over_3.5"),
            ):
                if not isinstance(published.get(published_key), (int, float)):
                    continue
                errors.append(abs(projections[derived_key]["probability"] - published[published_key]))

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
    first = fixture_projections(published_block())
    second = fixture_projections(published_block())
    assert first == second
    assert first[0] is not second[0]
    first[0]["probability"] = 0.1234
    assert fixture_projections(published_block())[0]["probability"] != 0.1234


# --------------------------------------------------------------------------
# provenance
# --------------------------------------------------------------------------

def test_full_time_projections_are_exact_and_half_time_are_estimated():
    projections = fixture_projections(raw_block())
    for projection in projections:
        if projection["scope"] == FULL_TIME:
            assert projection["provenance"] == PROVENANCE_EXACT, projection["key"]
        else:
            assert projection["provenance"] == PROVENANCE_ESTIMATED, projection["key"]


def test_half_time_projections_are_dropped_when_no_ht_lambda_is_published():
    """No assumption available means no half-time rows, not invented ones."""
    projections = fixture_projections(raw_block(expected_ht_goals=None))
    assert projections, "full-time projections should still be produced"
    assert all(projection["scope"] == FULL_TIME for projection in projections)
    assert not [projection for projection in projections if projection["family"] == "half_full"]


def test_ht_projections_need_both_lambdas():
    projections = fixture_projections(raw_block(expected_away_goals=None))
    assert projections == []


# --------------------------------------------------------------------------
# highlight selection — the "selection" behaviour
# --------------------------------------------------------------------------

def selected_for(**overrides) -> list[dict]:
    return select_highlights(fixture_projections(raw_block(**overrides)))


def test_selection_respects_threshold_ceiling_and_cap():
    selected = selected_for()
    assert len(selected) <= HIGHLIGHT_LIMIT
    for projection in selected:
        assert HIGHLIGHT_THRESHOLD <= projection["probability"] <= HIGHLIGHT_CEILING


def test_selection_excludes_near_certain_and_coin_flip_projections():
    """A highlight must be decisive but still in play.

    Long shots are decisive and useless (half-time under 6.5 is ~99.99% on most
    fixtures); anything near even is not a view at all.
    """
    selected = selected_for()
    for projection in selected:
        assert projection["probability"] < 0.999
        assert abs(projection["probability"] - 0.5) > 0.05


def test_selection_only_uses_mainstream_projections():
    """No long lines, no team totals, no exact score in a one-line summary."""
    for projection in selected_for():
        assert projection["promotable"] is True
        if projection["family"] == "goal_totals":
            assert projection["line"] in (1.5, 2.5, 3.5)
        if projection["family"] == "goal_margin":
            assert projection["line"] in (-1.0, -0.5, 0.0, 0.5, 1.0)
        assert projection["family"] not in ("team_total", "exact_score")


def test_measured_projections_outrank_assumed_ones():
    """Provenance is ranked ahead of decisiveness, so a 94% assumption never
    displaces a 61% measurement."""
    for block in (raw_block(), published_block()):
        selected = select_highlights(fixture_projections(block))
        seen_estimated = False
        for projection in selected:
            if projection["provenance"] == PROVENANCE_ESTIMATED:
                seen_estimated = True
            else:
                assert not seen_estimated, "an exact row appeared after an estimated row"


def test_estimated_highlights_only_appear_once_exact_projections_run_out():
    """Half-time rows may fill leftover slots, but never displace a full-time one."""
    high = published_block(
        expected_home_goals=1.9, expected_away_goals=0.4, expected_ht_goals=1.1,
    )
    selected = select_highlights(fixture_projections(high))
    assert selected
    full_time_count = sum(1 for projection in selected if projection["scope"] == FULL_TIME)
    assert full_time_count == len(selected) or full_time_count >= HIGHLIGHT_LIMIT - 2


def test_selection_collapses_projections_rounding_to_the_same_percentage():
    """AH -0.5 and AH -1 are near-identical scenarios at this scale; one slot only."""
    selected = selected_for()
    seen = set()
    for projection in selected:
        identity = (projection["family"], projection["scope"], round(projection["probability"] * 100))
        assert identity not in seen, f"{projection['label']} duplicates an earlier highlight"
        seen.add(identity)


def test_selection_is_deterministic():
    projections = fixture_projections(raw_block())
    first = [projection["key"] for projection in select_highlights(projections)]
    second = [projection["key"] for projection in select_highlights(list(reversed(projections)))]
    assert first == second


def test_selection_tolerates_missing_and_malformed_rows():
    assert select_highlights([]) == []
    assert select_highlights(None) == []
    assert select_highlights([{"label": "x", "probability": None}]) == []
    assert select_highlights([{"label": "x", "probability": "0.9"}]) == []
    assert select_highlights([{"label": "x", "probability": 0.9, "promotable": False}]) == []
    assert select_highlights("not a list") == []


def test_selection_respects_a_custom_threshold_and_limit():
    projections = fixture_projections(raw_block())
    assert len(select_highlights(projections, limit=2)) == 2
    assert len(select_highlights(projections, limit=0)) == 0
    loose = select_highlights(projections, threshold=0.0, ceiling=1.0, limit=3)
    assert len(loose) == 3
    for projection in select_highlights(projections, threshold=0.9):
        assert projection["probability"] >= 0.9


def test_a_ceiling_below_the_threshold_is_raised_to_it():
    """Misconfiguration must not silently return nothing."""
    projections = fixture_projections(raw_block())
    assert select_highlights(projections, threshold=0.9, ceiling=0.1) == \
        select_highlights(projections, threshold=0.9, ceiling=0.9)


def test_both_score_yes_becomes_a_highlight_when_the_model_expects_goals():
    """The behaviour the feature was asked for: a decisive goal-total line surfaces."""
    high_scoring = fixture_projections(raw_block(
        expected_home_goals=2.4, expected_away_goals=2.1, expected_ht_goals=1.6,
    ))
    selected = select_highlights(high_scoring)
    labels = {projection["label"] for projection in selected}
    assert "2+ goals" in labels
    assert all(projection["scope"] == FULL_TIME for projection in selected)


def test_low_scoring_fixture_promotes_under_lines():
    projections = fixture_projections(raw_block(
        expected_home_goals=0.7, expected_away_goals=0.8, expected_ht_goals=0.5,
    ))
    labels = {projection["label"] for projection in select_highlights(projections)}
    assert "3 or fewer goals" in labels or "2 or fewer goals" in labels


# --------------------------------------------------------------------------
# the served shape
# --------------------------------------------------------------------------

def test_projections_from_prediction_returns_projections_and_selection():
    out = projections_from_prediction({"raw": raw_block(), "xi": DEFAULT_RHO})
    assert set(out) == {"projections", "highlights"}
    assert out["projections"] and out["highlights"]
    assert len(out["highlights"]) <= HIGHLIGHT_LIMIT


def test_projections_from_prediction_ignores_the_placeholder_xi():
    """Every block publishes xi=0.0019, so honouring it would make the same
    wrong assumption everywhere. The correction is solved for instead, which is
    why the served projections are closer to the feed than that placeholder gives."""
    served = projections_from_prediction({"raw": published_block(), "xi": DEFAULT_RHO})
    assert served == projections_from_prediction({"raw": published_block()})

    placeholder = {
        projection["key"]: projection["probability"]
        for projection in fixture_projections(published_block(), rho=DEFAULT_RHO)
    }
    actual = {projection["key"]: projection["probability"] for projection in served["projections"]}
    assert abs(actual["ft.outcome.home"] - PUBLISHED["home"]) < \
        abs(placeholder["ft.outcome.home"] - PUBLISHED["home"])


def test_projections_from_prediction_on_a_block_without_lambdas():
    out = projections_from_prediction({"raw": {"home": 0.3, "away": 0.4}})
    assert out == {"projections": [], "highlights": []}


@pytest.mark.parametrize("preds", [None, {}, "nope", {"raw": None}, {"raw": "nope"}])
def test_projections_from_prediction_tolerates_junk(preds):
    assert projections_from_prediction(preds) == {"projections": [], "highlights": []}


def test_no_prediction_is_invented_for_a_missing_prediction_block():
    assert projections_from_prediction({}) == {"projections": [], "highlights": []}
    assert fixture_projections({}) == []
    assert fixture_projections(None) == []


def test_every_served_row_has_the_shape_the_table_relies_on():
    required = {"key", "family", "label", "scope", "line", "selection", "probability", "provenance", "promotable"}
    for projection in fixture_projections(raw_block()):
        assert required <= set(projection)
        assert projection["scope"] in (FULL_TIME, HALF_TIME, HALF_TO_FULL)
        assert projection["provenance"] in (PROVENANCE_EXACT, PROVENANCE_ESTIMATED)
        assert 0.0 <= projection["probability"] <= 1.0
        assert projection["key"].count(".") >= 1
    keys = [projection["key"] for projection in fixture_projections(raw_block())]
    assert len(keys) == len(set(keys)), "projection keys must be unique"


# ---------------------------------------------------------------------------
# projection_detail — the explanation behind one derived projection
# ---------------------------------------------------------------------------


def explain(raw: dict, key: str) -> dict | None:
    """The explanation the API serves for `key` on a fixture built from `raw`."""
    rows = by_key(fixture_projections(raw))
    assert key in rows, key
    return projection_detail(raw, rows[key])


def test_every_derived_projection_has_an_explanation():
    """No projection may be listed without a mechanism behind it."""
    for row in fixture_projections(published_block()):
        detail = projection_detail(published_block(), row)
        assert detail is not None, row["key"]


def test_explanation_reproduces_the_row_it_explains():
    """The number in the table and the number in the modal must not disagree."""
    for row in fixture_projections(published_block()):
        detail = projection_detail(published_block(), row)
        if detail is None or detail.get("factors"):
            continue
        assert detail["outcomes"]["win"] == pytest.approx(row["probability"], abs=TOL)
        if isinstance(row.get("refund"), (int, float)) and row["refund"] > 0:
            assert detail["outcomes"]["refund"] == pytest.approx(row["refund"], abs=TOL)


def test_a_result_projection_lists_exactly_the_scorelines_on_its_side():
    detail = explain(published_block(), "ft.outcome.home")
    for cell in detail["cells"]:
        assert cell["home_goals"] > cell["away_goals"]
    assert detail["successful_cells"] == len(detail["cells"])
    assert detail["outcomes"]["refund"] == 0.0
    # A result cannot refund, so every listed cell is a clean win.
    assert {cell["outcome"] for cell in detail["cells"]} == {"win"}


def test_a_exact_score_projection_names_exactly_one_scoreline():
    detail = explain(published_block(), "ft.exact_score.2-1")
    assert len(detail["cells"]) == 1
    assert detail["cells"][0]["score"] == "2-1"
    assert detail["successful_cells"] == 1


def test_a_totals_projection_only_lists_scorelines_over_the_line():
    detail = explain(published_block(), "ft.goal_totals.over_2.5")
    for cell in detail["cells"]:
        assert cell["home_goals"] + cell["away_goals"] > 2.5


def test_cells_are_ordered_by_how_likely_they_are():
    detail = explain(published_block(), "ft.goal_totals.over_2.5")
    probabilities = [cell["probability"] for cell in detail["cells"]]
    assert probabilities == sorted(probabilities, reverse=True)


def test_shares_are_a_split_of_each_successful_outcome():
    """A share is a share of something, so each outcome's shares must add up."""
    detail = explain(published_block(), "ft.goal_margin.-1.0_home")
    for outcome in ("win", "refund"):
        total = sum(
            cell["share"]
            for cell in detail["cells"]
            if outcome in cell["outcome"].split("+")
        )
        assert total == pytest.approx(1.0, abs=0.01), outcome


def test_a_quarter_line_splits_a_draw_between_refund_and_lose():
    detail = explain(published_block(), "ft.goal_margin.-0.25_home")
    draws = [c for c in detail["cells"] if c["home_goals"] == c["away_goals"]]
    assert draws
    # Half the share is refunded and half is lost, so neither side is a clean win.
    assert {c["outcome"] for c in draws} == {"refund+lose"}


def test_the_away_side_of_a_margin_is_the_mirror_of_the_home_side():
    home = explain(published_block(), "ft.goal_margin.-0.5_home")
    away = explain(published_block(), "ft.goal_margin.-0.5_away")
    assert home["outcomes"]["lose"] == pytest.approx(away["outcomes"]["win"], abs=TOL)
    assert home["outcomes"]["win"] == pytest.approx(away["outcomes"]["lose"], abs=TOL)
    # Home -0.5 can never refund, so both sides count on the same scorelines.
    assert home["successful_cells"] + away["successful_cells"] == home["grid_cells"]


def test_a_whole_margin_line_refunds_on_the_exact_scoreline():
    detail = explain(published_block(), "ft.goal_margin.-1.0_home")
    refunds = [c for c in detail["cells"] if c["outcome"] == "refund"]
    # Handing over exactly one goal: the one-goal scorelines refund and nothing
    # else does, because every other margin counts cleanly.
    assert refunds
    assert {c["home_goals"] - c["away_goals"] for c in refunds} == {1}
    assert detail["outcomes"]["refund"] > 0
    # The refund is every one-goal result, and those are the only refunded cells.
    one_goal = {c["score"] for c in detail["cells"] if c["home_goals"] - c["away_goals"] == 1}
    assert {c["score"] for c in refunds} == one_goal


def test_half_time_full_time_explains_itself_with_factors_not_scorelines():
    detail = explain(published_block(), "half_full.home.home")
    assert detail["cells"] == []
    assert detail["successful_cells"] == 0
    assert detail["factors"]["half_time_side"] == "home"
    assert detail["factors"]["full_time_side"] == "home"
    # Quoted at the win probability, which is the product of the two splits.
    expected = (
        detail["factors"]["half_time"]["home"] * detail["factors"]["full_time"]["home"]
    )
    assert detail["outcomes"]["win"] == pytest.approx(expected, abs=TOL)


def test_an_unexplainable_row_returns_none_rather_than_guessing():
    """A row the grid cannot rebuild must be refused, not approximated."""
    assert projection_detail(published_block(), {"family": "made_up", "scope": FULL_TIME}) is None
    assert projection_detail(published_block(), {"family": "goal_totals", "scope": FULL_TIME, "line": "nonsense"}) is None


def test_no_explanation_without_usable_lambdas():
    """The same rule as the menu: a block with no goals serves no projections."""
    raw = published_block()
    for key in ("expected_home_goals", "expected_away_goals"):
        raw.pop(key)
    assert projection_detail(raw, {"family": "outcome", "scope": FULL_TIME, "selection": "home"}) is None
