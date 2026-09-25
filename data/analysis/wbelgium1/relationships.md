# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:50:43+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super League Women (Belgium)
- Scope: league `wbelgium1`

- Matches analysed: **120** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_goals_avg | 0.013 | -0.219 | -0.170 |
| home_position_before_match | -0.178 | 0.316 | 0.127 |
| home_team_home_conceded_avg | -0.173 | 0.267 | 0.090 |
| home_team_goals_scored_last_5 | 0.070 | -0.169 | -0.086 |
| away_position_before_match | 0.294 | -0.173 | 0.078 |
| rest_days_difference | -0.012 | 0.096 | 0.073 |
| home_team_points_last_5 | 0.085 | -0.159 | -0.067 |
| home_rest_days | -0.037 | 0.109 | 0.065 |
| away_team_away_win_rate | -0.132 | 0.188 | 0.056 |
| home_points_before_match | 0.075 | -0.133 | -0.053 |
| away_team_away_conceded_avg | 0.142 | -0.072 | 0.047 |
| away_points_before_match | -0.168 | 0.105 | -0.040 |
| position_difference | -0.348 | 0.356 | 0.032 |
| home_team_goals_conceded_last_5 | -0.226 | 0.168 | -0.032 |
| home_team_home_win_rate | 0.117 | -0.140 | -0.028 |
| away_team_away_goals_avg | -0.204 | 0.153 | -0.027 |
| away_rest_days | -0.030 | 0.050 | 0.021 |
| home_team_wins_last_5 | 0.054 | -0.074 | -0.021 |
| points_difference | 0.285 | -0.282 | -0.019 |
| away_team_wins_last_5 | -0.253 | 0.217 | -0.011 |
| away_team_goals_scored_last_5 | -0.223 | 0.213 | 0.008 |
| away_team_goals_conceded_last_5 | 0.103 | -0.085 | 0.008 |
| away_team_points_last_5 | -0.225 | 0.204 | -0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 23 | 6 | 4 | 13 | 26.1% | 17.4% | 56.5% |
| -4..-2 | 23 | 4 | 10 | 9 | 17.4% | 43.5% | 39.1% |
| -1..1 | 31 | 12 | 5 | 14 | 38.7% | 16.1% | 45.2% |
| 2..4 | 15 | 8 | 3 | 4 | 53.3% | 20.0% | 26.7% |
| >4 | 28 | 22 | 4 | 2 | 78.6% | 14.3% | 7.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 3 | 3 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| -5..-2 | 40 | 29 | 8 | 3 | 72.5% | 20.0% | 7.5% |
| -1..1 | 37 | 14 | 9 | 14 | 37.8% | 24.3% | 37.8% |
| 2..5 | 36 | 5 | 8 | 23 | 13.9% | 22.2% | 63.9% |
| >=6 | 4 | 1 | 1 | 2 | 25.0% | 25.0% | 50.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 7 | 3 | 0 | 4 | 42.9% | 0.0% | 57.1% |
| -1..0 | 15 | 6 | 4 | 5 | 40.0% | 26.7% | 33.3% |
| 0 | 69 | 32 | 16 | 21 | 46.4% | 23.2% | 30.4% |
| 1..2 | 12 | 5 | 2 | 5 | 41.7% | 16.7% | 41.7% |
| >2 | 9 | 1 | 2 | 6 | 11.1% | 22.2% | 66.7% |
| unknown | 8 | 5 | 2 | 1 | 62.5% | 25.0% | 12.5% |
- *8 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **34.0%** home win (16/47)
- `>= 0.5` tier: **49.3%** home win (36/73)
- Home-win gap (>= split minus < split): **+15.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 47 | 16 | 8 | 23 | 34.0% |
| high | >= 0.5 | 73 | 36 | 18 | 19 | 49.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 7.096 | -0.846 | -6.190 | 13.287 |
| away_points_before_match | 12.077 | 19.154 | 19.262 | 7.185 |
| home_points_before_match | 19.173 | 18.308 | 13.071 | 6.102 |
| position_difference | -1.731 | 0.192 | 1.810 | 3.540 |
| away_team_points_last_5 | 4.212 | 6.000 | 7.333 | 3.122 |
| away_team_goals_scored_last_5 | 5.115 | 6.385 | 7.548 | 2.432 |
| home_team_goals_conceded_last_5 | 5.000 | 6.038 | 7.214 | 2.214 |
| home_position_before_match | 3.615 | 4.269 | 5.429 | 1.813 |
| home_team_points_last_5 | 6.692 | 5.115 | 4.905 | 1.788 |
| away_team_goals_conceded_last_5 | 7.212 | 5.962 | 5.476 | 1.735 |
| away_position_before_match | 5.346 | 4.077 | 3.619 | 1.727 |
| home_team_goals_scored_last_5 | 7.058 | 5.462 | 5.333 | 1.724 |
| away_rest_days | 9.915 | 8.708 | 10.000 | 1.292 |
| away_team_wins_last_5 | 1.942 | 2.538 | 3.143 | 1.201 |
| rest_days_difference | -0.340 | 0.667 | 0.146 | 1.007 |
| home_rest_days | 9.574 | 9.375 | 10.146 | 0.771 |
| home_team_home_conceded_avg | 0.931 | 1.146 | 1.543 | 0.612 |
| away_team_away_goals_avg | 0.964 | 1.430 | 1.551 | 0.587 |
| home_team_home_goals_avg | 1.478 | 1.374 | 1.077 | 0.402 |
| home_team_wins_last_5 | 2.731 | 2.346 | 2.333 | 0.397 |
| away_team_away_conceded_avg | 1.425 | 1.339 | 1.038 | 0.386 |
| home_team_home_win_rate | 0.657 | 0.595 | 0.481 | 0.176 |
| away_team_away_win_rate | 0.456 | 0.544 | 0.618 | 0.162 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\wbelgium1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\wbelgium1\charts\relationships_home_win_pct_by_position.png)

