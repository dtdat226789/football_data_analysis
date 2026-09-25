# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:47:23+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Prva liga (Slovenia)
- Scope: league `slovenia1`

- Matches analysed: **216** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_points_last_5 | 0.272 | -0.037 | 0.185 |
| home_team_wins_last_5 | 0.279 | -0.066 | 0.168 |
| home_position_before_match | -0.254 | 0.041 | -0.167 |
| home_team_goals_scored_last_5 | 0.227 | -0.028 | 0.156 |
| away_team_away_goals_avg | -0.038 | 0.213 | 0.132 |
| home_rest_days | 0.116 | 0.034 | 0.117 |
| home_points_before_match | 0.213 | -0.099 | 0.091 |
| home_team_home_goals_avg | 0.177 | -0.064 | 0.090 |
| position_difference | -0.303 | 0.199 | -0.086 |
| away_rest_days | 0.142 | -0.034 | 0.085 |
| points_difference | 0.350 | -0.254 | 0.080 |
| away_team_points_last_5 | -0.073 | 0.178 | 0.079 |
| away_team_away_win_rate | -0.064 | 0.165 | 0.076 |
| away_team_away_conceded_avg | 0.192 | -0.102 | 0.073 |
| away_team_goals_scored_last_5 | -0.028 | 0.123 | 0.072 |
| home_team_home_win_rate | 0.181 | -0.092 | 0.072 |
| away_team_wins_last_5 | -0.085 | 0.164 | 0.059 |
| away_position_before_match | 0.165 | -0.235 | -0.049 |
| home_team_goals_conceded_last_5 | -0.118 | 0.061 | -0.046 |
| away_points_before_match | -0.030 | 0.079 | 0.036 |
| rest_days_difference | -0.066 | 0.109 | 0.032 |
| home_team_home_conceded_avg | -0.060 | 0.058 | -0.003 |
| away_team_goals_conceded_last_5 | 0.187 | -0.193 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 34 | 9 | 7 | 18 | 26.5% | 20.6% | 52.9% |
| -4..-2 | 35 | 15 | 12 | 8 | 42.9% | 34.3% | 22.9% |
| -1..1 | 72 | 32 | 13 | 27 | 44.4% | 18.1% | 37.5% |
| 2..4 | 52 | 27 | 8 | 17 | 51.9% | 15.4% | 32.7% |
| >4 | 23 | 16 | 6 | 1 | 69.6% | 26.1% | 4.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 14 | 11 | 3 | 0 | 78.6% | 21.4% | 0.0% |
| -5..-2 | 62 | 32 | 14 | 16 | 51.6% | 22.6% | 25.8% |
| -1..1 | 57 | 29 | 6 | 22 | 50.9% | 10.5% | 38.6% |
| 2..5 | 62 | 23 | 20 | 19 | 37.1% | 32.3% | 30.6% |
| >=6 | 21 | 4 | 3 | 14 | 19.0% | 14.3% | 66.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 28 | 16 | 6 | 6 | 57.1% | 21.4% | 21.4% |
| -1..0 | 47 | 23 | 9 | 15 | 48.9% | 19.1% | 31.9% |
| 0 | 51 | 26 | 11 | 14 | 51.0% | 21.6% | 27.5% |
| 1..2 | 70 | 29 | 14 | 27 | 41.4% | 20.0% | 38.6% |
| >2 | 9 | 2 | 3 | 4 | 22.2% | 33.3% | 44.4% |
| unknown | 11 | 3 | 3 | 5 | 27.3% | 27.3% | 45.5% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.9%** home win (19/56)
- `>= 0.5` tier: **50.0%** home win (80/160)
- Home-win gap (>= split minus < split): **+16.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 56 | 19 | 16 | 21 | 33.9% |
| high | >= 0.5 | 160 | 80 | 30 | 50 | 50.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.293 | 0.087 | -4.944 | 8.237 |
| home_points_before_match | 22.364 | 15.543 | 16.183 | 6.820 |
| away_points_before_match | 19.071 | 15.457 | 21.127 | 5.670 |
| away_rest_days | 9.688 | 9.721 | 7.091 | 2.630 |
| position_difference | -1.020 | 0.348 | 1.479 | 2.499 |
| home_rest_days | 8.844 | 9.727 | 7.485 | 2.242 |
| away_team_goals_conceded_last_5 | 7.374 | 6.065 | 5.197 | 2.177 |
| away_position_before_match | 6.182 | 5.261 | 4.549 | 1.633 |
| home_team_points_last_5 | 6.384 | 5.935 | 5.113 | 1.271 |
| rest_days_difference | -0.844 | 0.116 | 0.394 | 1.238 |
| away_team_points_last_5 | 5.475 | 6.152 | 6.634 | 1.159 |
| home_team_goals_scored_last_5 | 6.778 | 6.130 | 5.817 | 0.961 |
| home_position_before_match | 5.162 | 5.609 | 6.028 | 0.867 |
| home_team_goals_conceded_last_5 | 6.172 | 6.283 | 6.958 | 0.786 |
| away_team_goals_scored_last_5 | 6.172 | 6.413 | 6.746 | 0.575 |
| home_team_wins_last_5 | 2.808 | 2.587 | 2.239 | 0.569 |
| away_team_wins_last_5 | 2.424 | 2.630 | 2.887 | 0.463 |
| away_team_away_conceded_avg | 1.521 | 1.263 | 1.212 | 0.309 |
| away_team_away_goals_avg | 1.227 | 1.382 | 1.513 | 0.286 |
| home_team_home_goals_avg | 1.493 | 1.358 | 1.302 | 0.191 |
| away_team_away_win_rate | 0.483 | 0.534 | 0.587 | 0.104 |
| home_team_home_win_rate | 0.623 | 0.565 | 0.539 | 0.084 |
| home_team_home_conceded_avg | 1.287 | 1.307 | 1.367 | 0.080 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\slovenia1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\slovenia1\charts\relationships_home_win_pct_by_position.png)

