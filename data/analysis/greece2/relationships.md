# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:00:16+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super League 2 (Greece)
- Scope: league `greece2`

- Matches analysed: **289** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_conceded_last_5 | 0.231 | -0.096 | 0.119 |
| away_team_away_win_rate | -0.251 | 0.142 | -0.103 |
| away_team_away_goals_avg | -0.251 | 0.148 | -0.099 |
| away_position_before_match | 0.319 | -0.236 | 0.091 |
| away_rest_days | -0.032 | -0.078 | -0.082 |
| away_points_before_match | -0.192 | 0.105 | -0.081 |
| position_difference | -0.440 | 0.394 | -0.077 |
| home_team_home_win_rate | 0.187 | -0.111 | 0.073 |
| away_team_away_conceded_avg | 0.218 | -0.150 | 0.071 |
| away_team_wins_last_5 | -0.228 | 0.164 | -0.068 |
| away_team_points_last_5 | -0.264 | 0.206 | -0.068 |
| home_rest_days | -0.024 | -0.062 | -0.064 |
| home_team_home_conceded_avg | -0.133 | 0.065 | -0.062 |
| home_team_wins_last_5 | 0.196 | -0.137 | 0.062 |
| points_difference | 0.377 | -0.358 | 0.052 |
| rest_days_difference | 0.023 | 0.044 | 0.051 |
| home_team_goals_scored_last_5 | 0.190 | -0.153 | 0.045 |
| home_points_before_match | 0.118 | -0.189 | -0.038 |
| away_team_goals_scored_last_5 | -0.191 | 0.256 | 0.027 |
| home_team_points_last_5 | 0.183 | -0.177 | 0.023 |
| home_team_goals_conceded_last_5 | -0.167 | 0.181 | -0.007 |
| home_position_before_match | -0.225 | 0.251 | -0.004 |
| home_team_home_goals_avg | 0.186 | -0.207 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 54 | 7 | 10 | 37 | 13.0% | 18.5% | 68.5% |
| -4..-2 | 56 | 18 | 13 | 25 | 32.1% | 23.2% | 44.6% |
| -1..1 | 85 | 40 | 29 | 16 | 47.1% | 34.1% | 18.8% |
| 2..4 | 38 | 23 | 7 | 8 | 60.5% | 18.4% | 21.1% |
| >4 | 56 | 43 | 8 | 5 | 76.8% | 14.3% | 8.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 62 | 49 | 10 | 3 | 79.0% | 16.1% | 4.8% |
| -5..-2 | 46 | 26 | 13 | 7 | 56.5% | 28.3% | 15.2% |
| -1..1 | 55 | 26 | 19 | 10 | 47.3% | 34.5% | 18.2% |
| 2..5 | 57 | 21 | 15 | 21 | 36.8% | 26.3% | 36.8% |
| >=6 | 69 | 9 | 10 | 50 | 13.0% | 14.5% | 72.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 5 | 2 | 2 | 1 | 40.0% | 40.0% | 20.0% |
| -1..0 | 46 | 19 | 9 | 18 | 41.3% | 19.6% | 39.1% |
| 0 | 169 | 82 | 35 | 52 | 48.5% | 20.7% | 30.8% |
| 1..2 | 46 | 17 | 11 | 18 | 37.0% | 23.9% | 39.1% |
| >2 | 5 | 3 | 1 | 1 | 60.0% | 20.0% | 20.0% |
| unknown | 18 | 8 | 9 | 1 | 44.4% | 50.0% | 5.6% |
- *18 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.9%** home win (36/95)
- `>= 0.5` tier: **49.0%** home win (95/194)
- Home-win gap (>= split minus < split): **+11.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 95 | 36 | 20 | 39 | 37.9% |
| high | >= 0.5 | 194 | 95 | 47 | 52 | 49.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.038 | 0.328 | -8.000 | 13.038 |
| position_difference | -3.229 | 0.075 | 5.582 | 8.811 |
| home_points_before_match | 18.282 | 16.269 | 11.396 | 6.887 |
| away_points_before_match | 13.244 | 15.940 | 19.396 | 6.151 |
| away_position_before_match | 12.405 | 9.627 | 7.945 | 4.460 |
| home_position_before_match | 9.176 | 9.701 | 13.527 | 4.352 |
| away_team_points_last_5 | 4.344 | 6.269 | 7.549 | 3.206 |
| away_team_goals_scored_last_5 | 3.672 | 5.045 | 6.110 | 2.438 |
| home_team_points_last_5 | 6.634 | 5.776 | 4.341 | 2.293 |
| home_team_goals_conceded_last_5 | 3.893 | 4.433 | 6.121 | 2.228 |
| home_team_goals_scored_last_5 | 5.221 | 4.582 | 3.626 | 1.595 |
| away_team_goals_conceded_last_5 | 5.244 | 4.030 | 3.978 | 1.266 |
| home_rest_days | 8.106 | 9.000 | 7.744 | 1.256 |
| away_team_wins_last_5 | 2.115 | 2.716 | 3.198 | 1.083 |
| away_rest_days | 8.081 | 8.862 | 7.789 | 1.073 |
| home_team_wins_last_5 | 2.908 | 2.403 | 2.121 | 0.788 |
| away_team_away_goals_avg | 0.656 | 0.936 | 1.085 | 0.429 |
| home_team_home_goals_avg | 1.275 | 1.179 | 0.855 | 0.420 |
| away_team_away_conceded_avg | 1.326 | 1.131 | 0.956 | 0.370 |
| away_team_away_win_rate | 0.409 | 0.509 | 0.643 | 0.234 |
| home_team_home_conceded_avg | 0.789 | 0.830 | 1.007 | 0.218 |
| rest_days_difference | 0.024 | 0.138 | -0.044 | 0.182 |
| home_team_home_win_rate | 0.643 | 0.563 | 0.512 | 0.131 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\greece2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\greece2\charts\relationships_home_win_pct_by_position.png)

