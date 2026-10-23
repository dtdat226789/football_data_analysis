# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:07:10+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Segunda RFEF - Group 2 (Spain)
- Scope: league `segunda2`

- Matches analysed: **306** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_points_before_match | 0.158 | -0.021 | 0.112 |
| home_team_goals_scored_last_5 | 0.201 | -0.111 | 0.087 |
| away_points_before_match | 0.012 | 0.100 | 0.074 |
| points_difference | 0.209 | -0.174 | 0.052 |
| home_team_home_win_rate | -0.010 | -0.060 | -0.047 |
| away_team_goals_scored_last_5 | -0.015 | 0.088 | 0.045 |
| home_position_before_match | -0.178 | 0.150 | -0.043 |
| home_team_wins_last_5 | 0.113 | -0.078 | 0.039 |
| position_difference | -0.214 | 0.203 | -0.038 |
| home_team_points_last_5 | 0.115 | -0.083 | 0.037 |
| away_team_away_conceded_avg | 0.106 | -0.080 | 0.032 |
| home_team_home_goals_avg | 0.108 | -0.085 | 0.030 |
| home_team_home_conceded_avg | -0.013 | 0.058 | 0.027 |
| away_team_wins_last_5 | -0.068 | 0.048 | -0.023 |
| home_rest_days | -0.032 | 0.009 | -0.019 |
| away_team_away_win_rate | -0.008 | 0.038 | 0.018 |
| away_team_points_last_5 | -0.073 | 0.063 | -0.017 |
| away_rest_days | -0.014 | -0.004 | -0.014 |
| away_team_goals_conceded_last_5 | 0.102 | -0.105 | 0.012 |
| rest_days_difference | -0.039 | 0.029 | -0.012 |
| away_position_before_match | 0.119 | -0.131 | 0.009 |
| away_team_away_goals_avg | 0.036 | -0.044 | -0.000 |
| home_team_goals_conceded_last_5 | -0.022 | 0.027 | 0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 43 | 14 | 13 | 16 | 32.6% | 30.2% | 37.2% |
| -4..-2 | 68 | 25 | 21 | 22 | 36.8% | 30.9% | 32.4% |
| -1..1 | 98 | 42 | 24 | 32 | 42.9% | 24.5% | 32.7% |
| 2..4 | 65 | 32 | 19 | 14 | 49.2% | 29.2% | 21.5% |
| >4 | 32 | 17 | 12 | 3 | 53.1% | 37.5% | 9.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 60 | 38 | 14 | 8 | 63.3% | 23.3% | 13.3% |
| -5..-2 | 67 | 33 | 20 | 14 | 49.3% | 29.9% | 20.9% |
| -1..1 | 40 | 15 | 16 | 9 | 37.5% | 40.0% | 22.5% |
| 2..5 | 64 | 22 | 16 | 26 | 34.4% | 25.0% | 40.6% |
| >=6 | 75 | 22 | 23 | 30 | 29.3% | 30.7% | 40.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 1 | 1 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| -1..0 | 70 | 29 | 21 | 20 | 41.4% | 30.0% | 28.6% |
| 0 | 165 | 70 | 46 | 49 | 42.4% | 27.9% | 29.7% |
| 1..2 | 59 | 25 | 18 | 16 | 42.4% | 30.5% | 27.1% |
| >2 | 2 | 1 | 0 | 1 | 50.0% | 0.0% | 50.0% |
| unknown | 9 | 4 | 4 | 1 | 44.4% | 44.4% | 11.1% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **41.3%** home win (74/179)
- `>= 0.5` tier: **44.1%** home win (56/127)
- Home-win gap (>= split minus < split): **+2.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 179 | 74 | 54 | 51 | 41.3% |
| high | >= 0.5 | 127 | 56 | 35 | 36 | 44.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.908 | -0.348 | -3.736 | 5.643 |
| position_difference | -1.392 | 0.584 | 2.874 | 4.266 |
| away_points_before_match | 20.762 | 22.809 | 24.874 | 4.112 |
| away_position_before_match | 10.669 | 9.191 | 8.345 | 2.324 |
| home_position_before_match | 9.277 | 9.775 | 11.218 | 1.941 |
| home_points_before_match | 22.669 | 22.461 | 21.138 | 1.531 |
| home_team_goals_conceded_last_5 | 5.746 | 5.270 | 6.425 | 1.156 |
| away_team_goals_conceded_last_5 | 6.169 | 5.146 | 5.253 | 1.023 |
| away_team_points_last_5 | 5.892 | 6.494 | 6.747 | 0.855 |
| away_team_goals_scored_last_5 | 5.754 | 5.539 | 6.299 | 0.760 |
| home_team_goals_scored_last_5 | 5.823 | 5.652 | 5.092 | 0.731 |
| home_team_points_last_5 | 6.169 | 6.225 | 5.586 | 0.639 |
| away_team_wins_last_5 | 1.523 | 1.798 | 1.724 | 0.275 |
| away_team_away_conceded_avg | 1.424 | 1.190 | 1.166 | 0.258 |
| home_team_wins_last_5 | 1.608 | 1.607 | 1.414 | 0.194 |
| home_rest_days | 7.183 | 7.118 | 7.302 | 0.185 |
| away_rest_days | 7.198 | 7.153 | 7.314 | 0.161 |
| home_team_home_conceded_avg | 0.956 | 0.939 | 1.065 | 0.125 |
| away_team_away_goals_avg | 1.038 | 0.961 | 0.960 | 0.078 |
| home_team_home_goals_avg | 1.295 | 1.297 | 1.230 | 0.067 |
| away_team_away_win_rate | 0.233 | 0.264 | 0.267 | 0.034 |
| rest_days_difference | -0.016 | -0.035 | -0.012 | 0.024 |
| home_team_home_win_rate | 0.417 | 0.405 | 0.423 | 0.017 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\segunda2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\segunda2\charts\relationships_home_win_pct_by_position.png)

