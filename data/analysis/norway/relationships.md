# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:04:09+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Eliteserien (Norway)
- Scope: league `norway`

- Matches analysed: **408** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_goals_avg | 0.213 | -0.094 | 0.108 |
| home_points_before_match | 0.221 | -0.104 | 0.107 |
| away_points_before_match | -0.015 | 0.130 | 0.081 |
| home_team_goals_scored_last_5 | 0.168 | -0.088 | 0.074 |
| home_rest_days | 0.035 | 0.057 | 0.069 |
| away_rest_days | 0.024 | 0.046 | 0.053 |
| home_team_home_win_rate | 0.096 | -0.037 | 0.053 |
| away_team_goals_scored_last_5 | -0.098 | 0.183 | 0.051 |
| away_team_away_conceded_avg | 0.022 | 0.031 | 0.040 |
| home_team_wins_last_5 | 0.132 | -0.095 | 0.040 |
| rest_days_difference | 0.038 | 0.012 | 0.039 |
| away_team_goals_conceded_last_5 | 0.083 | -0.049 | 0.033 |
| away_team_points_last_5 | -0.097 | 0.156 | 0.033 |
| home_team_points_last_5 | 0.168 | -0.147 | 0.033 |
| home_team_goals_conceded_last_5 | -0.100 | 0.157 | 0.031 |
| away_team_away_goals_avg | -0.062 | 0.113 | 0.030 |
| away_position_before_match | 0.160 | -0.141 | 0.030 |
| points_difference | 0.284 | -0.283 | 0.029 |
| away_team_wins_last_5 | -0.068 | 0.109 | 0.023 |
| position_difference | -0.254 | 0.258 | -0.023 |
| away_team_away_win_rate | -0.081 | 0.071 | -0.015 |
| home_position_before_match | -0.191 | 0.215 | -0.002 |
| home_team_home_conceded_avg | -0.128 | 0.143 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 72 | 24 | 17 | 31 | 33.3% | 23.6% | 43.1% |
| -4..-2 | 84 | 30 | 13 | 41 | 35.7% | 15.5% | 48.8% |
| -1..1 | 109 | 62 | 20 | 27 | 56.9% | 18.3% | 24.8% |
| 2..4 | 74 | 41 | 16 | 17 | 55.4% | 21.6% | 23.0% |
| >4 | 69 | 47 | 12 | 10 | 68.1% | 17.4% | 14.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 76 | 56 | 10 | 10 | 73.7% | 13.2% | 13.2% |
| -5..-2 | 91 | 53 | 19 | 19 | 58.2% | 20.9% | 20.9% |
| -1..1 | 71 | 32 | 13 | 26 | 45.1% | 18.3% | 36.6% |
| 2..5 | 79 | 34 | 12 | 33 | 43.0% | 15.2% | 41.8% |
| >=6 | 91 | 29 | 24 | 38 | 31.9% | 26.4% | 41.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 40 | 18 | 8 | 14 | 45.0% | 20.0% | 35.0% |
| -1..0 | 57 | 28 | 12 | 17 | 49.1% | 21.1% | 29.8% |
| 0 | 188 | 92 | 39 | 57 | 48.9% | 20.7% | 30.3% |
| 1..2 | 71 | 39 | 13 | 19 | 54.9% | 18.3% | 26.8% |
| >2 | 35 | 16 | 6 | 13 | 45.7% | 17.1% | 37.1% |
| unknown | 17 | 11 | 0 | 6 | 64.7% | 0.0% | 35.3% |
- *17 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **44.2%** home win (38/86)
- `>= 0.5` tier: **51.6%** home win (166/322)
- Home-win gap (>= split minus < split): **+7.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 86 | 38 | 15 | 33 | 44.2% |
| high | >= 0.5 | 322 | 166 | 63 | 93 | 51.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.137 | -1.564 | -5.373 | 8.510 |
| home_points_before_match | 19.721 | 16.551 | 14.603 | 5.117 |
| position_difference | -1.701 | 1.282 | 2.675 | 4.376 |
| away_points_before_match | 16.583 | 18.115 | 19.976 | 3.393 |
| home_position_before_match | 7.662 | 9.308 | 9.857 | 2.195 |
| away_position_before_match | 9.363 | 8.026 | 7.183 | 2.180 |
| away_team_goals_scored_last_5 | 6.235 | 7.064 | 7.960 | 1.725 |
| away_team_points_last_5 | 5.554 | 6.615 | 7.159 | 1.605 |
| home_team_points_last_5 | 6.574 | 6.282 | 5.214 | 1.359 |
| home_team_goals_scored_last_5 | 7.265 | 6.603 | 6.167 | 1.098 |
| away_rest_days | 8.575 | 8.244 | 9.325 | 1.081 |
| home_team_goals_conceded_last_5 | 6.544 | 7.231 | 7.540 | 0.996 |
| away_team_goals_conceded_last_5 | 7.010 | 7.013 | 6.119 | 0.894 |
| home_rest_days | 8.710 | 8.654 | 9.361 | 0.707 |
| home_team_wins_last_5 | 2.711 | 2.821 | 2.325 | 0.495 |
| rest_days_difference | 0.135 | 0.410 | -0.050 | 0.460 |
| away_team_wins_last_5 | 2.525 | 2.769 | 2.905 | 0.380 |
| home_team_home_goals_avg | 1.736 | 1.472 | 1.417 | 0.318 |
| home_team_home_conceded_avg | 1.051 | 1.336 | 1.290 | 0.285 |
| away_team_away_goals_avg | 1.089 | 1.207 | 1.316 | 0.228 |
| away_team_away_conceded_avg | 1.568 | 1.703 | 1.545 | 0.158 |
| away_team_away_win_rate | 0.427 | 0.471 | 0.512 | 0.086 |
| home_team_home_win_rate | 0.637 | 0.635 | 0.598 | 0.039 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\norway\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\norway\charts\relationships_home_win_pct_by_position.png)

