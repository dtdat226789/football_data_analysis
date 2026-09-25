# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:02:23+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie C - Group B (Italy)
- Scope: league `italy3b`

- Matches analysed: **417** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.112 | -0.013 | 0.070 |
| away_team_away_win_rate | -0.165 | 0.070 | -0.068 |
| home_team_home_goals_avg | 0.074 | 0.022 | 0.067 |
| away_position_before_match | 0.164 | -0.077 | 0.062 |
| home_team_home_win_rate | 0.060 | 0.019 | 0.055 |
| home_team_points_last_5 | 0.107 | -0.037 | 0.051 |
| points_difference | 0.235 | -0.174 | 0.048 |
| position_difference | -0.234 | 0.174 | -0.047 |
| rest_days_difference | 0.021 | 0.045 | 0.045 |
| away_team_away_goals_avg | -0.145 | 0.084 | -0.045 |
| home_team_goals_scored_last_5 | 0.077 | -0.018 | 0.042 |
| home_team_home_conceded_avg | -0.046 | 0.107 | 0.041 |
| away_points_before_match | -0.131 | 0.077 | -0.040 |
| home_team_wins_last_5 | 0.048 | -0.001 | 0.033 |
| away_team_goals_conceded_last_5 | 0.075 | -0.040 | 0.026 |
| away_rest_days | -0.018 | -0.015 | -0.023 |
| away_team_points_last_5 | -0.145 | 0.119 | -0.021 |
| away_team_wins_last_5 | -0.113 | 0.087 | -0.020 |
| away_team_goals_scored_last_5 | -0.115 | 0.094 | -0.017 |
| home_rest_days | -0.002 | 0.026 | 0.017 |
| home_points_before_match | 0.027 | -0.040 | -0.008 |
| home_team_goals_conceded_last_5 | -0.094 | 0.101 | 0.002 |
| home_position_before_match | -0.159 | 0.163 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 59 | 15 | 19 | 25 | 25.4% | 32.2% | 42.4% |
| -4..-2 | 90 | 27 | 29 | 34 | 30.0% | 32.2% | 37.8% |
| -1..1 | 132 | 57 | 39 | 36 | 43.2% | 29.5% | 27.3% |
| 2..4 | 86 | 31 | 31 | 24 | 36.0% | 36.0% | 27.9% |
| >4 | 50 | 33 | 13 | 4 | 66.0% | 26.0% | 8.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 98 | 57 | 28 | 13 | 58.2% | 28.6% | 13.3% |
| -5..-2 | 66 | 22 | 23 | 21 | 33.3% | 34.8% | 31.8% |
| -1..1 | 72 | 29 | 27 | 16 | 40.3% | 37.5% | 22.2% |
| 2..5 | 66 | 28 | 17 | 21 | 42.4% | 25.8% | 31.8% |
| >=6 | 115 | 27 | 36 | 52 | 23.5% | 31.3% | 45.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 43 | 16 | 14 | 13 | 37.2% | 32.6% | 30.2% |
| -1..0 | 77 | 32 | 23 | 22 | 41.6% | 29.9% | 28.6% |
| 0 | 172 | 71 | 48 | 53 | 41.3% | 27.9% | 30.8% |
| 1..2 | 94 | 31 | 34 | 29 | 33.0% | 36.2% | 30.9% |
| >2 | 11 | 2 | 4 | 5 | 18.2% | 36.4% | 45.5% |
| unknown | 20 | 11 | 8 | 1 | 55.0% | 40.0% | 5.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **40.5%** home win (34/84)
- `>= 0.5` tier: **38.7%** home win (129/333)
- Home-win gap (>= split minus < split): **-1.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 84 | 34 | 26 | 24 | 40.5% |
| high | >= 0.5 | 333 | 129 | 105 | 99 | 38.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.258 | -0.267 | -4.683 | 7.941 |
| away_points_before_match | 18.828 | 21.313 | 24.260 | 5.432 |
| position_difference | -1.890 | 0.481 | 3.415 | 5.304 |
| home_position_before_match | 9.092 | 10.809 | 12.358 | 3.266 |
| home_points_before_match | 22.086 | 21.046 | 19.577 | 2.509 |
| away_position_before_match | 10.982 | 10.328 | 8.943 | 2.039 |
| away_team_points_last_5 | 5.221 | 5.702 | 6.813 | 1.592 |
| away_team_goals_scored_last_5 | 4.454 | 4.649 | 5.602 | 1.148 |
| home_team_goals_conceded_last_5 | 4.423 | 4.924 | 5.480 | 1.056 |
| home_team_points_last_5 | 6.160 | 5.435 | 5.309 | 0.851 |
| home_team_goals_scored_last_5 | 5.092 | 4.641 | 4.789 | 0.451 |
| away_team_wins_last_5 | 2.656 | 2.817 | 3.106 | 0.449 |
| away_team_goals_conceded_last_5 | 4.896 | 4.832 | 4.610 | 0.286 |
| away_team_away_goals_avg | 0.857 | 0.970 | 1.084 | 0.227 |
| away_rest_days | 6.743 | 6.967 | 6.746 | 0.224 |
| rest_days_difference | -0.211 | -0.268 | -0.082 | 0.186 |
| home_team_wins_last_5 | 2.908 | 2.733 | 2.772 | 0.175 |
| home_rest_days | 6.533 | 6.699 | 6.664 | 0.166 |
| home_team_home_conceded_avg | 0.902 | 0.888 | 1.046 | 0.158 |
| away_team_away_conceded_avg | 1.128 | 1.082 | 0.988 | 0.140 |
| home_team_home_goals_avg | 1.153 | 1.014 | 1.053 | 0.139 |
| away_team_away_win_rate | 0.500 | 0.532 | 0.622 | 0.121 |
| home_team_home_win_rate | 0.652 | 0.633 | 0.637 | 0.019 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\italy3b\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\italy3b\charts\relationships_home_win_pct_by_position.png)

