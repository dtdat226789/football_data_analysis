# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:42:36+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Primera RFEF - Group 1 (Spain)
- Scope: league `primera1`

- Matches analysed: **438** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_scored_last_5 | 0.046 | 0.088 | 0.092 |
| position_difference | -0.015 | 0.150 | 0.091 |
| away_team_away_conceded_avg | 0.122 | 0.006 | 0.090 |
| away_team_away_goals_avg | 0.029 | 0.077 | 0.073 |
| points_difference | 0.049 | -0.146 | -0.064 |
| home_team_home_conceded_avg | 0.050 | 0.040 | 0.062 |
| home_position_before_match | 0.004 | 0.087 | 0.062 |
| away_position_before_match | 0.025 | -0.114 | -0.060 |
| home_team_home_goals_avg | 0.071 | 0.008 | 0.056 |
| away_team_wins_last_5 | 0.013 | 0.068 | 0.055 |
| away_team_goals_conceded_last_5 | 0.091 | -0.015 | 0.055 |
| away_points_before_match | -0.009 | 0.088 | 0.053 |
| away_team_away_win_rate | -0.029 | 0.100 | 0.048 |
| away_team_points_last_5 | -0.029 | 0.087 | 0.039 |
| home_rest_days | -0.010 | -0.046 | -0.038 |
| away_rest_days | -0.015 | -0.034 | -0.033 |
| home_team_goals_scored_last_5 | -0.003 | -0.027 | -0.021 |
| home_team_wins_last_5 | 0.033 | -0.006 | 0.019 |
| home_points_before_match | 0.018 | 0.008 | 0.018 |
| home_team_home_win_rate | -0.013 | 0.034 | 0.014 |
| home_team_goals_conceded_last_5 | -0.010 | -0.007 | -0.012 |
| home_team_points_last_5 | 0.029 | -0.021 | 0.006 |
| rest_days_difference | 0.005 | -0.012 | -0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 63 | 21 | 18 | 24 | 33.3% | 28.6% | 38.1% |
| -4..-2 | 100 | 45 | 25 | 30 | 45.0% | 25.0% | 30.0% |
| -1..1 | 148 | 74 | 42 | 32 | 50.0% | 28.4% | 21.6% |
| 2..4 | 78 | 42 | 22 | 14 | 53.8% | 28.2% | 17.9% |
| >4 | 49 | 20 | 15 | 14 | 40.8% | 30.6% | 28.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 104 | 47 | 34 | 23 | 45.2% | 32.7% | 22.1% |
| -5..-2 | 73 | 43 | 16 | 14 | 58.9% | 21.9% | 19.2% |
| -1..1 | 67 | 28 | 27 | 12 | 41.8% | 40.3% | 17.9% |
| 2..5 | 73 | 31 | 18 | 24 | 42.5% | 24.7% | 32.9% |
| >=6 | 121 | 53 | 27 | 41 | 43.8% | 22.3% | 33.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 29 | 11 | 13 | 5 | 37.9% | 44.8% | 17.2% |
| -1..0 | 100 | 47 | 24 | 29 | 47.0% | 24.0% | 29.0% |
| 0 | 164 | 76 | 44 | 44 | 46.3% | 26.8% | 26.8% |
| 1..2 | 115 | 53 | 34 | 28 | 46.1% | 29.6% | 24.3% |
| >2 | 9 | 6 | 1 | 2 | 66.7% | 11.1% | 22.2% |
| unknown | 21 | 9 | 6 | 6 | 42.9% | 28.6% | 28.6% |
- *21 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **53.8%** home win (42/78)
- `>= 0.5` tier: **44.4%** home win (160/360)
- Home-win gap (>= split minus < split): **-9.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 78 | 42 | 17 | 19 | 53.8% |
| high | >= 0.5 | 360 | 160 | 105 | 95 | 44.4% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 21.772 | 25.697 | 24.377 | 3.924 |
| home_points_before_match | 22.470 | 25.762 | 22.140 | 3.622 |
| points_difference | 0.698 | 0.066 | -2.237 | 2.935 |
| position_difference | 0.045 | -0.475 | 2.360 | 2.835 |
| home_position_before_match | 11.510 | 10.156 | 12.368 | 2.213 |
| away_position_before_match | 11.465 | 10.631 | 10.009 | 1.457 |
| home_team_goals_scored_last_5 | 4.960 | 5.648 | 4.816 | 0.832 |
| away_team_points_last_5 | 5.693 | 6.344 | 6.404 | 0.710 |
| home_team_points_last_5 | 5.658 | 6.057 | 5.456 | 0.601 |
| away_team_goals_conceded_last_5 | 5.337 | 5.033 | 4.974 | 0.363 |
| away_team_goals_scored_last_5 | 5.252 | 5.320 | 5.596 | 0.344 |
| home_rest_days | 7.192 | 6.905 | 7.111 | 0.287 |
| away_team_wins_last_5 | 2.723 | 2.967 | 2.842 | 0.244 |
| away_rest_days | 7.218 | 7.000 | 7.120 | 0.218 |
| home_team_wins_last_5 | 2.708 | 2.811 | 2.596 | 0.215 |
| home_team_goals_conceded_last_5 | 5.223 | 5.385 | 5.325 | 0.162 |
| home_team_home_goals_avg | 1.185 | 1.279 | 1.118 | 0.161 |
| away_team_away_conceded_avg | 1.297 | 1.175 | 1.143 | 0.155 |
| rest_days_difference | -0.026 | -0.095 | -0.009 | 0.086 |
| away_team_away_win_rate | 0.444 | 0.504 | 0.499 | 0.060 |
| home_team_home_win_rate | 0.647 | 0.698 | 0.672 | 0.051 |
| away_team_away_goals_avg | 0.883 | 0.917 | 0.916 | 0.034 |
| home_team_home_conceded_avg | 0.900 | 0.889 | 0.900 | 0.011 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\primera1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\primera1\charts\relationships_home_win_pct_by_position.png)

