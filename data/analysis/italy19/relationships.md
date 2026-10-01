# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:57:15+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Primavera 1 (Italy)
- Scope: league `italy19`

- Matches analysed: **382** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.110 | 0.067 | 0.120 |
| away_team_away_win_rate | -0.155 | -0.004 | -0.115 |
| away_team_goals_conceded_last_5 | 0.103 | 0.051 | 0.105 |
| home_points_before_match | 0.096 | 0.018 | 0.080 |
| away_points_before_match | 0.023 | 0.086 | 0.070 |
| away_team_goals_scored_last_5 | 0.029 | 0.067 | 0.063 |
| home_team_points_last_5 | 0.074 | 0.006 | 0.058 |
| home_team_home_goals_avg | 0.087 | -0.017 | 0.052 |
| home_team_home_win_rate | 0.022 | 0.047 | 0.045 |
| home_team_wins_last_5 | 0.055 | 0.006 | 0.043 |
| away_team_wins_last_5 | -0.072 | 0.015 | -0.043 |
| away_team_points_last_5 | -0.084 | 0.034 | -0.040 |
| home_position_before_match | -0.094 | 0.048 | -0.038 |
| home_rest_days | 0.009 | 0.034 | 0.027 |
| away_team_away_goals_avg | -0.054 | 0.105 | 0.026 |
| away_rest_days | 0.016 | 0.022 | 0.025 |
| home_team_goals_conceded_last_5 | -0.060 | 0.037 | -0.020 |
| position_difference | -0.113 | 0.104 | -0.017 |
| home_team_home_conceded_avg | -0.021 | -0.003 | -0.017 |
| points_difference | 0.123 | -0.118 | 0.016 |
| away_position_before_match | 0.063 | -0.095 | -0.013 |
| home_team_goals_scored_last_5 | 0.052 | -0.050 | 0.007 |
| rest_days_difference | -0.022 | 0.034 | 0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 56 | 26 | 14 | 16 | 46.4% | 25.0% | 28.6% |
| -4..-2 | 76 | 24 | 25 | 27 | 31.6% | 32.9% | 35.5% |
| -1..1 | 132 | 49 | 39 | 44 | 37.1% | 29.5% | 33.3% |
| 2..4 | 71 | 27 | 27 | 17 | 38.0% | 38.0% | 23.9% |
| >4 | 47 | 26 | 12 | 9 | 55.3% | 25.5% | 19.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 91 | 38 | 33 | 20 | 41.8% | 36.3% | 22.0% |
| -5..-2 | 74 | 40 | 16 | 18 | 54.1% | 21.6% | 24.3% |
| -1..1 | 48 | 21 | 12 | 15 | 43.8% | 25.0% | 31.2% |
| 2..5 | 67 | 19 | 26 | 22 | 28.4% | 38.8% | 32.8% |
| >=6 | 102 | 34 | 30 | 38 | 33.3% | 29.4% | 37.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 34 | 11 | 11 | 12 | 32.4% | 32.4% | 35.3% |
| -1..0 | 93 | 42 | 30 | 21 | 45.2% | 32.3% | 22.6% |
| 0 | 135 | 60 | 37 | 38 | 44.4% | 27.4% | 28.1% |
| 1..2 | 110 | 36 | 35 | 39 | 32.7% | 31.8% | 35.5% |
| >2 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 10 | 3 | 4 | 3 | 30.0% | 40.0% | 30.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.1%** home win (102/268)
- `>= 0.5` tier: **43.9%** home win (50/114)
- Home-win gap (>= split minus < split): **+5.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 268 | 102 | 83 | 83 | 38.1% |
| high | >= 0.5 | 114 | 50 | 34 | 30 | 43.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.276 | -0.120 | -2.575 | 3.852 |
| home_points_before_match | 25.599 | 26.034 | 23.274 | 2.760 |
| position_difference | -0.901 | 0.179 | 1.823 | 2.724 |
| away_points_before_match | 24.322 | 26.154 | 25.850 | 1.831 |
| home_position_before_match | 10.388 | 10.581 | 12.062 | 1.674 |
| away_position_before_match | 11.289 | 10.402 | 10.239 | 1.051 |
| home_team_points_last_5 | 6.138 | 6.504 | 5.690 | 0.814 |
| away_team_goals_scored_last_5 | 6.112 | 6.769 | 6.088 | 0.681 |
| away_team_points_last_5 | 6.000 | 6.607 | 6.442 | 0.607 |
| home_team_goals_conceded_last_5 | 6.046 | 6.427 | 6.637 | 0.591 |
| home_team_goals_scored_last_5 | 6.434 | 6.410 | 5.850 | 0.585 |
| away_team_goals_conceded_last_5 | 6.217 | 6.402 | 5.956 | 0.446 |
| home_team_wins_last_5 | 1.546 | 1.709 | 1.451 | 0.258 |
| rest_days_difference | -0.154 | -0.062 | 0.018 | 0.173 |
| away_team_wins_last_5 | 1.546 | 1.709 | 1.664 | 0.163 |
| home_team_home_goals_avg | 1.401 | 1.336 | 1.252 | 0.149 |
| away_team_away_goals_avg | 1.063 | 1.184 | 1.177 | 0.121 |
| home_rest_days | 7.255 | 7.310 | 7.373 | 0.118 |
| away_team_away_win_rate | 0.261 | 0.331 | 0.297 | 0.071 |
| away_team_away_conceded_avg | 1.389 | 1.353 | 1.328 | 0.061 |
| away_rest_days | 7.409 | 7.372 | 7.355 | 0.055 |
| home_team_home_conceded_avg | 1.114 | 1.162 | 1.131 | 0.048 |
| home_team_home_win_rate | 0.382 | 0.387 | 0.374 | 0.013 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\italy19\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\italy19\charts\relationships_home_win_pct_by_position.png)

