# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:02:28+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: National League North (England)
- Scope: league `north`

- Matches analysed: **560** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.196 | -0.026 | 0.137 |
| home_team_wins_last_5 | 0.200 | -0.046 | 0.126 |
| home_team_points_last_5 | 0.191 | -0.052 | 0.114 |
| home_position_before_match | -0.172 | 0.038 | -0.110 |
| home_team_home_goals_avg | 0.119 | 0.001 | 0.095 |
| home_team_home_win_rate | 0.098 | 0.003 | 0.080 |
| points_difference | 0.229 | -0.163 | 0.065 |
| position_difference | -0.213 | 0.146 | -0.065 |
| away_team_wins_last_5 | -0.033 | 0.120 | 0.060 |
| away_team_points_last_5 | -0.032 | 0.119 | 0.059 |
| home_points_before_match | 0.109 | -0.047 | 0.052 |
| away_team_goals_conceded_last_5 | 0.002 | -0.071 | -0.050 |
| away_team_away_win_rate | -0.080 | 0.147 | 0.042 |
| home_team_goals_conceded_last_5 | -0.084 | 0.034 | -0.042 |
| home_team_home_conceded_avg | -0.050 | 0.002 | -0.038 |
| home_rest_days | 0.002 | 0.050 | 0.037 |
| away_team_away_goals_avg | -0.068 | 0.125 | 0.036 |
| away_team_goals_scored_last_5 | -0.061 | 0.114 | 0.032 |
| rest_days_difference | -0.010 | 0.050 | 0.028 |
| away_position_before_match | 0.121 | -0.165 | -0.022 |
| away_team_away_conceded_avg | 0.054 | -0.082 | -0.016 |
| away_rest_days | 0.010 | 0.007 | 0.013 |
| away_points_before_match | -0.044 | 0.061 | 0.009 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 91 | 35 | 16 | 40 | 38.5% | 17.6% | 44.0% |
| -4..-2 | 117 | 40 | 26 | 51 | 34.2% | 22.2% | 43.6% |
| -1..1 | 156 | 71 | 33 | 52 | 45.5% | 21.2% | 33.3% |
| 2..4 | 107 | 43 | 31 | 33 | 40.2% | 29.0% | 30.8% |
| >4 | 89 | 50 | 20 | 19 | 56.2% | 22.5% | 21.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 162 | 81 | 41 | 40 | 50.0% | 25.3% | 24.7% |
| -5..-2 | 93 | 45 | 17 | 31 | 48.4% | 18.3% | 33.3% |
| -1..1 | 57 | 27 | 17 | 13 | 47.4% | 29.8% | 22.8% |
| 2..5 | 87 | 33 | 15 | 39 | 37.9% | 17.2% | 44.8% |
| >=6 | 161 | 53 | 36 | 72 | 32.9% | 22.4% | 44.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 75 | 29 | 21 | 25 | 38.7% | 28.0% | 33.3% |
| -1..0 | 1 | 0 | 1 | 0 | 0.0% | 100.0% | 0.0% |
| 0 | 400 | 173 | 82 | 145 | 43.2% | 20.5% | 36.2% |
| 1..2 | 5 | 1 | 2 | 2 | 20.0% | 40.0% | 40.0% |
| >2 | 67 | 28 | 17 | 22 | 41.8% | 25.4% | 32.8% |
| unknown | 12 | 8 | 3 | 1 | 66.7% | 25.0% | 8.3% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **40.1%** home win (144/359)
- `>= 0.5` tier: **47.3%** home win (95/201)
- Home-win gap (>= split minus < split): **+7.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 359 | 144 | 81 | 134 | 40.1% |
| high | >= 0.5 | 201 | 95 | 45 | 61 | 47.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.699 | -0.095 | -3.810 | 6.509 |
| away_points_before_match | 30.803 | 29.651 | 34.600 | 4.949 |
| position_difference | -1.536 | -0.460 | 2.626 | 4.161 |
| home_points_before_match | 33.502 | 29.556 | 30.790 | 3.947 |
| away_position_before_match | 12.649 | 13.183 | 10.800 | 2.383 |
| home_position_before_match | 11.113 | 12.722 | 13.426 | 2.313 |
| home_team_points_last_5 | 6.983 | 6.460 | 5.918 | 1.065 |
| home_team_goals_scored_last_5 | 7.598 | 6.762 | 6.667 | 0.932 |
| away_team_points_last_5 | 6.406 | 6.135 | 7.041 | 0.906 |
| away_team_goals_scored_last_5 | 6.967 | 6.794 | 7.621 | 0.827 |
| home_team_goals_conceded_last_5 | 6.858 | 7.032 | 7.549 | 0.691 |
| away_team_goals_conceded_last_5 | 6.967 | 7.357 | 6.862 | 0.496 |
| away_rest_days | 5.810 | 5.976 | 5.552 | 0.424 |
| home_team_wins_last_5 | 1.996 | 1.802 | 1.600 | 0.396 |
| home_rest_days | 5.697 | 5.821 | 5.562 | 0.259 |
| away_team_wins_last_5 | 1.782 | 1.730 | 1.985 | 0.254 |
| rest_days_difference | -0.113 | -0.154 | 0.010 | 0.165 |
| away_team_away_goals_avg | 1.306 | 1.285 | 1.446 | 0.161 |
| home_team_home_conceded_avg | 1.310 | 1.346 | 1.386 | 0.076 |
| away_team_away_win_rate | 0.295 | 0.293 | 0.360 | 0.067 |
| away_team_away_conceded_avg | 1.551 | 1.541 | 1.492 | 0.059 |
| home_team_home_goals_avg | 1.552 | 1.502 | 1.530 | 0.051 |
| home_team_home_win_rate | 0.427 | 0.427 | 0.411 | 0.016 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\north\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\north\charts\relationships_home_win_pct_by_position.png)

