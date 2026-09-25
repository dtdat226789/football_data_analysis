# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:54:49+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Bundesliga (Austria)
- Scope: league `austria1`

- Matches analysed: **237** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| points_difference | -0.050 | -0.119 | -0.128 |
| away_position_before_match | 0.024 | -0.180 | -0.114 |
| home_team_home_win_rate | 0.091 | 0.044 | 0.105 |
| away_team_away_win_rate | -0.028 | 0.166 | 0.101 |
| away_team_away_conceded_avg | -0.050 | -0.073 | -0.094 |
| home_team_home_conceded_avg | -0.123 | 0.013 | -0.088 |
| home_team_goals_conceded_last_5 | -0.048 | -0.053 | -0.078 |
| home_team_home_goals_avg | 0.090 | 0.001 | 0.073 |
| position_difference | -0.038 | 0.128 | 0.064 |
| away_team_away_goals_avg | -0.102 | 0.188 | 0.058 |
| away_team_points_last_5 | -0.050 | 0.130 | 0.056 |
| home_rest_days | -0.040 | -0.027 | -0.052 |
| home_team_points_last_5 | 0.038 | 0.024 | 0.048 |
| away_rest_days | -0.056 | -0.003 | -0.047 |
| away_team_goals_conceded_last_5 | 0.039 | -0.099 | -0.042 |
| home_points_before_match | -0.044 | -0.001 | -0.036 |
| home_position_before_match | -0.024 | -0.015 | -0.030 |
| rest_days_difference | 0.088 | -0.127 | -0.025 |
| away_team_wins_last_5 | -0.067 | 0.100 | 0.021 |
| home_team_goals_scored_last_5 | 0.046 | -0.025 | 0.018 |
| away_team_goals_scored_last_5 | -0.055 | 0.083 | 0.018 |
| away_points_before_match | -0.024 | 0.049 | 0.017 |
| home_team_wins_last_5 | -0.018 | 0.038 | 0.014 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 36 | 16 | 11 | 9 | 44.4% | 30.6% | 25.0% |
| -4..-2 | 50 | 22 | 12 | 16 | 44.0% | 24.0% | 32.0% |
| -1..1 | 72 | 25 | 22 | 25 | 34.7% | 30.6% | 34.7% |
| 2..4 | 51 | 28 | 7 | 16 | 54.9% | 13.7% | 31.4% |
| >4 | 28 | 15 | 7 | 6 | 53.6% | 25.0% | 21.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 25 | 12 | 6 | 7 | 48.0% | 24.0% | 28.0% |
| -5..-2 | 57 | 26 | 15 | 16 | 45.6% | 26.3% | 28.1% |
| -1..1 | 58 | 31 | 12 | 15 | 53.4% | 20.7% | 25.9% |
| 2..5 | 75 | 31 | 17 | 27 | 41.3% | 22.7% | 36.0% |
| >=6 | 22 | 6 | 9 | 7 | 27.3% | 40.9% | 31.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 15 | 4 | 3 | 8 | 26.7% | 20.0% | 53.3% |
| -1..0 | 41 | 16 | 11 | 14 | 39.0% | 26.8% | 34.1% |
| 0 | 108 | 54 | 25 | 29 | 50.0% | 23.1% | 26.9% |
| 1..2 | 57 | 24 | 14 | 19 | 42.1% | 24.6% | 33.3% |
| >2 | 4 | 2 | 2 | 0 | 50.0% | 50.0% | 0.0% |
| unknown | 12 | 6 | 4 | 2 | 50.0% | 33.3% | 16.7% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **49.2%** home win (32/65)
- `>= 0.5` tier: **43.0%** home win (74/172)
- Home-win gap (>= split minus < split): **-6.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 65 | 32 | 10 | 23 | 49.2% |
| high | >= 0.5 | 172 | 74 | 49 | 49 | 43.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 18.255 | 20.729 | 17.528 | 3.201 |
| home_points_before_match | 18.566 | 20.271 | 17.153 | 3.118 |
| away_position_before_match | 7.208 | 5.864 | 6.181 | 1.343 |
| home_team_goals_conceded_last_5 | 5.849 | 6.407 | 5.194 | 1.212 |
| away_team_points_last_5 | 5.434 | 6.644 | 6.083 | 1.210 |
| position_difference | -0.377 | 0.593 | 0.375 | 0.971 |
| away_team_goals_conceded_last_5 | 6.104 | 5.356 | 5.250 | 0.854 |
| away_team_goals_scored_last_5 | 5.538 | 6.322 | 5.875 | 0.784 |
| points_difference | 0.311 | -0.458 | -0.375 | 0.769 |
| home_team_goals_scored_last_5 | 5.679 | 5.814 | 5.333 | 0.480 |
| away_team_wins_last_5 | 2.528 | 2.983 | 2.722 | 0.455 |
| rest_days_difference | 0.130 | 0.091 | -0.257 | 0.387 |
| home_position_before_match | 6.830 | 6.458 | 6.556 | 0.373 |
| home_rest_days | 9.060 | 9.182 | 8.814 | 0.368 |
| away_team_away_goals_avg | 1.022 | 1.126 | 1.310 | 0.289 |
| home_team_points_last_5 | 5.604 | 5.864 | 5.694 | 0.261 |
| away_rest_days | 8.930 | 9.091 | 9.071 | 0.161 |
| home_team_home_goals_avg | 1.263 | 1.326 | 1.225 | 0.102 |
| home_team_home_win_rate | 0.556 | 0.632 | 0.533 | 0.100 |
| home_team_wins_last_5 | 2.585 | 2.644 | 2.667 | 0.082 |
| away_team_away_win_rate | 0.493 | 0.528 | 0.567 | 0.074 |
| away_team_away_conceded_avg | 1.318 | 1.268 | 1.315 | 0.050 |
| home_team_home_conceded_avg | 1.137 | 1.124 | 1.146 | 0.022 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\austria1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\austria1\charts\relationships_home_win_pct_by_position.png)

