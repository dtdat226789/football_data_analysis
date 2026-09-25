# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:03:11+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premier League (Kuwait)
- Scope: league `kuwait`

- Matches analysed: **116** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | -0.212 | -0.026 | -0.201 |
| home_position_before_match | -0.284 | 0.101 | -0.184 |
| points_difference | 0.370 | -0.239 | 0.171 |
| home_team_goals_conceded_last_5 | -0.234 | 0.069 | -0.160 |
| position_difference | -0.376 | 0.265 | -0.160 |
| home_team_wins_last_5 | 0.231 | -0.132 | 0.118 |
| home_team_points_last_5 | 0.243 | -0.159 | 0.112 |
| home_team_home_goals_avg | 0.247 | -0.164 | 0.112 |
| home_team_home_win_rate | 0.183 | -0.086 | 0.105 |
| away_team_goals_conceded_last_5 | 0.260 | -0.213 | 0.092 |
| home_points_before_match | 0.187 | -0.115 | 0.090 |
| away_team_points_last_5 | -0.182 | 0.110 | -0.089 |
| home_team_goals_scored_last_5 | 0.225 | -0.170 | 0.089 |
| away_team_wins_last_5 | -0.164 | 0.100 | -0.080 |
| rest_days_difference | -0.130 | 0.090 | -0.060 |
| away_team_goals_scored_last_5 | -0.172 | 0.144 | -0.059 |
| away_team_away_conceded_avg | 0.191 | -0.202 | 0.039 |
| away_team_away_win_rate | -0.067 | 0.035 | -0.036 |
| away_points_before_match | -0.065 | 0.049 | -0.026 |
| away_team_away_goals_avg | -0.003 | 0.025 | 0.014 |
| away_position_before_match | 0.171 | -0.222 | 0.009 |
| home_rest_days | -0.134 | 0.184 | -0.007 |
| away_rest_days | -0.108 | 0.166 | 0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 14 | 3 | 0 | 11 | 21.4% | 0.0% | 78.6% |
| -4..-2 | 22 | 4 | 14 | 4 | 18.2% | 63.6% | 18.2% |
| -1..1 | 39 | 14 | 8 | 17 | 35.9% | 20.5% | 43.6% |
| 2..4 | 25 | 17 | 5 | 3 | 68.0% | 20.0% | 12.0% |
| >4 | 16 | 10 | 2 | 4 | 62.5% | 12.5% | 25.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 7 | 6 | 0 | 1 | 85.7% | 0.0% | 14.3% |
| -5..-2 | 34 | 19 | 9 | 6 | 55.9% | 26.5% | 17.6% |
| -1..1 | 38 | 13 | 8 | 17 | 34.2% | 21.1% | 44.7% |
| 2..5 | 31 | 8 | 9 | 14 | 25.8% | 29.0% | 45.2% |
| >=6 | 6 | 2 | 3 | 1 | 33.3% | 50.0% | 16.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 14 | 5 | 4 | 5 | 35.7% | 28.6% | 35.7% |
| -1..0 | 20 | 10 | 5 | 5 | 50.0% | 25.0% | 25.0% |
| 0 | 32 | 16 | 7 | 9 | 50.0% | 21.9% | 28.1% |
| 1..2 | 29 | 9 | 9 | 11 | 31.0% | 31.0% | 37.9% |
| >2 | 10 | 4 | 3 | 3 | 40.0% | 30.0% | 30.0% |
| unknown | 11 | 4 | 1 | 6 | 36.4% | 9.1% | 54.5% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **31.9%** home win (15/47)
- `>= 0.5` tier: **47.8%** home win (33/69)
- Home-win gap (>= split minus < split): **+15.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 47 | 15 | 13 | 19 | 31.9% |
| high | >= 0.5 | 69 | 33 | 16 | 20 | 47.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.646 | -2.310 | -1.795 | 5.956 |
| away_rest_days | 12.909 | 11.036 | 16.970 | 5.934 |
| home_rest_days | 12.523 | 11.607 | 17.273 | 5.666 |
| home_points_before_match | 14.458 | 11.931 | 9.256 | 5.202 |
| away_points_before_match | 10.812 | 14.241 | 11.051 | 3.429 |
| position_difference | -1.625 | 0.793 | 0.872 | 2.497 |
| home_team_goals_scored_last_5 | 6.438 | 5.103 | 4.026 | 2.412 |
| home_team_points_last_5 | 6.312 | 5.552 | 4.154 | 2.159 |
| away_team_goals_conceded_last_5 | 6.042 | 4.345 | 3.923 | 2.119 |
| away_team_points_last_5 | 4.188 | 6.000 | 5.308 | 1.812 |
| away_team_goals_scored_last_5 | 3.979 | 5.655 | 5.179 | 1.676 |
| away_position_before_match | 6.271 | 4.724 | 5.154 | 1.547 |
| home_team_goals_conceded_last_5 | 4.292 | 4.793 | 5.744 | 1.452 |
| home_position_before_match | 4.646 | 5.517 | 6.026 | 1.380 |
| rest_days_difference | -0.386 | 0.571 | 0.303 | 0.958 |
| home_team_wins_last_5 | 2.854 | 2.448 | 1.897 | 0.957 |
| away_team_wins_last_5 | 1.896 | 2.759 | 2.436 | 0.863 |
| home_team_home_goals_avg | 1.493 | 0.900 | 0.945 | 0.592 |
| away_team_away_conceded_avg | 1.390 | 0.873 | 0.818 | 0.571 |
| home_team_home_conceded_avg | 0.881 | 0.844 | 1.112 | 0.268 |
| away_team_away_goals_avg | 0.932 | 1.152 | 0.917 | 0.235 |
| home_team_home_win_rate | 0.589 | 0.467 | 0.432 | 0.157 |
| away_team_away_win_rate | 0.494 | 0.597 | 0.532 | 0.103 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\kuwait\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\kuwait\charts\relationships_home_win_pct_by_position.png)

