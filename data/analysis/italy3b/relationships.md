# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:58:45+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie C - Group B (Italy)
- Scope: league `italy3b`

- Matches analysed: **357** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.167 | -0.035 | 0.093 |
| home_team_points_last_5 | 0.172 | -0.055 | 0.084 |
| home_team_wins_last_5 | 0.183 | -0.072 | 0.079 |
| home_team_home_goals_avg | 0.131 | -0.024 | 0.076 |
| home_team_home_win_rate | 0.108 | -0.002 | 0.074 |
| home_team_goals_scored_last_5 | 0.150 | -0.046 | 0.073 |
| away_team_goals_conceded_last_5 | 0.148 | -0.075 | 0.053 |
| rest_days_difference | 0.030 | 0.045 | 0.052 |
| points_difference | 0.251 | -0.185 | 0.049 |
| home_team_home_conceded_avg | -0.012 | 0.067 | 0.038 |
| position_difference | -0.239 | 0.192 | -0.036 |
| home_rest_days | -0.006 | 0.055 | 0.034 |
| away_position_before_match | 0.173 | -0.134 | 0.029 |
| home_points_before_match | 0.091 | -0.052 | 0.028 |
| home_position_before_match | -0.159 | 0.133 | -0.020 |
| away_team_away_win_rate | -0.108 | 0.082 | -0.020 |
| away_team_goals_scored_last_5 | -0.061 | 0.089 | 0.018 |
| home_team_goals_conceded_last_5 | -0.039 | 0.064 | 0.017 |
| away_rest_days | -0.031 | 0.009 | -0.016 |
| away_points_before_match | -0.094 | 0.084 | -0.008 |
| away_team_away_goals_avg | -0.111 | 0.103 | -0.007 |
| away_team_points_last_5 | -0.102 | 0.114 | 0.007 |
| away_team_wins_last_5 | -0.115 | 0.119 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 55 | 15 | 18 | 22 | 27.3% | 32.7% | 40.0% |
| -4..-2 | 75 | 22 | 22 | 31 | 29.3% | 29.3% | 41.3% |
| -1..1 | 102 | 41 | 30 | 31 | 40.2% | 29.4% | 30.4% |
| 2..4 | 77 | 25 | 30 | 22 | 32.5% | 39.0% | 28.6% |
| >4 | 48 | 31 | 13 | 4 | 64.6% | 27.1% | 8.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 88 | 49 | 27 | 12 | 55.7% | 30.7% | 13.6% |
| -5..-2 | 59 | 19 | 22 | 18 | 32.2% | 37.3% | 30.5% |
| -1..1 | 58 | 20 | 22 | 16 | 34.5% | 37.9% | 27.6% |
| 2..5 | 55 | 23 | 13 | 19 | 41.8% | 23.6% | 34.5% |
| >=6 | 97 | 23 | 29 | 45 | 23.7% | 29.9% | 46.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 40 | 14 | 13 | 13 | 35.0% | 32.5% | 32.5% |
| -1..0 | 68 | 26 | 23 | 19 | 38.2% | 33.8% | 27.9% |
| 0 | 142 | 58 | 39 | 45 | 40.8% | 27.5% | 31.7% |
| 1..2 | 86 | 29 | 30 | 27 | 33.7% | 34.9% | 31.4% |
| >2 | 11 | 2 | 4 | 5 | 18.2% | 36.4% | 45.5% |
| unknown | 10 | 5 | 4 | 1 | 50.0% | 40.0% | 10.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **32.8%** home win (84/256)
- `>= 0.5` tier: **49.5%** home win (50/101)
- Home-win gap (>= split minus < split): **+16.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 256 | 84 | 89 | 83 | 32.8% |
| high | >= 0.5 | 101 | 50 | 24 | 27 | 49.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.799 | -0.115 | -5.064 | 8.862 |
| position_difference | -2.082 | -0.142 | 3.309 | 5.391 |
| home_points_before_match | 26.149 | 23.894 | 21.518 | 4.631 |
| away_points_before_match | 22.351 | 24.009 | 26.582 | 4.231 |
| home_position_before_match | 9.030 | 10.637 | 12.045 | 3.016 |
| away_position_before_match | 11.112 | 10.779 | 8.736 | 2.376 |
| away_team_points_last_5 | 5.799 | 5.912 | 7.073 | 1.274 |
| home_team_points_last_5 | 6.776 | 5.796 | 5.564 | 1.212 |
| away_team_goals_scored_last_5 | 4.925 | 4.752 | 5.773 | 1.021 |
| home_team_goals_scored_last_5 | 5.582 | 4.903 | 4.918 | 0.679 |
| away_team_goals_conceded_last_5 | 5.381 | 5.088 | 4.718 | 0.662 |
| home_team_goals_conceded_last_5 | 4.873 | 5.186 | 5.527 | 0.654 |
| away_team_wins_last_5 | 1.425 | 1.469 | 1.927 | 0.502 |
| home_team_wins_last_5 | 1.791 | 1.442 | 1.318 | 0.473 |
| away_rest_days | 6.798 | 7.202 | 6.936 | 0.403 |
| home_rest_days | 6.612 | 6.881 | 6.844 | 0.268 |
| rest_days_difference | -0.186 | -0.321 | -0.092 | 0.229 |
| away_team_away_goals_avg | 0.945 | 1.027 | 1.135 | 0.190 |
| home_team_home_goals_avg | 1.174 | 1.032 | 1.009 | 0.165 |
| away_team_away_conceded_avg | 1.122 | 1.118 | 0.959 | 0.162 |
| away_team_away_win_rate | 0.284 | 0.277 | 0.365 | 0.088 |
| home_team_home_win_rate | 0.399 | 0.332 | 0.349 | 0.067 |
| home_team_home_conceded_avg | 0.996 | 0.982 | 1.047 | 0.065 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\italy3b\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\italy3b\charts\relationships_home_win_pct_by_position.png)

