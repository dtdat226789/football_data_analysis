# Relationships Analysis
- Report: `relationships`
- Generated: 2026-10-30T03:52:41+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Bundesliga (Germany)
- Scope: league `germany1`

- Matches analysed: **1634** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.280 | 0.126 | -0.138 |
| home_team_home_goals_avg | 0.247 | -0.093 | 0.134 |
| home_team_home_win_rate | 0.216 | -0.106 | 0.100 |
| home_team_goals_conceded_last_5 | -0.134 | 0.021 | -0.094 |
| away_position_before_match | 0.118 | -0.262 | -0.092 |
| home_team_home_conceded_avg | -0.147 | 0.042 | -0.089 |
| home_team_goals_scored_last_5 | 0.187 | -0.108 | 0.075 |
| away_team_away_conceded_avg | 0.024 | -0.126 | -0.071 |
| home_points_before_match | 0.147 | -0.080 | 0.062 |
| away_team_goals_scored_last_5 | -0.112 | 0.211 | 0.059 |
| away_team_goals_conceded_last_5 | 0.051 | -0.140 | -0.059 |
| away_team_away_win_rate | -0.083 | 0.176 | 0.058 |
| away_team_away_goals_avg | -0.110 | 0.202 | 0.055 |
| away_rest_days | 0.067 | -0.005 | 0.050 |
| home_rest_days | 0.061 | -0.003 | 0.047 |
| home_team_wins_last_5 | 0.169 | -0.131 | 0.044 |
| home_team_points_last_5 | 0.164 | -0.133 | 0.039 |
| away_points_before_match | -0.081 | 0.145 | 0.038 |
| position_difference | -0.290 | 0.284 | -0.033 |
| away_team_wins_last_5 | -0.101 | 0.158 | 0.031 |
| points_difference | 0.271 | -0.268 | 0.029 |
| away_team_points_last_5 | -0.109 | 0.158 | 0.025 |
| rest_days_difference | -0.006 | 0.001 | -0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 297 | 88 | 66 | 143 | 29.6% | 22.2% | 48.1% |
| -4..-2 | 312 | 116 | 84 | 112 | 37.2% | 26.9% | 35.9% |
| -1..1 | 458 | 193 | 115 | 150 | 42.1% | 25.1% | 32.8% |
| 2..4 | 306 | 153 | 72 | 81 | 50.0% | 23.5% | 26.5% |
| >4 | 261 | 162 | 67 | 32 | 62.1% | 25.7% | 12.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 360 | 227 | 89 | 44 | 63.1% | 24.7% | 12.2% |
| -5..-2 | 308 | 159 | 72 | 77 | 51.6% | 23.4% | 25.0% |
| -1..1 | 250 | 104 | 68 | 78 | 41.6% | 27.2% | 31.2% |
| 2..5 | 372 | 141 | 96 | 135 | 37.9% | 25.8% | 36.3% |
| >=6 | 344 | 81 | 79 | 184 | 23.5% | 23.0% | 53.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 142 | 71 | 40 | 31 | 50.0% | 28.2% | 21.8% |
| -1..0 | 391 | 174 | 101 | 116 | 44.5% | 25.8% | 29.7% |
| 0 | 563 | 238 | 134 | 191 | 42.3% | 23.8% | 33.9% |
| 1..2 | 377 | 151 | 94 | 132 | 40.1% | 24.9% | 35.0% |
| >2 | 106 | 51 | 25 | 30 | 48.1% | 23.6% | 28.3% |
| unknown | 55 | 27 | 10 | 18 | 49.1% | 18.2% | 32.7% |
- *55 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **36.6%** home win (352/963)
- `>= 0.5` tier: **53.7%** home win (360/671)
- Home-win gap (>= split minus < split): **+17.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 963 | 352 | 247 | 364 | 36.6% |
| high | >= 0.5 | 671 | 360 | 157 | 154 | 53.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.747 | 0.218 | -5.857 | 9.604 |
| position_difference | -2.065 | -0.020 | 3.180 | 5.244 |
| away_points_before_match | 19.485 | 20.928 | 24.583 | 5.098 |
| home_points_before_match | 23.232 | 21.146 | 18.726 | 4.506 |
| away_position_before_match | 9.992 | 9.480 | 7.313 | 2.679 |
| home_position_before_match | 7.927 | 9.460 | 10.492 | 2.565 |
| away_team_goals_scored_last_5 | 6.388 | 6.938 | 8.162 | 1.775 |
| home_team_points_last_5 | 6.747 | 6.196 | 5.299 | 1.448 |
| home_team_goals_scored_last_5 | 7.664 | 6.691 | 6.222 | 1.442 |
| away_team_points_last_5 | 5.767 | 6.265 | 7.164 | 1.397 |
| away_team_goals_conceded_last_5 | 7.306 | 6.995 | 6.363 | 0.943 |
| home_team_goals_conceded_last_5 | 6.728 | 7.272 | 7.514 | 0.786 |
| away_rest_days | 8.766 | 8.906 | 8.333 | 0.573 |
| home_team_wins_last_5 | 1.879 | 1.708 | 1.375 | 0.505 |
| away_team_wins_last_5 | 1.559 | 1.720 | 2.014 | 0.455 |
| home_team_home_goals_avg | 1.863 | 1.538 | 1.460 | 0.402 |
| home_rest_days | 8.722 | 8.797 | 8.442 | 0.355 |
| away_team_away_goals_avg | 1.227 | 1.327 | 1.538 | 0.312 |
| home_team_home_conceded_avg | 1.263 | 1.337 | 1.467 | 0.204 |
| rest_days_difference | -0.047 | -0.099 | 0.102 | 0.201 |
| away_team_away_conceded_avg | 1.694 | 1.701 | 1.545 | 0.156 |
| home_team_home_win_rate | 0.465 | 0.397 | 0.339 | 0.125 |
| away_team_away_win_rate | 0.274 | 0.287 | 0.351 | 0.077 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](charts/relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](charts/relationships_home_win_pct_by_position.png)

