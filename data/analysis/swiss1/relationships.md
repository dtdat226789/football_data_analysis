# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:09:54+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super League (Switzerland)
- Scope: league `swiss1`

- Matches analysed: **230** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_win_rate | -0.023 | -0.174 | -0.142 |
| home_team_home_conceded_avg | 0.007 | 0.130 | 0.100 |
| points_difference | 0.273 | -0.156 | 0.098 |
| away_team_goals_conceded_last_5 | 0.052 | -0.184 | -0.092 |
| rest_days_difference | -0.027 | 0.134 | 0.076 |
| home_team_points_last_5 | 0.040 | -0.145 | -0.074 |
| away_team_away_goals_avg | -0.137 | 0.052 | -0.069 |
| home_team_home_goals_avg | -0.060 | -0.018 | -0.059 |
| away_points_before_match | -0.140 | 0.070 | -0.058 |
| away_team_goals_scored_last_5 | -0.098 | 0.043 | -0.044 |
| away_team_away_win_rate | -0.166 | 0.119 | -0.042 |
| away_position_before_match | 0.193 | -0.154 | 0.038 |
| home_team_wins_last_5 | 0.038 | -0.092 | -0.038 |
| away_rest_days | -0.041 | -0.008 | -0.037 |
| home_position_before_match | -0.115 | 0.165 | 0.029 |
| home_team_goals_conceded_last_5 | -0.083 | 0.129 | 0.029 |
| away_team_away_conceded_avg | 0.127 | -0.113 | 0.017 |
| home_team_goals_scored_last_5 | 0.054 | -0.080 | -0.016 |
| home_points_before_match | 0.056 | -0.042 | 0.013 |
| home_rest_days | -0.062 | 0.083 | 0.012 |
| away_team_points_last_5 | -0.145 | 0.141 | -0.011 |
| away_team_wins_last_5 | -0.125 | 0.119 | -0.011 |
| position_difference | -0.223 | 0.232 | -0.006 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 35 | 11 | 7 | 17 | 31.4% | 20.0% | 48.6% |
| -4..-2 | 55 | 14 | 19 | 22 | 25.5% | 34.5% | 40.0% |
| -1..1 | 54 | 24 | 9 | 21 | 44.4% | 16.7% | 38.9% |
| 2..4 | 49 | 24 | 14 | 11 | 49.0% | 28.6% | 22.4% |
| >4 | 37 | 20 | 8 | 9 | 54.1% | 21.6% | 24.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 30 | 21 | 6 | 3 | 70.0% | 20.0% | 10.0% |
| -5..-2 | 61 | 31 | 13 | 17 | 50.8% | 21.3% | 27.9% |
| -1..1 | 47 | 14 | 11 | 22 | 29.8% | 23.4% | 46.8% |
| 2..5 | 60 | 20 | 16 | 24 | 33.3% | 26.7% | 40.0% |
| >=6 | 32 | 7 | 11 | 14 | 21.9% | 34.4% | 43.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 14 | 5 | 4 | 5 | 35.7% | 28.6% | 35.7% |
| -1..0 | 49 | 24 | 14 | 11 | 49.0% | 28.6% | 22.4% |
| 0 | 99 | 44 | 16 | 39 | 44.4% | 16.2% | 39.4% |
| 1..2 | 49 | 15 | 17 | 17 | 30.6% | 34.7% | 34.7% |
| >2 | 12 | 2 | 5 | 5 | 16.7% | 41.7% | 41.7% |
| unknown | 7 | 3 | 1 | 3 | 42.9% | 14.3% | 42.9% |
- *7 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.9%** home win (53/140)
- `>= 0.5` tier: **44.4%** home win (40/90)
- Home-win gap (>= split minus < split): **+6.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 140 | 53 | 35 | 52 | 37.9% |
| high | >= 0.5 | 90 | 40 | 22 | 28 | 44.4% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.194 | -1.965 | -3.888 | 8.081 |
| home_points_before_match | 27.473 | 25.140 | 23.012 | 4.461 |
| away_points_before_match | 23.280 | 27.105 | 26.900 | 3.826 |
| position_difference | -1.570 | 0.737 | 1.525 | 3.095 |
| away_position_before_match | 7.495 | 6.386 | 5.688 | 1.807 |
| home_rest_days | 7.633 | 7.464 | 9.039 | 1.575 |
| away_team_points_last_5 | 5.495 | 6.632 | 6.987 | 1.493 |
| home_position_before_match | 5.925 | 7.123 | 7.213 | 1.288 |
| away_rest_days | 7.800 | 7.035 | 8.260 | 1.225 |
| away_team_goals_conceded_last_5 | 8.097 | 7.386 | 6.888 | 1.209 |
| away_team_goals_scored_last_5 | 6.946 | 8.053 | 7.700 | 1.106 |
| home_team_goals_conceded_last_5 | 6.935 | 7.474 | 8.012 | 1.077 |
| rest_days_difference | -0.167 | 0.339 | 0.779 | 0.946 |
| home_team_points_last_5 | 6.613 | 6.439 | 5.912 | 0.700 |
| away_team_wins_last_5 | 1.473 | 1.825 | 1.962 | 0.489 |
| home_team_goals_scored_last_5 | 7.645 | 7.544 | 7.175 | 0.470 |
| away_team_away_conceded_avg | 1.835 | 1.733 | 1.611 | 0.225 |
| away_team_away_goals_avg | 1.280 | 1.498 | 1.487 | 0.218 |
| home_team_home_goals_avg | 1.669 | 1.676 | 1.800 | 0.131 |
| home_team_wins_last_5 | 1.763 | 1.754 | 1.637 | 0.126 |
| home_team_home_conceded_avg | 1.358 | 1.450 | 1.473 | 0.115 |
| away_team_away_win_rate | 0.285 | 0.357 | 0.386 | 0.101 |
| home_team_home_win_rate | 0.396 | 0.359 | 0.375 | 0.037 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\swiss1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\swiss1\charts\relationships_home_win_pct_by_position.png)

