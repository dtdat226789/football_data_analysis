# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:46:57+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Chance Liga (Czech Republic)
- Scope: league `czech1`

- Matches analysed: **280** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_wins_last_5 | 0.198 | -0.089 | 0.084 |
| home_points_before_match | 0.205 | -0.098 | 0.083 |
| home_position_before_match | -0.214 | 0.132 | -0.065 |
| home_team_points_last_5 | 0.192 | -0.112 | 0.063 |
| home_team_goals_scored_last_5 | 0.162 | -0.087 | 0.059 |
| home_team_home_goals_avg | 0.174 | -0.101 | 0.058 |
| away_points_before_match | 0.004 | 0.070 | 0.054 |
| points_difference | 0.279 | -0.230 | 0.043 |
| rest_days_difference | -0.017 | -0.040 | -0.042 |
| home_team_goals_conceded_last_5 | -0.060 | 0.007 | -0.041 |
| away_team_goals_scored_last_5 | -0.019 | 0.074 | 0.040 |
| away_team_away_win_rate | -0.065 | 0.017 | -0.037 |
| position_difference | -0.240 | 0.199 | -0.036 |
| away_team_goals_conceded_last_5 | 0.095 | -0.057 | 0.030 |
| home_team_home_conceded_avg | 0.009 | 0.027 | 0.027 |
| home_rest_days | -0.042 | 0.016 | -0.021 |
| away_position_before_match | 0.093 | -0.123 | -0.020 |
| away_team_away_goals_avg | -0.077 | 0.057 | -0.016 |
| away_rest_days | -0.035 | 0.015 | -0.016 |
| home_team_home_win_rate | 0.095 | -0.114 | -0.011 |
| away_team_away_conceded_avg | 0.002 | 0.010 | 0.009 |
| away_team_wins_last_5 | -0.073 | 0.070 | -0.004 |
| away_team_points_last_5 | -0.083 | 0.087 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 50 | 13 | 10 | 27 | 26.0% | 20.0% | 54.0% |
| -4..-2 | 54 | 19 | 13 | 22 | 35.2% | 24.1% | 40.7% |
| -1..1 | 74 | 36 | 14 | 24 | 48.6% | 18.9% | 32.4% |
| 2..4 | 60 | 23 | 22 | 15 | 38.3% | 36.7% | 25.0% |
| >4 | 42 | 27 | 8 | 7 | 64.3% | 19.0% | 16.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 52 | 34 | 14 | 4 | 65.4% | 26.9% | 7.7% |
| -5..-2 | 66 | 30 | 18 | 18 | 45.5% | 27.3% | 27.3% |
| -1..1 | 52 | 18 | 18 | 16 | 34.6% | 34.6% | 30.8% |
| 2..5 | 60 | 23 | 9 | 28 | 38.3% | 15.0% | 46.7% |
| >=6 | 50 | 13 | 8 | 29 | 26.0% | 16.0% | 58.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 9 | 5 | 2 | 2 | 55.6% | 22.2% | 22.2% |
| -1..0 | 60 | 30 | 15 | 15 | 50.0% | 25.0% | 25.0% |
| 0 | 126 | 48 | 30 | 48 | 38.1% | 23.8% | 38.1% |
| 1..2 | 66 | 28 | 13 | 25 | 42.4% | 19.7% | 37.9% |
| >2 | 9 | 4 | 4 | 1 | 44.4% | 44.4% | 11.1% |
| unknown | 10 | 3 | 3 | 4 | 30.0% | 30.0% | 40.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **39.2%** home win (74/189)
- `>= 0.5` tier: **48.4%** home win (44/91)
- Home-win gap (>= split minus < split): **+9.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 189 | 74 | 43 | 72 | 39.2% |
| high | >= 0.5 | 91 | 44 | 24 | 23 | 48.4% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.686 | 1.746 | -5.495 | 9.181 |
| away_points_before_match | 22.822 | 17.687 | 25.958 | 8.271 |
| home_points_before_match | 26.508 | 19.433 | 20.463 | 7.076 |
| position_difference | -1.610 | -1.343 | 2.716 | 4.326 |
| home_position_before_match | 7.602 | 8.612 | 10.147 | 2.546 |
| away_position_before_match | 9.212 | 9.955 | 7.432 | 2.524 |
| home_team_points_last_5 | 6.839 | 6.164 | 5.263 | 1.576 |
| away_rest_days | 8.957 | 10.031 | 8.554 | 1.477 |
| home_rest_days | 8.888 | 10.094 | 8.692 | 1.401 |
| home_team_goals_scored_last_5 | 6.441 | 5.746 | 5.179 | 1.262 |
| away_team_points_last_5 | 5.983 | 5.836 | 6.884 | 1.048 |
| away_team_goals_scored_last_5 | 5.847 | 5.522 | 6.305 | 0.783 |
| away_team_goals_conceded_last_5 | 6.246 | 5.493 | 5.674 | 0.753 |
| home_team_wins_last_5 | 1.881 | 1.701 | 1.347 | 0.534 |
| home_team_goals_conceded_last_5 | 5.839 | 5.761 | 6.179 | 0.418 |
| away_team_wins_last_5 | 1.627 | 1.552 | 1.884 | 0.332 |
| home_team_home_goals_avg | 1.414 | 1.218 | 1.130 | 0.284 |
| away_team_away_goals_avg | 1.132 | 1.024 | 1.302 | 0.278 |
| rest_days_difference | -0.017 | 0.062 | 0.088 | 0.105 |
| away_team_away_win_rate | 0.291 | 0.242 | 0.344 | 0.102 |
| home_team_home_win_rate | 0.402 | 0.366 | 0.335 | 0.067 |
| home_team_home_conceded_avg | 1.150 | 1.184 | 1.179 | 0.033 |
| away_team_away_conceded_avg | 1.276 | 1.294 | 1.263 | 0.031 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\czech1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\czech1\charts\relationships_home_win_pct_by_position.png)

