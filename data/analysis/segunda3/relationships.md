# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:07:25+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Segunda RFEF - Group 3 (Spain)
- Scope: league `segunda3`

- Matches analysed: **306** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.171 | 0.173 | 0.223 |
| rest_days_difference | -0.133 | -0.093 | -0.148 |
| home_team_home_goals_avg | 0.144 | 0.066 | 0.140 |
| away_team_goals_conceded_last_5 | 0.133 | 0.050 | 0.123 |
| away_position_before_match | 0.134 | -0.023 | 0.080 |
| away_rest_days | 0.044 | 0.075 | 0.076 |
| home_team_home_conceded_avg | 0.001 | 0.125 | 0.076 |
| home_team_goals_scored_last_5 | 0.105 | 0.002 | 0.074 |
| away_team_away_goals_avg | 0.024 | 0.083 | 0.066 |
| home_team_home_win_rate | 0.102 | -0.011 | 0.064 |
| home_team_goals_conceded_last_5 | -0.005 | 0.099 | 0.055 |
| away_team_goals_scored_last_5 | -0.006 | 0.088 | 0.048 |
| home_rest_days | -0.067 | -0.003 | -0.048 |
| position_difference | -0.150 | 0.109 | -0.040 |
| points_difference | 0.148 | -0.114 | 0.035 |
| away_team_away_win_rate | -0.063 | 0.032 | -0.025 |
| away_team_points_last_5 | -0.054 | 0.027 | -0.021 |
| home_position_before_match | -0.082 | 0.132 | 0.021 |
| away_points_before_match | -0.062 | 0.045 | -0.016 |
| away_team_wins_last_5 | -0.035 | 0.016 | -0.015 |
| home_team_points_last_5 | 0.062 | -0.050 | 0.013 |
| home_team_wins_last_5 | 0.057 | -0.055 | 0.007 |
| home_points_before_match | 0.036 | -0.030 | 0.007 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 52 | 19 | 17 | 16 | 36.5% | 32.7% | 30.8% |
| -4..-2 | 59 | 23 | 18 | 18 | 39.0% | 30.5% | 30.5% |
| -1..1 | 99 | 45 | 36 | 18 | 45.5% | 36.4% | 18.2% |
| 2..4 | 62 | 33 | 17 | 12 | 53.2% | 27.4% | 19.4% |
| >4 | 34 | 20 | 9 | 5 | 58.8% | 26.5% | 14.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 66 | 36 | 20 | 10 | 54.5% | 30.3% | 15.2% |
| -5..-2 | 62 | 31 | 18 | 13 | 50.0% | 29.0% | 21.0% |
| -1..1 | 45 | 25 | 15 | 5 | 55.6% | 33.3% | 11.1% |
| 2..5 | 44 | 16 | 15 | 13 | 36.4% | 34.1% | 29.5% |
| >=6 | 89 | 32 | 29 | 28 | 36.0% | 32.6% | 31.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 8 | 4 | 3 | 1 | 50.0% | 37.5% | 12.5% |
| -1..0 | 39 | 17 | 9 | 13 | 43.6% | 23.1% | 33.3% |
| 0 | 202 | 93 | 66 | 43 | 46.0% | 32.7% | 21.3% |
| 1..2 | 41 | 18 | 14 | 9 | 43.9% | 34.1% | 22.0% |
| >2 | 7 | 2 | 2 | 3 | 28.6% | 28.6% | 42.9% |
| unknown | 9 | 6 | 3 | 0 | 66.7% | 33.3% | 0.0% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **42.4%** home win (61/144)
- `>= 0.5` tier: **48.8%** home win (79/162)
- Home-win gap (>= split minus < split): **+6.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 144 | 61 | 45 | 38 | 42.4% |
| high | >= 0.5 | 162 | 79 | 52 | 31 | 48.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 20.393 | 21.546 | 27.087 | 6.694 |
| points_difference | 1.486 | -1.485 | -3.420 | 4.906 |
| home_points_before_match | 21.879 | 20.062 | 23.667 | 3.605 |
| position_difference | -0.843 | 1.144 | 2.565 | 3.408 |
| home_position_before_match | 9.221 | 10.371 | 11.029 | 1.808 |
| away_position_before_match | 10.064 | 9.227 | 8.464 | 1.601 |
| away_team_points_last_5 | 5.964 | 6.299 | 7.000 | 1.036 |
| home_team_goals_conceded_last_5 | 5.150 | 5.773 | 6.159 | 1.009 |
| away_team_goals_scored_last_5 | 5.543 | 5.278 | 6.261 | 0.983 |
| away_team_goals_conceded_last_5 | 5.593 | 4.959 | 5.319 | 0.634 |
| home_team_points_last_5 | 6.057 | 5.784 | 5.551 | 0.506 |
| home_rest_days | 7.082 | 7.245 | 7.478 | 0.396 |
| away_team_wins_last_5 | 1.500 | 1.598 | 1.797 | 0.297 |
| away_rest_days | 7.149 | 7.170 | 7.420 | 0.271 |
| home_team_wins_last_5 | 1.500 | 1.474 | 1.290 | 0.210 |
| home_team_goals_scored_last_5 | 5.321 | 5.340 | 5.130 | 0.210 |
| away_team_away_goals_avg | 0.890 | 0.857 | 1.009 | 0.152 |
| rest_days_difference | -0.067 | 0.074 | 0.058 | 0.142 |
| home_team_home_conceded_avg | 0.856 | 0.935 | 0.982 | 0.125 |
| away_team_away_conceded_avg | 1.337 | 1.300 | 1.402 | 0.102 |
| away_team_away_win_rate | 0.143 | 0.162 | 0.200 | 0.057 |
| home_team_home_win_rate | 0.482 | 0.460 | 0.447 | 0.035 |
| home_team_home_goals_avg | 1.342 | 1.344 | 1.335 | 0.009 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\segunda3\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\segunda3\charts\relationships_home_win_pct_by_position.png)

