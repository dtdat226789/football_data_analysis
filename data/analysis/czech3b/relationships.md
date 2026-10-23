# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:47:43+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 3. CFL - Group B (Czech Republic)
- Scope: league `czech3b`

- Matches analysed: **272** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_conceded_last_5 | -0.132 | 0.281 | 0.119 |
| home_team_points_last_5 | 0.123 | -0.231 | -0.087 |
| home_rest_days | -0.007 | -0.095 | -0.080 |
| away_rest_days | 0.003 | -0.093 | -0.071 |
| home_team_wins_last_5 | 0.144 | -0.227 | -0.068 |
| home_position_before_match | -0.162 | 0.240 | 0.064 |
| home_team_goals_scored_last_5 | 0.198 | -0.120 | 0.058 |
| away_team_goals_scored_last_5 | -0.030 | 0.087 | 0.045 |
| home_team_home_goals_avg | 0.137 | -0.077 | 0.045 |
| away_position_before_match | 0.198 | -0.140 | 0.043 |
| away_team_away_goals_avg | -0.069 | 0.120 | 0.041 |
| away_team_wins_last_5 | -0.160 | 0.106 | -0.040 |
| home_team_home_conceded_avg | -0.166 | 0.209 | 0.036 |
| away_team_points_last_5 | -0.145 | 0.101 | -0.033 |
| away_team_away_conceded_avg | 0.090 | -0.054 | 0.026 |
| away_team_goals_conceded_last_5 | 0.096 | -0.061 | 0.025 |
| away_team_away_win_rate | -0.116 | 0.136 | 0.017 |
| rest_days_difference | -0.012 | -0.009 | -0.016 |
| position_difference | -0.262 | 0.277 | 0.016 |
| away_points_before_match | -0.094 | 0.107 | 0.012 |
| home_points_before_match | 0.153 | -0.137 | 0.010 |
| home_team_home_win_rate | 0.162 | -0.169 | -0.008 |
| points_difference | 0.269 | -0.267 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 52 | 11 | 8 | 33 | 21.2% | 15.4% | 63.5% |
| -4..-2 | 55 | 18 | 14 | 23 | 32.7% | 25.5% | 41.8% |
| -1..1 | 69 | 35 | 16 | 18 | 50.7% | 23.2% | 26.1% |
| 2..4 | 47 | 27 | 11 | 9 | 57.4% | 23.4% | 19.1% |
| >4 | 49 | 29 | 11 | 9 | 59.2% | 22.4% | 18.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 57 | 36 | 14 | 7 | 63.2% | 24.6% | 12.3% |
| -5..-2 | 55 | 32 | 15 | 8 | 58.2% | 27.3% | 14.5% |
| -1..1 | 39 | 16 | 8 | 15 | 41.0% | 20.5% | 38.5% |
| 2..5 | 65 | 17 | 15 | 33 | 26.2% | 23.1% | 50.8% |
| >=6 | 56 | 19 | 8 | 29 | 33.9% | 14.3% | 51.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 33 | 14 | 11 | 8 | 42.4% | 33.3% | 24.2% |
| -1..0 | 44 | 18 | 8 | 18 | 40.9% | 18.2% | 40.9% |
| 0 | 99 | 44 | 26 | 29 | 44.4% | 26.3% | 29.3% |
| 1..2 | 55 | 23 | 11 | 21 | 41.8% | 20.0% | 38.2% |
| >2 | 32 | 18 | 2 | 12 | 56.2% | 6.2% | 37.5% |
| unknown | 9 | 3 | 2 | 4 | 33.3% | 22.2% | 44.4% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **35.0%** home win (57/163)
- `>= 0.5` tier: **57.8%** home win (63/109)
- Home-win gap (>= split minus < split): **+22.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 163 | 57 | 40 | 66 | 35.0% |
| high | >= 0.5 | 109 | 63 | 20 | 26 | 57.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.608 | 1.117 | -7.228 | 11.837 |
| home_points_before_match | 25.008 | 19.817 | 18.033 | 6.976 |
| away_points_before_match | 20.400 | 18.700 | 25.261 | 6.561 |
| home_rest_days | 12.308 | 6.305 | 8.898 | 6.003 |
| position_difference | -1.792 | -0.750 | 3.424 | 5.216 |
| rest_days_difference | 1.752 | -2.466 | 0.318 | 4.218 |
| away_position_before_match | 9.567 | 10.583 | 7.217 | 3.366 |
| home_position_before_match | 7.775 | 9.833 | 10.641 | 2.866 |
| home_team_goals_conceded_last_5 | 6.375 | 8.300 | 9.022 | 2.647 |
| away_team_points_last_5 | 5.992 | 5.250 | 7.717 | 2.467 |
| home_team_points_last_5 | 7.392 | 5.583 | 5.000 | 2.392 |
| away_team_goals_conceded_last_5 | 7.983 | 8.250 | 6.163 | 2.087 |
| away_team_goals_scored_last_5 | 7.783 | 6.383 | 8.457 | 2.073 |
| away_rest_days | 10.556 | 8.759 | 8.580 | 1.976 |
| home_team_goals_scored_last_5 | 8.317 | 7.033 | 6.543 | 1.773 |
| away_team_wins_last_5 | 1.625 | 1.400 | 2.315 | 0.915 |
| home_team_wins_last_5 | 2.158 | 1.500 | 1.293 | 0.865 |
| home_team_home_conceded_avg | 1.204 | 1.509 | 1.643 | 0.439 |
| away_team_away_goals_avg | 1.410 | 1.252 | 1.568 | 0.317 |
| away_team_away_conceded_avg | 1.783 | 1.811 | 1.534 | 0.276 |
| home_team_home_goals_avg | 1.803 | 1.698 | 1.583 | 0.220 |
| home_team_home_win_rate | 0.500 | 0.371 | 0.318 | 0.182 |
| away_team_away_win_rate | 0.315 | 0.243 | 0.419 | 0.176 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\czech3b\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\czech3b\charts\relationships_home_win_pct_by_position.png)

