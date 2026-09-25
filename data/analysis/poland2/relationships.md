# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:41:21+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Division 1 (Poland)
- Scope: league `poland2`

- Matches analysed: **408** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_goals_avg | 0.084 | 0.005 | 0.067 |
| home_rest_days | 0.052 | 0.018 | 0.052 |
| away_rest_days | 0.039 | 0.028 | 0.049 |
| home_position_before_match | -0.142 | 0.089 | -0.044 |
| home_team_wins_last_5 | 0.052 | -0.115 | -0.042 |
| away_team_away_win_rate | -0.070 | 0.018 | -0.040 |
| points_difference | 0.101 | -0.162 | -0.039 |
| away_team_away_conceded_avg | -0.003 | -0.048 | -0.036 |
| away_position_before_match | 0.054 | -0.105 | -0.034 |
| away_team_points_last_5 | -0.063 | 0.022 | -0.032 |
| away_team_goals_scored_last_5 | 0.003 | 0.041 | 0.032 |
| home_team_goals_scored_last_5 | 0.083 | -0.049 | 0.028 |
| away_team_wins_last_5 | -0.036 | 0.001 | -0.026 |
| home_points_before_match | -0.007 | -0.026 | -0.024 |
| home_team_home_win_rate | 0.062 | -0.091 | -0.018 |
| home_team_points_last_5 | 0.101 | -0.083 | 0.017 |
| rest_days_difference | 0.060 | -0.046 | 0.013 |
| away_team_away_goals_avg | -0.065 | 0.056 | -0.010 |
| home_team_home_conceded_avg | -0.113 | 0.131 | 0.008 |
| position_difference | -0.142 | 0.141 | -0.007 |
| away_team_goals_conceded_last_5 | 0.037 | -0.049 | -0.006 |
| home_team_goals_conceded_last_5 | -0.058 | 0.070 | 0.006 |
| away_points_before_match | -0.068 | 0.073 | 0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 60 | 19 | 17 | 24 | 31.7% | 28.3% | 40.0% |
| -4..-2 | 93 | 46 | 19 | 28 | 49.5% | 20.4% | 30.1% |
| -1..1 | 114 | 41 | 33 | 40 | 36.0% | 28.9% | 35.1% |
| 2..4 | 80 | 37 | 21 | 22 | 46.2% | 26.2% | 27.5% |
| >4 | 61 | 27 | 22 | 12 | 44.3% | 36.1% | 19.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 90 | 42 | 31 | 17 | 46.7% | 34.4% | 18.9% |
| -5..-2 | 85 | 38 | 21 | 26 | 44.7% | 24.7% | 30.6% |
| -1..1 | 54 | 23 | 14 | 17 | 42.6% | 25.9% | 31.5% |
| 2..5 | 90 | 31 | 27 | 32 | 34.4% | 30.0% | 35.6% |
| >=6 | 89 | 36 | 19 | 34 | 40.4% | 21.3% | 38.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 59 | 27 | 15 | 17 | 45.8% | 25.4% | 28.8% |
| -1..0 | 90 | 26 | 29 | 35 | 28.9% | 32.2% | 38.9% |
| 0 | 89 | 41 | 26 | 22 | 46.1% | 29.2% | 24.7% |
| 1..2 | 135 | 65 | 33 | 37 | 48.1% | 24.4% | 27.4% |
| >2 | 16 | 5 | 3 | 8 | 31.2% | 18.8% | 50.0% |
| unknown | 19 | 6 | 6 | 7 | 31.6% | 31.6% | 36.8% |
- *19 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **42.5%** home win (45/106)
- `>= 0.5` tier: **41.4%** home win (125/302)
- Home-win gap (>= split minus < split): **-1.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 106 | 45 | 24 | 37 | 42.5% |
| high | >= 0.5 | 302 | 125 | 88 | 89 | 41.4% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.465 | 0.884 | -2.413 | 3.877 |
| position_difference | -0.694 | -1.196 | 1.746 | 2.942 |
| away_points_before_match | 18.935 | 18.580 | 21.048 | 2.467 |
| home_position_before_match | 9.582 | 9.339 | 11.373 | 2.034 |
| home_points_before_match | 20.400 | 19.464 | 18.635 | 1.765 |
| home_team_goals_scored_last_5 | 6.441 | 7.009 | 5.690 | 1.318 |
| home_team_points_last_5 | 6.129 | 6.205 | 5.286 | 0.920 |
| away_position_before_match | 10.276 | 10.536 | 9.627 | 0.909 |
| away_team_goals_conceded_last_5 | 6.371 | 6.795 | 6.103 | 0.691 |
| home_rest_days | 8.817 | 9.085 | 8.420 | 0.665 |
| away_rest_days | 8.780 | 9.113 | 8.529 | 0.584 |
| home_team_goals_conceded_last_5 | 6.065 | 6.509 | 6.603 | 0.538 |
| home_team_home_goals_avg | 1.469 | 1.757 | 1.398 | 0.359 |
| home_team_home_conceded_avg | 1.126 | 1.242 | 1.458 | 0.332 |
| home_team_wins_last_5 | 2.871 | 2.830 | 2.540 | 0.331 |
| away_team_points_last_5 | 5.853 | 5.768 | 5.992 | 0.224 |
| away_team_goals_scored_last_5 | 6.453 | 6.357 | 6.508 | 0.151 |
| rest_days_difference | 0.037 | -0.028 | -0.109 | 0.146 |
| away_team_away_goals_avg | 1.220 | 1.275 | 1.343 | 0.123 |
| home_team_home_win_rate | 0.630 | 0.696 | 0.584 | 0.112 |
| away_team_away_conceded_avg | 1.506 | 1.527 | 1.468 | 0.059 |
| away_team_wins_last_5 | 2.794 | 2.750 | 2.738 | 0.056 |
| away_team_away_win_rate | 0.532 | 0.537 | 0.548 | 0.016 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\poland2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\poland2\charts\relationships_home_win_pct_by_position.png)

