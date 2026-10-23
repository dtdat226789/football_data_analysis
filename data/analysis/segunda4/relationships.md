# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:07:39+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

- Matches analysed: **323** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | 0.035 | 0.141 | 0.115 |
| away_position_before_match | 0.106 | 0.019 | 0.089 |
| away_team_goals_scored_last_5 | -0.060 | -0.066 | -0.086 |
| position_difference | -0.189 | 0.085 | -0.082 |
| away_team_points_last_5 | -0.090 | -0.021 | -0.079 |
| away_team_wins_last_5 | -0.088 | -0.013 | -0.071 |
| home_team_home_goals_avg | 0.208 | -0.128 | 0.068 |
| away_team_away_win_rate | -0.077 | -0.014 | -0.065 |
| away_team_goals_conceded_last_5 | 0.148 | -0.080 | 0.056 |
| points_difference | 0.204 | -0.165 | 0.042 |
| home_team_goals_conceded_last_5 | -0.056 | 0.128 | 0.041 |
| home_team_goals_scored_last_5 | 0.108 | -0.060 | 0.039 |
| home_rest_days | 0.069 | -0.022 | 0.036 |
| home_points_before_match | 0.176 | -0.149 | 0.032 |
| away_rest_days | 0.080 | -0.043 | 0.031 |
| home_team_home_win_rate | 0.144 | -0.203 | -0.026 |
| away_team_away_goals_avg | -0.010 | -0.026 | -0.024 |
| home_position_before_match | -0.155 | 0.139 | -0.023 |
| home_team_points_last_5 | 0.127 | -0.119 | 0.016 |
| away_team_away_conceded_avg | 0.087 | -0.084 | 0.009 |
| home_team_wins_last_5 | 0.102 | -0.106 | 0.006 |
| rest_days_difference | -0.009 | 0.019 | 0.006 |
| away_points_before_match | 0.042 | -0.041 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 62 | 22 | 18 | 22 | 35.5% | 29.0% | 35.5% |
| -4..-2 | 62 | 28 | 17 | 17 | 45.2% | 27.4% | 27.4% |
| -1..1 | 101 | 51 | 25 | 25 | 50.5% | 24.8% | 24.8% |
| 2..4 | 60 | 35 | 17 | 8 | 58.3% | 28.3% | 13.3% |
| >4 | 38 | 26 | 7 | 5 | 68.4% | 18.4% | 13.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 69 | 44 | 12 | 13 | 63.8% | 17.4% | 18.8% |
| -5..-2 | 59 | 29 | 20 | 10 | 49.2% | 33.9% | 16.9% |
| -1..1 | 54 | 29 | 14 | 11 | 53.7% | 25.9% | 20.4% |
| 2..5 | 51 | 25 | 12 | 14 | 49.0% | 23.5% | 27.5% |
| >=6 | 90 | 35 | 26 | 29 | 38.9% | 28.9% | 32.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 12 | 7 | 3 | 2 | 58.3% | 25.0% | 16.7% |
| -1..0 | 31 | 15 | 8 | 8 | 48.4% | 25.8% | 25.8% |
| 0 | 225 | 111 | 60 | 54 | 49.3% | 26.7% | 24.0% |
| 1..2 | 28 | 18 | 6 | 4 | 64.3% | 21.4% | 14.3% |
| >2 | 17 | 6 | 4 | 7 | 35.3% | 23.5% | 41.2% |
| unknown | 10 | 5 | 3 | 2 | 50.0% | 30.0% | 20.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **40.7%** home win (66/162)
- `>= 0.5` tier: **59.6%** home win (96/161)
- Home-win gap (>= split minus < split): **+18.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 162 | 66 | 46 | 50 | 40.7% |
| high | >= 0.5 | 161 | 96 | 38 | 27 | 59.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 26.315 | 20.988 | 18.909 | 7.406 |
| points_difference | 2.488 | -2.298 | -3.909 | 6.397 |
| position_difference | -1.019 | 1.500 | 2.091 | 3.109 |
| home_position_before_match | 9.198 | 10.726 | 11.545 | 2.348 |
| home_team_points_last_5 | 6.556 | 5.845 | 5.130 | 1.426 |
| away_team_goals_conceded_last_5 | 5.383 | 4.810 | 4.195 | 1.188 |
| away_points_before_match | 23.827 | 23.286 | 22.818 | 1.009 |
| away_position_before_match | 10.216 | 9.226 | 9.455 | 0.990 |
| home_team_goals_conceded_last_5 | 4.827 | 5.548 | 5.597 | 0.770 |
| home_team_goals_scored_last_5 | 5.198 | 4.976 | 4.558 | 0.639 |
| away_team_points_last_5 | 6.216 | 6.619 | 6.831 | 0.615 |
| away_rest_days | 7.287 | 7.123 | 6.747 | 0.540 |
| rest_days_difference | 0.025 | -0.099 | 0.360 | 0.459 |
| away_team_goals_scored_last_5 | 5.080 | 5.536 | 5.117 | 0.455 |
| home_team_wins_last_5 | 1.747 | 1.595 | 1.351 | 0.396 |
| home_team_home_goals_avg | 1.234 | 1.177 | 0.882 | 0.352 |
| home_rest_days | 7.312 | 7.025 | 7.107 | 0.287 |
| away_team_wins_last_5 | 1.667 | 1.833 | 1.883 | 0.216 |
| away_team_away_conceded_avg | 1.194 | 1.156 | 0.980 | 0.214 |
| home_team_home_win_rate | 0.467 | 0.427 | 0.322 | 0.145 |
| home_team_home_conceded_avg | 0.862 | 0.988 | 0.942 | 0.126 |
| away_team_away_win_rate | 0.234 | 0.278 | 0.272 | 0.045 |
| away_team_away_goals_avg | 0.931 | 0.943 | 0.926 | 0.016 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\segunda4\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\segunda4\charts\relationships_home_win_pct_by_position.png)

