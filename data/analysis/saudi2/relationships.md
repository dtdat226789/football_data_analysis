# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:05:39+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Division 1 (Saudi Arabia)
- Scope: league `saudi2`

- Matches analysed: **309** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_goals_avg | -0.241 | 0.128 | -0.102 |
| home_team_goals_scored_last_5 | 0.280 | -0.179 | 0.097 |
| home_points_before_match | 0.236 | -0.157 | 0.077 |
| home_team_goals_conceded_last_5 | -0.015 | 0.104 | 0.062 |
| away_points_before_match | -0.036 | 0.125 | 0.060 |
| away_team_away_win_rate | -0.180 | 0.131 | -0.051 |
| away_position_before_match | 0.248 | -0.210 | 0.049 |
| home_team_home_goals_avg | 0.269 | -0.234 | 0.049 |
| home_team_wins_last_5 | 0.173 | -0.246 | -0.037 |
| away_team_goals_conceded_last_5 | 0.187 | -0.161 | 0.035 |
| position_difference | -0.341 | 0.338 | -0.033 |
| away_team_goals_scored_last_5 | -0.112 | 0.162 | 0.026 |
| home_rest_days | -0.104 | 0.083 | -0.025 |
| rest_days_difference | -0.065 | 0.039 | -0.025 |
| home_team_points_last_5 | 0.192 | -0.247 | -0.023 |
| home_team_home_win_rate | 0.162 | -0.212 | -0.022 |
| points_difference | 0.316 | -0.326 | 0.020 |
| away_rest_days | -0.079 | 0.070 | -0.015 |
| home_team_home_conceded_avg | -0.048 | 0.066 | 0.009 |
| away_team_away_conceded_avg | 0.130 | -0.138 | 0.006 |
| away_team_wins_last_5 | -0.151 | 0.176 | 0.005 |
| home_position_before_match | -0.228 | 0.260 | 0.003 |
| away_team_points_last_5 | -0.155 | 0.172 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 60 | 11 | 11 | 38 | 18.3% | 18.3% | 63.3% |
| -4..-2 | 49 | 15 | 9 | 25 | 30.6% | 18.4% | 51.0% |
| -1..1 | 81 | 38 | 22 | 21 | 46.9% | 27.2% | 25.9% |
| 2..4 | 62 | 26 | 15 | 21 | 41.9% | 24.2% | 33.9% |
| >4 | 57 | 38 | 15 | 4 | 66.7% | 26.3% | 7.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 78 | 49 | 17 | 12 | 62.8% | 21.8% | 15.4% |
| -5..-2 | 56 | 29 | 13 | 14 | 51.8% | 23.2% | 25.0% |
| -1..1 | 42 | 21 | 11 | 10 | 50.0% | 26.2% | 23.8% |
| 2..5 | 60 | 19 | 18 | 23 | 31.7% | 30.0% | 38.3% |
| >=6 | 73 | 10 | 13 | 50 | 13.7% | 17.8% | 68.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 30 | 8 | 13 | 9 | 26.7% | 43.3% | 30.0% |
| -1..0 | 78 | 37 | 15 | 26 | 47.4% | 19.2% | 33.3% |
| 0 | 105 | 55 | 18 | 32 | 52.4% | 17.1% | 30.5% |
| 1..2 | 81 | 24 | 22 | 35 | 29.6% | 27.2% | 43.2% |
| >2 | 6 | 2 | 0 | 4 | 33.3% | 0.0% | 66.7% |
| unknown | 9 | 2 | 4 | 3 | 22.2% | 44.4% | 33.3% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **35.9%** home win (75/209)
- `>= 0.5` tier: **53.0%** home win (53/100)
- Home-win gap (>= split minus < split): **+17.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 209 | 75 | 49 | 85 | 35.9% |
| high | >= 0.5 | 100 | 53 | 23 | 24 | 53.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 7.211 | -1.125 | -7.450 | 14.660 |
| home_points_before_match | 28.469 | 18.139 | 19.761 | 10.330 |
| away_points_before_match | 21.258 | 19.264 | 27.211 | 7.947 |
| position_difference | -3.547 | -0.097 | 3.835 | 7.382 |
| away_position_before_match | 11.516 | 9.722 | 7.560 | 3.956 |
| home_position_before_match | 7.969 | 9.625 | 11.394 | 3.426 |
| home_team_points_last_5 | 7.422 | 6.264 | 5.073 | 2.348 |
| away_team_points_last_5 | 5.500 | 5.750 | 7.679 | 2.179 |
| home_team_goals_scored_last_5 | 7.711 | 6.708 | 5.569 | 2.142 |
| away_team_goals_conceded_last_5 | 7.438 | 6.500 | 5.642 | 1.795 |
| away_team_goals_scored_last_5 | 6.047 | 6.347 | 7.679 | 1.632 |
| home_rest_days | 6.603 | 7.588 | 8.104 | 1.501 |
| away_rest_days | 6.627 | 8.029 | 7.755 | 1.402 |
| rest_days_difference | -0.024 | -0.441 | 0.349 | 0.790 |
| home_team_wins_last_5 | 2.117 | 1.708 | 1.339 | 0.778 |
| away_team_wins_last_5 | 1.438 | 1.528 | 2.193 | 0.755 |
| home_team_goals_conceded_last_5 | 6.500 | 6.472 | 7.193 | 0.720 |
| home_team_home_goals_avg | 1.561 | 1.246 | 1.088 | 0.473 |
| away_team_away_goals_avg | 1.120 | 1.302 | 1.583 | 0.463 |
| away_team_away_conceded_avg | 1.455 | 1.247 | 1.207 | 0.247 |
| home_team_home_conceded_avg | 1.232 | 1.347 | 1.406 | 0.175 |
| away_team_away_win_rate | 0.271 | 0.328 | 0.422 | 0.151 |
| home_team_home_win_rate | 0.404 | 0.335 | 0.278 | 0.126 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\saudi2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\saudi2\charts\relationships_home_win_pct_by_position.png)

