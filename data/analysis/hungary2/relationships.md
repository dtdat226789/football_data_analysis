# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:01:09+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: NB II. (Hungary)
- Scope: league `hungary2`

- Matches analysed: **301** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_rest_days | 0.084 | 0.051 | 0.102 |
| home_rest_days | 0.050 | 0.075 | 0.091 |
| home_team_home_win_rate | 0.056 | 0.063 | 0.088 |
| home_team_wins_last_5 | 0.081 | 0.033 | 0.088 |
| home_position_before_match | -0.177 | 0.084 | -0.085 |
| home_team_points_last_5 | 0.104 | 0.000 | 0.084 |
| away_team_away_win_rate | -0.002 | 0.117 | 0.079 |
| home_team_goals_conceded_last_5 | -0.088 | -0.010 | -0.078 |
| home_team_home_goals_avg | 0.108 | -0.029 | 0.067 |
| away_team_wins_last_5 | -0.031 | 0.127 | 0.061 |
| points_difference | 0.138 | -0.086 | 0.053 |
| rest_days_difference | -0.159 | 0.114 | -0.051 |
| home_team_goals_scored_last_5 | 0.066 | -0.009 | 0.046 |
| away_points_before_match | -0.116 | 0.070 | -0.046 |
| position_difference | -0.145 | 0.117 | -0.037 |
| away_team_goals_conceded_last_5 | 0.002 | -0.056 | -0.037 |
| home_team_home_conceded_avg | -0.026 | -0.021 | -0.036 |
| away_position_before_match | 0.024 | -0.077 | -0.033 |
| away_team_away_conceded_avg | 0.049 | -0.091 | -0.023 |
| away_team_goals_scored_last_5 | -0.039 | 0.075 | 0.020 |
| home_points_before_match | -0.028 | 0.016 | -0.012 |
| away_team_away_goals_avg | 0.023 | -0.019 | 0.006 |
| away_team_points_last_5 | -0.082 | 0.103 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 44 | 16 | 12 | 16 | 36.4% | 27.3% | 36.4% |
| -4..-2 | 65 | 23 | 20 | 22 | 35.4% | 30.8% | 33.8% |
| -1..1 | 97 | 47 | 23 | 27 | 48.5% | 23.7% | 27.8% |
| 2..4 | 60 | 30 | 14 | 16 | 50.0% | 23.3% | 26.7% |
| >4 | 35 | 21 | 5 | 9 | 60.0% | 14.3% | 25.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 59 | 36 | 9 | 14 | 61.0% | 15.3% | 23.7% |
| -5..-2 | 58 | 24 | 14 | 20 | 41.4% | 24.1% | 34.5% |
| -1..1 | 59 | 33 | 12 | 14 | 55.9% | 20.3% | 23.7% |
| 2..5 | 59 | 24 | 16 | 19 | 40.7% | 27.1% | 32.2% |
| >=6 | 66 | 20 | 23 | 23 | 30.3% | 34.8% | 34.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 11 | 9 | 1 | 1 | 81.8% | 9.1% | 9.1% |
| -1..0 | 28 | 16 | 4 | 8 | 57.1% | 14.3% | 28.6% |
| 0 | 207 | 92 | 54 | 61 | 44.4% | 26.1% | 29.5% |
| 1..2 | 33 | 12 | 9 | 12 | 36.4% | 27.3% | 36.4% |
| >2 | 6 | 1 | 1 | 4 | 16.7% | 16.7% | 66.7% |
| unknown | 16 | 7 | 5 | 4 | 43.8% | 31.2% | 25.0% |
- *16 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.9%** home win (21/54)
- `>= 0.5` tier: **47.0%** home win (116/247)
- Home-win gap (>= split minus < split): **+8.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 54 | 21 | 17 | 16 | 38.9% |
| high | >= 0.5 | 247 | 116 | 57 | 74 | 47.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 15.051 | 15.770 | 20.244 | 5.193 |
| home_points_before_match | 16.321 | 14.297 | 18.889 | 4.592 |
| position_difference | -1.299 | 1.554 | 1.022 | 2.853 |
| points_difference | 1.270 | -1.473 | -1.356 | 2.743 |
| home_position_before_match | 7.796 | 9.297 | 9.267 | 1.502 |
| away_rest_days | 10.400 | 8.899 | 9.698 | 1.501 |
| away_position_before_match | 9.095 | 7.743 | 8.244 | 1.352 |
| home_rest_days | 10.015 | 9.058 | 10.128 | 1.070 |
| home_team_points_last_5 | 5.985 | 5.095 | 5.522 | 0.891 |
| away_team_points_last_5 | 5.482 | 6.068 | 6.322 | 0.840 |
| rest_days_difference | -0.385 | 0.159 | 0.430 | 0.815 |
| home_team_goals_scored_last_5 | 5.635 | 4.973 | 5.089 | 0.662 |
| home_team_wins_last_5 | 2.745 | 2.338 | 2.589 | 0.407 |
| away_team_goals_scored_last_5 | 5.234 | 5.432 | 5.633 | 0.400 |
| away_team_goals_conceded_last_5 | 5.401 | 5.014 | 5.278 | 0.388 |
| away_team_wins_last_5 | 2.606 | 2.716 | 2.856 | 0.250 |
| away_team_away_conceded_avg | 1.396 | 1.148 | 1.255 | 0.248 |
| home_team_home_goals_avg | 1.408 | 1.174 | 1.210 | 0.234 |
| home_team_goals_conceded_last_5 | 5.328 | 5.527 | 5.544 | 0.216 |
| home_team_home_win_rate | 0.691 | 0.603 | 0.678 | 0.088 |
| home_team_home_conceded_avg | 1.047 | 0.964 | 0.990 | 0.082 |
| away_team_away_goals_avg | 1.044 | 1.030 | 0.977 | 0.067 |
| away_team_away_win_rate | 0.467 | 0.480 | 0.500 | 0.033 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\hungary2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\hungary2\charts\relationships_home_win_pct_by_position.png)

