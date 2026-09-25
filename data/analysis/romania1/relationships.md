# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:43:16+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Superliga (Romania)
- Scope: league `romania1`

- Matches analysed: **429** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_position_before_match | 0.243 | -0.044 | 0.169 |
| away_team_wins_last_5 | -0.221 | 0.025 | -0.163 |
| away_team_points_last_5 | -0.236 | 0.066 | -0.149 |
| away_team_away_win_rate | -0.213 | 0.044 | -0.145 |
| away_team_goals_scored_last_5 | -0.160 | 0.042 | -0.103 |
| position_difference | -0.243 | 0.154 | -0.101 |
| away_points_before_match | -0.123 | -0.002 | -0.101 |
| home_team_home_conceded_avg | -0.175 | 0.076 | -0.094 |
| points_difference | 0.215 | -0.131 | 0.092 |
| away_team_goals_conceded_last_5 | 0.155 | -0.057 | 0.089 |
| away_team_away_goals_avg | -0.151 | 0.053 | -0.089 |
| rest_days_difference | -0.038 | -0.060 | -0.068 |
| home_team_home_goals_avg | 0.025 | -0.140 | -0.066 |
| away_team_away_conceded_avg | 0.106 | -0.035 | 0.063 |
| home_rest_days | -0.081 | 0.011 | -0.059 |
| home_team_goals_conceded_last_5 | -0.148 | 0.109 | -0.052 |
| home_team_points_last_5 | 0.086 | -0.189 | -0.047 |
| home_points_before_match | 0.011 | -0.083 | -0.043 |
| home_team_goals_scored_last_5 | 0.056 | -0.140 | -0.041 |
| home_team_wins_last_5 | 0.056 | -0.140 | -0.041 |
| home_position_before_match | -0.068 | 0.153 | 0.039 |
| home_team_home_win_rate | 0.041 | -0.111 | -0.035 |
| away_rest_days | -0.059 | 0.048 | -0.018 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 68 | 18 | 17 | 33 | 26.5% | 25.0% | 48.5% |
| -4..-2 | 95 | 33 | 27 | 35 | 34.7% | 28.4% | 36.8% |
| -1..1 | 137 | 61 | 48 | 28 | 44.5% | 35.0% | 20.4% |
| 2..4 | 62 | 36 | 14 | 12 | 58.1% | 22.6% | 19.4% |
| >4 | 67 | 51 | 11 | 5 | 76.1% | 16.4% | 7.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 68 | 46 | 14 | 8 | 67.6% | 20.6% | 11.8% |
| -5..-2 | 115 | 65 | 26 | 24 | 56.5% | 22.6% | 20.9% |
| -1..1 | 68 | 23 | 25 | 20 | 33.8% | 36.8% | 29.4% |
| 2..5 | 100 | 41 | 33 | 26 | 41.0% | 33.0% | 26.0% |
| >=6 | 78 | 24 | 19 | 35 | 30.8% | 24.4% | 44.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 70 | 33 | 14 | 23 | 47.1% | 20.0% | 32.9% |
| -1..0 | 97 | 44 | 27 | 26 | 45.4% | 27.8% | 26.8% |
| 0 | 62 | 31 | 17 | 14 | 50.0% | 27.4% | 22.6% |
| 1..2 | 155 | 72 | 44 | 39 | 46.5% | 28.4% | 25.2% |
| >2 | 26 | 10 | 7 | 9 | 38.5% | 26.9% | 34.6% |
| unknown | 19 | 9 | 8 | 2 | 47.4% | 42.1% | 10.5% |
- *19 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.3%** home win (33/99)
- `>= 0.5` tier: **50.3%** home win (166/330)
- Home-win gap (>= split minus < split): **+17.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 99 | 33 | 31 | 35 | 33.3% |
| high | >= 0.5 | 330 | 166 | 86 | 78 | 50.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.774 | -0.419 | -3.850 | 6.623 |
| position_difference | -1.497 | 0.615 | 2.442 | 3.940 |
| away_points_before_match | 22.050 | 21.880 | 25.655 | 3.775 |
| home_points_before_match | 24.824 | 21.462 | 21.805 | 3.363 |
| away_position_before_match | 10.286 | 8.581 | 7.965 | 2.322 |
| away_team_points_last_5 | 5.312 | 6.239 | 7.460 | 2.149 |
| home_position_before_match | 8.789 | 9.197 | 10.407 | 1.618 |
| home_team_points_last_5 | 6.558 | 5.692 | 4.973 | 1.584 |
| home_team_goals_conceded_last_5 | 5.276 | 5.265 | 6.664 | 1.399 |
| away_team_goals_scored_last_5 | 5.070 | 5.846 | 6.389 | 1.319 |
| home_team_goals_scored_last_5 | 5.920 | 5.154 | 4.912 | 1.008 |
| away_team_goals_conceded_last_5 | 5.834 | 5.009 | 5.027 | 0.826 |
| away_team_wins_last_5 | 2.558 | 2.838 | 3.283 | 0.725 |
| home_team_wins_last_5 | 2.950 | 2.701 | 2.513 | 0.436 |
| away_rest_days | 7.616 | 7.655 | 7.910 | 0.294 |
| home_team_home_conceded_avg | 0.941 | 0.967 | 1.162 | 0.221 |
| home_rest_days | 7.791 | 7.844 | 7.982 | 0.191 |
| home_team_home_goals_avg | 1.451 | 1.308 | 1.263 | 0.188 |
| away_team_away_conceded_avg | 1.447 | 1.270 | 1.357 | 0.177 |
| away_team_away_goals_avg | 0.945 | 1.018 | 1.120 | 0.175 |
| rest_days_difference | 0.184 | 0.165 | 0.072 | 0.112 |
| away_team_away_win_rate | 0.486 | 0.508 | 0.589 | 0.104 |
| home_team_home_win_rate | 0.724 | 0.651 | 0.650 | 0.074 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\romania1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\romania1\charts\relationships_home_win_pct_by_position.png)

