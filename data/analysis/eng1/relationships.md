# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:57:45+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: League One (England)
- Scope: league `eng1`

- Matches analysed: **640** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.165 | 0.050 | -0.094 |
| away_team_away_win_rate | 0.015 | 0.089 | 0.071 |
| home_team_goals_scored_last_5 | 0.111 | -0.023 | 0.070 |
| home_team_home_conceded_avg | 0.057 | 0.015 | 0.054 |
| home_team_home_goals_avg | 0.093 | -0.028 | 0.053 |
| home_points_before_match | 0.054 | 0.011 | 0.049 |
| home_team_goals_conceded_last_5 | -0.095 | 0.038 | -0.048 |
| position_difference | -0.128 | 0.084 | -0.042 |
| away_team_away_goals_avg | 0.017 | 0.037 | 0.038 |
| away_position_before_match | 0.011 | -0.065 | -0.035 |
| points_difference | 0.173 | -0.150 | 0.033 |
| away_rest_days | 0.021 | 0.022 | 0.031 |
| away_points_before_match | -0.040 | 0.092 | 0.031 |
| home_team_wins_last_5 | 0.071 | -0.036 | 0.031 |
| rest_days_difference | -0.009 | -0.036 | -0.031 |
| home_team_points_last_5 | 0.088 | -0.060 | 0.027 |
| home_team_home_win_rate | -0.005 | -0.025 | -0.021 |
| away_team_away_conceded_avg | 0.003 | -0.033 | -0.020 |
| away_team_goals_scored_last_5 | -0.062 | 0.047 | -0.017 |
| away_team_points_last_5 | -0.076 | 0.063 | -0.016 |
| home_rest_days | 0.014 | -0.007 | 0.006 |
| away_team_wins_last_5 | -0.068 | 0.071 | -0.004 |
| away_team_goals_conceded_last_5 | -0.004 | 0.002 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 106 | 36 | 28 | 42 | 34.0% | 26.4% | 39.6% |
| -4..-2 | 140 | 55 | 38 | 47 | 39.3% | 27.1% | 33.6% |
| -1..1 | 193 | 93 | 49 | 51 | 48.2% | 25.4% | 26.4% |
| 2..4 | 120 | 54 | 37 | 29 | 45.0% | 30.8% | 24.2% |
| >4 | 81 | 48 | 14 | 19 | 59.3% | 17.3% | 23.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 176 | 100 | 37 | 39 | 56.8% | 21.0% | 22.2% |
| -5..-2 | 73 | 27 | 25 | 21 | 37.0% | 34.2% | 28.8% |
| -1..1 | 84 | 39 | 22 | 23 | 46.4% | 26.2% | 27.4% |
| 2..5 | 109 | 43 | 32 | 34 | 39.4% | 29.4% | 31.2% |
| >=6 | 198 | 77 | 50 | 71 | 38.9% | 25.3% | 35.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 66 | 27 | 21 | 18 | 40.9% | 31.8% | 27.3% |
| -1..0 | 18 | 6 | 6 | 6 | 33.3% | 33.3% | 33.3% |
| 0 | 450 | 198 | 116 | 136 | 44.0% | 25.8% | 30.2% |
| 1..2 | 29 | 16 | 8 | 5 | 55.2% | 27.6% | 17.2% |
| >2 | 53 | 25 | 11 | 17 | 47.2% | 20.8% | 32.1% |
| unknown | 24 | 14 | 4 | 6 | 58.3% | 16.7% | 25.0% |
- *24 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **45.3%** home win (48/106)
- `>= 0.5` tier: **44.6%** home win (238/534)
- Home-win gap (>= split minus < split): **-0.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 106 | 48 | 26 | 32 | 45.3% |
| high | >= 0.5 | 534 | 238 | 140 | 156 | 44.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.336 | -1.922 | -3.410 | 5.745 |
| position_difference | -0.962 | 1.084 | 2.527 | 3.488 |
| away_points_before_match | 26.427 | 29.681 | 29.410 | 3.254 |
| home_points_before_match | 28.762 | 27.759 | 26.000 | 2.762 |
| home_position_before_match | 11.580 | 12.795 | 14.160 | 2.579 |
| home_team_points_last_5 | 6.287 | 6.060 | 5.261 | 1.026 |
| away_position_before_match | 12.542 | 11.711 | 11.633 | 0.909 |
| home_team_goals_scored_last_5 | 6.010 | 5.777 | 5.261 | 0.750 |
| away_team_points_last_5 | 5.906 | 6.639 | 6.468 | 0.733 |
| away_team_goals_scored_last_5 | 5.759 | 6.343 | 6.000 | 0.585 |
| home_team_goals_conceded_last_5 | 5.699 | 6.139 | 6.245 | 0.545 |
| home_rest_days | 6.129 | 5.704 | 6.247 | 0.544 |
| rest_days_difference | 0.015 | -0.216 | 0.176 | 0.392 |
| home_team_wins_last_5 | 2.853 | 2.771 | 2.569 | 0.284 |
| away_team_goals_conceded_last_5 | 5.829 | 5.711 | 5.553 | 0.275 |
| away_team_wins_last_5 | 2.703 | 2.976 | 2.915 | 0.273 |
| away_rest_days | 6.114 | 5.920 | 6.071 | 0.194 |
| home_team_home_goals_avg | 1.412 | 1.419 | 1.270 | 0.149 |
| away_team_away_goals_avg | 1.003 | 1.033 | 0.978 | 0.055 |
| away_team_away_conceded_avg | 1.395 | 1.358 | 1.347 | 0.048 |
| home_team_home_win_rate | 0.660 | 0.677 | 0.637 | 0.041 |
| home_team_home_conceded_avg | 1.016 | 0.978 | 1.003 | 0.038 |
| away_team_away_win_rate | 0.467 | 0.505 | 0.490 | 0.037 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\eng1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\eng1\charts\relationships_home_win_pct_by_position.png)

