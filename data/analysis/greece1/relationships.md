# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:51:46+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super League (Greece)
- Scope: league `greece1`

- Matches analysed: **246** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.241 | -0.140 | 0.099 |
| home_rest_days | 0.060 | 0.050 | 0.085 |
| home_team_home_win_rate | 0.119 | -0.255 | -0.083 |
| away_rest_days | 0.071 | 0.031 | 0.080 |
| home_position_before_match | -0.190 | 0.294 | 0.052 |
| away_team_away_conceded_avg | 0.122 | -0.078 | 0.046 |
| away_position_before_match | 0.222 | -0.194 | 0.046 |
| home_team_points_last_5 | 0.163 | -0.134 | 0.040 |
| home_team_wins_last_5 | 0.185 | -0.159 | 0.039 |
| home_points_before_match | 0.097 | -0.164 | -0.037 |
| home_team_home_conceded_avg | -0.157 | 0.233 | 0.036 |
| home_team_goals_conceded_last_5 | -0.095 | 0.150 | 0.028 |
| away_team_wins_last_5 | -0.176 | 0.239 | 0.024 |
| points_difference | 0.287 | -0.365 | -0.022 |
| away_team_goals_conceded_last_5 | 0.199 | -0.200 | 0.022 |
| away_points_before_match | -0.120 | 0.112 | -0.020 |
| away_team_points_last_5 | -0.196 | 0.255 | 0.019 |
| away_team_goals_scored_last_5 | -0.114 | 0.159 | 0.019 |
| rest_days_difference | -0.035 | 0.056 | 0.010 |
| position_difference | -0.314 | 0.373 | 0.005 |
| home_team_home_goals_avg | 0.128 | -0.144 | 0.003 |
| away_team_away_goals_avg | -0.100 | 0.119 | 0.002 |
| away_team_away_win_rate | -0.063 | 0.070 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 49 | 9 | 15 | 25 | 18.4% | 30.6% | 51.0% |
| -4..-2 | 44 | 10 | 17 | 17 | 22.7% | 38.6% | 38.6% |
| -1..1 | 67 | 30 | 19 | 18 | 44.8% | 28.4% | 26.9% |
| 2..4 | 58 | 32 | 12 | 14 | 55.2% | 20.7% | 24.1% |
| >4 | 28 | 21 | 5 | 2 | 75.0% | 17.9% | 7.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 40 | 31 | 7 | 2 | 77.5% | 17.5% | 5.0% |
| -5..-2 | 51 | 24 | 13 | 14 | 47.1% | 25.5% | 27.5% |
| -1..1 | 59 | 25 | 19 | 15 | 42.4% | 32.2% | 25.4% |
| 2..5 | 47 | 11 | 15 | 21 | 23.4% | 31.9% | 44.7% |
| >=6 | 49 | 11 | 14 | 24 | 22.4% | 28.6% | 49.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 5 | 4 | 0 | 1 | 80.0% | 0.0% | 20.0% |
| -1..0 | 50 | 24 | 12 | 14 | 48.0% | 24.0% | 28.0% |
| 0 | 127 | 49 | 34 | 44 | 38.6% | 26.8% | 34.6% |
| 1..2 | 48 | 16 | 19 | 13 | 33.3% | 39.6% | 27.1% |
| >2 | 7 | 3 | 2 | 2 | 42.9% | 28.6% | 28.6% |
| unknown | 9 | 6 | 1 | 2 | 66.7% | 11.1% | 22.2% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **31.2%** home win (49/157)
- `>= 0.5` tier: **59.6%** home win (53/89)
- Home-win gap (>= split minus < split): **+28.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 157 | 49 | 49 | 59 | 31.2% |
| high | >= 0.5 | 89 | 53 | 19 | 17 | 59.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.324 | -1.750 | -6.158 | 10.481 |
| home_points_before_match | 23.225 | 24.221 | 16.566 | 7.655 |
| away_points_before_match | 18.902 | 25.971 | 22.724 | 7.069 |
| position_difference | -2.343 | 0.985 | 3.053 | 5.396 |
| home_position_before_match | 6.706 | 8.824 | 9.829 | 3.123 |
| away_team_points_last_5 | 5.167 | 7.029 | 7.474 | 2.307 |
| away_position_before_match | 9.049 | 7.838 | 6.776 | 2.273 |
| away_team_goals_conceded_last_5 | 6.461 | 5.235 | 4.408 | 2.053 |
| home_team_goals_conceded_last_5 | 5.206 | 5.632 | 6.882 | 1.676 |
| home_team_points_last_5 | 6.745 | 5.676 | 5.145 | 1.600 |
| away_team_goals_scored_last_5 | 5.039 | 6.515 | 6.303 | 1.475 |
| home_team_goals_scored_last_5 | 6.294 | 5.103 | 4.855 | 1.439 |
| away_team_wins_last_5 | 1.324 | 1.912 | 2.066 | 0.742 |
| home_team_wins_last_5 | 1.863 | 1.441 | 1.289 | 0.573 |
| away_rest_days | 8.083 | 7.897 | 8.459 | 0.562 |
| home_rest_days | 8.042 | 8.134 | 8.533 | 0.492 |
| home_team_home_conceded_avg | 0.894 | 1.167 | 1.368 | 0.473 |
| rest_days_difference | -0.042 | 0.209 | 0.108 | 0.251 |
| away_team_away_goals_avg | 0.962 | 1.202 | 1.118 | 0.240 |
| home_team_home_goals_avg | 1.423 | 1.294 | 1.222 | 0.201 |
| home_team_home_win_rate | 0.479 | 0.334 | 0.308 | 0.171 |
| away_team_away_conceded_avg | 1.401 | 1.333 | 1.231 | 0.170 |
| away_team_away_win_rate | 0.287 | 0.367 | 0.312 | 0.080 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\greece1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\greece1\charts\relationships_home_win_pct_by_position.png)

