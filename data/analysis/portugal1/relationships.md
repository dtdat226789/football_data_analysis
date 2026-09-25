# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:41:41+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Liga Portugal (Portugal)
- Scope: league `portugal1`

- Matches analysed: **370** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.231 | -0.106 | 0.110 |
| home_position_before_match | -0.302 | 0.195 | -0.103 |
| home_team_points_last_5 | 0.233 | -0.148 | 0.080 |
| rest_days_difference | -0.043 | -0.054 | -0.076 |
| home_team_wins_last_5 | 0.195 | -0.122 | 0.069 |
| home_team_home_goals_avg | 0.182 | -0.117 | 0.062 |
| position_difference | -0.364 | 0.321 | -0.058 |
| points_difference | 0.312 | -0.267 | 0.057 |
| home_points_before_match | 0.207 | -0.152 | 0.056 |
| away_rest_days | 0.026 | 0.043 | 0.054 |
| away_team_away_goals_avg | -0.129 | 0.205 | 0.049 |
| away_team_wins_last_5 | -0.096 | 0.166 | 0.046 |
| away_team_goals_scored_last_5 | -0.110 | 0.176 | 0.042 |
| away_team_goals_conceded_last_5 | 0.125 | -0.192 | -0.042 |
| away_team_points_last_5 | -0.125 | 0.182 | 0.034 |
| home_team_home_win_rate | 0.135 | -0.104 | 0.033 |
| away_position_before_match | 0.196 | -0.244 | -0.023 |
| home_team_goals_conceded_last_5 | -0.144 | 0.130 | -0.021 |
| away_team_away_conceded_avg | 0.146 | -0.174 | -0.011 |
| home_team_home_conceded_avg | -0.149 | 0.151 | -0.009 |
| away_points_before_match | -0.066 | 0.081 | 0.007 |
| home_rest_days | -0.001 | 0.007 | 0.005 |
| away_team_away_win_rate | -0.148 | 0.168 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 67 | 9 | 18 | 40 | 13.4% | 26.9% | 59.7% |
| -4..-2 | 63 | 26 | 14 | 23 | 41.3% | 22.2% | 36.5% |
| -1..1 | 113 | 43 | 35 | 35 | 38.1% | 31.0% | 31.0% |
| 2..4 | 67 | 38 | 17 | 12 | 56.7% | 25.4% | 17.9% |
| >4 | 60 | 35 | 18 | 7 | 58.3% | 30.0% | 11.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 84 | 56 | 18 | 10 | 66.7% | 21.4% | 11.9% |
| -5..-2 | 69 | 39 | 18 | 12 | 56.5% | 26.1% | 17.4% |
| -1..1 | 67 | 25 | 21 | 21 | 37.3% | 31.3% | 31.3% |
| 2..5 | 65 | 17 | 20 | 28 | 26.2% | 30.8% | 43.1% |
| >=6 | 85 | 14 | 25 | 46 | 16.5% | 29.4% | 54.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 44 | 19 | 7 | 18 | 43.2% | 15.9% | 40.9% |
| -1..0 | 81 | 35 | 20 | 26 | 43.2% | 24.7% | 32.1% |
| 0 | 92 | 39 | 26 | 27 | 42.4% | 28.3% | 29.3% |
| 1..2 | 116 | 40 | 36 | 40 | 34.5% | 31.0% | 34.5% |
| >2 | 17 | 10 | 5 | 2 | 58.8% | 29.4% | 11.8% |
| unknown | 20 | 8 | 8 | 4 | 40.0% | 40.0% | 20.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **31.8%** home win (34/107)
- `>= 0.5` tier: **44.5%** home win (117/263)
- Home-win gap (>= split minus < split): **+12.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 107 | 34 | 33 | 40 | 31.8% |
| high | >= 0.5 | 263 | 117 | 69 | 77 | 44.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 6.609 | -1.451 | -7.291 | 13.900 |
| home_points_before_match | 23.815 | 18.529 | 14.615 | 9.199 |
| position_difference | -3.166 | 0.882 | 3.744 | 6.909 |
| away_points_before_match | 17.205 | 19.980 | 21.906 | 4.701 |
| home_position_before_match | 7.828 | 10.549 | 11.462 | 3.634 |
| away_position_before_match | 10.993 | 9.667 | 7.718 | 3.275 |
| home_team_points_last_5 | 6.821 | 5.549 | 4.538 | 2.283 |
| home_team_goals_scored_last_5 | 6.589 | 5.382 | 4.709 | 1.880 |
| away_team_points_last_5 | 5.252 | 5.539 | 7.000 | 1.748 |
| away_team_goals_conceded_last_5 | 6.384 | 5.686 | 4.675 | 1.709 |
| away_team_goals_scored_last_5 | 5.285 | 5.422 | 6.855 | 1.570 |
| away_rest_days | 8.168 | 7.417 | 8.903 | 1.486 |
| home_team_goals_conceded_last_5 | 5.179 | 6.049 | 6.487 | 1.308 |
| home_rest_days | 8.294 | 7.819 | 8.614 | 0.795 |
| home_team_wins_last_5 | 3.020 | 2.549 | 2.350 | 0.669 |
| rest_days_difference | 0.126 | 0.372 | -0.257 | 0.629 |
| away_team_wins_last_5 | 2.470 | 2.676 | 3.068 | 0.598 |
| away_team_away_conceded_avg | 1.504 | 1.299 | 1.053 | 0.451 |
| home_team_home_goals_avg | 1.473 | 1.270 | 1.110 | 0.363 |
| away_team_away_goals_avg | 0.994 | 1.112 | 1.353 | 0.359 |
| home_team_home_conceded_avg | 0.981 | 1.149 | 1.299 | 0.318 |
| away_team_away_win_rate | 0.484 | 0.554 | 0.642 | 0.158 |
| home_team_home_win_rate | 0.641 | 0.570 | 0.526 | 0.115 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\portugal1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\portugal1\charts\relationships_home_win_pct_by_position.png)

