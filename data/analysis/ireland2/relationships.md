# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:56:14+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Division 1 (Ireland)
- Scope: league `ireland2`

- Matches analysed: **179** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_points_before_match | 0.299 | 0.081 | 0.303 |
| points_difference | 0.366 | -0.211 | 0.161 |
| away_points_before_match | -0.019 | 0.261 | 0.160 |
| home_position_before_match | -0.284 | 0.117 | -0.157 |
| position_difference | -0.370 | 0.224 | -0.156 |
| home_team_goals_scored_last_5 | 0.167 | 0.022 | 0.153 |
| home_team_home_win_rate | 0.195 | -0.018 | 0.150 |
| home_team_wins_last_5 | 0.210 | -0.045 | 0.144 |
| home_team_home_goals_avg | 0.184 | -0.032 | 0.131 |
| home_team_points_last_5 | 0.186 | -0.040 | 0.127 |
| away_rest_days | 0.019 | 0.139 | 0.110 |
| rest_days_difference | -0.065 | -0.054 | -0.091 |
| away_team_goals_scored_last_5 | -0.088 | 0.208 | 0.067 |
| away_position_before_match | 0.241 | -0.202 | 0.064 |
| home_rest_days | -0.019 | 0.105 | 0.055 |
| away_team_points_last_5 | -0.115 | 0.218 | 0.051 |
| away_team_wins_last_5 | -0.133 | 0.231 | 0.045 |
| away_team_away_goals_avg | -0.100 | 0.063 | -0.040 |
| away_team_away_win_rate | -0.162 | 0.159 | -0.027 |
| home_team_home_conceded_avg | 0.008 | -0.038 | -0.020 |
| away_team_goals_conceded_last_5 | 0.090 | -0.088 | 0.016 |
| home_team_goals_conceded_last_5 | -0.063 | 0.073 | -0.004 |
| away_team_away_conceded_avg | 0.081 | -0.101 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 36 | 10 | 10 | 16 | 27.8% | 27.8% | 44.4% |
| -4..-2 | 28 | 12 | 8 | 8 | 42.9% | 28.6% | 28.6% |
| -1..1 | 40 | 18 | 9 | 13 | 45.0% | 22.5% | 32.5% |
| 2..4 | 50 | 26 | 11 | 13 | 52.0% | 22.0% | 26.0% |
| >4 | 25 | 15 | 4 | 6 | 60.0% | 16.0% | 24.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 15 | 11 | 3 | 1 | 73.3% | 20.0% | 6.7% |
| -5..-2 | 62 | 37 | 12 | 13 | 59.7% | 19.4% | 21.0% |
| -1..1 | 36 | 17 | 7 | 12 | 47.2% | 19.4% | 33.3% |
| 2..5 | 48 | 14 | 12 | 22 | 29.2% | 25.0% | 45.8% |
| >=6 | 18 | 2 | 8 | 8 | 11.1% | 44.4% | 44.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 12 | 6 | 3 | 3 | 50.0% | 25.0% | 25.0% |
| -1..0 | 12 | 4 | 3 | 5 | 33.3% | 25.0% | 41.7% |
| 0 | 125 | 58 | 29 | 38 | 46.4% | 23.2% | 30.4% |
| 1..2 | 17 | 8 | 4 | 5 | 47.1% | 23.5% | 29.4% |
| >2 | 7 | 3 | 2 | 2 | 42.9% | 28.6% | 28.6% |
| unknown | 6 | 2 | 1 | 3 | 33.3% | 16.7% | 50.0% |
- *6 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **36.1%** home win (39/108)
- `>= 0.5` tier: **59.2%** home win (42/71)
- Home-win gap (>= split minus < split): **+23.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 108 | 39 | 29 | 40 | 36.1% |
| high | >= 0.5 | 71 | 42 | 13 | 16 | 59.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.963 | -2.571 | -5.518 | 10.481 |
| home_points_before_match | 28.321 | 21.619 | 19.625 | 8.696 |
| position_difference | -1.593 | 0.833 | 1.464 | 3.057 |
| home_position_before_match | 4.444 | 6.310 | 6.107 | 1.865 |
| away_points_before_match | 23.358 | 24.190 | 25.143 | 1.785 |
| home_team_points_last_5 | 7.037 | 5.690 | 5.589 | 1.448 |
| away_position_before_match | 6.037 | 5.476 | 4.643 | 1.394 |
| home_team_goals_scored_last_5 | 6.914 | 5.762 | 5.786 | 1.152 |
| away_team_goals_scored_last_5 | 5.852 | 6.976 | 6.268 | 1.124 |
| away_team_goals_conceded_last_5 | 6.605 | 6.262 | 5.536 | 1.069 |
| away_team_points_last_5 | 5.852 | 6.714 | 6.786 | 0.934 |
| home_rest_days | 6.810 | 7.619 | 6.698 | 0.921 |
| away_rest_days | 7.000 | 7.512 | 6.667 | 0.846 |
| home_team_wins_last_5 | 2.012 | 1.524 | 1.482 | 0.530 |
| away_team_wins_last_5 | 1.531 | 1.905 | 1.929 | 0.398 |
| rest_days_difference | -0.190 | 0.122 | 0.038 | 0.312 |
| away_team_away_conceded_avg | 1.398 | 1.514 | 1.203 | 0.311 |
| home_team_home_goals_avg | 1.489 | 1.284 | 1.184 | 0.305 |
| away_team_away_goals_avg | 0.981 | 1.280 | 1.009 | 0.298 |
| home_team_goals_conceded_last_5 | 6.296 | 6.381 | 6.518 | 0.222 |
| home_team_home_win_rate | 0.445 | 0.386 | 0.347 | 0.098 |
| away_team_away_win_rate | 0.287 | 0.341 | 0.382 | 0.095 |
| home_team_home_conceded_avg | 1.107 | 1.080 | 1.028 | 0.079 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\ireland2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\ireland2\charts\relationships_home_win_pct_by_position.png)

