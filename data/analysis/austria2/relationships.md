# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:44:28+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 2. Liga (Austria)
- Scope: league `austria2`

- Matches analysed: **223** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_win_rate | -0.162 | -0.075 | -0.177 |
| away_team_wins_last_5 | -0.136 | -0.101 | -0.175 |
| away_team_points_last_5 | -0.119 | -0.100 | -0.162 |
| away_team_away_goals_avg | -0.067 | -0.126 | -0.139 |
| away_points_before_match | -0.076 | -0.093 | -0.123 |
| away_position_before_match | 0.172 | -0.024 | 0.116 |
| home_points_before_match | 0.027 | -0.178 | -0.104 |
| away_team_away_conceded_avg | 0.178 | -0.088 | 0.077 |
| home_team_home_goals_avg | 0.024 | -0.130 | -0.073 |
| home_position_before_match | -0.068 | 0.164 | 0.062 |
| home_team_points_last_5 | 0.043 | -0.131 | -0.058 |
| home_rest_days | -0.019 | -0.060 | -0.055 |
| home_team_home_conceded_avg | -0.038 | -0.030 | -0.051 |
| home_team_goals_scored_last_5 | 0.026 | -0.099 | -0.050 |
| home_team_home_win_rate | 0.066 | -0.143 | -0.049 |
| away_team_goals_scored_last_5 | 0.043 | -0.115 | -0.047 |
| home_team_wins_last_5 | 0.041 | -0.103 | -0.040 |
| away_rest_days | -0.003 | -0.056 | -0.040 |
| home_team_goals_conceded_last_5 | -0.051 | 0.001 | -0.039 |
| position_difference | -0.170 | 0.133 | -0.038 |
| points_difference | 0.140 | -0.121 | 0.024 |
| away_team_goals_conceded_last_5 | 0.146 | -0.134 | 0.019 |
| rest_days_difference | -0.021 | 0.001 | -0.015 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 33 | 13 | 7 | 13 | 39.4% | 21.2% | 39.4% |
| -4..-2 | 52 | 20 | 10 | 22 | 38.5% | 19.2% | 42.3% |
| -1..1 | 54 | 21 | 16 | 17 | 38.9% | 29.6% | 31.5% |
| 2..4 | 57 | 27 | 15 | 15 | 47.4% | 26.3% | 26.3% |
| >4 | 27 | 11 | 10 | 6 | 40.7% | 37.0% | 22.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 48 | 31 | 9 | 8 | 64.6% | 18.8% | 16.7% |
| -5..-2 | 50 | 20 | 15 | 15 | 40.0% | 30.0% | 30.0% |
| -1..1 | 34 | 13 | 7 | 14 | 38.2% | 20.6% | 41.2% |
| 2..5 | 50 | 18 | 14 | 18 | 36.0% | 28.0% | 36.0% |
| >=6 | 41 | 10 | 13 | 18 | 24.4% | 31.7% | 43.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 20 | 7 | 4 | 9 | 35.0% | 20.0% | 45.0% |
| -1..0 | 42 | 17 | 9 | 16 | 40.5% | 21.4% | 38.1% |
| 0 | 93 | 46 | 26 | 21 | 49.5% | 28.0% | 22.6% |
| 1..2 | 50 | 16 | 16 | 18 | 32.0% | 32.0% | 36.0% |
| >2 | 10 | 5 | 2 | 3 | 50.0% | 20.0% | 30.0% |
| unknown | 8 | 1 | 1 | 6 | 12.5% | 12.5% | 75.0% |
- *8 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.0%** home win (57/150)
- `>= 0.5` tier: **47.9%** home win (35/73)
- Home-win gap (>= split minus < split): **+9.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 150 | 57 | 38 | 55 | 38.0% |
| high | >= 0.5 | 73 | 35 | 20 | 18 | 47.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 21.685 | 16.879 | 17.247 | 4.805 |
| points_difference | 2.511 | -0.897 | -1.753 | 4.264 |
| position_difference | -1.891 | 0.397 | 1.274 | 3.165 |
| away_rest_days | 11.538 | 10.316 | 8.612 | 2.927 |
| home_rest_days | 10.736 | 10.509 | 8.701 | 2.035 |
| home_position_before_match | 7.228 | 8.466 | 8.973 | 1.744 |
| away_position_before_match | 9.120 | 8.069 | 7.699 | 1.421 |
| away_points_before_match | 19.174 | 17.776 | 19.000 | 1.398 |
| away_team_goals_conceded_last_5 | 6.391 | 6.034 | 5.384 | 1.008 |
| rest_days_difference | -0.802 | 0.193 | 0.090 | 0.995 |
| home_team_points_last_5 | 6.489 | 6.293 | 5.534 | 0.955 |
| away_team_points_last_5 | 6.130 | 5.741 | 6.370 | 0.628 |
| home_team_goals_scored_last_5 | 6.076 | 6.276 | 5.658 | 0.618 |
| away_team_goals_scored_last_5 | 6.380 | 5.793 | 5.890 | 0.587 |
| home_team_goals_conceded_last_5 | 5.728 | 6.034 | 6.219 | 0.491 |
| away_team_away_conceded_avg | 1.482 | 1.258 | 1.147 | 0.335 |
| home_team_wins_last_5 | 1.761 | 1.724 | 1.452 | 0.309 |
| away_team_wins_last_5 | 1.630 | 1.483 | 1.740 | 0.257 |
| away_team_away_goals_avg | 1.288 | 1.419 | 1.230 | 0.190 |
| home_team_home_goals_avg | 1.433 | 1.360 | 1.248 | 0.185 |
| home_team_home_win_rate | 0.384 | 0.366 | 0.293 | 0.091 |
| home_team_home_conceded_avg | 1.287 | 1.259 | 1.310 | 0.051 |
| away_team_away_win_rate | 0.298 | 0.337 | 0.345 | 0.046 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\austria2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\austria2\charts\relationships_home_win_pct_by_position.png)

