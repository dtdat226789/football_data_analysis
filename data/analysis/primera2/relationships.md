# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:04:38+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

- Matches analysed: **380** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.178 | 0.077 | 0.177 |
| home_points_before_match | 0.182 | 0.070 | 0.176 |
| home_team_home_goals_avg | 0.104 | 0.125 | 0.154 |
| away_points_before_match | 0.095 | 0.120 | 0.145 |
| home_team_wins_last_5 | 0.085 | 0.075 | 0.108 |
| home_team_points_last_5 | 0.083 | 0.059 | 0.097 |
| home_team_goals_conceded_last_5 | 0.082 | 0.045 | 0.088 |
| rest_days_difference | 0.094 | 0.028 | 0.086 |
| home_team_home_conceded_avg | 0.029 | 0.092 | 0.079 |
| away_team_points_last_5 | 0.044 | 0.070 | 0.076 |
| away_team_goals_scored_last_5 | 0.037 | 0.077 | 0.076 |
| away_team_wins_last_5 | 0.050 | 0.060 | 0.074 |
| home_rest_days | 0.049 | 0.049 | 0.066 |
| away_team_away_conceded_avg | 0.033 | 0.066 | 0.066 |
| away_team_away_win_rate | 0.002 | 0.097 | 0.064 |
| home_team_home_win_rate | 0.050 | 0.043 | 0.063 |
| home_position_before_match | -0.077 | -0.005 | -0.058 |
| away_team_away_goals_avg | -0.014 | 0.101 | 0.054 |
| points_difference | 0.151 | -0.088 | 0.052 |
| position_difference | -0.116 | 0.059 | -0.046 |
| away_team_goals_conceded_last_5 | 0.011 | 0.009 | 0.014 |
| away_position_before_match | 0.085 | -0.087 | 0.005 |
| away_rest_days | -0.029 | 0.027 | -0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 49 | 19 | 16 | 14 | 38.8% | 32.7% | 28.6% |
| -4..-2 | 97 | 42 | 30 | 25 | 43.3% | 30.9% | 25.8% |
| -1..1 | 124 | 65 | 32 | 27 | 52.4% | 25.8% | 21.8% |
| 2..4 | 74 | 30 | 24 | 20 | 40.5% | 32.4% | 27.0% |
| >4 | 36 | 17 | 11 | 8 | 47.2% | 30.6% | 22.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 87 | 41 | 29 | 17 | 47.1% | 33.3% | 19.5% |
| -5..-2 | 75 | 38 | 20 | 17 | 50.7% | 26.7% | 22.7% |
| -1..1 | 52 | 25 | 14 | 13 | 48.1% | 26.9% | 25.0% |
| 2..5 | 68 | 33 | 20 | 15 | 48.5% | 29.4% | 22.1% |
| >=6 | 98 | 36 | 30 | 32 | 36.7% | 30.6% | 32.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 29 | 14 | 7 | 8 | 48.3% | 24.1% | 27.6% |
| -1..0 | 73 | 38 | 17 | 18 | 52.1% | 23.3% | 24.7% |
| 0 | 146 | 63 | 45 | 38 | 43.2% | 30.8% | 26.0% |
| 1..2 | 105 | 45 | 34 | 26 | 42.9% | 32.4% | 24.8% |
| >2 | 17 | 9 | 6 | 2 | 52.9% | 35.3% | 11.8% |
| unknown | 10 | 4 | 4 | 2 | 40.0% | 40.0% | 20.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **45.1%** home win (106/235)
- `>= 0.5` tier: **46.2%** home win (67/145)
- Home-win gap (>= split minus < split): **+1.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 235 | 106 | 62 | 67 | 45.1% |
| high | >= 0.5 | 145 | 67 | 51 | 27 | 46.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 24.890 | 22.708 | 27.500 | 4.792 |
| points_difference | 1.092 | -0.540 | -2.904 | 3.997 |
| home_points_before_match | 25.983 | 22.168 | 24.596 | 3.815 |
| position_difference | -0.509 | 0.425 | 2.160 | 2.668 |
| away_position_before_match | 11.532 | 10.248 | 9.777 | 1.755 |
| home_position_before_match | 11.023 | 10.673 | 11.936 | 1.264 |
| away_team_goals_scored_last_5 | 5.098 | 4.841 | 5.681 | 0.840 |
| away_team_goals_conceded_last_5 | 4.983 | 4.575 | 5.362 | 0.786 |
| home_team_goals_conceded_last_5 | 5.289 | 4.673 | 5.436 | 0.764 |
| home_team_goals_scored_last_5 | 5.173 | 4.646 | 4.830 | 0.527 |
| away_rest_days | 7.130 | 6.917 | 7.326 | 0.409 |
| rest_days_difference | 0.095 | 0.294 | -0.087 | 0.381 |
| away_team_points_last_5 | 6.341 | 6.292 | 6.585 | 0.293 |
| home_team_home_conceded_avg | 0.823 | 0.732 | 0.919 | 0.187 |
| away_team_away_goals_avg | 0.793 | 0.758 | 0.935 | 0.177 |
| home_team_points_last_5 | 6.092 | 5.920 | 6.096 | 0.175 |
| away_team_away_conceded_avg | 1.131 | 1.075 | 1.212 | 0.137 |
| home_team_wins_last_5 | 1.555 | 1.504 | 1.585 | 0.081 |
| home_team_home_goals_avg | 1.137 | 1.087 | 1.167 | 0.081 |
| away_team_wins_last_5 | 1.671 | 1.637 | 1.713 | 0.076 |
| home_team_home_win_rate | 0.406 | 0.433 | 0.401 | 0.033 |
| away_team_away_win_rate | 0.189 | 0.198 | 0.220 | 0.031 |
| home_rest_days | 7.225 | 7.211 | 7.239 | 0.028 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\primera2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\primera2\charts\relationships_home_win_pct_by_position.png)

