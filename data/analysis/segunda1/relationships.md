# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:06:53+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Segunda RFEF - Group 1 (Spain)
- Scope: league `segunda1`

- Matches analysed: **306** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_conceded_last_5 | 0.195 | -0.013 | 0.136 |
| away_team_away_win_rate | -0.175 | 0.029 | -0.111 |
| away_position_before_match | 0.188 | -0.060 | 0.101 |
| home_team_goals_conceded_last_5 | 0.004 | 0.150 | 0.099 |
| away_team_away_conceded_avg | 0.160 | -0.039 | 0.093 |
| home_team_home_conceded_avg | -0.028 | 0.164 | 0.084 |
| points_difference | 0.229 | -0.144 | 0.076 |
| away_team_points_last_5 | -0.140 | 0.051 | -0.071 |
| home_team_home_win_rate | 0.026 | -0.133 | -0.067 |
| home_points_before_match | 0.109 | -0.024 | 0.065 |
| rest_days_difference | -0.057 | -0.031 | -0.062 |
| away_team_wins_last_5 | -0.135 | 0.063 | -0.060 |
| home_team_home_goals_avg | 0.024 | -0.101 | -0.048 |
| away_team_away_goals_avg | -0.125 | 0.071 | -0.047 |
| position_difference | -0.190 | 0.150 | -0.044 |
| home_position_before_match | -0.075 | 0.150 | 0.041 |
| away_team_goals_scored_last_5 | -0.071 | 0.028 | -0.035 |
| away_rest_days | 0.015 | 0.037 | 0.034 |
| home_team_goals_scored_last_5 | 0.116 | -0.102 | 0.021 |
| home_team_points_last_5 | 0.066 | -0.102 | -0.017 |
| away_points_before_match | -0.052 | 0.078 | 0.011 |
| home_team_wins_last_5 | 0.066 | -0.086 | -0.007 |
| home_rest_days | -0.018 | 0.020 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 50 | 14 | 13 | 23 | 28.0% | 26.0% | 46.0% |
| -4..-2 | 78 | 33 | 19 | 26 | 42.3% | 24.4% | 33.3% |
| -1..1 | 72 | 27 | 24 | 21 | 37.5% | 33.3% | 29.2% |
| 2..4 | 67 | 34 | 17 | 16 | 50.7% | 25.4% | 23.9% |
| >4 | 39 | 19 | 11 | 9 | 48.7% | 28.2% | 23.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 75 | 37 | 21 | 17 | 49.3% | 28.0% | 22.7% |
| -5..-2 | 52 | 26 | 15 | 11 | 50.0% | 28.8% | 21.2% |
| -1..1 | 45 | 18 | 14 | 13 | 40.0% | 31.1% | 28.9% |
| 2..5 | 59 | 20 | 15 | 24 | 33.9% | 25.4% | 40.7% |
| >=6 | 75 | 26 | 19 | 30 | 34.7% | 25.3% | 40.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 1 | 0 | 0 | 1 | 0.0% | 0.0% | 100.0% |
| -1..0 | 63 | 28 | 18 | 17 | 44.4% | 28.6% | 27.0% |
| 0 | 176 | 72 | 49 | 55 | 40.9% | 27.8% | 31.2% |
| 1..2 | 54 | 21 | 13 | 20 | 38.9% | 24.1% | 37.0% |
| >2 | 3 | 2 | 1 | 0 | 66.7% | 33.3% | 0.0% |
| unknown | 9 | 4 | 3 | 2 | 44.4% | 33.3% | 22.2% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **39.8%** home win (78/196)
- `>= 0.5` tier: **44.5%** home win (49/110)
- Home-win gap (>= split minus < split): **+4.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 196 | 78 | 48 | 70 | 39.8% |
| high | >= 0.5 | 110 | 49 | 36 | 25 | 44.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.748 | 0.000 | -2.758 | 4.506 |
| position_difference | -1.118 | 0.095 | 2.137 | 3.255 |
| away_points_before_match | 21.953 | 21.000 | 24.116 | 3.116 |
| home_points_before_match | 23.701 | 21.000 | 21.358 | 2.701 |
| home_position_before_match | 9.024 | 9.500 | 10.947 | 1.924 |
| away_position_before_match | 10.142 | 9.405 | 8.811 | 1.331 |
| away_team_points_last_5 | 5.874 | 6.357 | 6.916 | 1.042 |
| home_team_goals_scored_last_5 | 5.866 | 5.571 | 4.979 | 0.887 |
| away_team_goals_conceded_last_5 | 5.976 | 5.500 | 5.105 | 0.871 |
| home_team_points_last_5 | 6.354 | 6.107 | 5.547 | 0.807 |
| home_team_goals_conceded_last_5 | 5.425 | 5.798 | 6.084 | 0.659 |
| away_team_wins_last_5 | 1.512 | 1.667 | 1.895 | 0.383 |
| away_team_goals_scored_last_5 | 5.583 | 5.940 | 5.958 | 0.375 |
| home_team_wins_last_5 | 1.677 | 1.619 | 1.400 | 0.277 |
| home_team_home_conceded_avg | 0.956 | 1.002 | 1.137 | 0.181 |
| home_rest_days | 7.154 | 7.309 | 7.226 | 0.154 |
| away_team_away_conceded_avg | 1.309 | 1.289 | 1.167 | 0.142 |
| away_rest_days | 7.154 | 7.296 | 7.258 | 0.142 |
| away_team_away_goals_avg | 0.962 | 1.065 | 1.071 | 0.109 |
| home_team_home_goals_avg | 1.315 | 1.253 | 1.215 | 0.100 |
| home_team_home_win_rate | 0.423 | 0.409 | 0.337 | 0.086 |
| rest_days_difference | 0.000 | 0.012 | -0.032 | 0.045 |
| away_team_away_win_rate | 0.255 | 0.260 | 0.296 | 0.041 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\segunda1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\segunda1\charts\relationships_home_win_pct_by_position.png)

