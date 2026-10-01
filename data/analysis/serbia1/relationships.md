# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:08:09+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Mozzart Bet Super Liga (Serbia)
- Scope: league `serbia1`

- Matches analysed: **297** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_goals_avg | 0.274 | -0.053 | 0.163 |
| home_team_home_win_rate | 0.244 | -0.093 | 0.114 |
| home_team_goals_conceded_last_5 | -0.186 | 0.033 | -0.113 |
| home_position_before_match | -0.265 | 0.118 | -0.112 |
| position_difference | -0.306 | 0.183 | -0.097 |
| home_team_goals_scored_last_5 | 0.203 | -0.077 | 0.095 |
| points_difference | 0.309 | -0.191 | 0.094 |
| away_points_before_match | -0.135 | 0.028 | -0.079 |
| away_team_away_win_rate | -0.086 | 0.198 | 0.073 |
| rest_days_difference | 0.028 | -0.129 | -0.068 |
| home_team_home_conceded_avg | -0.184 | 0.112 | -0.057 |
| away_team_away_conceded_avg | -0.055 | -0.020 | -0.054 |
| away_team_away_goals_avg | -0.109 | 0.180 | 0.044 |
| away_team_wins_last_5 | -0.081 | 0.147 | 0.042 |
| home_team_wins_last_5 | 0.171 | -0.123 | 0.040 |
| home_team_points_last_5 | 0.156 | -0.115 | 0.035 |
| away_team_goals_scored_last_5 | -0.090 | 0.132 | 0.025 |
| home_rest_days | -0.033 | 0.004 | -0.021 |
| away_team_goals_conceded_last_5 | 0.097 | -0.132 | -0.020 |
| away_position_before_match | 0.129 | -0.118 | 0.012 |
| away_team_points_last_5 | -0.110 | 0.130 | 0.010 |
| home_points_before_match | 0.097 | -0.113 | -0.007 |
| away_rest_days | -0.040 | 0.038 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 39 | 9 | 13 | 17 | 23.1% | 33.3% | 43.6% |
| -4..-2 | 64 | 23 | 17 | 24 | 35.9% | 26.6% | 37.5% |
| -1..1 | 87 | 40 | 23 | 24 | 46.0% | 26.4% | 27.6% |
| 2..4 | 61 | 22 | 22 | 17 | 36.1% | 36.1% | 27.9% |
| >4 | 46 | 30 | 11 | 5 | 65.2% | 23.9% | 10.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 49 | 30 | 12 | 7 | 61.2% | 24.5% | 14.3% |
| -5..-2 | 75 | 32 | 25 | 18 | 42.7% | 33.3% | 24.0% |
| -1..1 | 57 | 29 | 18 | 10 | 50.9% | 31.6% | 17.5% |
| 2..5 | 58 | 23 | 13 | 22 | 39.7% | 22.4% | 37.9% |
| >=6 | 58 | 10 | 18 | 30 | 17.2% | 31.0% | 51.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 18 | 6 | 4 | 8 | 33.3% | 22.2% | 44.4% |
| -1..0 | 65 | 23 | 23 | 19 | 35.4% | 35.4% | 29.2% |
| 0 | 119 | 52 | 34 | 33 | 43.7% | 28.6% | 27.7% |
| 1..2 | 75 | 34 | 20 | 21 | 45.3% | 26.7% | 28.0% |
| >2 | 11 | 5 | 2 | 4 | 45.5% | 18.2% | 36.4% |
| unknown | 9 | 4 | 3 | 2 | 44.4% | 33.3% | 22.2% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **35.1%** home win (59/168)
- `>= 0.5` tier: **50.4%** home win (65/129)
- Home-win gap (>= split minus < split): **+15.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 168 | 59 | 53 | 56 | 35.1% |
| high | >= 0.5 | 129 | 65 | 33 | 31 | 50.4% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.395 | -1.198 | -5.563 | 10.958 |
| away_points_before_match | 20.452 | 27.756 | 27.701 | 7.304 |
| home_points_before_match | 25.847 | 26.558 | 22.138 | 4.420 |
| position_difference | -1.806 | 0.302 | 2.448 | 4.255 |
| home_position_before_match | 7.637 | 9.151 | 9.816 | 2.179 |
| away_position_before_match | 9.444 | 8.849 | 7.368 | 2.076 |
| away_team_points_last_5 | 5.677 | 6.000 | 7.103 | 1.426 |
| away_team_goals_scored_last_5 | 5.621 | 5.953 | 7.011 | 1.391 |
| home_team_goals_scored_last_5 | 6.815 | 5.535 | 5.931 | 1.280 |
| away_team_goals_conceded_last_5 | 6.629 | 6.128 | 5.391 | 1.238 |
| home_team_points_last_5 | 6.895 | 5.965 | 5.816 | 1.079 |
| away_rest_days | 8.000 | 8.786 | 8.824 | 0.824 |
| home_team_goals_conceded_last_5 | 5.887 | 6.116 | 6.690 | 0.803 |
| home_rest_days | 8.208 | 8.714 | 8.694 | 0.506 |
| away_team_wins_last_5 | 1.476 | 1.523 | 1.966 | 0.490 |
| away_team_away_goals_avg | 1.015 | 1.175 | 1.473 | 0.457 |
| home_team_wins_last_5 | 1.919 | 1.512 | 1.483 | 0.437 |
| rest_days_difference | 0.208 | -0.084 | -0.129 | 0.338 |
| home_team_home_goals_avg | 1.667 | 1.334 | 1.419 | 0.334 |
| home_team_home_conceded_avg | 1.051 | 1.165 | 1.321 | 0.270 |
| away_team_away_win_rate | 0.226 | 0.274 | 0.362 | 0.137 |
| home_team_home_win_rate | 0.476 | 0.412 | 0.383 | 0.093 |
| away_team_away_conceded_avg | 1.483 | 1.510 | 1.483 | 0.027 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\serbia1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\serbia1\charts\relationships_home_win_pct_by_position.png)

