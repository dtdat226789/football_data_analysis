# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:46:26+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

- Matches analysed: **350** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | 0.026 | 0.103 | 0.085 |
| away_position_before_match | 0.101 | 0.014 | 0.083 |
| away_team_goals_scored_last_5 | -0.046 | -0.070 | -0.079 |
| away_team_points_last_5 | -0.077 | -0.029 | -0.075 |
| away_team_wins_last_5 | -0.068 | -0.038 | -0.075 |
| position_difference | -0.162 | 0.091 | -0.059 |
| home_team_home_goals_avg | 0.158 | -0.098 | 0.052 |
| away_team_goals_conceded_last_5 | 0.125 | -0.079 | 0.041 |
| points_difference | 0.191 | -0.160 | 0.037 |
| home_rest_days | 0.066 | -0.023 | 0.034 |
| away_team_away_win_rate | -0.066 | 0.024 | -0.033 |
| away_team_away_goals_avg | -0.011 | -0.037 | -0.032 |
| home_team_goals_conceded_last_5 | -0.043 | 0.093 | 0.028 |
| away_rest_days | 0.078 | -0.048 | 0.026 |
| home_team_home_win_rate | 0.110 | -0.090 | 0.023 |
| away_team_away_conceded_avg | 0.073 | -0.051 | 0.021 |
| home_points_before_match | 0.156 | -0.150 | 0.018 |
| home_team_goals_scored_last_5 | 0.085 | -0.070 | 0.017 |
| home_team_wins_last_5 | 0.121 | -0.120 | 0.011 |
| rest_days_difference | -0.009 | 0.023 | 0.008 |
| away_points_before_match | 0.039 | -0.052 | -0.005 |
| home_position_before_match | -0.121 | 0.142 | 0.003 |
| home_team_points_last_5 | 0.107 | -0.122 | -0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 63 | 22 | 19 | 22 | 34.9% | 30.2% | 34.9% |
| -4..-2 | 67 | 31 | 17 | 19 | 46.3% | 25.4% | 28.4% |
| -1..1 | 115 | 55 | 30 | 30 | 47.8% | 26.1% | 26.1% |
| 2..4 | 67 | 37 | 19 | 11 | 55.2% | 28.4% | 16.4% |
| >4 | 38 | 26 | 7 | 5 | 68.4% | 18.4% | 13.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 74 | 46 | 13 | 15 | 62.2% | 17.6% | 20.3% |
| -5..-2 | 63 | 30 | 22 | 11 | 47.6% | 34.9% | 17.5% |
| -1..1 | 63 | 32 | 17 | 14 | 50.8% | 27.0% | 22.2% |
| 2..5 | 55 | 26 | 12 | 17 | 47.3% | 21.8% | 30.9% |
| >=6 | 95 | 37 | 28 | 30 | 38.9% | 29.5% | 31.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 12 | 7 | 3 | 2 | 58.3% | 25.0% | 16.7% |
| -1..0 | 32 | 15 | 8 | 9 | 46.9% | 25.0% | 28.1% |
| 0 | 239 | 117 | 65 | 57 | 49.0% | 27.2% | 23.8% |
| 1..2 | 31 | 18 | 6 | 7 | 58.1% | 19.4% | 22.6% |
| >2 | 17 | 6 | 4 | 7 | 35.3% | 23.5% | 41.2% |
| unknown | 19 | 8 | 6 | 5 | 42.1% | 31.6% | 26.3% |
- *19 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.0%** home win (29/88)
- `>= 0.5` tier: **54.2%** home win (142/262)
- Home-win gap (>= split minus < split): **+21.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 88 | 29 | 26 | 33 | 33.0% |
| high | >= 0.5 | 262 | 142 | 66 | 54 | 54.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 24.977 | 19.283 | 16.931 | 8.046 |
| points_difference | 2.345 | -2.109 | -3.437 | 5.782 |
| position_difference | -0.947 | 1.457 | 1.747 | 2.694 |
| away_points_before_match | 22.632 | 21.391 | 20.368 | 2.264 |
| home_position_before_match | 9.234 | 10.576 | 11.207 | 1.973 |
| home_team_points_last_5 | 6.257 | 5.457 | 4.736 | 1.522 |
| away_team_goals_conceded_last_5 | 5.140 | 4.511 | 3.897 | 1.244 |
| away_position_before_match | 10.181 | 9.120 | 9.460 | 1.062 |
| home_team_goals_scored_last_5 | 4.971 | 4.620 | 4.218 | 0.752 |
| home_team_wins_last_5 | 2.924 | 2.478 | 2.253 | 0.671 |
| away_rest_days | 7.276 | 7.116 | 6.756 | 0.520 |
| away_team_goals_scored_last_5 | 4.877 | 5.174 | 4.655 | 0.519 |
| home_team_goals_conceded_last_5 | 4.643 | 5.152 | 5.069 | 0.509 |
| rest_days_difference | 0.025 | -0.093 | 0.354 | 0.447 |
| home_team_home_goals_avg | 1.181 | 1.129 | 0.861 | 0.320 |
| home_rest_days | 7.301 | 7.023 | 7.110 | 0.277 |
| away_team_points_last_5 | 5.947 | 6.174 | 6.218 | 0.271 |
| away_team_away_conceded_avg | 1.149 | 1.143 | 0.948 | 0.201 |
| home_team_home_win_rate | 0.702 | 0.632 | 0.577 | 0.125 |
| home_team_home_conceded_avg | 0.829 | 0.946 | 0.869 | 0.117 |
| away_team_away_goals_avg | 0.888 | 0.915 | 0.843 | 0.072 |
| away_team_away_win_rate | 0.472 | 0.507 | 0.520 | 0.048 |
| away_team_wins_last_5 | 2.754 | 2.761 | 2.793 | 0.039 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\segunda4\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\segunda4\charts\relationships_home_win_pct_by_position.png)

