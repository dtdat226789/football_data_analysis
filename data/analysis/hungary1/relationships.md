# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:00:59+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: NB I. (Hungary)
- Scope: league `hungary1`

- Matches analysed: **245** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_goals_avg | -0.277 | 0.049 | -0.179 |
| home_team_goals_conceded_last_5 | -0.206 | 0.005 | -0.156 |
| away_team_points_last_5 | -0.165 | -0.025 | -0.145 |
| away_team_goals_scored_last_5 | -0.130 | -0.062 | -0.144 |
| home_team_home_conceded_avg | -0.082 | -0.088 | -0.125 |
| away_team_wins_last_5 | -0.164 | 0.005 | -0.123 |
| away_points_before_match | -0.134 | -0.026 | -0.122 |
| away_team_away_win_rate | -0.245 | 0.098 | -0.120 |
| home_team_goals_scored_last_5 | -0.073 | -0.071 | -0.107 |
| home_team_points_last_5 | -0.011 | -0.122 | -0.095 |
| home_team_wins_last_5 | -0.018 | -0.098 | -0.084 |
| home_points_before_match | 0.018 | -0.135 | -0.083 |
| away_team_away_conceded_avg | 0.019 | -0.131 | -0.078 |
| position_difference | -0.183 | 0.096 | -0.073 |
| away_team_goals_conceded_last_5 | 0.024 | -0.120 | -0.067 |
| away_position_before_match | 0.158 | -0.077 | 0.067 |
| points_difference | 0.244 | -0.172 | 0.066 |
| rest_days_difference | -0.020 | -0.046 | -0.049 |
| home_rest_days | -0.070 | 0.011 | -0.046 |
| home_position_before_match | -0.104 | 0.060 | -0.038 |
| away_rest_days | -0.063 | 0.026 | -0.030 |
| home_team_home_win_rate | -0.024 | 0.041 | 0.010 |
| home_team_home_goals_avg | -0.028 | 0.020 | -0.007 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 29 | 7 | 11 | 11 | 24.1% | 37.9% | 37.9% |
| -4..-2 | 53 | 16 | 15 | 22 | 30.2% | 28.3% | 41.5% |
| -1..1 | 78 | 31 | 22 | 25 | 39.7% | 28.2% | 32.1% |
| 2..4 | 60 | 31 | 10 | 19 | 51.7% | 16.7% | 31.7% |
| >4 | 25 | 13 | 4 | 8 | 52.0% | 16.0% | 32.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 31 | 19 | 6 | 6 | 61.3% | 19.4% | 19.4% |
| -5..-2 | 68 | 30 | 11 | 27 | 44.1% | 16.2% | 39.7% |
| -1..1 | 44 | 18 | 13 | 13 | 40.9% | 29.5% | 29.5% |
| 2..5 | 68 | 21 | 25 | 22 | 30.9% | 36.8% | 32.4% |
| >=6 | 34 | 10 | 7 | 17 | 29.4% | 20.6% | 50.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 19 | 7 | 6 | 6 | 36.8% | 31.6% | 31.6% |
| -1..0 | 56 | 22 | 17 | 17 | 39.3% | 30.4% | 30.4% |
| 0 | 76 | 31 | 13 | 32 | 40.8% | 17.1% | 42.1% |
| 1..2 | 76 | 29 | 19 | 28 | 38.2% | 25.0% | 36.8% |
| >2 | 6 | 4 | 1 | 1 | 66.7% | 16.7% | 16.7% |
| unknown | 12 | 5 | 6 | 1 | 41.7% | 50.0% | 8.3% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.7%** home win (20/53)
- `>= 0.5` tier: **40.6%** home win (78/192)
- Home-win gap (>= split minus < split): **+2.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 53 | 20 | 17 | 16 | 37.7% |
| high | >= 0.5 | 192 | 78 | 45 | 69 | 40.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.459 | -1.226 | -2.624 | 5.083 |
| home_points_before_match | 21.143 | 16.484 | 16.941 | 4.659 |
| position_difference | -1.051 | 0.806 | 0.871 | 1.922 |
| away_points_before_match | 18.684 | 17.710 | 19.565 | 1.855 |
| away_rest_days | 8.312 | 8.929 | 9.821 | 1.510 |
| home_team_points_last_5 | 6.347 | 5.032 | 5.929 | 1.315 |
| home_rest_days | 8.441 | 8.732 | 9.714 | 1.273 |
| away_position_before_match | 7.357 | 6.145 | 6.247 | 1.212 |
| home_team_goals_conceded_last_5 | 5.980 | 6.468 | 7.035 | 1.056 |
| away_team_goals_conceded_last_5 | 6.816 | 5.919 | 6.353 | 0.897 |
| home_team_goals_scored_last_5 | 6.643 | 5.871 | 6.706 | 0.835 |
| home_position_before_match | 6.306 | 6.952 | 7.118 | 0.812 |
| away_team_points_last_5 | 5.439 | 6.032 | 6.200 | 0.761 |
| home_team_wins_last_5 | 2.898 | 2.290 | 2.776 | 0.608 |
| away_team_goals_scored_last_5 | 6.102 | 6.710 | 6.647 | 0.608 |
| away_team_away_goals_avg | 1.157 | 1.422 | 1.633 | 0.476 |
| rest_days_difference | 0.129 | -0.196 | -0.107 | 0.325 |
| home_team_home_goals_avg | 1.490 | 1.352 | 1.674 | 0.322 |
| away_team_wins_last_5 | 2.500 | 2.774 | 2.765 | 0.274 |
| away_team_away_win_rate | 0.484 | 0.549 | 0.668 | 0.184 |
| away_team_away_conceded_avg | 1.619 | 1.495 | 1.447 | 0.172 |
| home_team_home_conceded_avg | 1.394 | 1.319 | 1.416 | 0.097 |
| home_team_home_win_rate | 0.578 | 0.560 | 0.647 | 0.086 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\hungary1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\hungary1\charts\relationships_home_win_pct_by_position.png)

