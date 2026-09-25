# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:59:07+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

- Matches analysed: **371** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_position_before_match | 0.177 | -0.033 | 0.111 |
| home_team_home_goals_avg | -0.064 | -0.043 | -0.079 |
| away_team_away_conceded_avg | 0.108 | -0.018 | 0.069 |
| away_team_away_win_rate | -0.173 | 0.089 | -0.067 |
| points_difference | 0.158 | -0.088 | 0.056 |
| home_team_goals_scored_last_5 | -0.005 | -0.072 | -0.056 |
| home_position_before_match | -0.026 | 0.102 | 0.054 |
| home_team_goals_conceded_last_5 | -0.102 | 0.034 | -0.053 |
| home_points_before_match | 0.072 | -0.010 | 0.047 |
| position_difference | -0.158 | 0.110 | -0.041 |
| away_rest_days | 0.019 | 0.029 | 0.036 |
| home_team_wins_last_5 | 0.079 | -0.046 | 0.027 |
| home_rest_days | 0.087 | -0.056 | 0.026 |
| away_team_points_last_5 | -0.088 | 0.057 | -0.026 |
| home_team_home_win_rate | 0.029 | 0.000 | 0.022 |
| away_team_wins_last_5 | -0.082 | 0.114 | 0.020 |
| away_team_goals_scored_last_5 | -0.070 | 0.049 | -0.018 |
| home_team_points_last_5 | 0.064 | -0.089 | -0.015 |
| away_team_goals_conceded_last_5 | 0.043 | -0.030 | 0.011 |
| away_points_before_match | -0.032 | 0.049 | 0.010 |
| home_team_home_conceded_avg | -0.069 | 0.059 | -0.010 |
| away_team_away_goals_avg | -0.060 | 0.054 | -0.007 |
| rest_days_difference | 0.045 | -0.041 | 0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 47 | 12 | 14 | 21 | 25.5% | 29.8% | 44.7% |
| -4..-2 | 78 | 27 | 24 | 27 | 34.6% | 30.8% | 34.6% |
| -1..1 | 120 | 42 | 39 | 39 | 35.0% | 32.5% | 32.5% |
| 2..4 | 72 | 30 | 25 | 17 | 41.7% | 34.7% | 23.6% |
| >4 | 54 | 24 | 18 | 12 | 44.4% | 33.3% | 22.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 91 | 42 | 30 | 19 | 46.2% | 33.0% | 20.9% |
| -5..-2 | 68 | 26 | 28 | 14 | 38.2% | 41.2% | 20.6% |
| -1..1 | 48 | 14 | 17 | 17 | 29.2% | 35.4% | 35.4% |
| 2..5 | 69 | 27 | 16 | 26 | 39.1% | 23.2% | 37.7% |
| >=6 | 95 | 26 | 29 | 40 | 27.4% | 30.5% | 42.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 21 | 4 | 10 | 7 | 19.0% | 47.6% | 33.3% |
| -1..0 | 11 | 2 | 5 | 4 | 18.2% | 45.5% | 36.4% |
| 0 | 253 | 101 | 77 | 75 | 39.9% | 30.4% | 29.6% |
| 1..2 | 15 | 5 | 3 | 7 | 33.3% | 20.0% | 46.7% |
| >2 | 22 | 8 | 8 | 6 | 36.4% | 36.4% | 27.3% |
| unknown | 49 | 15 | 17 | 17 | 30.6% | 34.7% | 34.7% |
- *49 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.3%** home win (32/96)
- `>= 0.5` tier: **37.5%** home win (103/275)
- Home-win gap (>= split minus < split): **+4.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 96 | 32 | 26 | 38 | 33.3% |
| high | >= 0.5 | 275 | 103 | 94 | 78 | 37.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| position_difference | -1.630 | 0.242 | 2.345 | 3.974 |
| points_difference | 1.548 | 0.592 | -2.371 | 3.919 |
| home_points_before_match | 16.985 | 17.608 | 14.629 | 2.979 |
| away_position_before_match | 11.452 | 10.542 | 9.259 | 2.193 |
| home_position_before_match | 9.822 | 10.783 | 11.603 | 1.781 |
| away_points_before_match | 15.437 | 17.017 | 17.000 | 1.580 |
| home_rest_days | 9.792 | 8.865 | 8.657 | 1.135 |
| home_team_points_last_5 | 5.793 | 5.808 | 4.750 | 1.058 |
| rest_days_difference | 0.483 | -0.252 | 0.061 | 0.736 |
| home_team_goals_scored_last_5 | 5.030 | 5.150 | 4.431 | 0.719 |
| away_team_goals_scored_last_5 | 4.585 | 4.808 | 5.216 | 0.630 |
| away_team_points_last_5 | 5.119 | 5.558 | 5.681 | 0.563 |
| home_team_goals_conceded_last_5 | 4.563 | 4.883 | 5.086 | 0.523 |
| home_team_wins_last_5 | 2.815 | 2.758 | 2.422 | 0.392 |
| away_team_goals_conceded_last_5 | 4.956 | 4.575 | 4.776 | 0.381 |
| away_team_wins_last_5 | 2.481 | 2.658 | 2.802 | 0.320 |
| away_rest_days | 9.016 | 9.187 | 8.991 | 0.196 |
| away_team_away_conceded_avg | 1.188 | 1.071 | 1.036 | 0.153 |
| home_team_home_conceded_avg | 0.859 | 0.943 | 0.986 | 0.126 |
| away_team_away_win_rate | 0.470 | 0.522 | 0.596 | 0.126 |
| away_team_away_goals_avg | 0.887 | 0.937 | 0.989 | 0.102 |
| home_team_home_goals_avg | 1.083 | 1.155 | 1.078 | 0.077 |
| home_team_home_win_rate | 0.606 | 0.624 | 0.579 | 0.045 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\france3\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\france3\charts\relationships_home_win_pct_by_position.png)

