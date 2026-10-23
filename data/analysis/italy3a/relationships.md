# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:58:15+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie C - Group A (Italy)
- Scope: league `italy3a`

- Matches analysed: **380** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_wins_last_5 | -0.166 | 0.028 | -0.106 |
| away_team_points_last_5 | -0.171 | 0.041 | -0.101 |
| away_team_goals_scored_last_5 | -0.098 | -0.026 | -0.092 |
| home_team_points_last_5 | 0.027 | -0.123 | -0.064 |
| away_position_before_match | 0.181 | -0.111 | 0.061 |
| home_position_before_match | -0.062 | 0.134 | 0.045 |
| home_team_home_win_rate | 0.049 | -0.114 | -0.041 |
| home_team_wins_last_5 | 0.034 | -0.097 | -0.041 |
| away_points_before_match | -0.061 | 0.117 | 0.033 |
| home_team_home_goals_avg | 0.047 | -0.098 | -0.031 |
| home_team_goals_conceded_last_5 | -0.066 | 0.118 | 0.031 |
| points_difference | 0.167 | -0.223 | -0.026 |
| away_team_away_win_rate | -0.084 | 0.069 | -0.017 |
| away_team_goals_conceded_last_5 | 0.110 | -0.100 | 0.015 |
| home_points_before_match | 0.062 | -0.047 | 0.015 |
| position_difference | -0.179 | 0.182 | -0.012 |
| away_team_away_conceded_avg | 0.102 | -0.101 | 0.009 |
| rest_days_difference | -0.006 | -0.003 | -0.007 |
| away_team_away_goals_avg | -0.034 | 0.032 | -0.004 |
| home_team_home_conceded_avg | -0.050 | 0.061 | 0.003 |
| home_rest_days | 0.067 | -0.077 | -0.003 |
| home_team_goals_scored_last_5 | 0.014 | -0.019 | -0.002 |
| away_rest_days | 0.069 | -0.073 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 56 | 15 | 18 | 23 | 26.8% | 32.1% | 41.1% |
| -4..-2 | 88 | 26 | 26 | 36 | 29.5% | 29.5% | 40.9% |
| -1..1 | 97 | 36 | 32 | 29 | 37.1% | 33.0% | 29.9% |
| 2..4 | 80 | 43 | 18 | 19 | 53.8% | 22.5% | 23.8% |
| >4 | 59 | 24 | 21 | 14 | 40.7% | 35.6% | 23.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 89 | 46 | 29 | 14 | 51.7% | 32.6% | 15.7% |
| -5..-2 | 63 | 26 | 18 | 19 | 41.3% | 28.6% | 30.2% |
| -1..1 | 57 | 21 | 18 | 18 | 36.8% | 31.6% | 31.6% |
| 2..5 | 69 | 25 | 19 | 25 | 36.2% | 27.5% | 36.2% |
| >=6 | 102 | 26 | 31 | 45 | 25.5% | 30.4% | 44.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 24 | 8 | 5 | 11 | 33.3% | 20.8% | 45.8% |
| -1..0 | 76 | 30 | 23 | 23 | 39.5% | 30.3% | 30.3% |
| 0 | 170 | 66 | 52 | 52 | 38.8% | 30.6% | 30.6% |
| 1..2 | 93 | 35 | 31 | 27 | 37.6% | 33.3% | 29.0% |
| >2 | 7 | 2 | 1 | 4 | 28.6% | 14.3% | 57.1% |
| unknown | 10 | 3 | 3 | 4 | 30.0% | 30.0% | 40.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.6%** home win (112/298)
- `>= 0.5` tier: **39.0%** home win (32/82)
- Home-win gap (>= split minus < split): **+1.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 298 | 112 | 89 | 97 | 37.6% |
| high | >= 0.5 | 82 | 32 | 26 | 24 | 39.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.083 | 0.357 | -4.603 | 7.687 |
| away_points_before_match | 24.049 | 23.009 | 27.769 | 4.760 |
| position_difference | -1.799 | -0.043 | 2.777 | 4.575 |
| home_points_before_match | 27.132 | 23.365 | 23.165 | 3.967 |
| away_position_before_match | 11.639 | 11.243 | 8.810 | 2.829 |
| home_position_before_match | 9.840 | 11.200 | 11.587 | 1.746 |
| away_team_points_last_5 | 5.806 | 6.026 | 6.967 | 1.161 |
| away_team_goals_conceded_last_5 | 5.688 | 5.374 | 4.562 | 1.126 |
| home_team_goals_conceded_last_5 | 5.035 | 5.391 | 5.777 | 0.742 |
| home_team_points_last_5 | 6.569 | 5.991 | 5.835 | 0.735 |
| home_rest_days | 6.901 | 6.571 | 6.274 | 0.627 |
| away_rest_days | 6.830 | 6.562 | 6.385 | 0.445 |
| away_team_goals_scored_last_5 | 5.319 | 5.096 | 5.529 | 0.433 |
| away_team_wins_last_5 | 1.451 | 1.557 | 1.826 | 0.375 |
| home_team_goals_scored_last_5 | 5.438 | 5.174 | 5.264 | 0.264 |
| away_team_away_conceded_avg | 1.274 | 1.133 | 1.068 | 0.206 |
| home_team_home_goals_avg | 1.278 | 1.091 | 1.136 | 0.187 |
| home_team_wins_last_5 | 1.694 | 1.522 | 1.512 | 0.182 |
| rest_days_difference | 0.071 | 0.009 | -0.111 | 0.182 |
| home_team_home_conceded_avg | 0.977 | 1.061 | 1.080 | 0.103 |
| away_team_away_goals_avg | 1.014 | 1.010 | 1.098 | 0.088 |
| home_team_home_win_rate | 0.380 | 0.294 | 0.309 | 0.086 |
| away_team_away_win_rate | 0.284 | 0.292 | 0.350 | 0.066 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\italy3a\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\italy3a\charts\relationships_home_win_pct_by_position.png)

