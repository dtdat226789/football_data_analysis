# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:53:46+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Tweede Divisie (Netherlands)
- Scope: league `holland3`

- Matches analysed: **322** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | 0.091 | 0.141 | 0.177 |
| home_team_home_goals_avg | 0.080 | 0.125 | 0.156 |
| home_team_goals_conceded_last_5 | 0.123 | 0.020 | 0.112 |
| home_points_before_match | 0.154 | -0.045 | 0.089 |
| away_team_goals_conceded_last_5 | 0.073 | 0.032 | 0.081 |
| rest_days_difference | -0.103 | 0.006 | -0.076 |
| home_team_goals_scored_last_5 | 0.105 | -0.010 | 0.076 |
| away_team_away_goals_avg | -0.028 | 0.129 | 0.073 |
| away_team_goals_scored_last_5 | -0.017 | 0.117 | 0.073 |
| away_points_before_match | 0.031 | 0.051 | 0.062 |
| away_team_away_conceded_avg | 0.072 | -0.004 | 0.054 |
| position_difference | -0.196 | 0.150 | -0.043 |
| away_position_before_match | 0.114 | -0.069 | 0.039 |
| away_rest_days | 0.073 | -0.026 | 0.038 |
| points_difference | 0.169 | -0.132 | 0.036 |
| home_team_home_win_rate | 0.001 | -0.046 | -0.033 |
| away_team_points_last_5 | -0.045 | 0.077 | 0.022 |
| home_team_points_last_5 | 0.058 | -0.033 | 0.021 |
| away_team_wins_last_5 | -0.032 | 0.060 | 0.020 |
| home_rest_days | 0.045 | -0.021 | 0.020 |
| home_position_before_match | -0.141 | 0.126 | -0.018 |
| home_team_wins_last_5 | 0.047 | -0.040 | 0.007 |
| away_team_away_win_rate | -0.054 | 0.057 | 0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 51 | 24 | 9 | 18 | 47.1% | 17.6% | 35.3% |
| -4..-2 | 72 | 25 | 15 | 32 | 34.7% | 20.8% | 44.4% |
| -1..1 | 84 | 44 | 14 | 26 | 52.4% | 16.7% | 31.0% |
| 2..4 | 76 | 40 | 16 | 20 | 52.6% | 21.1% | 26.3% |
| >4 | 39 | 20 | 9 | 10 | 51.3% | 23.1% | 25.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 75 | 42 | 17 | 16 | 56.0% | 22.7% | 21.3% |
| -5..-2 | 60 | 34 | 9 | 17 | 56.7% | 15.0% | 28.3% |
| -1..1 | 44 | 24 | 8 | 12 | 54.5% | 18.2% | 27.3% |
| 2..5 | 73 | 29 | 16 | 28 | 39.7% | 21.9% | 38.4% |
| >=6 | 70 | 24 | 13 | 33 | 34.3% | 18.6% | 47.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 8 | 4 | 1 | 3 | 50.0% | 12.5% | 37.5% |
| -1..0 | 0 | 0 | 0 | 0 | - | - | - |
| 0 | 296 | 141 | 60 | 95 | 47.6% | 20.3% | 32.1% |
| 1..2 | 0 | 0 | 0 | 0 | - | - | - |
| >2 | 4 | 1 | 0 | 3 | 25.0% | 0.0% | 75.0% |
| unknown | 14 | 7 | 2 | 5 | 50.0% | 14.3% | 35.7% |
- *14 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **45.9%** home win (79/172)
- `>= 0.5` tier: **49.3%** home win (74/150)
- Home-win gap (>= split minus < split): **+3.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 172 | 79 | 32 | 61 | 45.9% |
| high | >= 0.5 | 150 | 74 | 31 | 45 | 49.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.614 | 0.365 | -2.915 | 4.529 |
| position_difference | -1.170 | -0.016 | 2.236 | 3.406 |
| home_points_before_match | 23.967 | 23.540 | 20.689 | 3.279 |
| home_position_before_match | 9.908 | 9.492 | 11.708 | 2.215 |
| away_team_goals_scored_last_5 | 6.830 | 8.524 | 7.679 | 1.694 |
| away_position_before_match | 11.078 | 9.508 | 9.472 | 1.607 |
| away_points_before_match | 22.353 | 23.175 | 23.604 | 1.251 |
| home_team_points_last_5 | 6.137 | 6.905 | 5.670 | 1.235 |
| away_rest_days | 8.623 | 7.556 | 8.373 | 1.068 |
| home_rest_days | 8.507 | 7.459 | 8.416 | 1.048 |
| home_team_goals_scored_last_5 | 7.392 | 7.587 | 6.679 | 0.908 |
| away_team_points_last_5 | 6.118 | 6.905 | 6.575 | 0.787 |
| away_team_goals_conceded_last_5 | 7.105 | 7.746 | 6.981 | 0.765 |
| home_team_wins_last_5 | 1.752 | 2.016 | 1.585 | 0.431 |
| home_team_goals_conceded_last_5 | 7.549 | 7.206 | 7.170 | 0.379 |
| away_team_away_goals_avg | 1.267 | 1.510 | 1.441 | 0.243 |
| away_team_wins_last_5 | 1.765 | 1.952 | 1.896 | 0.188 |
| away_team_away_conceded_avg | 1.613 | 1.680 | 1.500 | 0.181 |
| rest_days_difference | -0.116 | -0.049 | 0.000 | 0.116 |
| home_team_home_win_rate | 0.435 | 0.466 | 0.403 | 0.063 |
| home_team_home_conceded_avg | 1.350 | 1.375 | 1.404 | 0.054 |
| home_team_home_goals_avg | 1.575 | 1.613 | 1.583 | 0.038 |
| away_team_away_win_rate | 0.316 | 0.334 | 0.339 | 0.023 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\holland3\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\holland3\charts\relationships_home_win_pct_by_position.png)

