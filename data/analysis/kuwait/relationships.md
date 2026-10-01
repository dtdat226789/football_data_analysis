# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:01:01+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premier League (Kuwait)
- Scope: league `kuwait`

- Matches analysed: **98** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.350 | 0.123 | -0.242 |
| home_team_home_conceded_avg | -0.257 | 0.036 | -0.212 |
| home_team_points_last_5 | 0.313 | -0.122 | 0.208 |
| home_team_home_win_rate | 0.301 | -0.114 | 0.203 |
| position_difference | -0.437 | 0.319 | -0.198 |
| points_difference | 0.395 | -0.267 | 0.193 |
| home_team_wins_last_5 | 0.293 | -0.126 | 0.188 |
| home_team_goals_conceded_last_5 | -0.272 | 0.119 | -0.173 |
| home_team_home_goals_avg | 0.299 | -0.169 | 0.167 |
| home_points_before_match | 0.235 | -0.087 | 0.160 |
| away_team_goals_conceded_last_5 | 0.304 | -0.198 | 0.152 |
| home_team_goals_scored_last_5 | 0.270 | -0.151 | 0.151 |
| rest_days_difference | -0.149 | 0.081 | -0.086 |
| away_team_away_conceded_avg | 0.217 | -0.189 | 0.079 |
| away_team_wins_last_5 | -0.192 | 0.208 | -0.045 |
| away_team_points_last_5 | -0.196 | 0.215 | -0.043 |
| away_team_away_win_rate | -0.001 | 0.051 | 0.032 |
| away_team_away_goals_avg | -0.029 | 0.082 | 0.025 |
| away_points_before_match | -0.060 | 0.112 | 0.016 |
| away_team_goals_scored_last_5 | -0.183 | 0.240 | -0.015 |
| away_rest_days | -0.107 | 0.178 | 0.011 |
| home_rest_days | -0.137 | 0.195 | -0.006 |
| away_position_before_match | 0.196 | -0.279 | 0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 14 | 3 | 0 | 11 | 21.4% | 0.0% | 78.6% |
| -4..-2 | 20 | 3 | 13 | 4 | 15.0% | 65.0% | 20.0% |
| -1..1 | 25 | 8 | 5 | 12 | 32.0% | 20.0% | 48.0% |
| 2..4 | 23 | 16 | 5 | 2 | 69.6% | 21.7% | 8.7% |
| >4 | 16 | 10 | 2 | 4 | 62.5% | 12.5% | 25.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 6 | 5 | 0 | 1 | 83.3% | 0.0% | 16.7% |
| -5..-2 | 32 | 18 | 9 | 5 | 56.2% | 28.1% | 15.6% |
| -1..1 | 28 | 10 | 5 | 13 | 35.7% | 17.9% | 46.4% |
| 2..5 | 28 | 6 | 9 | 13 | 21.4% | 32.1% | 46.4% |
| >=6 | 4 | 1 | 2 | 1 | 25.0% | 50.0% | 25.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 14 | 5 | 4 | 5 | 35.7% | 28.6% | 35.7% |
| -1..0 | 14 | 6 | 4 | 4 | 42.9% | 28.6% | 28.6% |
| 0 | 29 | 15 | 6 | 8 | 51.7% | 20.7% | 27.6% |
| 1..2 | 26 | 8 | 8 | 10 | 30.8% | 30.8% | 38.5% |
| >2 | 10 | 4 | 3 | 3 | 40.0% | 30.0% | 30.0% |
| unknown | 5 | 2 | 0 | 3 | 40.0% | 0.0% | 60.0% |
- *5 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.8%** home win (22/65)
- `>= 0.5` tier: **54.5%** home win (18/33)
- Home-win gap (>= split minus < split): **+20.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 65 | 22 | 17 | 26 | 33.8% |
| high | >= 0.5 | 33 | 18 | 8 | 7 | 54.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.400 | -2.560 | -2.182 | 6.960 |
| away_rest_days | 14.158 | 11.800 | 18.100 | 6.300 |
| home_points_before_match | 17.025 | 13.680 | 10.727 | 6.298 |
| home_rest_days | 13.763 | 12.440 | 18.433 | 5.993 |
| away_points_before_match | 12.625 | 16.240 | 12.909 | 3.615 |
| position_difference | -1.950 | 0.720 | 1.030 | 2.980 |
| home_team_goals_scored_last_5 | 7.350 | 5.640 | 4.545 | 2.805 |
| home_team_points_last_5 | 7.250 | 6.280 | 4.697 | 2.553 |
| away_team_goals_conceded_last_5 | 6.850 | 4.880 | 4.455 | 2.395 |
| away_team_points_last_5 | 4.675 | 6.680 | 6.121 | 2.005 |
| away_team_goals_scored_last_5 | 4.425 | 6.360 | 5.909 | 1.935 |
| home_team_goals_conceded_last_5 | 4.775 | 5.280 | 6.576 | 1.801 |
| home_position_before_match | 4.275 | 5.440 | 6.000 | 1.725 |
| away_position_before_match | 6.225 | 4.720 | 4.970 | 1.505 |
| rest_days_difference | -0.395 | 0.640 | 0.333 | 1.035 |
| home_team_wins_last_5 | 1.975 | 1.760 | 1.273 | 0.702 |
| home_team_home_goals_avg | 1.666 | 1.044 | 0.996 | 0.671 |
| away_team_away_conceded_avg | 1.493 | 0.973 | 0.937 | 0.556 |
| away_team_wins_last_5 | 1.275 | 1.800 | 1.667 | 0.525 |
| away_team_away_goals_avg | 0.943 | 1.336 | 0.993 | 0.393 |
| home_team_home_conceded_avg | 0.857 | 0.979 | 1.163 | 0.306 |
| home_team_home_win_rate | 0.437 | 0.328 | 0.262 | 0.176 |
| away_team_away_win_rate | 0.323 | 0.482 | 0.311 | 0.171 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\kuwait\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\kuwait\charts\relationships_home_win_pct_by_position.png)

