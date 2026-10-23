"""Prediction markets derived from the dc_v2 Dixon-Coles parameters.

dc_v2 publishes only 13 raw and 8 calibrated numbers per fixture: 1X2, a fixed
handful of O/U lines and BTTS. It does not publish an Asian handicap, a correct
score, HT/FT or any price. Those cannot be read from the feed, so this module
reconstructs them.

What dc_v2 *does* publish are the parameters of a Dixon-Coles bivariate Poisson
(`expected_home_goals`, `expected_away_goals` and a draw correction `xi`).
Rebuilding the joint score grid from them and reading the markets back off
reproduces the probabilities the feed already publishes, which is what licenses
deriving the markets it never published.

The published `xi`, though, turns out not to be the parameter that generated
those probabilities. It is 0.0019 on all 241 collected blocks, and using it
leaves up to 2pp of error on the low total lines — in opposite directions on
over 0.5 and over 1.5, which is the signature of a mis-stated low-score
correction rather than a different model. Solving for the correction that does
reproduce the feed removes 96% of that error:

    residual over the 5 published O/U lines, summed absolute error
        using the published xi=0.0019     mean 0.0100   max 0.0426
        solving for the correction         mean 0.0004   max 0.0077

so `fit_rho` recovers it from the O/U lines the feed does publish. The true
correction is negative for most fixtures (median -0.008) and varies widely
(range -0.20 to +0.10), i.e. it is fitted per fixture and the published `xi` is
a placeholder that carries none of that information.

Two grades of number come out, and every row is tagged with which one it is so
the UI never presents an estimate as a measurement:

    model    read off the full-time grid. The lambdas and the correction are
             recovered from the feed, so 1X2, double chance, O/U, BTTS, Asian
             handicap, correct score and team totals are exact given the model.

    modelled carries an assumption. dc_v2 publishes `expected_ht_goals` as a
             single *total* and never says how it splits between the two teams,
             so half-time markets need a split. This module assumes it is
             proportional to the full-time ratio, and assumes the halves are
             independent. That is the only assumption standing between the feed
             and a half-time number, and it is the reason those rows are
             badged rather than presented as model output.
"""
from __future__ import annotations

import math
from functools import lru_cache

# Goals per side retained. A bivariate Poisson on realistic lambdas puts
# essentially all its mass inside 0..8, and normalising the retained block keeps
# every derived market summing to exactly 1.
GRID = 9

# dc_v2's published draw correction. Used only when a block publishes too few
# O/U lines to solve for the real one.
DEFAULT_RHO = 0.0019

# Bounds for that solve, chosen from the range observed across the collected
# feed and to keep every corrected cell positive.
RHO_MIN = -0.30
RHO_MAX = 0.30
# Golden-section iterations. The objective is smooth and single-bounded; 48 is
# well past the point where the interval stops moving at feed precision.
RHO_ITERATIONS = 48

# A market becomes a chip once the model is this sure of it, and at most this
# many are shown. `model` rows outrank equally decisive `modelled` ones, so an
# assumption never displaces a measured number.
#
# The ceiling matters as much as the floor. Ranking purely by distance from a
# coin flip fills every slot with near-certain long shots — "half-time under 6.5"
# is 99.99% on almost every fixture and tells nobody anything. A chip is only
# worth showing when the model is decisive about something still in play, so
# markets above the ceiling are kept in the full table but never promoted.
MARKET_THRESHOLD = 0.60
MARKET_CEILING = 0.95
MARKET_LIMIT = 6

# Only mainstream markets can be promoted to a chip. Ranking the whole menu
# fills the slots with long shots nobody prices — under 5.5 is 93% on most
# fixtures and under 6.5 at half time is 99.99% on nearly all of them, so they
# would crowd out every market the reader actually wants. The full table still
# serves all of them; this only decides what a one-line summary may show.
PROMOTABLE_TOTALS_LINES = (1.5, 2.5, 3.5)
PROMOTABLE_HANDICAP_LINES = (-1.0, -0.5, 0.0, 0.5, 1.0)

PROVENANCE_MODEL = "model"
PROVENANCE_MODELLED = "modelled"
_PROVENANCE_RANK = {PROVENANCE_MODEL: 0, PROVENANCE_MODELLED: 1}

TOTALS_LINES = (0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5)
TEAM_TOTAL_LINES = (0.5, 1.5, 2.5, 3.5)
# Whole goals, half goals and the quarter lines between them.
HANDICAP_LINES = (
    -1.5, -1.25, -1.0, -0.75, -0.5, -0.25,
    0.0,
    0.25, 0.5, 0.75, 1.0, 1.25, 1.5,
)

# Correct score is a 9x9 table; only the meaningful tail is worth rendering.
CORRECT_SCORE_FLOOR = 0.01

FULL_TIME = "full_time"
HALF_TIME = "half_time"
HALF_TO_FULL = "half_to_full"

Grid = tuple[tuple[float, ...], ...]


def _number(value) -> float | None:
    """A usable float, or None. Booleans are not numbers for our purposes."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if math.isfinite(number) else None


def _poisson(goals: int, lam: float) -> float:
    """P(X = goals) for X ~ Poisson(lam)."""
    return math.exp(-lam) * lam**goals / math.factorial(goals)


def _dixon_coles_tau(home_goals: int, away_goals: int, lam_h: float, lam_a: float, rho: float) -> float:
    """The DC low-score correction, applied to the four cells it touches.

    The correction exists because independent Poissons understate 0-0 and
    1-1 and overstate 0-1 and 1-0. It can go negative on the 0-0 cell for
    extreme lambdas, which the caller guards against before we get here.
    """
    if home_goals == 0 and away_goals == 0:
        return 1.0 - lam_h * lam_a * rho
    if home_goals == 0 and away_goals == 1:
        return 1.0 + lam_h * rho
    if home_goals == 1 and away_goals == 0:
        return 1.0 + lam_a * rho
    if home_goals == 1 and away_goals == 1:
        return 1.0 - rho
    return 1.0


@lru_cache(maxsize=4096)
def _poisson_matrix(lam_h: float, lam_a: float) -> tuple[tuple[float, ...], ...]:
    """Independent Poisson joint mass, independent of the draw correction.

    Split out because solving for the correction re-evaluates the grid dozens
    of times and the Poisson factors never change across those evaluations —
    only the four low-score cells do.
    """
    return tuple(
        tuple(_poisson(i, lam_h) * _poisson(j, lam_a) for j in range(GRID))
        for i in range(GRID)
    )


def _build_grid(lam_h: float, lam_a: float, rho: float) -> Grid:
    """Normalised joint distribution of (home goals, away goals)."""
    base = _poisson_matrix(lam_h, lam_a)
    cells = [
        [
            _dixon_coles_tau(i, j, lam_h, lam_a, rho) * base[i][j]
            for j in range(GRID)
        ]
        for i in range(GRID)
    ]

    # A DC correction that would drive any cell negative means the parameters
    # are outside the model's domain. Fall back to plain independent Poissons
    # rather than emit a negative probability.
    if any(value < 0.0 for row in cells for value in row):
        return _normalise(base)

    return _normalise(cells)


def _normalise(cells) -> Grid:
    """Scale a grid to sum to exactly 1, so every market derived from it does too."""
    total = math.fsum(value for row in cells for value in row)
    if total <= 0.0:
        return tuple()
    return tuple(tuple(value / total for value in row) for row in cells)


@lru_cache(maxsize=4096)
def _grid(lam_h: float, lam_a: float, rho: float) -> Grid:
    """`_build_grid`, cached on parameters rounded to 4dp.

    The feeds carry 4dp, so this collapses to a handful of entries across a
    whole league while keeping distinct fixtures distinct.
    """
    return _build_grid(lam_h, lam_a, rho)


def score_grid(lam_home, lam_away, rho=DEFAULT_RHO) -> Grid | None:
    """Joint score grid for one fixture, or None when it cannot be built.

    None means "no market can be derived here" — a missing or non-positive
    lambda. Callers must omit those markets rather than publish zeros.
    """
    lam_h = _number(lam_home)
    lam_a = _number(lam_away)
    if lam_h is None or lam_a is None or lam_h <= 0.0 or lam_a <= 0.0:
        return None
    rho_value = _number(rho)
    if rho_value is None:
        rho_value = DEFAULT_RHO
    rho_value = max(RHO_MIN, min(RHO_MAX, rho_value))
    return _grid(round(lam_h, 4), round(lam_a, 4), round(rho_value, 6))


def _where(grid: Grid, predicate) -> float:
    return math.fsum(
        grid[i][j] for i in range(len(grid)) for j in range(len(grid)) if predicate(i, j)
    )


def _marginals(grid: Grid) -> dict[str, float]:
    """P(home win), P(draw), P(away win) for one grid."""
    return {
        "home": _where(grid, lambda i, j: i > j),
        "draw": _where(grid, lambda i, j: i == j),
        "away": _where(grid, lambda i, j: i < j),
    }


def _row(
    key: str,
    family: str,
    label: str,
    scope: str,
    probability: float,
    provenance: str,
    *,
    line: float | None = None,
    selection: str | None = None,
    promotable: bool = False,
    **extra,
) -> dict:
    row = {
        "key": key,
        "family": family,
        "label": label,
        "scope": scope,
        "line": line,
        "selection": selection,
        "probability": round(probability, 4),
        "provenance": provenance,
        "promotable": promotable,
    }
    row.update(extra)
    return row


def _totals(grid: Grid, scope: str, provenance: str, prefix: str, lines=TOTALS_LINES) -> list[dict]:
    """Over/under pairs. Under is the exact complement of the rounded over."""
    rows: list[dict] = []
    for line in lines:
        over = round(_where(grid, lambda i, j, line=line: i + j > line), 4)
        promotable = line in PROMOTABLE_TOTALS_LINES
        rows.append(_row(
            f"{prefix}.totals.over_{line}", "totals", f"O{line}", scope, over, provenance,
            line=line, selection="over", promotable=promotable,
        ))
        rows.append(_row(
            f"{prefix}.totals.under_{line}", "totals", f"U{line}", scope,
            round(1.0 - over, 4), provenance, line=line, selection="under", promotable=promotable,
        ))
    return rows


def _result(grid: Grid, scope: str, provenance: str, prefix: str) -> list[dict]:
    marginals = _marginals(grid)
    home = round(marginals["home"], 4)
    away = round(marginals["away"], 4)
    draw = round(1.0 - home - away, 4)
    return [
        _row(f"{prefix}.result.home", "result", "1", scope, home, provenance, selection="home", promotable=True),
        _row(f"{prefix}.result.draw", "result", "X", scope, draw, provenance, selection="draw", promotable=True),
        _row(f"{prefix}.result.away", "result", "2", scope, away, provenance, selection="away", promotable=True),
    ]


def _double_chance(grid: Grid, scope: str, provenance: str, prefix: str) -> list[dict]:
    marginals = _marginals(grid)
    return [
        _row(f"{prefix}.double_chance.home_or_draw", "double_chance", "1X", scope,
             round(marginals["home"] + marginals["draw"], 4), provenance,
             selection="home_or_draw", promotable=True),
        _row(f"{prefix}.double_chance.draw_or_away", "double_chance", "X2", scope,
             round(marginals["draw"] + marginals["away"], 4), provenance,
             selection="draw_or_away", promotable=True),
        _row(f"{prefix}.double_chance.home_or_away", "double_chance", "12", scope,
             round(marginals["home"] + marginals["away"], 4), provenance,
             selection="home_or_away", promotable=True),
    ]


def _btts(grid: Grid, scope: str, provenance: str, prefix: str) -> list[dict]:
    yes = round(_where(grid, lambda i, j: i > 0 and j > 0), 4)
    return [
        _row(f"{prefix}.btts.yes", "btts", "BTTS yes", scope, yes, provenance,
             selection="yes", promotable=True),
        _row(f"{prefix}.btts.no", "btts", "BTTS no", scope, round(1.0 - yes, 4), provenance,
             selection="no", promotable=True),
    ]


def _handicap_components(line: float) -> tuple[float, ...]:
    """The bets a handicap line settles as: one, or two half-stakes.

    A quarter line is half of one half-goal line and half of the next, so -0.25
    settles as half of -0.5 plus half of 0.0. Settling it as a single line would
    report the wrong push probability, so the line is split into components.
    """
    lower = math.floor(line * 2) / 2
    if math.isclose(lower, line, abs_tol=1e-9):
        return (line,)
    return (lower, lower + 0.5)


def _handicap_cell_shares(grid: Grid, line: float) -> list[list[tuple[float, float, float]]]:
    """Per-cell (win, push, lose) mass for the home side of a handicap line.

    Each cell's mass is split evenly across the line's components, so a cell
    that pushes one half-stake and loses the other reports half of each. Away
    covering is the mirror of this: its win is the home side's lose, and it
    pushes on exactly the same scorelines.
    """
    components = _handicap_components(line)
    share = 1.0 / len(components)
    shares: list[list[tuple[float, float, float]]] = []
    for i, row in enumerate(grid):
        cells: list[tuple[float, float, float]] = []
        for j, value in enumerate(row):
            win = push = lose = 0.0
            for component in components:
                margin = (i - j) + component
                if margin > 0:
                    win += value
                elif margin == 0:
                    push += value
                else:
                    lose += value
            cells.append((win * share, push * share, lose * share))
        shares.append(cells)
    return shares


def handicap_settlement(grid: Grid, line: float) -> tuple[float, float, float]:
    """(win, push, lose) for the home team at an Asian handicap, from `grid`.

    A positive line means home receives that many goals, negative means home
    gives them; both are the same arithmetic, `margin + line`.
    """
    cells = _handicap_cell_shares(grid, line)
    size = len(cells)
    return tuple(
        math.fsum(cells[i][j][k] for i in range(size) for j in range(size))
        for k in range(3)
    )


def _handicaps(grid: Grid, scope: str, provenance: str, prefix: str) -> list[dict]:
    """Both sides of every handicap line, with the push probability carried.

    Away covers is exactly 1 - home - push, so it is written as the complement
    rather than recomputed.
    """
    rows: list[dict] = []
    for line in HANDICAP_LINES:
        win, push, lose = handicap_settlement(grid, line)
        home_p = round(win, 4)
        push_p = round(push, 4)
        promotable = line in PROMOTABLE_HANDICAP_LINES
        # Both sides of a line are two different bets and must not share a
        # label: a positive line means home receives goals, so the away bet on
        # the same handicap is quoted at the negated line. Labelled the way a
        # bettor would write it — "Home -0.5" and "Away +0.5".
        rows.append(_row(
            f"{prefix}.asian_handicap.{line}_home", "asian_handicap", f"Home {line:+g}", scope,
            home_p, provenance, line=line, selection="home", push=push_p, promotable=promotable,
        ))
        rows.append(_row(
            f"{prefix}.asian_handicap.{line}_away", "asian_handicap", f"Away {-line:+g}", scope,
            round(1.0 - home_p - push_p, 4), provenance, line=line, selection="away",
            promotable=promotable,
        ))
    return rows


def _team_totals(grid: Grid, scope: str, provenance: str, prefix: str) -> list[dict]:
    """Per-team goal lines, e.g. "Home over 1.5"."""
    rows: list[dict] = []
    for side, index in (("home", 0), ("away", 1)):
        for line in TEAM_TOTAL_LINES:
            over = round(
                _where(grid, lambda i, j, index=index, line=line: (i if index == 0 else j) > line),
                4,
            )
            name = "Home" if side == "home" else "Away"
            rows.append(_row(
                f"{prefix}.team_total.{side}.over_{line}", "team_total", f"{name} O{line}", scope,
                over, provenance, line=line, selection=side,
            ))
            rows.append(_row(
                f"{prefix}.team_total.{side}.under_{line}", "team_total", f"{name} U{line}", scope,
                round(1.0 - over, 4), provenance, line=line, selection=side,
            ))
    return rows


def _correct_score(grid: Grid, scope: str, provenance: str, prefix: str) -> list[dict]:
    """The meaningful part of the score grid, most likely first."""
    rows = [
        _row(
            f"{prefix}.correct_score.{i}-{j}", "correct_score", f"{i}-{j}", scope, grid[i][j],
            provenance, line=None, selection="home_away",
        )
        for i in range(len(grid)) for j in range(len(grid))
        if grid[i][j] >= CORRECT_SCORE_FLOOR
    ]
    rows.sort(key=lambda row: (-row["probability"], row["key"]))
    return rows


def _ht_ft(ht_grid: Grid, ft_grid: Grid) -> list[dict]:
    """All nine half-time/full-time combinations.

    The two halves are indexed independently — the half-time score and the
    full-time score are not the same cell of anything — so independence makes
    each combination a plain product of the two marginals. That independence
    is not confirmed by the feed, hence `modelled`.
    """
    ht = _marginals(ht_grid)
    ft = _marginals(ft_grid)
    short = {"home": "1", "draw": "X", "away": "2"}
    return [
        _row(
            f"ht_ft.{ht_side}.{ft_side}", "ht_ft", f"{short[ht_side]}/{short[ft_side]}",
            HALF_TO_FULL, round(ht[ht_side] * ft[ft_side], 4), PROVENANCE_MODELLED,
            selection=f"{ht_side}_{ft_side}", promotable=True,
        )
        for ht_side in ("home", "draw", "away")
        for ft_side in ("home", "draw", "away")
    ]


def _half_time_grid(raw: dict, lam_h: float, lam_a: float, lam_ht: float) -> Grid | None:
    """The half-time grid: a split of the published total, then a solved correction.

    dc_v2 publishes `expected_ht_goals` as a single number and never says how it
    splits between the teams. The only defensible split available is
    proportional to the full-time ratio — that assumption is unavoidable, and is
    why half-time rows are badged `modelled`.

    The low-score correction *is* solvable, because the feed also publishes the
    two half-time O/U lines. Fitting it there rather than reusing the
    full-time value takes the half-time line error from 0.0064 mean / 0.0204 max
    down to 0.00006 / 0.0014.
    """
    if lam_ht <= 0.0:
        return None
    share = lam_h / (lam_h + lam_a)
    lam_h_ht = lam_ht * share
    lam_a_ht = lam_ht * (1.0 - share)
    rho = fit_rho(raw, lam_h_ht, lam_a_ht, prefix="ht_", lines=HALF_TIME_LINES)
    return score_grid(lam_h_ht, lam_a_ht, rho)


def full_time_markets(grid: Grid) -> list[dict]:
    """Every full-time market, all of them `model` provenance."""
    rows: list[dict] = []
    rows += _result(grid, FULL_TIME, PROVENANCE_MODEL, "ft")
    rows += _double_chance(grid, FULL_TIME, PROVENANCE_MODEL, "ft")
    rows += _totals(grid, FULL_TIME, PROVENANCE_MODEL, "ft")
    rows += _btts(grid, FULL_TIME, PROVENANCE_MODEL, "ft")
    rows += _handicaps(grid, FULL_TIME, PROVENANCE_MODEL, "ft")
    rows += _team_totals(grid, FULL_TIME, PROVENANCE_MODEL, "ft")
    rows += _correct_score(grid, FULL_TIME, PROVENANCE_MODEL, "ft")
    return rows


def half_time_markets(ht_grid: Grid) -> list[dict]:
    """Half-time markets, all of them `modelled` provenance."""
    rows: list[dict] = []
    rows += _result(ht_grid, HALF_TIME, PROVENANCE_MODELLED, "ht")
    rows += _double_chance(ht_grid, HALF_TIME, PROVENANCE_MODELLED, "ht")
    rows += _totals(ht_grid, HALF_TIME, PROVENANCE_MODELLED, "ht")
    rows += _btts(ht_grid, HALF_TIME, PROVENANCE_MODELLED, "ht")
    rows += _handicaps(ht_grid, HALF_TIME, PROVENANCE_MODELLED, "ht")
    rows += _team_totals(ht_grid, HALF_TIME, PROVENANCE_MODELLED, "ht")
    return rows


def _over_probabilities(grid: Grid, lines) -> list[float]:
    """P(total goals > line) for each requested line."""
    totals = [0.0] * (2 * len(grid) - 1)
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            totals[i + j] += value
    # Line L is beaten by every total of L+1 or more.
    return [math.fsum(totals[int(line) + 1:]) for line in lines]


def _rho_bounds(lam_h: float, lam_a: float) -> tuple[float, float]:
    """The search range, tightened so no corrected cell can go negative."""
    upper = RHO_MAX
    product = lam_h * lam_a
    if product > 0:
        # 1 - lam_h*lam_a*rho > 0 on the 0-0 cell.
        upper = min(upper, 0.99 / product)
    return RHO_MIN, min(RHO_MAX, max(upper, RHO_MIN + 1e-6))


def _solve_rho(lam_h: float, lam_a: float, targets, lines) -> float:
    """Golden-section search for the correction matching `targets` best.

    `targets` is [(index into `lines`, published probability), ...]. A few dozen
    grid evaluations is nothing next to the derivation that follows.
    """
    def objective(rho: float) -> float:
        grid = _build_grid(lam_h, lam_a, rho)
        if not grid:
            return math.inf
        over = _over_probabilities(grid, lines)
        return math.fsum((over[index] - value) ** 2 for index, value in targets)

    low, high = _rho_bounds(lam_h, lam_a)
    golden = (math.sqrt(5.0) - 1.0) / 2.0
    a, b = high - golden * (high - low), low + golden * (high - low)
    fa, fb = objective(a), objective(b)
    for _ in range(RHO_ITERATIONS):
        if fa <= fb:
            high, b, fb = b, a, fa
            a = high - golden * (high - low)
            fa = objective(a)
        else:
            low, a, fa = a, b, fb
            b = low + golden * (high - low)
            fb = objective(b)

    rho = (low + high) / 2.0
    # Not worth shipping a correction that fits worse than the placeholder.
    return rho if objective(rho) <= objective(DEFAULT_RHO) else DEFAULT_RHO


# The lines the feed publishes, per scope.
FULL_TIME_LINES = (0.5, 1.5, 2.5, 3.5, 4.5)
HALF_TIME_LINES = (0.5, 1.5)


def _targets(raw: dict, prefix: str, lines) -> list[tuple[int, float]] | None:
    """The published probabilities this scope can be fitted against."""
    found = [
        (index, _number(raw.get(f"{prefix}over_{line:g}")))
        for index, line in enumerate(lines)
    ]
    usable = [(index, value) for index, value in found if isinstance(value, (int, float))]
    # One line cannot identify a parameter; two can, and the half-time scope
    # only ever publishes two, so this has to allow them.
    return usable if len(usable) >= 2 else None


def fit_rho(raw: dict, lam_home, lam_away, *, prefix: str = "", lines=FULL_TIME_LINES) -> float:
    """Recover the draw correction dc_v2 used but did not publish.

    A block publishes its two lambdas and five O/U lines. Between them there is
    exactly one free parameter left in a Dixon-Coles model — the low-score
    correction — so it can be solved for rather than assumed, which is what
    brings the reconstruction back onto the published numbers (see the module
    docstring for the before/after residuals).

    Falls back to the published placeholder when the block carries too few lines
    to identify the parameter, or when the solve does not beat the placeholder.
    """
    lam_h = _number(lam_home)
    lam_a = _number(lam_away)
    if lam_h is None or lam_a is None or lam_h <= 0.0 or lam_a <= 0.0:
        return DEFAULT_RHO
    targets = _targets(raw, prefix, lines)
    if targets is None:
        return DEFAULT_RHO
    return _solve_rho(lam_h, lam_a, targets, lines)


def _grids(raw: dict, rho=None) -> tuple[Grid | None, Grid | None]:
    """(full-time grid, half-time grid) for one dc_v2 raw block.

    Neither grid is derivable without both lambdas, so both are None together.
    The half-time grid is optional: a block that publishes no expected
    half-time total simply has no half-time markets.

    Solving for the corrections costs a few dozen grid builds per scope, so the
    cached entry point keys on the same signature `fixture_markets` uses.
    """
    if rho is not None:
        return _solve_grids(raw, rho)
    return _cached_grids(_signature(raw))


@lru_cache(maxsize=4096)
def _cached_grids(signature: tuple) -> tuple[Grid | None, Grid | None]:
    return _solve_grids(dict(zip(_SIGNATURE_KEYS, signature)), None)


def _solve_grids(raw: dict, rho) -> tuple[Grid | None, Grid | None]:
    """The uncached grid build, shared by the cached and forced-rho entry points."""
    lam_h = _number(raw.get("expected_home_goals"))
    lam_a = _number(raw.get("expected_away_goals"))
    if lam_h is None or lam_a is None or lam_h <= 0.0 or lam_a <= 0.0:
        return None, None

    if rho is None:
        rho = fit_rho(raw, lam_h, lam_a)
    ft_grid = score_grid(lam_h, lam_a, rho)
    if not ft_grid:
        return None, None

    ht_grid = None
    lam_ht = _number(raw.get("expected_ht_goals"))
    if lam_ht is not None and lam_ht > 0.0:
        ht_grid = _half_time_grid(raw, lam_h, lam_a, lam_ht)
    return ft_grid, ht_grid


def _build_markets(raw: dict, rho) -> list[dict]:
    """The uncached derivation, shared by the cached and forced-rho entry points."""
    ft_grid, ht_grid = _grids(raw, rho)
    if not ft_grid:
        return []

    rows = full_time_markets(ft_grid)
    if ht_grid:
        rows += half_time_markets(ht_grid)
        rows += _ht_ft(ht_grid, ft_grid)
    return rows


# Every raw-block key the derivation reads. Hashable, so it doubles as the cache
# key: the list feed re-derives the same fixtures on every request, and solving
# for the correction twice is pure waste.
_SIGNATURE_KEYS = (
    "expected_home_goals", "expected_away_goals", "expected_ht_goals",
    *(f"over_{line:g}" for line in FULL_TIME_LINES),
    *(f"ht_over_{line:g}" for line in HALF_TIME_LINES),
)


def _signature(raw: dict) -> tuple:
    return tuple(_number(raw.get(key)) for key in _SIGNATURE_KEYS)


@lru_cache(maxsize=4096)
def _cached_markets(signature: tuple) -> tuple[dict, ...]:
    return tuple(_build_markets(dict(zip(_SIGNATURE_KEYS, signature)), None))


def fixture_markets(raw: dict, rho=None) -> list[dict]:
    """Every derivable market for one fixture, or [] when none can be derived.

    `raw` is the dc_v2 `raw` block, which is where the lambdas and the published
    O/U lines live.

    The corrections are solved for from those lines, so the result is cached on
    the block's own numbers. Passing `rho` forces the full-time correction and
    bypasses the cache; it exists for tests, not for callers.

    Rows are handed out as fresh shallow copies, so callers may treat them as
    their own.
    """
    if not isinstance(raw, dict):
        return []
    if rho is not None:
        return _build_markets(raw, rho)
    return [dict(row) for row in _cached_markets(_signature(raw))]


def select_markets(
    markets: list[dict],
    threshold: float = MARKET_THRESHOLD,
    limit: int = MARKET_LIMIT,
    ceiling: float = MARKET_CEILING,
) -> list[dict]:
    """The markets the model is confident enough to show as chips.

    This is the "flexible rate" behaviour: rather than a fixed set of chips, a
    market earns a slot by being decisive about something still in play. Kept
    when it is a mainstream market whose probability sits in the
    threshold..ceiling band, ordered by how far from a coin flip it sits, and
    capped.

    Provenance is ranked *before* decisiveness, so a measured full-time market
    always outranks an assumed half-time one. Without that, a 94% assumed
    "half-time under 2.5" crowds out a measured "under 3.5" and the summary
    reads like it is mostly guesswork.

    Markets that round to the same percentage within a family and scope are
    collapsed to one. Half-time Asian handicaps and double chance are nearly
    the same bet — at one goal a half apart from a coin flip, "AH -0.5", "AH -1"
    and "X2" all land on 79% — and listing all three wastes a slot.
    """
    if threshold is None:
        threshold = MARKET_THRESHOLD
    if limit is None:
        limit = MARKET_LIMIT
    if ceiling is None:
        ceiling = 1.0
    threshold = float(threshold)
    ceiling = max(float(ceiling), threshold)
    limit = int(limit)

    ranked = [
        market for market in markets or []
        if isinstance(market, dict)
        and market.get("promotable")
        and isinstance(market.get("probability"), (int, float))
        and not isinstance(market.get("probability"), bool)
        and threshold <= market["probability"] <= ceiling
    ]
    ranked.sort(key=lambda market: (
        _PROVENANCE_RANK.get(market.get("provenance"), 2),
        -abs(market["probability"] - 0.5),
        str(market.get("family") or ""),
        str(market.get("key") or ""),
    ))

    chosen: list[dict] = []
    seen: set[tuple] = set()
    for market in ranked:
        if len(chosen) >= limit:
            break
        identity = (
            market.get("family"),
            market.get("scope"),
            round(float(market["probability"]) * 100),
        )
        if identity in seen:
            continue
        seen.add(identity)
        chosen.append(market)
    return chosen


def markets_from_prediction(preds: dict) -> dict:
    """Markets for one dc_v2 block, as served to the API.

    Returns {"markets": [...], "selected": [...]}. Both are empty when the block
    carries no usable lambdas, so callers never have to distinguish "no
    prediction" from "prediction without markets".

    `preds["xi"]` is deliberately not passed through: it is a constant
    placeholder, and letting `fixture_markets` solve the real correction from the
    published O/U lines is both more accurate and no more assumptive.
    """
    if not isinstance(preds, dict):
        return {"markets": [], "selected": []}
    markets = fixture_markets(preds.get("raw") or {})
    return {"markets": markets, "selected": select_markets(markets)}


# ── per-market explanation ───────────────────────────────────────────────────
# Every market above is a number with no visible mechanism: "Away +0.5 at 62%"
# does not say which scorelines pay it, or what a quarter line does on a level
# result. These helpers rebuild the grid a row came from and enumerate the cells
# behind it, so a reader can see why the number is what it is.

# Settlement kinds. A market either collects cells that all pay (1X2, a goal
# line, BTTS) or settles cell by cell against a handicap.
ALL_OR_NOTHING = "all_or_nothing"
SETTLED = "settled"

# Order the three settlement outcomes are reported in.
_OUTCOMES = ("win", "push", "lose")

_RESULT_SIDES = {
    "home": lambda i, j: i > j,
    "draw": lambda i, j: i == j,
    "away": lambda i, j: i < j,
}
_DOUBLE_CHANCE_SIDES = {
    "home_or_draw": lambda i, j: i >= j,
    "draw_or_away": lambda i, j: i <= j,
    "home_or_away": lambda i, j: i != j,
}

_METHOD = {
    "result": "every scoreline on the winning side of the draw line",
    "double_chance": "every scoreline that satisfies the two-outcome condition",
    "totals": "every scoreline clearing the line",
    "btts": "every scoreline with both teams scoring",
    "team_total": "every scoreline where that side clears the line",
    "asian_handicap": "every scoreline that covers the line, half-stake by half-stake",
    "correct_score": "the single scoreline named",
}


def _is_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _team_total_direction(key) -> str | None:
    """Over or under, for a team-total row.

    `_team_totals` records the side in `selection` for both directions, so the
    direction is only distinguishable from the key.
    """
    text = str(key or "")
    if ".over_" in text:
        return "over"
    if ".under_" in text:
        return "under"
    return None


def _correct_score_of(key) -> tuple[int, int] | None:
    """The (home, away) goals a correct-score row names."""
    tail = str(key or "").rsplit(".", 1)[-1]
    home, _, away = tail.partition("-")
    if home.isdigit() and away.isdigit():
        return int(home), int(away)
    return None


def _matcher(row: dict):
    """(predicate over (home_goals, away_goals), settlement kind) for one market.

    None when the family has no single-grid meaning. Half-time to full-time is
    the one such family: it is a product of two independent halves rather than a
    set of cells, so it is explained through its factors instead.
    """
    family = row.get("family")
    selection = row.get("selection")
    line = row.get("line")

    if family == "result":
        predicate = _RESULT_SIDES.get(selection)
    elif family == "double_chance":
        predicate = _DOUBLE_CHANCE_SIDES.get(selection)
    elif family == "totals" and _is_number(line):
        if selection == "over":
            predicate = lambda i, j: i + j > line  # noqa: E731
        elif selection == "under":
            predicate = lambda i, j: i + j <= line  # noqa: E731
        else:
            predicate = None
    elif family == "btts":
        predicate = {
            "yes": lambda i, j: i > 0 and j > 0,
            "no": lambda i, j: i == 0 or j == 0,
        }.get(selection)
    elif family == "team_total" and _is_number(line):
        direction = _team_total_direction(row.get("key"))
        if direction == "over":
            predicate = (
                (lambda i, _j: i > line) if selection == "home" else (lambda _i, j: j > line)
            )
        elif direction == "under":
            predicate = (
                (lambda i, _j: i <= line) if selection == "home" else (lambda _i, j: j <= line)
            )
        else:
            predicate = None
    elif family == "correct_score":
        scored = _correct_score_of(row.get("key"))
        predicate = None if scored is None else (
            lambda i, j: i == scored[0] and j == scored[1]
        )
    elif family == "asian_handicap" and _is_number(line):
        predicate = None
    else:
        predicate = None

    if predicate is None:
        return None
    return predicate, SETTLED if family == "asian_handicap" else ALL_OR_NOTHING


def _outcome_label(win: float, push: float, lose: float) -> str:
    """Name how a cell settles, including the blends a quarter line creates.

    A quarter line splits each cell across two half-stakes, so a level result
    against -0.25 is half a loss and half a refund. Joining the outcomes that
    have mass names that in one token rather than hiding it.
    """
    hit = [
        name for name, value in zip(_OUTCOMES, (win, push, lose))
        if value > 1e-12
    ]
    return "+".join(hit) if hit else "lose"


def _explain_cells(grid: Grid, predicate) -> list[dict]:
    """The cells that pay the bet, most likely first.

    Losing cells are left out: the settlement triple already carries how often
    the bet loses, and listing 40 scorelines that do not pay it buries the ones
    that do.
    """
    cells: list[dict] = []
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value > 0.0 and predicate(i, j):
                cells.append({
                    "home_goals": i,
                    "away_goals": j,
                    "score": f"{i}-{j}",
                    "probability": round(value, 4),
                })
    cells.sort(key=lambda cell: (-cell["probability"], cell["home_goals"], cell["away_goals"]))
    return cells


def _handicap_cells(grid: Grid, line: float, selection: str) -> list[dict]:
    """Winning and pushing cells for one side of an Asian handicap.

    Away covering is the mirror of the home side's settlement, so its win is the
    home side's lose while both push on the same scorelines.

    Each cell keeps its own per-outcome mass in `parts` because a quarter line
    splits it: a level result against -0.25 has mass in `push` and none in
    `win`, so a share taken against the win total would be meaningless for it.
    """
    shares = _handicap_cell_shares(grid, line)
    cells: list[dict] = []
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value <= 0.0:
                continue
            win, push, lose = shares[i][j]
            if selection == "away":
                win, lose = lose, win
            if win <= 0.0 and push <= 0.0:
                continue
            cells.append({
                "home_goals": i,
                "away_goals": j,
                "score": f"{i}-{j}",
                "probability": round(value, 4),
                "outcome": _outcome_label(win, push, lose),
                "parts": {"win": win, "push": push, "lose": lose},
            })
    cells.sort(key=lambda cell: (-cell["probability"], cell["home_goals"], cell["away_goals"]))
    return cells


def _cell_shares(cells: list[dict]) -> None:
    """Fill in each cell's `share` in place, against the outcome it feeds.

    The share answers "of the times this bet paid out for this outcome, how often
    was it this scoreline?" — so the denominator is the outcome the cell actually
    contributed mass to, and a cell that both pushes and loses is measured
    against its push. A cell that wins and pushes is measured against the win.
    Totals are summed from the cells themselves rather than taken from the
    settlement triple, which is rounded for display, so the shares stay exact and
    still sum to 1.
    """
    totals = {name: 0.0 for name in _OUTCOMES}
    for cell in cells:
        parts = cell.get("parts")
        if not parts:
            continue
        for name in _OUTCOMES:
            totals[name] += parts[name]
    for cell in cells:
        parts = cell.get("parts")
        if not parts:
            cell["share"] = 0.0
            continue
        anchor = max(_OUTCOMES, key=lambda name: parts[name])
        total = totals[anchor]
        cell["share"] = round(parts[anchor] / total, 4) if total > 0.0 else 0.0
    for cell in cells:
        cell.pop("parts", None)


def _settlement_probabilities(raw: dict, row: dict, ft_grid: Grid, ht_grid: Grid | None) -> dict | None:
    """(win, push, lose) for a market, recomputed from its own grid.

    Recomputed rather than copied off the row so the number and the cells below
    it always come from the same arithmetic. The row's own probability is the
    rounded form of this.
    """
    family = row.get("family")
    scope = row.get("scope")
    grid = ht_grid if scope == HALF_TIME else ft_grid

    if family == "ht_ft":
        if not ht_grid or scope != HALF_TO_FULL:
            return None
        ht_side, _, ft_side = str(row.get("selection") or "").partition("_")
        ht = _marginals(ht_grid)
        ft = _marginals(ft_grid)
        win = ht.get(ht_side, 0.0) * ft.get(ft_side, 0.0)
        return {"win": win, "push": 0.0, "lose": 1.0 - win}

    if not grid:
        return None
    if family == "asian_handicap":
        line = row.get("line")
        if not _is_number(line):
            return None
        win, push, lose = handicap_settlement(grid, float(line))
        if row.get("selection") == "away":
            win, lose = lose, win
        return {"win": win, "push": push, "lose": lose}

    matched = _matcher(row)
    if matched is None:
        return None
    predicate = matched[0]
    win = _where(grid, predicate)
    return {"win": win, "push": 0.0, "lose": 1.0 - win}


def market_detail(raw: dict, row: dict, rho=None) -> dict | None:
    """Explain one derived market: how it settles and which scorelines pay it.

    `row` is one entry from `fixture_markets` and `raw` the same dc_v2 raw block
    it was derived from. Returns None when the market cannot be explained — an
    unknown family, or a block with no usable lambdas — so a caller can omit the
    explanation rather than show an empty one.

    The settlement triple and the cell list are both recomputed from the grid,
    so they always agree with each other. They agree with `row["probability"]`
    to within the rounding that number carries.
    """
    if not isinstance(raw, dict) or not isinstance(row, dict):
        return None

    ft_grid, ht_grid = _grids(raw, rho)
    if not ft_grid:
        return None

    family = row.get("family")
    scope = row.get("scope")

    if family == "ht_ft":
        if not ht_grid or scope != HALF_TO_FULL:
            return None
        ht_side, _, ft_side = str(row.get("selection") or "").partition("_")
        if ht_side not in _RESULT_SIDES or ft_side not in _RESULT_SIDES:
            return None
        settlement = _settlement_probabilities(raw, row, ft_grid, ht_grid)
        if settlement is None:
            return None
        detail = {
            "key": row.get("key"),
            "family": family,
            "label": row.get("label"),
            "scope": scope,
            "line": row.get("line"),
            "selection": row.get("selection"),
            "provenance": row.get("provenance"),
            "promotable": bool(row.get("promotable")),
            "settlement": {k: round(v, 4) for k, v in settlement.items()},
            "cells": [],
            "grid_cells": 0,
            "paying_cells": 0,
            "factors": {
                "half_time": _marginals(ht_grid),
                "full_time": _marginals(ft_grid),
                "half_time_side": ht_side,
                "full_time_side": ft_side,
            },
            "method": "the half-time result and the full-time result, treated as independent",
        }
        return detail

    settlement = _settlement_probabilities(raw, row, ft_grid, ht_grid)
    if settlement is None:
        return None

    if family == "asian_handicap":
        grid = ht_grid if scope == HALF_TIME else ft_grid
        cells = _handicap_cells(grid, float(row["line"]), str(row.get("selection")))
    else:
        matched = _matcher(row)
        if matched is None:
            return None
        grid = ht_grid if scope == HALF_TIME else ft_grid
        cells = _explain_cells(grid, matched[0])
        for cell in cells:
            cell["outcome"] = "win"
            cell["parts"] = {"win": cell["probability"], "push": 0.0, "lose": 0.0}

    _cell_shares(cells)

    return {
        "key": row.get("key"),
        "family": family,
        "label": row.get("label"),
        "scope": scope,
        "line": row.get("line"),
        "selection": row.get("selection"),
        "provenance": row.get("provenance"),
        "promotable": bool(row.get("promotable")),
        "settlement": {k: round(v, 4) for k, v in settlement.items()},
        "cells": cells,
        "grid_cells": len(ft_grid) * len(ft_grid),
        "paying_cells": len(cells),
        "method": _METHOD.get(family, "the scorelines that satisfy this market"),
    }

