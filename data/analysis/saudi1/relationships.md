# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:05:24+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Saudi Professional League (Saudi Arabia)
- Scope: league `saudi1`

- Matches analysed: **314** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_position_before_match | 0.235 | -0.345 | -0.100 |
| away_team_goals_conceded_last_5 | 0.103 | -0.212 | -0.092 |
| home_team_goals_conceded_last_5 | -0.219 | 0.095 | -0.085 |
| home_team_home_win_rate | 0.274 | -0.149 | 0.083 |
| away_team_away_conceded_avg | 0.096 | -0.176 | -0.069 |
| away_points_before_match | -0.156 | 0.225 | 0.064 |
| home_team_wins_last_5 | 0.277 | -0.178 | 0.062 |
| away_team_away_win_rate | -0.192 | 0.253 | 0.060 |
| points_difference | 0.371 | -0.415 | -0.057 |
| away_team_wins_last_5 | -0.201 | 0.256 | 0.056 |
| away_team_points_last_5 | -0.204 | 0.257 | 0.054 |
| home_team_home_conceded_avg | -0.150 | 0.074 | -0.051 |
| position_difference | -0.397 | 0.429 | 0.048 |
| away_team_goals_scored_last_5 | -0.221 | 0.255 | 0.040 |
| home_team_points_last_5 | 0.258 | -0.193 | 0.036 |
| home_position_before_match | -0.319 | 0.252 | -0.034 |
| away_team_away_goals_avg | -0.215 | 0.227 | 0.021 |
| home_team_home_goals_avg | 0.206 | -0.168 | 0.018 |
| home_team_goals_scored_last_5 | 0.204 | -0.209 | -0.015 |
| rest_days_difference | 0.044 | -0.024 | 0.014 |
| home_rest_days | 0.075 | -0.056 | 0.011 |
| home_points_before_match | 0.202 | -0.173 | 0.011 |
| away_rest_days | 0.060 | -0.049 | 0.007 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 59 | 14 | 6 | 39 | 23.7% | 10.2% | 66.1% |
| -4..-2 | 60 | 19 | 17 | 24 | 31.7% | 28.3% | 40.0% |
| -1..1 | 85 | 31 | 25 | 29 | 36.5% | 29.4% | 34.1% |
| 2..4 | 59 | 34 | 16 | 9 | 57.6% | 27.1% | 15.3% |
| >4 | 51 | 41 | 8 | 2 | 80.4% | 15.7% | 3.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 74 | 54 | 15 | 5 | 73.0% | 20.3% | 6.8% |
| -5..-2 | 62 | 33 | 14 | 15 | 53.2% | 22.6% | 24.2% |
| -1..1 | 41 | 16 | 13 | 12 | 39.0% | 31.7% | 29.3% |
| 2..5 | 62 | 24 | 19 | 19 | 38.7% | 30.6% | 30.6% |
| >=6 | 75 | 12 | 11 | 52 | 16.0% | 14.7% | 69.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 44 | 22 | 8 | 14 | 50.0% | 18.2% | 31.8% |
| -1..0 | 68 | 37 | 14 | 17 | 54.4% | 20.6% | 25.0% |
| 0 | 88 | 31 | 24 | 33 | 35.2% | 27.3% | 37.5% |
| 1..2 | 93 | 37 | 23 | 33 | 39.8% | 24.7% | 35.5% |
| >2 | 11 | 7 | 2 | 2 | 63.6% | 18.2% | 18.2% |
| unknown | 10 | 5 | 1 | 4 | 50.0% | 10.0% | 40.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **36.7%** home win (73/199)
- `>= 0.5` tier: **57.4%** home win (66/115)
- Home-win gap (>= split minus < split): **+20.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 199 | 73 | 47 | 79 | 36.7% |
| high | >= 0.5 | 115 | 66 | 25 | 24 | 57.4% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 7.612 | 0.306 | -11.796 | 19.408 |
| home_points_before_match | 26.957 | 22.111 | 16.738 | 10.219 |
| away_points_before_match | 19.345 | 21.806 | 28.534 | 9.189 |
| position_difference | -3.482 | -0.361 | 5.252 | 8.734 |
| away_position_before_match | 11.676 | 10.694 | 7.165 | 4.511 |
| home_position_before_match | 8.194 | 10.333 | 12.417 | 4.223 |
| away_team_points_last_5 | 5.331 | 5.722 | 8.398 | 3.067 |
| away_team_goals_scored_last_5 | 5.849 | 6.750 | 8.641 | 2.792 |
| home_team_points_last_5 | 7.309 | 5.917 | 4.825 | 2.484 |
| away_team_goals_conceded_last_5 | 7.281 | 7.778 | 5.427 | 2.351 |
| home_team_goals_scored_last_5 | 7.748 | 6.542 | 5.524 | 2.224 |
| home_team_goals_conceded_last_5 | 6.187 | 7.208 | 7.738 | 1.551 |
| home_rest_days | 8.604 | 8.437 | 7.091 | 1.514 |
| away_rest_days | 8.582 | 8.169 | 7.303 | 1.279 |
| away_team_wins_last_5 | 1.403 | 1.583 | 2.476 | 1.073 |
| home_team_wins_last_5 | 2.115 | 1.583 | 1.252 | 0.863 |
| away_team_away_goals_avg | 1.133 | 1.313 | 1.759 | 0.627 |
| rest_days_difference | 0.022 | 0.268 | -0.212 | 0.480 |
| away_team_away_conceded_avg | 1.604 | 1.576 | 1.273 | 0.332 |
| home_team_home_goals_avg | 1.627 | 1.469 | 1.308 | 0.319 |
| home_team_home_conceded_avg | 1.269 | 1.337 | 1.504 | 0.235 |
| away_team_away_win_rate | 0.251 | 0.291 | 0.466 | 0.214 |
| home_team_home_win_rate | 0.452 | 0.416 | 0.309 | 0.143 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\saudi1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\saudi1\charts\relationships_home_win_pct_by_position.png)

