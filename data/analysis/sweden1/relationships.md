# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:09:25+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Allsvenskan (Sweden)
- Scope: league `sweden1`

- Matches analysed: **240** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_conceded_last_5 | -0.025 | 0.153 | 0.085 |
| away_position_before_match | 0.166 | -0.082 | 0.070 |
| away_team_away_win_rate | -0.086 | -0.004 | -0.068 |
| rest_days_difference | 0.014 | -0.114 | -0.067 |
| home_team_goals_scored_last_5 | 0.129 | -0.060 | 0.057 |
| position_difference | -0.238 | 0.183 | -0.056 |
| away_team_goals_scored_last_5 | 0.023 | 0.054 | 0.054 |
| points_difference | 0.235 | -0.208 | 0.036 |
| home_team_home_win_rate | 0.049 | -0.105 | -0.034 |
| away_team_goals_conceded_last_5 | 0.147 | -0.114 | 0.034 |
| home_points_before_match | 0.112 | -0.091 | 0.023 |
| away_team_wins_last_5 | -0.065 | 0.099 | 0.018 |
| home_team_home_goals_avg | 0.094 | -0.080 | 0.017 |
| away_rest_days | -0.013 | 0.037 | 0.015 |
| home_team_wins_last_5 | 0.101 | -0.131 | -0.012 |
| home_position_before_match | -0.179 | 0.183 | -0.011 |
| home_team_home_conceded_avg | -0.080 | 0.104 | 0.010 |
| away_points_before_match | -0.092 | 0.090 | -0.009 |
| home_rest_days | -0.009 | 0.004 | -0.004 |
| away_team_points_last_5 | -0.083 | 0.099 | 0.004 |
| away_team_away_conceded_avg | 0.045 | -0.055 | -0.003 |
| away_team_away_goals_avg | 0.010 | -0.010 | 0.001 |
| home_team_points_last_5 | 0.119 | -0.132 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 40 | 10 | 10 | 20 | 25.0% | 25.0% | 50.0% |
| -4..-2 | 45 | 13 | 9 | 23 | 28.9% | 20.0% | 51.1% |
| -1..1 | 60 | 23 | 16 | 21 | 38.3% | 26.7% | 35.0% |
| 2..4 | 60 | 32 | 8 | 20 | 53.3% | 13.3% | 33.3% |
| >4 | 35 | 18 | 10 | 7 | 51.4% | 28.6% | 20.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 57 | 40 | 8 | 9 | 70.2% | 14.0% | 15.8% |
| -5..-2 | 50 | 19 | 12 | 19 | 38.0% | 24.0% | 38.0% |
| -1..1 | 36 | 12 | 9 | 15 | 33.3% | 25.0% | 41.7% |
| 2..5 | 46 | 10 | 13 | 23 | 21.7% | 28.3% | 50.0% |
| >=6 | 51 | 15 | 11 | 25 | 29.4% | 21.6% | 49.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 18 | 6 | 3 | 9 | 33.3% | 16.7% | 50.0% |
| -1..0 | 67 | 27 | 13 | 27 | 40.3% | 19.4% | 40.3% |
| 0 | 72 | 29 | 16 | 27 | 40.3% | 22.2% | 37.5% |
| 1..2 | 69 | 29 | 17 | 23 | 42.0% | 24.6% | 33.3% |
| >2 | 6 | 2 | 3 | 1 | 33.3% | 50.0% | 16.7% |
| unknown | 8 | 3 | 1 | 4 | 37.5% | 12.5% | 50.0% |
- *8 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **36.6%** home win (56/153)
- `>= 0.5` tier: **46.0%** home win (40/87)
- Home-win gap (>= split minus < split): **+9.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 153 | 56 | 32 | 65 | 36.6% |
| high | >= 0.5 | 87 | 40 | 21 | 26 | 46.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.490 | -0.377 | -4.264 | 8.753 |
| home_points_before_match | 22.500 | 19.868 | 17.868 | 4.632 |
| position_difference | -2.427 | 0.302 | 2.066 | 4.493 |
| away_points_before_match | 18.010 | 20.245 | 22.132 | 4.121 |
| home_position_before_match | 7.177 | 8.981 | 9.989 | 2.812 |
| away_position_before_match | 9.604 | 8.679 | 7.923 | 1.681 |
| home_rest_days | 7.376 | 8.865 | 7.356 | 1.509 |
| home_team_points_last_5 | 6.885 | 6.623 | 5.396 | 1.490 |
| home_team_goals_conceded_last_5 | 5.667 | 6.698 | 7.044 | 1.377 |
| away_team_goals_conceded_last_5 | 6.990 | 6.434 | 5.637 | 1.352 |
| away_rest_days | 7.366 | 8.596 | 7.644 | 1.231 |
| away_team_points_last_5 | 5.604 | 6.774 | 6.626 | 1.169 |
| away_team_goals_scored_last_5 | 6.281 | 6.981 | 6.286 | 0.700 |
| home_team_goals_scored_last_5 | 6.625 | 6.396 | 5.989 | 0.636 |
| rest_days_difference | 0.011 | 0.269 | -0.287 | 0.557 |
| home_team_wins_last_5 | 1.958 | 1.906 | 1.495 | 0.464 |
| away_team_wins_last_5 | 1.521 | 1.962 | 1.846 | 0.441 |
| home_team_home_conceded_avg | 1.114 | 1.244 | 1.353 | 0.239 |
| home_team_home_goals_avg | 1.427 | 1.272 | 1.263 | 0.164 |
| away_team_away_conceded_avg | 1.385 | 1.298 | 1.324 | 0.088 |
| away_team_away_goals_avg | 1.237 | 1.283 | 1.218 | 0.065 |
| away_team_away_win_rate | 0.320 | 0.384 | 0.361 | 0.064 |
| home_team_home_win_rate | 0.412 | 0.385 | 0.363 | 0.049 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\sweden1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\sweden1\charts\relationships_home_win_pct_by_position.png)

