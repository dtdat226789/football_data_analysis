# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:49:32+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Challenge League (Switzerland)
- Scope: league `swiss2`

- Matches analysed: **231** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_points_before_match | 0.117 | 0.065 | 0.134 |
| home_team_home_conceded_avg | -0.148 | -0.020 | -0.127 |
| away_points_before_match | -0.053 | 0.239 | 0.125 |
| home_team_wins_last_5 | 0.144 | -0.018 | 0.097 |
| home_team_home_win_rate | 0.154 | -0.036 | 0.092 |
| home_position_before_match | -0.218 | 0.109 | -0.090 |
| away_rest_days | -0.086 | -0.027 | -0.086 |
| away_team_goals_conceded_last_5 | 0.096 | 0.007 | 0.077 |
| home_rest_days | -0.082 | -0.016 | -0.075 |
| home_team_goals_conceded_last_5 | -0.111 | 0.018 | -0.072 |
| home_team_points_last_5 | 0.113 | -0.024 | 0.069 |
| home_team_goals_scored_last_5 | 0.093 | -0.024 | 0.054 |
| away_team_away_goals_avg | -0.023 | 0.094 | 0.048 |
| away_team_wins_last_5 | -0.140 | 0.085 | -0.048 |
| away_position_before_match | 0.149 | -0.225 | -0.043 |
| position_difference | -0.269 | 0.244 | -0.035 |
| away_team_goals_scored_last_5 | -0.153 | 0.124 | -0.030 |
| away_team_away_conceded_avg | 0.031 | -0.071 | -0.026 |
| away_team_away_win_rate | -0.038 | 0.008 | -0.023 |
| rest_days_difference | -0.003 | 0.029 | 0.018 |
| points_difference | 0.219 | -0.223 | 0.011 |
| home_team_home_goals_avg | 0.112 | -0.109 | 0.009 |
| away_team_points_last_5 | -0.153 | 0.165 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 37 | 11 | 6 | 20 | 29.7% | 16.2% | 54.1% |
| -4..-2 | 45 | 16 | 15 | 14 | 35.6% | 33.3% | 31.1% |
| -1..1 | 71 | 26 | 14 | 31 | 36.6% | 19.7% | 43.7% |
| 2..4 | 43 | 26 | 11 | 6 | 60.5% | 25.6% | 14.0% |
| >4 | 35 | 24 | 6 | 5 | 68.6% | 17.1% | 14.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 17 | 15 | 2 | 0 | 88.2% | 11.8% | 0.0% |
| -5..-2 | 62 | 39 | 12 | 11 | 62.9% | 19.4% | 17.7% |
| -1..1 | 61 | 26 | 15 | 20 | 42.6% | 24.6% | 32.8% |
| 2..5 | 68 | 19 | 15 | 34 | 27.9% | 22.1% | 50.0% |
| >=6 | 23 | 4 | 8 | 11 | 17.4% | 34.8% | 47.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 24 | 11 | 6 | 7 | 45.8% | 25.0% | 29.2% |
| -1..0 | 40 | 18 | 7 | 15 | 45.0% | 17.5% | 37.5% |
| 0 | 95 | 41 | 26 | 28 | 43.2% | 27.4% | 29.5% |
| 1..2 | 52 | 25 | 7 | 20 | 48.1% | 13.5% | 38.5% |
| >2 | 8 | 3 | 2 | 3 | 37.5% | 25.0% | 37.5% |
| unknown | 12 | 5 | 4 | 3 | 41.7% | 33.3% | 25.0% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **43.9%** home win (25/57)
- `>= 0.5` tier: **44.8%** home win (78/174)
- Home-win gap (>= split minus < split): **+0.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 57 | 25 | 15 | 17 | 43.9% |
| high | >= 0.5 | 174 | 78 | 37 | 59 | 44.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.466 | -0.519 | -6.750 | 11.216 |
| away_points_before_match | 17.534 | 19.173 | 26.513 | 8.979 |
| position_difference | -1.583 | 0.923 | 1.908 | 3.490 |
| home_points_before_match | 22.000 | 18.654 | 19.763 | 3.346 |
| away_team_points_last_5 | 5.379 | 5.577 | 7.421 | 2.042 |
| away_position_before_match | 6.427 | 5.577 | 4.408 | 2.019 |
| away_team_goals_scored_last_5 | 5.864 | 5.962 | 7.776 | 1.912 |
| home_position_before_match | 4.845 | 6.500 | 6.316 | 1.655 |
| home_team_goals_scored_last_5 | 6.806 | 5.673 | 6.053 | 1.133 |
| home_team_points_last_5 | 6.427 | 5.308 | 5.553 | 1.119 |
| home_team_goals_conceded_last_5 | 6.000 | 6.308 | 6.961 | 0.961 |
| home_rest_days | 8.163 | 7.875 | 8.757 | 0.882 |
| away_rest_days | 8.153 | 7.755 | 8.446 | 0.691 |
| away_team_goals_conceded_last_5 | 6.631 | 5.942 | 6.395 | 0.689 |
| away_team_wins_last_5 | 2.524 | 2.462 | 3.079 | 0.617 |
| home_team_wins_last_5 | 2.816 | 2.385 | 2.474 | 0.431 |
| away_team_away_goals_avg | 1.119 | 1.059 | 1.452 | 0.393 |
| home_team_home_goals_avg | 1.604 | 1.263 | 1.372 | 0.340 |
| rest_days_difference | 0.010 | 0.146 | 0.342 | 0.332 |
| home_team_home_conceded_avg | 1.079 | 1.277 | 1.279 | 0.200 |
| home_team_home_win_rate | 0.690 | 0.571 | 0.620 | 0.119 |
| away_team_away_win_rate | 0.482 | 0.451 | 0.559 | 0.108 |
| away_team_away_conceded_avg | 1.482 | 1.397 | 1.450 | 0.085 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\swiss2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\swiss2\charts\relationships_home_win_pct_by_position.png)

