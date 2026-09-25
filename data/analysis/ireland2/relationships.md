# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:01:36+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Division 1 (Ireland)
- Scope: league `ireland2`

- Matches analysed: **339** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_points_before_match | 0.297 | 0.103 | 0.312 |
| home_position_before_match | -0.293 | 0.047 | -0.211 |
| home_team_goals_scored_last_5 | 0.232 | 0.025 | 0.208 |
| points_difference | 0.346 | -0.142 | 0.193 |
| position_difference | -0.341 | 0.140 | -0.190 |
| home_team_points_last_5 | 0.224 | -0.001 | 0.185 |
| home_team_home_goals_avg | 0.235 | -0.021 | 0.180 |
| away_points_before_match | 0.020 | 0.219 | 0.160 |
| home_team_home_win_rate | 0.204 | -0.030 | 0.150 |
| home_team_wins_last_5 | 0.164 | -0.013 | 0.127 |
| away_team_goals_scored_last_5 | -0.020 | 0.176 | 0.099 |
| away_team_goals_conceded_last_5 | 0.107 | 0.012 | 0.096 |
| away_rest_days | -0.037 | 0.188 | 0.092 |
| home_rest_days | -0.052 | 0.171 | 0.068 |
| away_position_before_match | 0.187 | -0.150 | 0.056 |
| away_team_away_goals_avg | -0.072 | 0.010 | -0.053 |
| rest_days_difference | -0.032 | -0.037 | -0.051 |
| home_team_home_conceded_avg | -0.007 | -0.060 | -0.045 |
| away_team_away_win_rate | -0.066 | 0.020 | -0.041 |
| away_team_points_last_5 | -0.052 | 0.129 | 0.041 |
| away_team_away_conceded_avg | 0.102 | -0.085 | 0.029 |
| home_team_goals_conceded_last_5 | -0.048 | 0.032 | -0.019 |
| away_team_wins_last_5 | -0.028 | 0.049 | 0.009 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 63 | 22 | 17 | 24 | 34.9% | 27.0% | 38.1% |
| -4..-2 | 56 | 32 | 13 | 11 | 57.1% | 23.2% | 19.6% |
| -1..1 | 91 | 34 | 24 | 33 | 37.4% | 26.4% | 36.3% |
| 2..4 | 83 | 44 | 20 | 19 | 53.0% | 24.1% | 22.9% |
| >4 | 46 | 30 | 5 | 11 | 65.2% | 10.9% | 23.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 28 | 21 | 4 | 3 | 75.0% | 14.3% | 10.7% |
| -5..-2 | 109 | 62 | 22 | 25 | 56.9% | 20.2% | 22.9% |
| -1..1 | 68 | 30 | 17 | 21 | 44.1% | 25.0% | 30.9% |
| 2..5 | 102 | 43 | 23 | 36 | 42.2% | 22.5% | 35.3% |
| >=6 | 32 | 6 | 13 | 13 | 18.8% | 40.6% | 40.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 14 | 7 | 4 | 3 | 50.0% | 28.6% | 21.4% |
| -1..0 | 19 | 6 | 5 | 8 | 31.6% | 26.3% | 42.1% |
| 0 | 250 | 122 | 56 | 72 | 48.8% | 22.4% | 28.8% |
| 1..2 | 36 | 17 | 10 | 9 | 47.2% | 27.8% | 25.0% |
| >2 | 9 | 5 | 2 | 2 | 55.6% | 22.2% | 22.2% |
| unknown | 11 | 5 | 2 | 4 | 45.5% | 18.2% | 36.4% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.5%** home win (20/52)
- `>= 0.5` tier: **49.5%** home win (142/287)
- Home-win gap (>= split minus < split): **+11.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 52 | 20 | 14 | 18 | 38.5% |
| high | >= 0.5 | 287 | 142 | 65 | 80 | 49.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.463 | -2.430 | -3.908 | 7.371 |
| home_points_before_match | 25.444 | 19.038 | 21.031 | 6.406 |
| away_points_before_match | 21.981 | 21.468 | 24.939 | 3.470 |
| position_difference | -1.056 | 0.810 | 1.214 | 2.270 |
| home_position_before_match | 4.698 | 6.215 | 6.010 | 1.518 |
| home_team_points_last_5 | 6.778 | 5.418 | 5.857 | 1.360 |
| home_team_goals_scored_last_5 | 6.728 | 5.405 | 5.969 | 1.323 |
| away_position_before_match | 5.753 | 5.405 | 4.796 | 0.957 |
| away_team_goals_scored_last_5 | 5.877 | 6.684 | 6.429 | 0.807 |
| away_team_points_last_5 | 6.111 | 6.430 | 6.776 | 0.664 |
| away_team_goals_conceded_last_5 | 6.272 | 6.316 | 5.694 | 0.623 |
| home_rest_days | 6.758 | 7.359 | 7.117 | 0.601 |
| away_rest_days | 6.783 | 7.299 | 7.084 | 0.515 |
| home_team_wins_last_5 | 2.963 | 2.532 | 2.653 | 0.431 |
| home_team_goals_conceded_last_5 | 6.247 | 6.203 | 6.571 | 0.369 |
| away_team_away_goals_avg | 0.958 | 1.239 | 0.965 | 0.280 |
| home_team_home_goals_avg | 1.457 | 1.257 | 1.219 | 0.238 |
| away_team_away_conceded_avg | 1.375 | 1.447 | 1.235 | 0.212 |
| home_team_home_conceded_avg | 1.039 | 1.131 | 0.962 | 0.169 |
| home_team_home_win_rate | 0.695 | 0.634 | 0.598 | 0.098 |
| rest_days_difference | -0.025 | 0.065 | 0.032 | 0.090 |
| away_team_wins_last_5 | 2.864 | 2.810 | 2.898 | 0.088 |
| away_team_away_win_rate | 0.510 | 0.524 | 0.515 | 0.014 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\ireland2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\ireland2\charts\relationships_home_win_pct_by_position.png)

