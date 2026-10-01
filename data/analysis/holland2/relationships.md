# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:53:17+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Eerste Divisie (Netherlands)
- Scope: league `holland2`

- Matches analysed: **392** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_rest_days | 0.103 | 0.086 | 0.140 |
| away_team_goals_scored_last_5 | 0.052 | 0.127 | 0.129 |
| away_team_wins_last_5 | -0.001 | 0.162 | 0.112 |
| position_difference | -0.058 | 0.208 | 0.100 |
| away_team_points_last_5 | -0.001 | 0.140 | 0.097 |
| away_rest_days | 0.073 | 0.050 | 0.091 |
| away_position_before_match | 0.029 | -0.161 | -0.090 |
| away_team_away_conceded_avg | -0.040 | -0.076 | -0.084 |
| rest_days_difference | 0.033 | 0.065 | 0.070 |
| away_team_away_win_rate | -0.049 | 0.148 | 0.065 |
| home_team_points_last_5 | 0.060 | 0.011 | 0.054 |
| home_team_wins_last_5 | 0.081 | -0.016 | 0.052 |
| home_points_before_match | 0.004 | -0.074 | -0.049 |
| home_position_before_match | -0.051 | 0.127 | 0.049 |
| away_team_away_goals_avg | -0.040 | 0.106 | 0.043 |
| points_difference | 0.110 | -0.182 | -0.042 |
| home_team_goals_scored_last_5 | 0.056 | -0.004 | 0.041 |
| home_team_home_win_rate | 0.000 | -0.051 | -0.035 |
| away_points_before_match | -0.073 | 0.053 | -0.020 |
| home_team_home_goals_avg | 0.025 | -0.050 | -0.016 |
| home_team_goals_conceded_last_5 | -0.046 | 0.032 | -0.013 |
| home_team_home_conceded_avg | 0.035 | -0.026 | 0.009 |
| away_team_goals_conceded_last_5 | 0.031 | -0.043 | -0.006 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 67 | 22 | 14 | 31 | 32.8% | 20.9% | 46.3% |
| -4..-2 | 78 | 30 | 21 | 27 | 38.5% | 26.9% | 34.6% |
| -1..1 | 97 | 48 | 17 | 32 | 49.5% | 17.5% | 33.0% |
| 2..4 | 96 | 48 | 21 | 27 | 50.0% | 21.9% | 28.1% |
| >4 | 54 | 19 | 12 | 23 | 35.2% | 22.2% | 42.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 95 | 45 | 25 | 25 | 47.4% | 26.3% | 26.3% |
| -5..-2 | 82 | 37 | 20 | 25 | 45.1% | 24.4% | 30.5% |
| -1..1 | 42 | 23 | 5 | 14 | 54.8% | 11.9% | 33.3% |
| 2..5 | 63 | 23 | 10 | 30 | 36.5% | 15.9% | 47.6% |
| >=6 | 110 | 39 | 25 | 46 | 35.5% | 22.7% | 41.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 71 | 32 | 15 | 24 | 45.1% | 21.1% | 33.8% |
| -1..0 | 37 | 10 | 9 | 18 | 27.0% | 24.3% | 48.6% |
| 0 | 185 | 77 | 47 | 61 | 41.6% | 25.4% | 33.0% |
| 1..2 | 45 | 23 | 8 | 14 | 51.1% | 17.8% | 31.1% |
| >2 | 42 | 17 | 6 | 19 | 40.5% | 14.3% | 45.2% |
| unknown | 12 | 8 | 0 | 4 | 66.7% | 0.0% | 33.3% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **43.0%** home win (105/244)
- `>= 0.5` tier: **41.9%** home win (62/148)
- Home-win gap (>= split minus < split): **-1.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 244 | 105 | 48 | 91 | 43.0% |
| high | >= 0.5 | 148 | 62 | 37 | 49 | 41.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.928 | 0.388 | -2.836 | 4.764 |
| away_points_before_match | 25.533 | 26.847 | 28.500 | 2.967 |
| position_difference | -0.862 | 0.071 | 1.914 | 2.777 |
| home_points_before_match | 27.461 | 27.235 | 25.664 | 1.797 |
| home_position_before_match | 9.916 | 10.871 | 11.329 | 1.412 |
| away_position_before_match | 10.778 | 10.800 | 9.414 | 1.386 |
| home_team_goals_conceded_last_5 | 7.126 | 8.153 | 7.436 | 1.027 |
| away_team_goals_conceded_last_5 | 7.174 | 7.824 | 6.971 | 0.852 |
| rest_days_difference | -0.252 | -0.612 | 0.184 | 0.796 |
| away_team_points_last_5 | 6.210 | 6.424 | 6.886 | 0.676 |
| home_rest_days | 6.669 | 6.447 | 7.036 | 0.589 |
| home_team_goals_scored_last_5 | 7.395 | 7.529 | 7.100 | 0.429 |
| away_team_wins_last_5 | 1.713 | 1.788 | 2.000 | 0.287 |
| away_team_goals_scored_last_5 | 7.449 | 7.659 | 7.629 | 0.210 |
| home_team_points_last_5 | 6.419 | 6.329 | 6.514 | 0.185 |
| away_rest_days | 6.874 | 7.059 | 6.882 | 0.185 |
| home_team_home_goals_avg | 1.707 | 1.737 | 1.602 | 0.135 |
| away_team_away_conceded_avg | 1.683 | 1.743 | 1.639 | 0.104 |
| away_team_away_goals_avg | 1.320 | 1.339 | 1.420 | 0.100 |
| home_team_home_conceded_avg | 1.339 | 1.395 | 1.301 | 0.094 |
| away_team_away_win_rate | 0.303 | 0.354 | 0.358 | 0.055 |
| home_team_wins_last_5 | 1.826 | 1.776 | 1.807 | 0.050 |
| home_team_home_win_rate | 0.435 | 0.454 | 0.414 | 0.040 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\holland2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\holland2\charts\relationships_home_win_pct_by_position.png)

