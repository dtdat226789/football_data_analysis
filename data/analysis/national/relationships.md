# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:03:50+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: National League (England)
- Scope: league `national`

- Matches analysed: **665** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | 0.035 | 0.109 | 0.103 |
| home_team_goals_conceded_last_5 | -0.045 | 0.146 | 0.066 |
| home_points_before_match | 0.116 | -0.039 | 0.064 |
| away_team_away_goals_avg | -0.024 | 0.117 | 0.063 |
| points_difference | 0.244 | -0.187 | 0.062 |
| away_team_away_conceded_avg | 0.125 | -0.070 | 0.049 |
| home_team_home_goals_avg | 0.139 | -0.092 | 0.045 |
| away_team_goals_scored_last_5 | -0.072 | 0.143 | 0.043 |
| home_position_before_match | -0.175 | 0.140 | -0.040 |
| away_team_goals_conceded_last_5 | 0.077 | -0.033 | 0.037 |
| home_team_wins_last_5 | 0.069 | -0.125 | -0.033 |
| away_team_away_win_rate | -0.069 | 0.121 | 0.030 |
| home_team_points_last_5 | 0.079 | -0.130 | -0.029 |
| home_team_goals_scored_last_5 | 0.090 | -0.068 | 0.024 |
| position_difference | -0.222 | 0.218 | -0.023 |
| away_points_before_match | -0.056 | 0.092 | 0.020 |
| home_team_home_win_rate | 0.058 | -0.088 | -0.016 |
| away_position_before_match | 0.124 | -0.155 | -0.010 |
| away_team_points_last_5 | -0.090 | 0.114 | 0.008 |
| home_rest_days | 0.031 | -0.041 | -0.004 |
| away_rest_days | -0.007 | 0.002 | -0.004 |
| away_team_wins_last_5 | -0.100 | 0.112 | -0.001 |
| rest_days_difference | 0.046 | -0.053 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 117 | 38 | 19 | 60 | 32.5% | 16.2% | 51.3% |
| -4..-2 | 130 | 47 | 35 | 48 | 36.2% | 26.9% | 36.9% |
| -1..1 | 174 | 70 | 44 | 60 | 40.2% | 25.3% | 34.5% |
| 2..4 | 126 | 66 | 31 | 29 | 52.4% | 24.6% | 23.0% |
| >4 | 118 | 72 | 20 | 26 | 61.0% | 16.9% | 22.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 189 | 124 | 28 | 37 | 65.6% | 14.8% | 19.6% |
| -5..-2 | 102 | 46 | 34 | 22 | 45.1% | 33.3% | 21.6% |
| -1..1 | 82 | 28 | 25 | 29 | 34.1% | 30.5% | 35.4% |
| 2..5 | 89 | 36 | 14 | 39 | 40.4% | 15.7% | 43.8% |
| >=6 | 203 | 59 | 48 | 96 | 29.1% | 23.6% | 47.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 62 | 26 | 14 | 22 | 41.9% | 22.6% | 35.5% |
| -1..0 | 36 | 16 | 5 | 15 | 44.4% | 13.9% | 41.7% |
| 0 | 452 | 200 | 106 | 146 | 44.2% | 23.5% | 32.3% |
| 1..2 | 30 | 10 | 7 | 13 | 33.3% | 23.3% | 43.3% |
| >2 | 60 | 31 | 11 | 18 | 51.7% | 18.3% | 30.0% |
| unknown | 25 | 10 | 6 | 9 | 40.0% | 24.0% | 36.0% |
- *25 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.7%** home win (63/163)
- `>= 0.5` tier: **45.8%** home win (230/502)
- Home-win gap (>= split minus < split): **+7.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 163 | 63 | 36 | 64 | 38.7% |
| high | >= 0.5 | 502 | 230 | 113 | 159 | 45.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.184 | -1.745 | -6.063 | 11.247 |
| position_difference | -3.031 | 0.591 | 3.883 | 6.914 |
| home_points_before_match | 30.580 | 25.987 | 24.242 | 6.338 |
| away_points_before_match | 25.396 | 27.732 | 30.305 | 4.909 |
| home_position_before_match | 10.587 | 12.611 | 14.229 | 3.642 |
| away_position_before_match | 13.618 | 12.020 | 10.345 | 3.272 |
| away_team_points_last_5 | 5.645 | 6.383 | 6.933 | 1.288 |
| home_team_points_last_5 | 6.618 | 6.503 | 5.372 | 1.246 |
| away_team_goals_scored_last_5 | 6.075 | 6.812 | 7.211 | 1.136 |
| home_team_goals_conceded_last_5 | 6.126 | 6.483 | 7.121 | 0.995 |
| home_team_goals_scored_last_5 | 6.775 | 6.940 | 5.973 | 0.967 |
| away_team_goals_conceded_last_5 | 6.734 | 6.946 | 6.013 | 0.933 |
| away_team_wins_last_5 | 2.539 | 2.678 | 3.040 | 0.501 |
| home_team_wins_last_5 | 2.904 | 2.893 | 2.457 | 0.447 |
| home_rest_days | 5.760 | 5.483 | 5.498 | 0.277 |
| rest_days_difference | 0.039 | -0.196 | -0.224 | 0.263 |
| away_team_away_conceded_avg | 1.558 | 1.466 | 1.307 | 0.251 |
| home_team_home_goals_avg | 1.553 | 1.499 | 1.314 | 0.239 |
| away_team_away_goals_avg | 1.139 | 1.266 | 1.281 | 0.142 |
| away_team_away_win_rate | 0.478 | 0.555 | 0.572 | 0.094 |
| home_team_home_conceded_avg | 1.170 | 1.199 | 1.263 | 0.093 |
| home_team_home_win_rate | 0.636 | 0.622 | 0.572 | 0.064 |
| away_rest_days | 5.715 | 5.678 | 5.715 | 0.037 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\national\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\national\charts\relationships_home_win_pct_by_position.png)

