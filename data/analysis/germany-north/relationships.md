# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:50:49+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Regionalliga North (Germany)
- Scope: league `germany-north`

- Matches analysed: **317** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_wins_last_5 | 0.255 | -0.097 | 0.140 |
| home_team_goals_scored_last_5 | 0.218 | -0.078 | 0.123 |
| home_team_points_last_5 | 0.230 | -0.120 | 0.102 |
| position_difference | -0.312 | 0.227 | -0.091 |
| away_team_points_last_5 | -0.172 | 0.088 | -0.078 |
| away_position_before_match | 0.223 | -0.148 | 0.076 |
| away_rest_days | -0.081 | -0.009 | -0.074 |
| points_difference | 0.302 | -0.244 | 0.071 |
| away_points_before_match | -0.165 | 0.093 | -0.069 |
| away_team_goals_scored_last_5 | -0.140 | 0.085 | -0.053 |
| rest_days_difference | 0.050 | 0.015 | 0.053 |
| away_team_wins_last_5 | -0.150 | 0.099 | -0.052 |
| home_team_home_conceded_avg | -0.004 | 0.074 | 0.051 |
| home_position_before_match | -0.208 | 0.166 | -0.050 |
| home_team_home_goals_avg | 0.157 | -0.112 | 0.047 |
| home_team_home_win_rate | 0.142 | -0.103 | 0.042 |
| away_team_away_goals_avg | -0.096 | 0.054 | -0.039 |
| home_team_goals_conceded_last_5 | -0.099 | 0.062 | -0.036 |
| away_team_away_win_rate | -0.100 | 0.083 | -0.021 |
| home_rest_days | -0.031 | 0.009 | -0.019 |
| away_team_goals_conceded_last_5 | 0.126 | -0.117 | 0.019 |
| home_points_before_match | 0.095 | -0.119 | -0.009 |
| away_team_away_conceded_avg | 0.148 | -0.171 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 64 | 19 | 12 | 33 | 29.7% | 18.8% | 51.6% |
| -4..-2 | 67 | 23 | 23 | 21 | 34.3% | 34.3% | 31.3% |
| -1..1 | 79 | 39 | 9 | 31 | 49.4% | 11.4% | 39.2% |
| 2..4 | 47 | 20 | 12 | 15 | 42.6% | 25.5% | 31.9% |
| >4 | 60 | 34 | 13 | 13 | 56.7% | 21.7% | 21.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 75 | 49 | 12 | 14 | 65.3% | 16.0% | 18.7% |
| -5..-2 | 53 | 29 | 9 | 15 | 54.7% | 17.0% | 28.3% |
| -1..1 | 50 | 17 | 9 | 24 | 34.0% | 18.0% | 48.0% |
| 2..5 | 66 | 19 | 20 | 27 | 28.8% | 30.3% | 40.9% |
| >=6 | 73 | 21 | 19 | 33 | 28.8% | 26.0% | 45.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 60 | 20 | 20 | 20 | 33.3% | 33.3% | 33.3% |
| -1..0 | 62 | 22 | 12 | 28 | 35.5% | 19.4% | 45.2% |
| 0 | 79 | 34 | 14 | 31 | 43.0% | 17.7% | 39.2% |
| 1..2 | 59 | 35 | 12 | 12 | 59.3% | 20.3% | 20.3% |
| >2 | 46 | 21 | 10 | 15 | 45.7% | 21.7% | 32.6% |
| unknown | 11 | 3 | 1 | 7 | 27.3% | 9.1% | 63.6% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **36.7%** home win (69/188)
- `>= 0.5` tier: **51.2%** home win (66/129)
- Home-win gap (>= split minus < split): **+14.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 188 | 69 | 47 | 72 | 36.7% |
| high | >= 0.5 | 129 | 66 | 22 | 41 | 51.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.852 | -3.536 | -5.549 | 10.401 |
| away_points_before_match | 20.044 | 26.304 | 26.088 | 6.260 |
| away_rest_days | 7.386 | 12.309 | 8.729 | 4.922 |
| position_difference | -2.519 | 2.130 | 2.372 | 4.890 |
| home_points_before_match | 24.896 | 22.768 | 20.540 | 4.356 |
| home_position_before_match | 8.489 | 11.536 | 10.717 | 3.047 |
| home_rest_days | 7.684 | 10.485 | 9.057 | 2.801 |
| away_position_before_match | 11.007 | 9.406 | 8.345 | 2.662 |
| rest_days_difference | 0.311 | -1.824 | 0.311 | 2.135 |
| home_team_goals_scored_last_5 | 9.037 | 7.551 | 7.345 | 1.692 |
| home_team_points_last_5 | 6.978 | 5.812 | 5.496 | 1.482 |
| away_team_goals_scored_last_5 | 7.481 | 8.174 | 8.956 | 1.474 |
| away_team_goals_conceded_last_5 | 8.496 | 8.536 | 7.195 | 1.342 |
| away_team_points_last_5 | 5.889 | 6.391 | 7.159 | 1.270 |
| home_team_goals_conceded_last_5 | 7.748 | 8.957 | 8.434 | 1.208 |
| home_team_wins_last_5 | 2.037 | 1.580 | 1.504 | 0.533 |
| away_team_wins_last_5 | 1.637 | 1.739 | 2.088 | 0.451 |
| away_team_away_conceded_avg | 2.007 | 1.879 | 1.647 | 0.359 |
| home_team_home_goals_avg | 1.984 | 1.787 | 1.676 | 0.308 |
| home_team_home_conceded_avg | 1.549 | 1.792 | 1.667 | 0.243 |
| away_team_away_goals_avg | 1.528 | 1.728 | 1.715 | 0.200 |
| home_team_home_win_rate | 0.460 | 0.381 | 0.383 | 0.079 |
| away_team_away_win_rate | 0.323 | 0.386 | 0.387 | 0.064 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\germany-north\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\germany-north\charts\relationships_home_win_pct_by_position.png)

