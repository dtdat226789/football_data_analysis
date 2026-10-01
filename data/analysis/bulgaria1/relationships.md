# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:46:02+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: efbet League (Bulgaria)
- Scope: league `bulgaria1`

- Matches analysed: **294** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| rest_days_difference | -0.082 | -0.066 | -0.112 |
| home_team_goals_scored_last_5 | 0.174 | -0.061 | 0.089 |
| home_team_wins_last_5 | 0.171 | -0.063 | 0.086 |
| away_team_goals_conceded_last_5 | -0.019 | -0.093 | -0.085 |
| home_team_points_last_5 | 0.159 | -0.067 | 0.073 |
| away_team_away_win_rate | -0.105 | 0.197 | 0.066 |
| home_team_home_goals_avg | 0.106 | -0.047 | 0.047 |
| points_difference | 0.219 | -0.288 | -0.046 |
| away_team_away_conceded_avg | 0.066 | -0.128 | -0.045 |
| away_team_wins_last_5 | -0.055 | 0.112 | 0.041 |
| home_team_goals_conceded_last_5 | -0.140 | 0.091 | -0.041 |
| home_team_home_win_rate | 0.124 | -0.074 | 0.041 |
| home_team_home_conceded_avg | -0.151 | 0.104 | -0.040 |
| away_team_away_goals_avg | -0.145 | 0.101 | -0.037 |
| away_rest_days | 0.028 | 0.020 | 0.036 |
| away_team_points_last_5 | -0.065 | 0.114 | 0.035 |
| home_points_before_match | 0.053 | -0.099 | -0.033 |
| home_position_before_match | -0.180 | 0.159 | -0.021 |
| away_team_goals_scored_last_5 | -0.082 | 0.110 | 0.019 |
| away_position_before_match | 0.129 | -0.153 | -0.015 |
| home_rest_days | 0.009 | 0.006 | 0.012 |
| position_difference | -0.238 | 0.240 | -0.005 |
| away_points_before_match | -0.093 | 0.092 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 47 | 10 | 14 | 23 | 21.3% | 29.8% | 48.9% |
| -4..-2 | 67 | 22 | 20 | 25 | 32.8% | 29.9% | 37.3% |
| -1..1 | 75 | 40 | 23 | 12 | 53.3% | 30.7% | 16.0% |
| 2..4 | 60 | 25 | 17 | 18 | 41.7% | 28.3% | 30.0% |
| >4 | 45 | 28 | 8 | 9 | 62.2% | 17.8% | 20.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 51 | 32 | 11 | 8 | 62.7% | 21.6% | 15.7% |
| -5..-2 | 73 | 37 | 22 | 14 | 50.7% | 30.1% | 19.2% |
| -1..1 | 56 | 24 | 20 | 12 | 42.9% | 35.7% | 21.4% |
| 2..5 | 59 | 21 | 15 | 23 | 35.6% | 25.4% | 39.0% |
| >=6 | 55 | 11 | 14 | 30 | 20.0% | 25.5% | 54.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 34 | 13 | 13 | 8 | 38.2% | 38.2% | 23.5% |
| -1..0 | 75 | 34 | 17 | 24 | 45.3% | 22.7% | 32.0% |
| 0 | 86 | 41 | 18 | 27 | 47.7% | 20.9% | 31.4% |
| 1..2 | 78 | 26 | 27 | 25 | 33.3% | 34.6% | 32.1% |
| >2 | 12 | 6 | 3 | 3 | 50.0% | 25.0% | 25.0% |
| unknown | 9 | 5 | 4 | 0 | 55.6% | 44.4% | 0.0% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **36.9%** home win (73/198)
- `>= 0.5` tier: **54.2%** home win (52/96)
- Home-win gap (>= split minus < split): **+17.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 198 | 73 | 58 | 67 | 36.9% |
| high | >= 0.5 | 96 | 52 | 24 | 20 | 54.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.920 | -0.390 | -5.379 | 9.299 |
| away_points_before_match | 22.888 | 21.780 | 27.402 | 5.622 |
| home_points_before_match | 26.808 | 21.390 | 22.023 | 5.418 |
| position_difference | -1.856 | 0.159 | 2.931 | 4.787 |
| home_position_before_match | 7.728 | 9.098 | 10.322 | 2.594 |
| away_position_before_match | 9.584 | 8.939 | 7.391 | 2.193 |
| home_team_points_last_5 | 6.920 | 5.585 | 5.563 | 1.357 |
| home_team_goals_scored_last_5 | 5.928 | 4.866 | 4.678 | 1.250 |
| home_rest_days | 8.281 | 8.436 | 9.391 | 1.110 |
| away_team_points_last_5 | 5.920 | 6.134 | 7.023 | 1.103 |
| home_team_goals_conceded_last_5 | 5.000 | 5.159 | 6.069 | 1.069 |
| away_rest_days | 8.400 | 8.333 | 9.276 | 0.943 |
| away_team_goals_scored_last_5 | 5.040 | 5.049 | 5.966 | 0.926 |
| away_team_goals_conceded_last_5 | 5.400 | 5.329 | 4.851 | 0.549 |
| home_team_wins_last_5 | 1.880 | 1.451 | 1.425 | 0.455 |
| away_team_wins_last_5 | 1.520 | 1.610 | 1.885 | 0.365 |
| home_team_home_goals_avg | 1.380 | 1.143 | 1.136 | 0.243 |
| home_team_home_conceded_avg | 0.892 | 0.912 | 1.130 | 0.238 |
| away_team_away_conceded_avg | 1.351 | 1.206 | 1.120 | 0.231 |
| rest_days_difference | -0.100 | 0.103 | 0.115 | 0.215 |
| away_team_away_goals_avg | 0.900 | 0.951 | 1.071 | 0.172 |
| home_team_home_win_rate | 0.445 | 0.356 | 0.333 | 0.112 |
| away_team_away_win_rate | 0.220 | 0.238 | 0.304 | 0.084 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\bulgaria1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\bulgaria1\charts\relationships_home_win_pct_by_position.png)

