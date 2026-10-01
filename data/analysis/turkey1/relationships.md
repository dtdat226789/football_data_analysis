# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:10:37+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super Lig (Turkey)
- Scope: league `turkey1`

- Matches analysed: **306** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.313 | -0.062 | 0.188 |
| home_team_points_last_5 | 0.296 | -0.067 | 0.172 |
| home_points_before_match | 0.294 | -0.066 | 0.171 |
| home_team_home_goals_avg | 0.259 | -0.032 | 0.169 |
| home_team_wins_last_5 | 0.295 | -0.074 | 0.166 |
| home_position_before_match | -0.263 | 0.045 | -0.162 |
| home_team_home_win_rate | 0.227 | -0.032 | 0.145 |
| away_points_before_match | 0.057 | 0.085 | 0.103 |
| away_position_before_match | 0.140 | -0.281 | -0.098 |
| away_team_goals_scored_last_5 | -0.061 | 0.198 | 0.097 |
| away_team_points_last_5 | -0.048 | 0.176 | 0.091 |
| points_difference | 0.279 | -0.180 | 0.078 |
| away_team_wins_last_5 | -0.086 | 0.162 | 0.052 |
| home_rest_days | -0.069 | 0.002 | -0.050 |
| position_difference | -0.292 | 0.235 | -0.048 |
| away_rest_days | -0.035 | -0.026 | -0.044 |
| away_team_away_goals_avg | -0.098 | 0.162 | 0.044 |
| home_team_goals_conceded_last_5 | -0.058 | 0.009 | -0.036 |
| away_team_away_win_rate | -0.110 | 0.161 | 0.034 |
| rest_days_difference | -0.091 | 0.078 | -0.012 |
| home_team_home_conceded_avg | -0.098 | 0.090 | -0.008 |
| away_team_goals_conceded_last_5 | 0.059 | -0.071 | -0.007 |
| away_team_away_conceded_avg | 0.085 | -0.092 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 45 | 11 | 11 | 23 | 24.4% | 24.4% | 51.1% |
| -4..-2 | 76 | 26 | 20 | 30 | 34.2% | 26.3% | 39.5% |
| -1..1 | 80 | 32 | 28 | 20 | 40.0% | 35.0% | 25.0% |
| 2..4 | 55 | 29 | 14 | 12 | 52.7% | 25.5% | 21.8% |
| >4 | 50 | 31 | 16 | 3 | 62.0% | 32.0% | 6.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 77 | 48 | 19 | 10 | 62.3% | 24.7% | 13.0% |
| -5..-2 | 48 | 19 | 24 | 5 | 39.6% | 50.0% | 10.4% |
| -1..1 | 45 | 18 | 15 | 12 | 40.0% | 33.3% | 26.7% |
| 2..5 | 58 | 23 | 17 | 18 | 39.7% | 29.3% | 31.0% |
| >=6 | 78 | 21 | 14 | 43 | 26.9% | 17.9% | 55.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 43 | 22 | 12 | 9 | 51.2% | 27.9% | 20.9% |
| -1..0 | 57 | 26 | 14 | 17 | 45.6% | 24.6% | 29.8% |
| 0 | 102 | 50 | 27 | 25 | 49.0% | 26.5% | 24.5% |
| 1..2 | 84 | 26 | 29 | 29 | 31.0% | 34.5% | 34.5% |
| >2 | 9 | 0 | 4 | 5 | 0.0% | 44.4% | 55.6% |
| unknown | 11 | 5 | 3 | 3 | 45.5% | 27.3% | 27.3% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **40.4%** home win (84/208)
- `>= 0.5` tier: **45.9%** home win (45/98)
- Home-win gap (>= split minus < split): **+5.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 208 | 84 | 55 | 69 | 40.4% |
| high | >= 0.5 | 98 | 45 | 34 | 19 | 45.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.163 | 2.348 | -7.398 | 10.561 |
| home_points_before_match | 25.194 | 22.573 | 17.364 | 7.830 |
| position_difference | -2.078 | -0.831 | 4.216 | 6.293 |
| away_points_before_match | 22.031 | 20.225 | 24.761 | 4.537 |
| away_position_before_match | 11.078 | 9.966 | 7.034 | 4.043 |
| home_position_before_match | 9.000 | 9.135 | 11.250 | 2.250 |
| away_team_goals_scored_last_5 | 5.225 | 6.000 | 7.148 | 1.923 |
| home_team_goals_scored_last_5 | 6.682 | 6.045 | 4.795 | 1.887 |
| home_team_points_last_5 | 6.698 | 6.449 | 4.909 | 1.789 |
| away_team_points_last_5 | 5.519 | 6.258 | 7.136 | 1.617 |
| away_team_goals_conceded_last_5 | 5.938 | 6.315 | 5.386 | 0.928 |
| rest_days_difference | -0.484 | 0.070 | 0.188 | 0.672 |
| home_team_wins_last_5 | 1.791 | 1.730 | 1.159 | 0.632 |
| away_team_wins_last_5 | 1.333 | 1.640 | 1.955 | 0.621 |
| home_rest_days | 8.024 | 8.598 | 8.576 | 0.574 |
| away_team_away_goals_avg | 1.034 | 1.238 | 1.342 | 0.308 |
| home_team_goals_conceded_last_5 | 5.930 | 6.213 | 6.125 | 0.283 |
| home_team_home_goals_avg | 1.293 | 1.244 | 1.018 | 0.275 |
| away_team_away_conceded_avg | 1.249 | 1.297 | 1.092 | 0.204 |
| away_rest_days | 8.504 | 8.529 | 8.388 | 0.141 |
| home_team_home_conceded_avg | 1.137 | 1.218 | 1.264 | 0.128 |
| away_team_away_win_rate | 0.256 | 0.309 | 0.378 | 0.121 |
| home_team_home_win_rate | 0.383 | 0.379 | 0.301 | 0.081 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\turkey1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\turkey1\charts\relationships_home_win_pct_by_position.png)

