# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:01:27+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premier Division (Ireland)
- Scope: league `ireland1`

- Matches analysed: **338** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.157 | 0.040 | 0.134 |
| away_team_goals_conceded_last_5 | 0.152 | 0.034 | 0.127 |
| away_position_before_match | 0.240 | -0.063 | 0.125 |
| position_difference | -0.250 | 0.106 | -0.105 |
| away_team_points_last_5 | -0.161 | 0.017 | -0.100 |
| points_difference | 0.218 | -0.092 | 0.092 |
| home_team_goals_conceded_last_5 | -0.150 | 0.038 | -0.079 |
| away_team_away_win_rate | -0.136 | 0.024 | -0.079 |
| home_team_home_goals_avg | -0.017 | -0.093 | -0.072 |
| home_team_wins_last_5 | 0.105 | -0.005 | 0.069 |
| away_team_away_goals_avg | -0.097 | 0.000 | -0.067 |
| away_team_wins_last_5 | -0.096 | 0.017 | -0.056 |
| away_points_before_match | -0.115 | 0.037 | -0.056 |
| away_rest_days | -0.065 | 0.001 | -0.044 |
| home_team_points_last_5 | 0.101 | -0.044 | 0.042 |
| home_team_home_win_rate | 0.067 | -0.008 | 0.041 |
| rest_days_difference | 0.055 | -0.013 | 0.030 |
| home_team_home_conceded_avg | -0.123 | 0.087 | -0.029 |
| home_position_before_match | -0.117 | 0.087 | -0.025 |
| home_team_goals_scored_last_5 | 0.022 | -0.054 | -0.020 |
| home_rest_days | -0.021 | -0.008 | -0.019 |
| home_points_before_match | 0.040 | -0.028 | 0.010 |
| away_team_goals_scored_last_5 | -0.060 | 0.054 | -0.007 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 55 | 14 | 20 | 21 | 25.5% | 36.4% | 38.2% |
| -4..-2 | 69 | 24 | 23 | 22 | 34.8% | 33.3% | 31.9% |
| -1..1 | 100 | 48 | 26 | 26 | 48.0% | 26.0% | 26.0% |
| 2..4 | 69 | 32 | 20 | 17 | 46.4% | 29.0% | 24.6% |
| >4 | 45 | 19 | 14 | 12 | 42.2% | 31.1% | 26.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 33 | 19 | 7 | 7 | 57.6% | 21.2% | 21.2% |
| -5..-2 | 104 | 53 | 27 | 24 | 51.0% | 26.0% | 23.1% |
| -1..1 | 72 | 24 | 25 | 23 | 33.3% | 34.7% | 31.9% |
| 2..5 | 87 | 34 | 29 | 24 | 39.1% | 33.3% | 27.6% |
| >=6 | 42 | 7 | 15 | 20 | 16.7% | 35.7% | 47.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 41 | 17 | 16 | 8 | 41.5% | 39.0% | 19.5% |
| -1..0 | 23 | 7 | 8 | 8 | 30.4% | 34.8% | 34.8% |
| 0 | 209 | 87 | 61 | 61 | 41.6% | 29.2% | 29.2% |
| 1..2 | 27 | 7 | 8 | 12 | 25.9% | 29.6% | 44.4% |
| >2 | 27 | 15 | 5 | 7 | 55.6% | 18.5% | 25.9% |
| unknown | 11 | 4 | 5 | 2 | 36.4% | 45.5% | 18.2% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **46.8%** home win (22/47)
- `>= 0.5` tier: **39.5%** home win (115/291)
- Home-win gap (>= split minus < split): **-7.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 47 | 22 | 13 | 12 | 46.8% |
| high | >= 0.5 | 291 | 115 | 90 | 86 | 39.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.635 | -1.709 | -2.490 | 5.125 |
| away_points_before_match | 20.321 | 22.883 | 24.235 | 3.914 |
| position_difference | -1.015 | 0.612 | 1.092 | 2.106 |
| home_points_before_match | 22.956 | 21.175 | 21.745 | 1.781 |
| away_position_before_match | 6.212 | 5.039 | 4.806 | 1.406 |
| away_team_points_last_5 | 5.708 | 6.447 | 6.776 | 1.067 |
| home_team_goals_conceded_last_5 | 5.606 | 6.039 | 6.429 | 0.823 |
| away_rest_days | 6.978 | 7.796 | 7.771 | 0.818 |
| rest_days_difference | 0.158 | -0.602 | -0.375 | 0.760 |
| away_team_goals_scored_last_5 | 5.628 | 6.039 | 6.347 | 0.719 |
| home_position_before_match | 5.197 | 5.650 | 5.898 | 0.701 |
| away_team_goals_conceded_last_5 | 6.109 | 5.563 | 5.602 | 0.546 |
| home_team_points_last_5 | 6.226 | 5.981 | 5.755 | 0.471 |
| away_team_wins_last_5 | 2.891 | 3.029 | 3.204 | 0.314 |
| home_rest_days | 7.098 | 7.192 | 7.396 | 0.298 |
| home_team_goals_scored_last_5 | 5.891 | 5.854 | 5.633 | 0.258 |
| home_team_wins_last_5 | 3.029 | 2.816 | 2.939 | 0.214 |
| home_team_home_conceded_avg | 0.975 | 1.050 | 1.129 | 0.154 |
| away_team_away_goals_avg | 0.990 | 1.075 | 1.127 | 0.138 |
| away_team_away_conceded_avg | 1.401 | 1.304 | 1.290 | 0.111 |
| away_team_away_win_rate | 0.491 | 0.569 | 0.586 | 0.095 |
| home_team_home_goals_avg | 1.345 | 1.374 | 1.312 | 0.062 |
| home_team_home_win_rate | 0.683 | 0.687 | 0.685 | 0.004 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\ireland1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\ireland1\charts\relationships_home_win_pct_by_position.png)

