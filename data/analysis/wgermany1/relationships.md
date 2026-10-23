# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:24:24+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Bundesliga Women (Germany)
- Scope: league `wgermany1`

- Matches analysed: **182** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_scored_last_5 | -0.228 | 0.424 | 0.166 |
| away_team_away_goals_avg | -0.197 | 0.380 | 0.155 |
| away_team_away_win_rate | -0.172 | 0.352 | 0.152 |
| away_team_away_conceded_avg | 0.049 | -0.222 | -0.146 |
| away_position_before_match | 0.224 | -0.355 | -0.111 |
| away_team_wins_last_5 | -0.247 | 0.355 | 0.092 |
| away_team_points_last_5 | -0.236 | 0.343 | 0.091 |
| rest_days_difference | -0.016 | -0.065 | -0.068 |
| home_team_home_goals_avg | 0.193 | -0.113 | 0.067 |
| position_difference | -0.420 | 0.490 | 0.061 |
| home_team_home_win_rate | 0.275 | -0.213 | 0.050 |
| home_rest_days | 0.021 | -0.070 | -0.042 |
| home_team_points_last_5 | 0.196 | -0.148 | 0.038 |
| home_team_wins_last_5 | 0.208 | -0.172 | 0.029 |
| home_team_home_conceded_avg | -0.254 | 0.218 | -0.028 |
| home_position_before_match | -0.353 | 0.317 | -0.028 |
| home_team_goals_conceded_last_5 | -0.200 | 0.167 | -0.027 |
| points_difference | 0.411 | -0.435 | -0.023 |
| away_team_goals_conceded_last_5 | 0.168 | -0.192 | -0.022 |
| home_points_before_match | 0.181 | -0.199 | -0.017 |
| away_rest_days | 0.034 | -0.015 | 0.016 |
| away_points_before_match | -0.204 | 0.209 | 0.005 |
| home_team_goals_scored_last_5 | 0.174 | -0.169 | 0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 39 | 6 | 5 | 28 | 15.4% | 12.8% | 71.8% |
| -4..-2 | 24 | 10 | 3 | 11 | 41.7% | 12.5% | 45.8% |
| -1..1 | 56 | 26 | 13 | 17 | 46.4% | 23.2% | 30.4% |
| 2..4 | 31 | 18 | 5 | 8 | 58.1% | 16.1% | 25.8% |
| >4 | 32 | 21 | 6 | 5 | 65.6% | 18.8% | 15.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 28 | 20 | 5 | 3 | 71.4% | 17.9% | 10.7% |
| -5..-2 | 40 | 25 | 7 | 8 | 62.5% | 17.5% | 20.0% |
| -1..1 | 40 | 22 | 7 | 11 | 55.0% | 17.5% | 27.5% |
| 2..5 | 45 | 13 | 10 | 22 | 28.9% | 22.2% | 48.9% |
| >=6 | 29 | 1 | 3 | 25 | 3.4% | 10.3% | 86.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 35 | 16 | 6 | 13 | 45.7% | 17.1% | 37.1% |
| -1..0 | 36 | 22 | 3 | 11 | 61.1% | 8.3% | 30.6% |
| 0 | 35 | 13 | 7 | 15 | 37.1% | 20.0% | 42.9% |
| 1..2 | 57 | 22 | 9 | 26 | 38.6% | 15.8% | 45.6% |
| >2 | 12 | 6 | 4 | 2 | 50.0% | 33.3% | 16.7% |
| unknown | 7 | 2 | 3 | 2 | 28.6% | 42.9% | 28.6% |
- *7 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **32.7%** home win (32/98)
- `>= 0.5` tier: **58.3%** home win (49/84)
- Home-win gap (>= split minus < split): **+25.6 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 98 | 32 | 18 | 48 | 32.7% |
| high | >= 0.5 | 84 | 49 | 14 | 21 | 58.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.778 | 1.656 | -8.696 | 14.473 |
| away_points_before_match | 14.889 | 15.562 | 22.609 | 7.720 |
| home_points_before_match | 20.667 | 17.219 | 13.913 | 6.754 |
| position_difference | -2.457 | -0.625 | 3.522 | 5.979 |
| home_position_before_match | 6.000 | 8.219 | 9.493 | 3.493 |
| away_team_goals_scored_last_5 | 6.395 | 6.500 | 9.652 | 3.257 |
| home_rest_days | 10.494 | 11.931 | 9.030 | 2.901 |
| away_position_before_match | 8.457 | 8.844 | 5.971 | 2.873 |
| away_team_points_last_5 | 5.481 | 5.250 | 7.681 | 2.431 |
| home_team_goals_scored_last_5 | 8.802 | 6.562 | 6.580 | 2.240 |
| home_team_goals_conceded_last_5 | 6.728 | 7.625 | 8.899 | 2.170 |
| home_team_points_last_5 | 7.296 | 5.656 | 5.246 | 2.050 |
| away_team_goals_conceded_last_5 | 8.148 | 7.906 | 6.507 | 1.641 |
| rest_days_difference | 0.544 | 0.862 | -0.627 | 1.489 |
| away_rest_days | 9.949 | 11.069 | 9.657 | 1.412 |
| away_team_wins_last_5 | 1.543 | 1.438 | 2.319 | 0.881 |
| away_team_away_goals_avg | 1.273 | 1.191 | 2.052 | 0.861 |
| home_team_wins_last_5 | 2.198 | 1.688 | 1.449 | 0.748 |
| home_team_home_conceded_avg | 1.261 | 1.451 | 1.958 | 0.697 |
| home_team_home_goals_avg | 1.871 | 1.576 | 1.373 | 0.498 |
| away_team_away_conceded_avg | 1.737 | 1.792 | 1.485 | 0.308 |
| home_team_home_win_rate | 0.524 | 0.409 | 0.288 | 0.235 |
| away_team_away_win_rate | 0.289 | 0.259 | 0.436 | 0.177 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\wgermany1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\wgermany1\charts\relationships_home_win_pct_by_position.png)

