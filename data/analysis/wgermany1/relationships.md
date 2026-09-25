# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:51:18+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Bundesliga Women (Germany)
- Scope: league `wgermany1`

- Matches analysed: **217** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_win_rate | -0.002 | 0.245 | 0.202 |
| away_team_goals_scored_last_5 | -0.182 | 0.357 | 0.150 |
| away_position_before_match | 0.217 | -0.379 | -0.140 |
| away_team_away_goals_avg | -0.162 | 0.311 | 0.128 |
| away_team_points_last_5 | -0.186 | 0.306 | 0.105 |
| away_team_away_conceded_avg | 0.059 | -0.182 | -0.103 |
| away_team_wins_last_5 | -0.135 | 0.240 | 0.090 |
| home_team_home_goals_avg | 0.192 | -0.094 | 0.076 |
| rest_days_difference | -0.022 | -0.067 | -0.073 |
| position_difference | -0.399 | 0.470 | 0.070 |
| home_team_wins_last_5 | 0.168 | -0.089 | 0.061 |
| home_team_home_win_rate | 0.234 | -0.168 | 0.049 |
| home_team_points_last_5 | 0.205 | -0.140 | 0.049 |
| home_position_before_match | -0.324 | 0.257 | -0.047 |
| home_rest_days | 0.011 | -0.058 | -0.038 |
| home_team_home_conceded_avg | -0.178 | 0.209 | 0.030 |
| points_difference | 0.391 | -0.409 | -0.025 |
| away_rest_days | 0.029 | -0.001 | 0.023 |
| home_team_goals_scored_last_5 | 0.183 | -0.150 | 0.022 |
| away_team_goals_conceded_last_5 | 0.170 | -0.190 | -0.021 |
| away_points_before_match | -0.175 | 0.185 | 0.013 |
| home_points_before_match | 0.164 | -0.170 | -0.009 |
| home_team_goals_conceded_last_5 | -0.152 | 0.141 | -0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 42 | 7 | 6 | 29 | 16.7% | 14.3% | 69.0% |
| -4..-2 | 30 | 11 | 3 | 16 | 36.7% | 10.0% | 53.3% |
| -1..1 | 71 | 32 | 15 | 24 | 45.1% | 21.1% | 33.8% |
| 2..4 | 40 | 25 | 7 | 8 | 62.5% | 17.5% | 20.0% |
| >4 | 34 | 23 | 6 | 5 | 67.6% | 17.6% | 14.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 33 | 24 | 6 | 3 | 72.7% | 18.2% | 9.1% |
| -5..-2 | 49 | 31 | 9 | 9 | 63.3% | 18.4% | 18.4% |
| -1..1 | 50 | 26 | 8 | 16 | 52.0% | 16.0% | 32.0% |
| 2..5 | 53 | 15 | 11 | 27 | 28.3% | 20.8% | 50.9% |
| >=6 | 32 | 2 | 3 | 27 | 6.2% | 9.4% | 84.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 40 | 20 | 6 | 14 | 50.0% | 15.0% | 35.0% |
| -1..0 | 41 | 25 | 4 | 12 | 61.0% | 9.8% | 29.3% |
| 0 | 42 | 17 | 8 | 17 | 40.5% | 19.0% | 40.5% |
| 1..2 | 67 | 26 | 11 | 30 | 38.8% | 16.4% | 44.8% |
| >2 | 13 | 7 | 4 | 2 | 53.8% | 30.8% | 15.4% |
| unknown | 14 | 3 | 4 | 7 | 21.4% | 28.6% | 50.0% |
- *14 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **30.7%** home win (27/88)
- `>= 0.5` tier: **55.0%** home win (71/129)
- Home-win gap (>= split minus < split): **+24.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 88 | 27 | 16 | 45 | 30.7% |
| high | >= 0.5 | 129 | 71 | 21 | 37 | 55.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.959 | 1.459 | -7.610 | 12.569 |
| away_points_before_match | 12.735 | 13.811 | 19.598 | 6.863 |
| position_difference | -2.388 | -0.838 | 3.402 | 5.790 |
| home_points_before_match | 17.694 | 15.270 | 11.988 | 5.706 |
| away_position_before_match | 8.551 | 8.919 | 5.780 | 3.138 |
| home_position_before_match | 6.163 | 8.081 | 9.183 | 3.020 |
| away_team_goals_scored_last_5 | 5.857 | 5.973 | 8.768 | 2.911 |
| home_rest_days | 9.842 | 11.455 | 8.827 | 2.628 |
| away_team_points_last_5 | 4.959 | 4.892 | 7.037 | 2.145 |
| home_team_goals_scored_last_5 | 7.939 | 6.054 | 5.829 | 2.110 |
| home_team_points_last_5 | 6.643 | 5.270 | 4.695 | 1.948 |
| home_team_goals_conceded_last_5 | 6.112 | 7.027 | 7.927 | 1.815 |
| away_team_goals_conceded_last_5 | 7.500 | 7.405 | 5.756 | 1.744 |
| rest_days_difference | 0.411 | 0.818 | -0.533 | 1.352 |
| away_rest_days | 9.432 | 10.636 | 9.360 | 1.276 |
| away_team_away_goals_avg | 1.180 | 1.151 | 1.995 | 0.843 |
| home_team_home_conceded_avg | 1.129 | 1.498 | 1.818 | 0.689 |
| away_team_wins_last_5 | 2.184 | 2.189 | 2.768 | 0.585 |
| home_team_wins_last_5 | 2.643 | 2.135 | 2.085 | 0.557 |
| home_team_home_goals_avg | 1.679 | 1.539 | 1.259 | 0.420 |
| away_team_away_conceded_avg | 1.579 | 1.685 | 1.335 | 0.351 |
| home_team_home_win_rate | 0.637 | 0.535 | 0.438 | 0.199 |
| away_team_away_win_rate | 0.458 | 0.403 | 0.565 | 0.162 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\wgermany1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\wgermany1\charts\relationships_home_win_pct_by_position.png)

