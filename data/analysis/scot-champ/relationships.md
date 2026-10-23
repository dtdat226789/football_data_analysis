# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:05:53+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Championship (Scotland)
- Scope: league `scot-champ`

- Matches analysed: **190** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | -0.103 | -0.059 | -0.118 |
| away_team_goals_scored_last_5 | -0.117 | -0.034 | -0.113 |
| home_team_wins_last_5 | -0.027 | -0.110 | -0.091 |
| away_position_before_match | 0.143 | -0.043 | 0.084 |
| away_points_before_match | -0.065 | -0.047 | -0.081 |
| home_team_points_last_5 | -0.019 | -0.096 | -0.076 |
| position_difference | -0.209 | 0.142 | -0.071 |
| away_team_points_last_5 | -0.091 | 0.013 | -0.063 |
| home_team_goals_scored_last_5 | 0.003 | -0.091 | -0.056 |
| home_points_before_match | 0.071 | -0.160 | -0.048 |
| points_difference | 0.188 | -0.153 | 0.047 |
| away_team_away_conceded_avg | -0.058 | 0.004 | -0.042 |
| away_team_wins_last_5 | -0.066 | 0.015 | -0.042 |
| home_team_home_goals_avg | 0.077 | -0.153 | -0.039 |
| away_team_away_goals_avg | -0.074 | 0.030 | -0.039 |
| away_team_away_win_rate | -0.074 | 0.031 | -0.038 |
| home_rest_days | 0.042 | -0.093 | -0.029 |
| rest_days_difference | 0.067 | -0.122 | -0.029 |
| away_team_goals_conceded_last_5 | 0.053 | -0.026 | 0.024 |
| home_team_goals_conceded_last_5 | -0.013 | -0.020 | -0.023 |
| home_team_home_win_rate | 0.103 | -0.104 | 0.013 |
| home_position_before_match | -0.136 | 0.147 | -0.011 |
| away_rest_days | -0.021 | 0.029 | 0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 30 | 9 | 10 | 11 | 30.0% | 33.3% | 36.7% |
| -4..-2 | 41 | 16 | 9 | 16 | 39.0% | 22.0% | 39.0% |
| -1..1 | 62 | 25 | 25 | 12 | 40.3% | 40.3% | 19.4% |
| 2..4 | 40 | 17 | 13 | 10 | 42.5% | 32.5% | 25.0% |
| >4 | 17 | 7 | 7 | 3 | 41.2% | 41.2% | 17.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 17 | 10 | 7 | 0 | 58.8% | 41.2% | 0.0% |
| -5..-2 | 53 | 27 | 14 | 12 | 50.9% | 26.4% | 22.6% |
| -1..1 | 52 | 14 | 21 | 17 | 26.9% | 40.4% | 32.7% |
| 2..5 | 43 | 19 | 11 | 13 | 44.2% | 25.6% | 30.2% |
| >=6 | 25 | 4 | 11 | 10 | 16.0% | 44.0% | 40.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 25 | 10 | 6 | 9 | 40.0% | 24.0% | 36.0% |
| -1..0 | 16 | 3 | 3 | 10 | 18.8% | 18.8% | 62.5% |
| 0 | 100 | 39 | 36 | 25 | 39.0% | 36.0% | 25.0% |
| 1..2 | 16 | 6 | 6 | 4 | 37.5% | 37.5% | 25.0% |
| >2 | 26 | 14 | 8 | 4 | 53.8% | 30.8% | 15.4% |
| unknown | 7 | 2 | 5 | 0 | 28.6% | 71.4% | 0.0% |
- *7 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **35.2%** home win (50/142)
- `>= 0.5` tier: **50.0%** home win (24/48)
- Home-win gap (>= split minus < split): **+14.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 142 | 50 | 47 | 45 | 35.2% |
| high | >= 0.5 | 48 | 24 | 17 | 7 | 50.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 26.446 | 22.828 | 18.923 | 7.523 |
| points_difference | 2.527 | -1.859 | -3.327 | 5.854 |
| away_points_before_match | 23.919 | 24.688 | 22.250 | 2.438 |
| position_difference | -0.959 | 0.438 | 1.288 | 2.248 |
| rest_days_difference | 0.625 | 0.339 | -0.885 | 1.510 |
| home_position_before_match | 5.054 | 5.500 | 6.500 | 1.446 |
| away_position_before_match | 6.014 | 5.062 | 5.212 | 0.951 |
| away_rest_days | 7.329 | 7.305 | 8.115 | 0.810 |
| home_rest_days | 8.000 | 7.644 | 7.231 | 0.769 |
| away_team_points_last_5 | 6.270 | 6.062 | 6.731 | 0.668 |
| home_team_points_last_5 | 5.959 | 5.859 | 5.346 | 0.613 |
| home_team_goals_scored_last_5 | 5.676 | 5.344 | 5.077 | 0.599 |
| away_team_goals_conceded_last_5 | 5.473 | 4.922 | 5.058 | 0.551 |
| away_team_goals_scored_last_5 | 5.419 | 5.469 | 5.962 | 0.543 |
| home_team_goals_conceded_last_5 | 5.932 | 5.562 | 5.692 | 0.370 |
| home_team_wins_last_5 | 1.446 | 1.516 | 1.192 | 0.323 |
| home_team_home_goals_avg | 1.351 | 1.177 | 1.086 | 0.265 |
| away_team_wins_last_5 | 1.581 | 1.516 | 1.731 | 0.215 |
| away_team_away_goals_avg | 1.021 | 1.097 | 1.169 | 0.148 |
| home_team_home_conceded_avg | 1.055 | 1.034 | 1.136 | 0.102 |
| home_team_home_win_rate | 0.352 | 0.311 | 0.263 | 0.089 |
| away_team_away_conceded_avg | 1.198 | 1.164 | 1.249 | 0.085 |
| away_team_away_win_rate | 0.274 | 0.262 | 0.321 | 0.060 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\scot-champ\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\scot-champ\charts\relationships_home_win_pct_by_position.png)

