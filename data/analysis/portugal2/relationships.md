# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:03:50+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Liga Portugal 2 (Portugal)
- Scope: league `portugal2`

- Matches analysed: **310** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.052 | 0.081 | 0.090 |
| home_team_goals_conceded_last_5 | 0.004 | 0.063 | 0.046 |
| away_team_points_last_5 | 0.021 | 0.047 | 0.046 |
| home_rest_days | 0.024 | 0.035 | 0.041 |
| home_team_home_win_rate | 0.032 | 0.017 | 0.033 |
| position_difference | -0.063 | 0.014 | -0.033 |
| home_position_before_match | -0.080 | 0.031 | -0.032 |
| away_team_away_win_rate | -0.026 | 0.068 | 0.029 |
| away_team_away_goals_avg | -0.048 | 0.086 | 0.027 |
| home_team_home_goals_avg | -0.006 | 0.044 | 0.026 |
| rest_days_difference | -0.001 | 0.037 | 0.024 |
| away_team_goals_scored_last_5 | -0.008 | 0.037 | 0.020 |
| away_team_wins_last_5 | 0.001 | 0.025 | 0.017 |
| home_team_points_last_5 | 0.029 | -0.006 | 0.016 |
| away_rest_days | 0.021 | -0.000 | 0.014 |
| away_position_before_match | 0.009 | 0.011 | 0.014 |
| home_team_goals_scored_last_5 | 0.060 | -0.039 | 0.014 |
| away_team_goals_conceded_last_5 | -0.005 | 0.024 | 0.013 |
| home_points_before_match | 0.023 | -0.042 | -0.013 |
| points_difference | 0.022 | -0.038 | -0.011 |
| home_team_wins_last_5 | 0.016 | -0.027 | -0.008 |
| away_points_before_match | 0.009 | -0.017 | -0.006 |
| home_team_home_conceded_avg | -0.063 | 0.056 | -0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 40 | 16 | 9 | 15 | 40.0% | 22.5% | 37.5% |
| -4..-2 | 79 | 32 | 21 | 26 | 40.5% | 26.6% | 32.9% |
| -1..1 | 92 | 41 | 20 | 31 | 44.6% | 21.7% | 33.7% |
| 2..4 | 60 | 30 | 16 | 14 | 50.0% | 26.7% | 23.3% |
| >4 | 39 | 12 | 10 | 17 | 30.8% | 25.6% | 43.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 78 | 33 | 17 | 28 | 42.3% | 21.8% | 35.9% |
| -5..-2 | 54 | 30 | 13 | 11 | 55.6% | 24.1% | 20.4% |
| -1..1 | 45 | 17 | 13 | 15 | 37.8% | 28.9% | 33.3% |
| 2..5 | 50 | 14 | 12 | 24 | 28.0% | 24.0% | 48.0% |
| >=6 | 83 | 37 | 21 | 25 | 44.6% | 25.3% | 30.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 50 | 17 | 14 | 19 | 34.0% | 28.0% | 38.0% |
| -1..0 | 63 | 31 | 15 | 17 | 49.2% | 23.8% | 27.0% |
| 0 | 83 | 36 | 21 | 26 | 43.4% | 25.3% | 31.3% |
| 1..2 | 80 | 35 | 17 | 28 | 43.8% | 21.2% | 35.0% |
| >2 | 23 | 8 | 5 | 10 | 34.8% | 21.7% | 43.5% |
| unknown | 11 | 4 | 4 | 3 | 36.4% | 36.4% | 27.3% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **41.7%** home win (93/223)
- `>= 0.5` tier: **43.7%** home win (38/87)
- Home-win gap (>= split minus < split): **+2.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 223 | 93 | 57 | 73 | 41.7% |
| high | >= 0.5 | 87 | 38 | 19 | 30 | 43.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 24.412 | 19.908 | 22.340 | 4.504 |
| home_points_before_match | 24.244 | 19.934 | 22.194 | 4.310 |
| away_rest_days | 8.000 | 9.333 | 8.440 | 1.333 |
| home_rest_days | 8.047 | 9.041 | 8.500 | 0.994 |
| home_position_before_match | 9.756 | 10.684 | 10.010 | 0.928 |
| away_position_before_match | 9.565 | 10.434 | 9.981 | 0.869 |
| home_team_goals_conceded_last_5 | 5.756 | 4.921 | 5.718 | 0.835 |
| home_team_goals_scored_last_5 | 5.863 | 5.066 | 5.223 | 0.797 |
| away_team_goals_conceded_last_5 | 5.420 | 5.145 | 5.748 | 0.603 |
| away_team_points_last_5 | 6.611 | 6.224 | 6.097 | 0.514 |
| away_team_goals_scored_last_5 | 5.794 | 5.579 | 5.388 | 0.406 |
| rest_days_difference | 0.063 | -0.222 | 0.060 | 0.285 |
| home_team_points_last_5 | 6.321 | 6.118 | 6.058 | 0.262 |
| position_difference | 0.191 | 0.250 | 0.029 | 0.221 |
| points_difference | -0.168 | 0.026 | -0.146 | 0.194 |
| away_team_wins_last_5 | 1.817 | 1.750 | 1.631 | 0.186 |
| away_team_away_goals_avg | 1.080 | 0.998 | 1.131 | 0.132 |
| home_team_home_goals_avg | 1.204 | 1.115 | 1.231 | 0.117 |
| home_team_wins_last_5 | 1.740 | 1.684 | 1.641 | 0.100 |
| away_team_away_win_rate | 0.318 | 0.260 | 0.327 | 0.067 |
| away_team_away_conceded_avg | 1.157 | 1.207 | 1.213 | 0.056 |
| home_team_home_win_rate | 0.367 | 0.323 | 0.376 | 0.053 |
| home_team_home_conceded_avg | 1.082 | 1.043 | 1.083 | 0.040 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\portugal2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\portugal2\charts\relationships_home_win_pct_by_position.png)

