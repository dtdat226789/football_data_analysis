# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:48:01+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: LaLiga (Spain)
- Scope: league `spain1`

- Matches analysed: **449** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.277 | 0.035 | -0.196 |
| home_team_home_goals_avg | 0.275 | -0.047 | 0.186 |
| home_team_goals_scored_last_5 | 0.247 | -0.023 | 0.180 |
| home_team_points_last_5 | 0.218 | -0.041 | 0.146 |
| points_difference | 0.273 | -0.111 | 0.143 |
| home_team_wins_last_5 | 0.180 | -0.021 | 0.128 |
| position_difference | -0.262 | 0.129 | -0.124 |
| away_team_away_goals_avg | -0.029 | 0.189 | 0.100 |
| home_points_before_match | 0.167 | -0.051 | 0.099 |
| home_team_goals_conceded_last_5 | -0.131 | 0.034 | -0.082 |
| home_rest_days | -0.055 | -0.038 | -0.068 |
| home_team_home_win_rate | 0.149 | -0.085 | 0.062 |
| away_team_goals_scored_last_5 | -0.046 | 0.153 | 0.062 |
| rest_days_difference | -0.065 | -0.010 | -0.058 |
| away_rest_days | -0.024 | -0.030 | -0.038 |
| away_team_wins_last_5 | 0.002 | 0.053 | 0.036 |
| away_team_away_conceded_avg | 0.036 | -0.090 | -0.030 |
| home_team_home_conceded_avg | -0.121 | 0.104 | -0.029 |
| away_team_away_win_rate | -0.045 | 0.098 | 0.029 |
| away_position_before_match | 0.089 | -0.145 | -0.024 |
| away_team_points_last_5 | -0.044 | 0.090 | 0.023 |
| away_team_goals_conceded_last_5 | 0.007 | -0.018 | -0.006 |
| away_points_before_match | -0.029 | 0.029 | -0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 73 | 27 | 21 | 25 | 37.0% | 28.8% | 34.2% |
| -4..-2 | 96 | 41 | 25 | 30 | 42.7% | 26.0% | 31.2% |
| -1..1 | 139 | 65 | 34 | 40 | 46.8% | 24.5% | 28.8% |
| 2..4 | 89 | 46 | 21 | 22 | 51.7% | 23.6% | 24.7% |
| >4 | 52 | 38 | 9 | 5 | 73.1% | 17.3% | 9.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 104 | 72 | 14 | 18 | 69.2% | 13.5% | 17.3% |
| -5..-2 | 79 | 43 | 18 | 18 | 54.4% | 22.8% | 22.8% |
| -1..1 | 58 | 24 | 17 | 17 | 41.4% | 29.3% | 29.3% |
| 2..5 | 80 | 27 | 25 | 28 | 33.8% | 31.2% | 35.0% |
| >=6 | 128 | 51 | 36 | 41 | 39.8% | 28.1% | 32.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 47 | 26 | 12 | 9 | 55.3% | 25.5% | 19.1% |
| -1..0 | 110 | 53 | 30 | 27 | 48.2% | 27.3% | 24.5% |
| 0 | 117 | 53 | 28 | 36 | 45.3% | 23.9% | 30.8% |
| 1..2 | 136 | 67 | 29 | 40 | 49.3% | 21.3% | 29.4% |
| >2 | 17 | 8 | 5 | 4 | 47.1% | 29.4% | 23.5% |
| unknown | 22 | 10 | 6 | 6 | 45.5% | 27.3% | 27.3% |
- *22 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.5%** home win (30/80)
- `>= 0.5` tier: **50.7%** home win (187/369)
- Home-win gap (>= split minus < split): **+13.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 80 | 30 | 26 | 24 | 37.5% |
| high | >= 0.5 | 369 | 187 | 84 | 98 | 50.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 24.917 | 17.773 | 20.361 | 7.144 |
| points_difference | 2.945 | -2.664 | -4.098 | 7.043 |
| position_difference | -1.673 | 2.373 | 2.287 | 4.046 |
| away_points_before_match | 21.972 | 20.436 | 24.459 | 4.023 |
| home_position_before_match | 9.585 | 13.209 | 11.238 | 3.624 |
| away_position_before_match | 11.258 | 10.836 | 8.951 | 2.307 |
| home_team_points_last_5 | 6.442 | 4.682 | 5.648 | 1.761 |
| home_team_goals_scored_last_5 | 6.419 | 4.664 | 5.574 | 1.756 |
| away_team_points_last_5 | 5.885 | 5.627 | 6.967 | 1.340 |
| away_team_goals_scored_last_5 | 5.682 | 5.682 | 6.877 | 1.195 |
| home_team_goals_conceded_last_5 | 5.590 | 6.273 | 6.238 | 0.683 |
| away_rest_days | 7.126 | 7.610 | 7.085 | 0.524 |
| away_team_goals_conceded_last_5 | 5.857 | 6.082 | 5.582 | 0.500 |
| home_team_home_goals_avg | 1.593 | 1.107 | 1.284 | 0.486 |
| home_rest_days | 7.101 | 7.587 | 7.314 | 0.485 |
| home_team_wins_last_5 | 2.820 | 2.355 | 2.615 | 0.466 |
| away_team_wins_last_5 | 2.751 | 2.573 | 2.951 | 0.378 |
| away_team_away_goals_avg | 0.971 | 0.957 | 1.258 | 0.302 |
| rest_days_difference | -0.024 | -0.019 | 0.250 | 0.274 |
| home_team_home_conceded_avg | 0.925 | 1.078 | 1.169 | 0.245 |
| away_team_away_conceded_avg | 1.415 | 1.435 | 1.314 | 0.121 |
| home_team_home_win_rate | 0.722 | 0.603 | 0.636 | 0.119 |
| away_team_away_win_rate | 0.450 | 0.484 | 0.525 | 0.075 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\spain1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\spain1\charts\relationships_home_win_pct_by_position.png)

