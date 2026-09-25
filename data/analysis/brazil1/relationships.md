# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:55:31+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie A Betano (Brazil)
- Scope: league `brazil1`

- Matches analysed: **657** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_points_before_match | 0.141 | -0.051 | 0.075 |
| away_team_away_goals_avg | -0.146 | 0.076 | -0.063 |
| away_points_before_match | -0.014 | 0.099 | 0.056 |
| away_team_points_last_5 | -0.128 | 0.080 | -0.046 |
| rest_days_difference | -0.028 | -0.032 | -0.043 |
| position_difference | -0.207 | 0.179 | -0.041 |
| away_position_before_match | 0.128 | -0.090 | 0.039 |
| away_team_away_win_rate | -0.093 | 0.050 | -0.039 |
| home_team_home_goals_avg | 0.006 | -0.053 | -0.031 |
| away_team_wins_last_5 | -0.090 | 0.064 | -0.027 |
| points_difference | 0.215 | -0.212 | 0.025 |
| away_team_goals_scored_last_5 | -0.062 | 0.038 | -0.023 |
| home_team_goals_scored_last_5 | 0.061 | -0.038 | 0.021 |
| away_team_away_conceded_avg | 0.069 | -0.048 | 0.021 |
| home_rest_days | -0.047 | 0.024 | -0.021 |
| home_position_before_match | -0.161 | 0.159 | -0.018 |
| away_team_goals_conceded_last_5 | 0.089 | -0.085 | 0.012 |
| home_team_home_win_rate | 0.034 | -0.055 | -0.011 |
| home_team_wins_last_5 | 0.086 | -0.089 | 0.008 |
| home_team_home_conceded_avg | -0.085 | 0.089 | -0.006 |
| home_team_goals_conceded_last_5 | -0.086 | 0.106 | 0.004 |
| away_rest_days | -0.033 | 0.044 | 0.004 |
| home_team_points_last_5 | 0.070 | -0.081 | 0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 91 | 33 | 24 | 34 | 36.3% | 26.4% | 37.4% |
| -4..-2 | 164 | 72 | 49 | 43 | 43.9% | 29.9% | 26.2% |
| -1..1 | 200 | 98 | 56 | 46 | 49.0% | 28.0% | 23.0% |
| 2..4 | 118 | 67 | 24 | 27 | 56.8% | 20.3% | 22.9% |
| >4 | 84 | 51 | 23 | 10 | 60.7% | 27.4% | 11.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 155 | 100 | 35 | 20 | 64.5% | 22.6% | 12.9% |
| -5..-2 | 112 | 53 | 39 | 20 | 47.3% | 34.8% | 17.9% |
| -1..1 | 88 | 47 | 20 | 21 | 53.4% | 22.7% | 23.9% |
| 2..5 | 114 | 51 | 33 | 30 | 44.7% | 28.9% | 26.3% |
| >=6 | 188 | 70 | 49 | 69 | 37.2% | 26.1% | 36.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 74 | 37 | 19 | 18 | 50.0% | 25.7% | 24.3% |
| -1..0 | 121 | 60 | 35 | 26 | 49.6% | 28.9% | 21.5% |
| 0 | 235 | 117 | 59 | 59 | 49.8% | 25.1% | 25.1% |
| 1..2 | 163 | 72 | 46 | 45 | 44.2% | 28.2% | 27.6% |
| >2 | 44 | 24 | 11 | 9 | 54.5% | 25.0% | 20.5% |
| unknown | 20 | 11 | 6 | 3 | 55.0% | 30.0% | 15.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **40.9%** home win (27/66)
- `>= 0.5` tier: **49.7%** home win (294/591)
- Home-win gap (>= split minus < split): **+8.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 66 | 27 | 25 | 14 | 40.9% |
| high | >= 0.5 | 591 | 294 | 151 | 146 | 49.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.012 | -1.295 | -4.537 | 6.550 |
| position_difference | -1.087 | 0.886 | 3.531 | 4.618 |
| home_points_before_match | 23.713 | 21.068 | 19.663 | 4.051 |
| home_position_before_match | 10.115 | 11.210 | 12.800 | 2.685 |
| away_points_before_match | 21.701 | 22.364 | 24.200 | 2.499 |
| away_position_before_match | 11.202 | 10.324 | 9.269 | 1.934 |
| away_rest_days | 7.394 | 7.035 | 8.318 | 1.283 |
| away_team_points_last_5 | 5.894 | 6.483 | 7.156 | 1.262 |
| home_rest_days | 7.506 | 7.476 | 8.471 | 0.995 |
| away_team_goals_conceded_last_5 | 6.084 | 5.381 | 5.112 | 0.972 |
| home_team_goals_conceded_last_5 | 5.698 | 5.648 | 6.400 | 0.752 |
| home_team_points_last_5 | 6.255 | 5.932 | 5.638 | 0.618 |
| away_team_goals_scored_last_5 | 5.760 | 5.756 | 6.287 | 0.532 |
| home_team_goals_scored_last_5 | 5.807 | 5.545 | 5.344 | 0.463 |
| away_team_wins_last_5 | 2.835 | 2.926 | 3.244 | 0.409 |
| rest_days_difference | 0.113 | 0.441 | 0.153 | 0.328 |
| home_team_wins_last_5 | 2.960 | 2.727 | 2.675 | 0.285 |
| away_team_away_goals_avg | 0.890 | 0.923 | 1.051 | 0.161 |
| away_team_away_conceded_avg | 1.475 | 1.366 | 1.346 | 0.129 |
| home_team_home_goals_avg | 1.454 | 1.413 | 1.350 | 0.104 |
| home_team_home_conceded_avg | 0.896 | 0.968 | 0.979 | 0.083 |
| away_team_away_win_rate | 0.467 | 0.470 | 0.526 | 0.059 |
| home_team_home_win_rate | 0.751 | 0.700 | 0.717 | 0.051 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\brazil1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\brazil1\charts\relationships_home_win_pct_by_position.png)

