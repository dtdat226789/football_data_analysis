# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:57:33+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premier League (Egypt)
- Scope: league `egypt`

- Matches analysed: **372** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_goals_avg | 0.216 | -0.001 | 0.143 |
| home_team_goals_scored_last_5 | 0.251 | -0.041 | 0.140 |
| home_rest_days | 0.163 | 0.040 | 0.137 |
| rest_days_difference | 0.159 | 0.032 | 0.129 |
| away_team_points_last_5 | 0.051 | 0.130 | 0.123 |
| home_team_goals_conceded_last_5 | 0.057 | 0.117 | 0.118 |
| away_points_before_match | 0.053 | 0.106 | 0.108 |
| away_team_wins_last_5 | 0.063 | 0.085 | 0.101 |
| home_points_before_match | 0.172 | -0.022 | 0.099 |
| away_position_before_match | 0.055 | -0.182 | -0.088 |
| away_team_goals_scored_last_5 | 0.010 | 0.114 | 0.085 |
| home_team_home_conceded_avg | 0.053 | 0.071 | 0.084 |
| away_team_away_win_rate | 0.031 | 0.080 | 0.076 |
| home_team_points_last_5 | 0.187 | -0.089 | 0.064 |
| home_position_before_match | -0.225 | 0.127 | -0.062 |
| away_team_away_goals_avg | -0.011 | 0.088 | 0.054 |
| home_team_home_win_rate | 0.034 | -0.102 | -0.048 |
| away_rest_days | 0.042 | 0.017 | 0.040 |
| away_team_goals_conceded_last_5 | 0.039 | -0.069 | -0.021 |
| away_team_away_conceded_avg | 0.050 | -0.078 | -0.020 |
| position_difference | -0.210 | 0.232 | 0.019 |
| points_difference | 0.199 | -0.214 | -0.015 |
| home_team_wins_last_5 | 0.123 | -0.124 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 46 | 11 | 17 | 18 | 23.9% | 37.0% | 39.1% |
| -4..-2 | 79 | 23 | 26 | 30 | 29.1% | 32.9% | 38.0% |
| -1..1 | 134 | 44 | 54 | 36 | 32.8% | 40.3% | 26.9% |
| 2..4 | 71 | 28 | 22 | 21 | 39.4% | 31.0% | 29.6% |
| >4 | 42 | 22 | 13 | 7 | 52.4% | 31.0% | 16.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 92 | 51 | 23 | 18 | 55.4% | 25.0% | 19.6% |
| -5..-2 | 56 | 17 | 23 | 16 | 30.4% | 41.1% | 28.6% |
| -1..1 | 66 | 22 | 28 | 16 | 33.3% | 42.4% | 24.2% |
| 2..5 | 70 | 20 | 29 | 21 | 28.6% | 41.4% | 30.0% |
| >=6 | 88 | 18 | 29 | 41 | 20.5% | 33.0% | 46.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 52 | 19 | 19 | 14 | 36.5% | 36.5% | 26.9% |
| -1..0 | 64 | 22 | 21 | 21 | 34.4% | 32.8% | 32.8% |
| 0 | 111 | 42 | 38 | 31 | 37.8% | 34.2% | 27.9% |
| 1..2 | 84 | 24 | 31 | 29 | 28.6% | 36.9% | 34.5% |
| >2 | 40 | 15 | 13 | 12 | 37.5% | 32.5% | 30.0% |
| unknown | 21 | 6 | 10 | 5 | 28.6% | 47.6% | 23.8% |
- *21 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **26.6%** home win (25/94)
- `>= 0.5` tier: **37.1%** home win (103/278)
- Home-win gap (>= split minus < split): **+10.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 94 | 25 | 34 | 35 | 26.6% |
| high | >= 0.5 | 278 | 103 | 98 | 77 | 37.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| position_difference | -2.938 | 0.485 | 2.643 | 5.580 |
| points_difference | 2.633 | -0.182 | -2.884 | 5.517 |
| home_points_before_match | 18.727 | 17.091 | 14.027 | 4.700 |
| home_position_before_match | 9.711 | 11.720 | 13.357 | 3.646 |
| home_rest_days | 11.500 | 8.336 | 8.916 | 3.164 |
| rest_days_difference | 2.197 | -0.475 | -0.075 | 2.672 |
| away_position_before_match | 12.648 | 11.235 | 10.714 | 1.934 |
| home_team_points_last_5 | 6.219 | 5.288 | 4.661 | 1.558 |
| home_team_goals_scored_last_5 | 4.922 | 4.045 | 3.554 | 1.368 |
| away_points_before_match | 16.094 | 17.273 | 16.911 | 1.179 |
| home_team_wins_last_5 | 3.156 | 2.848 | 2.518 | 0.638 |
| away_team_goals_scored_last_5 | 3.742 | 4.205 | 4.375 | 0.633 |
| away_rest_days | 9.268 | 8.811 | 8.991 | 0.457 |
| home_team_goals_conceded_last_5 | 3.992 | 4.212 | 4.393 | 0.401 |
| away_team_points_last_5 | 5.367 | 5.652 | 5.554 | 0.284 |
| away_team_goals_conceded_last_5 | 4.250 | 3.977 | 4.062 | 0.273 |
| home_team_home_goals_avg | 0.976 | 0.756 | 0.726 | 0.250 |
| away_team_wins_last_5 | 2.867 | 2.985 | 2.839 | 0.146 |
| away_team_away_goals_avg | 0.744 | 0.856 | 0.878 | 0.134 |
| away_team_away_conceded_avg | 0.883 | 0.835 | 0.801 | 0.081 |
| home_team_home_win_rate | 0.651 | 0.619 | 0.582 | 0.069 |
| home_team_home_conceded_avg | 0.852 | 0.849 | 0.894 | 0.046 |
| away_team_away_win_rate | 0.599 | 0.597 | 0.625 | 0.028 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\egypt\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\egypt\charts\relationships_home_win_pct_by_position.png)

