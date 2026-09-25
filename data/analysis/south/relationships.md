# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:47:42+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: National League South (England)
- Scope: league `south`

- Matches analysed: **716** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_conceded_last_5 | 0.156 | 0.031 | 0.137 |
| away_team_away_conceded_avg | 0.147 | 0.026 | 0.127 |
| away_team_goals_scored_last_5 | 0.051 | 0.094 | 0.102 |
| home_points_before_match | 0.138 | -0.012 | 0.094 |
| away_points_before_match | 0.069 | 0.051 | 0.086 |
| home_team_goals_scored_last_5 | 0.075 | 0.038 | 0.082 |
| home_team_goals_conceded_last_5 | -0.017 | 0.130 | 0.077 |
| home_team_wins_last_5 | 0.073 | 0.016 | 0.066 |
| home_team_home_goals_avg | 0.102 | -0.019 | 0.062 |
| away_team_wins_last_5 | 0.006 | 0.075 | 0.057 |
| home_team_points_last_5 | 0.086 | -0.011 | 0.056 |
| away_team_away_goals_avg | 0.020 | 0.052 | 0.051 |
| home_team_home_conceded_avg | -0.019 | 0.086 | 0.045 |
| home_team_home_win_rate | 0.092 | -0.040 | 0.041 |
| away_rest_days | -0.036 | -0.020 | -0.041 |
| away_position_before_match | 0.033 | -0.075 | -0.028 |
| away_team_points_last_5 | -0.025 | 0.061 | 0.023 |
| home_rest_days | 0.005 | -0.034 | -0.019 |
| home_position_before_match | -0.093 | 0.073 | -0.018 |
| away_team_away_win_rate | -0.046 | 0.029 | -0.014 |
| points_difference | 0.115 | -0.106 | 0.012 |
| position_difference | -0.102 | 0.122 | 0.009 |
| rest_days_difference | 0.010 | -0.022 | -0.008 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 115 | 47 | 26 | 42 | 40.9% | 22.6% | 36.5% |
| -4..-2 | 151 | 66 | 40 | 45 | 43.7% | 26.5% | 29.8% |
| -1..1 | 199 | 78 | 48 | 73 | 39.2% | 24.1% | 36.7% |
| 2..4 | 146 | 77 | 32 | 37 | 52.7% | 21.9% | 25.3% |
| >4 | 105 | 59 | 20 | 26 | 56.2% | 19.0% | 24.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 228 | 129 | 45 | 54 | 56.6% | 19.7% | 23.7% |
| -5..-2 | 85 | 42 | 17 | 26 | 49.4% | 20.0% | 30.6% |
| -1..1 | 85 | 33 | 26 | 26 | 38.8% | 30.6% | 30.6% |
| 2..5 | 101 | 46 | 25 | 30 | 45.5% | 24.8% | 29.7% |
| >=6 | 217 | 77 | 53 | 87 | 35.5% | 24.4% | 40.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 64 | 31 | 14 | 19 | 48.4% | 21.9% | 29.7% |
| -1..0 | 12 | 7 | 2 | 3 | 58.3% | 16.7% | 25.0% |
| 0 | 481 | 214 | 112 | 155 | 44.5% | 23.3% | 32.2% |
| 1..2 | 14 | 4 | 8 | 2 | 28.6% | 57.1% | 14.3% |
| >2 | 73 | 38 | 13 | 22 | 52.1% | 17.8% | 30.1% |
| unknown | 72 | 33 | 17 | 22 | 45.8% | 23.6% | 30.6% |
- *72 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.1%** home win (56/151)
- `>= 0.5` tier: **48.0%** home win (271/565)
- Home-win gap (>= split minus < split): **+10.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 151 | 56 | 42 | 53 | 37.1% |
| high | >= 0.5 | 565 | 271 | 124 | 170 | 48.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 29.211 | 23.325 | 23.516 | 5.886 |
| points_difference | 2.239 | -1.012 | -2.274 | 4.512 |
| position_difference | -2.003 | 0.488 | 1.883 | 3.886 |
| away_points_before_match | 26.972 | 24.337 | 25.789 | 2.635 |
| home_position_before_match | 12.538 | 14.114 | 15.085 | 2.547 |
| away_position_before_match | 14.541 | 13.627 | 13.202 | 1.339 |
| home_rest_days | 6.729 | 5.497 | 6.558 | 1.232 |
| rest_days_difference | 0.844 | -0.007 | 0.736 | 0.850 |
| away_team_goals_conceded_last_5 | 6.346 | 5.789 | 5.570 | 0.776 |
| home_team_points_last_5 | 6.398 | 5.645 | 5.803 | 0.753 |
| home_team_goals_scored_last_5 | 6.291 | 5.663 | 6.121 | 0.628 |
| home_team_goals_conceded_last_5 | 5.801 | 6.012 | 6.395 | 0.593 |
| away_team_points_last_5 | 5.881 | 6.066 | 6.287 | 0.406 |
| away_rest_days | 5.772 | 5.690 | 5.947 | 0.257 |
| home_team_wins_last_5 | 2.740 | 2.548 | 2.601 | 0.192 |
| away_team_away_conceded_avg | 1.391 | 1.204 | 1.280 | 0.187 |
| home_team_home_goals_avg | 1.417 | 1.244 | 1.250 | 0.173 |
| away_team_goals_scored_last_5 | 6.083 | 6.018 | 6.166 | 0.148 |
| home_team_home_conceded_avg | 1.041 | 0.983 | 1.119 | 0.136 |
| away_team_wins_last_5 | 2.657 | 2.669 | 2.771 | 0.114 |
| away_team_away_goals_avg | 1.094 | 1.026 | 1.139 | 0.113 |
| home_team_home_win_rate | 0.669 | 0.603 | 0.589 | 0.080 |
| away_team_away_win_rate | 0.516 | 0.514 | 0.536 | 0.022 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\south\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\south\charts\relationships_home_win_pct_by_position.png)

