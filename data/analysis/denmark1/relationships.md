# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:57:05+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Superliga (Denmark)
- Scope: league `denmark1`

- Matches analysed: **248** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| rest_days_difference | -0.049 | -0.149 | -0.145 |
| away_position_before_match | 0.210 | -0.087 | 0.108 |
| position_difference | -0.267 | 0.195 | -0.078 |
| away_team_goals_conceded_last_5 | 0.116 | -0.024 | 0.077 |
| home_team_home_win_rate | 0.073 | 0.021 | 0.074 |
| points_difference | 0.242 | -0.180 | 0.068 |
| home_rest_days | -0.010 | -0.079 | -0.063 |
| away_points_before_match | -0.084 | 0.020 | -0.053 |
| away_team_away_goals_avg | 0.005 | 0.064 | 0.049 |
| home_team_home_goals_avg | 0.092 | -0.037 | 0.049 |
| away_team_goals_scored_last_5 | -0.097 | 0.179 | 0.048 |
| away_team_wins_last_5 | -0.128 | 0.084 | -0.044 |
| away_rest_days | -0.001 | -0.051 | -0.037 |
| home_team_home_conceded_avg | 0.044 | 0.001 | 0.036 |
| away_team_away_conceded_avg | 0.087 | -0.049 | 0.036 |
| away_team_away_win_rate | -0.067 | 0.126 | 0.034 |
| home_team_points_last_5 | 0.065 | -0.041 | 0.024 |
| home_team_goals_scored_last_5 | 0.095 | -0.076 | 0.024 |
| home_team_wins_last_5 | 0.047 | -0.022 | 0.022 |
| home_points_before_match | 0.050 | -0.080 | -0.016 |
| home_team_goals_conceded_last_5 | -0.024 | 0.048 | 0.014 |
| home_position_before_match | -0.130 | 0.164 | 0.010 |
| away_team_points_last_5 | -0.120 | 0.129 | -0.007 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 46 | 12 | 12 | 22 | 26.1% | 26.1% | 47.8% |
| -4..-2 | 56 | 22 | 14 | 20 | 39.3% | 25.0% | 35.7% |
| -1..1 | 62 | 27 | 16 | 19 | 43.5% | 25.8% | 30.6% |
| 2..4 | 47 | 24 | 9 | 14 | 51.1% | 19.1% | 29.8% |
| >4 | 37 | 19 | 10 | 8 | 51.4% | 27.0% | 21.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 26 | 15 | 7 | 4 | 57.7% | 26.9% | 15.4% |
| -5..-2 | 59 | 32 | 8 | 19 | 54.2% | 13.6% | 32.2% |
| -1..1 | 67 | 26 | 24 | 17 | 38.8% | 35.8% | 25.4% |
| 2..5 | 69 | 25 | 15 | 29 | 36.2% | 21.7% | 42.0% |
| >=6 | 27 | 6 | 7 | 14 | 22.2% | 25.9% | 51.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 32 | 12 | 8 | 12 | 37.5% | 25.0% | 37.5% |
| -1..0 | 39 | 13 | 9 | 17 | 33.3% | 23.1% | 43.6% |
| 0 | 97 | 49 | 17 | 31 | 50.5% | 17.5% | 32.0% |
| 1..2 | 59 | 26 | 17 | 16 | 44.1% | 28.8% | 27.1% |
| >2 | 9 | 1 | 4 | 4 | 11.1% | 44.4% | 44.4% |
| unknown | 12 | 3 | 6 | 3 | 25.0% | 50.0% | 25.0% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **47.5%** home win (29/61)
- `>= 0.5` tier: **40.1%** home win (75/187)
- Home-win gap (>= split minus < split): **-7.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 61 | 29 | 16 | 16 | 47.5% |
| high | >= 0.5 | 187 | 75 | 45 | 67 | 40.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.596 | -0.590 | -2.554 | 4.150 |
| away_points_before_match | 16.000 | 20.033 | 19.976 | 4.033 |
| position_difference | -0.923 | 0.557 | 1.470 | 2.393 |
| home_points_before_match | 17.596 | 19.443 | 17.422 | 2.021 |
| away_team_goals_scored_last_5 | 5.952 | 6.246 | 7.627 | 1.675 |
| away_team_points_last_5 | 5.490 | 6.049 | 6.735 | 1.245 |
| away_position_before_match | 7.192 | 6.246 | 5.988 | 1.204 |
| home_position_before_match | 6.269 | 6.803 | 7.458 | 1.189 |
| home_team_goals_scored_last_5 | 6.760 | 6.639 | 5.590 | 1.169 |
| home_rest_days | 9.762 | 8.618 | 8.637 | 1.144 |
| away_rest_days | 9.693 | 8.564 | 8.775 | 1.129 |
| away_team_goals_conceded_last_5 | 6.750 | 5.754 | 6.434 | 0.996 |
| home_team_points_last_5 | 6.115 | 5.689 | 5.373 | 0.742 |
| away_team_wins_last_5 | 2.510 | 2.639 | 2.928 | 0.418 |
| home_team_goals_conceded_last_5 | 6.337 | 6.590 | 6.639 | 0.302 |
| rest_days_difference | 0.069 | 0.055 | -0.138 | 0.207 |
| home_team_wins_last_5 | 2.712 | 2.639 | 2.506 | 0.206 |
| away_team_away_conceded_avg | 1.576 | 1.377 | 1.441 | 0.200 |
| away_team_away_goals_avg | 1.308 | 1.214 | 1.397 | 0.183 |
| home_team_home_conceded_avg | 1.306 | 1.394 | 1.242 | 0.152 |
| home_team_home_goals_avg | 1.501 | 1.499 | 1.396 | 0.105 |
| away_team_away_win_rate | 0.475 | 0.467 | 0.568 | 0.101 |
| home_team_home_win_rate | 0.602 | 0.572 | 0.608 | 0.036 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\denmark1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\denmark1\charts\relationships_home_win_pct_by_position.png)

