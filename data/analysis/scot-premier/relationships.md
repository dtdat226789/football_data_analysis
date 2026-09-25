# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:44:41+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premiership (Scotland)
- Scope: league `scot-premier`

- Matches analysed: **276** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_points_before_match | 0.070 | 0.141 | 0.153 |
| home_points_before_match | 0.228 | -0.064 | 0.121 |
| away_position_before_match | 0.076 | -0.200 | -0.087 |
| home_position_before_match | -0.233 | 0.146 | -0.067 |
| away_team_goals_scored_last_5 | 0.016 | 0.059 | 0.054 |
| home_team_home_goals_avg | 0.123 | -0.052 | 0.053 |
| home_team_goals_conceded_last_5 | -0.071 | 0.147 | 0.053 |
| away_team_away_win_rate | -0.019 | 0.092 | 0.052 |
| home_team_goals_scored_last_5 | 0.145 | -0.081 | 0.049 |
| points_difference | 0.220 | -0.290 | -0.045 |
| away_team_wins_last_5 | -0.006 | 0.049 | 0.030 |
| away_team_away_conceded_avg | 0.032 | -0.072 | -0.028 |
| home_team_home_win_rate | 0.142 | -0.109 | 0.026 |
| away_team_points_last_5 | -0.048 | 0.084 | 0.025 |
| home_team_home_conceded_avg | -0.132 | 0.103 | -0.023 |
| away_team_goals_conceded_last_5 | 0.138 | -0.111 | 0.022 |
| home_rest_days | -0.029 | 0.058 | 0.020 |
| away_rest_days | -0.041 | 0.070 | 0.020 |
| position_difference | -0.242 | 0.268 | 0.014 |
| home_team_wins_last_5 | 0.182 | -0.170 | 0.013 |
| home_team_points_last_5 | 0.187 | -0.183 | 0.007 |
| away_team_away_goals_avg | -0.068 | 0.068 | -0.002 |
| rest_days_difference | 0.015 | -0.018 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 48 | 8 | 14 | 26 | 16.7% | 29.2% | 54.2% |
| -4..-2 | 48 | 22 | 11 | 15 | 45.8% | 22.9% | 31.2% |
| -1..1 | 85 | 39 | 24 | 22 | 45.9% | 28.2% | 25.9% |
| 2..4 | 52 | 25 | 15 | 12 | 48.1% | 28.8% | 23.1% |
| >4 | 43 | 27 | 9 | 7 | 62.8% | 20.9% | 16.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 35 | 25 | 7 | 3 | 71.4% | 20.0% | 8.6% |
| -5..-2 | 71 | 35 | 17 | 19 | 49.3% | 23.9% | 26.8% |
| -1..1 | 64 | 33 | 17 | 14 | 51.6% | 26.6% | 21.9% |
| 2..5 | 72 | 21 | 23 | 28 | 29.2% | 31.9% | 38.9% |
| >=6 | 34 | 7 | 9 | 18 | 20.6% | 26.5% | 52.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 22 | 8 | 5 | 9 | 36.4% | 22.7% | 40.9% |
| -1..0 | 50 | 22 | 14 | 14 | 44.0% | 28.0% | 28.0% |
| 0 | 114 | 51 | 29 | 34 | 44.7% | 25.4% | 29.8% |
| 1..2 | 52 | 20 | 13 | 19 | 38.5% | 25.0% | 36.5% |
| >2 | 24 | 14 | 7 | 3 | 58.3% | 29.2% | 12.5% |
| unknown | 14 | 6 | 5 | 3 | 42.9% | 35.7% | 21.4% |
- *14 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **30.3%** home win (20/66)
- `>= 0.5` tier: **48.1%** home win (101/210)
- Home-win gap (>= split minus < split): **+17.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 66 | 20 | 23 | 23 | 30.3% |
| high | >= 0.5 | 210 | 101 | 50 | 59 | 48.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 26.438 | 15.685 | 18.854 | 10.753 |
| points_difference | 4.736 | -2.247 | -5.220 | 9.955 |
| away_points_before_match | 21.702 | 17.932 | 24.073 | 6.142 |
| position_difference | -1.545 | 0.534 | 1.927 | 3.472 |
| home_team_points_last_5 | 6.876 | 4.973 | 4.829 | 2.047 |
| home_position_before_match | 5.653 | 7.452 | 7.622 | 1.969 |
| away_position_before_match | 7.198 | 6.918 | 5.695 | 1.503 |
| home_team_goals_scored_last_5 | 6.397 | 5.000 | 5.427 | 1.397 |
| home_team_goals_conceded_last_5 | 5.446 | 5.808 | 6.780 | 1.334 |
| away_rest_days | 7.200 | 7.456 | 8.468 | 1.268 |
| away_team_points_last_5 | 5.901 | 5.329 | 6.573 | 1.244 |
| away_team_goals_conceded_last_5 | 6.314 | 5.493 | 5.220 | 1.095 |
| away_team_goals_scored_last_5 | 6.008 | 5.466 | 6.354 | 0.888 |
| home_team_wins_last_5 | 3.091 | 2.370 | 2.317 | 0.774 |
| rest_days_difference | 0.330 | 0.471 | -0.304 | 0.774 |
| home_rest_days | 7.530 | 7.870 | 8.165 | 0.634 |
| away_team_wins_last_5 | 2.826 | 2.534 | 2.866 | 0.332 |
| home_team_home_conceded_avg | 0.963 | 1.111 | 1.230 | 0.267 |
| home_team_home_goals_avg | 1.422 | 1.175 | 1.290 | 0.248 |
| away_team_away_goals_avg | 0.990 | 1.104 | 1.190 | 0.200 |
| home_team_home_win_rate | 0.694 | 0.577 | 0.602 | 0.118 |
| away_team_away_conceded_avg | 1.363 | 1.288 | 1.268 | 0.095 |
| away_team_away_win_rate | 0.542 | 0.550 | 0.604 | 0.062 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\scot-premier\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\scot-premier\charts\relationships_home_win_pct_by_position.png)

