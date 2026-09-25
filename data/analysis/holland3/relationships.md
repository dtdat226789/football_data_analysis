# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:00:49+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Tweede Divisie (Netherlands)
- Scope: league `holland3`

- Matches analysed: **376** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | 0.043 | 0.077 | 0.092 |
| home_team_home_goals_avg | 0.042 | 0.077 | 0.091 |
| rest_days_difference | -0.096 | 0.005 | -0.072 |
| home_team_goals_conceded_last_5 | 0.071 | 0.006 | 0.062 |
| home_points_before_match | 0.126 | -0.057 | 0.061 |
| away_team_goals_scored_last_5 | -0.034 | 0.099 | 0.046 |
| home_team_goals_scored_last_5 | 0.072 | -0.020 | 0.044 |
| away_team_goals_conceded_last_5 | 0.049 | -0.001 | 0.039 |
| away_points_before_match | 0.021 | 0.028 | 0.038 |
| away_rest_days | 0.073 | -0.028 | 0.037 |
| position_difference | -0.185 | 0.156 | -0.035 |
| points_difference | 0.158 | -0.128 | 0.034 |
| away_team_away_goals_avg | -0.049 | 0.094 | 0.029 |
| home_position_before_match | -0.150 | 0.126 | -0.029 |
| home_team_home_win_rate | 0.005 | -0.040 | -0.025 |
| home_rest_days | 0.047 | -0.024 | 0.020 |
| away_position_before_match | 0.089 | -0.077 | 0.016 |
| away_team_wins_last_5 | -0.075 | 0.064 | -0.013 |
| home_team_wins_last_5 | 0.041 | -0.031 | 0.011 |
| away_team_points_last_5 | -0.062 | 0.059 | -0.007 |
| home_team_points_last_5 | 0.036 | -0.046 | -0.005 |
| away_team_away_conceded_avg | 0.036 | -0.044 | -0.004 |
| away_team_away_win_rate | -0.075 | 0.081 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 55 | 26 | 9 | 20 | 47.3% | 16.4% | 36.4% |
| -4..-2 | 83 | 27 | 19 | 37 | 32.5% | 22.9% | 44.6% |
| -1..1 | 109 | 54 | 18 | 37 | 49.5% | 16.5% | 33.9% |
| 2..4 | 87 | 43 | 21 | 23 | 49.4% | 24.1% | 26.4% |
| >4 | 42 | 21 | 10 | 11 | 50.0% | 23.8% | 26.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 84 | 45 | 20 | 19 | 53.6% | 23.8% | 22.6% |
| -5..-2 | 71 | 37 | 14 | 20 | 52.1% | 19.7% | 28.2% |
| -1..1 | 58 | 31 | 10 | 17 | 53.4% | 17.2% | 29.3% |
| 2..5 | 80 | 31 | 16 | 33 | 38.8% | 20.0% | 41.2% |
| >=6 | 83 | 27 | 17 | 39 | 32.5% | 20.5% | 47.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 8 | 4 | 1 | 3 | 50.0% | 12.5% | 37.5% |
| -1..0 | 1 | 0 | 1 | 0 | 0.0% | 100.0% | 0.0% |
| 0 | 339 | 152 | 73 | 114 | 44.8% | 21.5% | 33.6% |
| 1..2 | 1 | 1 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| >2 | 4 | 1 | 0 | 3 | 25.0% | 0.0% | 75.0% |
| unknown | 23 | 13 | 2 | 8 | 56.5% | 8.7% | 34.8% |
- *23 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **45.4%** home win (54/119)
- `>= 0.5` tier: **45.5%** home win (117/257)
- Home-win gap (>= split minus < split): **+0.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 119 | 54 | 22 | 43 | 45.4% |
| high | >= 0.5 | 257 | 117 | 55 | 85 | 45.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 21.725 | 20.260 | 17.625 | 4.100 |
| points_difference | 1.450 | 0.403 | -2.531 | 3.982 |
| position_difference | -1.064 | -0.156 | 2.195 | 3.260 |
| home_position_before_match | 9.754 | 9.325 | 11.438 | 2.113 |
| away_team_goals_scored_last_5 | 6.480 | 8.208 | 7.148 | 1.728 |
| away_position_before_match | 10.819 | 9.481 | 9.242 | 1.577 |
| home_team_points_last_5 | 5.772 | 6.649 | 5.188 | 1.462 |
| home_team_goals_scored_last_5 | 6.988 | 7.364 | 6.219 | 1.145 |
| away_team_goals_conceded_last_5 | 6.766 | 7.481 | 6.430 | 1.051 |
| away_rest_days | 8.494 | 7.455 | 8.165 | 1.039 |
| home_rest_days | 8.392 | 7.360 | 8.200 | 1.032 |
| away_team_points_last_5 | 5.749 | 6.545 | 6.055 | 0.797 |
| home_team_wins_last_5 | 2.474 | 2.753 | 2.281 | 0.472 |
| away_points_before_match | 20.275 | 19.857 | 20.156 | 0.418 |
| away_team_wins_last_5 | 2.427 | 2.831 | 2.555 | 0.404 |
| home_team_goals_conceded_last_5 | 7.193 | 6.844 | 6.805 | 0.388 |
| away_team_away_goals_avg | 1.218 | 1.547 | 1.384 | 0.329 |
| away_team_away_conceded_avg | 1.596 | 1.713 | 1.422 | 0.291 |
| rest_days_difference | -0.101 | -0.053 | 0.000 | 0.101 |
| away_team_away_win_rate | 0.435 | 0.529 | 0.503 | 0.093 |
| home_team_home_goals_avg | 1.546 | 1.612 | 1.537 | 0.075 |
| home_team_home_win_rate | 0.569 | 0.600 | 0.528 | 0.072 |
| home_team_home_conceded_avg | 1.331 | 1.365 | 1.346 | 0.034 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\holland3\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\holland3\charts\relationships_home_win_pct_by_position.png)

