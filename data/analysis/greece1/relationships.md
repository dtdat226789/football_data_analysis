# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:00:06+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super League (Greece)
- Scope: league `greece1`

- Matches analysed: **281** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.212 | -0.117 | 0.096 |
| home_rest_days | 0.051 | 0.066 | 0.089 |
| away_rest_days | 0.059 | 0.035 | 0.074 |
| home_team_home_win_rate | 0.057 | -0.163 | -0.067 |
| home_team_points_last_5 | 0.142 | -0.106 | 0.045 |
| rest_days_difference | -0.023 | 0.086 | 0.041 |
| home_team_wins_last_5 | 0.076 | -0.040 | 0.036 |
| home_points_before_match | 0.075 | -0.130 | -0.028 |
| home_team_home_goals_avg | 0.157 | -0.150 | 0.026 |
| away_team_away_conceded_avg | 0.070 | -0.049 | 0.025 |
| away_position_before_match | 0.168 | -0.168 | 0.023 |
| away_team_away_goals_avg | -0.059 | 0.102 | 0.022 |
| away_points_before_match | -0.118 | 0.116 | -0.018 |
| away_team_goals_scored_last_5 | -0.121 | 0.167 | 0.016 |
| points_difference | 0.276 | -0.351 | -0.015 |
| home_team_goals_conceded_last_5 | -0.145 | 0.154 | -0.014 |
| position_difference | -0.316 | 0.361 | -0.012 |
| away_team_away_win_rate | -0.076 | 0.108 | 0.012 |
| away_team_points_last_5 | -0.194 | 0.244 | 0.008 |
| home_team_home_conceded_avg | -0.173 | 0.218 | 0.008 |
| home_position_before_match | -0.241 | 0.298 | 0.007 |
| away_team_goals_conceded_last_5 | 0.145 | -0.165 | 0.006 |
| away_team_wins_last_5 | -0.189 | 0.225 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 55 | 9 | 17 | 29 | 16.4% | 30.9% | 52.7% |
| -4..-2 | 49 | 12 | 18 | 19 | 24.5% | 36.7% | 38.8% |
| -1..1 | 86 | 39 | 23 | 24 | 45.3% | 26.7% | 27.9% |
| 2..4 | 61 | 34 | 13 | 14 | 55.7% | 21.3% | 23.0% |
| >4 | 30 | 22 | 6 | 2 | 73.3% | 20.0% | 6.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 43 | 33 | 8 | 2 | 76.7% | 18.6% | 4.7% |
| -5..-2 | 56 | 25 | 15 | 16 | 44.6% | 26.8% | 28.6% |
| -1..1 | 75 | 35 | 22 | 18 | 46.7% | 29.3% | 24.0% |
| 2..5 | 52 | 12 | 17 | 23 | 23.1% | 32.7% | 44.2% |
| >=6 | 55 | 11 | 15 | 29 | 20.0% | 27.3% | 52.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 9 | 5 | 2 | 2 | 55.6% | 22.2% | 22.2% |
| -1..0 | 61 | 28 | 16 | 17 | 45.9% | 26.2% | 27.9% |
| 0 | 133 | 52 | 34 | 47 | 39.1% | 25.6% | 35.3% |
| 1..2 | 54 | 17 | 21 | 16 | 31.5% | 38.9% | 29.6% |
| >2 | 7 | 3 | 2 | 2 | 42.9% | 28.6% | 28.6% |
| unknown | 17 | 11 | 2 | 4 | 64.7% | 11.8% | 23.5% |
- *17 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **35.1%** home win (34/97)
- `>= 0.5` tier: **44.6%** home win (82/184)
- Home-win gap (>= split minus < split): **+9.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 97 | 34 | 22 | 41 | 35.1% |
| high | >= 0.5 | 184 | 82 | 55 | 47 | 44.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.836 | -1.571 | -5.682 | 9.518 |
| home_points_before_match | 20.750 | 21.662 | 14.591 | 7.071 |
| away_points_before_match | 16.914 | 23.234 | 20.273 | 6.320 |
| position_difference | -2.172 | 0.922 | 3.182 | 5.354 |
| home_position_before_match | 6.483 | 8.909 | 9.852 | 3.370 |
| away_team_points_last_5 | 4.836 | 6.506 | 7.102 | 2.266 |
| away_position_before_match | 8.655 | 7.987 | 6.670 | 1.985 |
| away_team_goals_conceded_last_5 | 5.888 | 5.078 | 4.080 | 1.808 |
| home_team_goals_conceded_last_5 | 4.741 | 5.455 | 6.511 | 1.770 |
| home_team_points_last_5 | 6.259 | 5.286 | 4.727 | 1.531 |
| home_team_goals_scored_last_5 | 5.871 | 4.753 | 4.466 | 1.405 |
| away_team_goals_scored_last_5 | 4.698 | 6.091 | 6.034 | 1.393 |
| away_team_wins_last_5 | 2.336 | 2.974 | 3.148 | 0.812 |
| away_rest_days | 7.971 | 7.805 | 8.321 | 0.516 |
| home_rest_days | 7.867 | 7.907 | 8.360 | 0.494 |
| home_team_home_conceded_avg | 0.838 | 1.115 | 1.295 | 0.457 |
| home_team_wins_last_5 | 2.776 | 2.584 | 2.364 | 0.412 |
| home_team_home_goals_avg | 1.432 | 1.233 | 1.146 | 0.286 |
| away_team_away_conceded_avg | 1.323 | 1.393 | 1.183 | 0.211 |
| away_team_away_goals_avg | 0.919 | 1.114 | 1.051 | 0.195 |
| rest_days_difference | -0.105 | 0.080 | 0.071 | 0.185 |
| home_team_home_win_rate | 0.635 | 0.624 | 0.507 | 0.128 |
| away_team_away_win_rate | 0.462 | 0.549 | 0.527 | 0.087 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\greece1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\greece1\charts\relationships_home_win_pct_by_position.png)

