# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:43:34+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premier League (Russia)
- Scope: league `russia`

- Matches analysed: **320** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.187 | -0.023 | 0.121 |
| away_points_before_match | -0.108 | -0.028 | -0.099 |
| home_team_home_win_rate | 0.055 | -0.176 | -0.085 |
| points_difference | 0.273 | -0.166 | 0.083 |
| home_team_points_last_5 | 0.203 | -0.131 | 0.056 |
| home_position_before_match | -0.191 | 0.125 | -0.051 |
| position_difference | -0.290 | 0.228 | -0.051 |
| home_team_home_goals_avg | 0.172 | -0.123 | 0.039 |
| rest_days_difference | 0.020 | -0.077 | -0.039 |
| home_points_before_match | 0.112 | -0.163 | -0.034 |
| home_team_wins_last_5 | 0.181 | -0.141 | 0.033 |
| away_rest_days | 0.075 | -0.048 | 0.021 |
| away_team_wins_last_5 | -0.073 | 0.047 | -0.020 |
| away_team_goals_conceded_last_5 | 0.173 | -0.150 | 0.020 |
| home_team_home_conceded_avg | 0.008 | 0.020 | 0.020 |
| away_position_before_match | 0.215 | -0.194 | 0.020 |
| home_rest_days | 0.073 | -0.053 | 0.016 |
| away_team_goals_scored_last_5 | -0.054 | 0.038 | -0.013 |
| away_team_away_win_rate | -0.121 | 0.140 | 0.011 |
| away_team_away_conceded_avg | 0.163 | -0.180 | -0.008 |
| home_team_goals_conceded_last_5 | -0.045 | 0.038 | -0.006 |
| away_team_away_goals_avg | -0.058 | 0.065 | 0.004 |
| away_team_points_last_5 | -0.066 | 0.070 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 54 | 14 | 17 | 23 | 25.9% | 31.5% | 42.6% |
| -4..-2 | 60 | 19 | 20 | 21 | 31.7% | 33.3% | 35.0% |
| -1..1 | 106 | 41 | 33 | 32 | 38.7% | 31.1% | 30.2% |
| 2..4 | 53 | 33 | 15 | 5 | 62.3% | 28.3% | 9.4% |
| >4 | 47 | 30 | 8 | 9 | 63.8% | 17.0% | 19.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 71 | 47 | 14 | 10 | 66.2% | 19.7% | 14.1% |
| -5..-2 | 59 | 32 | 20 | 7 | 54.2% | 33.9% | 11.9% |
| -1..1 | 53 | 22 | 17 | 14 | 41.5% | 32.1% | 26.4% |
| 2..5 | 70 | 23 | 17 | 30 | 32.9% | 24.3% | 42.9% |
| >=6 | 67 | 13 | 25 | 29 | 19.4% | 37.3% | 43.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 11 | 3 | 5 | 3 | 27.3% | 45.5% | 27.3% |
| -1..0 | 79 | 32 | 19 | 28 | 40.5% | 24.1% | 35.4% |
| 0 | 109 | 49 | 35 | 25 | 45.0% | 32.1% | 22.9% |
| 1..2 | 103 | 47 | 29 | 27 | 45.6% | 28.2% | 26.2% |
| >2 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 18 | 6 | 5 | 7 | 33.3% | 27.8% | 38.9% |
- *18 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **36.6%** home win (26/71)
- `>= 0.5` tier: **44.6%** home win (111/249)
- Home-win gap (>= split minus < split): **+8.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 71 | 26 | 19 | 26 | 36.6% |
| high | >= 0.5 | 249 | 111 | 74 | 64 | 44.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.613 | -1.376 | -4.900 | 8.513 |
| position_difference | -2.569 | 0.763 | 3.056 | 5.625 |
| home_points_before_match | 18.562 | 14.968 | 13.711 | 4.851 |
| home_rest_days | 11.573 | 7.534 | 8.470 | 4.038 |
| away_rest_days | 11.450 | 7.477 | 8.388 | 3.973 |
| away_points_before_match | 14.949 | 16.344 | 18.611 | 3.662 |
| away_position_before_match | 10.307 | 8.226 | 7.433 | 2.873 |
| home_position_before_match | 7.737 | 8.989 | 10.489 | 2.752 |
| home_team_points_last_5 | 6.467 | 5.387 | 4.478 | 1.989 |
| away_team_goals_conceded_last_5 | 6.015 | 5.366 | 4.589 | 1.426 |
| away_team_points_last_5 | 5.226 | 6.290 | 6.178 | 1.064 |
| away_team_goals_scored_last_5 | 5.015 | 6.043 | 5.711 | 1.028 |
| home_team_goals_conceded_last_5 | 5.066 | 5.817 | 5.989 | 0.923 |
| home_team_goals_scored_last_5 | 5.774 | 5.323 | 4.944 | 0.829 |
| home_team_wins_last_5 | 2.993 | 2.591 | 2.278 | 0.715 |
| away_team_wins_last_5 | 2.540 | 2.957 | 2.911 | 0.417 |
| away_team_away_conceded_avg | 1.486 | 1.095 | 1.158 | 0.392 |
| home_team_home_goals_avg | 1.428 | 1.265 | 1.037 | 0.391 |
| away_team_away_goals_avg | 1.026 | 1.137 | 1.220 | 0.194 |
| rest_days_difference | 0.122 | 0.057 | -0.048 | 0.170 |
| home_team_home_conceded_avg | 1.062 | 1.229 | 1.117 | 0.167 |
| away_team_away_win_rate | 0.426 | 0.584 | 0.562 | 0.158 |
| home_team_home_win_rate | 0.689 | 0.649 | 0.569 | 0.120 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\russia\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\russia\charts\relationships_home_win_pct_by_position.png)

