# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:02:33+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: J1 League (Japan)
- Scope: league `japan1`

- Matches analysed: **241** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | -0.029 | -0.101 | -0.096 |
| home_team_goals_conceded_last_5 | -0.050 | -0.079 | -0.096 |
| away_team_goals_scored_last_5 | -0.062 | -0.050 | -0.083 |
| away_team_away_win_rate | -0.099 | -0.008 | -0.080 |
| away_team_goals_conceded_last_5 | 0.026 | -0.129 | -0.076 |
| home_team_home_goals_avg | -0.054 | -0.043 | -0.072 |
| home_position_before_match | -0.093 | 0.006 | -0.065 |
| away_position_before_match | 0.082 | -0.168 | -0.062 |
| away_team_wins_last_5 | -0.043 | -0.039 | -0.061 |
| home_points_before_match | 0.035 | -0.102 | -0.050 |
| away_team_away_goals_avg | -0.094 | 0.029 | -0.049 |
| home_rest_days | 0.044 | 0.005 | 0.038 |
| home_team_home_win_rate | -0.024 | -0.026 | -0.037 |
| rest_days_difference | 0.044 | 0.004 | 0.037 |
| away_points_before_match | -0.032 | -0.018 | -0.037 |
| away_team_points_last_5 | -0.033 | -0.015 | -0.036 |
| home_team_points_last_5 | 0.015 | -0.048 | -0.024 |
| points_difference | 0.088 | -0.115 | -0.019 |
| home_team_goals_scored_last_5 | 0.028 | -0.049 | -0.015 |
| away_team_away_conceded_avg | 0.076 | -0.058 | 0.014 |
| home_team_wins_last_5 | 0.035 | -0.045 | -0.007 |
| away_rest_days | 0.002 | 0.002 | 0.003 |
| position_difference | -0.127 | 0.127 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 39 | 21 | 2 | 16 | 53.8% | 5.1% | 41.0% |
| -4..-2 | 50 | 22 | 5 | 23 | 44.0% | 10.0% | 46.0% |
| -1..1 | 83 | 47 | 3 | 33 | 56.6% | 3.6% | 39.8% |
| 2..4 | 49 | 30 | 6 | 13 | 61.2% | 12.2% | 26.5% |
| >4 | 20 | 11 | 1 | 8 | 55.0% | 5.0% | 40.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 56 | 34 | 5 | 17 | 60.7% | 8.9% | 30.4% |
| -5..-2 | 42 | 25 | 2 | 15 | 59.5% | 4.8% | 35.7% |
| -1..1 | 41 | 23 | 3 | 15 | 56.1% | 7.3% | 36.6% |
| 2..5 | 38 | 21 | 1 | 16 | 55.3% | 2.6% | 42.1% |
| >=6 | 64 | 28 | 6 | 30 | 43.8% | 9.4% | 46.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 12 | 4 | 0 | 8 | 33.3% | 0.0% | 66.7% |
| -1..0 | 34 | 16 | 3 | 15 | 47.1% | 8.8% | 44.1% |
| 0 | 137 | 76 | 12 | 49 | 55.5% | 8.8% | 35.8% |
| 1..2 | 28 | 20 | 1 | 7 | 71.4% | 3.6% | 25.0% |
| >2 | 10 | 5 | 0 | 5 | 50.0% | 0.0% | 50.0% |
| unknown | 20 | 10 | 1 | 9 | 50.0% | 5.0% | 45.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **51.5%** home win (51/99)
- `>= 0.5` tier: **56.3%** home win (80/142)
- Home-win gap (>= split minus < split): **+4.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 99 | 51 | 7 | 41 | 51.5% |
| high | >= 0.5 | 142 | 80 | 10 | 52 | 56.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 9.374 | 4.882 | 9.925 | 5.042 |
| home_points_before_match | 9.924 | 4.882 | 8.613 | 5.041 |
| position_difference | -0.695 | -0.471 | 2.054 | 2.748 |
| away_position_before_match | 10.985 | 11.235 | 9.118 | 2.117 |
| points_difference | 0.550 | 0.000 | -1.312 | 1.861 |
| away_team_points_last_5 | 5.763 | 4.353 | 6.118 | 1.765 |
| home_team_goals_conceded_last_5 | 5.725 | 4.647 | 5.710 | 1.078 |
| home_team_points_last_5 | 5.405 | 4.353 | 5.151 | 1.052 |
| home_position_before_match | 10.290 | 10.765 | 11.172 | 0.882 |
| home_team_goals_scored_last_5 | 5.489 | 4.647 | 5.398 | 0.841 |
| away_team_goals_scored_last_5 | 5.550 | 5.118 | 5.882 | 0.764 |
| away_team_goals_conceded_last_5 | 5.603 | 5.294 | 5.215 | 0.388 |
| home_rest_days | 6.231 | 5.875 | 5.988 | 0.356 |
| rest_days_difference | 0.165 | -0.125 | -0.071 | 0.290 |
| home_team_home_conceded_avg | 1.275 | 0.990 | 1.166 | 0.285 |
| away_team_away_goals_avg | 1.104 | 1.319 | 1.225 | 0.214 |
| home_team_wins_last_5 | 1.939 | 1.765 | 1.860 | 0.174 |
| away_team_away_conceded_avg | 1.361 | 1.211 | 1.222 | 0.150 |
| away_team_wins_last_5 | 2.038 | 2.000 | 2.140 | 0.140 |
| away_team_away_win_rate | 0.372 | 0.451 | 0.391 | 0.079 |
| home_team_home_goals_avg | 1.274 | 1.343 | 1.269 | 0.074 |
| home_team_home_win_rate | 0.486 | 0.549 | 0.477 | 0.072 |
| away_rest_days | 6.066 | 6.000 | 6.060 | 0.066 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\japan1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\japan1\charts\relationships_home_win_pct_by_position.png)

