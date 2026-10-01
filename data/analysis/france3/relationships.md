# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:50:34+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

- Matches analysed: **303** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_position_before_match | 0.193 | -0.015 | 0.130 |
| points_difference | 0.190 | -0.101 | 0.065 |
| away_team_away_win_rate | -0.131 | 0.043 | -0.064 |
| position_difference | -0.202 | 0.117 | -0.062 |
| home_points_before_match | 0.097 | -0.022 | 0.054 |
| away_team_wins_last_5 | -0.068 | -0.002 | -0.051 |
| away_team_away_goals_avg | -0.089 | 0.023 | -0.048 |
| home_position_before_match | -0.066 | 0.129 | 0.046 |
| away_team_goals_scored_last_5 | -0.079 | 0.021 | -0.043 |
| home_team_goals_conceded_last_5 | -0.088 | 0.033 | -0.040 |
| home_team_goals_scored_last_5 | 0.052 | -0.103 | -0.037 |
| home_team_home_conceded_avg | -0.062 | 0.011 | -0.037 |
| home_team_home_goals_avg | 0.014 | -0.064 | -0.036 |
| away_rest_days | 0.022 | 0.027 | 0.036 |
| away_team_away_conceded_avg | -0.009 | -0.039 | -0.035 |
| away_team_goals_conceded_last_5 | -0.003 | -0.034 | -0.027 |
| home_rest_days | 0.099 | -0.068 | 0.024 |
| away_team_points_last_5 | -0.071 | 0.043 | -0.020 |
| home_team_wins_last_5 | 0.127 | -0.147 | -0.014 |
| away_points_before_match | -0.039 | 0.050 | 0.008 |
| home_team_home_win_rate | 0.040 | -0.051 | -0.008 |
| rest_days_difference | 0.051 | -0.046 | 0.004 |
| home_team_points_last_5 | 0.125 | -0.128 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 43 | 11 | 11 | 21 | 25.6% | 25.6% | 48.8% |
| -4..-2 | 65 | 21 | 23 | 21 | 32.3% | 35.4% | 32.3% |
| -1..1 | 89 | 31 | 31 | 27 | 34.8% | 34.8% | 30.3% |
| 2..4 | 57 | 24 | 20 | 13 | 42.1% | 35.1% | 22.8% |
| >4 | 49 | 22 | 15 | 12 | 44.9% | 30.6% | 24.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 77 | 36 | 23 | 18 | 46.8% | 29.9% | 23.4% |
| -5..-2 | 59 | 24 | 25 | 10 | 40.7% | 42.4% | 16.9% |
| -1..1 | 34 | 8 | 13 | 13 | 23.5% | 38.2% | 38.2% |
| 2..5 | 51 | 20 | 13 | 18 | 39.2% | 25.5% | 35.3% |
| >=6 | 82 | 21 | 26 | 35 | 25.6% | 31.7% | 42.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 18 | 4 | 9 | 5 | 22.2% | 50.0% | 27.8% |
| -1..0 | 11 | 2 | 5 | 4 | 18.2% | 45.5% | 36.4% |
| 0 | 201 | 80 | 60 | 61 | 39.8% | 29.9% | 30.3% |
| 1..2 | 11 | 4 | 3 | 4 | 36.4% | 27.3% | 36.4% |
| >2 | 22 | 8 | 8 | 6 | 36.4% | 36.4% | 27.3% |
| unknown | 40 | 11 | 15 | 14 | 27.5% | 37.5% | 35.0% |
- *40 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **34.0%** home win (67/197)
- `>= 0.5` tier: **39.6%** home win (42/106)
- Home-win gap (>= split minus < split): **+5.6 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 197 | 67 | 67 | 63 | 34.0% |
| high | >= 0.5 | 106 | 42 | 33 | 31 | 39.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.917 | 0.530 | -2.819 | 4.737 |
| position_difference | -2.028 | 0.730 | 2.447 | 4.474 |
| home_points_before_match | 20.174 | 19.900 | 17.138 | 3.036 |
| home_position_before_match | 9.972 | 11.580 | 12.213 | 2.240 |
| away_position_before_match | 12.000 | 10.850 | 9.766 | 2.234 |
| away_points_before_match | 18.257 | 19.370 | 19.957 | 1.701 |
| home_team_points_last_5 | 6.385 | 5.860 | 4.979 | 1.407 |
| home_rest_days | 10.340 | 9.258 | 8.952 | 1.388 |
| rest_days_difference | 0.571 | -0.282 | 0.050 | 0.854 |
| home_team_goals_scored_last_5 | 5.523 | 5.290 | 4.691 | 0.831 |
| away_team_goals_conceded_last_5 | 5.312 | 4.750 | 5.170 | 0.562 |
| away_team_goals_scored_last_5 | 5.073 | 5.000 | 5.521 | 0.521 |
| home_team_wins_last_5 | 1.651 | 1.500 | 1.181 | 0.471 |
| away_team_points_last_5 | 5.615 | 5.710 | 6.000 | 0.385 |
| home_team_goals_conceded_last_5 | 4.991 | 5.040 | 5.372 | 0.382 |
| away_rest_days | 9.426 | 9.640 | 9.368 | 0.273 |
| away_team_away_conceded_avg | 1.188 | 1.137 | 1.117 | 0.072 |
| home_team_home_goals_avg | 1.185 | 1.130 | 1.121 | 0.064 |
| away_team_wins_last_5 | 1.440 | 1.470 | 1.500 | 0.060 |
| away_team_away_goals_avg | 0.940 | 0.975 | 0.995 | 0.055 |
| away_team_away_win_rate | 0.237 | 0.261 | 0.287 | 0.051 |
| home_team_home_conceded_avg | 0.931 | 0.972 | 0.973 | 0.042 |
| home_team_home_win_rate | 0.347 | 0.322 | 0.323 | 0.025 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\france3\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\france3\charts\relationships_home_win_pct_by_position.png)

