# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:00:27+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Eredivisie (Netherlands)
- Scope: league `holland1`

- Matches analysed: **384** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.219 | 0.070 | -0.125 |
| rest_days_difference | -0.036 | -0.120 | -0.118 |
| points_difference | 0.289 | -0.159 | 0.116 |
| home_team_home_conceded_avg | 0.005 | 0.143 | 0.109 |
| away_team_goals_conceded_last_5 | 0.053 | -0.182 | -0.092 |
| away_position_before_match | 0.137 | -0.272 | -0.090 |
| home_team_goals_scored_last_5 | 0.166 | -0.068 | 0.084 |
| away_points_before_match | -0.061 | -0.043 | -0.081 |
| away_team_away_conceded_avg | 0.070 | -0.181 | -0.078 |
| away_team_away_goals_avg | -0.087 | 0.198 | 0.076 |
| away_team_away_win_rate | -0.095 | 0.206 | 0.076 |
| home_team_goals_conceded_last_5 | -0.055 | -0.033 | -0.069 |
| away_rest_days | 0.013 | 0.078 | 0.068 |
| home_team_home_win_rate | 0.062 | -0.157 | -0.067 |
| away_team_points_last_5 | -0.051 | 0.146 | 0.067 |
| home_team_points_last_5 | 0.137 | -0.074 | 0.056 |
| home_team_home_goals_avg | 0.140 | -0.080 | 0.054 |
| away_team_wins_last_5 | -0.037 | 0.096 | 0.041 |
| away_team_goals_scored_last_5 | -0.074 | 0.130 | 0.036 |
| position_difference | -0.272 | 0.257 | -0.029 |
| home_team_wins_last_5 | 0.083 | -0.102 | -0.008 |
| home_points_before_match | 0.137 | -0.152 | -0.002 |
| home_rest_days | -0.009 | 0.007 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 62 | 19 | 16 | 27 | 30.6% | 25.8% | 43.5% |
| -4..-2 | 82 | 30 | 20 | 32 | 36.6% | 24.4% | 39.0% |
| -1..1 | 114 | 45 | 34 | 35 | 39.5% | 29.8% | 30.7% |
| 2..4 | 76 | 37 | 20 | 19 | 48.7% | 26.3% | 25.0% |
| >4 | 50 | 31 | 10 | 9 | 62.0% | 20.0% | 18.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 81 | 51 | 16 | 14 | 63.0% | 19.8% | 17.3% |
| -5..-2 | 75 | 36 | 21 | 18 | 48.0% | 28.0% | 24.0% |
| -1..1 | 64 | 25 | 20 | 19 | 39.1% | 31.2% | 29.7% |
| 2..5 | 72 | 24 | 23 | 25 | 33.3% | 31.9% | 34.7% |
| >=6 | 92 | 26 | 20 | 46 | 28.3% | 21.7% | 50.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 23 | 7 | 6 | 10 | 30.4% | 26.1% | 43.5% |
| -1..0 | 85 | 32 | 19 | 34 | 37.6% | 22.4% | 40.0% |
| 0 | 120 | 57 | 31 | 32 | 47.5% | 25.8% | 26.7% |
| 1..2 | 114 | 46 | 33 | 35 | 40.4% | 28.9% | 30.7% |
| >2 | 20 | 8 | 7 | 5 | 40.0% | 35.0% | 25.0% |
| unknown | 22 | 12 | 4 | 6 | 54.5% | 18.2% | 27.3% |
- *22 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.3%** home win (31/93)
- `>= 0.5` tier: **45.0%** home win (131/291)
- Home-win gap (>= split minus < split): **+11.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 93 | 31 | 28 | 34 | 33.3% |
| high | >= 0.5 | 291 | 131 | 72 | 88 | 45.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.222 | -0.500 | -4.238 | 7.460 |
| home_points_before_match | 21.543 | 19.920 | 15.992 | 5.551 |
| position_difference | -1.981 | 0.330 | 3.311 | 5.293 |
| away_position_before_match | 11.216 | 9.900 | 8.205 | 3.011 |
| home_position_before_match | 9.235 | 10.230 | 11.516 | 2.282 |
| away_points_before_match | 18.321 | 20.420 | 20.230 | 2.099 |
| home_team_goals_scored_last_5 | 7.358 | 6.980 | 5.918 | 1.440 |
| away_team_goals_scored_last_5 | 6.290 | 7.140 | 7.492 | 1.202 |
| home_team_points_last_5 | 6.154 | 5.950 | 4.984 | 1.171 |
| away_team_goals_conceded_last_5 | 7.148 | 6.980 | 6.025 | 1.124 |
| away_team_points_last_5 | 5.438 | 6.060 | 6.443 | 1.004 |
| rest_days_difference | 0.133 | 0.344 | -0.259 | 0.602 |
| home_rest_days | 7.967 | 8.479 | 8.068 | 0.512 |
| away_rest_days | 7.860 | 8.135 | 8.362 | 0.502 |
| home_team_wins_last_5 | 2.759 | 2.710 | 2.393 | 0.366 |
| away_team_away_goals_avg | 1.200 | 1.410 | 1.562 | 0.362 |
| home_team_home_goals_avg | 1.754 | 1.597 | 1.454 | 0.300 |
| home_team_goals_conceded_last_5 | 6.870 | 6.970 | 6.680 | 0.290 |
| away_team_away_conceded_avg | 1.674 | 1.688 | 1.405 | 0.283 |
| away_team_wins_last_5 | 2.525 | 2.780 | 2.803 | 0.279 |
| home_team_home_conceded_avg | 1.254 | 1.480 | 1.356 | 0.226 |
| away_team_away_win_rate | 0.442 | 0.507 | 0.575 | 0.133 |
| home_team_home_win_rate | 0.654 | 0.567 | 0.583 | 0.087 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\holland1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\holland1\charts\relationships_home_win_pct_by_position.png)

