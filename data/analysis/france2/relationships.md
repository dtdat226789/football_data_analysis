# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:50:19+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Ligue 2 (France)
- Scope: league `france2`

- Matches analysed: **310** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_win_rate | 0.178 | -0.035 | 0.101 |
| home_position_before_match | -0.207 | 0.083 | -0.089 |
| away_team_goals_conceded_last_5 | 0.039 | 0.075 | 0.075 |
| home_points_before_match | 0.133 | -0.033 | 0.071 |
| away_team_points_last_5 | -0.063 | -0.031 | -0.064 |
| points_difference | 0.197 | -0.114 | 0.062 |
| away_team_wins_last_5 | -0.048 | -0.042 | -0.061 |
| position_difference | -0.187 | 0.107 | -0.060 |
| home_rest_days | -0.027 | -0.055 | -0.055 |
| home_team_home_goals_avg | 0.113 | -0.039 | 0.053 |
| home_team_wins_last_5 | 0.132 | -0.064 | 0.050 |
| away_rest_days | -0.028 | -0.047 | -0.050 |
| away_team_goals_scored_last_5 | -0.076 | 0.009 | -0.047 |
| home_team_home_conceded_avg | -0.098 | 0.039 | -0.042 |
| home_team_points_last_5 | 0.116 | -0.063 | 0.040 |
| home_team_goals_scored_last_5 | 0.126 | -0.079 | 0.036 |
| away_team_away_goals_avg | 0.029 | 0.014 | 0.029 |
| away_points_before_match | -0.004 | 0.046 | 0.027 |
| rest_days_difference | 0.000 | -0.031 | -0.020 |
| away_team_away_win_rate | 0.081 | -0.066 | 0.014 |
| home_team_goals_conceded_last_5 | -0.018 | 0.035 | 0.010 |
| away_position_before_match | 0.052 | -0.065 | -0.006 |
| away_team_away_conceded_avg | -0.042 | 0.047 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 44 | 8 | 20 | 16 | 18.2% | 45.5% | 36.4% |
| -4..-2 | 62 | 24 | 16 | 22 | 38.7% | 25.8% | 35.5% |
| -1..1 | 98 | 32 | 30 | 36 | 32.7% | 30.6% | 36.7% |
| 2..4 | 65 | 30 | 20 | 15 | 46.2% | 30.8% | 23.1% |
| >4 | 41 | 23 | 9 | 9 | 56.1% | 22.0% | 22.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 67 | 34 | 17 | 16 | 50.7% | 25.4% | 23.9% |
| -5..-2 | 63 | 29 | 14 | 20 | 46.0% | 22.2% | 31.7% |
| -1..1 | 39 | 13 | 17 | 9 | 33.3% | 43.6% | 23.1% |
| 2..5 | 69 | 28 | 19 | 22 | 40.6% | 27.5% | 31.9% |
| >=6 | 72 | 13 | 28 | 31 | 18.1% | 38.9% | 43.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 28 | 13 | 4 | 11 | 46.4% | 14.3% | 39.3% |
| -1..0 | 54 | 20 | 22 | 12 | 37.0% | 40.7% | 22.2% |
| 0 | 135 | 52 | 33 | 50 | 38.5% | 24.4% | 37.0% |
| 1..2 | 70 | 24 | 22 | 24 | 34.3% | 31.4% | 34.3% |
| >2 | 12 | 5 | 6 | 1 | 41.7% | 50.0% | 8.3% |
| unknown | 11 | 3 | 8 | 0 | 27.3% | 72.7% | 0.0% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.9%** home win (78/230)
- `>= 0.5` tier: **48.8%** home win (39/80)
- Home-win gap (>= split minus < split): **+14.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 230 | 78 | 75 | 77 | 33.9% |
| high | >= 0.5 | 80 | 39 | 20 | 21 | 48.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.556 | -0.947 | -2.796 | 5.351 |
| home_points_before_match | 24.769 | 21.526 | 20.112 | 4.657 |
| position_difference | -1.667 | 1.021 | 1.959 | 3.626 |
| home_position_before_match | 8.658 | 10.000 | 10.949 | 2.291 |
| away_position_before_match | 10.325 | 8.979 | 8.990 | 1.346 |
| home_team_goals_scored_last_5 | 6.265 | 4.958 | 5.480 | 1.307 |
| home_team_points_last_5 | 6.795 | 5.632 | 5.776 | 1.163 |
| home_team_goals_conceded_last_5 | 5.496 | 5.189 | 6.224 | 1.035 |
| away_team_points_last_5 | 5.692 | 6.337 | 6.490 | 0.797 |
| away_team_goals_scored_last_5 | 5.376 | 5.611 | 6.163 | 0.787 |
| away_points_before_match | 22.214 | 22.474 | 22.908 | 0.694 |
| away_team_goals_conceded_last_5 | 5.726 | 5.295 | 5.908 | 0.613 |
| home_rest_days | 8.113 | 8.506 | 7.959 | 0.547 |
| home_team_wins_last_5 | 1.786 | 1.400 | 1.449 | 0.386 |
| away_rest_days | 8.263 | 8.382 | 8.082 | 0.300 |
| home_team_home_goals_avg | 1.332 | 1.083 | 1.198 | 0.249 |
| rest_days_difference | -0.132 | 0.115 | -0.122 | 0.247 |
| away_team_wins_last_5 | 1.419 | 1.663 | 1.633 | 0.244 |
| home_team_home_conceded_avg | 1.108 | 1.063 | 1.233 | 0.171 |
| away_team_away_goals_avg | 1.135 | 1.065 | 1.200 | 0.135 |
| away_team_away_conceded_avg | 1.195 | 1.178 | 1.292 | 0.114 |
| home_team_home_win_rate | 0.389 | 0.304 | 0.304 | 0.086 |
| away_team_away_win_rate | 0.317 | 0.267 | 0.292 | 0.051 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\france2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\france2\charts\relationships_home_win_pct_by_position.png)

