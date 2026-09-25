# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:59:41+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 2. Bundesliga (Germany)
- Scope: league `germany2`

- Matches analysed: **364** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.149 | -0.006 | -0.111 |
| home_team_home_win_rate | 0.109 | 0.015 | 0.088 |
| rest_days_difference | 0.047 | 0.033 | 0.056 |
| points_difference | 0.109 | -0.040 | 0.052 |
| away_team_away_win_rate | 0.004 | 0.072 | 0.050 |
| away_position_before_match | 0.005 | -0.076 | -0.046 |
| away_team_points_last_5 | -0.070 | 0.006 | -0.046 |
| position_difference | -0.109 | 0.050 | -0.046 |
| home_team_home_conceded_avg | -0.058 | 0.012 | -0.034 |
| home_points_before_match | 0.109 | -0.073 | 0.031 |
| away_team_wins_last_5 | -0.047 | 0.007 | -0.029 |
| away_team_goals_scored_last_5 | -0.018 | -0.024 | -0.029 |
| home_team_home_goals_avg | 0.047 | -0.010 | 0.027 |
| home_team_goals_scored_last_5 | 0.027 | -0.061 | -0.020 |
| home_team_wins_last_5 | 0.064 | -0.041 | 0.019 |
| home_team_points_last_5 | 0.028 | -0.051 | -0.014 |
| home_team_goals_conceded_last_5 | -0.047 | 0.036 | -0.010 |
| away_team_away_conceded_avg | 0.013 | -0.026 | -0.008 |
| away_team_away_goals_avg | -0.021 | 0.012 | -0.007 |
| home_rest_days | -0.010 | 0.020 | 0.006 |
| away_points_before_match | 0.036 | -0.046 | -0.005 |
| away_team_goals_conceded_last_5 | 0.029 | -0.032 | -0.001 |
| away_rest_days | -0.016 | 0.019 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 52 | 18 | 19 | 15 | 34.6% | 36.5% | 28.8% |
| -4..-2 | 87 | 30 | 25 | 32 | 34.5% | 28.7% | 36.8% |
| -1..1 | 112 | 62 | 23 | 27 | 55.4% | 20.5% | 24.1% |
| 2..4 | 66 | 36 | 10 | 20 | 54.5% | 15.2% | 30.3% |
| >4 | 47 | 19 | 13 | 15 | 40.4% | 27.7% | 31.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 82 | 47 | 16 | 19 | 57.3% | 19.5% | 23.2% |
| -5..-2 | 60 | 28 | 15 | 17 | 46.7% | 25.0% | 28.3% |
| -1..1 | 57 | 27 | 11 | 19 | 47.4% | 19.3% | 33.3% |
| 2..5 | 74 | 29 | 17 | 28 | 39.2% | 23.0% | 37.8% |
| >=6 | 91 | 34 | 31 | 26 | 37.4% | 34.1% | 28.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 28 | 13 | 5 | 10 | 46.4% | 17.9% | 35.7% |
| -1..0 | 84 | 44 | 15 | 25 | 52.4% | 17.9% | 29.8% |
| 0 | 104 | 45 | 24 | 35 | 43.3% | 23.1% | 33.7% |
| 1..2 | 128 | 50 | 42 | 36 | 39.1% | 32.8% | 28.1% |
| >2 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 20 | 13 | 4 | 3 | 65.0% | 20.0% | 15.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **40.4%** home win (38/94)
- `>= 0.5` tier: **47.0%** home win (127/270)
- Home-win gap (>= split minus < split): **+6.6 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 94 | 38 | 24 | 32 | 40.4% |
| high | >= 0.5 | 270 | 127 | 66 | 77 | 47.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 19.558 | 23.222 | 18.688 | 4.534 |
| home_points_before_match | 21.267 | 20.822 | 17.110 | 4.157 |
| points_difference | 1.709 | -2.400 | -1.578 | 4.109 |
| position_difference | -1.055 | 1.722 | 1.138 | 2.777 |
| home_position_before_match | 9.067 | 10.289 | 10.688 | 1.621 |
| away_position_before_match | 10.121 | 8.567 | 9.550 | 1.555 |
| away_team_points_last_5 | 5.576 | 6.533 | 6.055 | 0.958 |
| away_rest_days | 8.765 | 8.057 | 8.830 | 0.773 |
| away_team_goals_scored_last_5 | 6.188 | 6.900 | 6.339 | 0.712 |
| home_team_goals_conceded_last_5 | 6.012 | 6.567 | 6.596 | 0.584 |
| away_team_goals_conceded_last_5 | 6.297 | 6.456 | 5.991 | 0.465 |
| away_team_wins_last_5 | 2.509 | 2.933 | 2.679 | 0.424 |
| home_rest_days | 8.724 | 8.407 | 8.792 | 0.385 |
| rest_days_difference | -0.066 | 0.302 | -0.038 | 0.368 |
| home_team_points_last_5 | 5.848 | 5.622 | 5.541 | 0.307 |
| home_team_wins_last_5 | 2.648 | 2.600 | 2.514 | 0.135 |
| home_team_home_conceded_avg | 1.165 | 1.221 | 1.294 | 0.129 |
| away_team_away_goals_avg | 1.174 | 1.276 | 1.224 | 0.103 |
| home_team_goals_scored_last_5 | 6.194 | 6.144 | 6.092 | 0.102 |
| away_team_away_win_rate | 0.457 | 0.537 | 0.492 | 0.080 |
| home_team_home_win_rate | 0.615 | 0.582 | 0.565 | 0.050 |
| home_team_home_goals_avg | 1.392 | 1.360 | 1.355 | 0.036 |
| away_team_away_conceded_avg | 1.395 | 1.363 | 1.374 | 0.033 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\germany2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\germany2\charts\relationships_home_win_pct_by_position.png)

