# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:01:55+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Primavera 1 (Italy)
- Scope: league `italy19`

- Matches analysed: **432** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_win_rate | 0.107 | -0.019 | 0.066 |
| away_team_wins_last_5 | -0.083 | -0.006 | -0.064 |
| away_team_points_last_5 | -0.077 | -0.011 | -0.062 |
| away_team_goals_conceded_last_5 | 0.073 | 0.015 | 0.062 |
| away_team_away_win_rate | -0.068 | -0.008 | -0.054 |
| away_team_away_conceded_avg | 0.035 | 0.041 | 0.050 |
| home_team_goals_conceded_last_5 | -0.070 | 0.005 | -0.048 |
| home_position_before_match | -0.102 | 0.049 | -0.044 |
| home_points_before_match | 0.068 | -0.030 | 0.031 |
| position_difference | -0.118 | 0.097 | -0.027 |
| home_team_home_conceded_avg | -0.028 | -0.005 | -0.023 |
| home_team_goals_scored_last_5 | 0.030 | -0.073 | -0.022 |
| away_points_before_match | 0.006 | 0.029 | 0.022 |
| home_team_points_last_5 | 0.058 | -0.035 | 0.021 |
| home_team_wins_last_5 | 0.066 | -0.044 | 0.021 |
| away_rest_days | 0.014 | 0.017 | 0.020 |
| away_team_goals_scored_last_5 | 0.005 | 0.025 | 0.019 |
| home_rest_days | 0.009 | 0.021 | 0.019 |
| points_difference | 0.114 | -0.111 | 0.016 |
| home_team_home_goals_avg | 0.043 | -0.030 | 0.013 |
| away_team_away_goals_avg | -0.051 | 0.082 | 0.012 |
| away_position_before_match | 0.059 | -0.083 | -0.007 |
| rest_days_difference | -0.015 | 0.011 | -0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 59 | 27 | 15 | 17 | 45.8% | 25.4% | 28.8% |
| -4..-2 | 81 | 25 | 27 | 29 | 30.9% | 33.3% | 35.8% |
| -1..1 | 160 | 56 | 48 | 56 | 35.0% | 30.0% | 35.0% |
| 2..4 | 84 | 32 | 30 | 22 | 38.1% | 35.7% | 26.2% |
| >4 | 48 | 26 | 13 | 9 | 54.2% | 27.1% | 18.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 102 | 44 | 36 | 22 | 43.1% | 35.3% | 21.6% |
| -5..-2 | 85 | 42 | 20 | 23 | 49.4% | 23.5% | 27.1% |
| -1..1 | 65 | 25 | 17 | 23 | 38.5% | 26.2% | 35.4% |
| 2..5 | 70 | 19 | 27 | 24 | 27.1% | 38.6% | 34.3% |
| >=6 | 110 | 36 | 33 | 41 | 32.7% | 30.0% | 37.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 38 | 12 | 13 | 13 | 31.6% | 34.2% | 34.2% |
| -1..0 | 105 | 45 | 32 | 28 | 42.9% | 30.5% | 26.7% |
| 0 | 147 | 63 | 44 | 40 | 42.9% | 29.9% | 27.2% |
| 1..2 | 122 | 39 | 38 | 45 | 32.0% | 31.1% | 36.9% |
| >2 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 20 | 7 | 6 | 7 | 35.0% | 30.0% | 35.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **29.7%** home win (27/91)
- `>= 0.5` tier: **40.8%** home win (139/341)
- Home-win gap (>= split minus < split): **+11.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 91 | 27 | 29 | 35 | 29.7% |
| high | >= 0.5 | 341 | 139 | 104 | 98 | 40.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 23.687 | 23.301 | 20.135 | 3.551 |
| points_difference | 1.211 | -0.045 | -2.211 | 3.421 |
| position_difference | -1.042 | 0.075 | 1.662 | 2.704 |
| home_position_before_match | 10.217 | 10.481 | 11.955 | 1.738 |
| away_points_before_match | 22.476 | 23.346 | 22.346 | 1.000 |
| away_position_before_match | 11.259 | 10.406 | 10.293 | 0.966 |
| home_team_points_last_5 | 5.867 | 6.120 | 5.195 | 0.925 |
| home_team_goals_scored_last_5 | 6.133 | 6.105 | 5.444 | 0.689 |
| away_team_goals_scored_last_5 | 5.831 | 6.308 | 5.729 | 0.579 |
| away_team_points_last_5 | 5.699 | 6.150 | 5.857 | 0.452 |
| away_team_goals_conceded_last_5 | 5.976 | 6.015 | 5.586 | 0.429 |
| home_team_goals_conceded_last_5 | 5.741 | 6.090 | 6.128 | 0.387 |
| home_team_wins_last_5 | 2.904 | 2.887 | 2.549 | 0.355 |
| away_team_wins_last_5 | 2.759 | 2.977 | 2.820 | 0.218 |
| rest_days_difference | -0.151 | -0.071 | 0.008 | 0.159 |
| home_team_home_goals_avg | 1.373 | 1.284 | 1.218 | 0.155 |
| away_team_away_goals_avg | 1.030 | 1.166 | 1.166 | 0.135 |
| home_team_home_win_rate | 0.662 | 0.592 | 0.576 | 0.086 |
| home_rest_days | 7.233 | 7.236 | 7.317 | 0.085 |
| away_rest_days | 7.384 | 7.307 | 7.310 | 0.077 |
| away_team_away_win_rate | 0.524 | 0.575 | 0.539 | 0.050 |
| away_team_away_conceded_avg | 1.339 | 1.296 | 1.324 | 0.043 |
| home_team_home_conceded_avg | 1.098 | 1.135 | 1.108 | 0.036 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\italy19\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\italy19\charts\relationships_home_win_pct_by_position.png)

