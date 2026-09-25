# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:50:25+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 1. Lig (Turkey)
- Scope: league `turkey2`

- Matches analysed: **465** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_conceded_last_5 | 0.385 | -0.136 | 0.221 |
| home_team_home_conceded_avg | -0.133 | 0.428 | 0.205 |
| away_team_away_conceded_avg | 0.311 | -0.122 | 0.170 |
| home_team_goals_conceded_last_5 | -0.150 | 0.393 | 0.165 |
| home_position_before_match | -0.121 | 0.350 | 0.158 |
| away_position_before_match | 0.316 | -0.169 | 0.140 |
| away_team_wins_last_5 | -0.230 | 0.084 | -0.130 |
| away_team_points_last_5 | -0.234 | 0.104 | -0.118 |
| away_points_before_match | -0.185 | 0.095 | -0.085 |
| home_team_home_win_rate | 0.123 | -0.239 | -0.073 |
| home_team_wins_last_5 | 0.152 | -0.264 | -0.067 |
| home_points_before_match | 0.090 | -0.191 | -0.065 |
| away_team_goals_scored_last_5 | -0.154 | 0.093 | -0.060 |
| away_team_away_goals_avg | -0.123 | 0.063 | -0.057 |
| away_team_away_win_rate | -0.156 | 0.112 | -0.048 |
| home_team_points_last_5 | 0.162 | -0.237 | -0.040 |
| home_rest_days | -0.027 | -0.017 | -0.035 |
| home_team_home_goals_avg | 0.100 | -0.160 | -0.035 |
| away_rest_days | 0.009 | -0.048 | -0.028 |
| points_difference | 0.399 | -0.414 | 0.028 |
| home_team_goals_scored_last_5 | 0.153 | -0.146 | 0.021 |
| rest_days_difference | -0.089 | 0.074 | -0.019 |
| position_difference | -0.321 | 0.378 | 0.011 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 85 | 17 | 19 | 49 | 20.0% | 22.4% | 57.6% |
| -4..-2 | 89 | 36 | 25 | 28 | 40.4% | 28.1% | 31.5% |
| -1..1 | 128 | 56 | 38 | 34 | 43.8% | 29.7% | 26.6% |
| 2..4 | 95 | 47 | 29 | 19 | 49.5% | 30.5% | 20.0% |
| >4 | 68 | 47 | 12 | 9 | 69.1% | 17.6% | 13.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 118 | 74 | 28 | 16 | 62.7% | 23.7% | 13.6% |
| -5..-2 | 72 | 42 | 18 | 12 | 58.3% | 25.0% | 16.7% |
| -1..1 | 74 | 30 | 23 | 21 | 40.5% | 31.1% | 28.4% |
| 2..5 | 74 | 23 | 23 | 28 | 31.1% | 31.1% | 37.8% |
| >=6 | 127 | 34 | 31 | 62 | 26.8% | 24.4% | 48.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 29 | 17 | 8 | 4 | 58.6% | 27.6% | 13.8% |
| -1..0 | 96 | 39 | 26 | 31 | 40.6% | 27.1% | 32.3% |
| 0 | 182 | 86 | 41 | 55 | 47.3% | 22.5% | 30.2% |
| 1..2 | 132 | 52 | 40 | 40 | 39.4% | 30.3% | 30.3% |
| >2 | 6 | 1 | 1 | 4 | 16.7% | 16.7% | 66.7% |
| unknown | 20 | 8 | 7 | 5 | 40.0% | 35.0% | 25.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **31.2%** home win (30/96)
- `>= 0.5` tier: **46.9%** home win (173/369)
- Home-win gap (>= split minus < split): **+15.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 96 | 30 | 25 | 41 | 31.2% |
| high | >= 0.5 | 369 | 173 | 98 | 98 | 46.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.005 | -0.528 | -7.216 | 12.221 |
| position_difference | -2.562 | 0.341 | 4.173 | 6.734 |
| away_points_before_match | 19.970 | 21.057 | 26.576 | 6.605 |
| home_points_before_match | 24.975 | 20.528 | 19.360 | 5.616 |
| home_position_before_match | 9.616 | 10.154 | 13.151 | 3.535 |
| home_team_goals_conceded_last_5 | 5.256 | 5.553 | 8.496 | 3.240 |
| away_position_before_match | 12.177 | 9.813 | 8.978 | 3.199 |
| away_team_goals_conceded_last_5 | 7.424 | 4.919 | 5.374 | 2.505 |
| home_team_points_last_5 | 6.532 | 5.984 | 4.813 | 1.719 |
| away_team_points_last_5 | 5.414 | 6.203 | 6.978 | 1.565 |
| away_team_goals_scored_last_5 | 5.906 | 6.211 | 7.309 | 1.403 |
| home_team_goals_scored_last_5 | 6.660 | 6.114 | 5.317 | 1.344 |
| home_team_wins_last_5 | 3.025 | 2.732 | 2.295 | 0.730 |
| home_team_home_conceded_avg | 0.947 | 0.944 | 1.557 | 0.613 |
| away_rest_days | 7.077 | 7.147 | 6.552 | 0.594 |
| away_team_wins_last_5 | 2.557 | 2.870 | 3.022 | 0.465 |
| home_rest_days | 7.051 | 7.207 | 6.754 | 0.453 |
| away_team_away_conceded_avg | 1.678 | 1.314 | 1.364 | 0.363 |
| rest_days_difference | -0.026 | 0.060 | 0.201 | 0.227 |
| home_team_home_goals_avg | 1.566 | 1.515 | 1.352 | 0.214 |
| away_team_away_goals_avg | 1.074 | 1.178 | 1.196 | 0.122 |
| home_team_home_win_rate | 0.711 | 0.709 | 0.604 | 0.107 |
| away_team_away_win_rate | 0.463 | 0.532 | 0.555 | 0.092 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\turkey2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\turkey2\charts\relationships_home_win_pct_by_position.png)

