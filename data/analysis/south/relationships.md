# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:08:40+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: National League South (England)
- Scope: league `south`

- Matches analysed: **605** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.115 | 0.083 | 0.141 |
| away_team_goals_conceded_last_5 | 0.142 | 0.044 | 0.135 |
| home_points_before_match | 0.141 | 0.020 | 0.117 |
| away_points_before_match | 0.060 | 0.095 | 0.109 |
| home_team_goals_scored_last_5 | 0.097 | 0.045 | 0.102 |
| away_team_goals_scored_last_5 | 0.042 | 0.097 | 0.097 |
| home_team_home_goals_avg | 0.130 | -0.017 | 0.084 |
| home_team_points_last_5 | 0.097 | -0.004 | 0.069 |
| home_team_goals_conceded_last_5 | -0.024 | 0.118 | 0.064 |
| home_team_wins_last_5 | 0.097 | -0.021 | 0.057 |
| away_position_before_match | 0.019 | -0.091 | -0.049 |
| away_rest_days | -0.042 | -0.025 | -0.048 |
| home_team_home_conceded_avg | -0.003 | 0.068 | 0.045 |
| home_team_home_win_rate | 0.115 | -0.059 | 0.044 |
| home_position_before_match | -0.116 | 0.070 | -0.037 |
| away_team_away_goals_avg | 0.013 | 0.039 | 0.036 |
| away_team_points_last_5 | -0.033 | 0.076 | 0.028 |
| home_rest_days | 0.002 | -0.035 | -0.023 |
| position_difference | -0.106 | 0.132 | 0.012 |
| points_difference | 0.124 | -0.116 | 0.012 |
| rest_days_difference | 0.007 | -0.023 | -0.010 |
| away_team_away_win_rate | -0.037 | 0.029 | -0.008 |
| away_team_wins_last_5 | -0.054 | 0.061 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 106 | 43 | 25 | 38 | 40.6% | 23.6% | 35.8% |
| -4..-2 | 129 | 60 | 30 | 39 | 46.5% | 23.3% | 30.2% |
| -1..1 | 156 | 66 | 34 | 56 | 42.3% | 21.8% | 35.9% |
| 2..4 | 118 | 66 | 27 | 25 | 55.9% | 22.9% | 21.2% |
| >4 | 96 | 54 | 19 | 23 | 56.2% | 19.8% | 24.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 196 | 117 | 39 | 40 | 59.7% | 19.9% | 20.4% |
| -5..-2 | 76 | 37 | 15 | 24 | 48.7% | 19.7% | 31.6% |
| -1..1 | 66 | 26 | 21 | 19 | 39.4% | 31.8% | 28.8% |
| 2..5 | 73 | 37 | 18 | 18 | 50.7% | 24.7% | 24.7% |
| >=6 | 194 | 72 | 42 | 80 | 37.1% | 21.6% | 41.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 58 | 31 | 12 | 15 | 53.4% | 20.7% | 25.9% |
| -1..0 | 9 | 6 | 2 | 1 | 66.7% | 22.2% | 11.1% |
| 0 | 400 | 184 | 88 | 128 | 46.0% | 22.0% | 32.0% |
| 1..2 | 11 | 4 | 5 | 2 | 36.4% | 45.5% | 18.2% |
| >2 | 69 | 37 | 13 | 19 | 53.6% | 18.8% | 27.5% |
| unknown | 58 | 27 | 15 | 16 | 46.6% | 25.9% | 27.6% |
- *58 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **41.3%** home win (140/339)
- `>= 0.5` tier: **56.0%** home win (149/266)
- Home-win gap (>= split minus < split): **+14.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 339 | 140 | 80 | 119 | 41.3% |
| high | >= 0.5 | 266 | 149 | 55 | 62 | 56.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.474 | -1.126 | -2.923 | 5.397 |
| home_points_before_match | 32.301 | 27.193 | 27.724 | 5.108 |
| position_difference | -2.118 | 0.296 | 2.519 | 4.637 |
| home_position_before_match | 12.810 | 14.726 | 15.917 | 3.107 |
| away_points_before_match | 29.827 | 28.319 | 30.646 | 2.328 |
| away_position_before_match | 14.927 | 14.430 | 13.398 | 1.530 |
| home_rest_days | 6.996 | 5.680 | 6.965 | 1.316 |
| home_team_points_last_5 | 6.592 | 5.674 | 6.166 | 0.918 |
| rest_days_difference | 0.939 | 0.033 | 0.945 | 0.912 |
| home_team_goals_scored_last_5 | 6.522 | 5.748 | 6.392 | 0.774 |
| away_team_points_last_5 | 6.090 | 6.126 | 6.807 | 0.717 |
| away_team_goals_conceded_last_5 | 6.512 | 6.015 | 5.834 | 0.678 |
| away_team_goals_scored_last_5 | 6.287 | 6.037 | 6.575 | 0.538 |
| home_team_goals_conceded_last_5 | 6.017 | 6.444 | 6.541 | 0.524 |
| home_team_wins_last_5 | 1.889 | 1.563 | 1.696 | 0.326 |
| away_rest_days | 5.941 | 5.873 | 6.156 | 0.283 |
| away_team_wins_last_5 | 1.668 | 1.719 | 1.923 | 0.255 |
| home_team_home_goals_avg | 1.459 | 1.257 | 1.281 | 0.201 |
| away_team_away_goals_avg | 1.103 | 1.025 | 1.151 | 0.125 |
| home_team_home_win_rate | 0.456 | 0.373 | 0.364 | 0.092 |
| away_team_away_conceded_avg | 1.372 | 1.284 | 1.360 | 0.089 |
| home_team_home_conceded_avg | 1.051 | 1.045 | 1.094 | 0.049 |
| away_team_away_win_rate | 0.276 | 0.281 | 0.294 | 0.019 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\south\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\south\charts\relationships_home_win_pct_by_position.png)

