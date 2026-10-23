# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:47:11+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: ChNL (Czech Republic)
- Scope: league `czech2`

- Matches analysed: **240** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_scored_last_5 | -0.136 | 0.028 | -0.100 |
| away_team_points_last_5 | -0.163 | 0.076 | -0.092 |
| home_team_goals_conceded_last_5 | -0.112 | 0.007 | -0.092 |
| home_team_goals_scored_last_5 | -0.032 | -0.075 | -0.076 |
| away_points_before_match | -0.064 | -0.031 | -0.075 |
| away_team_wins_last_5 | -0.143 | 0.092 | -0.065 |
| away_team_away_goals_avg | -0.040 | 0.149 | 0.061 |
| rest_days_difference | -0.048 | -0.031 | -0.061 |
| home_points_before_match | 0.037 | -0.129 | -0.051 |
| position_difference | -0.188 | 0.176 | -0.048 |
| home_team_wins_last_5 | 0.025 | -0.099 | -0.042 |
| home_team_points_last_5 | 0.026 | -0.095 | -0.039 |
| away_position_before_match | 0.154 | -0.150 | 0.036 |
| away_rest_days | 0.023 | 0.021 | 0.033 |
| home_position_before_match | -0.113 | 0.101 | -0.033 |
| points_difference | 0.129 | -0.122 | 0.033 |
| away_team_away_conceded_avg | 0.072 | -0.049 | 0.031 |
| home_team_home_conceded_avg | 0.002 | -0.048 | -0.030 |
| away_team_away_win_rate | -0.075 | 0.136 | 0.023 |
| away_team_goals_conceded_last_5 | 0.073 | -0.064 | 0.022 |
| home_team_home_goals_avg | 0.036 | -0.060 | -0.007 |
| home_team_home_win_rate | 0.025 | -0.029 | 0.003 |
| home_rest_days | -0.003 | 0.005 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 46 | 19 | 8 | 19 | 41.3% | 17.4% | 41.3% |
| -4..-2 | 42 | 14 | 12 | 16 | 33.3% | 28.6% | 38.1% |
| -1..1 | 61 | 25 | 11 | 25 | 41.0% | 18.0% | 41.0% |
| 2..4 | 55 | 37 | 6 | 12 | 67.3% | 10.9% | 21.8% |
| >4 | 36 | 16 | 13 | 7 | 44.4% | 36.1% | 19.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 52 | 30 | 9 | 13 | 57.7% | 17.3% | 25.0% |
| -5..-2 | 53 | 31 | 12 | 10 | 58.5% | 22.6% | 18.9% |
| -1..1 | 26 | 10 | 6 | 10 | 38.5% | 23.1% | 38.5% |
| 2..5 | 58 | 22 | 13 | 23 | 37.9% | 22.4% | 39.7% |
| >=6 | 51 | 18 | 10 | 23 | 35.3% | 19.6% | 45.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 29 | 14 | 6 | 9 | 48.3% | 20.7% | 31.0% |
| -1..0 | 45 | 17 | 12 | 16 | 37.8% | 26.7% | 35.6% |
| 0 | 83 | 40 | 14 | 29 | 48.2% | 16.9% | 34.9% |
| 1..2 | 64 | 35 | 13 | 16 | 54.7% | 20.3% | 25.0% |
| >2 | 10 | 2 | 5 | 3 | 20.0% | 50.0% | 30.0% |
| unknown | 9 | 3 | 0 | 6 | 33.3% | 0.0% | 66.7% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **42.8%** home win (59/138)
- `>= 0.5` tier: **51.0%** home win (52/102)
- Home-win gap (>= split minus < split): **+8.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 138 | 59 | 29 | 50 | 42.8% |
| high | >= 0.5 | 102 | 52 | 21 | 29 | 51.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 22.243 | 20.480 | 17.190 | 5.053 |
| points_difference | 2.090 | -1.440 | -2.772 | 4.862 |
| home_rest_days | 10.560 | 12.980 | 8.986 | 3.994 |
| position_difference | -1.360 | 0.520 | 1.937 | 3.297 |
| rest_days_difference | -0.917 | 2.060 | -0.178 | 2.977 |
| away_rest_days | 11.519 | 10.920 | 9.164 | 2.354 |
| away_points_before_match | 20.153 | 21.920 | 19.962 | 1.958 |
| away_position_before_match | 9.243 | 8.540 | 7.506 | 1.737 |
| home_position_before_match | 7.883 | 9.060 | 9.443 | 1.560 |
| home_team_points_last_5 | 6.423 | 6.740 | 5.658 | 1.082 |
| away_team_points_last_5 | 5.919 | 6.500 | 6.747 | 0.828 |
| home_team_goals_scored_last_5 | 5.901 | 6.340 | 5.785 | 0.555 |
| away_team_goals_scored_last_5 | 5.856 | 6.220 | 6.342 | 0.486 |
| home_team_goals_conceded_last_5 | 5.946 | 5.940 | 6.405 | 0.465 |
| home_team_wins_last_5 | 1.829 | 1.940 | 1.570 | 0.370 |
| home_team_home_goals_avg | 1.484 | 1.689 | 1.352 | 0.338 |
| away_team_wins_last_5 | 1.658 | 1.760 | 1.975 | 0.317 |
| home_team_home_conceded_avg | 1.132 | 1.348 | 1.060 | 0.287 |
| away_team_away_goals_avg | 1.055 | 1.224 | 1.195 | 0.169 |
| away_team_goals_conceded_last_5 | 6.027 | 5.920 | 5.861 | 0.166 |
| away_team_away_conceded_avg | 1.548 | 1.482 | 1.398 | 0.150 |
| away_team_away_win_rate | 0.315 | 0.377 | 0.357 | 0.062 |
| home_team_home_win_rate | 0.436 | 0.457 | 0.396 | 0.061 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\czech2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\czech2\charts\relationships_home_win_pct_by_position.png)

