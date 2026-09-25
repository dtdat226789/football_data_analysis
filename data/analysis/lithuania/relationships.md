# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:03:29+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: TOPLYGA (Lithuania)
- Scope: league `lithuania`

- Matches analysed: **324** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_win_rate | -0.200 | -0.041 | -0.193 |
| away_team_away_goals_avg | -0.162 | -0.004 | -0.135 |
| position_difference | -0.325 | 0.252 | -0.085 |
| away_position_before_match | 0.228 | -0.142 | 0.085 |
| points_difference | 0.317 | -0.246 | 0.083 |
| home_points_before_match | 0.165 | -0.094 | 0.068 |
| away_team_away_conceded_avg | 0.153 | -0.089 | 0.061 |
| home_team_goals_conceded_last_5 | -0.228 | 0.188 | -0.051 |
| home_position_before_match | -0.240 | 0.221 | -0.039 |
| away_team_goals_scored_last_5 | -0.134 | 0.107 | -0.033 |
| home_team_goals_scored_last_5 | 0.113 | -0.170 | -0.030 |
| away_team_goals_conceded_last_5 | 0.112 | -0.168 | -0.028 |
| away_team_points_last_5 | -0.139 | 0.121 | -0.026 |
| home_team_home_goals_avg | 0.135 | -0.129 | 0.018 |
| home_team_wins_last_5 | 0.185 | -0.191 | 0.015 |
| home_rest_days | 0.048 | -0.074 | -0.013 |
| away_rest_days | 0.008 | -0.025 | -0.012 |
| home_team_home_conceded_avg | -0.140 | 0.170 | 0.007 |
| home_team_home_win_rate | 0.155 | -0.186 | -0.006 |
| away_points_before_match | -0.079 | 0.095 | 0.004 |
| rest_days_difference | 0.050 | -0.063 | -0.004 |
| away_team_wins_last_5 | -0.113 | 0.125 | -0.003 |
| home_team_points_last_5 | 0.179 | -0.204 | 0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 59 | 14 | 14 | 31 | 23.7% | 23.7% | 52.5% |
| -4..-2 | 74 | 26 | 20 | 28 | 35.1% | 27.0% | 37.8% |
| -1..1 | 99 | 37 | 31 | 31 | 37.4% | 31.3% | 31.3% |
| 2..4 | 47 | 21 | 12 | 14 | 44.7% | 25.5% | 29.8% |
| >4 | 45 | 32 | 7 | 6 | 71.1% | 15.6% | 13.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 27 | 19 | 6 | 2 | 70.4% | 22.2% | 7.4% |
| -5..-2 | 96 | 47 | 27 | 22 | 49.0% | 28.1% | 22.9% |
| -1..1 | 78 | 30 | 22 | 26 | 38.5% | 28.2% | 33.3% |
| 2..5 | 94 | 29 | 20 | 45 | 30.9% | 21.3% | 47.9% |
| >=6 | 29 | 5 | 9 | 15 | 17.2% | 31.0% | 51.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 36 | 15 | 11 | 10 | 41.7% | 30.6% | 27.8% |
| -1..0 | 66 | 24 | 19 | 23 | 36.4% | 28.8% | 34.8% |
| 0 | 97 | 47 | 21 | 29 | 48.5% | 21.6% | 29.9% |
| 1..2 | 89 | 34 | 22 | 33 | 38.2% | 24.7% | 37.1% |
| >2 | 26 | 8 | 9 | 9 | 30.8% | 34.6% | 34.6% |
| unknown | 10 | 2 | 2 | 6 | 20.0% | 20.0% | 60.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **27.8%** home win (25/90)
- `>= 0.5` tier: **44.9%** home win (105/234)
- Home-win gap (>= split minus < split): **+17.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 90 | 25 | 25 | 40 | 27.8% |
| high | >= 0.5 | 234 | 105 | 59 | 70 | 44.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.162 | -0.821 | -5.264 | 9.425 |
| home_points_before_match | 24.669 | 22.202 | 19.455 | 5.215 |
| away_points_before_match | 20.508 | 23.024 | 24.718 | 4.210 |
| position_difference | -1.315 | 0.000 | 1.645 | 2.961 |
| home_team_points_last_5 | 6.785 | 5.833 | 5.236 | 1.548 |
| home_team_goals_conceded_last_5 | 5.315 | 6.214 | 6.845 | 1.530 |
| away_position_before_match | 6.200 | 5.500 | 4.700 | 1.500 |
| home_position_before_match | 4.885 | 5.500 | 6.345 | 1.461 |
| away_team_points_last_5 | 5.938 | 6.679 | 7.173 | 1.234 |
| away_team_goals_conceded_last_5 | 6.385 | 5.548 | 5.155 | 1.230 |
| away_team_goals_scored_last_5 | 5.615 | 6.488 | 6.700 | 1.085 |
| home_team_goals_scored_last_5 | 6.238 | 5.738 | 5.264 | 0.975 |
| home_team_wins_last_5 | 3.077 | 2.690 | 2.455 | 0.622 |
| home_rest_days | 7.289 | 7.622 | 7.038 | 0.583 |
| away_rest_days | 6.867 | 7.427 | 7.010 | 0.560 |
| away_team_wins_last_5 | 2.785 | 2.964 | 3.209 | 0.424 |
| rest_days_difference | 0.422 | 0.195 | 0.029 | 0.393 |
| away_team_away_conceded_avg | 1.446 | 1.197 | 1.255 | 0.249 |
| home_team_home_goals_avg | 1.402 | 1.333 | 1.180 | 0.223 |
| away_team_away_goals_avg | 1.052 | 1.275 | 1.184 | 0.223 |
| home_team_home_conceded_avg | 1.029 | 1.139 | 1.251 | 0.222 |
| home_team_home_win_rate | 0.660 | 0.628 | 0.523 | 0.137 |
| away_team_away_win_rate | 0.536 | 0.620 | 0.577 | 0.084 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\lithuania\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\lithuania\charts\relationships_home_win_pct_by_position.png)

