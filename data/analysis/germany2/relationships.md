# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:51:16+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 2. Bundesliga (Germany)
- Scope: league `germany2`

- Matches analysed: **310** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_goals_avg | 0.044 | 0.089 | 0.091 |
| home_points_before_match | 0.146 | -0.039 | 0.083 |
| home_position_before_match | -0.131 | 0.042 | -0.070 |
| away_team_goals_conceded_last_5 | 0.070 | 0.014 | 0.062 |
| points_difference | 0.110 | -0.039 | 0.057 |
| home_team_home_win_rate | 0.083 | -0.015 | 0.052 |
| home_team_goals_conceded_last_5 | -0.024 | 0.102 | 0.048 |
| away_team_wins_last_5 | -0.077 | 0.016 | -0.047 |
| away_points_before_match | 0.064 | -0.010 | 0.041 |
| position_difference | -0.102 | 0.061 | -0.036 |
| home_team_wins_last_5 | -0.018 | -0.024 | -0.029 |
| away_team_goals_scored_last_5 | 0.022 | 0.020 | 0.029 |
| rest_days_difference | 0.032 | 0.005 | 0.028 |
| home_rest_days | -0.027 | -0.010 | -0.026 |
| away_team_points_last_5 | -0.065 | 0.037 | -0.024 |
| away_rest_days | -0.029 | -0.004 | -0.024 |
| away_team_away_conceded_avg | 0.035 | -0.004 | 0.023 |
| home_team_home_goals_avg | 0.027 | 0.002 | 0.022 |
| away_position_before_match | 0.016 | -0.046 | -0.018 |
| away_team_away_win_rate | -0.011 | 0.034 | 0.014 |
| home_team_points_last_5 | 0.022 | -0.013 | 0.009 |
| home_team_home_conceded_avg | -0.069 | 0.088 | 0.007 |
| home_team_goals_scored_last_5 | 0.030 | -0.034 | 0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 46 | 17 | 17 | 12 | 37.0% | 37.0% | 26.1% |
| -4..-2 | 77 | 26 | 22 | 29 | 33.8% | 28.6% | 37.7% |
| -1..1 | 86 | 53 | 15 | 18 | 61.6% | 17.4% | 20.9% |
| 2..4 | 56 | 31 | 8 | 17 | 55.4% | 14.3% | 30.4% |
| >4 | 45 | 17 | 13 | 15 | 37.8% | 28.9% | 33.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 71 | 42 | 13 | 16 | 59.2% | 18.3% | 22.5% |
| -5..-2 | 51 | 24 | 12 | 15 | 47.1% | 23.5% | 29.4% |
| -1..1 | 45 | 23 | 8 | 14 | 51.1% | 17.8% | 31.1% |
| 2..5 | 65 | 25 | 16 | 24 | 38.5% | 24.6% | 36.9% |
| >=6 | 78 | 30 | 26 | 22 | 38.5% | 33.3% | 28.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 27 | 13 | 5 | 9 | 48.1% | 18.5% | 33.3% |
| -1..0 | 69 | 37 | 11 | 21 | 53.6% | 15.9% | 30.4% |
| 0 | 92 | 42 | 20 | 30 | 45.7% | 21.7% | 32.6% |
| 1..2 | 111 | 43 | 38 | 30 | 38.7% | 34.2% | 27.0% |
| >2 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 11 | 9 | 1 | 1 | 81.8% | 9.1% | 9.1% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **43.2%** home win (73/169)
- `>= 0.5` tier: **50.4%** home win (71/141)
- Home-win gap (>= split minus < split): **+7.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 169 | 73 | 42 | 54 | 43.2% |
| high | >= 0.5 | 141 | 71 | 33 | 37 | 50.4% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 21.944 | 27.040 | 21.615 | 5.425 |
| points_difference | 1.861 | -2.653 | -1.637 | 4.514 |
| home_points_before_match | 23.806 | 24.387 | 19.978 | 4.409 |
| position_difference | -1.076 | 1.773 | 1.253 | 2.850 |
| home_position_before_match | 9.125 | 10.333 | 10.890 | 1.765 |
| away_position_before_match | 10.201 | 8.560 | 9.637 | 1.641 |
| away_team_points_last_5 | 5.924 | 7.013 | 6.484 | 1.090 |
| away_team_goals_scored_last_5 | 6.486 | 7.253 | 6.714 | 0.767 |
| home_team_goals_conceded_last_5 | 6.278 | 6.893 | 7.044 | 0.766 |
| away_rest_days | 8.801 | 8.320 | 8.678 | 0.481 |
| rest_days_difference | -0.081 | 0.338 | -0.044 | 0.419 |
| away_team_wins_last_5 | 1.639 | 1.920 | 1.791 | 0.281 |
| away_team_goals_conceded_last_5 | 6.625 | 6.693 | 6.462 | 0.232 |
| home_team_home_conceded_avg | 1.155 | 1.266 | 1.330 | 0.176 |
| home_team_goals_scored_last_5 | 6.451 | 6.480 | 6.582 | 0.131 |
| away_team_away_goals_avg | 1.178 | 1.305 | 1.247 | 0.127 |
| home_rest_days | 8.748 | 8.716 | 8.633 | 0.115 |
| away_team_away_conceded_avg | 1.450 | 1.368 | 1.422 | 0.081 |
| home_team_home_win_rate | 0.450 | 0.444 | 0.404 | 0.046 |
| away_team_away_win_rate | 0.300 | 0.339 | 0.309 | 0.039 |
| home_team_home_goals_avg | 1.400 | 1.432 | 1.439 | 0.038 |
| home_team_points_last_5 | 6.139 | 6.147 | 6.121 | 0.026 |
| home_team_wins_last_5 | 1.674 | 1.667 | 1.681 | 0.015 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\germany2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\germany2\charts\relationships_home_win_pct_by_position.png)

