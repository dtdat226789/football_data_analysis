# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:43:50+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Saudi Professional League (Saudi Arabia)
- Scope: league `saudi1`

- Matches analysed: **377** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_position_before_match | 0.225 | -0.358 | -0.111 |
| home_team_home_win_rate | 0.221 | -0.090 | 0.093 |
| home_team_goals_conceded_last_5 | -0.183 | 0.055 | -0.092 |
| away_team_goals_conceded_last_5 | 0.102 | -0.215 | -0.090 |
| away_points_before_match | -0.110 | 0.206 | 0.077 |
| home_team_home_goals_avg | 0.236 | -0.126 | 0.076 |
| away_team_points_last_5 | -0.169 | 0.255 | 0.072 |
| home_position_before_match | -0.313 | 0.207 | -0.071 |
| home_team_points_last_5 | 0.258 | -0.165 | 0.063 |
| away_team_goals_scored_last_5 | -0.176 | 0.243 | 0.057 |
| away_team_wins_last_5 | -0.133 | 0.200 | 0.056 |
| home_team_home_conceded_avg | -0.106 | 0.033 | -0.052 |
| away_team_away_conceded_avg | 0.125 | -0.188 | -0.052 |
| away_team_away_goals_avg | -0.167 | 0.224 | 0.050 |
| points_difference | 0.344 | -0.392 | -0.049 |
| home_points_before_match | 0.198 | -0.143 | 0.035 |
| position_difference | -0.389 | 0.410 | 0.030 |
| away_team_away_win_rate | -0.173 | 0.193 | 0.021 |
| away_rest_days | 0.065 | -0.045 | 0.014 |
| home_rest_days | 0.074 | -0.056 | 0.013 |
| home_team_goals_scored_last_5 | 0.201 | -0.179 | 0.011 |
| home_team_wins_last_5 | 0.177 | -0.160 | 0.008 |
| rest_days_difference | 0.027 | -0.033 | -0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 67 | 16 | 8 | 43 | 23.9% | 11.9% | 64.2% |
| -4..-2 | 72 | 20 | 21 | 31 | 27.8% | 29.2% | 43.1% |
| -1..1 | 108 | 40 | 35 | 33 | 37.0% | 32.4% | 30.6% |
| 2..4 | 69 | 40 | 16 | 13 | 58.0% | 23.2% | 18.8% |
| >4 | 61 | 47 | 11 | 3 | 77.0% | 18.0% | 4.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 85 | 61 | 17 | 7 | 71.8% | 20.0% | 8.2% |
| -5..-2 | 76 | 39 | 19 | 18 | 51.3% | 25.0% | 23.7% |
| -1..1 | 56 | 23 | 18 | 15 | 41.1% | 32.1% | 26.8% |
| 2..5 | 68 | 25 | 21 | 22 | 36.8% | 30.9% | 32.4% |
| >=6 | 92 | 15 | 16 | 61 | 16.3% | 17.4% | 66.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 52 | 25 | 11 | 16 | 48.1% | 21.2% | 30.8% |
| -1..0 | 77 | 40 | 16 | 21 | 51.9% | 20.8% | 27.3% |
| 0 | 105 | 39 | 28 | 38 | 37.1% | 26.7% | 36.2% |
| 1..2 | 113 | 43 | 31 | 39 | 38.1% | 27.4% | 34.5% |
| >2 | 11 | 7 | 2 | 2 | 63.6% | 18.2% | 18.2% |
| unknown | 19 | 9 | 3 | 7 | 47.4% | 15.8% | 36.8% |
- *19 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **34.6%** home win (44/127)
- `>= 0.5` tier: **47.6%** home win (119/250)
- Home-win gap (>= split minus < split): **+13.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 127 | 44 | 33 | 50 | 34.6% |
| high | >= 0.5 | 250 | 119 | 58 | 73 | 47.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 6.767 | 0.187 | -10.220 | 16.986 |
| home_points_before_match | 23.810 | 18.165 | 14.520 | 9.289 |
| position_difference | -3.362 | -0.176 | 5.065 | 8.427 |
| away_points_before_match | 17.043 | 17.978 | 24.740 | 7.697 |
| away_position_before_match | 11.479 | 10.879 | 6.813 | 4.666 |
| home_position_before_match | 8.117 | 10.703 | 11.878 | 3.761 |
| away_team_points_last_5 | 5.067 | 5.187 | 7.846 | 2.778 |
| home_team_points_last_5 | 7.018 | 5.308 | 4.537 | 2.482 |
| away_team_goals_scored_last_5 | 5.546 | 6.077 | 8.016 | 2.470 |
| away_team_goals_conceded_last_5 | 6.840 | 7.319 | 4.886 | 2.433 |
| home_team_goals_scored_last_5 | 7.374 | 5.802 | 5.146 | 2.228 |
| home_rest_days | 8.091 | 7.693 | 6.802 | 1.289 |
| home_team_goals_conceded_last_5 | 5.834 | 6.725 | 6.992 | 1.158 |
| away_rest_days | 8.097 | 7.466 | 7.009 | 1.089 |
| away_team_wins_last_5 | 2.429 | 2.374 | 3.179 | 0.805 |
| home_team_wins_last_5 | 2.957 | 2.516 | 2.195 | 0.762 |
| away_team_away_goals_avg | 1.111 | 1.226 | 1.679 | 0.568 |
| away_team_away_conceded_avg | 1.564 | 1.557 | 1.089 | 0.476 |
| rest_days_difference | -0.006 | 0.227 | -0.207 | 0.434 |
| home_team_home_goals_avg | 1.597 | 1.278 | 1.228 | 0.369 |
| away_team_away_win_rate | 0.463 | 0.487 | 0.660 | 0.197 |
| home_team_home_conceded_avg | 1.232 | 1.345 | 1.369 | 0.138 |
| home_team_home_win_rate | 0.634 | 0.561 | 0.500 | 0.135 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\saudi1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\saudi1\charts\relationships_home_win_pct_by_position.png)

