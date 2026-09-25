# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:00:39+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Eerste Divisie (Netherlands)
- Scope: league `holland2`

- Matches analysed: **466** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_rest_days | 0.086 | 0.086 | 0.126 |
| position_difference | -0.040 | 0.211 | 0.116 |
| home_points_before_match | -0.038 | -0.094 | -0.094 |
| away_position_before_match | 0.029 | -0.163 | -0.090 |
| away_team_away_conceded_avg | -0.003 | -0.114 | -0.081 |
| away_rest_days | 0.051 | 0.054 | 0.077 |
| away_team_goals_scored_last_5 | 0.034 | 0.071 | 0.075 |
| rest_days_difference | 0.041 | 0.056 | 0.070 |
| home_position_before_match | -0.024 | 0.123 | 0.066 |
| away_points_before_match | -0.098 | 0.013 | -0.066 |
| away_team_away_goals_avg | 0.004 | 0.086 | 0.062 |
| away_team_points_last_5 | -0.011 | 0.100 | 0.060 |
| home_team_home_goals_avg | 0.023 | -0.092 | -0.046 |
| points_difference | 0.095 | -0.170 | -0.045 |
| away_team_goals_conceded_last_5 | 0.028 | -0.094 | -0.044 |
| away_team_away_win_rate | -0.054 | 0.110 | 0.035 |
| home_team_goals_conceded_last_5 | -0.029 | -0.006 | -0.026 |
| home_team_home_win_rate | 0.030 | -0.062 | -0.020 |
| home_team_goals_scored_last_5 | 0.061 | -0.050 | 0.012 |
| home_team_home_conceded_avg | 0.006 | -0.020 | -0.009 |
| away_team_wins_last_5 | -0.020 | 0.032 | 0.007 |
| home_team_wins_last_5 | -0.001 | 0.004 | 0.003 |
| home_team_points_last_5 | 0.035 | -0.037 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 74 | 24 | 14 | 36 | 32.4% | 18.9% | 48.6% |
| -4..-2 | 95 | 41 | 25 | 29 | 43.2% | 26.3% | 30.5% |
| -1..1 | 123 | 58 | 22 | 43 | 47.2% | 17.9% | 35.0% |
| 2..4 | 113 | 61 | 23 | 29 | 54.0% | 20.4% | 25.7% |
| >4 | 61 | 22 | 13 | 26 | 36.1% | 21.3% | 42.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 112 | 55 | 27 | 30 | 49.1% | 24.1% | 26.8% |
| -5..-2 | 90 | 41 | 21 | 28 | 45.6% | 23.3% | 31.1% |
| -1..1 | 61 | 33 | 9 | 19 | 54.1% | 14.8% | 31.1% |
| 2..5 | 79 | 32 | 13 | 34 | 40.5% | 16.5% | 43.0% |
| >=6 | 124 | 45 | 27 | 52 | 36.3% | 21.8% | 41.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 85 | 39 | 16 | 30 | 45.9% | 18.8% | 35.3% |
| -1..0 | 42 | 13 | 10 | 19 | 31.0% | 23.8% | 45.2% |
| 0 | 211 | 90 | 52 | 69 | 42.7% | 24.6% | 32.7% |
| 1..2 | 56 | 31 | 9 | 16 | 55.4% | 16.1% | 28.6% |
| >2 | 50 | 21 | 7 | 22 | 42.0% | 14.0% | 44.0% |
| unknown | 22 | 12 | 3 | 7 | 54.5% | 13.6% | 31.8% |
- *22 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **45.9%** home win (50/109)
- `>= 0.5` tier: **43.7%** home win (156/357)
- Home-win gap (>= split minus < split): **-2.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 109 | 50 | 15 | 44 | 45.9% |
| high | >= 0.5 | 357 | 156 | 82 | 119 | 43.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.583 | 0.320 | -2.479 | 4.061 |
| away_points_before_match | 21.592 | 24.041 | 25.074 | 3.481 |
| position_difference | -0.757 | 0.124 | 1.798 | 2.555 |
| home_points_before_match | 23.175 | 24.361 | 22.595 | 1.766 |
| away_position_before_match | 10.806 | 10.577 | 9.374 | 1.432 |
| home_position_before_match | 10.049 | 10.701 | 11.172 | 1.123 |
| home_team_goals_conceded_last_5 | 6.913 | 7.701 | 7.129 | 0.788 |
| away_team_goals_conceded_last_5 | 7.063 | 7.454 | 6.699 | 0.754 |
| rest_days_difference | -0.180 | -0.543 | 0.135 | 0.677 |
| away_team_points_last_5 | 5.820 | 6.113 | 6.491 | 0.670 |
| home_rest_days | 6.610 | 6.404 | 7.013 | 0.608 |
| home_team_goals_scored_last_5 | 7.228 | 7.052 | 6.810 | 0.418 |
| away_rest_days | 6.753 | 6.947 | 6.904 | 0.194 |
| away_team_wins_last_5 | 2.587 | 2.691 | 2.724 | 0.137 |
| home_team_points_last_5 | 6.068 | 6.010 | 6.141 | 0.131 |
| home_team_home_goals_avg | 1.678 | 1.664 | 1.547 | 0.131 |
| away_team_away_conceded_avg | 1.696 | 1.671 | 1.565 | 0.130 |
| away_team_away_goals_avg | 1.353 | 1.294 | 1.414 | 0.120 |
| home_team_wins_last_5 | 2.602 | 2.649 | 2.718 | 0.116 |
| away_team_goals_scored_last_5 | 7.214 | 7.278 | 7.301 | 0.087 |
| away_team_away_win_rate | 0.460 | 0.516 | 0.534 | 0.074 |
| home_team_home_win_rate | 0.598 | 0.626 | 0.568 | 0.057 |
| home_team_home_conceded_avg | 1.351 | 1.370 | 1.317 | 0.053 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\holland2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\holland2\charts\relationships_home_win_pct_by_position.png)

