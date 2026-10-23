# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:55:16+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: ISL (India)
- Scope: league `india1`

- Matches analysed: **247** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| points_difference | 0.159 | -0.292 | -0.089 |
| home_team_home_conceded_avg | -0.019 | 0.115 | 0.068 |
| away_team_away_goals_avg | -0.050 | 0.139 | 0.062 |
| home_rest_days | 0.003 | 0.083 | 0.061 |
| home_team_goals_conceded_last_5 | -0.039 | 0.121 | 0.058 |
| away_team_away_conceded_avg | 0.055 | 0.015 | 0.053 |
| home_team_wins_last_5 | 0.040 | -0.109 | -0.048 |
| home_points_before_match | 0.027 | -0.084 | -0.040 |
| away_rest_days | -0.043 | 0.088 | 0.030 |
| away_points_before_match | -0.093 | 0.139 | 0.029 |
| home_position_before_match | -0.160 | 0.209 | 0.029 |
| home_team_home_goals_avg | 0.175 | -0.149 | 0.025 |
| position_difference | -0.202 | 0.245 | 0.022 |
| rest_days_difference | 0.042 | -0.015 | 0.022 |
| home_team_goals_scored_last_5 | 0.077 | -0.111 | -0.021 |
| away_team_wins_last_5 | -0.086 | 0.062 | -0.021 |
| home_team_points_last_5 | 0.054 | -0.072 | -0.011 |
| away_team_away_win_rate | -0.028 | 0.044 | 0.010 |
| away_team_goals_conceded_last_5 | 0.068 | -0.064 | 0.006 |
| home_team_home_win_rate | 0.145 | -0.145 | 0.005 |
| away_team_points_last_5 | -0.097 | 0.109 | 0.005 |
| away_team_goals_scored_last_5 | -0.073 | 0.081 | 0.003 |
| away_position_before_match | 0.119 | -0.130 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 34 | 10 | 14 | 10 | 29.4% | 41.2% | 29.4% |
| -4..-2 | 54 | 15 | 15 | 24 | 27.8% | 27.8% | 44.4% |
| -1..1 | 74 | 27 | 21 | 26 | 36.5% | 28.4% | 35.1% |
| 2..4 | 47 | 24 | 9 | 14 | 51.1% | 19.1% | 29.8% |
| >4 | 38 | 25 | 8 | 5 | 65.8% | 21.1% | 13.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 38 | 27 | 9 | 2 | 71.1% | 23.7% | 5.3% |
| -5..-2 | 60 | 28 | 12 | 20 | 46.7% | 20.0% | 33.3% |
| -1..1 | 47 | 19 | 14 | 14 | 40.4% | 29.8% | 29.8% |
| 2..5 | 66 | 17 | 23 | 26 | 25.8% | 34.8% | 39.4% |
| >=6 | 36 | 10 | 9 | 17 | 27.8% | 25.0% | 47.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 64 | 23 | 18 | 23 | 35.9% | 28.1% | 35.9% |
| -1..0 | 47 | 20 | 11 | 16 | 42.6% | 23.4% | 34.0% |
| 0 | 16 | 6 | 3 | 7 | 37.5% | 18.8% | 43.8% |
| 1..2 | 58 | 23 | 20 | 15 | 39.7% | 34.5% | 25.9% |
| >2 | 47 | 21 | 12 | 14 | 44.7% | 25.5% | 29.8% |
| unknown | 15 | 8 | 3 | 4 | 53.3% | 20.0% | 26.7% |
- *15 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.1%** home win (59/159)
- `>= 0.5` tier: **47.7%** home win (42/88)
- Home-win gap (>= split minus < split): **+10.6 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 159 | 59 | 44 | 56 | 37.1% |
| high | >= 0.5 | 88 | 42 | 23 | 23 | 47.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.604 | -1.537 | -2.684 | 5.288 |
| position_difference | -1.743 | 0.687 | 1.835 | 3.578 |
| away_points_before_match | 11.604 | 13.597 | 14.570 | 2.966 |
| home_points_before_match | 14.208 | 12.060 | 11.886 | 2.322 |
| home_position_before_match | 6.347 | 7.627 | 8.430 | 2.084 |
| away_rest_days | 7.462 | 6.846 | 8.467 | 1.621 |
| away_position_before_match | 8.089 | 6.940 | 6.595 | 1.494 |
| away_team_points_last_5 | 4.980 | 6.254 | 5.987 | 1.274 |
| away_team_goals_conceded_last_5 | 6.337 | 5.776 | 5.101 | 1.235 |
| home_rest_days | 7.726 | 7.000 | 8.133 | 1.133 |
| home_team_points_last_5 | 6.337 | 5.373 | 5.215 | 1.121 |
| home_team_goals_scored_last_5 | 6.257 | 5.776 | 5.177 | 1.080 |
| home_team_goals_conceded_last_5 | 5.287 | 5.776 | 6.190 | 0.903 |
| away_team_goals_scored_last_5 | 5.257 | 6.030 | 5.823 | 0.772 |
| rest_days_difference | 0.312 | 0.203 | -0.333 | 0.645 |
| away_team_wins_last_5 | 1.327 | 1.746 | 1.532 | 0.420 |
| home_team_home_goals_avg | 1.513 | 1.160 | 1.111 | 0.402 |
| home_team_wins_last_5 | 1.743 | 1.448 | 1.342 | 0.401 |
| away_team_away_conceded_avg | 1.438 | 1.310 | 1.238 | 0.200 |
| home_team_home_conceded_avg | 1.128 | 1.047 | 1.213 | 0.167 |
| home_team_home_win_rate | 0.444 | 0.317 | 0.292 | 0.152 |
| away_team_away_goals_avg | 1.035 | 1.164 | 1.152 | 0.130 |
| away_team_away_win_rate | 0.282 | 0.325 | 0.290 | 0.043 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\india1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\india1\charts\relationships_home_win_pct_by_position.png)

