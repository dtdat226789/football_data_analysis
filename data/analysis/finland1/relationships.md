# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:58:20+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Veikkausliiga (Finland)
- Scope: league `finland1`

- Matches analysed: **273** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_conceded_last_5 | 0.204 | -0.065 | 0.109 |
| rest_days_difference | 0.054 | 0.092 | 0.105 |
| points_difference | 0.306 | -0.201 | 0.092 |
| away_position_before_match | 0.239 | -0.151 | 0.075 |
| home_rest_days | -0.045 | 0.140 | 0.063 |
| away_team_goals_scored_last_5 | -0.079 | 0.172 | 0.060 |
| away_team_away_conceded_avg | 0.186 | -0.123 | 0.055 |
| home_team_goals_scored_last_5 | 0.123 | -0.066 | 0.047 |
| home_position_before_match | -0.099 | 0.170 | 0.043 |
| away_points_before_match | -0.158 | 0.116 | -0.039 |
| home_team_wins_last_5 | 0.147 | -0.108 | 0.035 |
| home_team_points_last_5 | 0.139 | -0.101 | 0.035 |
| home_points_before_match | 0.082 | -0.041 | 0.033 |
| home_team_home_win_rate | 0.083 | -0.137 | -0.032 |
| home_team_home_conceded_avg | -0.066 | 0.118 | 0.032 |
| position_difference | -0.248 | 0.232 | -0.026 |
| away_rest_days | -0.087 | 0.059 | -0.025 |
| away_team_wins_last_5 | -0.071 | 0.090 | 0.009 |
| away_team_away_goals_avg | -0.039 | 0.033 | -0.007 |
| home_team_home_goals_avg | 0.054 | -0.067 | -0.006 |
| home_team_goals_conceded_last_5 | -0.057 | 0.054 | -0.005 |
| away_team_points_last_5 | -0.115 | 0.129 | 0.003 |
| away_team_away_win_rate | -0.014 | 0.016 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 50 | 18 | 9 | 23 | 36.0% | 18.0% | 46.0% |
| -4..-2 | 55 | 19 | 12 | 24 | 34.5% | 21.8% | 43.6% |
| -1..1 | 74 | 31 | 18 | 25 | 41.9% | 24.3% | 33.8% |
| 2..4 | 55 | 28 | 18 | 9 | 50.9% | 32.7% | 16.4% |
| >4 | 39 | 23 | 10 | 6 | 59.0% | 25.6% | 15.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 34 | 22 | 8 | 4 | 64.7% | 23.5% | 11.8% |
| -5..-2 | 81 | 42 | 20 | 19 | 51.9% | 24.7% | 23.5% |
| -1..1 | 44 | 23 | 10 | 11 | 52.3% | 22.7% | 25.0% |
| 2..5 | 76 | 25 | 19 | 32 | 32.9% | 25.0% | 42.1% |
| >=6 | 38 | 7 | 10 | 21 | 18.4% | 26.3% | 55.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 31 | 14 | 9 | 8 | 45.2% | 29.0% | 25.8% |
| -1..0 | 46 | 20 | 11 | 15 | 43.5% | 23.9% | 32.6% |
| 0 | 112 | 58 | 24 | 30 | 51.8% | 21.4% | 26.8% |
| 1..2 | 58 | 17 | 15 | 26 | 29.3% | 25.9% | 44.8% |
| >2 | 14 | 6 | 5 | 3 | 42.9% | 35.7% | 21.4% |
| unknown | 12 | 4 | 3 | 5 | 33.3% | 25.0% | 41.7% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.2%** home win (26/68)
- `>= 0.5` tier: **45.4%** home win (93/205)
- Home-win gap (>= split minus < split): **+7.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 68 | 26 | 16 | 26 | 38.2% |
| high | >= 0.5 | 205 | 93 | 51 | 61 | 45.4% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.613 | -0.701 | -4.379 | 6.993 |
| away_points_before_match | 12.748 | 15.537 | 18.805 | 6.057 |
| position_difference | -1.370 | 0.269 | 2.034 | 3.404 |
| away_position_before_match | 7.395 | 5.985 | 5.414 | 1.981 |
| home_team_points_last_5 | 6.176 | 6.373 | 4.931 | 1.442 |
| home_position_before_match | 6.025 | 6.254 | 7.448 | 1.423 |
| away_team_points_last_5 | 5.639 | 5.925 | 7.034 | 1.396 |
| away_team_goals_scored_last_5 | 5.958 | 6.254 | 7.230 | 1.272 |
| away_team_goals_conceded_last_5 | 6.689 | 6.164 | 5.552 | 1.137 |
| home_team_goals_scored_last_5 | 6.479 | 6.388 | 5.379 | 1.100 |
| home_points_before_match | 15.361 | 14.836 | 14.425 | 0.936 |
| home_team_goals_conceded_last_5 | 5.933 | 6.448 | 6.701 | 0.768 |
| home_team_wins_last_5 | 2.866 | 2.821 | 2.310 | 0.555 |
| away_team_wins_last_5 | 2.647 | 2.642 | 3.080 | 0.439 |
| away_rest_days | 6.957 | 7.016 | 7.366 | 0.409 |
| away_team_away_conceded_avg | 1.533 | 1.228 | 1.158 | 0.375 |
| home_rest_days | 6.852 | 6.922 | 7.195 | 0.343 |
| home_team_home_conceded_avg | 1.097 | 1.187 | 1.327 | 0.230 |
| home_team_home_goals_avg | 1.358 | 1.385 | 1.289 | 0.096 |
| away_team_away_goals_avg | 1.216 | 1.178 | 1.270 | 0.092 |
| home_team_home_win_rate | 0.664 | 0.653 | 0.573 | 0.091 |
| rest_days_difference | -0.104 | -0.094 | -0.171 | 0.077 |
| away_team_away_win_rate | 0.508 | 0.531 | 0.530 | 0.023 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\finland1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\finland1\charts\relationships_home_win_pct_by_position.png)

