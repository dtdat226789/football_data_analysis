# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:49:08+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: League Two (England)
- Scope: league `eng2`

- Matches analysed: **557** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_rest_days | 0.048 | 0.045 | 0.068 |
| away_rest_days | 0.068 | 0.017 | 0.064 |
| home_team_goals_conceded_last_5 | -0.139 | 0.064 | -0.064 |
| points_difference | 0.207 | -0.153 | 0.055 |
| home_team_points_last_5 | 0.134 | -0.081 | 0.047 |
| home_team_goals_scored_last_5 | 0.096 | -0.048 | 0.041 |
| away_team_goals_scored_last_5 | -0.048 | 0.112 | 0.040 |
| home_team_home_conceded_avg | -0.089 | 0.042 | -0.040 |
| away_position_before_match | 0.146 | -0.108 | 0.039 |
| position_difference | -0.215 | 0.187 | -0.037 |
| home_team_home_win_rate | 0.090 | -0.047 | 0.037 |
| away_team_away_win_rate | -0.012 | 0.066 | 0.036 |
| home_team_wins_last_5 | 0.112 | -0.081 | 0.030 |
| away_team_away_goals_avg | -0.016 | 0.059 | 0.028 |
| away_points_before_match | -0.068 | 0.037 | -0.027 |
| away_team_points_last_5 | -0.074 | 0.122 | 0.027 |
| away_team_away_conceded_avg | 0.077 | -0.048 | 0.026 |
| away_team_wins_last_5 | -0.072 | 0.114 | 0.022 |
| away_team_goals_conceded_last_5 | 0.049 | -0.080 | -0.017 |
| home_position_before_match | -0.150 | 0.150 | -0.013 |
| home_points_before_match | 0.069 | -0.063 | 0.009 |
| home_team_home_goals_avg | 0.075 | -0.075 | 0.006 |
| rest_days_difference | -0.037 | 0.050 | 0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 88 | 25 | 21 | 42 | 28.4% | 23.9% | 47.7% |
| -4..-2 | 123 | 48 | 32 | 43 | 39.0% | 26.0% | 35.0% |
| -1..1 | 143 | 57 | 35 | 51 | 39.9% | 24.5% | 35.7% |
| 2..4 | 103 | 44 | 27 | 32 | 42.7% | 26.2% | 31.1% |
| >4 | 100 | 59 | 24 | 17 | 59.0% | 24.0% | 17.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 156 | 81 | 40 | 35 | 51.9% | 25.6% | 22.4% |
| -5..-2 | 87 | 43 | 21 | 23 | 49.4% | 24.1% | 26.4% |
| -1..1 | 65 | 34 | 14 | 17 | 52.3% | 21.5% | 26.2% |
| 2..5 | 83 | 32 | 23 | 28 | 38.6% | 27.7% | 33.7% |
| >=6 | 166 | 43 | 41 | 82 | 25.9% | 24.7% | 49.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 39 | 20 | 7 | 12 | 51.3% | 17.9% | 30.8% |
| -1..0 | 13 | 4 | 5 | 4 | 30.8% | 38.5% | 30.8% |
| 0 | 441 | 180 | 111 | 150 | 40.8% | 25.2% | 34.0% |
| 1..2 | 21 | 13 | 4 | 4 | 61.9% | 19.0% | 19.0% |
| >2 | 31 | 12 | 7 | 12 | 38.7% | 22.6% | 38.7% |
| unknown | 12 | 4 | 5 | 3 | 33.3% | 41.7% | 25.0% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.3%** home win (134/350)
- `>= 0.5` tier: **47.8%** home win (99/207)
- Home-win gap (>= split minus < split): **+9.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 350 | 134 | 83 | 133 | 38.3% |
| high | >= 0.5 | 207 | 99 | 56 | 52 | 47.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.047 | 0.317 | -4.373 | 7.420 |
| position_difference | -2.236 | -0.122 | 3.286 | 5.523 |
| home_points_before_match | 33.060 | 31.698 | 28.654 | 4.406 |
| home_position_before_match | 11.412 | 11.496 | 14.492 | 3.080 |
| away_points_before_match | 30.013 | 31.381 | 33.027 | 3.014 |
| away_position_before_match | 13.648 | 11.619 | 11.205 | 2.443 |
| home_team_points_last_5 | 6.996 | 6.590 | 5.686 | 1.309 |
| home_team_goals_conceded_last_5 | 5.511 | 5.942 | 6.427 | 0.916 |
| away_team_points_last_5 | 6.099 | 6.489 | 6.930 | 0.831 |
| home_team_goals_scored_last_5 | 6.185 | 6.086 | 5.432 | 0.752 |
| away_team_goals_conceded_last_5 | 6.313 | 5.727 | 5.708 | 0.605 |
| away_team_goals_scored_last_5 | 5.833 | 6.058 | 6.351 | 0.519 |
| home_team_wins_last_5 | 1.948 | 1.770 | 1.535 | 0.413 |
| away_team_wins_last_5 | 1.657 | 1.770 | 1.919 | 0.262 |
| home_team_home_goals_avg | 1.358 | 1.380 | 1.202 | 0.179 |
| home_rest_days | 6.013 | 6.187 | 6.055 | 0.173 |
| rest_days_difference | -0.074 | 0.045 | 0.016 | 0.119 |
| away_rest_days | 6.087 | 6.142 | 6.038 | 0.103 |
| home_team_home_conceded_avg | 1.121 | 1.101 | 1.197 | 0.096 |
| away_team_away_conceded_avg | 1.360 | 1.265 | 1.279 | 0.095 |
| home_team_home_win_rate | 0.407 | 0.416 | 0.349 | 0.067 |
| away_team_away_win_rate | 0.314 | 0.338 | 0.318 | 0.024 |
| away_team_away_goals_avg | 1.141 | 1.137 | 1.161 | 0.024 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\eng2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\eng2\charts\relationships_home_win_pct_by_position.png)

