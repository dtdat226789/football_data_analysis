# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:24:08+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premiere Ligue Women (France)
- Scope: league `wfrance1`

- Matches analysed: **135** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_goals_avg | -0.032 | 0.302 | 0.216 |
| away_team_goals_scored_last_5 | -0.073 | 0.222 | 0.116 |
| home_position_before_match | -0.413 | 0.298 | -0.111 |
| away_position_before_match | 0.149 | -0.289 | -0.106 |
| home_team_home_conceded_avg | -0.295 | 0.181 | -0.105 |
| away_team_goals_conceded_last_5 | 0.073 | -0.197 | -0.097 |
| away_team_away_win_rate | -0.113 | 0.238 | 0.095 |
| home_team_goals_conceded_last_5 | -0.273 | 0.173 | -0.092 |
| home_team_home_win_rate | 0.342 | -0.256 | 0.085 |
| away_team_away_conceded_avg | 0.097 | -0.028 | 0.060 |
| points_difference | 0.441 | -0.395 | 0.057 |
| away_team_wins_last_5 | -0.087 | 0.163 | 0.057 |
| home_team_home_goals_avg | 0.326 | -0.278 | 0.053 |
| home_points_before_match | 0.306 | -0.262 | 0.049 |
| away_rest_days | 0.064 | -0.128 | -0.048 |
| rest_days_difference | 0.121 | -0.079 | 0.039 |
| home_rest_days | 0.098 | -0.149 | -0.037 |
| away_team_points_last_5 | -0.120 | 0.158 | 0.026 |
| home_team_goals_scored_last_5 | 0.311 | -0.309 | 0.016 |
| home_team_points_last_5 | 0.279 | -0.307 | -0.010 |
| away_points_before_match | -0.089 | 0.092 | -0.002 |
| position_difference | -0.412 | 0.433 | -0.002 |
| home_team_wins_last_5 | 0.299 | -0.316 | 0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 27 | 2 | 8 | 17 | 7.4% | 29.6% | 63.0% |
| -4..-2 | 24 | 7 | 3 | 14 | 29.2% | 12.5% | 58.3% |
| -1..1 | 34 | 13 | 6 | 15 | 38.2% | 17.6% | 44.1% |
| 2..4 | 20 | 12 | 3 | 5 | 60.0% | 15.0% | 25.0% |
| >4 | 30 | 19 | 5 | 6 | 63.3% | 16.7% | 20.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 17 | 13 | 4 | 0 | 76.5% | 23.5% | 0.0% |
| -5..-2 | 37 | 20 | 6 | 11 | 54.1% | 16.2% | 29.7% |
| -1..1 | 23 | 11 | 2 | 10 | 47.8% | 8.7% | 43.5% |
| 2..5 | 43 | 9 | 10 | 24 | 20.9% | 23.3% | 55.8% |
| >=6 | 15 | 0 | 3 | 12 | 0.0% | 20.0% | 80.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 3 | 1 | 0 | 2 | 33.3% | 0.0% | 66.7% |
| -1..0 | 15 | 6 | 4 | 5 | 40.0% | 26.7% | 33.3% |
| 0 | 88 | 33 | 15 | 40 | 37.5% | 17.0% | 45.5% |
| 1..2 | 21 | 9 | 4 | 8 | 42.9% | 19.0% | 38.1% |
| >2 | 2 | 1 | 1 | 0 | 50.0% | 50.0% | 0.0% |
| unknown | 6 | 3 | 1 | 2 | 50.0% | 16.7% | 33.3% |
- *6 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **28.6%** home win (24/84)
- `>= 0.5` tier: **56.9%** home win (29/51)
- Home-win gap (>= split minus < split): **+28.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 84 | 24 | 16 | 44 | 28.6% |
| high | >= 0.5 | 51 | 29 | 9 | 13 | 56.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 7.679 | -2.080 | -5.860 | 13.539 |
| home_points_before_match | 19.736 | 15.160 | 12.228 | 7.508 |
| away_points_before_match | 12.057 | 17.240 | 18.088 | 6.031 |
| position_difference | -2.811 | -0.040 | 2.526 | 5.338 |
| home_team_goals_scored_last_5 | 8.792 | 5.360 | 5.316 | 3.477 |
| home_rest_days | 12.980 | 10.042 | 10.891 | 2.938 |
| home_position_before_match | 4.774 | 6.640 | 7.702 | 2.928 |
| away_rest_days | 12.740 | 9.875 | 11.000 | 2.865 |
| home_team_points_last_5 | 7.717 | 5.480 | 5.070 | 2.647 |
| home_team_goals_conceded_last_5 | 4.943 | 7.240 | 7.421 | 2.478 |
| away_position_before_match | 7.585 | 6.680 | 5.175 | 2.409 |
| away_team_points_last_5 | 5.094 | 6.400 | 7.228 | 2.134 |
| away_team_goals_scored_last_5 | 5.528 | 6.840 | 7.368 | 1.840 |
| away_team_goals_conceded_last_5 | 7.283 | 6.680 | 5.509 | 1.774 |
| home_team_wins_last_5 | 2.340 | 1.520 | 1.368 | 0.971 |
| home_team_home_goals_avg | 1.964 | 1.204 | 1.195 | 0.769 |
| away_team_wins_last_5 | 1.453 | 1.920 | 2.105 | 0.652 |
| home_team_home_conceded_avg | 1.129 | 1.609 | 1.681 | 0.553 |
| away_team_away_goals_avg | 1.278 | 1.577 | 1.755 | 0.477 |
| rest_days_difference | 0.240 | 0.167 | -0.109 | 0.349 |
| home_team_home_win_rate | 0.527 | 0.337 | 0.320 | 0.207 |
| away_team_away_win_rate | 0.289 | 0.400 | 0.456 | 0.168 |
| away_team_away_conceded_avg | 1.494 | 1.405 | 1.428 | 0.089 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\wfrance1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\wfrance1\charts\relationships_home_win_pct_by_position.png)

