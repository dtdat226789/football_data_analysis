# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:00:16+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: K League 1 (South Korea)
- Scope: league `korea1`

- Matches analysed: **198** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_scored_last_5 | 0.220 | 0.102 | 0.221 |
| home_points_before_match | 0.222 | 0.018 | 0.167 |
| away_team_goals_conceded_last_5 | 0.168 | 0.030 | 0.137 |
| away_team_away_goals_avg | 0.057 | 0.144 | 0.135 |
| away_points_before_match | 0.122 | 0.066 | 0.129 |
| away_team_away_conceded_avg | 0.172 | 0.012 | 0.128 |
| home_team_home_goals_avg | 0.069 | 0.103 | 0.117 |
| home_team_goals_scored_last_5 | 0.120 | 0.025 | 0.100 |
| away_rest_days | 0.128 | -0.009 | 0.083 |
| home_team_home_win_rate | -0.002 | 0.128 | 0.083 |
| home_team_points_last_5 | 0.123 | -0.010 | 0.079 |
| away_team_wins_last_5 | 0.058 | 0.046 | 0.071 |
| away_position_before_match | 0.149 | -0.054 | 0.068 |
| position_difference | -0.141 | 0.048 | -0.067 |
| away_team_points_last_5 | 0.053 | 0.039 | 0.063 |
| home_team_home_conceded_avg | 0.002 | -0.095 | -0.062 |
| home_rest_days | 0.121 | -0.042 | 0.057 |
| points_difference | 0.147 | -0.070 | 0.056 |
| home_team_wins_last_5 | 0.095 | -0.050 | 0.033 |
| home_position_before_match | -0.051 | 0.013 | -0.027 |
| rest_days_difference | 0.015 | -0.053 | -0.024 |
| home_team_goals_conceded_last_5 | 0.011 | 0.007 | 0.012 |
| away_team_away_win_rate | -0.105 | 0.117 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 37 | 15 | 10 | 12 | 40.5% | 27.0% | 32.4% |
| -4..-2 | 31 | 13 | 9 | 9 | 41.9% | 29.0% | 29.0% |
| -1..1 | 59 | 24 | 11 | 24 | 40.7% | 18.6% | 40.7% |
| 2..4 | 40 | 17 | 12 | 11 | 42.5% | 30.0% | 27.5% |
| >4 | 31 | 14 | 10 | 7 | 45.2% | 32.3% | 22.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 27 | 13 | 7 | 7 | 48.1% | 25.9% | 25.9% |
| -5..-2 | 50 | 27 | 12 | 11 | 54.0% | 24.0% | 22.0% |
| -1..1 | 41 | 17 | 8 | 16 | 41.5% | 19.5% | 39.0% |
| 2..5 | 52 | 17 | 15 | 20 | 32.7% | 28.8% | 38.5% |
| >=6 | 28 | 9 | 10 | 9 | 32.1% | 35.7% | 32.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 15 | 6 | 3 | 6 | 40.0% | 20.0% | 40.0% |
| -1..0 | 58 | 21 | 17 | 20 | 36.2% | 29.3% | 34.5% |
| 0 | 65 | 25 | 20 | 20 | 38.5% | 30.8% | 30.8% |
| 1..2 | 45 | 23 | 8 | 14 | 51.1% | 17.8% | 31.1% |
| >2 | 9 | 5 | 3 | 1 | 55.6% | 33.3% | 11.1% |
| unknown | 6 | 3 | 1 | 2 | 50.0% | 16.7% | 33.3% |
- *6 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **44.8%** home win (60/134)
- `>= 0.5` tier: **35.9%** home win (23/64)
- Home-win gap (>= split minus < split): **-8.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 134 | 60 | 38 | 36 | 44.8% |
| high | >= 0.5 | 64 | 23 | 14 | 27 | 35.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.169 | -1.750 | -1.317 | 3.919 |
| home_points_before_match | 23.843 | 20.885 | 20.270 | 3.574 |
| position_difference | -0.892 | 0.654 | 0.667 | 1.558 |
| home_rest_days | 8.287 | 7.588 | 6.787 | 1.501 |
| away_position_before_match | 7.205 | 6.462 | 5.984 | 1.221 |
| away_points_before_match | 21.675 | 22.635 | 21.587 | 1.047 |
| away_rest_days | 8.213 | 7.294 | 7.230 | 0.983 |
| home_position_before_match | 6.313 | 7.115 | 6.651 | 0.802 |
| rest_days_difference | 0.075 | 0.294 | -0.443 | 0.737 |
| away_team_goals_scored_last_5 | 6.108 | 5.423 | 5.714 | 0.685 |
| home_team_points_last_5 | 6.530 | 6.192 | 5.937 | 0.594 |
| home_team_goals_scored_last_5 | 6.048 | 5.712 | 5.635 | 0.413 |
| away_team_goals_conceded_last_5 | 5.892 | 5.865 | 5.556 | 0.336 |
| away_team_points_last_5 | 6.337 | 6.058 | 6.238 | 0.280 |
| home_team_wins_last_5 | 1.795 | 1.731 | 1.556 | 0.240 |
| home_team_goals_conceded_last_5 | 5.747 | 5.981 | 5.889 | 0.234 |
| home_team_home_goals_avg | 1.042 | 1.107 | 1.208 | 0.167 |
| away_team_away_goals_avg | 0.954 | 1.079 | 1.100 | 0.146 |
| away_team_away_conceded_avg | 1.145 | 1.157 | 1.032 | 0.125 |
| away_team_wins_last_5 | 1.747 | 1.635 | 1.667 | 0.112 |
| home_team_home_conceded_avg | 1.029 | 1.112 | 1.000 | 0.112 |
| away_team_away_win_rate | 0.258 | 0.315 | 0.360 | 0.101 |
| home_team_home_win_rate | 0.352 | 0.387 | 0.431 | 0.080 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\korea1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\korea1\charts\relationships_home_win_pct_by_position.png)

