# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:55:45+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premier Division (Ireland)
- Scope: league `ireland1`

- Matches analysed: **180** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_conceded_last_5 | -0.222 | 0.032 | -0.139 |
| home_team_home_goals_avg | -0.069 | -0.127 | -0.130 |
| away_position_before_match | 0.208 | -0.063 | 0.109 |
| position_difference | -0.244 | 0.104 | -0.108 |
| away_team_away_win_rate | -0.135 | -0.003 | -0.098 |
| points_difference | 0.213 | -0.092 | 0.094 |
| away_points_before_match | -0.112 | -0.022 | -0.094 |
| away_team_away_conceded_avg | 0.111 | 0.005 | 0.083 |
| home_team_goals_scored_last_5 | -0.026 | -0.100 | -0.082 |
| away_team_away_goals_avg | -0.028 | -0.064 | -0.061 |
| away_team_wins_last_5 | -0.147 | 0.076 | -0.057 |
| away_team_points_last_5 | -0.135 | 0.069 | -0.053 |
| home_team_home_conceded_avg | -0.114 | 0.047 | -0.052 |
| home_rest_days | -0.088 | 0.027 | -0.046 |
| home_position_before_match | -0.128 | 0.081 | -0.041 |
| home_team_home_win_rate | -0.031 | -0.022 | -0.036 |
| away_team_goals_conceded_last_5 | 0.097 | -0.061 | 0.031 |
| home_points_before_match | 0.032 | -0.083 | -0.030 |
| rest_days_difference | 0.065 | -0.119 | -0.029 |
| away_team_goals_scored_last_5 | -0.030 | -0.002 | -0.022 |
| away_rest_days | -0.146 | 0.133 | -0.021 |
| home_team_wins_last_5 | 0.050 | -0.062 | -0.004 |
| home_team_points_last_5 | 0.062 | -0.075 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 29 | 8 | 8 | 13 | 27.6% | 27.6% | 44.8% |
| -4..-2 | 39 | 15 | 14 | 10 | 38.5% | 35.9% | 25.6% |
| -1..1 | 58 | 31 | 13 | 14 | 53.4% | 22.4% | 24.1% |
| 2..4 | 32 | 13 | 10 | 9 | 40.6% | 31.2% | 28.1% |
| >4 | 22 | 10 | 7 | 5 | 45.5% | 31.8% | 22.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 16 | 9 | 4 | 3 | 56.2% | 25.0% | 18.8% |
| -5..-2 | 53 | 29 | 11 | 13 | 54.7% | 20.8% | 24.5% |
| -1..1 | 43 | 14 | 16 | 13 | 32.6% | 37.2% | 30.2% |
| 2..5 | 46 | 21 | 13 | 12 | 45.7% | 28.3% | 26.1% |
| >=6 | 22 | 4 | 8 | 10 | 18.2% | 36.4% | 45.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 22 | 8 | 7 | 7 | 36.4% | 31.8% | 31.8% |
| -1..0 | 14 | 5 | 5 | 4 | 35.7% | 35.7% | 28.6% |
| 0 | 110 | 50 | 30 | 30 | 45.5% | 27.3% | 27.3% |
| 1..2 | 16 | 4 | 5 | 7 | 25.0% | 31.2% | 43.8% |
| >2 | 13 | 8 | 3 | 2 | 61.5% | 23.1% | 15.4% |
| unknown | 5 | 2 | 2 | 1 | 40.0% | 40.0% | 20.0% |
- *5 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **44.1%** home win (49/111)
- `>= 0.5` tier: **40.6%** home win (28/69)
- Home-win gap (>= split minus < split): **-3.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 111 | 49 | 31 | 31 | 44.1% |
| high | >= 0.5 | 69 | 28 | 21 | 20 | 40.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.558 | -2.038 | -2.451 | 5.009 |
| away_points_before_match | 21.844 | 26.192 | 24.706 | 4.348 |
| away_rest_days | 6.493 | 7.420 | 8.920 | 2.427 |
| home_points_before_match | 24.403 | 24.154 | 22.255 | 2.148 |
| position_difference | -0.792 | 0.654 | 1.098 | 1.890 |
| rest_days_difference | 0.547 | -0.060 | -1.040 | 1.587 |
| away_position_before_match | 6.182 | 4.712 | 4.902 | 1.470 |
| away_team_points_last_5 | 5.649 | 6.788 | 7.059 | 1.409 |
| away_team_goals_conceded_last_5 | 5.896 | 4.942 | 5.196 | 0.954 |
| home_team_goals_conceded_last_5 | 5.455 | 5.808 | 6.314 | 0.859 |
| home_rest_days | 7.040 | 7.360 | 7.880 | 0.840 |
| home_team_goals_scored_last_5 | 5.390 | 6.077 | 5.333 | 0.744 |
| home_team_points_last_5 | 5.987 | 6.481 | 5.804 | 0.677 |
| home_position_before_match | 5.390 | 5.365 | 6.000 | 0.635 |
| away_team_wins_last_5 | 1.429 | 1.827 | 1.922 | 0.493 |
| away_team_goals_scored_last_5 | 5.468 | 5.731 | 5.863 | 0.395 |
| home_team_wins_last_5 | 1.545 | 1.788 | 1.490 | 0.298 |
| home_team_home_goals_avg | 1.257 | 1.472 | 1.263 | 0.215 |
| away_team_away_conceded_avg | 1.419 | 1.220 | 1.295 | 0.199 |
| home_team_home_conceded_avg | 0.988 | 1.027 | 1.061 | 0.074 |
| home_team_home_win_rate | 0.386 | 0.459 | 0.436 | 0.072 |
| away_team_away_win_rate | 0.234 | 0.305 | 0.289 | 0.071 |
| away_team_away_goals_avg | 1.022 | 1.039 | 1.022 | 0.018 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\ireland1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\ireland1\charts\relationships_home_win_pct_by_position.png)

