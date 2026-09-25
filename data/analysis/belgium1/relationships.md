# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:55:20+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Jupiler Pro League (Belgium)
- Scope: league `belgium1`

- Matches analysed: **384** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_wins_last_5 | -0.158 | 0.028 | -0.098 |
| home_team_goals_conceded_last_5 | -0.133 | 0.008 | -0.093 |
| home_team_goals_scored_last_5 | 0.059 | 0.056 | 0.083 |
| away_team_points_last_5 | -0.157 | 0.055 | -0.078 |
| away_rest_days | -0.040 | -0.061 | -0.072 |
| away_team_away_win_rate | -0.102 | 0.017 | -0.064 |
| rest_days_difference | 0.044 | 0.033 | 0.056 |
| away_team_goals_scored_last_5 | -0.114 | 0.041 | -0.056 |
| home_team_points_last_5 | 0.056 | 0.017 | 0.053 |
| home_rest_days | -0.018 | -0.045 | -0.045 |
| position_difference | -0.192 | 0.141 | -0.044 |
| home_points_before_match | 0.087 | -0.035 | 0.040 |
| away_team_goals_conceded_last_5 | 0.029 | -0.074 | -0.031 |
| home_position_before_match | -0.142 | 0.108 | -0.029 |
| away_points_before_match | -0.027 | 0.068 | 0.028 |
| away_position_before_match | 0.107 | -0.074 | 0.027 |
| points_difference | 0.208 | -0.187 | 0.023 |
| home_team_wins_last_5 | 0.008 | 0.018 | 0.018 |
| home_team_home_win_rate | 0.049 | -0.075 | -0.017 |
| away_team_away_conceded_avg | 0.021 | -0.045 | -0.016 |
| home_team_home_conceded_avg | -0.130 | 0.116 | -0.015 |
| away_team_away_goals_avg | -0.061 | 0.045 | -0.014 |
| home_team_home_goals_avg | 0.078 | -0.070 | 0.009 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 66 | 22 | 15 | 29 | 33.3% | 22.7% | 43.9% |
| -4..-2 | 80 | 31 | 22 | 27 | 38.8% | 27.5% | 33.8% |
| -1..1 | 108 | 43 | 30 | 35 | 39.8% | 27.8% | 32.4% |
| 2..4 | 76 | 37 | 15 | 24 | 48.7% | 19.7% | 31.6% |
| >4 | 54 | 31 | 11 | 12 | 57.4% | 20.4% | 22.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 76 | 41 | 19 | 16 | 53.9% | 25.0% | 21.1% |
| -5..-2 | 72 | 37 | 16 | 19 | 51.4% | 22.2% | 26.4% |
| -1..1 | 72 | 34 | 17 | 21 | 47.2% | 23.6% | 29.2% |
| 2..5 | 82 | 33 | 16 | 33 | 40.2% | 19.5% | 40.2% |
| >=6 | 82 | 19 | 25 | 38 | 23.2% | 30.5% | 46.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 28 | 8 | 4 | 16 | 28.6% | 14.3% | 57.1% |
| -1..0 | 82 | 44 | 22 | 16 | 53.7% | 26.8% | 19.5% |
| 0 | 133 | 53 | 38 | 42 | 39.8% | 28.6% | 31.6% |
| 1..2 | 110 | 43 | 21 | 46 | 39.1% | 19.1% | 41.8% |
| >2 | 12 | 6 | 1 | 5 | 50.0% | 8.3% | 41.7% |
| unknown | 19 | 10 | 7 | 2 | 52.6% | 36.8% | 10.5% |
- *19 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **35.5%** home win (27/76)
- `>= 0.5` tier: **44.5%** home win (137/308)
- Home-win gap (>= split minus < split): **+9.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 76 | 27 | 25 | 24 | 35.5% |
| high | >= 0.5 | 308 | 137 | 68 | 103 | 44.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.823 | -1.022 | -3.268 | 6.091 |
| away_points_before_match | 21.000 | 21.849 | 24.732 | 3.732 |
| position_difference | -1.415 | 0.624 | 2.008 | 3.423 |
| home_points_before_match | 23.823 | 20.828 | 21.465 | 2.995 |
| home_position_before_match | 8.189 | 9.280 | 10.197 | 2.008 |
| away_team_points_last_5 | 5.427 | 5.849 | 6.913 | 1.487 |
| away_position_before_match | 9.604 | 8.656 | 8.189 | 1.415 |
| away_team_goals_scored_last_5 | 5.488 | 5.613 | 6.693 | 1.205 |
| home_team_goals_scored_last_5 | 5.774 | 5.043 | 6.024 | 0.981 |
| home_team_goals_conceded_last_5 | 5.445 | 5.892 | 6.386 | 0.941 |
| home_team_points_last_5 | 6.018 | 5.161 | 5.882 | 0.857 |
| home_rest_days | 7.994 | 7.360 | 7.624 | 0.633 |
| away_team_wins_last_5 | 2.512 | 2.667 | 3.039 | 0.527 |
| away_team_goals_conceded_last_5 | 5.970 | 5.484 | 5.488 | 0.486 |
| away_rest_days | 7.831 | 7.442 | 7.472 | 0.389 |
| home_team_wins_last_5 | 2.652 | 2.430 | 2.748 | 0.318 |
| home_team_home_goals_avg | 1.475 | 1.172 | 1.315 | 0.303 |
| home_team_home_conceded_avg | 0.938 | 1.089 | 1.236 | 0.298 |
| rest_days_difference | 0.162 | -0.081 | 0.152 | 0.244 |
| away_team_away_goals_avg | 1.049 | 1.054 | 1.183 | 0.134 |
| home_team_home_win_rate | 0.681 | 0.549 | 0.640 | 0.132 |
| away_team_away_win_rate | 0.504 | 0.494 | 0.560 | 0.066 |
| away_team_away_conceded_avg | 1.353 | 1.288 | 1.325 | 0.065 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\belgium1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\belgium1\charts\relationships_home_win_pct_by_position.png)

