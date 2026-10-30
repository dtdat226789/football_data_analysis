# Relationships Analysis
- Report: `relationships`
- Generated: 2026-10-30T04:04:07+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Ekstraklasa (Poland)
- Scope: league `poland1`

- Matches analysed: **1770** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| points_difference | 0.195 | -0.082 | 0.095 |
| position_difference | -0.169 | 0.084 | -0.073 |
| away_team_away_win_rate | -0.092 | -0.001 | -0.071 |
| away_team_away_conceded_avg | 0.092 | -0.002 | 0.068 |
| away_position_before_match | 0.116 | -0.031 | 0.067 |
| away_team_goals_conceded_last_5 | 0.070 | -0.007 | 0.049 |
| rest_days_difference | 0.046 | 0.018 | 0.046 |
| away_points_before_match | -0.062 | 0.007 | -0.043 |
| away_team_points_last_5 | -0.067 | 0.022 | -0.037 |
| home_position_before_match | -0.123 | 0.088 | -0.036 |
| home_team_home_goals_avg | 0.097 | -0.064 | 0.031 |
| away_team_wins_last_5 | -0.066 | 0.029 | -0.031 |
| home_team_goals_conceded_last_5 | -0.026 | 0.063 | 0.021 |
| home_points_before_match | 0.067 | -0.047 | 0.020 |
| home_team_home_win_rate | 0.090 | -0.075 | 0.019 |
| away_team_away_goals_avg | -0.023 | 0.001 | -0.017 |
| away_team_goals_scored_last_5 | -0.032 | 0.015 | -0.015 |
| home_team_goals_scored_last_5 | 0.068 | -0.057 | 0.014 |
| home_team_home_conceded_avg | -0.019 | 0.043 | 0.014 |
| away_rest_days | -0.027 | 0.016 | -0.010 |
| home_team_points_last_5 | 0.066 | -0.067 | 0.006 |
| home_rest_days | -0.010 | 0.022 | 0.006 |
| home_team_wins_last_5 | 0.067 | -0.070 | 0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 263 | 96 | 71 | 96 | 36.5% | 27.0% | 36.5% |
| -4..-2 | 387 | 159 | 113 | 115 | 41.1% | 29.2% | 29.7% |
| -1..1 | 533 | 225 | 147 | 161 | 42.2% | 27.6% | 30.2% |
| 2..4 | 383 | 177 | 102 | 104 | 46.2% | 26.6% | 27.2% |
| >4 | 204 | 113 | 53 | 38 | 55.4% | 26.0% | 18.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 405 | 216 | 102 | 87 | 53.3% | 25.2% | 21.5% |
| -5..-2 | 323 | 145 | 84 | 94 | 44.9% | 26.0% | 29.1% |
| -1..1 | 259 | 108 | 74 | 77 | 41.7% | 28.6% | 29.7% |
| 2..5 | 351 | 147 | 105 | 99 | 41.9% | 29.9% | 28.2% |
| >=6 | 432 | 154 | 121 | 157 | 35.6% | 28.0% | 36.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 303 | 128 | 88 | 87 | 42.2% | 29.0% | 28.7% |
| -1..0 | 391 | 166 | 102 | 123 | 42.5% | 26.1% | 31.5% |
| 0 | 331 | 141 | 104 | 86 | 42.6% | 31.4% | 26.0% |
| 1..2 | 583 | 260 | 154 | 169 | 44.6% | 26.4% | 29.0% |
| >2 | 108 | 51 | 23 | 34 | 47.2% | 21.3% | 31.5% |
| unknown | 54 | 24 | 15 | 15 | 44.4% | 27.8% | 27.8% |
- *54 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **41.2%** home win (432/1049)
- `>= 0.5` tier: **46.9%** home win (338/721)
- Home-win gap (>= split minus < split): **+5.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 1049 | 432 | 283 | 334 | 41.2% |
| high | >= 0.5 | 721 | 338 | 203 | 180 | 46.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.471 | -0.916 | -2.261 | 3.732 |
| position_difference | -0.877 | 0.603 | 1.531 | 2.408 |
| away_points_before_match | 21.070 | 22.998 | 23.385 | 2.315 |
| home_points_before_match | 22.542 | 22.082 | 21.125 | 1.417 |
| away_position_before_match | 10.217 | 9.323 | 8.932 | 1.285 |
| home_position_before_match | 9.340 | 9.926 | 10.463 | 1.123 |
| away_rest_days | 8.975 | 9.688 | 9.430 | 0.713 |
| away_team_points_last_5 | 6.017 | 6.601 | 6.535 | 0.584 |
| home_team_points_last_5 | 6.256 | 6.212 | 5.681 | 0.575 |
| home_team_goals_scored_last_5 | 6.013 | 6.047 | 5.494 | 0.553 |
| away_team_goals_scored_last_5 | 5.870 | 6.368 | 6.091 | 0.498 |
| away_team_goals_conceded_last_5 | 6.081 | 5.772 | 5.681 | 0.400 |
| home_rest_days | 9.121 | 9.514 | 9.370 | 0.393 |
| home_team_goals_conceded_last_5 | 5.894 | 6.163 | 6.232 | 0.338 |
| rest_days_difference | 0.146 | -0.174 | -0.064 | 0.320 |
| home_team_wins_last_5 | 1.677 | 1.667 | 1.457 | 0.219 |
| away_team_wins_last_5 | 1.582 | 1.786 | 1.772 | 0.204 |
| home_team_home_goals_avg | 1.446 | 1.386 | 1.307 | 0.139 |
| away_team_away_conceded_avg | 1.439 | 1.369 | 1.343 | 0.095 |
| home_team_home_win_rate | 0.432 | 0.419 | 0.378 | 0.054 |
| away_team_away_win_rate | 0.253 | 0.282 | 0.293 | 0.040 |
| away_team_away_goals_avg | 1.081 | 1.098 | 1.118 | 0.037 |
| home_team_home_conceded_avg | 1.085 | 1.108 | 1.118 | 0.034 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](charts/relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](charts/relationships_home_win_pct_by_position.png)

