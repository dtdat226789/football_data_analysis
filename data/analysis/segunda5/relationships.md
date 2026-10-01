# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:07:55+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Segunda RFEF - Group 5 (Spain)
- Scope: league `segunda5`

- Matches analysed: **306** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | 0.052 | 0.227 | 0.200 |
| home_team_goals_conceded_last_5 | 0.033 | 0.115 | 0.107 |
| home_team_home_win_rate | 0.014 | -0.131 | -0.081 |
| away_team_goals_conceded_last_5 | 0.095 | -0.002 | 0.072 |
| away_position_before_match | 0.167 | -0.083 | 0.072 |
| away_team_wins_last_5 | -0.130 | 0.048 | -0.068 |
| home_points_before_match | 0.032 | 0.056 | 0.065 |
| home_team_goals_scored_last_5 | 0.036 | 0.042 | 0.058 |
| away_team_away_win_rate | -0.049 | 0.119 | 0.046 |
| away_points_before_match | -0.083 | 0.153 | 0.043 |
| away_team_points_last_5 | -0.125 | 0.079 | -0.042 |
| position_difference | -0.145 | 0.113 | -0.034 |
| away_team_away_goals_avg | 0.004 | 0.042 | 0.033 |
| points_difference | 0.171 | -0.143 | 0.033 |
| home_team_wins_last_5 | 0.016 | -0.062 | -0.031 |
| away_team_goals_scored_last_5 | -0.082 | 0.054 | -0.026 |
| home_team_points_last_5 | 0.014 | -0.052 | -0.026 |
| away_rest_days | -0.093 | 0.138 | 0.025 |
| rest_days_difference | 0.044 | -0.083 | -0.025 |
| home_position_before_match | -0.037 | 0.076 | 0.024 |
| away_team_away_conceded_avg | 0.080 | -0.114 | -0.018 |
| home_team_home_goals_avg | 0.027 | -0.011 | 0.014 |
| home_rest_days | -0.058 | 0.069 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 46 | 9 | 14 | 23 | 19.6% | 30.4% | 50.0% |
| -4..-2 | 58 | 29 | 17 | 12 | 50.0% | 29.3% | 20.7% |
| -1..1 | 104 | 50 | 27 | 27 | 48.1% | 26.0% | 26.0% |
| 2..4 | 59 | 29 | 13 | 17 | 49.2% | 22.0% | 28.8% |
| >4 | 39 | 21 | 6 | 12 | 53.8% | 15.4% | 30.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 65 | 34 | 15 | 16 | 52.3% | 23.1% | 24.6% |
| -5..-2 | 62 | 36 | 13 | 13 | 58.1% | 21.0% | 21.0% |
| -1..1 | 49 | 24 | 14 | 11 | 49.0% | 28.6% | 22.4% |
| 2..5 | 49 | 18 | 12 | 19 | 36.7% | 24.5% | 38.8% |
| >=6 | 81 | 26 | 23 | 32 | 32.1% | 28.4% | 39.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 10 | 3 | 0 | 7 | 30.0% | 0.0% | 70.0% |
| -1..0 | 39 | 17 | 7 | 15 | 43.6% | 17.9% | 38.5% |
| 0 | 199 | 91 | 56 | 52 | 45.7% | 28.1% | 26.1% |
| 1..2 | 38 | 17 | 8 | 13 | 44.7% | 21.1% | 34.2% |
| >2 | 11 | 6 | 4 | 1 | 54.5% | 36.4% | 9.1% |
| unknown | 9 | 4 | 2 | 3 | 44.4% | 22.2% | 33.3% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **40.0%** home win (62/155)
- `>= 0.5` tier: **50.3%** home win (76/151)
- Home-win gap (>= split minus < split): **+10.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 155 | 62 | 37 | 56 | 40.0% |
| high | >= 0.5 | 151 | 76 | 40 | 35 | 50.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 20.594 | 22.338 | 26.121 | 5.527 |
| points_difference | 1.775 | -0.740 | -2.758 | 4.534 |
| position_difference | -0.993 | 0.571 | 1.967 | 2.960 |
| away_position_before_match | 10.630 | 8.909 | 8.516 | 2.114 |
| home_points_before_match | 22.370 | 21.597 | 23.363 | 1.765 |
| away_team_points_last_5 | 5.659 | 7.221 | 6.670 | 1.561 |
| away_team_goals_scored_last_5 | 5.457 | 6.481 | 6.231 | 1.024 |
| home_position_before_match | 9.638 | 9.481 | 10.484 | 1.003 |
| away_rest_days | 6.888 | 6.987 | 7.886 | 0.998 |
| away_team_goals_conceded_last_5 | 6.087 | 5.325 | 5.714 | 0.762 |
| rest_days_difference | 0.172 | 0.280 | -0.432 | 0.712 |
| away_team_wins_last_5 | 1.507 | 2.013 | 1.791 | 0.506 |
| home_rest_days | 7.060 | 7.267 | 7.455 | 0.395 |
| home_team_points_last_5 | 6.152 | 6.299 | 5.956 | 0.343 |
| home_team_goals_conceded_last_5 | 5.812 | 5.935 | 6.154 | 0.342 |
| home_team_home_conceded_avg | 0.868 | 0.875 | 1.048 | 0.180 |
| away_team_away_conceded_avg | 1.402 | 1.327 | 1.234 | 0.168 |
| home_team_wins_last_5 | 1.659 | 1.727 | 1.560 | 0.167 |
| home_team_goals_scored_last_5 | 5.696 | 5.857 | 5.857 | 0.161 |
| away_team_away_win_rate | 0.240 | 0.230 | 0.310 | 0.080 |
| home_team_home_win_rate | 0.457 | 0.453 | 0.395 | 0.062 |
| away_team_away_goals_avg | 0.897 | 0.941 | 0.956 | 0.059 |
| home_team_home_goals_avg | 1.345 | 1.337 | 1.313 | 0.032 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\segunda5\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\segunda5\charts\relationships_home_win_pct_by_position.png)

