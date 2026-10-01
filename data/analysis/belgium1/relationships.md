# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:45:10+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Jupiler Pro League (Belgium)
- Scope: league `belgium1`

- Matches analysed: **321** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.079 | 0.086 | 0.117 |
| home_team_wins_last_5 | 0.074 | 0.056 | 0.092 |
| away_rest_days | -0.049 | -0.076 | -0.088 |
| home_team_points_last_5 | 0.058 | 0.062 | 0.084 |
| home_points_before_match | 0.140 | -0.035 | 0.077 |
| home_team_goals_conceded_last_5 | -0.115 | 0.015 | -0.073 |
| away_points_before_match | 0.018 | 0.081 | 0.069 |
| home_rest_days | -0.029 | -0.065 | -0.066 |
| rest_days_difference | 0.051 | 0.028 | 0.057 |
| away_team_points_last_5 | -0.120 | 0.053 | -0.051 |
| home_team_home_goals_avg | 0.132 | -0.071 | 0.047 |
| home_team_home_win_rate | 0.156 | -0.102 | 0.043 |
| position_difference | -0.147 | 0.104 | -0.035 |
| home_team_home_conceded_avg | -0.131 | 0.090 | -0.033 |
| away_team_wins_last_5 | -0.104 | 0.065 | -0.031 |
| away_position_before_match | 0.071 | -0.030 | 0.031 |
| away_team_goals_scored_last_5 | -0.074 | 0.049 | -0.020 |
| away_team_away_conceded_avg | 0.020 | 0.008 | 0.020 |
| points_difference | 0.205 | -0.193 | 0.016 |
| home_position_before_match | -0.120 | 0.105 | -0.015 |
| away_team_goals_conceded_last_5 | 0.041 | -0.025 | 0.013 |
| away_team_away_win_rate | -0.048 | 0.035 | -0.011 |
| away_team_away_goals_avg | -0.007 | 0.002 | -0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 56 | 20 | 13 | 23 | 35.7% | 23.2% | 41.1% |
| -4..-2 | 68 | 27 | 21 | 20 | 39.7% | 30.9% | 29.4% |
| -1..1 | 83 | 29 | 23 | 31 | 34.9% | 27.7% | 37.3% |
| 2..4 | 66 | 30 | 13 | 23 | 45.5% | 19.7% | 34.8% |
| >4 | 48 | 26 | 11 | 11 | 54.2% | 22.9% | 22.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 69 | 34 | 19 | 16 | 49.3% | 27.5% | 23.2% |
| -5..-2 | 53 | 26 | 12 | 15 | 49.1% | 22.6% | 28.3% |
| -1..1 | 60 | 27 | 14 | 19 | 45.0% | 23.3% | 31.7% |
| 2..5 | 72 | 30 | 13 | 29 | 41.7% | 18.1% | 40.3% |
| >=6 | 67 | 15 | 23 | 29 | 22.4% | 34.3% | 43.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 23 | 7 | 3 | 13 | 30.4% | 13.0% | 56.5% |
| -1..0 | 67 | 34 | 19 | 14 | 50.7% | 28.4% | 20.9% |
| 0 | 119 | 47 | 34 | 38 | 39.5% | 28.6% | 31.9% |
| 1..2 | 96 | 36 | 19 | 41 | 37.5% | 19.8% | 42.7% |
| >2 | 6 | 4 | 1 | 1 | 66.7% | 16.7% | 16.7% |
| unknown | 10 | 4 | 5 | 1 | 40.0% | 50.0% | 10.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.8%** home win (72/213)
- `>= 0.5` tier: **55.6%** home win (60/108)
- Home-win gap (>= split minus < split): **+21.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 213 | 72 | 60 | 81 | 33.8% |
| high | >= 0.5 | 108 | 60 | 21 | 27 | 55.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.189 | -1.037 | -3.333 | 6.523 |
| home_points_before_match | 28.432 | 23.531 | 24.630 | 4.901 |
| away_points_before_match | 25.242 | 24.568 | 27.963 | 3.395 |
| position_difference | -1.212 | 0.556 | 1.463 | 2.675 |
| home_position_before_match | 8.068 | 9.222 | 9.926 | 1.858 |
| away_team_points_last_5 | 5.932 | 6.198 | 7.037 | 1.105 |
| home_team_goals_scored_last_5 | 6.136 | 5.309 | 6.278 | 0.969 |
| away_team_goals_scored_last_5 | 5.811 | 5.827 | 6.769 | 0.958 |
| home_team_points_last_5 | 6.402 | 5.556 | 6.343 | 0.846 |
| away_position_before_match | 9.280 | 8.667 | 8.463 | 0.817 |
| home_team_goals_conceded_last_5 | 5.773 | 6.074 | 6.546 | 0.774 |
| home_rest_days | 8.172 | 7.474 | 7.664 | 0.698 |
| away_rest_days | 8.031 | 7.474 | 7.598 | 0.558 |
| away_team_goals_conceded_last_5 | 6.167 | 5.704 | 5.898 | 0.463 |
| away_team_wins_last_5 | 1.591 | 1.691 | 1.954 | 0.363 |
| home_team_home_goals_avg | 1.535 | 1.212 | 1.314 | 0.323 |
| home_team_wins_last_5 | 1.773 | 1.457 | 1.704 | 0.316 |
| home_team_home_conceded_avg | 0.984 | 1.094 | 1.177 | 0.193 |
| rest_days_difference | 0.141 | 0.000 | 0.065 | 0.141 |
| home_team_home_win_rate | 0.473 | 0.358 | 0.356 | 0.117 |
| away_team_away_goals_avg | 1.076 | 1.116 | 1.107 | 0.040 |
| away_team_away_conceded_avg | 1.343 | 1.343 | 1.365 | 0.023 |
| away_team_away_win_rate | 0.280 | 0.288 | 0.298 | 0.018 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\belgium1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\belgium1\charts\relationships_home_win_pct_by_position.png)

