# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:06:23+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: League One (Scotland)
- Scope: league `scot1`

- Matches analysed: **191** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_win_rate | -0.193 | -0.138 | -0.257 |
| position_difference | -0.306 | 0.122 | -0.154 |
| away_position_before_match | 0.149 | 0.023 | 0.137 |
| points_difference | 0.251 | -0.106 | 0.122 |
| away_team_away_conceded_avg | 0.137 | 0.016 | 0.121 |
| away_team_away_goals_avg | -0.096 | -0.053 | -0.116 |
| home_points_before_match | 0.160 | -0.065 | 0.080 |
| away_team_goals_scored_last_5 | -0.029 | -0.074 | -0.079 |
| home_position_before_match | -0.270 | 0.191 | -0.074 |
| home_team_home_win_rate | 0.183 | -0.109 | 0.065 |
| home_team_goals_conceded_last_5 | -0.133 | 0.226 | 0.062 |
| home_rest_days | -0.025 | -0.043 | -0.051 |
| home_team_goals_scored_last_5 | 0.075 | -0.139 | -0.044 |
| away_rest_days | -0.059 | 0.004 | -0.044 |
| home_team_home_goals_avg | 0.170 | -0.130 | 0.039 |
| away_team_points_last_5 | -0.012 | -0.036 | -0.036 |
| away_points_before_match | -0.065 | 0.030 | -0.029 |
| away_team_wins_last_5 | 0.004 | -0.042 | -0.028 |
| rest_days_difference | 0.044 | -0.075 | -0.020 |
| home_team_home_conceded_avg | -0.130 | 0.127 | -0.009 |
| home_team_wins_last_5 | 0.137 | -0.138 | 0.007 |
| away_team_goals_conceded_last_5 | 0.037 | -0.037 | 0.002 |
| home_team_points_last_5 | 0.187 | -0.202 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 35 | 13 | 9 | 13 | 37.1% | 25.7% | 37.1% |
| -4..-2 | 35 | 12 | 11 | 12 | 34.3% | 31.4% | 34.3% |
| -1..1 | 60 | 28 | 13 | 19 | 46.7% | 21.7% | 31.7% |
| 2..4 | 33 | 12 | 13 | 8 | 36.4% | 39.4% | 24.2% |
| >4 | 28 | 15 | 6 | 7 | 53.6% | 21.4% | 25.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 19 | 14 | 3 | 2 | 73.7% | 15.8% | 10.5% |
| -5..-2 | 50 | 25 | 13 | 12 | 50.0% | 26.0% | 24.0% |
| -1..1 | 42 | 17 | 13 | 12 | 40.5% | 31.0% | 28.6% |
| 2..5 | 60 | 21 | 16 | 23 | 35.0% | 26.7% | 38.3% |
| >=6 | 20 | 3 | 7 | 10 | 15.0% | 35.0% | 50.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 20 | 8 | 7 | 5 | 40.0% | 35.0% | 25.0% |
| -1..0 | 2 | 0 | 2 | 0 | 0.0% | 100.0% | 0.0% |
| 0 | 141 | 57 | 37 | 47 | 40.4% | 26.2% | 33.3% |
| 1..2 | 1 | 0 | 1 | 0 | 0.0% | 100.0% | 0.0% |
| >2 | 19 | 11 | 5 | 3 | 57.9% | 26.3% | 15.8% |
| unknown | 8 | 4 | 0 | 4 | 50.0% | 0.0% | 50.0% |
- *8 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.4%** home win (37/99)
- `>= 0.5` tier: **46.7%** home win (43/92)
- Home-win gap (>= split minus < split): **+9.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 99 | 37 | 25 | 37 | 37.4% |
| high | >= 0.5 | 92 | 43 | 27 | 22 | 46.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.412 | -3.750 | -4.678 | 10.090 |
| away_points_before_match | 21.788 | 29.808 | 24.525 | 8.020 |
| home_points_before_match | 27.200 | 26.058 | 19.847 | 7.353 |
| position_difference | -1.350 | 0.788 | 1.475 | 2.825 |
| home_position_before_match | 4.625 | 6.096 | 6.627 | 2.002 |
| home_team_points_last_5 | 6.588 | 6.692 | 4.746 | 1.947 |
| home_team_goals_scored_last_5 | 6.100 | 6.577 | 4.983 | 1.594 |
| away_team_goals_scored_last_5 | 6.138 | 6.808 | 5.695 | 1.113 |
| home_team_goals_conceded_last_5 | 5.675 | 5.769 | 6.763 | 1.088 |
| away_team_points_last_5 | 6.287 | 6.942 | 5.932 | 1.010 |
| away_rest_days | 7.211 | 7.654 | 8.214 | 1.004 |
| away_position_before_match | 5.975 | 5.308 | 5.153 | 0.822 |
| home_rest_days | 7.273 | 7.538 | 7.927 | 0.655 |
| away_team_goals_conceded_last_5 | 5.750 | 6.288 | 5.678 | 0.610 |
| rest_days_difference | 0.118 | -0.115 | -0.382 | 0.500 |
| home_team_wins_last_5 | 1.725 | 1.769 | 1.322 | 0.447 |
| home_team_home_goals_avg | 1.403 | 1.311 | 1.074 | 0.329 |
| away_team_wins_last_5 | 1.688 | 1.885 | 1.576 | 0.308 |
| home_team_home_conceded_avg | 1.049 | 1.191 | 1.240 | 0.191 |
| home_team_home_win_rate | 0.441 | 0.421 | 0.334 | 0.107 |
| away_team_away_goals_avg | 1.127 | 1.234 | 1.145 | 0.107 |
| away_team_away_conceded_avg | 1.274 | 1.319 | 1.225 | 0.094 |
| away_team_away_win_rate | 0.321 | 0.375 | 0.336 | 0.054 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\scot1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\scot1\charts\relationships_home_win_pct_by_position.png)

