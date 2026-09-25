# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:56:32+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: ChNL (Czech Republic)
- Scope: league `czech2`

- Matches analysed: **312** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_win_rate | 0.044 | 0.107 | 0.108 |
| away_points_before_match | -0.071 | -0.045 | -0.088 |
| away_position_before_match | 0.166 | -0.090 | 0.078 |
| away_team_wins_last_5 | -0.127 | 0.042 | -0.077 |
| position_difference | -0.196 | 0.134 | -0.073 |
| away_team_away_conceded_avg | 0.105 | -0.022 | 0.073 |
| away_team_points_last_5 | -0.132 | 0.062 | -0.068 |
| away_team_goals_scored_last_5 | -0.106 | 0.036 | -0.064 |
| home_points_before_match | 0.019 | -0.120 | -0.064 |
| rest_days_difference | -0.047 | -0.023 | -0.055 |
| away_team_away_goals_avg | -0.038 | 0.125 | 0.051 |
| home_team_home_goals_avg | 0.071 | -0.015 | 0.049 |
| home_team_goals_conceded_last_5 | -0.053 | 0.010 | -0.038 |
| points_difference | 0.127 | -0.103 | 0.037 |
| away_team_goals_conceded_last_5 | 0.077 | -0.043 | 0.035 |
| home_team_wins_last_5 | 0.042 | -0.009 | 0.029 |
| home_position_before_match | -0.105 | 0.096 | -0.024 |
| away_rest_days | 0.015 | 0.010 | 0.020 |
| home_team_goals_scored_last_5 | 0.009 | -0.035 | -0.015 |
| away_team_away_win_rate | -0.096 | 0.103 | -0.012 |
| home_rest_days | -0.009 | -0.002 | -0.009 |
| home_team_points_last_5 | 0.039 | -0.057 | -0.006 |
| home_team_home_conceded_avg | 0.022 | -0.029 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 50 | 20 | 11 | 19 | 40.0% | 22.0% | 38.0% |
| -4..-2 | 59 | 22 | 16 | 21 | 37.3% | 27.1% | 35.6% |
| -1..1 | 92 | 40 | 22 | 30 | 43.5% | 23.9% | 32.6% |
| 2..4 | 68 | 42 | 8 | 18 | 61.8% | 11.8% | 26.5% |
| >4 | 43 | 18 | 17 | 8 | 41.9% | 39.5% | 18.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 60 | 34 | 12 | 14 | 56.7% | 20.0% | 23.3% |
| -5..-2 | 68 | 38 | 15 | 15 | 55.9% | 22.1% | 22.1% |
| -1..1 | 43 | 16 | 14 | 13 | 37.2% | 32.6% | 30.2% |
| 2..5 | 76 | 32 | 17 | 27 | 42.1% | 22.4% | 35.5% |
| >=6 | 65 | 22 | 16 | 27 | 33.8% | 24.6% | 41.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 36 | 19 | 7 | 10 | 52.8% | 19.4% | 27.8% |
| -1..0 | 54 | 21 | 15 | 18 | 38.9% | 27.8% | 33.3% |
| 0 | 114 | 49 | 25 | 40 | 43.0% | 21.9% | 35.1% |
| 1..2 | 81 | 44 | 18 | 19 | 54.3% | 22.2% | 23.5% |
| >2 | 10 | 2 | 5 | 3 | 20.0% | 50.0% | 30.0% |
| unknown | 17 | 7 | 4 | 6 | 41.2% | 23.5% | 35.3% |
- *17 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **48.6%** home win (36/74)
- `>= 0.5` tier: **44.5%** home win (106/238)
- Home-win gap (>= split minus < split): **-4.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 74 | 36 | 15 | 23 | 48.6% |
| high | >= 0.5 | 238 | 106 | 59 | 73 | 44.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.655 | -1.149 | -2.240 | 3.895 |
| home_points_before_match | 18.514 | 15.378 | 15.229 | 3.285 |
| position_difference | -1.007 | 0.662 | 1.760 | 2.767 |
| home_rest_days | 9.765 | 11.343 | 8.703 | 2.640 |
| rest_days_difference | -0.763 | 1.500 | -0.122 | 2.263 |
| away_rest_days | 10.556 | 9.843 | 8.822 | 1.733 |
| away_position_before_match | 9.035 | 8.338 | 7.625 | 1.410 |
| home_position_before_match | 8.028 | 9.000 | 9.385 | 1.357 |
| away_points_before_match | 16.859 | 16.527 | 17.469 | 0.942 |
| away_team_points_last_5 | 5.592 | 5.770 | 6.406 | 0.815 |
| home_team_goals_conceded_last_5 | 5.810 | 5.432 | 6.042 | 0.609 |
| away_team_goals_scored_last_5 | 5.585 | 5.703 | 6.135 | 0.551 |
| home_team_points_last_5 | 5.930 | 5.905 | 5.573 | 0.357 |
| away_team_goals_conceded_last_5 | 5.761 | 5.486 | 5.740 | 0.274 |
| away_team_wins_last_5 | 2.521 | 2.716 | 2.719 | 0.198 |
| home_team_home_goals_avg | 1.406 | 1.518 | 1.348 | 0.170 |
| away_team_away_goals_avg | 1.008 | 1.086 | 1.156 | 0.148 |
| away_team_away_conceded_avg | 1.468 | 1.373 | 1.346 | 0.122 |
| home_team_home_conceded_avg | 1.074 | 1.147 | 1.039 | 0.108 |
| away_team_away_win_rate | 0.460 | 0.492 | 0.518 | 0.058 |
| home_team_wins_last_5 | 2.620 | 2.581 | 2.573 | 0.047 |
| home_team_goals_scored_last_5 | 5.704 | 5.676 | 5.708 | 0.033 |
| home_team_home_win_rate | 0.594 | 0.613 | 0.615 | 0.021 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\czech2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\czech2\charts\relationships_home_win_pct_by_position.png)

