# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:08:24+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Prva liga (Slovenia)
- Scope: league `slovenia1`

- Matches analysed: **164** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_points_last_5 | 0.300 | -0.058 | 0.196 |
| home_position_before_match | -0.330 | 0.094 | -0.192 |
| home_team_wins_last_5 | 0.278 | -0.043 | 0.190 |
| home_team_goals_scored_last_5 | 0.259 | -0.079 | 0.147 |
| home_rest_days | 0.121 | 0.031 | 0.122 |
| home_team_home_win_rate | 0.127 | 0.010 | 0.110 |
| away_team_away_goals_avg | -0.182 | 0.317 | 0.100 |
| home_team_goals_conceded_last_5 | -0.184 | 0.064 | -0.099 |
| away_team_wins_last_5 | -0.133 | 0.249 | 0.087 |
| away_rest_days | 0.145 | -0.042 | 0.085 |
| points_difference | 0.393 | -0.298 | 0.084 |
| position_difference | -0.378 | 0.283 | -0.084 |
| away_position_before_match | 0.196 | -0.299 | -0.075 |
| home_team_home_goals_avg | 0.176 | -0.092 | 0.070 |
| away_team_points_last_5 | -0.150 | 0.241 | 0.068 |
| away_team_away_win_rate | -0.189 | 0.265 | 0.055 |
| away_team_goals_conceded_last_5 | 0.164 | -0.236 | -0.053 |
| rest_days_difference | -0.067 | 0.121 | 0.040 |
| home_points_before_match | 0.192 | -0.150 | 0.038 |
| home_team_home_conceded_avg | -0.123 | 0.086 | -0.033 |
| away_team_goals_scored_last_5 | -0.133 | 0.172 | 0.028 |
| away_points_before_match | -0.114 | 0.082 | -0.028 |
| away_team_away_conceded_avg | 0.143 | -0.155 | -0.006 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 29 | 7 | 5 | 17 | 24.1% | 17.2% | 58.6% |
| -4..-2 | 26 | 12 | 8 | 6 | 46.2% | 30.8% | 23.1% |
| -1..1 | 48 | 22 | 8 | 18 | 45.8% | 16.7% | 37.5% |
| 2..4 | 41 | 24 | 6 | 11 | 58.5% | 14.6% | 26.8% |
| >4 | 20 | 16 | 3 | 1 | 80.0% | 15.0% | 5.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 11 | 11 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| -5..-2 | 50 | 27 | 12 | 11 | 54.0% | 24.0% | 22.0% |
| -1..1 | 36 | 20 | 3 | 13 | 55.6% | 8.3% | 36.1% |
| 2..5 | 51 | 20 | 14 | 17 | 39.2% | 27.5% | 33.3% |
| >=6 | 16 | 3 | 1 | 12 | 18.8% | 6.2% | 75.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 23 | 14 | 4 | 5 | 60.9% | 17.4% | 21.7% |
| -1..0 | 32 | 18 | 5 | 9 | 56.2% | 15.6% | 28.1% |
| 0 | 43 | 23 | 8 | 12 | 53.5% | 18.6% | 27.9% |
| 1..2 | 53 | 21 | 11 | 21 | 39.6% | 20.8% | 39.6% |
| >2 | 7 | 2 | 1 | 4 | 28.6% | 14.3% | 57.1% |
| unknown | 6 | 3 | 1 | 2 | 50.0% | 16.7% | 33.3% |
- *6 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **47.5%** home win (47/99)
- `>= 0.5` tier: **52.3%** home win (34/65)
- Home-win gap (>= split minus < split): **+4.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 99 | 47 | 18 | 34 | 47.5% |
| high | >= 0.5 | 65 | 34 | 12 | 19 | 52.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.025 | 0.100 | -6.415 | 10.440 |
| home_points_before_match | 25.877 | 20.467 | 19.755 | 6.122 |
| away_points_before_match | 21.852 | 20.367 | 26.170 | 5.803 |
| away_rest_days | 10.192 | 10.897 | 7.137 | 3.759 |
| position_difference | -1.284 | 0.400 | 1.849 | 3.133 |
| home_rest_days | 9.256 | 10.733 | 7.686 | 3.047 |
| away_team_goals_conceded_last_5 | 7.827 | 7.067 | 5.623 | 2.205 |
| away_position_before_match | 6.185 | 5.400 | 4.321 | 1.864 |
| away_team_points_last_5 | 5.494 | 7.000 | 7.321 | 1.827 |
| home_team_points_last_5 | 6.765 | 6.600 | 5.245 | 1.520 |
| rest_days_difference | -0.936 | 0.034 | 0.549 | 1.485 |
| home_team_goals_scored_last_5 | 7.444 | 6.967 | 6.094 | 1.350 |
| away_team_goals_scored_last_5 | 6.321 | 7.600 | 7.642 | 1.321 |
| home_position_before_match | 4.901 | 5.800 | 6.170 | 1.269 |
| home_team_goals_conceded_last_5 | 6.593 | 7.333 | 7.566 | 0.973 |
| away_team_wins_last_5 | 1.543 | 2.033 | 2.151 | 0.608 |
| away_team_away_goals_avg | 1.177 | 1.495 | 1.730 | 0.552 |
| home_team_wins_last_5 | 1.951 | 1.900 | 1.491 | 0.460 |
| away_team_away_conceded_avg | 1.612 | 1.494 | 1.334 | 0.278 |
| home_team_home_goals_avg | 1.601 | 1.574 | 1.435 | 0.166 |
| away_team_away_win_rate | 0.262 | 0.381 | 0.419 | 0.157 |
| home_team_home_conceded_avg | 1.323 | 1.454 | 1.468 | 0.146 |
| home_team_home_win_rate | 0.446 | 0.425 | 0.422 | 0.024 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\slovenia1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\slovenia1\charts\relationships_home_win_pct_by_position.png)

