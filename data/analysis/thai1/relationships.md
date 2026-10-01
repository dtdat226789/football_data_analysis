# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:10:22+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Thai League 1 (Thailand)
- Scope: league `thai1`

- Matches analysed: **240** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_rest_days | -0.117 | -0.036 | -0.122 |
| home_position_before_match | -0.215 | 0.123 | -0.102 |
| rest_days_difference | 0.083 | 0.028 | 0.087 |
| points_difference | 0.267 | -0.235 | 0.075 |
| position_difference | -0.270 | 0.256 | -0.064 |
| away_team_goals_conceded_last_5 | 0.123 | -0.073 | 0.057 |
| home_points_before_match | 0.157 | -0.122 | 0.054 |
| away_team_away_win_rate | -0.122 | 0.246 | 0.054 |
| away_team_away_conceded_avg | 0.012 | -0.099 | -0.053 |
| home_team_home_conceded_avg | -0.105 | 0.057 | -0.052 |
| home_team_home_win_rate | 0.152 | -0.121 | 0.051 |
| home_team_goals_scored_last_5 | 0.148 | -0.130 | 0.042 |
| away_team_goals_scored_last_5 | -0.083 | 0.170 | 0.038 |
| home_team_wins_last_5 | 0.151 | -0.154 | 0.029 |
| home_team_points_last_5 | 0.154 | -0.162 | 0.026 |
| home_rest_days | -0.025 | -0.006 | -0.025 |
| home_team_goals_conceded_last_5 | -0.116 | 0.119 | -0.022 |
| home_team_home_goals_avg | 0.148 | -0.163 | 0.021 |
| away_team_points_last_5 | -0.126 | 0.136 | -0.019 |
| away_position_before_match | 0.167 | -0.243 | -0.014 |
| away_points_before_match | -0.072 | 0.079 | -0.010 |
| away_team_wins_last_5 | -0.111 | 0.162 | 0.010 |
| away_team_away_goals_avg | -0.136 | 0.183 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 38 | 8 | 13 | 17 | 21.1% | 34.2% | 44.7% |
| -4..-2 | 45 | 17 | 11 | 17 | 37.8% | 24.4% | 37.8% |
| -1..1 | 80 | 36 | 32 | 12 | 45.0% | 40.0% | 15.0% |
| 2..4 | 43 | 19 | 15 | 9 | 44.2% | 34.9% | 20.9% |
| >4 | 34 | 24 | 4 | 6 | 70.6% | 11.8% | 17.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 45 | 31 | 8 | 6 | 68.9% | 17.8% | 13.3% |
| -5..-2 | 51 | 27 | 17 | 7 | 52.9% | 33.3% | 13.7% |
| -1..1 | 33 | 14 | 11 | 8 | 42.4% | 33.3% | 24.2% |
| 2..5 | 58 | 20 | 21 | 17 | 34.5% | 36.2% | 29.3% |
| >=6 | 53 | 12 | 18 | 23 | 22.6% | 34.0% | 43.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 29 | 14 | 5 | 10 | 48.3% | 17.2% | 34.5% |
| -1..0 | 49 | 22 | 16 | 11 | 44.9% | 32.7% | 22.4% |
| 0 | 68 | 31 | 22 | 15 | 45.6% | 32.4% | 22.1% |
| 1..2 | 62 | 23 | 21 | 18 | 37.1% | 33.9% | 29.0% |
| >2 | 24 | 11 | 7 | 6 | 45.8% | 29.2% | 25.0% |
| unknown | 8 | 3 | 4 | 1 | 37.5% | 50.0% | 12.5% |
- *8 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.5%** home win (55/143)
- `>= 0.5` tier: **50.5%** home win (49/97)
- Home-win gap (>= split minus < split): **+12.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 143 | 55 | 46 | 42 | 38.5% |
| high | >= 0.5 | 97 | 49 | 29 | 19 | 50.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.615 | -1.933 | -5.869 | 9.484 |
| position_difference | -2.202 | 1.320 | 3.295 | 5.497 |
| home_points_before_match | 22.096 | 16.933 | 16.803 | 5.293 |
| away_points_before_match | 18.481 | 18.867 | 22.672 | 4.191 |
| away_position_before_match | 9.865 | 8.480 | 6.623 | 3.242 |
| home_position_before_match | 7.663 | 9.800 | 9.918 | 2.255 |
| away_team_goals_scored_last_5 | 5.702 | 5.667 | 7.574 | 1.907 |
| away_team_points_last_5 | 5.548 | 6.093 | 7.246 | 1.698 |
| home_team_goals_conceded_last_5 | 5.317 | 6.653 | 6.574 | 1.336 |
| home_team_points_last_5 | 6.673 | 5.387 | 5.426 | 1.286 |
| away_team_goals_conceded_last_5 | 6.644 | 5.667 | 5.443 | 1.202 |
| home_team_goals_scored_last_5 | 6.452 | 5.800 | 5.262 | 1.190 |
| home_rest_days | 9.000 | 9.775 | 9.467 | 0.775 |
| away_team_wins_last_5 | 1.365 | 1.547 | 1.967 | 0.602 |
| away_team_away_goals_avg | 0.968 | 1.007 | 1.387 | 0.420 |
| home_team_home_goals_avg | 1.601 | 1.489 | 1.205 | 0.397 |
| away_rest_days | 8.832 | 9.225 | 9.167 | 0.394 |
| home_team_wins_last_5 | 1.731 | 1.347 | 1.344 | 0.387 |
| rest_days_difference | 0.168 | 0.549 | 0.300 | 0.381 |
| home_team_home_conceded_avg | 0.975 | 1.193 | 1.127 | 0.219 |
| away_team_away_win_rate | 0.191 | 0.209 | 0.365 | 0.174 |
| away_team_away_conceded_avg | 1.546 | 1.453 | 1.384 | 0.162 |
| home_team_home_win_rate | 0.440 | 0.334 | 0.329 | 0.111 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\thai1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\thai1\charts\relationships_home_win_pct_by_position.png)

