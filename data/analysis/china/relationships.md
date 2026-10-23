# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:46:40+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super League (China)
- Scope: league `china`

- Matches analysed: **240** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_scored_last_5 | 0.005 | 0.232 | 0.173 |
| away_team_away_win_rate | -0.004 | 0.232 | 0.167 |
| away_position_before_match | 0.126 | -0.337 | -0.156 |
| home_team_home_goals_avg | 0.160 | 0.052 | 0.154 |
| away_team_away_goals_avg | -0.030 | 0.236 | 0.151 |
| away_team_points_last_5 | -0.048 | 0.247 | 0.146 |
| away_points_before_match | -0.022 | 0.215 | 0.141 |
| home_team_home_win_rate | 0.151 | 0.033 | 0.133 |
| away_team_wins_last_5 | -0.055 | 0.224 | 0.124 |
| away_team_away_conceded_avg | 0.060 | -0.189 | -0.095 |
| home_points_before_match | 0.173 | -0.051 | 0.087 |
| position_difference | -0.237 | 0.350 | 0.085 |
| home_team_goals_scored_last_5 | 0.172 | -0.080 | 0.066 |
| points_difference | 0.222 | -0.307 | -0.064 |
| home_team_home_conceded_avg | -0.001 | 0.081 | 0.059 |
| home_team_goals_conceded_last_5 | -0.025 | 0.083 | 0.042 |
| home_position_before_match | -0.200 | 0.142 | -0.040 |
| home_team_points_last_5 | 0.143 | -0.093 | 0.035 |
| home_team_wins_last_5 | 0.132 | -0.083 | 0.035 |
| away_team_goals_conceded_last_5 | 0.114 | -0.155 | -0.032 |
| rest_days_difference | 0.028 | -0.008 | 0.014 |
| away_rest_days | -0.026 | 0.010 | -0.011 |
| home_rest_days | -0.016 | 0.007 | -0.006 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 41 | 13 | 8 | 20 | 31.7% | 19.5% | 48.8% |
| -4..-2 | 43 | 15 | 12 | 16 | 34.9% | 27.9% | 37.2% |
| -1..1 | 77 | 32 | 26 | 19 | 41.6% | 33.8% | 24.7% |
| 2..4 | 51 | 34 | 8 | 9 | 66.7% | 15.7% | 17.6% |
| >4 | 28 | 18 | 8 | 2 | 64.3% | 28.6% | 7.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 45 | 30 | 10 | 5 | 66.7% | 22.2% | 11.1% |
| -5..-2 | 46 | 31 | 9 | 6 | 67.4% | 19.6% | 13.0% |
| -1..1 | 46 | 23 | 15 | 8 | 50.0% | 32.6% | 17.4% |
| 2..5 | 50 | 16 | 15 | 19 | 32.0% | 30.0% | 38.0% |
| >=6 | 53 | 12 | 13 | 28 | 22.6% | 24.5% | 52.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 19 | 11 | 3 | 5 | 57.9% | 15.8% | 26.3% |
| -1..0 | 51 | 25 | 10 | 16 | 49.0% | 19.6% | 31.4% |
| 0 | 90 | 42 | 19 | 29 | 46.7% | 21.1% | 32.2% |
| 1..2 | 56 | 22 | 22 | 12 | 39.3% | 39.3% | 21.4% |
| >2 | 16 | 9 | 4 | 3 | 56.2% | 25.0% | 18.8% |
| unknown | 8 | 3 | 4 | 1 | 37.5% | 50.0% | 12.5% |
- *8 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **42.1%** home win (53/126)
- `>= 0.5` tier: **51.8%** home win (59/114)
- Home-win gap (>= split minus < split): **+9.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 126 | 53 | 32 | 41 | 42.1% |
| high | >= 0.5 | 114 | 59 | 30 | 25 | 51.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.688 | -0.919 | -7.545 | 11.233 |
| away_points_before_match | 17.518 | 20.968 | 24.136 | 6.619 |
| position_difference | -2.125 | 0.677 | 3.955 | 6.080 |
| home_points_before_match | 21.205 | 20.048 | 16.591 | 4.614 |
| away_position_before_match | 10.027 | 7.952 | 6.439 | 3.587 |
| home_position_before_match | 7.902 | 8.629 | 10.394 | 2.492 |
| away_team_points_last_5 | 5.571 | 6.419 | 7.682 | 2.110 |
| away_team_goals_scored_last_5 | 6.670 | 7.129 | 8.591 | 1.921 |
| home_team_goals_scored_last_5 | 7.634 | 7.161 | 6.182 | 1.452 |
| home_team_points_last_5 | 6.411 | 6.226 | 5.045 | 1.365 |
| away_team_goals_conceded_last_5 | 7.732 | 6.452 | 6.409 | 1.323 |
| home_team_goals_conceded_last_5 | 7.286 | 6.984 | 8.045 | 1.062 |
| home_rest_days | 9.468 | 9.966 | 9.062 | 0.904 |
| away_team_wins_last_5 | 1.464 | 1.758 | 2.197 | 0.733 |
| rest_days_difference | 0.138 | 0.534 | -0.092 | 0.627 |
| away_team_away_goals_avg | 1.202 | 1.331 | 1.659 | 0.457 |
| home_team_wins_last_5 | 1.732 | 1.726 | 1.333 | 0.399 |
| away_rest_days | 9.330 | 9.431 | 9.154 | 0.277 |
| away_team_away_conceded_avg | 1.712 | 1.570 | 1.455 | 0.257 |
| home_team_home_conceded_avg | 1.284 | 1.279 | 1.408 | 0.129 |
| away_team_away_win_rate | 0.228 | 0.272 | 0.355 | 0.127 |
| home_team_home_goals_avg | 1.675 | 1.623 | 1.556 | 0.119 |
| home_team_home_win_rate | 0.438 | 0.435 | 0.388 | 0.050 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\china\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\china\charts\relationships_home_win_pct_by_position.png)

