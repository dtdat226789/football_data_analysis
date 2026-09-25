# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:58:10+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Meistriliiga (Estonia)
- Scope: league `estonia`

- Matches analysed: **325** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| points_difference | 0.398 | -0.359 | 0.100 |
| away_team_away_goals_avg | -0.252 | 0.190 | -0.091 |
| away_team_away_win_rate | -0.291 | 0.247 | -0.085 |
| rest_days_difference | -0.091 | 0.002 | -0.083 |
| away_team_wins_last_5 | -0.290 | 0.253 | -0.080 |
| position_difference | -0.392 | 0.383 | -0.076 |
| away_team_away_conceded_avg | 0.257 | -0.229 | 0.067 |
| away_team_goals_conceded_last_5 | 0.273 | -0.254 | 0.062 |
| away_position_before_match | 0.323 | -0.319 | 0.060 |
| home_team_home_conceded_avg | -0.228 | 0.209 | -0.054 |
| home_position_before_match | -0.243 | 0.234 | -0.050 |
| away_team_points_last_5 | -0.272 | 0.271 | -0.049 |
| away_points_before_match | -0.213 | 0.200 | -0.047 |
| home_points_before_match | 0.150 | -0.127 | 0.044 |
| away_rest_days | 0.017 | 0.036 | 0.044 |
| away_team_goals_scored_last_5 | -0.219 | 0.228 | -0.032 |
| home_team_home_goals_avg | 0.067 | -0.063 | 0.015 |
| home_team_goals_scored_last_5 | 0.085 | -0.121 | -0.012 |
| home_team_points_last_5 | 0.112 | -0.153 | -0.012 |
| home_team_goals_conceded_last_5 | -0.167 | 0.193 | -0.011 |
| home_team_wins_last_5 | 0.138 | -0.157 | 0.011 |
| home_rest_days | -0.043 | 0.039 | -0.010 |
| home_team_home_win_rate | 0.139 | -0.161 | 0.008 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 55 | 13 | 6 | 36 | 23.6% | 10.9% | 65.5% |
| -4..-2 | 62 | 21 | 8 | 33 | 33.9% | 12.9% | 53.2% |
| -1..1 | 85 | 39 | 11 | 35 | 45.9% | 12.9% | 41.2% |
| 2..4 | 59 | 32 | 13 | 14 | 54.2% | 22.0% | 23.7% |
| >4 | 64 | 46 | 4 | 14 | 71.9% | 6.2% | 21.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 32 | 26 | 1 | 5 | 81.2% | 3.1% | 15.6% |
| -5..-2 | 98 | 61 | 12 | 25 | 62.2% | 12.2% | 25.5% |
| -1..1 | 72 | 31 | 14 | 27 | 43.1% | 19.4% | 37.5% |
| 2..5 | 92 | 29 | 11 | 52 | 31.5% | 12.0% | 56.5% |
| >=6 | 31 | 4 | 4 | 23 | 12.9% | 12.9% | 74.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 33 | 19 | 5 | 9 | 57.6% | 15.2% | 27.3% |
| -1..0 | 69 | 35 | 8 | 26 | 50.7% | 11.6% | 37.7% |
| 0 | 103 | 51 | 16 | 36 | 49.5% | 15.5% | 35.0% |
| 1..2 | 90 | 35 | 9 | 46 | 38.9% | 10.0% | 51.1% |
| >2 | 20 | 7 | 3 | 10 | 35.0% | 15.0% | 50.0% |
| unknown | 10 | 4 | 1 | 5 | 40.0% | 10.0% | 50.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.1%** home win (46/124)
- `>= 0.5` tier: **52.2%** home win (105/201)
- Home-win gap (>= split minus < split): **+15.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 124 | 46 | 18 | 60 | 37.1% |
| high | >= 0.5 | 201 | 105 | 24 | 72 | 52.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 6.808 | -4.595 | -7.205 | 14.012 |
| away_points_before_match | 18.225 | 28.976 | 27.061 | 10.751 |
| home_points_before_match | 25.033 | 24.381 | 19.856 | 5.177 |
| position_difference | -1.801 | 0.429 | 1.826 | 3.627 |
| away_team_goals_conceded_last_5 | 8.503 | 7.333 | 5.530 | 2.973 |
| away_team_points_last_5 | 5.199 | 6.833 | 7.848 | 2.650 |
| away_position_before_match | 6.742 | 5.095 | 4.409 | 2.333 |
| away_team_goals_scored_last_5 | 6.066 | 7.667 | 8.371 | 2.305 |
| away_rest_days | 6.959 | 8.195 | 6.850 | 1.345 |
| home_team_goals_conceded_last_5 | 6.636 | 6.667 | 7.947 | 1.311 |
| home_position_before_match | 4.940 | 5.524 | 6.235 | 1.294 |
| home_team_points_last_5 | 7.073 | 6.690 | 6.023 | 1.050 |
| home_rest_days | 6.864 | 7.854 | 7.228 | 0.990 |
| away_team_wins_last_5 | 2.099 | 2.595 | 3.030 | 0.931 |
| home_team_goals_scored_last_5 | 7.583 | 6.690 | 6.780 | 0.892 |
| rest_days_difference | -0.095 | -0.341 | 0.378 | 0.719 |
| away_team_away_conceded_avg | 1.955 | 1.674 | 1.320 | 0.635 |
| home_team_wins_last_5 | 2.755 | 2.595 | 2.326 | 0.429 |
| away_team_away_goals_avg | 1.106 | 1.502 | 1.508 | 0.402 |
| home_team_home_conceded_avg | 1.170 | 1.234 | 1.495 | 0.326 |
| away_team_away_win_rate | 0.405 | 0.543 | 0.594 | 0.189 |
| home_team_home_goals_avg | 1.735 | 1.569 | 1.641 | 0.166 |
| home_team_home_win_rate | 0.574 | 0.572 | 0.501 | 0.074 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\estonia\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\estonia\charts\relationships_home_win_pct_by_position.png)

