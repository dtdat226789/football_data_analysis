# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:57:23+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

- Matches analysed: **34** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.508 | -0.023 | 0.402 |
| home_team_goals_conceded_last_5 | 0.342 | 0.096 | 0.341 |
| home_position_before_match | 0.233 | 0.210 | 0.323 |
| away_team_goals_conceded_last_5 | 0.415 | -0.028 | 0.322 |
| away_team_away_win_rate | 0.467 | -0.108 | 0.315 |
| away_team_goals_scored_last_5 | 0.414 | -0.070 | 0.295 |
| away_team_away_goals_avg | 0.522 | -0.243 | 0.275 |
| away_team_points_last_5 | 0.390 | -0.077 | 0.271 |
| away_points_before_match | 0.390 | -0.077 | 0.271 |
| away_team_wins_last_5 | 0.399 | -0.095 | 0.267 |
| position_difference | 0.191 | 0.107 | 0.223 |
| home_team_wins_last_5 | 0.435 | -0.252 | 0.198 |
| points_difference | -0.086 | -0.195 | -0.193 |
| away_rest_days | 0.047 | 0.226 | 0.174 |
| home_team_goals_scored_last_5 | 0.329 | -0.195 | 0.147 |
| home_rest_days | -0.052 | 0.266 | 0.124 |
| home_team_home_win_rate | 0.312 | -0.217 | 0.119 |
| home_team_home_goals_avg | 0.235 | -0.127 | 0.113 |
| home_team_home_conceded_avg | 0.178 | -0.058 | 0.110 |
| home_team_points_last_5 | 0.289 | -0.308 | 0.043 |
| home_points_before_match | 0.289 | -0.308 | 0.043 |
| away_position_before_match | -0.050 | 0.044 | -0.014 |
| rest_days_difference | -0.113 | 0.168 | 0.013 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 3 | 2 | 0 | 1 | 66.7% | 0.0% | 33.3% |
| -4..-2 | 3 | 2 | 0 | 1 | 66.7% | 0.0% | 33.3% |
| -1..1 | 21 | 6 | 6 | 9 | 28.6% | 28.6% | 42.9% |
| 2..4 | 5 | 2 | 3 | 0 | 40.0% | 60.0% | 0.0% |
| >4 | 2 | 2 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 10 | 4 | 3 | 3 | 40.0% | 30.0% | 30.0% |
| -5..-2 | 3 | 1 | 2 | 0 | 33.3% | 66.7% | 0.0% |
| -1..1 | 9 | 3 | 1 | 5 | 33.3% | 11.1% | 55.6% |
| 2..5 | 6 | 2 | 3 | 1 | 33.3% | 50.0% | 16.7% |
| >=6 | 6 | 4 | 0 | 2 | 66.7% | 0.0% | 33.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 7 | 4 | 2 | 1 | 57.1% | 28.6% | 14.3% |
| -1..0 | 1 | 0 | 0 | 1 | 0.0% | 0.0% | 100.0% |
| 0 | 10 | 6 | 2 | 2 | 60.0% | 20.0% | 20.0% |
| 1..2 | 5 | 3 | 1 | 1 | 60.0% | 20.0% | 20.0% |
| >2 | 1 | 0 | 1 | 0 | 0.0% | 100.0% | 0.0% |
| unknown | 10 | 1 | 3 | 6 | 10.0% | 30.0% | 60.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **28.0%** home win (7/25)
- `>= 0.5` tier: **77.8%** home win (7/9)
- Home-win gap (>= split minus < split): **+49.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 25 | 7 | 7 | 11 | 28.0% |
| high | >= 0.5 | 9 | 7 | 2 | 0 | 77.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| position_difference | 0.357 | -2.444 | 1.091 | 3.535 |
| home_team_goals_scored_last_5 | 4.357 | 2.556 | 1.000 | 3.357 |
| away_team_goals_conceded_last_5 | 4.571 | 2.667 | 1.364 | 3.208 |
| home_team_points_last_5 | 3.429 | 2.333 | 0.455 | 2.974 |
| home_points_before_match | 3.429 | 2.333 | 0.455 | 2.974 |
| away_position_before_match | 8.214 | 10.333 | 7.455 | 2.879 |
| away_team_goals_scored_last_5 | 4.643 | 2.556 | 1.818 | 2.825 |
| home_team_goals_conceded_last_5 | 4.071 | 1.889 | 1.727 | 2.344 |
| home_rest_days | 8.154 | 10.143 | 8.600 | 1.989 |
| away_team_points_last_5 | 3.429 | 1.556 | 1.455 | 1.974 |
| away_points_before_match | 3.429 | 1.556 | 1.455 | 1.974 |
| points_difference | 0.000 | 0.778 | -1.000 | 1.778 |
| away_team_away_goals_avg | 1.750 | 1.111 | 0.273 | 1.477 |
| home_team_home_goals_avg | 1.643 | 0.611 | 0.182 | 1.461 |
| rest_days_difference | -0.846 | 0.500 | -0.400 | 1.346 |
| home_team_wins_last_5 | 1.571 | 1.000 | 0.273 | 1.299 |
| home_team_home_conceded_avg | 1.643 | 0.444 | 0.545 | 1.198 |
| away_team_away_conceded_avg | 1.214 | 0.778 | 0.091 | 1.123 |
| away_team_wins_last_5 | 1.429 | 1.111 | 0.545 | 0.883 |
| home_position_before_match | 8.571 | 7.889 | 8.545 | 0.683 |
| home_team_home_win_rate | 0.429 | 0.222 | 0.000 | 0.429 |
| away_team_away_win_rate | 0.607 | 0.444 | 0.182 | 0.425 |
| away_rest_days | 9.000 | 9.286 | 9.333 | 0.333 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\develop21\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\develop21\charts\relationships_home_win_pct_by_position.png)

