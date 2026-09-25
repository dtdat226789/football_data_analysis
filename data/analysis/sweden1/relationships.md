# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:48:36+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Allsvenskan (Sweden)
- Scope: league `sweden1`

- Matches analysed: **416** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| rest_days_difference | -0.011 | -0.138 | -0.102 |
| home_team_home_goals_avg | 0.149 | -0.059 | 0.076 |
| away_rest_days | 0.012 | 0.091 | 0.071 |
| home_team_goals_scored_last_5 | 0.139 | -0.059 | 0.067 |
| position_difference | -0.239 | 0.189 | -0.055 |
| away_team_goals_scored_last_5 | -0.017 | 0.089 | 0.048 |
| home_team_home_win_rate | 0.136 | -0.084 | 0.048 |
| away_team_away_win_rate | -0.034 | 0.106 | 0.047 |
| home_rest_days | 0.009 | 0.052 | 0.043 |
| away_team_points_last_5 | -0.064 | 0.134 | 0.043 |
| home_position_before_match | -0.160 | 0.119 | -0.042 |
| away_team_wins_last_5 | -0.056 | 0.120 | 0.039 |
| away_team_away_conceded_avg | 0.046 | -0.108 | -0.039 |
| home_team_wins_last_5 | 0.102 | -0.061 | 0.037 |
| away_position_before_match | 0.177 | -0.147 | 0.036 |
| points_difference | 0.223 | -0.204 | 0.033 |
| home_team_goals_conceded_last_5 | -0.062 | 0.118 | 0.033 |
| home_team_points_last_5 | 0.126 | -0.097 | 0.031 |
| away_points_before_match | -0.131 | 0.106 | -0.029 |
| away_team_away_goals_avg | -0.011 | 0.036 | 0.016 |
| home_team_home_conceded_avg | -0.094 | 0.090 | -0.011 |
| away_team_goals_conceded_last_5 | 0.102 | -0.111 | 0.003 |
| home_points_before_match | 0.057 | -0.067 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 69 | 17 | 18 | 34 | 24.6% | 26.1% | 49.3% |
| -4..-2 | 80 | 26 | 19 | 35 | 32.5% | 23.8% | 43.8% |
| -1..1 | 116 | 45 | 29 | 42 | 38.8% | 25.0% | 36.2% |
| 2..4 | 91 | 47 | 14 | 30 | 51.6% | 15.4% | 33.0% |
| >4 | 60 | 34 | 14 | 12 | 56.7% | 23.3% | 20.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 88 | 60 | 13 | 15 | 68.2% | 14.8% | 17.0% |
| -5..-2 | 92 | 40 | 20 | 32 | 43.5% | 21.7% | 34.8% |
| -1..1 | 69 | 23 | 18 | 28 | 33.3% | 26.1% | 40.6% |
| 2..5 | 81 | 25 | 22 | 34 | 30.9% | 27.2% | 42.0% |
| >=6 | 86 | 21 | 21 | 44 | 24.4% | 24.4% | 51.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 46 | 16 | 9 | 21 | 34.8% | 19.6% | 45.7% |
| -1..0 | 103 | 42 | 23 | 38 | 40.8% | 22.3% | 36.9% |
| 0 | 117 | 48 | 24 | 45 | 41.0% | 20.5% | 38.5% |
| 1..2 | 121 | 50 | 32 | 39 | 41.3% | 26.4% | 32.2% |
| >2 | 13 | 7 | 3 | 3 | 53.8% | 23.1% | 23.1% |
| unknown | 16 | 6 | 3 | 7 | 37.5% | 18.8% | 43.8% |
- *16 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **34.3%** home win (47/137)
- `>= 0.5` tier: **43.7%** home win (122/279)
- Home-win gap (>= split minus < split): **+9.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 137 | 47 | 36 | 54 | 34.3% |
| high | >= 0.5 | 279 | 122 | 58 | 99 | 43.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.515 | -0.362 | -3.725 | 7.240 |
| away_points_before_match | 15.822 | 17.032 | 20.190 | 4.367 |
| position_difference | -2.154 | 0.691 | 2.072 | 4.226 |
| home_points_before_match | 19.337 | 16.670 | 16.464 | 2.873 |
| away_position_before_match | 9.840 | 8.351 | 7.588 | 2.252 |
| home_position_before_match | 7.686 | 9.043 | 9.660 | 1.974 |
| home_team_points_last_5 | 6.669 | 6.096 | 5.386 | 1.283 |
| home_team_goals_conceded_last_5 | 5.888 | 6.734 | 7.105 | 1.217 |
| away_rest_days | 7.301 | 8.209 | 8.295 | 0.994 |
| home_rest_days | 7.356 | 8.297 | 7.959 | 0.941 |
| away_team_points_last_5 | 5.639 | 6.500 | 6.575 | 0.936 |
| away_team_goals_conceded_last_5 | 6.751 | 6.309 | 5.941 | 0.810 |
| home_team_goals_scored_last_5 | 6.781 | 6.223 | 6.013 | 0.768 |
| away_team_goals_scored_last_5 | 6.124 | 6.809 | 6.693 | 0.684 |
| rest_days_difference | 0.055 | 0.088 | -0.336 | 0.424 |
| home_team_wins_last_5 | 2.870 | 2.670 | 2.497 | 0.373 |
| away_team_wins_last_5 | 2.598 | 2.755 | 2.915 | 0.317 |
| home_team_home_conceded_avg | 1.117 | 1.267 | 1.338 | 0.222 |
| home_team_home_goals_avg | 1.513 | 1.319 | 1.351 | 0.195 |
| away_team_away_conceded_avg | 1.499 | 1.351 | 1.356 | 0.148 |
| home_team_home_win_rate | 0.639 | 0.571 | 0.545 | 0.094 |
| away_team_away_goals_avg | 1.177 | 1.269 | 1.260 | 0.091 |
| away_team_away_win_rate | 0.500 | 0.562 | 0.587 | 0.087 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\sweden1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\sweden1\charts\relationships_home_win_pct_by_position.png)

