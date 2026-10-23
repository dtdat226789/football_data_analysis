# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:54:16+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: NB I. (Hungary)
- Scope: league `hungary1`

- Matches analysed: **198** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_win_rate | -0.205 | -0.029 | -0.181 |
| away_team_goals_scored_last_5 | -0.124 | -0.095 | -0.166 |
| away_team_points_last_5 | -0.149 | -0.046 | -0.150 |
| away_team_wins_last_5 | -0.141 | -0.053 | -0.148 |
| away_team_away_goals_avg | -0.240 | 0.056 | -0.145 |
| away_points_before_match | -0.116 | -0.036 | -0.117 |
| home_team_points_last_5 | 0.046 | -0.199 | -0.111 |
| home_team_goals_conceded_last_5 | -0.173 | 0.043 | -0.103 |
| home_team_wins_last_5 | 0.042 | -0.180 | -0.100 |
| away_position_before_match | 0.197 | -0.078 | 0.096 |
| home_team_goals_scored_last_5 | -0.009 | -0.119 | -0.094 |
| home_team_home_goals_avg | 0.061 | 0.049 | 0.083 |
| position_difference | -0.238 | 0.147 | -0.077 |
| home_points_before_match | 0.075 | -0.178 | -0.073 |
| points_difference | 0.275 | -0.201 | 0.065 |
| home_team_home_conceded_avg | -0.020 | -0.060 | -0.060 |
| home_team_home_win_rate | -0.055 | -0.016 | -0.054 |
| rest_days_difference | -0.035 | -0.022 | -0.044 |
| away_team_goals_conceded_last_5 | 0.075 | -0.117 | -0.028 |
| home_rest_days | -0.056 | 0.021 | -0.028 |
| home_position_before_match | -0.148 | 0.135 | -0.016 |
| away_rest_days | -0.046 | 0.027 | -0.016 |
| away_team_away_conceded_avg | 0.100 | -0.102 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 27 | 6 | 10 | 11 | 22.2% | 37.0% | 40.7% |
| -4..-2 | 44 | 12 | 12 | 20 | 27.3% | 27.3% | 45.5% |
| -1..1 | 53 | 22 | 14 | 17 | 41.5% | 26.4% | 32.1% |
| 2..4 | 51 | 26 | 9 | 16 | 51.0% | 17.6% | 31.4% |
| >4 | 23 | 12 | 4 | 7 | 52.2% | 17.4% | 30.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 27 | 16 | 6 | 5 | 59.3% | 22.2% | 18.5% |
| -5..-2 | 55 | 26 | 8 | 21 | 47.3% | 14.5% | 38.2% |
| -1..1 | 33 | 14 | 10 | 9 | 42.4% | 30.3% | 27.3% |
| 2..5 | 54 | 15 | 20 | 19 | 27.8% | 37.0% | 35.2% |
| >=6 | 29 | 7 | 5 | 17 | 24.1% | 17.2% | 58.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 12 | 5 | 3 | 4 | 41.7% | 25.0% | 33.3% |
| -1..0 | 45 | 19 | 14 | 12 | 42.2% | 31.1% | 26.7% |
| 0 | 67 | 26 | 11 | 30 | 38.8% | 16.4% | 44.8% |
| 1..2 | 63 | 23 | 16 | 24 | 36.5% | 25.4% | 38.1% |
| >2 | 5 | 3 | 1 | 1 | 60.0% | 20.0% | 20.0% |
| unknown | 6 | 2 | 4 | 0 | 33.3% | 66.7% | 0.0% |
- *6 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **41.1%** home win (60/146)
- `>= 0.5` tier: **34.6%** home win (18/52)
- Home-win gap (>= split minus < split): **-6.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 146 | 60 | 36 | 50 | 41.1% |
| high | >= 0.5 | 52 | 18 | 13 | 21 | 34.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 25.551 | 19.837 | 19.014 | 6.537 |
| points_difference | 3.154 | -1.306 | -3.338 | 6.492 |
| position_difference | -1.385 | 0.551 | 1.296 | 2.680 |
| home_team_points_last_5 | 7.064 | 5.408 | 6.028 | 1.656 |
| away_rest_days | 8.474 | 9.067 | 9.930 | 1.456 |
| home_position_before_match | 6.026 | 6.918 | 7.437 | 1.411 |
| home_rest_days | 8.539 | 9.089 | 9.930 | 1.390 |
| away_position_before_match | 7.410 | 6.367 | 6.141 | 1.269 |
| away_points_before_match | 22.397 | 21.143 | 22.352 | 1.255 |
| home_team_goals_conceded_last_5 | 6.218 | 6.816 | 7.352 | 1.134 |
| home_team_goals_scored_last_5 | 7.103 | 6.286 | 6.732 | 0.817 |
| away_team_goals_conceded_last_5 | 7.064 | 6.367 | 6.676 | 0.697 |
| away_team_points_last_5 | 5.885 | 6.367 | 6.493 | 0.608 |
| home_team_wins_last_5 | 1.936 | 1.469 | 1.634 | 0.467 |
| away_team_away_goals_avg | 1.287 | 1.449 | 1.714 | 0.427 |
| away_team_goals_scored_last_5 | 6.526 | 6.857 | 6.930 | 0.404 |
| away_team_wins_last_5 | 1.577 | 1.735 | 1.817 | 0.240 |
| home_team_home_goals_avg | 1.498 | 1.398 | 1.588 | 0.191 |
| away_team_away_conceded_avg | 1.597 | 1.468 | 1.461 | 0.136 |
| home_team_home_win_rate | 0.326 | 0.291 | 0.369 | 0.077 |
| away_team_away_win_rate | 0.300 | 0.343 | 0.377 | 0.077 |
| rest_days_difference | 0.066 | 0.022 | 0.000 | 0.066 |
| home_team_home_conceded_avg | 1.478 | 1.420 | 1.471 | 0.058 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\hungary1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\hungary1\charts\relationships_home_win_pct_by_position.png)

