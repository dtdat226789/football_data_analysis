# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:03:01+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: K League 2 (South Korea)
- Scope: league `korea2`

- Matches analysed: **493** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_rest_days | 0.035 | 0.118 | 0.101 |
| home_team_points_last_5 | 0.166 | -0.065 | 0.078 |
| home_position_before_match | -0.208 | 0.116 | -0.075 |
| away_team_goals_conceded_last_5 | 0.050 | -0.169 | -0.074 |
| away_position_before_match | 0.105 | -0.226 | -0.072 |
| home_team_goals_scored_last_5 | 0.130 | -0.042 | 0.066 |
| away_rest_days | 0.021 | 0.079 | 0.066 |
| rest_days_difference | 0.025 | 0.073 | 0.065 |
| home_team_goals_conceded_last_5 | -0.105 | 0.018 | -0.064 |
| home_team_home_conceded_avg | -0.147 | 0.075 | -0.057 |
| away_team_points_last_5 | -0.070 | 0.162 | 0.055 |
| home_team_wins_last_5 | 0.128 | -0.071 | 0.046 |
| away_team_wins_last_5 | -0.076 | 0.150 | 0.043 |
| away_team_away_win_rate | -0.028 | 0.094 | 0.041 |
| away_team_away_conceded_avg | 0.043 | -0.107 | -0.039 |
| away_team_away_goals_avg | -0.011 | 0.058 | 0.030 |
| away_team_goals_scored_last_5 | -0.070 | 0.116 | 0.025 |
| away_points_before_match | -0.089 | 0.066 | -0.022 |
| home_team_home_goals_avg | 0.099 | -0.082 | 0.018 |
| home_points_before_match | 0.078 | -0.112 | -0.017 |
| home_team_home_win_rate | 0.146 | -0.143 | 0.012 |
| points_difference | 0.216 | -0.229 | 0.006 |
| position_difference | -0.224 | 0.244 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 76 | 14 | 29 | 33 | 18.4% | 38.2% | 43.4% |
| -4..-2 | 95 | 24 | 29 | 42 | 25.3% | 30.5% | 44.2% |
| -1..1 | 146 | 56 | 43 | 47 | 38.4% | 29.5% | 32.2% |
| 2..4 | 100 | 41 | 29 | 30 | 41.0% | 29.0% | 30.0% |
| >4 | 76 | 38 | 23 | 15 | 50.0% | 30.3% | 19.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 103 | 48 | 32 | 23 | 46.6% | 31.1% | 22.3% |
| -5..-2 | 102 | 47 | 34 | 21 | 46.1% | 33.3% | 20.6% |
| -1..1 | 79 | 30 | 28 | 21 | 38.0% | 35.4% | 26.6% |
| 2..5 | 111 | 33 | 29 | 49 | 29.7% | 26.1% | 44.1% |
| >=6 | 98 | 15 | 30 | 53 | 15.3% | 30.6% | 54.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 22 | 7 | 7 | 8 | 31.8% | 31.8% | 36.4% |
| -1..0 | 73 | 27 | 23 | 23 | 37.0% | 31.5% | 31.5% |
| 0 | 264 | 99 | 80 | 85 | 37.5% | 30.3% | 32.2% |
| 1..2 | 104 | 26 | 38 | 40 | 25.0% | 36.5% | 38.5% |
| >2 | 14 | 7 | 2 | 5 | 50.0% | 14.3% | 35.7% |
| unknown | 16 | 7 | 3 | 6 | 43.8% | 18.8% | 37.5% |
- *16 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **20.9%** home win (27/129)
- `>= 0.5` tier: **40.1%** home win (146/364)
- Home-win gap (>= split minus < split): **+19.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 129 | 27 | 42 | 60 | 20.9% |
| high | >= 0.5 | 364 | 146 | 111 | 107 | 40.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.711 | -0.412 | -4.204 | 7.915 |
| away_points_before_match | 19.324 | 22.569 | 23.898 | 4.575 |
| position_difference | -1.890 | -0.013 | 2.479 | 4.369 |
| home_points_before_match | 23.035 | 22.157 | 19.695 | 3.340 |
| home_position_before_match | 7.046 | 8.503 | 9.473 | 2.427 |
| away_position_before_match | 8.936 | 8.516 | 6.994 | 1.942 |
| away_team_points_last_5 | 5.306 | 6.353 | 6.551 | 1.245 |
| home_team_points_last_5 | 6.676 | 6.144 | 5.521 | 1.155 |
| away_team_goals_scored_last_5 | 5.341 | 6.209 | 6.299 | 0.958 |
| away_team_goals_conceded_last_5 | 6.312 | 5.928 | 5.503 | 0.809 |
| home_team_goals_conceded_last_5 | 5.497 | 5.954 | 6.293 | 0.796 |
| home_team_goals_scored_last_5 | 6.243 | 5.837 | 5.569 | 0.674 |
| home_rest_days | 7.783 | 7.393 | 7.975 | 0.582 |
| away_team_wins_last_5 | 2.659 | 3.059 | 3.150 | 0.491 |
| away_rest_days | 7.735 | 7.353 | 7.708 | 0.382 |
| home_team_wins_last_5 | 3.162 | 2.967 | 2.802 | 0.359 |
| home_team_home_conceded_avg | 1.081 | 1.207 | 1.358 | 0.277 |
| rest_days_difference | 0.048 | 0.040 | 0.273 | 0.233 |
| home_team_home_goals_avg | 1.387 | 1.246 | 1.221 | 0.166 |
| away_team_away_conceded_avg | 1.317 | 1.331 | 1.199 | 0.133 |
| home_team_home_win_rate | 0.692 | 0.600 | 0.568 | 0.124 |
| away_team_away_goals_avg | 1.163 | 1.230 | 1.253 | 0.090 |
| away_team_away_win_rate | 0.550 | 0.594 | 0.615 | 0.064 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\korea2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\korea2\charts\relationships_home_win_pct_by_position.png)

