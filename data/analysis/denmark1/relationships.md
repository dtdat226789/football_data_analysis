# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:47:57+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Superliga (Denmark)
- Scope: league `denmark1`

- Matches analysed: **193** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| rest_days_difference | -0.080 | -0.154 | -0.169 |
| away_position_before_match | 0.230 | -0.093 | 0.125 |
| away_points_before_match | -0.130 | 0.013 | -0.098 |
| position_difference | -0.261 | 0.179 | -0.093 |
| points_difference | 0.250 | -0.177 | 0.086 |
| home_rest_days | -0.020 | -0.077 | -0.068 |
| home_team_home_goals_avg | 0.094 | -0.021 | 0.063 |
| away_team_points_last_5 | -0.173 | 0.131 | -0.054 |
| home_points_before_match | 0.021 | -0.095 | -0.046 |
| away_rest_days | -0.009 | -0.056 | -0.045 |
| home_team_home_conceded_avg | 0.062 | -0.019 | 0.037 |
| home_team_goals_conceded_last_5 | -0.045 | 0.003 | -0.035 |
| away_team_away_goals_avg | -0.021 | 0.077 | 0.035 |
| away_team_goals_conceded_last_5 | 0.101 | -0.078 | 0.030 |
| away_team_away_conceded_avg | 0.103 | -0.083 | 0.028 |
| away_team_wins_last_5 | -0.160 | 0.153 | -0.028 |
| away_team_away_win_rate | -0.126 | 0.118 | -0.024 |
| home_team_points_last_5 | 0.012 | -0.042 | -0.019 |
| home_team_goals_scored_last_5 | 0.072 | -0.105 | -0.011 |
| home_team_wins_last_5 | 0.019 | -0.036 | -0.009 |
| home_position_before_match | -0.100 | 0.136 | 0.009 |
| home_team_home_win_rate | -0.040 | 0.060 | 0.008 |
| away_team_goals_scored_last_5 | -0.165 | 0.201 | 0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 36 | 11 | 8 | 17 | 30.6% | 22.2% | 47.2% |
| -4..-2 | 44 | 18 | 10 | 16 | 40.9% | 22.7% | 36.4% |
| -1..1 | 45 | 17 | 10 | 18 | 37.8% | 22.2% | 40.0% |
| 2..4 | 39 | 19 | 8 | 12 | 48.7% | 20.5% | 30.8% |
| >4 | 29 | 15 | 9 | 5 | 51.7% | 31.0% | 17.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 22 | 12 | 7 | 3 | 54.5% | 31.8% | 13.6% |
| -5..-2 | 47 | 25 | 6 | 16 | 53.2% | 12.8% | 34.0% |
| -1..1 | 50 | 18 | 17 | 15 | 36.0% | 34.0% | 30.0% |
| 2..5 | 54 | 19 | 12 | 23 | 35.2% | 22.2% | 42.6% |
| >=6 | 20 | 6 | 3 | 11 | 30.0% | 15.0% | 55.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 23 | 9 | 5 | 9 | 39.1% | 21.7% | 39.1% |
| -1..0 | 27 | 8 | 5 | 14 | 29.6% | 18.5% | 51.9% |
| 0 | 82 | 41 | 16 | 25 | 50.0% | 19.5% | 30.5% |
| 1..2 | 48 | 21 | 12 | 15 | 43.8% | 25.0% | 31.2% |
| >2 | 7 | 0 | 4 | 3 | 0.0% | 57.1% | 42.9% |
| unknown | 6 | 1 | 3 | 2 | 16.7% | 50.0% | 33.3% |
- *6 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **42.3%** home win (47/111)
- `>= 0.5` tier: **40.2%** home win (33/82)
- Home-win gap (>= split minus < split): **-2.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 111 | 47 | 22 | 42 | 42.3% |
| high | >= 0.5 | 82 | 33 | 23 | 26 | 40.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 19.300 | 25.222 | 22.794 | 5.922 |
| home_points_before_match | 21.025 | 25.022 | 20.059 | 4.963 |
| points_difference | 1.725 | -0.200 | -2.735 | 4.460 |
| position_difference | -0.750 | 0.000 | 1.382 | 2.132 |
| away_team_goals_scored_last_5 | 6.350 | 7.022 | 8.103 | 1.753 |
| home_team_goals_scored_last_5 | 7.375 | 7.467 | 5.765 | 1.702 |
| away_rest_days | 10.329 | 9.048 | 9.197 | 1.281 |
| home_position_before_match | 6.562 | 6.200 | 7.456 | 1.256 |
| away_position_before_match | 7.312 | 6.200 | 6.074 | 1.239 |
| home_rest_days | 10.418 | 9.333 | 9.182 | 1.236 |
| away_team_goals_conceded_last_5 | 7.425 | 6.222 | 6.765 | 1.203 |
| home_team_points_last_5 | 6.362 | 6.689 | 5.544 | 1.145 |
| away_team_points_last_5 | 5.862 | 6.622 | 6.941 | 1.079 |
| home_team_wins_last_5 | 1.762 | 1.867 | 1.485 | 0.381 |
| away_team_wins_last_5 | 1.600 | 1.867 | 1.971 | 0.371 |
| home_team_goals_conceded_last_5 | 7.150 | 6.822 | 6.912 | 0.328 |
| rest_days_difference | 0.089 | 0.286 | -0.015 | 0.301 |
| away_team_away_conceded_avg | 1.738 | 1.477 | 1.500 | 0.260 |
| home_team_home_goals_avg | 1.605 | 1.693 | 1.445 | 0.247 |
| home_team_home_conceded_avg | 1.461 | 1.455 | 1.304 | 0.157 |
| away_team_away_goals_avg | 1.403 | 1.355 | 1.449 | 0.094 |
| home_team_home_win_rate | 0.383 | 0.426 | 0.413 | 0.043 |
| away_team_away_win_rate | 0.328 | 0.332 | 0.364 | 0.036 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\denmark1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\denmark1\charts\relationships_home_win_pct_by_position.png)

