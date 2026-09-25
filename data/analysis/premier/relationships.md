# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:42:16+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premier League (England)
- Scope: league `premier`

- Matches analysed: **2330** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.255 | 0.175 | -0.074 |
| home_team_goals_scored_last_5 | 0.176 | -0.102 | 0.065 |
| home_points_before_match | 0.146 | -0.082 | 0.055 |
| home_team_home_goals_avg | 0.165 | -0.104 | 0.055 |
| home_team_points_last_5 | 0.181 | -0.142 | 0.039 |
| points_difference | 0.283 | -0.254 | 0.039 |
| position_difference | -0.281 | 0.258 | -0.035 |
| away_team_goals_scored_last_5 | -0.082 | 0.133 | 0.032 |
| away_team_away_goals_avg | -0.087 | 0.132 | 0.026 |
| away_position_before_match | 0.136 | -0.184 | -0.026 |
| home_team_home_win_rate | 0.140 | -0.118 | 0.025 |
| away_points_before_match | -0.080 | 0.121 | 0.024 |
| home_team_home_conceded_avg | -0.133 | 0.113 | -0.023 |
| home_team_wins_last_5 | 0.149 | -0.142 | 0.015 |
| away_team_away_win_rate | -0.089 | 0.117 | 0.014 |
| away_team_goals_conceded_last_5 | 0.096 | -0.086 | 0.014 |
| home_team_goals_conceded_last_5 | -0.116 | 0.110 | -0.012 |
| rest_days_difference | -0.021 | 0.034 | 0.007 |
| away_team_away_conceded_avg | 0.076 | -0.090 | -0.005 |
| away_rest_days | -0.011 | 0.009 | -0.002 |
| away_team_wins_last_5 | -0.078 | 0.087 | 0.001 |
| home_rest_days | -0.022 | 0.026 | 0.001 |
| away_team_points_last_5 | -0.098 | 0.107 | 0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 390 | 98 | 94 | 198 | 25.1% | 24.1% | 50.8% |
| -4..-2 | 498 | 171 | 118 | 209 | 34.3% | 23.7% | 42.0% |
| -1..1 | 672 | 317 | 161 | 194 | 47.2% | 24.0% | 28.9% |
| 2..4 | 382 | 188 | 99 | 95 | 49.2% | 25.9% | 24.9% |
| >4 | 388 | 227 | 81 | 80 | 58.5% | 20.9% | 20.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 578 | 352 | 124 | 102 | 60.9% | 21.5% | 17.6% |
| -5..-2 | 406 | 200 | 98 | 108 | 49.3% | 24.1% | 26.6% |
| -1..1 | 328 | 163 | 74 | 91 | 49.7% | 22.6% | 27.7% |
| 2..5 | 399 | 148 | 96 | 155 | 37.1% | 24.1% | 38.8% |
| >=6 | 619 | 138 | 161 | 320 | 22.3% | 26.0% | 51.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 243 | 108 | 61 | 74 | 44.4% | 25.1% | 30.5% |
| -1..0 | 409 | 207 | 83 | 119 | 50.6% | 20.3% | 29.1% |
| 0 | 879 | 348 | 217 | 314 | 39.6% | 24.7% | 35.7% |
| 1..2 | 606 | 251 | 157 | 198 | 41.4% | 25.9% | 32.7% |
| >2 | 121 | 52 | 24 | 45 | 43.0% | 19.8% | 37.2% |
| unknown | 72 | 35 | 11 | 26 | 48.6% | 15.3% | 36.1% |
- *72 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.0%** home win (171/518)
- `>= 0.5` tier: **45.8%** home win (830/1812)
- Home-win gap (>= split minus < split): **+12.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 518 | 171 | 114 | 233 | 33.0% |
| high | >= 0.5 | 1812 | 830 | 439 | 543 | 45.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.098 | -1.078 | -6.135 | 11.233 |
| position_difference | -2.619 | 0.591 | 3.478 | 6.097 |
| home_points_before_match | 28.052 | 23.638 | 22.013 | 6.039 |
| away_points_before_match | 22.954 | 24.716 | 28.148 | 5.194 |
| home_position_before_match | 9.116 | 11.199 | 12.564 | 3.449 |
| away_position_before_match | 11.735 | 10.608 | 9.086 | 2.649 |
| home_team_points_last_5 | 6.962 | 6.085 | 5.291 | 1.671 |
| home_team_goals_scored_last_5 | 7.124 | 6.392 | 5.718 | 1.406 |
| away_team_points_last_5 | 5.854 | 6.477 | 6.966 | 1.112 |
| home_team_goals_conceded_last_5 | 6.070 | 6.747 | 7.139 | 1.069 |
| away_team_goals_conceded_last_5 | 6.953 | 6.454 | 5.906 | 1.047 |
| away_team_goals_scored_last_5 | 6.163 | 6.640 | 7.149 | 0.987 |
| home_team_wins_last_5 | 3.042 | 2.808 | 2.461 | 0.581 |
| away_team_wins_last_5 | 2.697 | 2.846 | 3.039 | 0.341 |
| home_rest_days | 7.389 | 7.454 | 7.702 | 0.313 |
| home_team_home_goals_avg | 1.608 | 1.467 | 1.297 | 0.312 |
| home_team_home_conceded_avg | 1.131 | 1.260 | 1.353 | 0.222 |
| away_team_away_goals_avg | 1.139 | 1.262 | 1.357 | 0.218 |
| away_rest_days | 7.452 | 7.437 | 7.618 | 0.181 |
| away_team_away_conceded_avg | 1.539 | 1.494 | 1.359 | 0.180 |
| rest_days_difference | -0.063 | 0.017 | 0.084 | 0.147 |
| home_team_home_win_rate | 0.673 | 0.633 | 0.568 | 0.105 |
| away_team_away_win_rate | 0.494 | 0.538 | 0.583 | 0.089 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\premier\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\premier\charts\relationships_home_win_pct_by_position.png)

