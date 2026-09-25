# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:58:31+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Ykkosliiga (Finland)
- Scope: league `finland2`

- Matches analysed: **255** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.247 | -0.076 | 0.127 |
| away_team_away_goals_avg | 0.065 | 0.114 | 0.123 |
| home_team_home_goals_avg | 0.143 | -0.009 | 0.097 |
| home_team_goals_scored_last_5 | 0.120 | 0.012 | 0.095 |
| away_team_goals_conceded_last_5 | 0.165 | -0.063 | 0.077 |
| home_team_goals_conceded_last_5 | 0.024 | 0.075 | 0.068 |
| away_team_goals_scored_last_5 | -0.024 | 0.110 | 0.056 |
| away_team_away_win_rate | -0.193 | 0.128 | -0.054 |
| home_position_before_match | -0.180 | 0.121 | -0.049 |
| away_rest_days | -0.074 | 0.014 | -0.046 |
| rest_days_difference | 0.035 | 0.021 | 0.041 |
| home_team_home_conceded_avg | 0.031 | 0.027 | 0.041 |
| away_team_wins_last_5 | -0.176 | 0.136 | -0.036 |
| position_difference | -0.267 | 0.250 | -0.026 |
| home_rest_days | -0.051 | 0.021 | -0.024 |
| home_team_home_win_rate | 0.079 | -0.050 | 0.024 |
| home_team_points_last_5 | 0.073 | -0.057 | 0.015 |
| away_position_before_match | 0.191 | -0.229 | -0.014 |
| home_points_before_match | 0.075 | -0.060 | 0.014 |
| away_points_before_match | -0.129 | 0.158 | 0.012 |
| away_team_points_last_5 | -0.170 | 0.168 | -0.011 |
| home_team_wins_last_5 | 0.076 | -0.070 | 0.008 |
| points_difference | 0.229 | -0.244 | 0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 39 | 10 | 6 | 23 | 25.6% | 15.4% | 59.0% |
| -4..-2 | 56 | 18 | 18 | 20 | 32.1% | 32.1% | 35.7% |
| -1..1 | 80 | 37 | 16 | 27 | 46.2% | 20.0% | 33.8% |
| 2..4 | 41 | 23 | 8 | 10 | 56.1% | 19.5% | 24.4% |
| >4 | 39 | 20 | 13 | 6 | 51.3% | 33.3% | 15.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 19 | 12 | 5 | 2 | 63.2% | 26.3% | 10.5% |
| -5..-2 | 82 | 47 | 16 | 19 | 57.3% | 19.5% | 23.2% |
| -1..1 | 60 | 28 | 17 | 15 | 46.7% | 28.3% | 25.0% |
| 2..5 | 72 | 18 | 20 | 34 | 25.0% | 27.8% | 47.2% |
| >=6 | 22 | 3 | 3 | 16 | 13.6% | 13.6% | 72.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 26 | 8 | 10 | 8 | 30.8% | 38.5% | 30.8% |
| -1..0 | 57 | 29 | 13 | 15 | 50.9% | 22.8% | 26.3% |
| 0 | 85 | 31 | 19 | 35 | 36.5% | 22.4% | 41.2% |
| 1..2 | 59 | 26 | 12 | 21 | 44.1% | 20.3% | 35.6% |
| >2 | 17 | 9 | 4 | 4 | 52.9% | 23.5% | 23.5% |
| unknown | 11 | 5 | 3 | 3 | 45.5% | 27.3% | 27.3% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.9%** home win (21/62)
- `>= 0.5` tier: **45.1%** home win (87/193)
- Home-win gap (>= split minus < split): **+11.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 62 | 21 | 16 | 25 | 33.9% |
| high | >= 0.5 | 193 | 87 | 45 | 61 | 45.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.287 | 0.164 | -4.105 | 8.392 |
| away_points_before_match | 14.306 | 16.738 | 19.733 | 5.427 |
| position_difference | -1.546 | 0.000 | 1.756 | 3.302 |
| home_points_before_match | 18.593 | 16.902 | 15.628 | 2.965 |
| away_position_before_match | 6.370 | 5.689 | 4.407 | 1.963 |
| away_team_points_last_5 | 5.472 | 5.672 | 7.326 | 1.853 |
| away_team_goals_conceded_last_5 | 7.167 | 6.328 | 5.733 | 1.434 |
| home_position_before_match | 4.824 | 5.689 | 6.163 | 1.339 |
| home_team_goals_scored_last_5 | 6.926 | 6.705 | 5.791 | 1.135 |
| home_team_points_last_5 | 6.444 | 6.131 | 5.384 | 1.061 |
| away_team_goals_scored_last_5 | 6.435 | 6.000 | 6.965 | 0.965 |
| away_rest_days | 6.615 | 7.466 | 7.169 | 0.850 |
| away_team_wins_last_5 | 2.509 | 2.590 | 3.163 | 0.654 |
| home_rest_days | 6.709 | 7.203 | 7.313 | 0.605 |
| away_team_away_conceded_avg | 1.661 | 1.463 | 1.139 | 0.521 |
| rest_days_difference | 0.068 | -0.276 | 0.145 | 0.420 |
| home_team_wins_last_5 | 2.889 | 2.754 | 2.477 | 0.412 |
| home_team_home_conceded_avg | 1.206 | 1.533 | 1.235 | 0.327 |
| home_team_goals_conceded_last_5 | 6.574 | 6.361 | 6.605 | 0.244 |
| home_team_home_goals_avg | 1.557 | 1.480 | 1.351 | 0.206 |
| away_team_away_win_rate | 0.474 | 0.514 | 0.618 | 0.144 |
| home_team_home_win_rate | 0.656 | 0.596 | 0.586 | 0.070 |
| away_team_away_goals_avg | 1.295 | 1.281 | 1.249 | 0.046 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\finland2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\finland2\charts\relationships_home_win_pct_by_position.png)

