# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:44:07+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Division 1 (Saudi Arabia)
- Scope: league `saudi2`

- Matches analysed: **362** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.297 | -0.097 | 0.166 |
| home_points_before_match | 0.249 | -0.083 | 0.138 |
| home_team_goals_conceded_last_5 | 0.041 | 0.133 | 0.123 |
| home_team_home_goals_avg | 0.289 | -0.152 | 0.121 |
| away_points_before_match | 0.015 | 0.159 | 0.121 |
| away_team_goals_conceded_last_5 | 0.220 | -0.087 | 0.113 |
| away_team_goals_scored_last_5 | -0.035 | 0.176 | 0.093 |
| home_team_wins_last_5 | 0.226 | -0.148 | 0.075 |
| away_position_before_match | 0.237 | -0.170 | 0.069 |
| home_team_home_conceded_avg | 0.022 | 0.075 | 0.069 |
| away_team_away_goals_avg | -0.169 | 0.100 | -0.064 |
| away_team_away_win_rate | -0.160 | 0.091 | -0.063 |
| away_team_away_conceded_avg | 0.150 | -0.087 | 0.058 |
| away_team_points_last_5 | -0.089 | 0.176 | 0.051 |
| position_difference | -0.309 | 0.283 | -0.048 |
| home_team_points_last_5 | 0.220 | -0.183 | 0.046 |
| away_team_wins_last_5 | -0.068 | 0.143 | 0.045 |
| home_team_home_win_rate | 0.151 | -0.114 | 0.040 |
| points_difference | 0.295 | -0.304 | 0.022 |
| away_rest_days | -0.053 | 0.083 | 0.014 |
| rest_days_difference | -0.053 | 0.043 | -0.012 |
| home_rest_days | -0.075 | 0.098 | 0.007 |
| home_position_before_match | -0.188 | 0.219 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 62 | 11 | 12 | 39 | 17.7% | 19.4% | 62.9% |
| -4..-2 | 58 | 18 | 14 | 26 | 31.0% | 24.1% | 44.8% |
| -1..1 | 110 | 45 | 35 | 30 | 40.9% | 31.8% | 27.3% |
| 2..4 | 73 | 31 | 19 | 23 | 42.5% | 26.0% | 31.5% |
| >4 | 59 | 39 | 16 | 4 | 66.1% | 27.1% | 6.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 89 | 52 | 22 | 15 | 58.4% | 24.7% | 16.9% |
| -5..-2 | 67 | 33 | 19 | 15 | 49.3% | 28.4% | 22.4% |
| -1..1 | 57 | 26 | 15 | 16 | 45.6% | 26.3% | 28.1% |
| 2..5 | 66 | 20 | 23 | 23 | 30.3% | 34.8% | 34.8% |
| >=6 | 83 | 13 | 17 | 53 | 15.7% | 20.5% | 63.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 34 | 10 | 15 | 9 | 29.4% | 44.1% | 26.5% |
| -1..0 | 86 | 39 | 18 | 29 | 45.3% | 20.9% | 33.7% |
| 0 | 118 | 59 | 25 | 34 | 50.0% | 21.2% | 28.8% |
| 1..2 | 100 | 30 | 31 | 39 | 30.0% | 31.0% | 39.0% |
| >2 | 6 | 2 | 0 | 4 | 33.3% | 0.0% | 66.7% |
| unknown | 18 | 4 | 7 | 7 | 22.2% | 38.9% | 38.9% |
- *18 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **28.6%** home win (32/112)
- `>= 0.5` tier: **44.8%** home win (112/250)
- Home-win gap (>= split minus < split): **+16.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 112 | 32 | 39 | 41 | 28.6% |
| high | >= 0.5 | 250 | 112 | 57 | 81 | 44.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 6.479 | -0.885 | -6.664 | 13.143 |
| home_points_before_match | 25.736 | 14.365 | 17.893 | 11.372 |
| away_points_before_match | 19.257 | 15.250 | 24.557 | 9.307 |
| position_difference | -3.215 | -0.146 | 3.352 | 6.568 |
| away_position_before_match | 11.451 | 9.656 | 7.795 | 3.656 |
| home_position_before_match | 8.236 | 9.510 | 11.148 | 2.911 |
| home_team_points_last_5 | 7.028 | 5.458 | 4.770 | 2.257 |
| home_team_goals_scored_last_5 | 7.208 | 5.594 | 5.131 | 2.077 |
| away_team_points_last_5 | 5.250 | 5.115 | 7.107 | 1.992 |
| away_team_goals_conceded_last_5 | 7.007 | 5.396 | 5.238 | 1.769 |
| away_team_goals_scored_last_5 | 5.715 | 5.344 | 7.049 | 1.705 |
| home_rest_days | 6.543 | 7.146 | 7.896 | 1.353 |
| home_team_goals_conceded_last_5 | 6.111 | 5.469 | 6.615 | 1.146 |
| away_rest_days | 6.557 | 7.427 | 7.557 | 0.999 |
| home_team_wins_last_5 | 3.069 | 2.542 | 2.311 | 0.758 |
| rest_days_difference | -0.014 | -0.281 | 0.339 | 0.620 |
| away_team_wins_last_5 | 2.528 | 2.510 | 3.090 | 0.580 |
| home_team_home_goals_avg | 1.479 | 1.085 | 0.995 | 0.483 |
| away_team_away_goals_avg | 1.080 | 1.174 | 1.459 | 0.379 |
| away_team_away_conceded_avg | 1.403 | 1.065 | 1.124 | 0.338 |
| away_team_away_win_rate | 0.498 | 0.610 | 0.659 | 0.161 |
| home_team_home_conceded_avg | 1.199 | 1.187 | 1.290 | 0.103 |
| home_team_home_win_rate | 0.636 | 0.558 | 0.535 | 0.101 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\saudi2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\saudi2\charts\relationships_home_win_pct_by_position.png)

