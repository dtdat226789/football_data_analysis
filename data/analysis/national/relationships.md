# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:02:06+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: National League (England)
- Scope: league `national`

- Matches analysed: **557** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | -0.020 | 0.162 | 0.095 |
| home_points_before_match | 0.142 | -0.034 | 0.089 |
| home_team_goals_conceded_last_5 | -0.059 | 0.177 | 0.075 |
| points_difference | 0.261 | -0.198 | 0.070 |
| home_team_home_goals_avg | 0.167 | -0.096 | 0.066 |
| away_team_goals_conceded_last_5 | 0.095 | -0.030 | 0.054 |
| position_difference | -0.261 | 0.225 | -0.052 |
| away_team_goals_scored_last_5 | -0.073 | 0.157 | 0.050 |
| away_team_away_conceded_avg | 0.123 | -0.076 | 0.045 |
| home_position_before_match | -0.205 | 0.174 | -0.043 |
| home_team_goals_scored_last_5 | 0.110 | -0.067 | 0.041 |
| away_team_away_goals_avg | -0.058 | 0.117 | 0.034 |
| away_points_before_match | -0.060 | 0.119 | 0.034 |
| away_position_before_match | 0.151 | -0.133 | 0.028 |
| home_team_home_win_rate | 0.077 | -0.127 | -0.026 |
| away_team_wins_last_5 | -0.083 | 0.131 | 0.025 |
| away_team_points_last_5 | -0.097 | 0.136 | 0.017 |
| away_rest_days | -0.016 | 0.001 | -0.012 |
| home_team_points_last_5 | 0.106 | -0.139 | -0.011 |
| home_rest_days | 0.029 | -0.043 | -0.007 |
| rest_days_difference | 0.053 | -0.052 | 0.006 |
| home_team_wins_last_5 | 0.107 | -0.132 | -0.006 |
| away_team_away_win_rate | -0.094 | 0.107 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 101 | 32 | 16 | 53 | 31.7% | 15.8% | 52.5% |
| -4..-2 | 108 | 37 | 31 | 40 | 34.3% | 28.7% | 37.0% |
| -1..1 | 139 | 54 | 38 | 47 | 38.8% | 27.3% | 33.8% |
| 2..4 | 103 | 52 | 25 | 26 | 50.5% | 24.3% | 25.2% |
| >4 | 106 | 67 | 18 | 21 | 63.2% | 17.0% | 19.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 164 | 108 | 25 | 31 | 65.9% | 15.2% | 18.9% |
| -5..-2 | 85 | 38 | 29 | 18 | 44.7% | 34.1% | 21.2% |
| -1..1 | 61 | 20 | 20 | 21 | 32.8% | 32.8% | 34.4% |
| 2..5 | 78 | 31 | 12 | 35 | 39.7% | 15.4% | 44.9% |
| >=6 | 169 | 45 | 42 | 82 | 26.6% | 24.9% | 48.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 62 | 26 | 14 | 22 | 41.9% | 22.6% | 35.5% |
| -1..0 | 29 | 12 | 5 | 12 | 41.4% | 17.2% | 41.4% |
| 0 | 370 | 161 | 90 | 119 | 43.5% | 24.3% | 32.2% |
| 1..2 | 23 | 7 | 5 | 11 | 30.4% | 21.7% | 47.8% |
| >2 | 60 | 31 | 11 | 18 | 51.7% | 18.3% | 30.0% |
| unknown | 13 | 5 | 3 | 5 | 38.5% | 23.1% | 38.5% |
- *13 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.0%** home win (126/341)
- `>= 0.5` tier: **53.7%** home win (116/216)
- Home-win gap (>= split minus < split): **+16.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 341 | 126 | 77 | 138 | 37.0% |
| high | >= 0.5 | 216 | 116 | 51 | 49 | 53.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 6.231 | -1.953 | -7.053 | 13.285 |
| home_points_before_match | 35.860 | 29.297 | 27.898 | 7.961 |
| position_difference | -3.550 | 0.547 | 4.075 | 7.624 |
| away_points_before_match | 29.628 | 31.250 | 34.952 | 5.324 |
| home_position_before_match | 10.293 | 12.773 | 14.717 | 4.423 |
| away_position_before_match | 13.843 | 12.227 | 10.642 | 3.201 |
| home_team_points_last_5 | 7.054 | 6.766 | 5.561 | 1.492 |
| away_team_points_last_5 | 5.893 | 6.594 | 7.267 | 1.375 |
| home_team_goals_conceded_last_5 | 6.331 | 6.672 | 7.535 | 1.204 |
| away_team_goals_scored_last_5 | 6.351 | 7.008 | 7.524 | 1.173 |
| home_team_goals_scored_last_5 | 7.128 | 7.164 | 6.241 | 0.923 |
| away_team_goals_conceded_last_5 | 7.037 | 7.195 | 6.283 | 0.912 |
| home_team_wins_last_5 | 1.979 | 1.875 | 1.481 | 0.498 |
| away_team_wins_last_5 | 1.607 | 1.898 | 2.032 | 0.425 |
| home_rest_days | 5.852 | 5.552 | 5.530 | 0.322 |
| rest_days_difference | 0.051 | -0.240 | -0.258 | 0.309 |
| home_team_home_goals_avg | 1.608 | 1.483 | 1.378 | 0.230 |
| away_team_away_conceded_avg | 1.587 | 1.517 | 1.359 | 0.229 |
| home_team_home_conceded_avg | 1.139 | 1.199 | 1.338 | 0.199 |
| away_team_away_goals_avg | 1.143 | 1.277 | 1.307 | 0.164 |
| home_team_home_win_rate | 0.455 | 0.417 | 0.367 | 0.089 |
| away_team_away_win_rate | 0.279 | 0.335 | 0.366 | 0.087 |
| away_rest_days | 5.794 | 5.792 | 5.780 | 0.014 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\national\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\national\charts\relationships_home_win_pct_by_position.png)

