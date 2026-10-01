# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:51:31+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 3. Liga (Germany)
- Scope: league `germany3`

- Matches analysed: **380** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_position_before_match | 0.158 | -0.003 | 0.116 |
| away_team_goals_conceded_last_5 | 0.109 | 0.027 | 0.100 |
| position_difference | -0.220 | 0.102 | -0.093 |
| away_team_away_conceded_avg | 0.123 | -0.006 | 0.088 |
| points_difference | 0.227 | -0.117 | 0.087 |
| home_team_goals_scored_last_5 | 0.157 | -0.073 | 0.066 |
| home_points_before_match | 0.156 | -0.073 | 0.066 |
| home_team_goals_conceded_last_5 | -0.042 | 0.125 | 0.057 |
| rest_days_difference | -0.034 | -0.031 | -0.047 |
| away_team_wins_last_5 | -0.056 | -0.004 | -0.044 |
| home_team_home_goals_avg | 0.087 | -0.047 | 0.032 |
| away_team_away_goals_avg | -0.054 | 0.093 | 0.025 |
| home_team_home_conceded_avg | -0.017 | 0.049 | 0.021 |
| away_team_points_last_5 | -0.043 | 0.017 | -0.021 |
| home_team_points_last_5 | 0.142 | -0.123 | 0.020 |
| home_rest_days | -0.055 | 0.031 | -0.019 |
| home_position_before_match | -0.153 | 0.140 | -0.016 |
| away_rest_days | -0.049 | 0.037 | -0.010 |
| home_team_wins_last_5 | 0.126 | -0.120 | 0.009 |
| home_team_home_win_rate | 0.047 | -0.056 | -0.005 |
| away_points_before_match | -0.004 | 0.010 | 0.004 |
| away_team_goals_scored_last_5 | -0.036 | 0.044 | 0.004 |
| away_team_away_win_rate | -0.058 | 0.064 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 58 | 21 | 13 | 24 | 36.2% | 22.4% | 41.4% |
| -4..-2 | 87 | 34 | 17 | 36 | 39.1% | 19.5% | 41.4% |
| -1..1 | 107 | 50 | 30 | 27 | 46.7% | 28.0% | 25.2% |
| 2..4 | 72 | 32 | 19 | 21 | 44.4% | 26.4% | 29.2% |
| >4 | 56 | 38 | 10 | 8 | 67.9% | 17.9% | 14.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 96 | 59 | 20 | 17 | 61.5% | 20.8% | 17.7% |
| -5..-2 | 59 | 26 | 19 | 14 | 44.1% | 32.2% | 23.7% |
| -1..1 | 45 | 22 | 12 | 11 | 48.9% | 26.7% | 24.4% |
| 2..5 | 78 | 35 | 13 | 30 | 44.9% | 16.7% | 38.5% |
| >=6 | 102 | 33 | 25 | 44 | 32.4% | 24.5% | 43.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 8 | 5 | 0 | 3 | 62.5% | 0.0% | 37.5% |
| -1..0 | 104 | 45 | 26 | 33 | 43.3% | 25.0% | 31.7% |
| 0 | 164 | 83 | 29 | 52 | 50.6% | 17.7% | 31.7% |
| 1..2 | 94 | 39 | 27 | 28 | 41.5% | 28.7% | 29.8% |
| >2 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 10 | 3 | 7 | 0 | 30.0% | 70.0% | 0.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **46.7%** home win (99/212)
- `>= 0.5` tier: **45.2%** home win (76/168)
- Home-win gap (>= split minus < split): **-1.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 212 | 99 | 42 | 71 | 46.7% |
| high | >= 0.5 | 168 | 76 | 47 | 45 | 45.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.771 | -0.315 | -4.698 | 7.470 |
| home_points_before_match | 27.766 | 24.247 | 22.621 | 5.145 |
| position_difference | -1.566 | 0.303 | 3.216 | 4.781 |
| home_position_before_match | 10.074 | 10.045 | 12.974 | 2.929 |
| away_points_before_match | 24.994 | 24.562 | 27.319 | 2.757 |
| away_position_before_match | 11.640 | 9.742 | 9.759 | 1.898 |
| home_team_goals_conceded_last_5 | 7.046 | 6.685 | 8.147 | 1.461 |
| home_team_points_last_5 | 6.857 | 6.157 | 5.414 | 1.443 |
| home_team_goals_scored_last_5 | 7.777 | 6.742 | 6.586 | 1.191 |
| away_rest_days | 7.669 | 7.220 | 8.293 | 1.074 |
| home_rest_days | 7.605 | 7.268 | 8.267 | 0.999 |
| away_team_goals_conceded_last_5 | 7.577 | 6.764 | 7.017 | 0.813 |
| away_team_points_last_5 | 6.166 | 6.382 | 6.974 | 0.808 |
| away_team_goals_scored_last_5 | 7.114 | 7.090 | 7.879 | 0.789 |
| home_team_wins_last_5 | 1.914 | 1.663 | 1.448 | 0.466 |
| away_team_wins_last_5 | 1.686 | 1.775 | 1.966 | 0.280 |
| away_team_away_goals_avg | 1.291 | 1.330 | 1.508 | 0.217 |
| home_team_home_conceded_avg | 1.325 | 1.300 | 1.452 | 0.152 |
| away_team_away_conceded_avg | 1.611 | 1.480 | 1.530 | 0.131 |
| home_team_home_goals_avg | 1.614 | 1.556 | 1.484 | 0.130 |
| rest_days_difference | -0.064 | 0.049 | -0.026 | 0.113 |
| away_team_away_win_rate | 0.268 | 0.275 | 0.324 | 0.056 |
| home_team_home_win_rate | 0.431 | 0.428 | 0.388 | 0.043 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\germany3\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\germany3\charts\relationships_home_win_pct_by_position.png)

