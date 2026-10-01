# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:49:22+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Meistriliiga (Estonia)
- Scope: league `estonia`

- Matches analysed: **180** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_position_before_match | 0.430 | -0.278 | 0.169 |
| away_team_points_last_5 | -0.380 | 0.236 | -0.158 |
| away_team_goals_conceded_last_5 | 0.386 | -0.244 | 0.157 |
| away_team_away_win_rate | -0.341 | 0.197 | -0.153 |
| away_rest_days | 0.086 | 0.091 | 0.152 |
| away_team_away_conceded_avg | 0.371 | -0.239 | 0.147 |
| away_team_away_goals_avg | -0.266 | 0.121 | -0.147 |
| rest_days_difference | -0.019 | -0.154 | -0.143 |
| position_difference | -0.485 | 0.381 | -0.136 |
| away_team_wins_last_5 | -0.349 | 0.229 | -0.135 |
| points_difference | 0.456 | -0.360 | 0.127 |
| away_team_goals_scored_last_5 | -0.273 | 0.168 | -0.115 |
| away_points_before_match | -0.260 | 0.168 | -0.103 |
| home_team_goals_scored_last_5 | 0.084 | -0.194 | -0.081 |
| home_rest_days | 0.070 | -0.003 | 0.062 |
| home_team_wins_last_5 | 0.131 | -0.221 | -0.059 |
| home_team_points_last_5 | 0.136 | -0.221 | -0.055 |
| home_team_home_goals_avg | 0.109 | -0.188 | -0.053 |
| home_team_goals_conceded_last_5 | -0.141 | 0.210 | 0.041 |
| home_position_before_match | -0.263 | 0.268 | -0.023 |
| home_team_home_win_rate | 0.127 | -0.171 | -0.022 |
| home_points_before_match | 0.174 | -0.177 | 0.017 |
| home_team_home_conceded_avg | -0.218 | 0.250 | 0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 34 | 6 | 3 | 25 | 17.6% | 8.8% | 73.5% |
| -4..-2 | 27 | 11 | 3 | 13 | 40.7% | 11.1% | 48.1% |
| -1..1 | 50 | 20 | 9 | 21 | 40.0% | 18.0% | 42.0% |
| 2..4 | 29 | 15 | 8 | 6 | 51.7% | 27.6% | 20.7% |
| >4 | 40 | 32 | 1 | 7 | 80.0% | 2.5% | 17.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 19 | 18 | 1 | 0 | 94.7% | 5.3% | 0.0% |
| -5..-2 | 49 | 31 | 6 | 12 | 63.3% | 12.2% | 24.5% |
| -1..1 | 41 | 16 | 9 | 16 | 39.0% | 22.0% | 39.0% |
| 2..5 | 58 | 17 | 8 | 33 | 29.3% | 13.8% | 56.9% |
| >=6 | 13 | 2 | 0 | 11 | 15.4% | 0.0% | 84.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 16 | 9 | 2 | 5 | 56.2% | 12.5% | 31.2% |
| -1..0 | 41 | 19 | 7 | 15 | 46.3% | 17.1% | 36.6% |
| 0 | 55 | 29 | 7 | 19 | 52.7% | 12.7% | 34.5% |
| 1..2 | 53 | 20 | 5 | 28 | 37.7% | 9.4% | 52.8% |
| >2 | 10 | 6 | 2 | 2 | 60.0% | 20.0% | 20.0% |
| unknown | 5 | 1 | 1 | 3 | 20.0% | 20.0% | 60.0% |
- *5 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **35.6%** home win (36/101)
- `>= 0.5` tier: **60.8%** home win (48/79)
- Home-win gap (>= split minus < split): **+25.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 101 | 36 | 13 | 52 | 35.6% |
| high | >= 0.5 | 79 | 48 | 11 | 20 | 60.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 8.869 | -3.917 | -9.806 | 18.675 |
| away_points_before_match | 19.643 | 32.125 | 29.847 | 12.482 |
| home_points_before_match | 28.512 | 28.208 | 20.042 | 8.470 |
| position_difference | -2.024 | -0.042 | 2.181 | 4.204 |
| away_team_goals_conceded_last_5 | 9.060 | 7.375 | 5.222 | 3.837 |
| away_team_points_last_5 | 5.060 | 6.625 | 7.944 | 2.885 |
| away_position_before_match | 6.821 | 5.333 | 4.292 | 2.530 |
| home_team_points_last_5 | 7.714 | 6.750 | 5.625 | 2.089 |
| away_team_goals_scored_last_5 | 6.202 | 7.458 | 8.250 | 2.048 |
| home_team_goals_scored_last_5 | 8.310 | 6.958 | 6.528 | 1.782 |
| home_team_goals_conceded_last_5 | 6.810 | 6.417 | 8.181 | 1.764 |
| home_position_before_match | 4.798 | 5.292 | 6.472 | 1.675 |
| away_team_wins_last_5 | 1.488 | 2.125 | 2.417 | 0.929 |
| away_team_away_conceded_avg | 1.928 | 1.584 | 1.127 | 0.801 |
| home_rest_days | 7.325 | 7.826 | 7.029 | 0.797 |
| home_team_wins_last_5 | 2.393 | 2.042 | 1.681 | 0.712 |
| away_rest_days | 7.120 | 7.565 | 6.957 | 0.609 |
| home_team_home_goals_avg | 1.836 | 1.518 | 1.369 | 0.468 |
| home_team_home_conceded_avg | 1.222 | 1.197 | 1.661 | 0.464 |
| away_team_away_goals_avg | 1.274 | 1.445 | 1.589 | 0.316 |
| rest_days_difference | 0.205 | 0.261 | 0.072 | 0.188 |
| away_team_away_win_rate | 0.345 | 0.481 | 0.513 | 0.168 |
| home_team_home_win_rate | 0.479 | 0.438 | 0.343 | 0.137 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\estonia\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\estonia\charts\relationships_home_win_pct_by_position.png)

