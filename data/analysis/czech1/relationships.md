# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:56:22+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Chance Liga (Czech Republic)
- Scope: league `czech1`

- Matches analysed: **351** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_win_rate | -0.105 | -0.054 | -0.120 |
| home_position_before_match | -0.242 | 0.124 | -0.094 |
| home_team_goals_conceded_last_5 | -0.107 | 0.002 | -0.080 |
| home_team_home_goals_avg | 0.156 | -0.065 | 0.072 |
| position_difference | -0.264 | 0.179 | -0.071 |
| away_team_away_goals_avg | -0.116 | 0.026 | -0.070 |
| points_difference | 0.266 | -0.209 | 0.051 |
| away_team_wins_last_5 | -0.105 | 0.044 | -0.048 |
| away_team_points_last_5 | -0.096 | 0.036 | -0.047 |
| home_team_goals_scored_last_5 | 0.146 | -0.091 | 0.045 |
| home_points_before_match | 0.155 | -0.100 | 0.045 |
| home_team_points_last_5 | 0.182 | -0.136 | 0.040 |
| rest_days_difference | -0.000 | -0.043 | -0.031 |
| away_team_away_conceded_avg | -0.036 | -0.002 | -0.029 |
| home_team_home_conceded_avg | -0.055 | 0.024 | -0.025 |
| home_rest_days | -0.037 | 0.007 | -0.023 |
| home_team_home_win_rate | 0.151 | -0.134 | 0.017 |
| away_rest_days | -0.033 | 0.012 | -0.016 |
| away_team_goals_scored_last_5 | -0.077 | 0.059 | -0.016 |
| away_points_before_match | -0.021 | 0.039 | 0.012 |
| away_team_goals_conceded_last_5 | 0.057 | -0.051 | 0.006 |
| away_position_before_match | 0.095 | -0.105 | -0.005 |
| home_team_wins_last_5 | 0.147 | -0.155 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 56 | 13 | 12 | 31 | 23.2% | 21.4% | 55.4% |
| -4..-2 | 73 | 25 | 20 | 28 | 34.2% | 27.4% | 38.4% |
| -1..1 | 98 | 47 | 16 | 35 | 48.0% | 16.3% | 35.7% |
| 2..4 | 74 | 32 | 24 | 18 | 43.2% | 32.4% | 24.3% |
| >4 | 50 | 33 | 10 | 7 | 66.0% | 20.0% | 14.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 63 | 42 | 17 | 4 | 66.7% | 27.0% | 6.3% |
| -5..-2 | 81 | 38 | 19 | 24 | 46.9% | 23.5% | 29.6% |
| -1..1 | 68 | 27 | 20 | 21 | 39.7% | 29.4% | 30.9% |
| 2..5 | 75 | 28 | 12 | 35 | 37.3% | 16.0% | 46.7% |
| >=6 | 64 | 15 | 14 | 35 | 23.4% | 21.9% | 54.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 18 | 9 | 3 | 6 | 50.0% | 16.7% | 33.3% |
| -1..0 | 71 | 34 | 18 | 19 | 47.9% | 25.4% | 26.8% |
| 0 | 147 | 60 | 33 | 54 | 40.8% | 22.4% | 36.7% |
| 1..2 | 80 | 30 | 19 | 31 | 37.5% | 23.8% | 38.8% |
| >2 | 17 | 9 | 6 | 2 | 52.9% | 35.3% | 11.8% |
| unknown | 18 | 8 | 3 | 7 | 44.4% | 16.7% | 38.9% |
- *18 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **36.1%** home win (35/97)
- `>= 0.5` tier: **45.3%** home win (115/254)
- Home-win gap (>= split minus < split): **+9.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 97 | 35 | 27 | 35 | 36.1% |
| high | >= 0.5 | 254 | 115 | 55 | 84 | 45.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.253 | 1.256 | -4.706 | 7.959 |
| away_points_before_match | 19.053 | 15.402 | 21.933 | 6.530 |
| home_points_before_match | 22.307 | 16.659 | 17.227 | 5.648 |
| position_difference | -1.793 | -0.659 | 2.655 | 4.449 |
| home_position_before_match | 7.407 | 9.073 | 10.034 | 2.627 |
| away_position_before_match | 9.200 | 9.732 | 7.378 | 2.354 |
| home_team_points_last_5 | 6.640 | 5.646 | 4.916 | 1.724 |
| home_rest_days | 8.531 | 9.608 | 8.304 | 1.304 |
| home_team_goals_scored_last_5 | 6.260 | 5.427 | 5.050 | 1.210 |
| away_rest_days | 8.655 | 9.418 | 8.310 | 1.108 |
| away_team_points_last_5 | 5.647 | 5.610 | 6.479 | 0.869 |
| away_team_goals_scored_last_5 | 5.480 | 5.476 | 6.118 | 0.642 |
| home_team_goals_conceded_last_5 | 5.493 | 5.659 | 6.118 | 0.624 |
| home_team_wins_last_5 | 2.960 | 2.549 | 2.361 | 0.599 |
| away_team_goals_conceded_last_5 | 5.953 | 5.427 | 5.437 | 0.527 |
| away_team_wins_last_5 | 2.553 | 2.585 | 2.916 | 0.363 |
| home_team_home_goals_avg | 1.427 | 1.182 | 1.130 | 0.297 |
| rest_days_difference | -0.085 | 0.190 | -0.045 | 0.274 |
| away_team_away_goals_avg | 1.091 | 1.118 | 1.279 | 0.188 |
| home_team_home_win_rate | 0.689 | 0.567 | 0.546 | 0.144 |
| away_team_away_win_rate | 0.530 | 0.479 | 0.576 | 0.098 |
| home_team_home_conceded_avg | 1.119 | 1.181 | 1.200 | 0.081 |
| away_team_away_conceded_avg | 1.287 | 1.298 | 1.244 | 0.054 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\czech1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\czech1\charts\relationships_home_win_pct_by_position.png)

