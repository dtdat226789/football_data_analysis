# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:01:19+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Virsliga (Latvia)
- Scope: league `latvia`

- Matches analysed: **182** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_rest_days | 0.028 | 0.211 | 0.170 |
| home_team_home_conceded_avg | -0.269 | 0.064 | -0.150 |
| home_points_before_match | 0.222 | -0.024 | 0.144 |
| rest_days_difference | 0.060 | -0.227 | -0.117 |
| home_rest_days | 0.055 | 0.100 | 0.110 |
| away_team_away_win_rate | -0.200 | 0.359 | 0.110 |
| away_points_before_match | -0.115 | 0.265 | 0.105 |
| home_team_goals_scored_last_5 | 0.232 | -0.092 | 0.103 |
| away_position_before_match | 0.159 | -0.297 | -0.095 |
| home_team_points_last_5 | 0.253 | -0.128 | 0.093 |
| home_position_before_match | -0.287 | 0.165 | -0.091 |
| away_team_away_goals_avg | -0.245 | 0.366 | 0.082 |
| away_team_points_last_5 | -0.175 | 0.292 | 0.081 |
| away_team_goals_scored_last_5 | -0.200 | 0.314 | 0.078 |
| home_team_goals_conceded_last_5 | -0.240 | 0.136 | -0.078 |
| away_team_wins_last_5 | -0.166 | 0.276 | 0.075 |
| away_team_goals_conceded_last_5 | -0.011 | -0.083 | -0.067 |
| home_team_home_win_rate | 0.132 | -0.060 | 0.053 |
| home_team_wins_last_5 | 0.239 | -0.173 | 0.051 |
| away_team_away_conceded_avg | 0.066 | -0.131 | -0.045 |
| points_difference | 0.351 | -0.308 | 0.036 |
| position_difference | -0.316 | 0.327 | 0.003 |
| home_team_home_goals_avg | 0.039 | -0.038 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 35 | 7 | 5 | 23 | 20.0% | 14.3% | 65.7% |
| -4..-2 | 34 | 10 | 11 | 13 | 29.4% | 32.4% | 38.2% |
| -1..1 | 46 | 24 | 10 | 12 | 52.2% | 21.7% | 26.1% |
| 2..4 | 35 | 19 | 10 | 6 | 54.3% | 28.6% | 17.1% |
| >4 | 32 | 23 | 7 | 2 | 71.9% | 21.9% | 6.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 18 | 15 | 2 | 1 | 83.3% | 11.1% | 5.6% |
| -5..-2 | 45 | 23 | 10 | 12 | 51.1% | 22.2% | 26.7% |
| -1..1 | 46 | 23 | 14 | 9 | 50.0% | 30.4% | 19.6% |
| 2..5 | 53 | 19 | 14 | 20 | 35.8% | 26.4% | 37.7% |
| >=6 | 20 | 3 | 3 | 14 | 15.0% | 15.0% | 70.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 14 | 3 | 2 | 9 | 21.4% | 14.3% | 64.3% |
| -1..0 | 39 | 19 | 10 | 10 | 48.7% | 25.6% | 25.6% |
| 0 | 59 | 23 | 14 | 22 | 39.0% | 23.7% | 37.3% |
| 1..2 | 62 | 35 | 14 | 13 | 56.5% | 22.6% | 21.0% |
| >2 | 2 | 0 | 1 | 1 | 0.0% | 50.0% | 50.0% |
| unknown | 6 | 3 | 2 | 1 | 50.0% | 33.3% | 16.7% |
- *6 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **35.9%** home win (28/78)
- `>= 0.5` tier: **52.9%** home win (55/104)
- Home-win gap (>= split minus < split): **+17.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 78 | 28 | 25 | 25 | 35.9% |
| high | >= 0.5 | 104 | 55 | 18 | 31 | 52.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 6.639 | -0.442 | -11.411 | 18.049 |
| away_points_before_match | 18.687 | 23.163 | 34.196 | 15.510 |
| away_team_goals_scored_last_5 | 5.470 | 5.837 | 9.500 | 4.030 |
| position_difference | -1.446 | 0.419 | 2.375 | 3.821 |
| away_team_points_last_5 | 5.205 | 5.349 | 8.821 | 3.617 |
| home_points_before_match | 25.325 | 22.721 | 22.786 | 2.604 |
| away_position_before_match | 6.410 | 6.000 | 3.911 | 2.499 |
| home_team_points_last_5 | 7.265 | 5.721 | 5.411 | 1.854 |
| home_team_goals_conceded_last_5 | 5.807 | 7.093 | 7.446 | 1.639 |
| home_team_goals_scored_last_5 | 7.386 | 5.767 | 6.000 | 1.618 |
| away_rest_days | 6.812 | 6.366 | 7.964 | 1.598 |
| home_position_before_match | 4.964 | 6.419 | 6.286 | 1.455 |
| away_team_wins_last_5 | 1.386 | 1.442 | 2.607 | 1.222 |
| away_team_goals_conceded_last_5 | 7.072 | 7.209 | 6.107 | 1.102 |
| away_team_away_goals_avg | 0.819 | 0.883 | 1.702 | 0.883 |
| rest_days_difference | 0.212 | 0.195 | -0.600 | 0.812 |
| home_team_wins_last_5 | 2.157 | 1.558 | 1.411 | 0.746 |
| home_rest_days | 7.025 | 6.667 | 7.364 | 0.697 |
| away_team_away_win_rate | 0.144 | 0.169 | 0.435 | 0.290 |
| away_team_away_conceded_avg | 1.779 | 1.672 | 1.545 | 0.234 |
| home_team_home_conceded_avg | 1.012 | 1.135 | 1.171 | 0.159 |
| home_team_home_goals_avg | 1.670 | 1.593 | 1.613 | 0.077 |
| home_team_home_win_rate | 0.503 | 0.448 | 0.475 | 0.055 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\latvia\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\latvia\charts\relationships_home_win_pct_by_position.png)

