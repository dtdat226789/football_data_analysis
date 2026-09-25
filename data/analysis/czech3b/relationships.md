# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:56:52+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 3. CFL - Group B (Czech Republic)
- Scope: league `czech3b`

- Matches analysed: **326** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_conceded_last_5 | -0.136 | 0.271 | 0.099 |
| home_team_goals_scored_last_5 | 0.163 | -0.056 | 0.087 |
| home_rest_days | -0.002 | -0.091 | -0.072 |
| away_rest_days | 0.005 | -0.089 | -0.065 |
| home_team_wins_last_5 | 0.043 | -0.125 | -0.061 |
| away_team_away_conceded_avg | -0.021 | -0.053 | -0.057 |
| home_team_home_goals_avg | 0.086 | -0.029 | 0.046 |
| away_team_away_win_rate | -0.077 | 0.137 | 0.043 |
| away_position_before_match | 0.188 | -0.143 | 0.040 |
| away_team_goals_scored_last_5 | -0.080 | 0.134 | 0.039 |
| home_team_points_last_5 | 0.109 | -0.163 | -0.037 |
| home_points_before_match | 0.133 | -0.093 | 0.035 |
| away_team_away_goals_avg | -0.095 | 0.140 | 0.031 |
| away_points_before_match | -0.077 | 0.118 | 0.028 |
| away_team_points_last_5 | -0.157 | 0.136 | -0.021 |
| home_position_before_match | -0.188 | 0.220 | 0.018 |
| home_team_home_win_rate | 0.082 | -0.108 | -0.017 |
| position_difference | -0.273 | 0.264 | -0.016 |
| rest_days_difference | -0.009 | -0.009 | -0.013 |
| away_team_goals_conceded_last_5 | 0.060 | -0.046 | 0.012 |
| away_team_wins_last_5 | -0.117 | 0.107 | -0.011 |
| home_team_home_conceded_avg | -0.161 | 0.182 | 0.011 |
| points_difference | 0.250 | -0.251 | 0.007 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 57 | 13 | 9 | 35 | 22.8% | 15.8% | 61.4% |
| -4..-2 | 68 | 21 | 19 | 28 | 30.9% | 27.9% | 41.2% |
| -1..1 | 90 | 42 | 23 | 25 | 46.7% | 25.6% | 27.8% |
| 2..4 | 56 | 30 | 14 | 12 | 53.6% | 25.0% | 21.4% |
| >4 | 55 | 34 | 11 | 10 | 61.8% | 20.0% | 18.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 66 | 42 | 15 | 9 | 63.6% | 22.7% | 13.6% |
| -5..-2 | 67 | 34 | 20 | 13 | 50.7% | 29.9% | 19.4% |
| -1..1 | 51 | 22 | 12 | 17 | 43.1% | 23.5% | 33.3% |
| 2..5 | 72 | 19 | 16 | 37 | 26.4% | 22.2% | 51.4% |
| >=6 | 70 | 23 | 13 | 34 | 32.9% | 18.6% | 48.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 38 | 15 | 12 | 11 | 39.5% | 31.6% | 28.9% |
| -1..0 | 53 | 20 | 11 | 22 | 37.7% | 20.8% | 41.5% |
| 0 | 116 | 50 | 34 | 32 | 43.1% | 29.3% | 27.6% |
| 1..2 | 63 | 25 | 13 | 25 | 39.7% | 20.6% | 39.7% |
| >2 | 39 | 21 | 3 | 15 | 53.8% | 7.7% | 38.5% |
| unknown | 17 | 9 | 3 | 5 | 52.9% | 17.6% | 29.4% |
- *17 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **42.7%** home win (44/103)
- `>= 0.5` tier: **43.0%** home win (96/223)
- Home-win gap (>= split minus < split): **+0.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 103 | 44 | 23 | 36 | 42.7% |
| high | >= 0.5 | 223 | 96 | 53 | 74 | 43.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.086 | 0.750 | -6.155 | 10.240 |
| away_points_before_match | 17.836 | 15.750 | 21.964 | 6.214 |
| home_points_before_match | 21.921 | 16.500 | 15.809 | 6.112 |
| home_rest_days | 11.863 | 6.541 | 8.714 | 5.322 |
| position_difference | -1.686 | -0.316 | 3.091 | 4.777 |
| rest_days_difference | 1.695 | -1.918 | 0.343 | 3.612 |
| away_position_before_match | 9.443 | 10.079 | 7.218 | 2.861 |
| home_position_before_match | 7.757 | 9.763 | 10.309 | 2.552 |
| home_team_goals_conceded_last_5 | 5.929 | 7.592 | 8.318 | 2.390 |
| away_team_points_last_5 | 5.464 | 5.132 | 7.236 | 2.105 |
| home_team_points_last_5 | 6.800 | 5.250 | 4.855 | 1.945 |
| away_team_goals_scored_last_5 | 7.000 | 6.211 | 8.036 | 1.826 |
| away_rest_days | 10.168 | 8.452 | 8.371 | 1.797 |
| away_team_goals_conceded_last_5 | 7.464 | 7.474 | 5.773 | 1.701 |
| home_team_goals_scored_last_5 | 7.686 | 6.461 | 6.227 | 1.458 |
| away_team_wins_last_5 | 2.521 | 2.368 | 2.945 | 0.577 |
| home_team_wins_last_5 | 2.843 | 2.434 | 2.345 | 0.497 |
| home_team_home_conceded_avg | 1.130 | 1.422 | 1.514 | 0.384 |
| away_team_away_conceded_avg | 1.676 | 1.855 | 1.540 | 0.315 |
| away_team_away_goals_avg | 1.268 | 1.194 | 1.471 | 0.276 |
| home_team_home_goals_avg | 1.693 | 1.663 | 1.584 | 0.108 |
| home_team_home_win_rate | 0.626 | 0.592 | 0.542 | 0.084 |
| away_team_away_win_rate | 0.472 | 0.469 | 0.550 | 0.080 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\czech3b\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\czech3b\charts\relationships_home_win_pct_by_position.png)

