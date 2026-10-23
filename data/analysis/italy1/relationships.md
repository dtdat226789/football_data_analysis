# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:56:43+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie A (Italy)
- Scope: league `italy1`

- Matches analysed: **380** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_win_rate | 0.228 | -0.091 | 0.118 |
| position_difference | -0.341 | 0.232 | -0.111 |
| home_position_before_match | -0.232 | 0.124 | -0.099 |
| home_team_points_last_5 | 0.172 | -0.055 | 0.098 |
| home_points_before_match | 0.150 | -0.034 | 0.095 |
| home_team_wins_last_5 | 0.178 | -0.077 | 0.088 |
| home_team_home_goals_avg | 0.188 | -0.101 | 0.080 |
| away_team_wins_last_5 | -0.225 | 0.143 | -0.080 |
| home_team_goals_conceded_last_5 | -0.126 | 0.032 | -0.077 |
| points_difference | 0.311 | -0.264 | 0.066 |
| rest_days_difference | 0.048 | 0.030 | 0.058 |
| away_position_before_match | 0.246 | -0.202 | 0.056 |
| home_team_goals_scored_last_5 | 0.172 | -0.127 | 0.049 |
| away_team_points_last_5 | -0.199 | 0.161 | -0.047 |
| away_points_before_match | -0.108 | 0.185 | 0.040 |
| home_team_home_conceded_avg | -0.095 | 0.055 | -0.038 |
| away_team_away_goals_avg | -0.078 | 0.137 | 0.032 |
| away_team_away_win_rate | -0.161 | 0.144 | -0.029 |
| home_rest_days | -0.000 | 0.027 | 0.018 |
| away_rest_days | -0.024 | 0.013 | -0.010 |
| away_team_goals_scored_last_5 | -0.154 | 0.165 | -0.009 |
| away_team_away_conceded_avg | 0.060 | -0.082 | -0.009 |
| away_team_goals_conceded_last_5 | 0.096 | -0.109 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 55 | 10 | 16 | 29 | 18.2% | 29.1% | 52.7% |
| -4..-2 | 86 | 27 | 19 | 40 | 31.4% | 22.1% | 46.5% |
| -1..1 | 113 | 48 | 31 | 34 | 42.5% | 27.4% | 30.1% |
| 2..4 | 60 | 26 | 17 | 17 | 43.3% | 28.3% | 28.3% |
| >4 | 66 | 37 | 16 | 13 | 56.1% | 24.2% | 19.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 95 | 56 | 20 | 19 | 58.9% | 21.1% | 20.0% |
| -5..-2 | 65 | 29 | 25 | 11 | 44.6% | 38.5% | 16.9% |
| -1..1 | 51 | 19 | 15 | 17 | 37.3% | 29.4% | 33.3% |
| 2..5 | 65 | 19 | 19 | 27 | 29.2% | 29.2% | 41.5% |
| >=6 | 104 | 25 | 20 | 59 | 24.0% | 19.2% | 56.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 38 | 8 | 18 | 12 | 21.1% | 47.4% | 31.6% |
| -1..0 | 87 | 33 | 20 | 34 | 37.9% | 23.0% | 39.1% |
| 0 | 118 | 48 | 25 | 45 | 40.7% | 21.2% | 38.1% |
| 1..2 | 117 | 54 | 30 | 33 | 46.2% | 25.6% | 28.2% |
| >2 | 10 | 1 | 2 | 7 | 10.0% | 20.0% | 70.0% |
| unknown | 10 | 4 | 4 | 2 | 40.0% | 40.0% | 20.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **32.1%** home win (78/243)
- `>= 0.5` tier: **51.1%** home win (70/137)
- Home-win gap (>= split minus < split): **+19.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 243 | 78 | 60 | 105 | 32.1% |
| high | >= 0.5 | 137 | 70 | 39 | 28 | 51.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.297 | 0.505 | -6.880 | 12.177 |
| away_points_before_match | 22.547 | 23.354 | 29.722 | 7.175 |
| position_difference | -2.736 | -0.051 | 3.910 | 6.646 |
| home_points_before_match | 27.845 | 23.859 | 22.842 | 5.002 |
| away_position_before_match | 12.068 | 10.838 | 8.729 | 3.338 |
| home_position_before_match | 9.331 | 10.788 | 12.639 | 3.308 |
| away_team_points_last_5 | 5.574 | 6.455 | 7.060 | 1.486 |
| home_team_goals_scored_last_5 | 6.162 | 5.505 | 4.880 | 1.282 |
| home_team_points_last_5 | 6.838 | 6.343 | 5.617 | 1.221 |
| away_team_goals_scored_last_5 | 5.074 | 5.606 | 6.180 | 1.106 |
| home_team_goals_conceded_last_5 | 5.358 | 5.343 | 6.135 | 0.792 |
| away_team_goals_conceded_last_5 | 5.899 | 5.343 | 5.218 | 0.681 |
| away_team_wins_last_5 | 1.432 | 1.737 | 1.977 | 0.545 |
| home_team_wins_last_5 | 1.912 | 1.717 | 1.429 | 0.484 |
| home_team_home_goals_avg | 1.309 | 1.235 | 1.021 | 0.288 |
| rest_days_difference | 0.139 | -0.116 | -0.023 | 0.255 |
| home_rest_days | 7.479 | 7.232 | 7.382 | 0.248 |
| away_team_away_goals_avg | 0.963 | 1.038 | 1.123 | 0.160 |
| home_team_home_win_rate | 0.421 | 0.376 | 0.289 | 0.132 |
| home_team_home_conceded_avg | 0.989 | 1.015 | 1.095 | 0.106 |
| away_team_away_conceded_avg | 1.238 | 1.182 | 1.143 | 0.096 |
| away_team_away_win_rate | 0.267 | 0.302 | 0.362 | 0.095 |
| away_rest_days | 7.340 | 7.347 | 7.405 | 0.064 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\italy1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\italy1\charts\relationships_home_win_pct_by_position.png)

