# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:49:51+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Ykkosliiga (Finland)
- Scope: league `finland2`

- Matches analysed: **135** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.287 | 0.069 | -0.156 |
| home_team_home_win_rate | 0.238 | -0.036 | 0.144 |
| position_difference | -0.364 | 0.177 | -0.138 |
| away_team_away_conceded_avg | 0.240 | -0.069 | 0.123 |
| away_points_before_match | -0.180 | 0.027 | -0.109 |
| rest_days_difference | 0.074 | 0.069 | 0.103 |
| home_team_home_conceded_avg | -0.061 | -0.071 | -0.091 |
| away_rest_days | -0.103 | -0.016 | -0.089 |
| away_team_points_last_5 | -0.212 | 0.093 | -0.087 |
| away_team_goals_scored_last_5 | -0.101 | -0.021 | -0.086 |
| points_difference | 0.262 | -0.168 | 0.072 |
| home_team_home_goals_avg | 0.125 | -0.065 | 0.045 |
| away_team_wins_last_5 | -0.187 | 0.131 | -0.044 |
| away_team_away_goals_avg | 0.012 | 0.051 | 0.043 |
| home_points_before_match | 0.063 | -0.126 | -0.040 |
| home_team_goals_scored_last_5 | 0.078 | -0.027 | 0.037 |
| away_position_before_match | 0.220 | -0.179 | 0.035 |
| away_team_goals_conceded_last_5 | 0.124 | -0.161 | -0.021 |
| home_team_wins_last_5 | 0.094 | -0.070 | 0.020 |
| home_rest_days | -0.049 | 0.029 | -0.017 |
| away_team_away_win_rate | -0.153 | 0.137 | -0.016 |
| home_team_goals_conceded_last_5 | -0.042 | 0.021 | -0.015 |
| home_team_points_last_5 | 0.104 | -0.099 | 0.006 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 21 | 7 | 3 | 11 | 33.3% | 14.3% | 52.4% |
| -4..-2 | 31 | 10 | 12 | 9 | 32.3% | 38.7% | 29.0% |
| -1..1 | 41 | 14 | 10 | 17 | 34.1% | 24.4% | 41.5% |
| 2..4 | 20 | 13 | 4 | 3 | 65.0% | 20.0% | 15.0% |
| >4 | 22 | 14 | 6 | 2 | 63.6% | 27.3% | 9.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 9 | 7 | 2 | 0 | 77.8% | 22.2% | 0.0% |
| -5..-2 | 41 | 25 | 5 | 11 | 61.0% | 12.2% | 26.8% |
| -1..1 | 37 | 18 | 14 | 5 | 48.6% | 37.8% | 13.5% |
| 2..5 | 33 | 5 | 11 | 17 | 15.2% | 33.3% | 51.5% |
| >=6 | 15 | 3 | 3 | 9 | 20.0% | 20.0% | 60.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 10 | 3 | 5 | 2 | 30.0% | 50.0% | 20.0% |
| -1..0 | 32 | 15 | 10 | 7 | 46.9% | 31.2% | 21.9% |
| 0 | 47 | 19 | 11 | 17 | 40.4% | 23.4% | 36.2% |
| 1..2 | 30 | 13 | 5 | 12 | 43.3% | 16.7% | 40.0% |
| >2 | 11 | 6 | 3 | 2 | 54.5% | 27.3% | 18.2% |
| unknown | 5 | 2 | 1 | 2 | 40.0% | 20.0% | 40.0% |
- *5 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.6%** home win (32/85)
- `>= 0.5` tier: **52.0%** home win (26/50)
- Home-win gap (>= split minus < split): **+14.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 85 | 32 | 23 | 30 | 37.6% |
| high | >= 0.5 | 50 | 26 | 12 | 12 | 52.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.483 | -1.314 | -3.690 | 8.173 |
| away_points_before_match | 14.983 | 19.686 | 19.452 | 4.703 |
| home_points_before_match | 19.466 | 18.371 | 15.762 | 3.704 |
| position_difference | -1.621 | 0.686 | 1.762 | 3.383 |
| away_position_before_match | 6.362 | 5.171 | 4.571 | 1.791 |
| away_team_goals_conceded_last_5 | 8.207 | 7.114 | 6.476 | 1.731 |
| home_team_points_last_5 | 6.466 | 6.371 | 4.810 | 1.656 |
| away_team_points_last_5 | 5.448 | 6.457 | 7.071 | 1.623 |
| home_position_before_match | 4.741 | 5.857 | 6.333 | 1.592 |
| home_team_goals_scored_last_5 | 7.707 | 7.571 | 6.452 | 1.255 |
| away_rest_days | 6.304 | 7.294 | 7.075 | 0.991 |
| home_rest_days | 6.518 | 7.000 | 7.475 | 0.957 |
| rest_days_difference | 0.214 | -0.294 | 0.400 | 0.694 |
| away_team_goals_scored_last_5 | 7.448 | 7.114 | 7.762 | 0.648 |
| away_team_wins_last_5 | 1.431 | 1.771 | 2.000 | 0.569 |
| away_team_away_conceded_avg | 1.901 | 1.676 | 1.335 | 0.567 |
| home_team_home_conceded_avg | 1.431 | 1.941 | 1.516 | 0.510 |
| home_team_wins_last_5 | 1.741 | 1.714 | 1.238 | 0.503 |
| home_team_home_goals_avg | 1.756 | 1.629 | 1.586 | 0.169 |
| home_team_home_win_rate | 0.471 | 0.376 | 0.310 | 0.161 |
| away_team_away_win_rate | 0.275 | 0.324 | 0.384 | 0.108 |
| away_team_away_goals_avg | 1.603 | 1.576 | 1.518 | 0.084 |
| home_team_goals_conceded_last_5 | 7.362 | 7.371 | 7.429 | 0.067 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\finland2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\finland2\charts\relationships_home_win_pct_by_position.png)

