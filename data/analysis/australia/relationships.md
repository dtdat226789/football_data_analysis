# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:54:40+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: A-League (Australia)
- Scope: league `australia`

- Matches analysed: **332** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.177 | 0.086 | 0.189 |
| home_team_wins_last_5 | 0.092 | 0.068 | 0.114 |
| home_team_home_conceded_avg | -0.003 | 0.173 | 0.114 |
| home_team_points_last_5 | 0.126 | 0.024 | 0.109 |
| home_team_home_goals_avg | 0.092 | 0.050 | 0.102 |
| home_points_before_match | 0.148 | -0.013 | 0.101 |
| home_team_goals_conceded_last_5 | 0.009 | 0.120 | 0.088 |
| away_position_before_match | 0.126 | -0.011 | 0.086 |
| points_difference | 0.175 | -0.090 | 0.069 |
| rest_days_difference | -0.035 | 0.133 | 0.065 |
| away_team_goals_conceded_last_5 | 0.057 | 0.032 | 0.064 |
| position_difference | -0.167 | 0.091 | -0.063 |
| away_team_away_win_rate | -0.012 | 0.099 | 0.058 |
| away_team_away_goals_avg | -0.006 | 0.091 | 0.057 |
| away_points_before_match | 0.034 | 0.047 | 0.057 |
| home_rest_days | 0.022 | 0.028 | 0.035 |
| away_team_away_conceded_avg | -0.038 | -0.010 | -0.035 |
| home_team_home_win_rate | -0.013 | -0.036 | -0.034 |
| away_rest_days | 0.059 | -0.112 | -0.033 |
| away_team_goals_scored_last_5 | -0.060 | 0.050 | -0.011 |
| away_team_wins_last_5 | -0.079 | 0.080 | -0.004 |
| home_position_before_match | -0.098 | 0.112 | 0.003 |
| away_team_points_last_5 | -0.066 | 0.070 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 43 | 14 | 7 | 22 | 32.6% | 16.3% | 51.2% |
| -4..-2 | 69 | 22 | 16 | 31 | 31.9% | 23.2% | 44.9% |
| -1..1 | 111 | 43 | 33 | 35 | 38.7% | 29.7% | 31.5% |
| 2..4 | 59 | 17 | 18 | 24 | 28.8% | 30.5% | 40.7% |
| >4 | 50 | 25 | 13 | 12 | 50.0% | 26.0% | 24.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 38 | 15 | 6 | 17 | 39.5% | 15.8% | 44.7% |
| -5..-2 | 98 | 46 | 29 | 23 | 46.9% | 29.6% | 23.5% |
| -1..1 | 59 | 19 | 18 | 22 | 32.2% | 30.5% | 37.3% |
| 2..5 | 96 | 29 | 27 | 40 | 30.2% | 28.1% | 41.7% |
| >=6 | 41 | 12 | 7 | 22 | 29.3% | 17.1% | 53.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 62 | 26 | 16 | 20 | 41.9% | 25.8% | 32.3% |
| -1..0 | 71 | 29 | 16 | 26 | 40.8% | 22.5% | 36.6% |
| 0 | 68 | 31 | 15 | 22 | 45.6% | 22.1% | 32.4% |
| 1..2 | 87 | 25 | 25 | 37 | 28.7% | 28.7% | 42.5% |
| >2 | 31 | 5 | 9 | 17 | 16.1% | 29.0% | 54.8% |
| unknown | 13 | 5 | 6 | 2 | 38.5% | 46.2% | 15.4% |
- *13 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **41.4%** home win (36/87)
- `>= 0.5` tier: **34.7%** home win (85/245)
- Home-win gap (>= split minus < split): **-6.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 87 | 36 | 18 | 33 | 41.4% |
| high | >= 0.5 | 245 | 85 | 69 | 91 | 34.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 18.612 | 19.931 | 15.847 | 4.084 |
| points_difference | 1.876 | 0.207 | -1.395 | 3.271 |
| away_points_before_match | 16.736 | 19.724 | 17.242 | 2.989 |
| position_difference | -0.967 | -0.253 | 0.855 | 1.822 |
| home_position_before_match | 6.504 | 6.471 | 7.669 | 1.198 |
| home_team_goals_conceded_last_5 | 6.273 | 6.632 | 7.210 | 0.937 |
| away_team_goals_scored_last_5 | 6.405 | 7.322 | 6.984 | 0.917 |
| away_team_goals_conceded_last_5 | 6.769 | 7.437 | 6.556 | 0.880 |
| rest_days_difference | -0.517 | -0.074 | 0.352 | 0.870 |
| away_position_before_match | 7.471 | 6.724 | 6.815 | 0.747 |
| away_team_points_last_5 | 5.669 | 6.023 | 6.411 | 0.742 |
| away_rest_days | 8.078 | 7.732 | 7.385 | 0.692 |
| home_team_points_last_5 | 6.388 | 6.333 | 5.790 | 0.598 |
| away_team_wins_last_5 | 2.595 | 2.782 | 2.976 | 0.381 |
| home_team_home_conceded_avg | 1.209 | 1.229 | 1.450 | 0.241 |
| home_team_goals_scored_last_5 | 6.909 | 6.885 | 6.669 | 0.240 |
| home_rest_days | 7.560 | 7.654 | 7.738 | 0.177 |
| away_team_away_goals_avg | 1.260 | 1.340 | 1.358 | 0.098 |
| away_team_away_conceded_avg | 1.340 | 1.431 | 1.405 | 0.091 |
| home_team_wins_last_5 | 2.884 | 2.862 | 2.806 | 0.078 |
| home_team_home_goals_avg | 1.354 | 1.397 | 1.418 | 0.064 |
| away_team_away_win_rate | 0.552 | 0.575 | 0.598 | 0.047 |
| home_team_home_win_rate | 0.572 | 0.591 | 0.559 | 0.032 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\australia\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\australia\charts\relationships_home_win_pct_by_position.png)

