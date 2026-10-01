# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:02:48+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Eliteserien (Norway)
- Scope: league `norway`

- Matches analysed: **240** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_rest_days | 0.106 | 0.117 | 0.174 |
| away_rest_days | 0.072 | 0.070 | 0.111 |
| rest_days_difference | 0.051 | 0.070 | 0.094 |
| away_points_before_match | -0.005 | 0.106 | 0.073 |
| home_points_before_match | 0.253 | -0.191 | 0.071 |
| home_position_before_match | -0.203 | 0.307 | 0.056 |
| away_team_wins_last_5 | -0.098 | 0.181 | 0.051 |
| away_team_away_goals_avg | -0.064 | 0.142 | 0.051 |
| home_team_home_goals_avg | 0.204 | -0.169 | 0.046 |
| home_team_home_conceded_avg | -0.197 | 0.169 | -0.040 |
| away_team_points_last_5 | -0.108 | 0.169 | 0.034 |
| away_team_away_win_rate | -0.076 | 0.127 | 0.030 |
| away_team_away_conceded_avg | 0.047 | -0.014 | 0.029 |
| position_difference | -0.273 | 0.347 | 0.027 |
| away_team_goals_conceded_last_5 | 0.096 | -0.073 | 0.026 |
| home_team_home_win_rate | 0.166 | -0.154 | 0.025 |
| away_team_goals_scored_last_5 | -0.127 | 0.176 | 0.023 |
| away_position_before_match | 0.166 | -0.162 | 0.019 |
| home_team_goals_conceded_last_5 | -0.143 | 0.174 | 0.009 |
| home_team_points_last_5 | 0.168 | -0.201 | -0.007 |
| home_team_wins_last_5 | 0.183 | -0.203 | 0.004 |
| points_difference | 0.305 | -0.352 | -0.004 |
| home_team_goals_scored_last_5 | 0.143 | -0.160 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 44 | 15 | 9 | 20 | 34.1% | 20.5% | 45.5% |
| -4..-2 | 50 | 17 | 7 | 26 | 34.0% | 14.0% | 52.0% |
| -1..1 | 66 | 40 | 8 | 18 | 60.6% | 12.1% | 27.3% |
| 2..4 | 39 | 18 | 11 | 10 | 46.2% | 28.2% | 25.6% |
| >4 | 41 | 28 | 10 | 3 | 68.3% | 24.4% | 7.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 44 | 35 | 6 | 3 | 79.5% | 13.6% | 6.8% |
| -5..-2 | 51 | 29 | 13 | 9 | 56.9% | 25.5% | 17.6% |
| -1..1 | 39 | 14 | 6 | 19 | 35.9% | 15.4% | 48.7% |
| 2..5 | 60 | 26 | 9 | 25 | 43.3% | 15.0% | 41.7% |
| >=6 | 46 | 14 | 11 | 21 | 30.4% | 23.9% | 45.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 24 | 10 | 8 | 6 | 41.7% | 33.3% | 25.0% |
| -1..0 | 32 | 17 | 5 | 10 | 53.1% | 15.6% | 31.2% |
| 0 | 116 | 55 | 22 | 39 | 47.4% | 19.0% | 33.6% |
| 1..2 | 37 | 22 | 6 | 9 | 59.5% | 16.2% | 24.3% |
| >2 | 23 | 9 | 4 | 10 | 39.1% | 17.4% | 43.5% |
| unknown | 8 | 5 | 0 | 3 | 62.5% | 0.0% | 37.5% |
- *8 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **44.1%** home win (56/127)
- `>= 0.5` tier: **54.9%** home win (62/113)
- Home-win gap (>= split minus < split): **+10.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 127 | 56 | 23 | 48 | 44.1% |
| high | >= 0.5 | 113 | 62 | 22 | 29 | 54.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.085 | -0.756 | -7.143 | 11.228 |
| home_points_before_match | 23.254 | 19.578 | 15.584 | 7.670 |
| position_difference | -1.856 | 0.467 | 3.312 | 5.168 |
| away_points_before_match | 19.169 | 20.333 | 22.727 | 3.558 |
| home_position_before_match | 7.610 | 8.533 | 10.416 | 2.805 |
| away_position_before_match | 9.466 | 8.067 | 7.104 | 2.362 |
| home_team_points_last_5 | 6.653 | 7.111 | 4.948 | 2.163 |
| away_team_goals_scored_last_5 | 6.246 | 7.289 | 8.260 | 2.014 |
| away_team_points_last_5 | 5.619 | 6.644 | 7.442 | 1.823 |
| away_rest_days | 8.265 | 7.511 | 9.041 | 1.529 |
| home_team_goals_conceded_last_5 | 6.686 | 6.978 | 8.091 | 1.404 |
| home_rest_days | 8.363 | 7.933 | 9.203 | 1.269 |
| home_team_goals_scored_last_5 | 7.441 | 7.267 | 6.195 | 1.246 |
| away_team_goals_conceded_last_5 | 7.178 | 7.022 | 6.377 | 0.801 |
| home_team_wins_last_5 | 1.932 | 2.000 | 1.351 | 0.649 |
| away_team_wins_last_5 | 1.568 | 1.889 | 2.182 | 0.614 |
| home_team_home_conceded_avg | 1.090 | 1.388 | 1.457 | 0.367 |
| home_team_home_goals_avg | 1.726 | 1.585 | 1.362 | 0.364 |
| away_team_away_goals_avg | 1.132 | 1.247 | 1.458 | 0.326 |
| rest_days_difference | 0.097 | 0.422 | 0.162 | 0.325 |
| home_team_home_win_rate | 0.494 | 0.471 | 0.379 | 0.115 |
| away_team_away_win_rate | 0.258 | 0.350 | 0.352 | 0.094 |
| away_team_away_conceded_avg | 1.593 | 1.577 | 1.571 | 0.022 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\norway\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\norway\charts\relationships_home_win_pct_by_position.png)

