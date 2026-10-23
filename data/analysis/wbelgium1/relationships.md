# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:11:06+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super League Women (Belgium)
- Scope: league `wbelgium1`

- Matches analysed: **108** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_goals_avg | 0.066 | -0.274 | -0.181 |
| home_position_before_match | -0.140 | 0.318 | 0.165 |
| home_team_home_win_rate | 0.158 | -0.288 | -0.126 |
| home_team_home_conceded_avg | -0.166 | 0.276 | 0.111 |
| home_team_wins_last_5 | 0.150 | -0.249 | -0.100 |
| home_team_goals_scored_last_5 | 0.142 | -0.234 | -0.093 |
| rest_days_difference | -0.013 | 0.105 | 0.079 |
| home_team_points_last_5 | 0.147 | -0.221 | -0.078 |
| position_difference | -0.341 | 0.385 | 0.075 |
| away_team_away_win_rate | -0.207 | 0.096 | -0.070 |
| home_points_before_match | 0.124 | -0.184 | -0.065 |
| away_position_before_match | 0.318 | -0.205 | 0.059 |
| home_rest_days | -0.055 | 0.113 | 0.054 |
| away_team_away_goals_avg | -0.220 | 0.129 | -0.051 |
| away_points_before_match | -0.155 | 0.077 | -0.047 |
| away_team_away_conceded_avg | 0.186 | -0.120 | 0.034 |
| points_difference | 0.312 | -0.297 | -0.023 |
| away_team_goals_scored_last_5 | -0.170 | 0.168 | 0.017 |
| home_team_goals_conceded_last_5 | -0.182 | 0.138 | -0.016 |
| away_team_wins_last_5 | -0.162 | 0.159 | 0.016 |
| away_team_points_last_5 | -0.192 | 0.176 | 0.008 |
| away_rest_days | -0.046 | 0.048 | 0.006 |
| away_team_goals_conceded_last_5 | 0.164 | -0.149 | -0.006 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 23 | 6 | 4 | 13 | 26.1% | 17.4% | 56.5% |
| -4..-2 | 19 | 3 | 9 | 7 | 15.8% | 47.4% | 36.8% |
| -1..1 | 26 | 8 | 5 | 13 | 30.8% | 19.2% | 50.0% |
| 2..4 | 14 | 7 | 3 | 4 | 50.0% | 21.4% | 28.6% |
| >4 | 26 | 20 | 4 | 2 | 76.9% | 15.4% | 7.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 3 | 3 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| -5..-2 | 37 | 26 | 8 | 3 | 70.3% | 21.6% | 8.1% |
| -1..1 | 33 | 10 | 9 | 14 | 30.3% | 27.3% | 42.4% |
| 2..5 | 32 | 4 | 8 | 20 | 12.5% | 25.0% | 62.5% |
| >=6 | 3 | 1 | 0 | 2 | 33.3% | 0.0% | 66.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 7 | 3 | 0 | 4 | 42.9% | 0.0% | 57.1% |
| -1..0 | 14 | 6 | 4 | 4 | 42.9% | 28.6% | 28.6% |
| 0 | 63 | 28 | 16 | 19 | 44.4% | 25.4% | 30.2% |
| 1..2 | 11 | 5 | 1 | 5 | 45.5% | 9.1% | 45.5% |
| >2 | 9 | 1 | 2 | 6 | 11.1% | 22.2% | 66.7% |
| unknown | 4 | 1 | 2 | 1 | 25.0% | 50.0% | 25.0% |
- *4 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **32.9%** home win (24/73)
- `>= 0.5` tier: **57.1%** home win (20/35)
- Home-win gap (>= split minus < split): **+24.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 73 | 24 | 18 | 31 | 32.9% |
| high | >= 0.5 | 35 | 20 | 7 | 8 | 57.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 8.136 | -0.760 | -6.487 | 14.624 |
| home_points_before_match | 22.318 | 19.040 | 14.000 | 8.318 |
| away_points_before_match | 14.182 | 19.800 | 20.487 | 6.305 |
| position_difference | -1.841 | -0.040 | 1.692 | 3.533 |
| away_team_points_last_5 | 4.886 | 6.120 | 7.641 | 2.755 |
| home_team_goals_scored_last_5 | 8.045 | 5.680 | 5.667 | 2.379 |
| home_team_points_last_5 | 7.568 | 5.320 | 5.205 | 2.363 |
| away_team_goals_conceded_last_5 | 8.182 | 6.160 | 5.846 | 2.336 |
| away_position_before_match | 5.523 | 4.200 | 3.667 | 1.856 |
| away_team_goals_scored_last_5 | 5.977 | 6.400 | 7.795 | 1.818 |
| home_team_goals_conceded_last_5 | 5.773 | 6.120 | 7.513 | 1.740 |
| home_position_before_match | 3.682 | 4.160 | 5.359 | 1.677 |
| away_rest_days | 10.186 | 8.826 | 10.237 | 1.411 |
| rest_days_difference | -0.372 | 0.652 | 0.184 | 1.024 |
| home_rest_days | 9.814 | 9.478 | 10.421 | 0.943 |
| home_team_wins_last_5 | 2.227 | 1.440 | 1.359 | 0.868 |
| away_team_wins_last_5 | 1.318 | 1.760 | 2.179 | 0.861 |
| home_team_home_conceded_avg | 1.077 | 1.192 | 1.662 | 0.584 |
| away_team_away_goals_avg | 1.116 | 1.487 | 1.670 | 0.554 |
| home_team_home_goals_avg | 1.565 | 1.429 | 1.134 | 0.431 |
| away_team_away_conceded_avg | 1.434 | 1.392 | 1.118 | 0.315 |
| home_team_home_win_rate | 0.469 | 0.382 | 0.276 | 0.193 |
| away_team_away_win_rate | 0.278 | 0.367 | 0.413 | 0.135 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\wbelgium1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\wbelgium1\charts\relationships_home_win_pct_by_position.png)

