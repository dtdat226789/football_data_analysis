# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:45:14+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: League Two (Scotland)
- Scope: league `scot2`

- Matches analysed: **228** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_win_rate | 0.153 | 0.087 | 0.185 |
| home_team_home_goals_avg | 0.146 | 0.077 | 0.171 |
| home_points_before_match | 0.017 | -0.130 | -0.090 |
| home_team_goals_scored_last_5 | 0.089 | 0.011 | 0.076 |
| away_rest_days | -0.020 | 0.117 | 0.075 |
| home_position_before_match | -0.073 | -0.015 | -0.067 |
| away_points_before_match | -0.008 | -0.074 | -0.065 |
| rest_days_difference | -0.049 | -0.035 | -0.065 |
| away_team_goals_scored_last_5 | -0.092 | 0.010 | -0.061 |
| away_team_away_conceded_avg | 0.117 | -0.048 | 0.050 |
| away_position_before_match | 0.056 | -0.111 | -0.046 |
| away_team_wins_last_5 | -0.109 | 0.052 | -0.041 |
| points_difference | 0.037 | -0.083 | -0.038 |
| home_rest_days | -0.055 | 0.099 | 0.036 |
| home_team_wins_last_5 | 0.021 | 0.024 | 0.034 |
| home_team_home_conceded_avg | 0.065 | -0.021 | 0.033 |
| home_team_points_last_5 | 0.036 | 0.005 | 0.031 |
| away_team_away_win_rate | -0.031 | 0.062 | 0.025 |
| away_team_away_goals_avg | -0.070 | 0.097 | 0.024 |
| away_team_points_last_5 | -0.098 | 0.069 | -0.019 |
| position_difference | -0.094 | 0.070 | -0.016 |
| home_team_goals_conceded_last_5 | 0.011 | -0.028 | -0.014 |
| away_team_goals_conceded_last_5 | 0.094 | -0.088 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 36 | 17 | 12 | 7 | 47.2% | 33.3% | 19.4% |
| -4..-2 | 44 | 13 | 14 | 17 | 29.5% | 31.8% | 38.6% |
| -1..1 | 82 | 37 | 19 | 26 | 45.1% | 23.2% | 31.7% |
| 2..4 | 44 | 21 | 12 | 11 | 47.7% | 27.3% | 25.0% |
| >4 | 22 | 11 | 5 | 6 | 50.0% | 22.7% | 27.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 23 | 11 | 5 | 7 | 47.8% | 21.7% | 30.4% |
| -5..-2 | 56 | 26 | 15 | 15 | 46.4% | 26.8% | 26.8% |
| -1..1 | 49 | 24 | 12 | 13 | 49.0% | 24.5% | 26.5% |
| 2..5 | 73 | 27 | 22 | 24 | 37.0% | 30.1% | 32.9% |
| >=6 | 27 | 11 | 8 | 8 | 40.7% | 29.6% | 29.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 13 | 5 | 3 | 5 | 38.5% | 23.1% | 38.5% |
| -1..0 | 1 | 1 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| 0 | 188 | 82 | 54 | 52 | 43.6% | 28.7% | 27.7% |
| 1..2 | 1 | 0 | 0 | 1 | 0.0% | 0.0% | 100.0% |
| >2 | 13 | 5 | 4 | 4 | 38.5% | 30.8% | 30.8% |
| unknown | 12 | 6 | 1 | 5 | 50.0% | 8.3% | 41.7% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **49.1%** home win (27/55)
- `>= 0.5` tier: **41.6%** home win (72/173)
- Home-win gap (>= split minus < split): **-7.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 55 | 27 | 13 | 15 | 49.1% |
| high | >= 0.5 | 173 | 72 | 49 | 52 | 41.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 21.323 | 22.629 | 18.925 | 3.704 |
| home_points_before_match | 21.495 | 21.145 | 18.716 | 2.779 |
| points_difference | 0.172 | -1.484 | -0.209 | 1.656 |
| away_team_points_last_5 | 5.495 | 7.048 | 6.075 | 1.553 |
| away_team_goals_scored_last_5 | 6.020 | 7.452 | 6.284 | 1.431 |
| position_difference | -0.222 | 0.806 | 0.343 | 1.029 |
| away_rest_days | 7.140 | 7.806 | 8.065 | 0.925 |
| home_rest_days | 7.172 | 7.689 | 7.841 | 0.669 |
| home_position_before_match | 5.313 | 5.935 | 5.328 | 0.622 |
| away_position_before_match | 5.535 | 5.129 | 4.985 | 0.550 |
| away_team_goals_conceded_last_5 | 6.515 | 6.177 | 5.970 | 0.545 |
| away_team_wins_last_5 | 2.606 | 3.113 | 2.821 | 0.507 |
| home_team_goals_conceded_last_5 | 6.606 | 6.677 | 6.194 | 0.483 |
| home_team_points_last_5 | 5.475 | 5.952 | 5.836 | 0.477 |
| away_team_away_goals_avg | 1.232 | 1.578 | 1.444 | 0.345 |
| home_team_goals_scored_last_5 | 6.364 | 6.484 | 6.194 | 0.290 |
| home_team_wins_last_5 | 2.606 | 2.726 | 2.791 | 0.185 |
| home_team_home_conceded_avg | 1.390 | 1.469 | 1.285 | 0.184 |
| rest_days_difference | 0.032 | -0.131 | -0.145 | 0.177 |
| away_team_away_conceded_avg | 1.372 | 1.344 | 1.224 | 0.148 |
| away_team_away_win_rate | 0.547 | 0.626 | 0.581 | 0.079 |
| home_team_home_goals_avg | 1.348 | 1.350 | 1.306 | 0.044 |
| home_team_home_win_rate | 0.570 | 0.577 | 0.581 | 0.011 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\scot2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\scot2\charts\relationships_home_win_pct_by_position.png)

