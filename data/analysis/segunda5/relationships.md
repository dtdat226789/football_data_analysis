# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:46:43+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Segunda RFEF - Group 5 (Spain)
- Scope: league `segunda5`

- Matches analysed: **339** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | 0.014 | 0.154 | 0.117 |
| away_position_before_match | 0.157 | -0.045 | 0.090 |
| away_team_away_win_rate | 0.010 | 0.086 | 0.067 |
| away_team_goals_conceded_last_5 | 0.093 | -0.010 | 0.065 |
| home_team_goals_conceded_last_5 | 0.017 | 0.070 | 0.061 |
| away_team_away_conceded_avg | 0.039 | -0.119 | -0.052 |
| away_team_points_last_5 | -0.095 | 0.034 | -0.050 |
| position_difference | -0.143 | 0.093 | -0.047 |
| home_points_before_match | 0.026 | 0.036 | 0.045 |
| home_team_goals_scored_last_5 | 0.038 | 0.011 | 0.036 |
| home_team_home_goals_avg | 0.063 | -0.021 | 0.034 |
| points_difference | 0.160 | -0.132 | 0.033 |
| away_rest_days | -0.080 | 0.134 | 0.029 |
| home_team_points_last_5 | 0.025 | -0.069 | -0.028 |
| home_position_before_match | -0.037 | 0.081 | 0.027 |
| away_points_before_match | -0.073 | 0.118 | 0.025 |
| rest_days_difference | 0.037 | -0.077 | -0.023 |
| away_team_goals_scored_last_5 | -0.045 | 0.024 | -0.018 |
| home_team_wins_last_5 | 0.018 | -0.043 | -0.016 |
| away_team_away_goals_avg | 0.024 | -0.007 | 0.013 |
| home_team_home_win_rate | 0.057 | -0.079 | -0.010 |
| home_rest_days | -0.049 | 0.070 | 0.010 |
| away_team_wins_last_5 | -0.067 | 0.063 | -0.009 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 49 | 11 | 14 | 24 | 22.4% | 28.6% | 49.0% |
| -4..-2 | 61 | 30 | 19 | 12 | 49.2% | 31.1% | 19.7% |
| -1..1 | 127 | 61 | 32 | 34 | 48.0% | 25.2% | 26.8% |
| 2..4 | 61 | 30 | 14 | 17 | 49.2% | 23.0% | 27.9% |
| >4 | 41 | 22 | 6 | 13 | 53.7% | 14.6% | 31.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 68 | 36 | 15 | 17 | 52.9% | 22.1% | 25.0% |
| -5..-2 | 65 | 37 | 15 | 13 | 56.9% | 23.1% | 20.0% |
| -1..1 | 69 | 34 | 17 | 18 | 49.3% | 24.6% | 26.1% |
| 2..5 | 51 | 19 | 13 | 19 | 37.3% | 25.5% | 37.3% |
| >=6 | 86 | 28 | 25 | 33 | 32.6% | 29.1% | 38.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 10 | 3 | 0 | 7 | 30.0% | 0.0% | 70.0% |
| -1..0 | 42 | 20 | 7 | 15 | 47.6% | 16.7% | 35.7% |
| 0 | 210 | 98 | 58 | 54 | 46.7% | 27.6% | 25.7% |
| 1..2 | 41 | 17 | 11 | 13 | 41.5% | 26.8% | 31.7% |
| >2 | 11 | 6 | 4 | 1 | 54.5% | 36.4% | 9.1% |
| unknown | 25 | 10 | 5 | 10 | 40.0% | 20.0% | 40.0% |
- *25 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **47.4%** home win (37/78)
- `>= 0.5` tier: **44.8%** home win (117/261)
- Home-win gap (>= split minus < split): **-2.6 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 78 | 37 | 19 | 22 | 47.4% |
| high | >= 0.5 | 261 | 117 | 66 | 78 | 44.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 18.714 | 20.376 | 23.840 | 5.126 |
| points_difference | 1.545 | -0.694 | -2.510 | 4.055 |
| position_difference | -0.851 | 0.659 | 1.790 | 2.641 |
| away_position_before_match | 10.214 | 8.859 | 8.480 | 1.734 |
| home_points_before_match | 20.260 | 19.682 | 21.330 | 1.648 |
| away_team_points_last_5 | 5.331 | 6.682 | 6.140 | 1.351 |
| away_rest_days | 6.903 | 6.975 | 7.856 | 0.953 |
| home_position_before_match | 9.364 | 9.518 | 10.270 | 0.906 |
| away_team_goals_scored_last_5 | 5.123 | 5.941 | 5.730 | 0.818 |
| rest_days_difference | 0.139 | 0.300 | -0.422 | 0.722 |
| away_team_goals_conceded_last_5 | 5.643 | 4.953 | 5.260 | 0.690 |
| away_team_wins_last_5 | 2.474 | 2.965 | 2.840 | 0.491 |
| home_rest_days | 7.042 | 7.275 | 7.433 | 0.392 |
| home_team_points_last_5 | 5.727 | 5.824 | 5.490 | 0.334 |
| home_team_goals_conceded_last_5 | 5.377 | 5.694 | 5.620 | 0.317 |
| home_team_home_conceded_avg | 0.810 | 0.863 | 0.973 | 0.163 |
| away_team_away_conceded_avg | 1.295 | 1.249 | 1.143 | 0.153 |
| home_team_goals_scored_last_5 | 5.325 | 5.471 | 5.390 | 0.146 |
| home_team_home_goals_avg | 1.257 | 1.234 | 1.195 | 0.063 |
| home_team_home_win_rate | 0.648 | 0.627 | 0.598 | 0.049 |
| away_team_away_win_rate | 0.447 | 0.491 | 0.494 | 0.047 |
| home_team_wins_last_5 | 2.623 | 2.624 | 2.610 | 0.014 |
| away_team_away_goals_avg | 0.863 | 0.876 | 0.870 | 0.013 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\segunda5\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\segunda5\charts\relationships_home_win_pct_by_position.png)

