# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:51:37+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Allsvenskan Women (Sweden)
- Scope: league `wsweden`

- Matches analysed: **315** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_goals_avg | 0.230 | -0.128 | 0.096 |
| home_team_goals_conceded_last_5 | -0.162 | 0.272 | 0.083 |
| home_team_wins_last_5 | 0.095 | -0.182 | -0.068 |
| away_team_away_conceded_avg | 0.234 | -0.174 | 0.061 |
| away_team_goals_conceded_last_5 | 0.207 | -0.147 | 0.060 |
| home_points_before_match | 0.135 | -0.082 | 0.050 |
| rest_days_difference | -0.015 | 0.071 | 0.046 |
| home_team_goals_scored_last_5 | 0.153 | -0.108 | 0.045 |
| away_points_before_match | -0.242 | 0.308 | 0.043 |
| home_rest_days | 0.111 | -0.071 | 0.038 |
| home_team_points_last_5 | 0.111 | -0.164 | -0.038 |
| away_position_before_match | 0.291 | -0.264 | 0.037 |
| home_team_home_conceded_avg | -0.099 | 0.141 | 0.031 |
| away_team_away_win_rate | -0.246 | 0.227 | -0.028 |
| home_position_before_match | -0.262 | 0.309 | 0.026 |
| home_team_home_win_rate | 0.096 | -0.076 | 0.022 |
| away_team_wins_last_5 | -0.242 | 0.240 | -0.014 |
| away_team_points_last_5 | -0.278 | 0.281 | -0.012 |
| away_rest_days | 0.117 | -0.110 | 0.012 |
| points_difference | 0.424 | -0.439 | 0.009 |
| away_team_goals_scored_last_5 | -0.273 | 0.299 | 0.008 |
| position_difference | -0.412 | 0.427 | -0.008 |
| away_team_away_goals_avg | -0.233 | 0.254 | 0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 59 | 14 | 10 | 35 | 23.7% | 16.9% | 59.3% |
| -4..-2 | 63 | 19 | 9 | 35 | 30.2% | 14.3% | 55.6% |
| -1..1 | 85 | 44 | 15 | 26 | 51.8% | 17.6% | 30.6% |
| 2..4 | 49 | 30 | 8 | 11 | 61.2% | 16.3% | 22.4% |
| >4 | 59 | 38 | 10 | 11 | 64.4% | 16.9% | 18.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 46 | 38 | 5 | 3 | 82.6% | 10.9% | 6.5% |
| -5..-2 | 72 | 39 | 15 | 18 | 54.2% | 20.8% | 25.0% |
| -1..1 | 63 | 36 | 7 | 20 | 57.1% | 11.1% | 31.7% |
| 2..5 | 77 | 25 | 14 | 38 | 32.5% | 18.2% | 49.4% |
| >=6 | 57 | 7 | 11 | 39 | 12.3% | 19.3% | 68.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 29 | 17 | 3 | 9 | 58.6% | 10.3% | 31.0% |
| -1..0 | 64 | 27 | 10 | 27 | 42.2% | 15.6% | 42.2% |
| 0 | 103 | 53 | 16 | 34 | 51.5% | 15.5% | 33.0% |
| 1..2 | 81 | 28 | 17 | 36 | 34.6% | 21.0% | 44.4% |
| >2 | 24 | 9 | 5 | 10 | 37.5% | 20.8% | 41.7% |
| unknown | 14 | 11 | 1 | 2 | 78.6% | 7.1% | 14.3% |
- *14 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **42.9%** home win (36/84)
- `>= 0.5` tier: **47.2%** home win (109/231)
- Home-win gap (>= split minus < split): **+4.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 84 | 36 | 15 | 33 | 42.9% |
| high | >= 0.5 | 231 | 109 | 37 | 85 | 47.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.848 | -1.288 | -5.983 | 10.831 |
| away_points_before_match | 12.124 | 14.154 | 20.873 | 8.749 |
| position_difference | -2.186 | 0.942 | 3.119 | 5.305 |
| home_points_before_match | 16.972 | 12.865 | 14.890 | 4.107 |
| home_position_before_match | 6.338 | 8.250 | 9.305 | 2.967 |
| away_team_goals_scored_last_5 | 5.676 | 6.519 | 8.407 | 2.731 |
| home_team_goals_conceded_last_5 | 5.669 | 6.731 | 8.271 | 2.602 |
| away_team_points_last_5 | 5.152 | 5.865 | 7.703 | 2.552 |
| home_rest_days | 10.545 | 8.098 | 9.060 | 2.447 |
| away_position_before_match | 8.524 | 7.308 | 6.186 | 2.338 |
| away_rest_days | 10.679 | 8.922 | 8.767 | 1.912 |
| away_team_goals_conceded_last_5 | 7.421 | 6.962 | 6.008 | 1.412 |
| home_team_points_last_5 | 6.648 | 5.865 | 5.390 | 1.258 |
| home_team_goals_scored_last_5 | 7.338 | 6.673 | 6.186 | 1.151 |
| rest_days_difference | -0.134 | -0.824 | 0.293 | 1.117 |
| away_team_wins_last_5 | 2.200 | 2.442 | 3.042 | 0.842 |
| away_team_away_goals_avg | 0.981 | 1.253 | 1.481 | 0.500 |
| home_team_wins_last_5 | 2.745 | 2.365 | 2.271 | 0.474 |
| away_team_away_conceded_avg | 1.773 | 1.476 | 1.336 | 0.437 |
| home_team_home_goals_avg | 1.747 | 1.368 | 1.376 | 0.380 |
| home_team_home_conceded_avg | 1.076 | 1.252 | 1.341 | 0.265 |
| away_team_away_win_rate | 0.345 | 0.489 | 0.546 | 0.200 |
| home_team_home_win_rate | 0.652 | 0.605 | 0.592 | 0.061 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\wsweden\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\wsweden\charts\relationships_home_win_pct_by_position.png)

