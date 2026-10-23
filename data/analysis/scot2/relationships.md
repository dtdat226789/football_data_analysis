# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:06:38+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: League Two (Scotland)
- Scope: league `scot2`

- Matches analysed: **188** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_win_rate | 0.040 | 0.169 | 0.168 |
| home_team_home_goals_avg | 0.111 | 0.046 | 0.119 |
| away_rest_days | -0.011 | 0.124 | 0.094 |
| home_team_home_win_rate | 0.144 | -0.024 | 0.087 |
| rest_days_difference | -0.054 | -0.039 | -0.072 |
| home_team_home_conceded_avg | 0.063 | 0.030 | 0.071 |
| away_position_before_match | 0.037 | -0.120 | -0.071 |
| home_points_before_match | 0.101 | -0.169 | -0.063 |
| away_team_away_goals_avg | -0.037 | 0.110 | 0.062 |
| points_difference | 0.026 | -0.099 | -0.062 |
| away_team_goals_scored_last_5 | -0.094 | 0.011 | -0.060 |
| position_difference | -0.041 | 0.108 | 0.058 |
| home_rest_days | -0.048 | 0.104 | 0.050 |
| home_team_goals_conceded_last_5 | 0.055 | -0.022 | 0.023 |
| away_team_goals_conceded_last_5 | 0.076 | -0.091 | -0.018 |
| away_points_before_match | 0.081 | -0.093 | -0.016 |
| home_position_before_match | -0.020 | 0.032 | 0.011 |
| home_team_goals_scored_last_5 | 0.037 | -0.022 | 0.010 |
| away_team_away_conceded_avg | 0.032 | -0.040 | -0.009 |
| away_team_points_last_5 | -0.090 | 0.071 | -0.009 |
| home_team_points_last_5 | 0.001 | -0.010 | -0.007 |
| away_team_wins_last_5 | -0.077 | 0.075 | 0.004 |
| home_team_wins_last_5 | 0.018 | -0.019 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 32 | 15 | 11 | 6 | 46.9% | 34.4% | 18.8% |
| -4..-2 | 34 | 7 | 12 | 15 | 20.6% | 35.3% | 44.1% |
| -1..1 | 62 | 25 | 16 | 21 | 40.3% | 25.8% | 33.9% |
| 2..4 | 39 | 18 | 11 | 10 | 46.2% | 28.2% | 25.6% |
| >4 | 21 | 10 | 5 | 6 | 47.6% | 23.8% | 28.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 21 | 10 | 4 | 7 | 47.6% | 19.0% | 33.3% |
| -5..-2 | 47 | 20 | 13 | 14 | 42.6% | 27.7% | 29.8% |
| -1..1 | 35 | 15 | 11 | 9 | 42.9% | 31.4% | 25.7% |
| 2..5 | 64 | 24 | 20 | 20 | 37.5% | 31.2% | 31.2% |
| >=6 | 21 | 6 | 7 | 8 | 28.6% | 33.3% | 38.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 13 | 5 | 3 | 5 | 38.5% | 23.1% | 38.5% |
| -1..0 | 0 | 0 | 0 | 0 | - | - | - |
| 0 | 155 | 62 | 47 | 46 | 40.0% | 30.3% | 29.7% |
| 1..2 | 0 | 0 | 0 | 0 | - | - | - |
| >2 | 13 | 5 | 4 | 4 | 38.5% | 30.8% | 30.8% |
| unknown | 7 | 3 | 1 | 3 | 42.9% | 14.3% | 42.9% |
- *7 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **40.4%** home win (59/146)
- `>= 0.5` tier: **38.1%** home win (16/42)
- Home-win gap (>= split minus < split): **-2.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 146 | 59 | 41 | 46 | 40.4% |
| high | >= 0.5 | 42 | 16 | 14 | 12 | 38.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 26.840 | 23.309 | 20.966 | 5.874 |
| away_points_before_match | 26.467 | 24.691 | 21.155 | 5.311 |
| points_difference | 0.373 | -1.382 | -0.190 | 1.755 |
| away_team_goals_scored_last_5 | 6.253 | 7.655 | 6.397 | 1.401 |
| away_team_points_last_5 | 5.787 | 7.182 | 6.328 | 1.395 |
| position_difference | -0.440 | 0.836 | 0.276 | 1.276 |
| away_rest_days | 7.167 | 7.927 | 8.200 | 1.033 |
| home_position_before_match | 5.320 | 6.091 | 5.328 | 0.771 |
| away_position_before_match | 5.760 | 5.255 | 5.052 | 0.708 |
| home_rest_days | 7.222 | 7.796 | 7.929 | 0.706 |
| home_team_goals_conceded_last_5 | 7.067 | 6.691 | 6.362 | 0.705 |
| away_team_goals_conceded_last_5 | 6.893 | 6.509 | 6.207 | 0.686 |
| away_team_wins_last_5 | 1.480 | 1.982 | 1.690 | 0.502 |
| home_team_points_last_5 | 5.867 | 6.236 | 6.207 | 0.370 |
| home_team_goals_scored_last_5 | 6.853 | 6.600 | 6.534 | 0.319 |
| away_team_away_goals_avg | 1.298 | 1.612 | 1.498 | 0.314 |
| rest_days_difference | 0.056 | -0.148 | -0.182 | 0.237 |
| home_team_wins_last_5 | 1.507 | 1.691 | 1.603 | 0.184 |
| home_team_home_conceded_avg | 1.457 | 1.504 | 1.364 | 0.140 |
| away_team_away_conceded_avg | 1.367 | 1.376 | 1.236 | 0.140 |
| away_team_away_win_rate | 0.304 | 0.388 | 0.416 | 0.112 |
| home_team_home_goals_avg | 1.375 | 1.370 | 1.291 | 0.084 |
| home_team_home_win_rate | 0.336 | 0.323 | 0.290 | 0.046 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\scot2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\scot2\charts\relationships_home_win_pct_by_position.png)

