# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:01:50+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Botola Pro (Morocco)
- Scope: league `morocco`

- Matches analysed: **488** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.190 | -0.048 | 0.098 |
| away_team_goals_conceded_last_5 | 0.190 | -0.055 | 0.092 |
| home_team_wins_last_5 | 0.088 | -0.180 | -0.075 |
| away_position_before_match | 0.209 | -0.111 | 0.063 |
| home_team_goals_scored_last_5 | 0.074 | -0.146 | -0.059 |
| away_points_before_match | -0.059 | 0.132 | 0.058 |
| home_position_before_match | -0.119 | 0.185 | 0.057 |
| away_team_wins_last_5 | -0.120 | 0.039 | -0.055 |
| home_team_points_last_5 | 0.127 | -0.186 | -0.052 |
| away_team_away_win_rate | -0.140 | 0.066 | -0.048 |
| points_difference | 0.213 | -0.260 | -0.047 |
| away_team_away_goals_avg | -0.110 | 0.042 | -0.046 |
| away_team_points_last_5 | -0.123 | 0.058 | -0.043 |
| away_rest_days | -0.019 | 0.075 | 0.042 |
| away_team_goals_scored_last_5 | -0.107 | 0.049 | -0.038 |
| home_team_home_conceded_avg | -0.098 | 0.135 | 0.033 |
| home_rest_days | 0.053 | -0.007 | 0.032 |
| home_team_home_goals_avg | 0.108 | -0.133 | -0.025 |
| home_team_home_win_rate | 0.120 | -0.141 | -0.023 |
| home_points_before_match | 0.113 | -0.078 | 0.021 |
| rest_days_difference | 0.069 | -0.091 | -0.019 |
| position_difference | -0.236 | 0.212 | -0.006 |
| home_team_goals_conceded_last_5 | -0.112 | 0.110 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 76 | 16 | 27 | 33 | 21.1% | 35.5% | 43.4% |
| -4..-2 | 93 | 33 | 30 | 30 | 35.5% | 32.3% | 32.3% |
| -1..1 | 150 | 58 | 51 | 41 | 38.7% | 34.0% | 27.3% |
| 2..4 | 105 | 50 | 31 | 24 | 47.6% | 29.5% | 22.9% |
| >4 | 64 | 41 | 14 | 9 | 64.1% | 21.9% | 14.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 98 | 58 | 24 | 16 | 59.2% | 24.5% | 16.3% |
| -5..-2 | 105 | 49 | 33 | 23 | 46.7% | 31.4% | 21.9% |
| -1..1 | 79 | 27 | 28 | 24 | 34.2% | 35.4% | 30.4% |
| 2..5 | 101 | 40 | 30 | 31 | 39.6% | 29.7% | 30.7% |
| >=6 | 105 | 24 | 38 | 43 | 22.9% | 36.2% | 41.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 71 | 28 | 23 | 20 | 39.4% | 32.4% | 28.2% |
| -1..0 | 69 | 25 | 17 | 27 | 36.2% | 24.6% | 39.1% |
| 0 | 171 | 72 | 53 | 46 | 42.1% | 31.0% | 26.9% |
| 1..2 | 106 | 45 | 35 | 26 | 42.5% | 33.0% | 24.5% |
| >2 | 54 | 23 | 18 | 13 | 42.6% | 33.3% | 24.1% |
| unknown | 17 | 5 | 7 | 5 | 29.4% | 41.2% | 29.4% |
- *17 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **34.6%** home win (100/289)
- `>= 0.5` tier: **49.2%** home win (98/199)
- Home-win gap (>= split minus < split): **+14.6 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 289 | 100 | 95 | 94 | 34.6% |
| high | >= 0.5 | 199 | 98 | 58 | 43 | 49.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.323 | -0.150 | -5.219 | 8.542 |
| home_points_before_match | 21.475 | 18.824 | 16.314 | 5.161 |
| position_difference | -1.965 | 0.582 | 2.489 | 4.454 |
| away_points_before_match | 18.152 | 18.974 | 21.533 | 3.381 |
| home_position_before_match | 8.136 | 8.974 | 10.482 | 2.345 |
| away_position_before_match | 10.101 | 8.392 | 7.993 | 2.108 |
| away_rest_days | 8.642 | 9.767 | 10.727 | 2.085 |
| rest_days_difference | 0.487 | -0.363 | -1.394 | 1.881 |
| home_team_points_last_5 | 6.793 | 5.758 | 4.964 | 1.829 |
| away_team_goals_conceded_last_5 | 5.687 | 4.536 | 4.474 | 1.212 |
| home_team_goals_scored_last_5 | 5.303 | 4.810 | 4.219 | 1.084 |
| home_team_goals_conceded_last_5 | 4.571 | 4.693 | 5.642 | 1.072 |
| away_team_points_last_5 | 5.576 | 6.327 | 6.453 | 0.877 |
| home_team_wins_last_5 | 1.717 | 1.464 | 1.219 | 0.498 |
| away_team_goals_scored_last_5 | 4.838 | 5.033 | 5.328 | 0.490 |
| home_rest_days | 9.130 | 9.404 | 9.333 | 0.275 |
| away_team_away_conceded_avg | 1.208 | 1.015 | 0.964 | 0.244 |
| home_team_home_goals_avg | 1.166 | 1.118 | 0.924 | 0.242 |
| away_team_wins_last_5 | 1.409 | 1.641 | 1.650 | 0.241 |
| home_team_home_conceded_avg | 0.876 | 0.866 | 1.089 | 0.222 |
| away_team_away_goals_avg | 0.879 | 0.940 | 0.991 | 0.112 |
| home_team_home_win_rate | 0.394 | 0.369 | 0.291 | 0.103 |
| away_team_away_win_rate | 0.231 | 0.268 | 0.292 | 0.060 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\morocco\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\morocco\charts\relationships_home_win_pct_by_position.png)

