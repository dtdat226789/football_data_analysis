# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:48:19+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: LaLiga2 (Spain)
- Scope: league `spain2`

- Matches analysed: **575** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.198 | 0.068 | -0.101 |
| home_team_home_goals_avg | 0.133 | 0.001 | 0.098 |
| home_team_points_last_5 | 0.125 | -0.001 | 0.091 |
| home_points_before_match | 0.117 | 0.004 | 0.089 |
| points_difference | 0.204 | -0.095 | 0.088 |
| home_team_goals_scored_last_5 | 0.097 | 0.012 | 0.079 |
| position_difference | -0.185 | 0.092 | -0.077 |
| home_team_wins_last_5 | 0.126 | -0.042 | 0.065 |
| away_team_away_goals_avg | 0.009 | 0.071 | 0.052 |
| home_rest_days | 0.023 | 0.054 | 0.052 |
| home_team_home_win_rate | 0.106 | -0.043 | 0.050 |
| home_team_goals_conceded_last_5 | -0.102 | 0.042 | -0.048 |
| rest_days_difference | -0.004 | 0.077 | 0.047 |
| away_team_goals_conceded_last_5 | 0.064 | -0.006 | 0.043 |
| away_points_before_match | 0.008 | 0.054 | 0.041 |
| away_team_wins_last_5 | -0.086 | 0.045 | -0.035 |
| away_team_away_win_rate | -0.019 | 0.060 | 0.025 |
| away_rest_days | 0.028 | -0.007 | 0.016 |
| away_team_goals_scored_last_5 | -0.019 | 0.046 | 0.016 |
| away_team_away_conceded_avg | 0.030 | -0.014 | 0.013 |
| home_team_home_conceded_avg | -0.041 | 0.062 | 0.011 |
| away_position_before_match | 0.062 | -0.060 | 0.007 |
| away_team_points_last_5 | -0.040 | 0.048 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 84 | 31 | 23 | 30 | 36.9% | 27.4% | 35.7% |
| -4..-2 | 131 | 50 | 34 | 47 | 38.2% | 26.0% | 35.9% |
| -1..1 | 171 | 80 | 44 | 47 | 46.8% | 25.7% | 27.5% |
| 2..4 | 107 | 47 | 21 | 39 | 43.9% | 19.6% | 36.4% |
| >4 | 82 | 42 | 21 | 19 | 51.2% | 25.6% | 23.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 145 | 85 | 31 | 29 | 58.6% | 21.4% | 20.0% |
| -5..-2 | 100 | 44 | 26 | 30 | 44.0% | 26.0% | 30.0% |
| -1..1 | 68 | 33 | 17 | 18 | 48.5% | 25.0% | 26.5% |
| 2..5 | 95 | 33 | 27 | 35 | 34.7% | 28.4% | 36.8% |
| >=6 | 167 | 55 | 42 | 70 | 32.9% | 25.1% | 41.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 50 | 23 | 11 | 16 | 46.0% | 22.0% | 32.0% |
| -1..0 | 130 | 61 | 32 | 37 | 46.9% | 24.6% | 28.5% |
| 0 | 187 | 79 | 44 | 64 | 42.2% | 23.5% | 34.2% |
| 1..2 | 168 | 71 | 43 | 54 | 42.3% | 25.6% | 32.1% |
| >2 | 17 | 5 | 5 | 7 | 29.4% | 29.4% | 41.2% |
| unknown | 23 | 11 | 8 | 4 | 47.8% | 34.8% | 17.4% |
- *23 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **34.1%** home win (42/123)
- `>= 0.5` tier: **46.0%** home win (208/452)
- Home-win gap (>= split minus < split): **+11.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 123 | 42 | 34 | 47 | 34.1% |
| high | >= 0.5 | 452 | 208 | 109 | 135 | 46.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.452 | -0.846 | -3.588 | 6.040 |
| position_difference | -1.588 | 0.825 | 2.692 | 4.280 |
| home_points_before_match | 28.760 | 24.874 | 24.687 | 4.073 |
| away_points_before_match | 26.308 | 25.720 | 28.275 | 2.554 |
| home_position_before_match | 11.396 | 12.727 | 13.720 | 2.324 |
| away_position_before_match | 12.984 | 11.902 | 11.027 | 1.957 |
| home_team_points_last_5 | 6.368 | 5.531 | 5.791 | 0.837 |
| home_team_goals_conceded_last_5 | 5.552 | 5.657 | 6.313 | 0.761 |
| away_team_goals_conceded_last_5 | 5.676 | 6.119 | 5.401 | 0.718 |
| home_team_goals_scored_last_5 | 5.980 | 5.364 | 5.632 | 0.616 |
| away_team_points_last_5 | 6.148 | 5.853 | 6.440 | 0.586 |
| away_team_wins_last_5 | 2.780 | 2.622 | 3.011 | 0.389 |
| home_team_wins_last_5 | 2.904 | 2.594 | 2.637 | 0.310 |
| away_team_goals_scored_last_5 | 5.756 | 5.811 | 5.956 | 0.200 |
| rest_days_difference | -0.059 | 0.104 | 0.118 | 0.177 |
| home_team_home_goals_avg | 1.369 | 1.274 | 1.210 | 0.159 |
| away_rest_days | 7.025 | 6.919 | 6.899 | 0.126 |
| home_team_home_conceded_avg | 1.049 | 1.023 | 1.142 | 0.119 |
| away_team_away_conceded_avg | 1.324 | 1.275 | 1.216 | 0.108 |
| away_team_away_goals_avg | 1.039 | 1.123 | 1.104 | 0.084 |
| home_rest_days | 6.967 | 7.022 | 7.017 | 0.056 |
| home_team_home_win_rate | 0.672 | 0.638 | 0.617 | 0.054 |
| away_team_away_win_rate | 0.518 | 0.551 | 0.555 | 0.037 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\spain2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\spain2\charts\relationships_home_win_pct_by_position.png)

