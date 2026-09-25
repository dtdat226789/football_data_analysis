# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:41:57+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Liga Portugal 2 (Portugal)
- Scope: league `portugal2`

- Matches analysed: **363** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.041 | 0.097 | 0.095 |
| away_team_wins_last_5 | 0.061 | 0.076 | 0.095 |
| home_team_home_win_rate | -0.006 | 0.110 | 0.072 |
| away_team_points_last_5 | 0.033 | 0.057 | 0.062 |
| home_team_wins_last_5 | 0.052 | 0.035 | 0.060 |
| home_team_goals_conceded_last_5 | 0.024 | 0.057 | 0.056 |
| away_team_away_goals_avg | -0.013 | 0.087 | 0.052 |
| home_team_home_goals_avg | 0.006 | 0.064 | 0.049 |
| away_team_goals_scored_last_5 | 0.004 | 0.048 | 0.037 |
| home_team_points_last_5 | 0.038 | 0.009 | 0.032 |
| home_rest_days | 0.030 | 0.015 | 0.031 |
| home_team_home_conceded_avg | -0.013 | 0.053 | 0.028 |
| home_position_before_match | -0.062 | 0.025 | -0.024 |
| rest_days_difference | 0.007 | 0.027 | 0.024 |
| away_team_goals_conceded_last_5 | 0.010 | 0.021 | 0.022 |
| position_difference | -0.059 | 0.026 | -0.021 |
| home_team_goals_scored_last_5 | 0.065 | -0.035 | 0.019 |
| points_difference | 0.020 | -0.037 | -0.013 |
| away_team_away_win_rate | 0.012 | 0.002 | 0.010 |
| away_points_before_match | 0.028 | -0.015 | 0.009 |
| away_rest_days | 0.021 | -0.013 | 0.005 |
| away_position_before_match | 0.019 | -0.011 | 0.005 |
| home_points_before_match | 0.040 | -0.036 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 45 | 18 | 11 | 16 | 40.0% | 24.4% | 35.6% |
| -4..-2 | 89 | 34 | 23 | 32 | 38.2% | 25.8% | 36.0% |
| -1..1 | 117 | 54 | 25 | 38 | 46.2% | 21.4% | 32.5% |
| 2..4 | 70 | 34 | 18 | 18 | 48.6% | 25.7% | 25.7% |
| >4 | 42 | 13 | 11 | 18 | 31.0% | 26.2% | 42.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 87 | 36 | 20 | 31 | 41.4% | 23.0% | 35.6% |
| -5..-2 | 65 | 35 | 15 | 15 | 53.8% | 23.1% | 23.1% |
| -1..1 | 58 | 25 | 14 | 19 | 43.1% | 24.1% | 32.8% |
| 2..5 | 58 | 16 | 15 | 27 | 27.6% | 25.9% | 46.6% |
| >=6 | 95 | 41 | 24 | 30 | 43.2% | 25.3% | 31.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 53 | 18 | 15 | 20 | 34.0% | 28.3% | 37.7% |
| -1..0 | 76 | 36 | 17 | 23 | 47.4% | 22.4% | 30.3% |
| 0 | 90 | 37 | 24 | 29 | 41.1% | 26.7% | 32.2% |
| 1..2 | 100 | 44 | 22 | 34 | 44.0% | 22.0% | 34.0% |
| >2 | 24 | 9 | 5 | 10 | 37.5% | 20.8% | 41.7% |
| unknown | 20 | 9 | 5 | 6 | 45.0% | 25.0% | 30.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **45.0%** home win (36/80)
- `>= 0.5` tier: **41.3%** home win (117/283)
- Home-win gap (>= split minus < split): **-3.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 80 | 36 | 19 | 25 | 45.0% |
| high | >= 0.5 | 283 | 117 | 69 | 97 | 41.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 21.340 | 17.705 | 19.516 | 3.635 |
| home_points_before_match | 21.183 | 17.659 | 19.311 | 3.524 |
| away_rest_days | 7.896 | 9.060 | 8.207 | 1.164 |
| home_position_before_match | 9.641 | 10.670 | 9.844 | 1.030 |
| away_position_before_match | 9.562 | 10.352 | 9.598 | 0.790 |
| home_rest_days | 8.000 | 8.762 | 8.267 | 0.762 |
| home_team_goals_scored_last_5 | 5.392 | 4.739 | 4.811 | 0.654 |
| home_team_goals_conceded_last_5 | 5.275 | 4.750 | 5.221 | 0.525 |
| away_team_goals_conceded_last_5 | 4.993 | 4.784 | 5.279 | 0.495 |
| rest_days_difference | 0.118 | -0.241 | 0.060 | 0.359 |
| away_team_points_last_5 | 6.098 | 5.886 | 5.803 | 0.295 |
| position_difference | 0.078 | 0.318 | 0.246 | 0.240 |
| away_team_goals_scored_last_5 | 5.261 | 5.239 | 5.066 | 0.196 |
| away_team_wins_last_5 | 2.752 | 2.568 | 2.656 | 0.183 |
| points_difference | -0.157 | -0.045 | -0.205 | 0.159 |
| home_team_points_last_5 | 5.837 | 5.727 | 5.689 | 0.148 |
| away_team_away_goals_avg | 1.010 | 0.982 | 1.069 | 0.088 |
| away_team_away_conceded_avg | 1.066 | 1.150 | 1.151 | 0.086 |
| home_team_home_goals_avg | 1.109 | 1.076 | 1.158 | 0.082 |
| away_team_away_win_rate | 0.570 | 0.502 | 0.550 | 0.068 |
| home_team_home_win_rate | 0.575 | 0.586 | 0.641 | 0.066 |
| home_team_wins_last_5 | 2.621 | 2.568 | 2.590 | 0.053 |
| home_team_home_conceded_avg | 1.024 | 1.031 | 1.000 | 0.031 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\portugal2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\portugal2\charts\relationships_home_win_pct_by_position.png)

