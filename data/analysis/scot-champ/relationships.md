# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:44:24+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Championship (Scotland)
- Scope: league `scot-champ`

- Matches analysed: **227** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_position_before_match | 0.150 | 0.011 | 0.123 |
| away_team_goals_conceded_last_5 | 0.067 | 0.049 | 0.084 |
| away_team_goals_scored_last_5 | -0.094 | 0.007 | -0.068 |
| position_difference | -0.219 | 0.157 | -0.065 |
| home_team_points_last_5 | 0.017 | -0.108 | -0.058 |
| home_team_goals_conceded_last_5 | -0.002 | 0.090 | 0.058 |
| points_difference | 0.186 | -0.154 | 0.042 |
| home_position_before_match | -0.137 | 0.217 | 0.038 |
| away_team_points_last_5 | -0.070 | 0.026 | -0.037 |
| away_team_away_win_rate | 0.040 | 0.002 | 0.032 |
| away_team_wins_last_5 | -0.069 | 0.037 | -0.029 |
| away_points_before_match | -0.034 | 0.002 | -0.025 |
| rest_days_difference | 0.068 | -0.111 | -0.022 |
| home_rest_days | 0.043 | -0.081 | -0.021 |
| home_team_home_win_rate | 0.060 | -0.095 | -0.017 |
| home_team_wins_last_5 | 0.031 | -0.054 | -0.012 |
| away_team_away_goals_avg | -0.041 | 0.062 | 0.009 |
| home_team_home_goals_avg | 0.087 | -0.112 | -0.007 |
| away_team_away_conceded_avg | -0.041 | 0.058 | 0.006 |
| away_rest_days | -0.018 | 0.026 | 0.003 |
| home_team_goals_scored_last_5 | 0.041 | -0.044 | 0.002 |
| home_points_before_match | 0.088 | -0.100 | 0.002 |
| home_team_home_conceded_avg | -0.062 | 0.074 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 33 | 10 | 10 | 13 | 30.3% | 30.3% | 39.4% |
| -4..-2 | 48 | 17 | 12 | 19 | 35.4% | 25.0% | 39.6% |
| -1..1 | 79 | 34 | 29 | 16 | 43.0% | 36.7% | 20.3% |
| 2..4 | 47 | 22 | 15 | 10 | 46.8% | 31.9% | 21.3% |
| >4 | 20 | 8 | 8 | 4 | 40.0% | 40.0% | 20.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 20 | 12 | 8 | 0 | 60.0% | 40.0% | 0.0% |
| -5..-2 | 62 | 32 | 17 | 13 | 51.6% | 27.4% | 21.0% |
| -1..1 | 62 | 19 | 24 | 19 | 30.6% | 38.7% | 30.6% |
| 2..5 | 55 | 23 | 13 | 19 | 41.8% | 23.6% | 34.5% |
| >=6 | 28 | 5 | 12 | 11 | 17.9% | 42.9% | 39.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 27 | 11 | 7 | 9 | 40.7% | 25.9% | 33.3% |
| -1..0 | 21 | 4 | 5 | 12 | 19.0% | 23.8% | 57.1% |
| 0 | 120 | 50 | 39 | 31 | 41.7% | 32.5% | 25.8% |
| 1..2 | 21 | 8 | 8 | 5 | 38.1% | 38.1% | 23.8% |
| >2 | 26 | 14 | 8 | 4 | 53.8% | 30.8% | 15.4% |
| unknown | 12 | 4 | 7 | 1 | 33.3% | 58.3% | 8.3% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **32.7%** home win (17/52)
- `>= 0.5` tier: **42.3%** home win (74/175)
- Home-win gap (>= split minus < split): **+9.6 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 52 | 17 | 17 | 18 | 32.7% |
| high | >= 0.5 | 175 | 74 | 57 | 44 | 42.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 22.462 | 20.338 | 16.242 | 6.220 |
| points_difference | 2.198 | -1.473 | -3.161 | 5.359 |
| position_difference | -0.901 | 0.284 | 1.548 | 2.449 |
| away_points_before_match | 20.264 | 21.811 | 19.403 | 2.408 |
| home_position_before_match | 4.901 | 5.324 | 6.694 | 1.792 |
| rest_days_difference | 0.494 | 0.254 | -0.770 | 1.265 |
| home_team_points_last_5 | 5.791 | 5.541 | 4.806 | 0.985 |
| away_rest_days | 7.455 | 7.388 | 8.164 | 0.776 |
| away_position_before_match | 5.802 | 5.041 | 5.145 | 0.762 |
| away_team_points_last_5 | 5.879 | 5.676 | 6.306 | 0.631 |
| home_rest_days | 7.989 | 7.642 | 7.393 | 0.595 |
| home_team_goals_scored_last_5 | 5.198 | 4.878 | 4.613 | 0.585 |
| away_team_goals_scored_last_5 | 4.912 | 5.054 | 5.484 | 0.572 |
| home_team_goals_conceded_last_5 | 5.220 | 5.027 | 5.548 | 0.521 |
| away_team_goals_conceded_last_5 | 4.945 | 4.568 | 4.742 | 0.377 |
| away_team_wins_last_5 | 2.934 | 2.811 | 3.081 | 0.270 |
| home_team_wins_last_5 | 2.934 | 2.676 | 2.677 | 0.258 |
| home_team_home_goals_avg | 1.274 | 1.110 | 1.030 | 0.244 |
| home_team_home_conceded_avg | 0.944 | 0.899 | 1.103 | 0.204 |
| away_team_away_goals_avg | 0.915 | 0.998 | 1.055 | 0.140 |
| home_team_home_win_rate | 0.703 | 0.633 | 0.576 | 0.127 |
| away_team_away_conceded_avg | 1.142 | 1.102 | 1.205 | 0.103 |
| away_team_away_win_rate | 0.598 | 0.597 | 0.583 | 0.015 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\scot-champ\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\scot-champ\charts\relationships_home_win_pct_by_position.png)

