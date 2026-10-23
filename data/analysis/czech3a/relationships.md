# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:47:28+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 3. CFL - Group A (Czech Republic)
- Scope: league `czech3a`

- Matches analysed: **272** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_rest_days | -0.051 | -0.139 | -0.136 |
| home_position_before_match | -0.260 | 0.090 | -0.131 |
| away_rest_days | -0.045 | -0.132 | -0.127 |
| away_team_goals_scored_last_5 | -0.014 | 0.178 | 0.114 |
| home_team_goals_scored_last_5 | 0.257 | -0.124 | 0.105 |
| home_team_wins_last_5 | 0.213 | -0.088 | 0.097 |
| home_team_points_last_5 | 0.205 | -0.104 | 0.081 |
| away_team_goals_conceded_last_5 | 0.113 | -0.014 | 0.074 |
| away_position_before_match | 0.101 | -0.189 | -0.058 |
| position_difference | -0.253 | 0.196 | -0.051 |
| rest_days_difference | -0.025 | -0.043 | -0.049 |
| home_team_home_goals_avg | 0.214 | -0.161 | 0.047 |
| home_team_home_conceded_avg | 0.107 | -0.064 | 0.036 |
| home_team_home_win_rate | 0.121 | -0.080 | 0.035 |
| away_points_before_match | -0.086 | 0.139 | 0.033 |
| away_team_wins_last_5 | -0.052 | 0.014 | -0.029 |
| home_points_before_match | 0.099 | -0.065 | 0.028 |
| away_team_away_win_rate | -0.173 | 0.155 | -0.020 |
| away_team_points_last_5 | -0.061 | 0.039 | -0.018 |
| away_team_away_goals_avg | -0.149 | 0.136 | -0.016 |
| home_team_goals_conceded_last_5 | -0.035 | 0.016 | -0.015 |
| points_difference | 0.242 | -0.268 | -0.008 |
| away_team_away_conceded_avg | 0.156 | -0.174 | -0.006 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 36 | 10 | 7 | 19 | 27.8% | 19.4% | 52.8% |
| -4..-2 | 59 | 26 | 8 | 25 | 44.1% | 13.6% | 42.4% |
| -1..1 | 84 | 47 | 15 | 22 | 56.0% | 17.9% | 26.2% |
| 2..4 | 52 | 23 | 17 | 12 | 44.2% | 32.7% | 23.1% |
| >4 | 41 | 18 | 10 | 13 | 43.9% | 24.4% | 31.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 64 | 34 | 10 | 20 | 53.1% | 15.6% | 31.2% |
| -5..-2 | 61 | 30 | 18 | 13 | 49.2% | 29.5% | 21.3% |
| -1..1 | 32 | 19 | 8 | 5 | 59.4% | 25.0% | 15.6% |
| 2..5 | 49 | 25 | 7 | 17 | 51.0% | 14.3% | 34.7% |
| >=6 | 66 | 16 | 14 | 36 | 24.2% | 21.2% | 54.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 18 | 4 | 7 | 7 | 22.2% | 38.9% | 38.9% |
| -1..0 | 54 | 27 | 12 | 15 | 50.0% | 22.2% | 27.8% |
| 0 | 121 | 52 | 22 | 47 | 43.0% | 18.2% | 38.8% |
| 1..2 | 50 | 28 | 11 | 11 | 56.0% | 22.0% | 22.0% |
| >2 | 20 | 9 | 3 | 8 | 45.0% | 15.0% | 40.0% |
| unknown | 9 | 4 | 2 | 3 | 44.4% | 22.2% | 33.3% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **41.3%** home win (57/138)
- `>= 0.5` tier: **50.0%** home win (67/134)
- Home-win gap (>= split minus < split): **+8.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 138 | 57 | 31 | 50 | 41.3% |
| high | >= 0.5 | 134 | 67 | 26 | 41 | 50.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.177 | 0.491 | -4.692 | 6.870 |
| home_points_before_match | 22.395 | 23.667 | 19.055 | 4.612 |
| away_points_before_match | 20.218 | 23.175 | 23.747 | 3.530 |
| position_difference | -1.476 | 0.316 | 1.945 | 3.421 |
| home_rest_days | 9.892 | 11.436 | 8.876 | 2.560 |
| away_position_before_match | 9.895 | 9.211 | 8.055 | 1.840 |
| home_team_goals_scored_last_5 | 7.863 | 7.684 | 6.033 | 1.830 |
| home_position_before_match | 8.419 | 9.526 | 10.000 | 1.581 |
| away_rest_days | 9.583 | 10.273 | 8.784 | 1.489 |
| home_team_points_last_5 | 6.798 | 6.825 | 5.484 | 1.341 |
| rest_days_difference | 0.308 | 1.164 | 0.114 | 1.050 |
| away_team_goals_conceded_last_5 | 7.411 | 6.561 | 6.934 | 0.850 |
| away_team_goals_scored_last_5 | 7.065 | 6.772 | 7.560 | 0.789 |
| home_team_goals_conceded_last_5 | 7.290 | 6.895 | 7.451 | 0.556 |
| home_team_wins_last_5 | 1.984 | 1.982 | 1.484 | 0.500 |
| away_team_away_conceded_avg | 1.810 | 1.620 | 1.369 | 0.441 |
| home_team_home_goals_avg | 1.786 | 1.690 | 1.348 | 0.438 |
| away_team_away_goals_avg | 1.286 | 1.352 | 1.628 | 0.341 |
| away_team_points_last_5 | 6.371 | 6.088 | 6.396 | 0.308 |
| away_team_wins_last_5 | 1.839 | 1.632 | 1.813 | 0.207 |
| home_team_home_conceded_avg | 1.494 | 1.373 | 1.335 | 0.159 |
| away_team_away_win_rate | 0.267 | 0.312 | 0.414 | 0.147 |
| home_team_home_win_rate | 0.459 | 0.464 | 0.376 | 0.088 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\czech3a\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\czech3a\charts\relationships_home_win_pct_by_position.png)

