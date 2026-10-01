# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:10:08+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Challenge League (Switzerland)
- Scope: league `swiss2`

- Matches analysed: **186** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_points_before_match | -0.017 | 0.253 | 0.164 |
| home_points_before_match | 0.173 | 0.048 | 0.159 |
| away_team_away_win_rate | -0.012 | 0.220 | 0.145 |
| home_team_home_conceded_avg | -0.140 | -0.061 | -0.144 |
| home_team_home_win_rate | 0.233 | -0.037 | 0.144 |
| away_team_away_goals_avg | -0.008 | 0.159 | 0.105 |
| away_team_wins_last_5 | -0.093 | 0.233 | 0.095 |
| away_position_before_match | 0.114 | -0.254 | -0.093 |
| home_team_points_last_5 | 0.133 | -0.017 | 0.085 |
| home_team_home_goals_avg | 0.210 | -0.109 | 0.077 |
| home_team_goals_conceded_last_5 | -0.080 | -0.027 | -0.077 |
| home_position_before_match | -0.232 | 0.136 | -0.074 |
| home_team_goals_scored_last_5 | 0.130 | -0.032 | 0.072 |
| away_rest_days | -0.057 | -0.043 | -0.072 |
| away_team_points_last_5 | -0.102 | 0.208 | 0.070 |
| home_team_wins_last_5 | 0.118 | -0.029 | 0.066 |
| home_rest_days | -0.054 | -0.031 | -0.061 |
| away_team_goals_conceded_last_5 | 0.075 | 0.007 | 0.060 |
| away_team_away_conceded_avg | -0.007 | -0.073 | -0.056 |
| away_team_goals_scored_last_5 | -0.101 | 0.155 | 0.034 |
| rest_days_difference | -0.003 | 0.029 | 0.018 |
| position_difference | -0.247 | 0.278 | 0.013 |
| points_difference | 0.223 | -0.239 | -0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 32 | 9 | 4 | 19 | 28.1% | 12.5% | 59.4% |
| -4..-2 | 37 | 15 | 9 | 13 | 40.5% | 24.3% | 35.1% |
| -1..1 | 52 | 18 | 13 | 21 | 34.6% | 25.0% | 40.4% |
| 2..4 | 34 | 20 | 9 | 5 | 58.8% | 26.5% | 14.7% |
| >4 | 31 | 21 | 5 | 5 | 67.7% | 16.1% | 16.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 14 | 13 | 1 | 0 | 92.9% | 7.1% | 0.0% |
| -5..-2 | 53 | 32 | 12 | 9 | 60.4% | 22.6% | 17.0% |
| -1..1 | 45 | 18 | 11 | 16 | 40.0% | 24.4% | 35.6% |
| 2..5 | 54 | 17 | 10 | 27 | 31.5% | 18.5% | 50.0% |
| >=6 | 20 | 3 | 6 | 11 | 15.0% | 30.0% | 55.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 22 | 10 | 6 | 6 | 45.5% | 27.3% | 27.3% |
| -1..0 | 34 | 14 | 5 | 15 | 41.2% | 14.7% | 44.1% |
| 0 | 66 | 32 | 17 | 17 | 48.5% | 25.8% | 25.8% |
| 1..2 | 49 | 22 | 7 | 20 | 44.9% | 14.3% | 40.8% |
| >2 | 8 | 3 | 2 | 3 | 37.5% | 25.0% | 37.5% |
| unknown | 7 | 2 | 3 | 2 | 28.6% | 42.9% | 28.6% |
- *7 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **36.9%** home win (45/122)
- `>= 0.5` tier: **59.4%** home win (38/64)
- Home-win gap (>= split minus < split): **+22.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 122 | 45 | 30 | 47 | 36.9% |
| high | >= 0.5 | 64 | 38 | 10 | 16 | 59.4% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.205 | -0.075 | -8.000 | 13.205 |
| away_points_before_match | 20.663 | 22.875 | 30.778 | 10.115 |
| position_difference | -1.651 | 0.550 | 2.111 | 3.762 |
| home_points_before_match | 25.867 | 22.800 | 22.778 | 3.090 |
| away_team_points_last_5 | 5.771 | 5.525 | 7.952 | 2.427 |
| away_team_goals_scored_last_5 | 6.253 | 6.025 | 8.238 | 2.213 |
| away_position_before_match | 6.458 | 5.950 | 4.413 | 2.045 |
| home_position_before_match | 4.807 | 6.500 | 6.524 | 1.717 |
| home_team_goals_scored_last_5 | 7.277 | 5.925 | 6.349 | 1.352 |
| home_team_points_last_5 | 6.771 | 5.675 | 5.841 | 1.096 |
| home_team_goals_conceded_last_5 | 6.506 | 6.350 | 7.286 | 0.936 |
| away_team_wins_last_5 | 1.542 | 1.525 | 2.349 | 0.824 |
| home_rest_days | 8.519 | 8.270 | 8.887 | 0.617 |
| away_team_goals_conceded_last_5 | 6.867 | 6.375 | 6.889 | 0.514 |
| away_team_away_goals_avg | 1.163 | 1.036 | 1.531 | 0.495 |
| away_rest_days | 8.481 | 8.053 | 8.484 | 0.431 |
| rest_days_difference | 0.037 | 0.243 | 0.443 | 0.406 |
| home_team_home_goals_avg | 1.666 | 1.276 | 1.324 | 0.390 |
| home_team_wins_last_5 | 1.940 | 1.575 | 1.603 | 0.365 |
| home_team_home_win_rate | 0.518 | 0.336 | 0.407 | 0.182 |
| home_team_home_conceded_avg | 1.148 | 1.324 | 1.293 | 0.177 |
| away_team_away_win_rate | 0.238 | 0.233 | 0.379 | 0.146 |
| away_team_away_conceded_avg | 1.481 | 1.393 | 1.494 | 0.100 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\swiss2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\swiss2\charts\relationships_home_win_pct_by_position.png)

