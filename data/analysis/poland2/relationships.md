# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:03:17+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Division 1 (Poland)
- Scope: league `poland2`

- Matches analysed: **328** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_goals_avg | 0.111 | -0.014 | 0.073 |
| home_points_before_match | -0.031 | -0.063 | -0.070 |
| home_rest_days | 0.059 | 0.013 | 0.054 |
| points_difference | 0.116 | -0.190 | -0.052 |
| away_rest_days | 0.046 | 0.021 | 0.051 |
| away_team_away_conceded_avg | -0.006 | -0.062 | -0.050 |
| away_position_before_match | 0.062 | -0.127 | -0.046 |
| home_team_home_conceded_avg | -0.136 | 0.188 | 0.035 |
| away_points_before_match | -0.110 | 0.066 | -0.035 |
| away_team_goals_scored_last_5 | -0.039 | 0.087 | 0.034 |
| away_team_goals_conceded_last_5 | 0.002 | -0.048 | -0.034 |
| home_position_before_match | -0.172 | 0.137 | -0.029 |
| away_team_points_last_5 | -0.100 | 0.065 | -0.028 |
| away_team_wins_last_5 | -0.104 | 0.069 | -0.028 |
| home_team_home_win_rate | 0.193 | -0.163 | 0.026 |
| home_team_goals_conceded_last_5 | -0.077 | 0.115 | 0.025 |
| home_team_points_last_5 | 0.075 | -0.108 | -0.022 |
| home_team_goals_scored_last_5 | 0.081 | -0.056 | 0.020 |
| rest_days_difference | 0.063 | -0.041 | 0.017 |
| position_difference | -0.168 | 0.190 | 0.012 |
| away_team_away_win_rate | -0.046 | 0.039 | -0.006 |
| away_team_away_goals_avg | -0.073 | 0.068 | -0.005 |
| home_team_wins_last_5 | 0.085 | -0.085 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 55 | 16 | 15 | 24 | 29.1% | 27.3% | 43.6% |
| -4..-2 | 70 | 33 | 14 | 23 | 47.1% | 20.0% | 32.9% |
| -1..1 | 83 | 29 | 28 | 26 | 34.9% | 33.7% | 31.3% |
| 2..4 | 66 | 32 | 15 | 19 | 48.5% | 22.7% | 28.8% |
| >4 | 54 | 26 | 17 | 11 | 48.1% | 31.5% | 20.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 73 | 37 | 22 | 14 | 50.7% | 30.1% | 19.2% |
| -5..-2 | 68 | 31 | 16 | 21 | 45.6% | 23.5% | 30.9% |
| -1..1 | 38 | 17 | 10 | 11 | 44.7% | 26.3% | 28.9% |
| 2..5 | 73 | 24 | 25 | 24 | 32.9% | 34.2% | 32.9% |
| >=6 | 76 | 27 | 16 | 33 | 35.5% | 21.1% | 43.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 49 | 22 | 11 | 16 | 44.9% | 22.4% | 32.7% |
| -1..0 | 72 | 21 | 23 | 28 | 29.2% | 31.9% | 38.9% |
| 0 | 74 | 35 | 22 | 17 | 47.3% | 29.7% | 23.0% |
| 1..2 | 110 | 50 | 26 | 34 | 45.5% | 23.6% | 30.9% |
| >2 | 13 | 4 | 3 | 6 | 30.8% | 23.1% | 46.2% |
| unknown | 10 | 4 | 4 | 2 | 40.0% | 40.0% | 20.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.6%** home win (73/189)
- `>= 0.5` tier: **45.3%** home win (63/139)
- Home-win gap (>= split minus < split): **+6.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 189 | 73 | 43 | 73 | 38.6% |
| high | >= 0.5 | 139 | 63 | 46 | 30 | 45.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.051 | 0.742 | -3.010 | 5.061 |
| position_difference | -1.301 | -0.607 | 2.155 | 3.457 |
| away_points_before_match | 22.022 | 22.056 | 24.903 | 2.881 |
| home_position_before_match | 9.331 | 9.697 | 11.796 | 2.465 |
| home_points_before_match | 24.074 | 22.798 | 21.893 | 2.180 |
| home_rest_days | 9.212 | 9.729 | 8.594 | 1.135 |
| home_team_goals_scored_last_5 | 6.963 | 7.303 | 6.184 | 1.119 |
| away_position_before_match | 10.632 | 10.303 | 9.641 | 0.992 |
| home_team_goals_conceded_last_5 | 6.412 | 6.899 | 7.301 | 0.889 |
| home_team_points_last_5 | 6.522 | 6.404 | 5.670 | 0.852 |
| away_rest_days | 9.205 | 9.624 | 8.772 | 0.851 |
| away_team_points_last_5 | 5.985 | 6.101 | 6.592 | 0.607 |
| away_team_goals_scored_last_5 | 6.728 | 6.787 | 7.233 | 0.505 |
| home_team_home_conceded_avg | 1.136 | 1.266 | 1.573 | 0.437 |
| away_team_goals_conceded_last_5 | 6.757 | 7.090 | 6.689 | 0.401 |
| home_team_wins_last_5 | 1.728 | 1.764 | 1.456 | 0.308 |
| rest_days_difference | 0.008 | 0.106 | -0.178 | 0.284 |
| home_team_home_goals_avg | 1.619 | 1.771 | 1.507 | 0.264 |
| away_team_wins_last_5 | 1.551 | 1.618 | 1.786 | 0.235 |
| home_team_home_win_rate | 0.438 | 0.465 | 0.323 | 0.142 |
| away_team_away_goals_avg | 1.252 | 1.362 | 1.392 | 0.140 |
| away_team_away_conceded_avg | 1.625 | 1.557 | 1.576 | 0.067 |
| away_team_away_win_rate | 0.274 | 0.259 | 0.286 | 0.027 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\poland2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\poland2\charts\relationships_home_win_pct_by_position.png)

