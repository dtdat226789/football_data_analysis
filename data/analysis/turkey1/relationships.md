# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:50:07+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super Lig (Turkey)
- Scope: league `turkey1`

- Matches analysed: **360** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_goals_avg | 0.262 | -0.040 | 0.174 |
| home_team_goals_scored_last_5 | 0.259 | -0.057 | 0.161 |
| away_team_away_win_rate | 0.026 | 0.158 | 0.131 |
| home_team_points_last_5 | 0.228 | -0.071 | 0.127 |
| home_team_home_win_rate | 0.215 | -0.074 | 0.114 |
| home_points_before_match | 0.195 | -0.056 | 0.111 |
| home_position_before_match | -0.194 | 0.057 | -0.111 |
| home_team_wins_last_5 | 0.172 | -0.045 | 0.102 |
| away_team_wins_last_5 | 0.007 | 0.135 | 0.099 |
| away_team_goals_scored_last_5 | -0.060 | 0.171 | 0.073 |
| points_difference | 0.239 | -0.166 | 0.068 |
| away_position_before_match | 0.137 | -0.248 | -0.067 |
| away_team_points_last_5 | -0.041 | 0.138 | 0.065 |
| away_team_away_goals_avg | -0.054 | 0.151 | 0.064 |
| home_rest_days | -0.072 | -0.004 | -0.059 |
| away_points_before_match | 0.009 | 0.072 | 0.058 |
| rest_days_difference | -0.116 | 0.069 | -0.043 |
| away_rest_days | -0.028 | -0.029 | -0.042 |
| home_team_goals_conceded_last_5 | -0.051 | 0.001 | -0.038 |
| away_team_away_conceded_avg | 0.095 | -0.056 | 0.034 |
| position_difference | -0.243 | 0.222 | -0.033 |
| home_team_home_conceded_avg | -0.100 | 0.077 | -0.024 |
| away_team_goals_conceded_last_5 | 0.046 | -0.061 | -0.007 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 48 | 13 | 12 | 23 | 27.1% | 25.0% | 47.9% |
| -4..-2 | 89 | 34 | 20 | 35 | 38.2% | 22.5% | 39.3% |
| -1..1 | 107 | 42 | 35 | 30 | 39.3% | 32.7% | 28.0% |
| 2..4 | 62 | 34 | 14 | 14 | 54.8% | 22.6% | 22.6% |
| >4 | 54 | 32 | 19 | 3 | 59.3% | 35.2% | 5.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 84 | 51 | 22 | 11 | 60.7% | 26.2% | 13.1% |
| -5..-2 | 58 | 24 | 25 | 9 | 41.4% | 43.1% | 15.5% |
| -1..1 | 60 | 25 | 19 | 16 | 41.7% | 31.7% | 26.7% |
| 2..5 | 69 | 28 | 19 | 22 | 40.6% | 27.5% | 31.9% |
| >=6 | 89 | 27 | 15 | 47 | 30.3% | 16.9% | 52.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 51 | 26 | 14 | 11 | 51.0% | 27.5% | 21.6% |
| -1..0 | 65 | 29 | 16 | 20 | 44.6% | 24.6% | 30.8% |
| 0 | 114 | 55 | 29 | 30 | 48.2% | 25.4% | 26.3% |
| 1..2 | 101 | 36 | 30 | 35 | 35.6% | 29.7% | 34.7% |
| >2 | 9 | 0 | 4 | 5 | 0.0% | 44.4% | 55.6% |
| unknown | 20 | 9 | 7 | 4 | 45.0% | 35.0% | 20.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **39.2%** home win (40/102)
- `>= 0.5` tier: **44.6%** home win (115/258)
- Home-win gap (>= split minus < split): **+5.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 102 | 40 | 28 | 34 | 39.2% |
| high | >= 0.5 | 258 | 115 | 72 | 71 | 44.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.548 | 2.190 | -6.295 | 8.844 |
| home_points_before_match | 21.555 | 20.480 | 15.038 | 6.517 |
| position_difference | -1.587 | -0.970 | 3.781 | 5.368 |
| away_position_before_match | 10.865 | 9.930 | 7.352 | 3.512 |
| away_points_before_match | 19.006 | 18.290 | 21.333 | 3.043 |
| home_position_before_match | 9.277 | 8.960 | 11.133 | 2.173 |
| home_team_goals_scored_last_5 | 6.200 | 5.740 | 4.562 | 1.638 |
| away_team_goals_scored_last_5 | 4.974 | 5.650 | 6.562 | 1.588 |
| home_team_points_last_5 | 6.161 | 6.130 | 4.600 | 1.561 |
| away_team_points_last_5 | 5.265 | 5.860 | 6.562 | 1.297 |
| away_team_goals_conceded_last_5 | 5.535 | 6.020 | 5.000 | 1.020 |
| rest_days_difference | -0.411 | 0.011 | 0.168 | 0.579 |
| home_rest_days | 7.905 | 8.426 | 8.297 | 0.521 |
| home_team_wins_last_5 | 2.845 | 2.850 | 2.390 | 0.460 |
| away_team_wins_last_5 | 2.658 | 2.760 | 2.981 | 0.323 |
| home_team_home_goals_avg | 1.283 | 1.202 | 0.996 | 0.287 |
| away_rest_days | 8.313 | 8.415 | 8.129 | 0.286 |
| home_team_goals_conceded_last_5 | 5.594 | 5.840 | 5.743 | 0.246 |
| away_team_away_goals_avg | 1.015 | 1.179 | 1.253 | 0.238 |
| away_team_away_conceded_avg | 1.214 | 1.272 | 1.035 | 0.238 |
| home_team_home_conceded_avg | 1.076 | 1.159 | 1.207 | 0.131 |
| home_team_home_win_rate | 0.641 | 0.623 | 0.518 | 0.123 |
| away_team_away_win_rate | 0.510 | 0.577 | 0.574 | 0.067 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\turkey1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\turkey1\charts\relationships_home_win_pct_by_position.png)

