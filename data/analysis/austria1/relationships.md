# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:44:13+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Bundesliga (Austria)
- Scope: league `austria1`

- Matches analysed: **195** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | -0.055 | -0.157 | -0.159 |
| points_difference | -0.112 | -0.095 | -0.153 |
| away_position_before_match | 0.048 | -0.223 | -0.135 |
| position_difference | 0.039 | 0.114 | 0.115 |
| home_team_home_conceded_avg | -0.024 | -0.079 | -0.077 |
| rest_days_difference | 0.015 | -0.113 | -0.076 |
| away_team_away_win_rate | -0.099 | 0.189 | 0.072 |
| home_team_goals_conceded_last_5 | 0.041 | -0.115 | -0.058 |
| away_team_goals_conceded_last_5 | 0.088 | -0.159 | -0.058 |
| away_points_before_match | 0.042 | 0.032 | 0.055 |
| home_rest_days | -0.046 | -0.023 | -0.051 |
| away_team_away_goals_avg | -0.107 | 0.168 | 0.050 |
| away_team_wins_last_5 | -0.060 | 0.112 | 0.042 |
| away_rest_days | -0.048 | -0.008 | -0.040 |
| home_team_goals_scored_last_5 | -0.023 | -0.024 | -0.035 |
| home_team_home_win_rate | 0.041 | 0.005 | 0.034 |
| away_team_points_last_5 | -0.070 | 0.105 | 0.029 |
| home_team_home_goals_avg | 0.023 | 0.017 | 0.029 |
| away_team_goals_scored_last_5 | -0.076 | 0.042 | -0.023 |
| home_points_before_match | -0.009 | -0.012 | -0.016 |
| home_position_before_match | 0.095 | -0.072 | 0.014 |
| home_team_points_last_5 | -0.046 | 0.030 | -0.011 |
| home_team_wins_last_5 | -0.023 | 0.032 | 0.008 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 31 | 15 | 9 | 7 | 48.4% | 29.0% | 22.6% |
| -4..-2 | 43 | 18 | 12 | 13 | 41.9% | 27.9% | 30.2% |
| -1..1 | 51 | 14 | 16 | 21 | 27.5% | 31.4% | 41.2% |
| 2..4 | 45 | 25 | 6 | 14 | 55.6% | 13.3% | 31.1% |
| >4 | 25 | 12 | 7 | 6 | 48.0% | 28.0% | 24.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 21 | 9 | 6 | 6 | 42.9% | 28.6% | 28.6% |
| -5..-2 | 50 | 23 | 12 | 15 | 46.0% | 24.0% | 30.0% |
| -1..1 | 43 | 21 | 9 | 13 | 48.8% | 20.9% | 30.2% |
| 2..5 | 63 | 25 | 17 | 21 | 39.7% | 27.0% | 33.3% |
| >=6 | 18 | 6 | 6 | 6 | 33.3% | 33.3% | 33.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 9 | 3 | 1 | 5 | 33.3% | 11.1% | 55.6% |
| -1..0 | 35 | 11 | 10 | 14 | 31.4% | 28.6% | 40.0% |
| 0 | 99 | 51 | 23 | 25 | 51.5% | 23.2% | 25.3% |
| 1..2 | 45 | 17 | 13 | 15 | 37.8% | 28.9% | 33.3% |
| >2 | 1 | 0 | 1 | 0 | 0.0% | 100.0% | 0.0% |
| unknown | 6 | 2 | 2 | 2 | 33.3% | 33.3% | 33.3% |
- *6 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **45.5%** home win (65/143)
- `>= 0.5` tier: **36.5%** home win (19/52)
- Home-win gap (>= split minus < split): **-9.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 143 | 65 | 35 | 43 | 45.5% |
| high | >= 0.5 | 52 | 19 | 15 | 18 | 36.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 21.929 | 23.440 | 19.967 | 3.473 |
| home_points_before_match | 22.167 | 23.160 | 19.820 | 3.340 |
| away_position_before_match | 7.429 | 6.040 | 5.967 | 1.461 |
| away_team_goals_conceded_last_5 | 6.667 | 5.720 | 5.426 | 1.240 |
| home_team_goals_conceded_last_5 | 6.512 | 6.540 | 5.377 | 1.163 |
| away_team_points_last_5 | 5.810 | 6.880 | 6.459 | 1.070 |
| home_position_before_match | 7.060 | 6.520 | 6.098 | 0.961 |
| position_difference | -0.369 | 0.480 | 0.131 | 0.849 |
| away_team_goals_scored_last_5 | 5.952 | 6.520 | 6.213 | 0.568 |
| points_difference | 0.238 | -0.280 | -0.148 | 0.518 |
| rest_days_difference | -0.024 | 0.229 | -0.220 | 0.450 |
| home_team_points_last_5 | 5.905 | 6.160 | 6.295 | 0.390 |
| home_team_goals_scored_last_5 | 5.940 | 6.200 | 5.820 | 0.380 |
| away_team_wins_last_5 | 1.536 | 1.860 | 1.770 | 0.324 |
| away_team_away_goals_avg | 1.125 | 1.169 | 1.399 | 0.274 |
| away_rest_days | 9.183 | 9.062 | 9.288 | 0.226 |
| home_rest_days | 9.159 | 9.292 | 9.068 | 0.224 |
| home_team_wins_last_5 | 1.560 | 1.680 | 1.689 | 0.129 |
| home_team_home_goals_avg | 1.262 | 1.375 | 1.262 | 0.113 |
| away_team_away_conceded_avg | 1.378 | 1.319 | 1.266 | 0.112 |
| home_team_home_conceded_avg | 1.292 | 1.197 | 1.184 | 0.109 |
| away_team_away_win_rate | 0.290 | 0.360 | 0.398 | 0.109 |
| home_team_home_win_rate | 0.352 | 0.415 | 0.336 | 0.079 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\austria1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\austria1\charts\relationships_home_win_pct_by_position.png)

