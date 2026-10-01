# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:59:15+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: J1 League (Japan)
- Scope: league `japan1`

- Matches analysed: **161** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_conceded_last_5 | -0.018 | -0.082 | -0.079 |
| home_rest_days | 0.087 | -0.006 | 0.063 |
| home_team_home_win_rate | -0.073 | -0.001 | -0.058 |
| home_points_before_match | 0.044 | -0.116 | -0.057 |
| rest_days_difference | 0.051 | 0.013 | 0.051 |
| away_team_goals_conceded_last_5 | 0.065 | -0.126 | -0.050 |
| home_team_home_goals_avg | -0.092 | 0.028 | -0.049 |
| home_team_goals_scored_last_5 | -0.030 | -0.032 | -0.048 |
| home_team_home_conceded_avg | -0.032 | -0.022 | -0.042 |
| points_difference | 0.070 | -0.115 | -0.037 |
| away_team_away_conceded_avg | 0.083 | -0.043 | 0.030 |
| away_points_before_match | -0.012 | -0.025 | -0.029 |
| away_position_before_match | 0.082 | -0.116 | -0.028 |
| position_difference | -0.084 | 0.116 | 0.026 |
| home_team_points_last_5 | -0.012 | -0.021 | -0.026 |
| home_team_wins_last_5 | -0.012 | -0.021 | -0.026 |
| away_team_away_win_rate | -0.011 | -0.015 | -0.021 |
| away_team_goals_scored_last_5 | 0.046 | -0.071 | -0.020 |
| away_team_away_goals_avg | 0.038 | -0.055 | -0.014 |
| away_rest_days | 0.037 | -0.020 | 0.013 |
| away_team_points_last_5 | 0.019 | -0.007 | 0.009 |
| away_team_wins_last_5 | 0.019 | -0.007 | 0.009 |
| home_position_before_match | -0.036 | 0.046 | 0.009 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 25 | 16 | 0 | 9 | 64.0% | 0.0% | 36.0% |
| -4..-2 | 33 | 15 | 0 | 18 | 45.5% | 0.0% | 54.5% |
| -1..1 | 58 | 34 | 0 | 24 | 58.6% | 0.0% | 41.4% |
| 2..4 | 33 | 22 | 0 | 11 | 66.7% | 0.0% | 33.3% |
| >4 | 12 | 7 | 0 | 5 | 58.3% | 0.0% | 41.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 40 | 26 | 0 | 14 | 65.0% | 0.0% | 35.0% |
| -5..-2 | 29 | 17 | 0 | 12 | 58.6% | 0.0% | 41.4% |
| -1..1 | 25 | 16 | 0 | 9 | 64.0% | 0.0% | 36.0% |
| 2..5 | 29 | 16 | 0 | 13 | 55.2% | 0.0% | 44.8% |
| >=6 | 38 | 19 | 0 | 19 | 50.0% | 0.0% | 50.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 11 | 4 | 0 | 7 | 36.4% | 0.0% | 63.6% |
| -1..0 | 23 | 13 | 0 | 10 | 56.5% | 0.0% | 43.5% |
| 0 | 86 | 51 | 0 | 35 | 59.3% | 0.0% | 40.7% |
| 1..2 | 21 | 16 | 0 | 5 | 76.2% | 0.0% | 23.8% |
| >2 | 10 | 5 | 0 | 5 | 50.0% | 0.0% | 50.0% |
| unknown | 10 | 5 | 0 | 5 | 50.0% | 0.0% | 50.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **53.1%** home win (34/64)
- `>= 0.5` tier: **61.9%** home win (60/97)
- Home-win gap (>= split minus < split): **+8.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 64 | 34 | 0 | 30 | 53.1% |
| high | >= 0.5 | 97 | 60 | 0 | 37 | 61.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| position_difference | -0.862 | - | 1.343 | 2.205 |
| home_points_before_match | 12.000 | - | 10.209 | 1.791 |
| points_difference | 0.670 | - | -1.119 | 1.790 |
| away_position_before_match | 11.191 | - | 9.791 | 1.400 |
| home_position_before_match | 10.330 | - | 11.134 | 0.805 |
| away_team_goals_conceded_last_5 | 6.021 | - | 5.418 | 0.603 |
| home_rest_days | 6.326 | - | 5.952 | 0.374 |
| home_team_goals_conceded_last_5 | 6.234 | - | 5.881 | 0.353 |
| away_team_goals_scored_last_5 | 6.074 | - | 5.821 | 0.254 |
| rest_days_difference | 0.213 | - | -0.016 | 0.230 |
| home_team_points_last_5 | 5.904 | - | 5.687 | 0.218 |
| away_rest_days | 6.112 | - | 5.968 | 0.145 |
| away_team_away_conceded_avg | 1.395 | - | 1.251 | 0.144 |
| home_team_wins_last_5 | 1.968 | - | 1.896 | 0.073 |
| away_team_away_goals_avg | 1.214 | - | 1.147 | 0.067 |
| home_team_home_conceded_avg | 1.260 | - | 1.202 | 0.058 |
| home_team_home_goals_avg | 1.313 | - | 1.358 | 0.045 |
| away_team_points_last_5 | 6.383 | - | 6.358 | 0.025 |
| home_team_goals_scored_last_5 | 5.830 | - | 5.851 | 0.021 |
| away_team_away_win_rate | 0.386 | - | 0.370 | 0.016 |
| away_team_wins_last_5 | 2.128 | - | 2.119 | 0.008 |
| home_team_home_win_rate | 0.484 | - | 0.481 | 0.003 |
| away_points_before_match | 11.330 | - | 11.328 | 0.001 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\japan1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\japan1\charts\relationships_home_win_pct_by_position.png)

