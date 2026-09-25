# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:45:49+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Segunda RFEF - Group 2 (Spain)
- Scope: league `segunda2`

- Matches analysed: **333** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_points_before_match | 0.123 | -0.021 | 0.084 |
| home_team_goals_scored_last_5 | 0.159 | -0.107 | 0.058 |
| points_difference | 0.201 | -0.170 | 0.051 |
| away_points_before_match | -0.007 | 0.088 | 0.051 |
| position_difference | -0.216 | 0.202 | -0.043 |
| home_position_before_match | -0.155 | 0.129 | -0.041 |
| away_team_away_win_rate | -0.071 | 0.026 | -0.039 |
| away_team_points_last_5 | -0.090 | 0.050 | -0.039 |
| home_team_home_win_rate | -0.043 | 0.001 | -0.033 |
| away_team_wins_last_5 | -0.082 | 0.063 | -0.025 |
| home_team_home_goals_avg | 0.034 | -0.076 | -0.022 |
| home_rest_days | -0.034 | 0.011 | -0.020 |
| away_position_before_match | 0.140 | -0.146 | 0.018 |
| away_rest_days | -0.017 | -0.002 | -0.015 |
| home_team_home_conceded_avg | -0.063 | 0.057 | -0.014 |
| away_team_goals_scored_last_5 | -0.042 | 0.071 | 0.012 |
| home_team_points_last_5 | 0.083 | -0.085 | 0.012 |
| rest_days_difference | -0.036 | 0.028 | -0.011 |
| home_team_goals_conceded_last_5 | -0.037 | 0.029 | -0.010 |
| away_team_goals_conceded_last_5 | 0.072 | -0.099 | -0.006 |
| away_team_away_goals_avg | 0.017 | -0.029 | -0.005 |
| home_team_wins_last_5 | 0.056 | -0.074 | -0.003 |
| away_team_away_conceded_avg | 0.062 | -0.076 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 45 | 16 | 13 | 16 | 35.6% | 28.9% | 35.6% |
| -4..-2 | 72 | 26 | 23 | 23 | 36.1% | 31.9% | 31.9% |
| -1..1 | 114 | 47 | 29 | 38 | 41.2% | 25.4% | 33.3% |
| 2..4 | 70 | 36 | 19 | 15 | 51.4% | 27.1% | 21.4% |
| >4 | 32 | 17 | 12 | 3 | 53.1% | 37.5% | 9.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 64 | 42 | 14 | 8 | 65.6% | 21.9% | 12.5% |
| -5..-2 | 70 | 34 | 21 | 15 | 48.6% | 30.0% | 21.4% |
| -1..1 | 51 | 18 | 20 | 13 | 35.3% | 39.2% | 25.5% |
| 2..5 | 67 | 23 | 17 | 27 | 34.3% | 25.4% | 40.3% |
| >=6 | 81 | 25 | 24 | 32 | 30.9% | 29.6% | 39.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 1 | 1 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| -1..0 | 72 | 31 | 21 | 20 | 43.1% | 29.2% | 27.8% |
| 0 | 179 | 76 | 50 | 53 | 42.5% | 27.9% | 29.6% |
| 1..2 | 61 | 27 | 18 | 16 | 44.3% | 29.5% | 26.2% |
| >2 | 2 | 1 | 0 | 1 | 50.0% | 0.0% | 50.0% |
| unknown | 18 | 6 | 7 | 5 | 33.3% | 38.9% | 27.8% |
- *18 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **48.3%** home win (29/60)
- `>= 0.5` tier: **41.4%** home win (113/273)
- Home-win gap (>= split minus < split): **-6.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 60 | 29 | 18 | 13 | 48.3% |
| high | >= 0.5 | 273 | 113 | 78 | 82 | 41.4% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.732 | -0.354 | -3.453 | 5.185 |
| position_difference | -1.282 | 0.604 | 2.789 | 4.071 |
| away_points_before_match | 19.148 | 21.240 | 22.895 | 3.747 |
| away_position_before_match | 10.627 | 9.115 | 8.137 | 2.490 |
| home_position_before_match | 9.345 | 9.719 | 10.926 | 1.581 |
| home_points_before_match | 20.880 | 20.885 | 19.442 | 1.443 |
| home_team_goals_conceded_last_5 | 5.430 | 4.927 | 6.084 | 1.157 |
| away_team_goals_conceded_last_5 | 5.775 | 4.875 | 4.853 | 0.922 |
| away_team_points_last_5 | 5.535 | 6.115 | 6.295 | 0.760 |
| home_team_goals_scored_last_5 | 5.465 | 5.281 | 4.768 | 0.696 |
| home_team_points_last_5 | 5.775 | 5.833 | 5.200 | 0.633 |
| away_team_goals_scored_last_5 | 5.408 | 5.302 | 5.874 | 0.572 |
| away_team_wins_last_5 | 2.676 | 2.719 | 3.095 | 0.419 |
| away_team_away_conceded_avg | 1.367 | 1.145 | 1.079 | 0.289 |
| home_team_wins_last_5 | 2.761 | 2.833 | 2.568 | 0.265 |
| home_team_home_conceded_avg | 0.903 | 0.892 | 1.070 | 0.178 |
| home_rest_days | 7.162 | 7.112 | 7.278 | 0.165 |
| away_rest_days | 7.176 | 7.146 | 7.289 | 0.143 |
| away_team_away_goals_avg | 1.007 | 0.922 | 0.900 | 0.107 |
| away_team_away_win_rate | 0.487 | 0.486 | 0.557 | 0.071 |
| home_team_home_win_rate | 0.650 | 0.640 | 0.669 | 0.030 |
| rest_days_difference | -0.015 | -0.034 | -0.011 | 0.023 |
| home_team_home_goals_avg | 1.221 | 1.213 | 1.200 | 0.021 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\segunda2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\segunda2\charts\relationships_home_win_pct_by_position.png)

