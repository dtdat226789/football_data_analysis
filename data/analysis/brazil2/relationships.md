# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:45:46+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie B (Brazil)
- Scope: league `brazil2`

- Matches analysed: **380** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_position_before_match | 0.159 | 0.041 | 0.141 |
| position_difference | -0.172 | 0.026 | -0.104 |
| away_team_goals_conceded_last_5 | 0.051 | 0.088 | 0.097 |
| points_difference | 0.156 | -0.035 | 0.087 |
| away_team_away_conceded_avg | 0.113 | 0.005 | 0.084 |
| home_team_wins_last_5 | 0.114 | 0.002 | 0.082 |
| home_team_points_last_5 | 0.109 | -0.000 | 0.077 |
| away_team_wins_last_5 | -0.046 | -0.050 | -0.067 |
| away_team_points_last_5 | -0.039 | -0.050 | -0.062 |
| home_points_before_match | 0.043 | 0.040 | 0.058 |
| away_team_away_win_rate | -0.038 | -0.033 | -0.050 |
| home_team_home_win_rate | 0.087 | -0.019 | 0.049 |
| home_rest_days | -0.046 | -0.022 | -0.048 |
| rest_days_difference | -0.040 | -0.018 | -0.041 |
| home_team_home_goals_avg | 0.044 | 0.006 | 0.035 |
| home_team_home_conceded_avg | -0.063 | 0.015 | -0.035 |
| home_team_goals_scored_last_5 | 0.015 | 0.032 | 0.033 |
| away_team_away_goals_avg | 0.043 | -0.003 | 0.029 |
| home_team_goals_conceded_last_5 | -0.079 | 0.047 | -0.024 |
| away_team_goals_scored_last_5 | -0.009 | -0.019 | -0.020 |
| away_points_before_match | -0.042 | 0.059 | 0.010 |
| away_rest_days | -0.007 | -0.005 | -0.009 |
| home_position_before_match | -0.078 | 0.077 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 54 | 18 | 19 | 17 | 33.3% | 35.2% | 31.5% |
| -4..-2 | 89 | 43 | 30 | 16 | 48.3% | 33.7% | 18.0% |
| -1..1 | 126 | 61 | 29 | 36 | 48.4% | 23.0% | 28.6% |
| 2..4 | 72 | 34 | 25 | 13 | 47.2% | 34.7% | 18.1% |
| >4 | 39 | 18 | 13 | 8 | 46.2% | 33.3% | 20.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 84 | 44 | 24 | 16 | 52.4% | 28.6% | 19.0% |
| -5..-2 | 67 | 35 | 23 | 9 | 52.2% | 34.3% | 13.4% |
| -1..1 | 51 | 24 | 11 | 16 | 47.1% | 21.6% | 31.4% |
| 2..5 | 69 | 34 | 20 | 15 | 49.3% | 29.0% | 21.7% |
| >=6 | 109 | 37 | 38 | 34 | 33.9% | 34.9% | 31.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 80 | 39 | 21 | 20 | 48.8% | 26.2% | 25.0% |
| -1..0 | 62 | 25 | 22 | 15 | 40.3% | 35.5% | 24.2% |
| 0 | 86 | 45 | 23 | 18 | 52.3% | 26.7% | 20.9% |
| 1..2 | 107 | 45 | 39 | 23 | 42.1% | 36.4% | 21.5% |
| >2 | 35 | 15 | 9 | 11 | 42.9% | 25.7% | 31.4% |
| unknown | 10 | 5 | 2 | 3 | 50.0% | 20.0% | 30.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **41.7%** home win (75/180)
- `>= 0.5` tier: **49.5%** home win (99/200)
- Home-win gap (>= split minus < split): **+7.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 180 | 75 | 60 | 45 | 41.7% |
| high | >= 0.5 | 200 | 99 | 56 | 45 | 49.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 23.305 | 26.991 | 26.822 | 3.687 |
| points_difference | 1.052 | -1.155 | -2.156 | 3.207 |
| position_difference | -0.828 | 1.207 | 1.911 | 2.739 |
| home_points_before_match | 24.356 | 25.836 | 24.667 | 1.480 |
| away_position_before_match | 11.201 | 10.319 | 9.811 | 1.390 |
| home_position_before_match | 10.374 | 11.526 | 11.722 | 1.349 |
| home_team_goals_conceded_last_5 | 4.920 | 5.241 | 5.600 | 0.680 |
| home_team_points_last_5 | 6.155 | 6.103 | 5.500 | 0.655 |
| away_rest_days | 6.325 | 5.947 | 6.483 | 0.535 |
| home_rest_days | 6.195 | 6.061 | 6.471 | 0.410 |
| away_team_points_last_5 | 6.356 | 6.647 | 6.333 | 0.313 |
| away_team_goals_scored_last_5 | 5.218 | 5.379 | 5.111 | 0.268 |
| rest_days_difference | -0.130 | 0.114 | -0.011 | 0.244 |
| home_team_wins_last_5 | 1.569 | 1.586 | 1.344 | 0.242 |
| home_team_goals_scored_last_5 | 4.897 | 5.129 | 4.989 | 0.233 |
| away_team_goals_conceded_last_5 | 4.994 | 5.164 | 5.022 | 0.170 |
| away_team_wins_last_5 | 1.667 | 1.759 | 1.656 | 0.103 |
| away_team_away_conceded_avg | 1.251 | 1.188 | 1.159 | 0.093 |
| home_team_home_conceded_avg | 0.784 | 0.837 | 0.839 | 0.056 |
| home_team_home_win_rate | 0.481 | 0.462 | 0.439 | 0.042 |
| home_team_home_goals_avg | 1.225 | 1.196 | 1.184 | 0.041 |
| away_team_away_goals_avg | 0.822 | 0.802 | 0.812 | 0.020 |
| away_team_away_win_rate | 0.215 | 0.208 | 0.215 | 0.007 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\brazil2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\brazil2\charts\relationships_home_win_pct_by_position.png)

