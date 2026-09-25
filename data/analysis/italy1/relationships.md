# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:01:46+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie A (Italy)
- Scope: league `italy1`

- Matches analysed: **430** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| position_difference | -0.347 | 0.232 | -0.114 |
| home_position_before_match | -0.231 | 0.128 | -0.094 |
| home_team_goals_conceded_last_5 | -0.127 | 0.015 | -0.089 |
| home_team_home_goals_avg | 0.198 | -0.102 | 0.085 |
| home_team_points_last_5 | 0.162 | -0.082 | 0.071 |
| away_team_points_last_5 | -0.186 | 0.116 | -0.067 |
| points_difference | 0.301 | -0.250 | 0.065 |
| away_position_before_match | 0.245 | -0.191 | 0.062 |
| home_team_home_win_rate | 0.121 | -0.054 | 0.058 |
| home_team_wins_last_5 | 0.112 | -0.051 | 0.053 |
| rest_days_difference | 0.047 | 0.024 | 0.053 |
| home_points_before_match | 0.116 | -0.063 | 0.048 |
| away_team_away_win_rate | 0.005 | 0.060 | 0.045 |
| away_team_away_goals_avg | -0.054 | 0.110 | 0.033 |
| home_team_goals_scored_last_5 | 0.162 | -0.139 | 0.033 |
| away_team_away_conceded_avg | 0.076 | -0.049 | 0.026 |
| away_team_goals_scored_last_5 | -0.141 | 0.123 | -0.026 |
| away_rest_days | -0.029 | 0.003 | -0.021 |
| away_team_wins_last_5 | -0.108 | 0.108 | -0.011 |
| home_team_home_conceded_avg | -0.068 | 0.066 | -0.008 |
| away_team_goals_conceded_last_5 | 0.096 | -0.119 | -0.006 |
| home_rest_days | -0.006 | 0.014 | 0.005 |
| away_points_before_match | -0.115 | 0.129 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 60 | 11 | 17 | 32 | 18.3% | 28.3% | 53.3% |
| -4..-2 | 93 | 29 | 22 | 42 | 31.2% | 23.7% | 45.2% |
| -1..1 | 138 | 56 | 35 | 47 | 40.6% | 25.4% | 34.1% |
| 2..4 | 71 | 35 | 18 | 18 | 49.3% | 25.4% | 25.4% |
| >4 | 68 | 39 | 16 | 13 | 57.4% | 23.5% | 19.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 101 | 61 | 20 | 20 | 60.4% | 19.8% | 19.8% |
| -5..-2 | 76 | 38 | 26 | 12 | 50.0% | 34.2% | 15.8% |
| -1..1 | 67 | 24 | 19 | 24 | 35.8% | 28.4% | 35.8% |
| 2..5 | 72 | 21 | 20 | 31 | 29.2% | 27.8% | 43.1% |
| >=6 | 114 | 26 | 23 | 65 | 22.8% | 20.2% | 57.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 42 | 10 | 19 | 13 | 23.8% | 45.2% | 31.0% |
| -1..0 | 95 | 37 | 22 | 36 | 38.9% | 23.2% | 37.9% |
| 0 | 132 | 54 | 27 | 51 | 40.9% | 20.5% | 38.6% |
| 1..2 | 131 | 61 | 33 | 37 | 46.6% | 25.2% | 28.2% |
| >2 | 10 | 1 | 2 | 7 | 10.0% | 20.0% | 70.0% |
| unknown | 20 | 7 | 5 | 8 | 35.0% | 25.0% | 40.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **28.2%** home win (29/103)
- `>= 0.5` tier: **43.1%** home win (141/327)
- Home-win gap (>= split minus < split): **+14.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 103 | 29 | 31 | 43 | 28.2% |
| high | >= 0.5 | 327 | 141 | 77 | 109 | 43.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.753 | 0.352 | -6.191 | 10.944 |
| position_difference | -2.771 | 0.157 | 3.836 | 6.606 |
| away_points_before_match | 19.959 | 21.806 | 26.349 | 6.390 |
| home_points_before_match | 24.712 | 22.157 | 20.158 | 4.554 |
| away_position_before_match | 12.082 | 10.620 | 8.678 | 3.405 |
| home_position_before_match | 9.312 | 10.778 | 12.513 | 3.201 |
| home_team_goals_scored_last_5 | 5.829 | 5.296 | 4.480 | 1.349 |
| home_team_points_last_5 | 6.424 | 6.102 | 5.086 | 1.338 |
| away_team_points_last_5 | 5.182 | 6.315 | 6.520 | 1.337 |
| away_team_goals_scored_last_5 | 4.735 | 5.546 | 5.671 | 0.936 |
| away_team_goals_conceded_last_5 | 5.559 | 5.213 | 4.737 | 0.822 |
| home_team_goals_conceded_last_5 | 5.000 | 5.176 | 5.743 | 0.743 |
| away_team_wins_last_5 | 2.500 | 2.870 | 2.849 | 0.370 |
| home_team_home_goals_avg | 1.281 | 1.206 | 0.930 | 0.351 |
| home_team_wins_last_5 | 2.812 | 2.769 | 2.480 | 0.332 |
| rest_days_difference | 0.135 | -0.097 | -0.014 | 0.232 |
| home_rest_days | 7.417 | 7.204 | 7.347 | 0.213 |
| away_team_away_goals_avg | 0.926 | 1.072 | 1.065 | 0.146 |
| away_team_away_conceded_avg | 1.172 | 1.185 | 1.059 | 0.126 |
| home_team_home_win_rate | 0.636 | 0.617 | 0.546 | 0.090 |
| home_team_home_conceded_avg | 0.969 | 1.018 | 1.056 | 0.087 |
| away_rest_days | 7.282 | 7.301 | 7.361 | 0.079 |
| away_team_away_win_rate | 0.544 | 0.576 | 0.561 | 0.032 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\italy1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\italy1\charts\relationships_home_win_pct_by_position.png)

