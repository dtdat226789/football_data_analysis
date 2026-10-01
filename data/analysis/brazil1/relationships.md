# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:45:28+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie A Betano (Brazil)
- Scope: league `brazil1`

- Matches analysed: **380** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_points_before_match | 0.200 | -0.041 | 0.136 |
| position_difference | -0.259 | 0.174 | -0.095 |
| away_points_before_match | 0.013 | 0.122 | 0.092 |
| away_position_before_match | 0.146 | -0.066 | 0.075 |
| home_team_goals_scored_last_5 | 0.088 | -0.004 | 0.070 |
| away_team_away_conceded_avg | 0.125 | -0.049 | 0.070 |
| away_team_goals_conceded_last_5 | 0.132 | -0.072 | 0.060 |
| home_rest_days | -0.085 | 0.018 | -0.058 |
| home_position_before_match | -0.214 | 0.175 | -0.058 |
| away_team_away_goals_avg | -0.131 | 0.077 | -0.056 |
| points_difference | 0.251 | -0.224 | 0.055 |
| home_team_points_last_5 | 0.116 | -0.065 | 0.051 |
| away_team_points_last_5 | -0.128 | 0.086 | -0.047 |
| away_team_wins_last_5 | -0.125 | 0.084 | -0.046 |
| away_rest_days | -0.055 | 0.008 | -0.040 |
| rest_days_difference | -0.059 | 0.018 | -0.036 |
| home_team_wins_last_5 | 0.080 | -0.054 | 0.029 |
| home_team_home_win_rate | 0.045 | -0.099 | -0.029 |
| away_team_goals_scored_last_5 | -0.052 | 0.052 | -0.007 |
| home_team_home_conceded_avg | -0.084 | 0.110 | 0.005 |
| home_team_home_goals_avg | 0.070 | -0.093 | -0.005 |
| home_team_goals_conceded_last_5 | -0.119 | 0.142 | -0.002 |
| away_team_away_win_rate | -0.125 | 0.150 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 55 | 22 | 12 | 21 | 40.0% | 21.8% | 38.2% |
| -4..-2 | 84 | 42 | 24 | 18 | 50.0% | 28.6% | 21.4% |
| -1..1 | 124 | 57 | 37 | 30 | 46.0% | 29.8% | 24.2% |
| 2..4 | 63 | 35 | 12 | 16 | 55.6% | 19.0% | 25.4% |
| >4 | 54 | 35 | 14 | 5 | 64.8% | 25.9% | 9.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 89 | 60 | 19 | 10 | 67.4% | 21.3% | 11.2% |
| -5..-2 | 63 | 30 | 21 | 12 | 47.6% | 33.3% | 19.0% |
| -1..1 | 51 | 29 | 13 | 9 | 56.9% | 25.5% | 17.6% |
| 2..5 | 65 | 29 | 16 | 20 | 44.6% | 24.6% | 30.8% |
| >=6 | 112 | 43 | 30 | 39 | 38.4% | 26.8% | 34.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 54 | 28 | 13 | 13 | 51.9% | 24.1% | 24.1% |
| -1..0 | 64 | 38 | 15 | 11 | 59.4% | 23.4% | 17.2% |
| 0 | 120 | 58 | 32 | 30 | 48.3% | 26.7% | 25.0% |
| 1..2 | 105 | 45 | 30 | 30 | 42.9% | 28.6% | 28.6% |
| >2 | 27 | 17 | 4 | 6 | 63.0% | 14.8% | 22.2% |
| unknown | 10 | 5 | 5 | 0 | 50.0% | 50.0% | 0.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **48.2%** home win (95/197)
- `>= 0.5` tier: **52.5%** home win (96/183)
- Home-win gap (>= split minus < split): **+4.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 197 | 95 | 52 | 50 | 48.2% |
| high | >= 0.5 | 183 | 96 | 47 | 40 | 52.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.403 | -1.566 | -5.500 | 7.903 |
| home_points_before_match | 27.194 | 23.455 | 21.922 | 5.271 |
| position_difference | -1.178 | 1.051 | 3.711 | 4.889 |
| home_position_before_match | 9.901 | 11.535 | 13.011 | 3.111 |
| away_points_before_match | 24.791 | 25.020 | 27.422 | 2.632 |
| away_position_before_match | 11.079 | 10.485 | 9.300 | 1.779 |
| home_rest_days | 6.581 | 6.564 | 7.956 | 1.392 |
| home_team_goals_conceded_last_5 | 5.576 | 5.384 | 6.644 | 1.261 |
| away_team_points_last_5 | 6.026 | 6.556 | 7.200 | 1.174 |
| away_rest_days | 6.425 | 6.543 | 7.500 | 1.075 |
| away_team_goals_conceded_last_5 | 6.010 | 5.263 | 5.022 | 0.988 |
| away_team_goals_scored_last_5 | 5.649 | 5.677 | 6.244 | 0.595 |
| home_team_points_last_5 | 6.387 | 6.040 | 5.811 | 0.576 |
| rest_days_difference | 0.156 | 0.021 | 0.456 | 0.434 |
| home_team_goals_scored_last_5 | 5.702 | 5.545 | 5.300 | 0.402 |
| away_team_wins_last_5 | 1.592 | 1.808 | 1.944 | 0.353 |
| away_team_away_conceded_avg | 1.460 | 1.297 | 1.306 | 0.163 |
| away_team_away_goals_avg | 0.832 | 0.840 | 0.972 | 0.141 |
| home_team_wins_last_5 | 1.696 | 1.657 | 1.578 | 0.119 |
| home_team_home_goals_avg | 1.437 | 1.322 | 1.324 | 0.115 |
| away_team_away_win_rate | 0.176 | 0.197 | 0.272 | 0.096 |
| home_team_home_conceded_avg | 0.834 | 0.844 | 0.926 | 0.092 |
| home_team_home_win_rate | 0.485 | 0.457 | 0.452 | 0.033 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\brazil1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\brazil1\charts\relationships_home_win_pct_by_position.png)

