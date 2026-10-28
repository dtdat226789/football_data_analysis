# Relationships Analysis
- Report: `relationships`
- Generated: 2026-10-27T01:45:08+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 1st Division (Denmark)
- Scope: league `denmark2`

- Matches analysed: **776** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_points_before_match | -0.152 | 0.048 | -0.082 |
| home_points_before_match | 0.021 | -0.130 | -0.081 |
| rest_days_difference | -0.073 | -0.019 | -0.071 |
| away_team_points_last_5 | -0.153 | 0.106 | -0.039 |
| away_rest_days | 0.036 | 0.008 | 0.034 |
| home_team_goals_scored_last_5 | 0.052 | -0.098 | -0.033 |
| home_team_points_last_5 | 0.075 | -0.116 | -0.029 |
| home_team_wins_last_5 | 0.068 | -0.103 | -0.025 |
| away_team_wins_last_5 | -0.151 | 0.123 | -0.025 |
| home_position_before_match | -0.129 | 0.165 | 0.025 |
| home_team_home_conceded_avg | -0.090 | 0.061 | -0.024 |
| away_position_before_match | 0.171 | -0.149 | 0.020 |
| away_team_goals_scored_last_5 | -0.126 | 0.104 | -0.020 |
| away_team_away_win_rate | -0.125 | 0.105 | -0.018 |
| away_team_away_conceded_avg | 0.073 | -0.097 | -0.016 |
| home_team_goals_conceded_last_5 | -0.095 | 0.080 | -0.014 |
| home_rest_days | -0.004 | -0.003 | -0.005 |
| position_difference | -0.216 | 0.227 | 0.003 |
| away_team_away_goals_avg | -0.105 | 0.105 | -0.002 |
| away_team_goals_conceded_last_5 | 0.074 | -0.078 | -0.001 |
| home_team_home_win_rate | 0.087 | -0.091 | -0.001 |
| points_difference | 0.217 | -0.223 | 0.001 |
| home_team_home_goals_avg | 0.093 | -0.096 | -0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 123 | 32 | 26 | 65 | 26.0% | 21.1% | 52.8% |
| -4..-2 | 157 | 52 | 42 | 63 | 33.1% | 26.8% | 40.1% |
| -1..1 | 227 | 97 | 50 | 80 | 42.7% | 22.0% | 35.2% |
| 2..4 | 153 | 84 | 31 | 38 | 54.9% | 20.3% | 24.8% |
| >4 | 116 | 59 | 29 | 28 | 50.9% | 25.0% | 24.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 95 | 54 | 24 | 17 | 56.8% | 25.3% | 17.9% |
| -5..-2 | 200 | 105 | 47 | 48 | 52.5% | 23.5% | 24.0% |
| -1..1 | 176 | 82 | 38 | 56 | 46.6% | 21.6% | 31.8% |
| 2..5 | 201 | 63 | 44 | 94 | 31.3% | 21.9% | 46.8% |
| >=6 | 104 | 20 | 25 | 59 | 19.2% | 24.0% | 56.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 121 | 52 | 29 | 40 | 43.0% | 24.0% | 33.1% |
| -1..0 | 156 | 72 | 33 | 51 | 46.2% | 21.2% | 32.7% |
| 0 | 169 | 69 | 34 | 66 | 40.8% | 20.1% | 39.1% |
| 1..2 | 236 | 90 | 58 | 88 | 38.1% | 24.6% | 37.3% |
| >2 | 58 | 24 | 14 | 20 | 41.4% | 24.1% | 34.5% |
| unknown | 36 | 17 | 10 | 9 | 47.2% | 27.8% | 25.0% |
- *36 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **39.0%** home win (176/451)
- `>= 0.5` tier: **45.5%** home win (148/325)
- Home-win gap (>= split minus < split): **+6.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 451 | 176 | 99 | 176 | 39.0% |
| high | >= 0.5 | 325 | 148 | 79 | 98 | 45.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.614 | -0.112 | -3.507 | 6.121 |
| away_points_before_match | 13.269 | 16.067 | 17.237 | 3.969 |
| position_difference | -1.167 | 0.045 | 1.770 | 2.937 |
| home_rest_days | 10.731 | 13.399 | 10.521 | 2.878 |
| away_rest_days | 10.831 | 12.858 | 10.411 | 2.447 |
| home_points_before_match | 15.883 | 15.955 | 13.730 | 2.225 |
| away_team_points_last_5 | 5.204 | 6.455 | 6.781 | 1.577 |
| away_position_before_match | 6.985 | 6.315 | 5.474 | 1.510 |
| home_position_before_match | 5.818 | 6.360 | 7.245 | 1.427 |
| away_team_goals_scored_last_5 | 5.673 | 6.601 | 6.923 | 1.251 |
| home_team_goals_conceded_last_5 | 5.978 | 6.213 | 6.949 | 0.971 |
| home_team_points_last_5 | 6.201 | 6.309 | 5.460 | 0.849 |
| away_team_goals_conceded_last_5 | 6.577 | 6.253 | 5.854 | 0.723 |
| rest_days_difference | -0.101 | 0.506 | 0.109 | 0.607 |
| home_team_goals_scored_last_5 | 6.506 | 6.517 | 5.923 | 0.593 |
| away_team_wins_last_5 | 1.401 | 1.781 | 1.960 | 0.559 |
| away_team_away_goals_avg | 1.139 | 1.215 | 1.454 | 0.315 |
| home_team_wins_last_5 | 1.738 | 1.730 | 1.518 | 0.219 |
| home_team_home_conceded_avg | 1.175 | 1.284 | 1.383 | 0.207 |
| away_team_away_conceded_avg | 1.514 | 1.463 | 1.310 | 0.204 |
| home_team_home_goals_avg | 1.530 | 1.407 | 1.338 | 0.191 |
| away_team_away_win_rate | 0.263 | 0.303 | 0.385 | 0.121 |
| home_team_home_win_rate | 0.430 | 0.395 | 0.360 | 0.071 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](charts/relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](charts/relationships_home_win_pct_by_position.png)

