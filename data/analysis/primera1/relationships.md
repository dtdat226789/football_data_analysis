# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:04:23+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Primera RFEF - Group 1 (Spain)
- Scope: league `primera1`

- Matches analysed: **398** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.147 | 0.043 | 0.134 |
| away_team_goals_scored_last_5 | 0.063 | 0.088 | 0.105 |
| away_team_away_goals_avg | 0.054 | 0.086 | 0.097 |
| position_difference | -0.010 | 0.132 | 0.083 |
| away_position_before_match | -0.007 | -0.103 | -0.075 |
| away_points_before_match | 0.003 | 0.105 | 0.074 |
| away_team_goals_conceded_last_5 | 0.099 | -0.005 | 0.068 |
| points_difference | 0.048 | -0.147 | -0.066 |
| home_team_home_win_rate | 0.074 | 0.007 | 0.058 |
| away_team_points_last_5 | -0.013 | 0.087 | 0.051 |
| home_team_home_goals_avg | 0.102 | -0.043 | 0.043 |
| home_position_before_match | -0.021 | 0.076 | 0.037 |
| home_rest_days | -0.005 | -0.045 | -0.034 |
| home_points_before_match | 0.032 | 0.016 | 0.034 |
| away_rest_days | -0.020 | -0.025 | -0.032 |
| away_team_wins_last_5 | -0.038 | 0.085 | 0.031 |
| home_team_home_conceded_avg | 0.051 | -0.016 | 0.025 |
| home_team_goals_scored_last_5 | 0.002 | -0.035 | -0.022 |
| home_team_goals_conceded_last_5 | -0.014 | -0.013 | -0.019 |
| home_team_points_last_5 | 0.042 | -0.019 | 0.017 |
| away_team_away_win_rate | -0.042 | 0.035 | -0.006 |
| home_team_wins_last_5 | 0.032 | -0.030 | 0.002 |
| rest_days_difference | 0.016 | -0.020 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 61 | 20 | 18 | 23 | 32.8% | 29.5% | 37.7% |
| -4..-2 | 93 | 42 | 24 | 27 | 45.2% | 25.8% | 29.0% |
| -1..1 | 122 | 60 | 36 | 26 | 49.2% | 29.5% | 21.3% |
| 2..4 | 74 | 41 | 20 | 13 | 55.4% | 27.0% | 17.6% |
| >4 | 48 | 19 | 15 | 14 | 39.6% | 31.2% | 29.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 100 | 44 | 33 | 23 | 44.0% | 33.0% | 23.0% |
| -5..-2 | 67 | 39 | 15 | 13 | 58.2% | 22.4% | 19.4% |
| -1..1 | 52 | 21 | 22 | 9 | 40.4% | 42.3% | 17.3% |
| 2..5 | 67 | 30 | 17 | 20 | 44.8% | 25.4% | 29.9% |
| >=6 | 112 | 48 | 26 | 38 | 42.9% | 23.2% | 33.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 26 | 8 | 13 | 5 | 30.8% | 50.0% | 19.2% |
| -1..0 | 91 | 42 | 21 | 28 | 46.2% | 23.1% | 30.8% |
| 0 | 157 | 72 | 43 | 42 | 45.9% | 27.4% | 26.8% |
| 1..2 | 104 | 49 | 32 | 23 | 47.1% | 30.8% | 22.1% |
| >2 | 9 | 6 | 1 | 2 | 66.7% | 11.1% | 22.2% |
| unknown | 11 | 5 | 3 | 3 | 45.5% | 27.3% | 27.3% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **42.5%** home win (85/200)
- `>= 0.5` tier: **49.0%** home win (97/198)
- Home-win gap (>= split minus < split): **+6.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 200 | 85 | 54 | 61 | 42.5% |
| high | >= 0.5 | 198 | 97 | 59 | 42 | 49.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 23.978 | 27.522 | 26.680 | 3.544 |
| home_points_before_match | 24.769 | 27.566 | 24.330 | 3.236 |
| points_difference | 0.791 | 0.044 | -2.350 | 3.141 |
| position_difference | 0.044 | -0.496 | 2.126 | 2.622 |
| home_position_before_match | 11.462 | 10.381 | 12.456 | 2.076 |
| away_position_before_match | 11.418 | 10.876 | 10.330 | 1.087 |
| home_team_goals_scored_last_5 | 5.363 | 5.841 | 5.175 | 0.666 |
| away_team_points_last_5 | 6.132 | 6.628 | 6.786 | 0.655 |
| away_team_goals_scored_last_5 | 5.654 | 5.540 | 5.981 | 0.441 |
| home_team_points_last_5 | 6.110 | 6.292 | 5.864 | 0.428 |
| away_team_goals_conceded_last_5 | 5.687 | 5.292 | 5.388 | 0.395 |
| home_rest_days | 7.215 | 6.918 | 7.100 | 0.297 |
| away_team_wins_last_5 | 1.599 | 1.752 | 1.883 | 0.285 |
| away_rest_days | 7.203 | 7.009 | 7.170 | 0.194 |
| home_team_wins_last_5 | 1.599 | 1.673 | 1.534 | 0.139 |
| home_team_home_goals_avg | 1.274 | 1.275 | 1.141 | 0.134 |
| away_team_away_conceded_avg | 1.330 | 1.215 | 1.226 | 0.115 |
| rest_days_difference | 0.011 | -0.091 | -0.070 | 0.102 |
| home_team_goals_conceded_last_5 | 5.588 | 5.655 | 5.689 | 0.101 |
| home_team_home_win_rate | 0.439 | 0.466 | 0.413 | 0.054 |
| away_team_away_goals_avg | 0.925 | 0.928 | 0.970 | 0.046 |
| home_team_home_conceded_avg | 0.957 | 0.925 | 0.914 | 0.044 |
| away_team_away_win_rate | 0.234 | 0.253 | 0.264 | 0.030 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\primera1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\primera1\charts\relationships_home_win_pct_by_position.png)

