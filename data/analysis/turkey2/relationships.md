# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:10:51+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 1. Lig (Turkey)
- Scope: league `turkey2`

- Matches analysed: **385** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | -0.142 | 0.459 | 0.229 |
| away_team_goals_conceded_last_5 | 0.411 | -0.160 | 0.222 |
| away_team_away_conceded_avg | 0.374 | -0.165 | 0.187 |
| home_position_before_match | -0.120 | 0.375 | 0.184 |
| home_team_goals_conceded_last_5 | -0.168 | 0.420 | 0.178 |
| away_team_points_last_5 | -0.282 | 0.090 | -0.167 |
| away_team_away_win_rate | -0.256 | 0.071 | -0.160 |
| away_position_before_match | 0.340 | -0.179 | 0.148 |
| away_team_wins_last_5 | -0.259 | 0.090 | -0.148 |
| home_team_home_win_rate | 0.104 | -0.297 | -0.138 |
| away_points_before_match | -0.242 | 0.087 | -0.137 |
| home_points_before_match | 0.077 | -0.237 | -0.115 |
| away_team_goals_scored_last_5 | -0.192 | 0.081 | -0.099 |
| away_team_away_goals_avg | -0.155 | 0.049 | -0.092 |
| home_team_points_last_5 | 0.154 | -0.284 | -0.088 |
| home_team_home_goals_avg | 0.138 | -0.246 | -0.072 |
| home_team_wins_last_5 | 0.132 | -0.237 | -0.070 |
| home_rest_days | -0.035 | -0.017 | -0.043 |
| away_rest_days | 0.005 | -0.048 | -0.032 |
| rest_days_difference | -0.103 | 0.073 | -0.031 |
| points_difference | 0.422 | -0.428 | 0.027 |
| position_difference | -0.337 | 0.404 | 0.026 |
| home_team_goals_scored_last_5 | 0.158 | -0.180 | -0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 75 | 16 | 14 | 45 | 21.3% | 18.7% | 60.0% |
| -4..-2 | 73 | 31 | 20 | 22 | 42.5% | 27.4% | 30.1% |
| -1..1 | 101 | 46 | 28 | 27 | 45.5% | 27.7% | 26.7% |
| 2..4 | 77 | 42 | 23 | 12 | 54.5% | 29.9% | 15.6% |
| >4 | 59 | 40 | 10 | 9 | 67.8% | 16.9% | 15.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 97 | 63 | 22 | 12 | 64.9% | 22.7% | 12.4% |
| -5..-2 | 65 | 39 | 16 | 10 | 60.0% | 24.6% | 15.4% |
| -1..1 | 55 | 23 | 16 | 16 | 41.8% | 29.1% | 29.1% |
| 2..5 | 61 | 19 | 19 | 23 | 31.1% | 31.1% | 37.7% |
| >=6 | 107 | 31 | 22 | 54 | 29.0% | 20.6% | 50.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 26 | 16 | 6 | 4 | 61.5% | 23.1% | 15.4% |
| -1..0 | 85 | 36 | 21 | 28 | 42.4% | 24.7% | 32.9% |
| 0 | 148 | 72 | 30 | 46 | 48.6% | 20.3% | 31.1% |
| 1..2 | 111 | 46 | 33 | 32 | 41.4% | 29.7% | 28.8% |
| >2 | 5 | 1 | 1 | 3 | 20.0% | 20.0% | 60.0% |
| unknown | 10 | 4 | 4 | 2 | 40.0% | 40.0% | 20.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **40.5%** home win (83/205)
- `>= 0.5` tier: **51.1%** home win (92/180)
- Home-win gap (>= split minus < split): **+10.6 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 205 | 83 | 45 | 77 | 40.5% |
| high | >= 0.5 | 180 | 92 | 50 | 38 | 51.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.577 | -0.558 | -8.513 | 14.090 |
| away_points_before_match | 22.623 | 25.811 | 30.930 | 8.308 |
| position_difference | -2.566 | 0.095 | 4.583 | 7.148 |
| home_points_before_match | 28.200 | 25.253 | 22.417 | 5.783 |
| home_position_before_match | 9.663 | 9.832 | 13.461 | 3.798 |
| home_team_goals_conceded_last_5 | 5.600 | 5.895 | 9.226 | 3.626 |
| away_position_before_match | 12.229 | 9.737 | 8.878 | 3.350 |
| away_team_goals_conceded_last_5 | 7.926 | 5.368 | 5.591 | 2.557 |
| home_team_points_last_5 | 6.880 | 6.547 | 5.017 | 1.863 |
| away_team_points_last_5 | 5.749 | 6.716 | 7.417 | 1.669 |
| home_team_goals_scored_last_5 | 7.114 | 6.758 | 5.539 | 1.575 |
| away_team_goals_scored_last_5 | 6.320 | 6.821 | 7.783 | 1.463 |
| home_team_home_conceded_avg | 1.013 | 1.001 | 1.659 | 0.658 |
| away_rest_days | 7.240 | 7.396 | 6.752 | 0.643 |
| away_team_wins_last_5 | 1.537 | 1.842 | 2.113 | 0.576 |
| home_rest_days | 7.199 | 7.495 | 6.920 | 0.574 |
| home_team_wins_last_5 | 1.846 | 1.821 | 1.348 | 0.498 |
| away_team_away_conceded_avg | 1.760 | 1.370 | 1.392 | 0.389 |
| home_team_home_goals_avg | 1.681 | 1.591 | 1.333 | 0.348 |
| rest_days_difference | -0.041 | 0.099 | 0.168 | 0.209 |
| away_team_away_goals_avg | 1.148 | 1.287 | 1.251 | 0.139 |
| home_team_home_win_rate | 0.458 | 0.454 | 0.346 | 0.112 |
| away_team_away_win_rate | 0.217 | 0.284 | 0.280 | 0.067 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\turkey2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\turkey2\charts\relationships_home_win_pct_by_position.png)

