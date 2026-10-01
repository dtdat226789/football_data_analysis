# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:24:40+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Allsvenskan Women (Sweden)
- Scope: league `wsweden`

- Matches analysed: **182** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_goals_avg | 0.306 | -0.131 | 0.149 |
| away_team_away_conceded_avg | 0.250 | -0.174 | 0.065 |
| away_position_before_match | 0.326 | -0.261 | 0.054 |
| rest_days_difference | -0.083 | 0.021 | -0.053 |
| home_team_home_win_rate | 0.171 | -0.115 | 0.048 |
| away_rest_days | 0.135 | -0.090 | 0.037 |
| home_team_goals_scored_last_5 | 0.185 | -0.147 | 0.032 |
| home_team_points_last_5 | 0.146 | -0.182 | -0.030 |
| home_position_before_match | -0.292 | 0.325 | 0.029 |
| home_team_home_conceded_avg | -0.091 | 0.123 | 0.028 |
| away_team_goals_conceded_last_5 | 0.180 | -0.148 | 0.027 |
| home_rest_days | 0.115 | -0.084 | 0.026 |
| home_points_before_match | 0.122 | -0.091 | 0.026 |
| position_difference | -0.451 | 0.428 | -0.019 |
| home_team_goals_conceded_last_5 | -0.200 | 0.221 | 0.019 |
| away_points_before_match | -0.272 | 0.291 | 0.017 |
| home_team_wins_last_5 | 0.158 | -0.174 | -0.014 |
| away_team_away_goals_avg | -0.267 | 0.281 | 0.012 |
| points_difference | 0.436 | -0.423 | 0.010 |
| away_team_goals_scored_last_5 | -0.312 | 0.320 | 0.007 |
| away_team_points_last_5 | -0.283 | 0.275 | -0.007 |
| away_team_away_win_rate | -0.254 | 0.246 | -0.006 |
| away_team_wins_last_5 | -0.285 | 0.279 | -0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 32 | 7 | 6 | 19 | 21.9% | 18.8% | 59.4% |
| -4..-2 | 43 | 12 | 5 | 26 | 27.9% | 11.6% | 60.5% |
| -1..1 | 48 | 25 | 8 | 15 | 52.1% | 16.7% | 31.2% |
| 2..4 | 25 | 16 | 3 | 6 | 64.0% | 12.0% | 24.0% |
| >4 | 34 | 25 | 3 | 6 | 73.5% | 8.8% | 17.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 27 | 24 | 2 | 1 | 88.9% | 7.4% | 3.7% |
| -5..-2 | 40 | 22 | 7 | 11 | 55.0% | 17.5% | 27.5% |
| -1..1 | 36 | 19 | 3 | 14 | 52.8% | 8.3% | 38.9% |
| 2..5 | 44 | 15 | 6 | 23 | 34.1% | 13.6% | 52.3% |
| >=6 | 35 | 5 | 7 | 23 | 14.3% | 20.0% | 65.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 15 | 11 | 1 | 3 | 73.3% | 6.7% | 20.0% |
| -1..0 | 39 | 15 | 5 | 19 | 38.5% | 12.8% | 48.7% |
| 0 | 64 | 34 | 8 | 22 | 53.1% | 12.5% | 34.4% |
| 1..2 | 48 | 16 | 9 | 23 | 33.3% | 18.8% | 47.9% |
| >2 | 9 | 4 | 1 | 4 | 44.4% | 11.1% | 44.4% |
| unknown | 7 | 5 | 1 | 1 | 71.4% | 14.3% | 14.3% |
- *7 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.8%** home win (31/82)
- `>= 0.5` tier: **54.0%** home win (54/100)
- Home-win gap (>= split minus < split): **+16.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 82 | 31 | 13 | 38 | 37.8% |
| high | >= 0.5 | 100 | 54 | 12 | 34 | 54.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.682 | -3.080 | -6.250 | 11.932 |
| away_points_before_match | 13.682 | 15.720 | 23.653 | 9.970 |
| home_points_before_match | 19.365 | 12.640 | 17.403 | 6.725 |
| position_difference | -2.329 | 1.560 | 3.153 | 5.482 |
| home_position_before_match | 6.271 | 8.360 | 9.431 | 3.160 |
| away_rest_days | 10.463 | 7.417 | 9.141 | 3.046 |
| home_team_goals_conceded_last_5 | 5.871 | 7.880 | 8.792 | 2.921 |
| home_rest_days | 10.350 | 7.625 | 9.338 | 2.725 |
| away_team_goals_scored_last_5 | 6.200 | 6.920 | 8.889 | 2.689 |
| away_team_points_last_5 | 5.388 | 6.320 | 7.736 | 2.348 |
| away_position_before_match | 8.600 | 6.800 | 6.278 | 2.322 |
| home_team_points_last_5 | 7.165 | 5.520 | 5.264 | 1.901 |
| home_team_goals_scored_last_5 | 8.059 | 6.640 | 6.500 | 1.559 |
| away_team_goals_conceded_last_5 | 7.800 | 7.560 | 6.639 | 1.161 |
| away_team_wins_last_5 | 1.588 | 1.920 | 2.347 | 0.759 |
| home_team_wins_last_5 | 2.165 | 1.680 | 1.542 | 0.623 |
| away_team_away_goals_avg | 1.049 | 1.438 | 1.662 | 0.613 |
| home_team_home_conceded_avg | 1.130 | 1.625 | 1.467 | 0.495 |
| home_team_home_goals_avg | 1.827 | 1.366 | 1.367 | 0.461 |
| away_team_away_conceded_avg | 1.812 | 1.568 | 1.381 | 0.431 |
| rest_days_difference | -0.113 | 0.208 | 0.197 | 0.321 |
| away_team_away_win_rate | 0.218 | 0.321 | 0.395 | 0.177 |
| home_team_home_win_rate | 0.528 | 0.421 | 0.435 | 0.107 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\wsweden\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\wsweden\charts\relationships_home_win_pct_by_position.png)

