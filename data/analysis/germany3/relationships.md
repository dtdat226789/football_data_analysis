# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:59:54+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 3. Liga (Germany)
- Scope: league `germany3`

- Matches analysed: **449** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| position_difference | -0.194 | 0.087 | -0.083 |
| points_difference | 0.209 | -0.107 | 0.080 |
| away_position_before_match | 0.118 | -0.028 | 0.068 |
| away_team_goals_conceded_last_5 | 0.073 | -0.002 | 0.053 |
| home_position_before_match | -0.153 | 0.093 | -0.048 |
| home_points_before_match | 0.136 | -0.075 | 0.048 |
| rest_days_difference | -0.021 | -0.034 | -0.040 |
| home_team_goals_scored_last_5 | 0.127 | -0.086 | 0.033 |
| away_team_points_last_5 | -0.041 | -0.000 | -0.030 |
| away_team_away_goals_avg | 0.005 | 0.037 | 0.030 |
| away_team_away_win_rate | -0.039 | 0.070 | 0.020 |
| home_team_goals_conceded_last_5 | -0.044 | 0.075 | 0.020 |
| home_team_home_goals_avg | 0.064 | -0.041 | 0.019 |
| away_team_away_conceded_avg | 0.059 | -0.042 | 0.014 |
| home_rest_days | -0.040 | 0.029 | -0.009 |
| home_team_home_win_rate | 0.061 | -0.052 | 0.009 |
| home_team_wins_last_5 | 0.107 | -0.100 | 0.009 |
| home_team_points_last_5 | 0.119 | -0.114 | 0.008 |
| away_team_goals_scored_last_5 | -0.030 | 0.025 | -0.005 |
| home_team_home_conceded_avg | 0.001 | 0.004 | 0.004 |
| away_points_before_match | 0.002 | -0.007 | -0.003 |
| away_team_wins_last_5 | -0.015 | 0.019 | 0.002 |
| away_rest_days | -0.036 | 0.035 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 62 | 23 | 13 | 26 | 37.1% | 21.0% | 41.9% |
| -4..-2 | 104 | 43 | 20 | 41 | 41.3% | 19.2% | 39.4% |
| -1..1 | 138 | 61 | 36 | 41 | 44.2% | 26.1% | 29.7% |
| 2..4 | 85 | 37 | 22 | 26 | 43.5% | 25.9% | 30.6% |
| >4 | 60 | 40 | 12 | 8 | 66.7% | 20.0% | 13.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 108 | 65 | 22 | 21 | 60.2% | 20.4% | 19.4% |
| -5..-2 | 76 | 29 | 27 | 20 | 38.2% | 35.5% | 26.3% |
| -1..1 | 59 | 29 | 13 | 17 | 49.2% | 22.0% | 28.8% |
| 2..5 | 86 | 39 | 13 | 34 | 45.3% | 15.1% | 39.5% |
| >=6 | 120 | 42 | 28 | 50 | 35.0% | 23.3% | 41.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 9 | 5 | 1 | 3 | 55.6% | 11.1% | 33.3% |
| -1..0 | 122 | 51 | 30 | 41 | 41.8% | 24.6% | 33.6% |
| 0 | 189 | 94 | 33 | 62 | 49.7% | 17.5% | 32.8% |
| 1..2 | 109 | 46 | 31 | 32 | 42.2% | 28.4% | 29.4% |
| >2 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 20 | 8 | 8 | 4 | 40.0% | 40.0% | 20.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.0%** home win (41/108)
- `>= 0.5` tier: **47.8%** home win (163/341)
- Home-win gap (>= split minus < split): **+9.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 108 | 41 | 24 | 43 | 38.0% |
| high | >= 0.5 | 341 | 163 | 79 | 99 | 47.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.319 | -0.165 | -3.908 | 6.227 |
| home_points_before_match | 24.417 | 21.621 | 19.141 | 5.276 |
| position_difference | -1.137 | -0.039 | 2.796 | 3.933 |
| home_position_before_match | 10.201 | 10.039 | 12.521 | 2.482 |
| away_position_before_match | 11.338 | 10.078 | 9.725 | 1.613 |
| home_team_points_last_5 | 6.436 | 5.961 | 5.085 | 1.352 |
| away_points_before_match | 22.098 | 21.786 | 23.049 | 1.263 |
| home_team_goals_scored_last_5 | 7.368 | 6.524 | 6.183 | 1.185 |
| home_team_goals_conceded_last_5 | 6.745 | 6.417 | 7.500 | 1.083 |
| away_rest_days | 7.577 | 7.147 | 8.167 | 1.019 |
| home_rest_days | 7.531 | 7.168 | 8.123 | 0.955 |
| away_team_goals_conceded_last_5 | 7.191 | 6.621 | 6.542 | 0.649 |
| away_team_goals_scored_last_5 | 6.843 | 6.738 | 7.324 | 0.586 |
| away_team_points_last_5 | 5.907 | 6.019 | 6.408 | 0.502 |
| home_team_wins_last_5 | 2.828 | 2.699 | 2.352 | 0.476 |
| away_team_wins_last_5 | 2.652 | 2.660 | 2.789 | 0.137 |
| home_team_home_goals_avg | 1.572 | 1.528 | 1.436 | 0.136 |
| away_team_away_goals_avg | 1.315 | 1.309 | 1.410 | 0.101 |
| home_team_home_conceded_avg | 1.318 | 1.301 | 1.386 | 0.085 |
| away_team_away_win_rate | 0.503 | 0.480 | 0.565 | 0.085 |
| away_team_away_conceded_avg | 1.546 | 1.528 | 1.466 | 0.081 |
| rest_days_difference | -0.046 | 0.021 | -0.043 | 0.067 |
| home_team_home_win_rate | 0.649 | 0.626 | 0.586 | 0.063 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\germany3\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\germany3\charts\relationships_home_win_pct_by_position.png)

