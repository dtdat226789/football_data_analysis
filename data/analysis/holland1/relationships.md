# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:52:47+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Eredivisie (Netherlands)
- Scope: league `holland1`

- Matches analysed: **321** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.221 | 0.040 | -0.153 |
| points_difference | 0.303 | -0.155 | 0.142 |
| home_team_home_goals_avg | 0.132 | 0.046 | 0.140 |
| home_team_goals_scored_last_5 | 0.142 | 0.023 | 0.132 |
| rest_days_difference | -0.055 | -0.126 | -0.131 |
| home_team_wins_last_5 | 0.132 | 0.029 | 0.128 |
| home_team_points_last_5 | 0.112 | 0.024 | 0.108 |
| position_difference | -0.279 | 0.218 | -0.079 |
| away_rest_days | 0.026 | 0.082 | 0.078 |
| away_team_wins_last_5 | -0.077 | 0.205 | 0.078 |
| away_team_points_last_5 | -0.079 | 0.206 | 0.077 |
| home_points_before_match | 0.141 | -0.066 | 0.070 |
| home_team_goals_conceded_last_5 | -0.062 | -0.021 | -0.065 |
| away_position_before_match | 0.144 | -0.249 | -0.052 |
| home_team_home_conceded_avg | -0.003 | 0.074 | 0.048 |
| away_team_goals_conceded_last_5 | 0.019 | -0.092 | -0.047 |
| away_team_away_conceded_avg | 0.043 | -0.117 | -0.045 |
| away_team_away_goals_avg | -0.128 | 0.218 | 0.045 |
| away_team_away_win_rate | -0.127 | 0.216 | 0.044 |
| away_points_before_match | -0.086 | 0.049 | -0.036 |
| home_team_home_win_rate | 0.019 | 0.025 | 0.032 |
| away_team_goals_scored_last_5 | -0.123 | 0.191 | 0.030 |
| home_rest_days | -0.005 | 0.012 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 54 | 18 | 15 | 21 | 33.3% | 27.8% | 38.9% |
| -4..-2 | 70 | 28 | 17 | 25 | 40.0% | 24.3% | 35.7% |
| -1..1 | 91 | 37 | 26 | 28 | 40.7% | 28.6% | 30.8% |
| 2..4 | 64 | 34 | 17 | 13 | 53.1% | 26.6% | 20.3% |
| >4 | 42 | 26 | 8 | 8 | 61.9% | 19.0% | 19.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 67 | 43 | 14 | 10 | 64.2% | 20.9% | 14.9% |
| -5..-2 | 66 | 35 | 15 | 16 | 53.0% | 22.7% | 24.2% |
| -1..1 | 50 | 19 | 18 | 13 | 38.0% | 36.0% | 26.0% |
| 2..5 | 57 | 21 | 17 | 19 | 36.8% | 29.8% | 33.3% |
| >=6 | 81 | 25 | 19 | 37 | 30.9% | 23.5% | 45.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 16 | 6 | 4 | 6 | 37.5% | 25.0% | 37.5% |
| -1..0 | 74 | 29 | 16 | 29 | 39.2% | 21.6% | 39.2% |
| 0 | 103 | 53 | 24 | 26 | 51.5% | 23.3% | 25.2% |
| 1..2 | 98 | 40 | 31 | 27 | 40.8% | 31.6% | 27.6% |
| >2 | 17 | 7 | 5 | 5 | 41.2% | 29.4% | 29.4% |
| unknown | 13 | 8 | 3 | 2 | 61.5% | 23.1% | 15.4% |
- *13 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **43.7%** home win (80/183)
- `>= 0.5` tier: **45.7%** home win (63/138)
- Home-win gap (>= split minus < split): **+2.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 183 | 80 | 46 | 57 | 43.7% |
| high | >= 0.5 | 138 | 63 | 37 | 38 | 45.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.322 | -0.783 | -5.032 | 8.353 |
| position_difference | -1.748 | 0.651 | 3.537 | 5.285 |
| away_points_before_match | 20.294 | 23.759 | 24.747 | 4.454 |
| home_points_before_match | 23.615 | 22.976 | 19.716 | 3.900 |
| away_position_before_match | 11.301 | 9.651 | 8.389 | 2.911 |
| home_position_before_match | 9.552 | 10.301 | 11.926 | 2.374 |
| away_team_goals_scored_last_5 | 6.448 | 7.434 | 8.116 | 1.668 |
| away_team_points_last_5 | 5.727 | 6.530 | 7.084 | 1.357 |
| home_team_goals_scored_last_5 | 7.371 | 6.964 | 6.432 | 0.939 |
| home_rest_days | 8.088 | 8.762 | 8.319 | 0.674 |
| home_team_points_last_5 | 6.245 | 6.181 | 5.579 | 0.666 |
| away_team_goals_conceded_last_5 | 7.217 | 6.867 | 6.632 | 0.585 |
| rest_days_difference | 0.081 | 0.338 | -0.161 | 0.499 |
| away_rest_days | 8.037 | 8.425 | 8.527 | 0.490 |
| away_team_wins_last_5 | 1.538 | 1.759 | 2.000 | 0.462 |
| away_team_away_goals_avg | 1.174 | 1.399 | 1.530 | 0.356 |
| home_team_wins_last_5 | 1.713 | 1.663 | 1.442 | 0.271 |
| home_team_goals_conceded_last_5 | 7.217 | 6.976 | 7.084 | 0.241 |
| away_team_away_conceded_avg | 1.759 | 1.672 | 1.583 | 0.176 |
| home_team_home_goals_avg | 1.786 | 1.653 | 1.644 | 0.142 |
| away_team_away_win_rate | 0.247 | 0.247 | 0.368 | 0.121 |
| home_team_home_conceded_avg | 1.279 | 1.380 | 1.300 | 0.100 |
| home_team_home_win_rate | 0.444 | 0.416 | 0.457 | 0.041 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\holland1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\holland1\charts\relationships_home_win_pct_by_position.png)

