# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:48:36+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premier League (Egypt)
- Scope: league `egypt`

- Matches analysed: **322** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_goals_avg | 0.227 | 0.062 | 0.192 |
| home_team_goals_scored_last_5 | 0.260 | 0.004 | 0.175 |
| home_team_home_win_rate | 0.265 | -0.021 | 0.162 |
| home_rest_days | 0.170 | 0.047 | 0.144 |
| away_team_points_last_5 | 0.047 | 0.157 | 0.137 |
| rest_days_difference | 0.172 | 0.034 | 0.136 |
| home_team_goals_conceded_last_5 | 0.053 | 0.150 | 0.136 |
| home_team_wins_last_5 | 0.202 | -0.007 | 0.129 |
| away_points_before_match | 0.047 | 0.144 | 0.128 |
| home_points_before_match | 0.185 | 0.005 | 0.126 |
| away_team_wins_last_5 | 0.032 | 0.152 | 0.124 |
| home_position_before_match | -0.251 | 0.076 | -0.115 |
| home_team_home_conceded_avg | 0.001 | 0.163 | 0.111 |
| away_position_before_match | 0.042 | -0.197 | -0.105 |
| away_team_goals_scored_last_5 | 0.017 | 0.136 | 0.103 |
| home_team_points_last_5 | 0.197 | -0.049 | 0.098 |
| away_team_away_goals_avg | 0.005 | 0.138 | 0.097 |
| away_rest_days | 0.036 | 0.025 | 0.041 |
| away_team_away_win_rate | -0.015 | 0.063 | 0.033 |
| away_team_goals_conceded_last_5 | 0.032 | -0.049 | -0.012 |
| position_difference | -0.221 | 0.205 | -0.008 |
| points_difference | 0.211 | -0.212 | -0.004 |
| away_team_away_conceded_avg | 0.023 | -0.028 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 40 | 10 | 16 | 14 | 25.0% | 40.0% | 35.0% |
| -4..-2 | 73 | 21 | 26 | 26 | 28.8% | 35.6% | 35.6% |
| -1..1 | 110 | 36 | 46 | 28 | 32.7% | 41.8% | 25.5% |
| 2..4 | 62 | 23 | 21 | 18 | 37.1% | 33.9% | 29.0% |
| >4 | 37 | 19 | 13 | 5 | 51.4% | 35.1% | 13.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 78 | 42 | 23 | 13 | 53.8% | 29.5% | 16.7% |
| -5..-2 | 51 | 16 | 21 | 14 | 31.4% | 41.2% | 27.5% |
| -1..1 | 54 | 17 | 23 | 14 | 31.5% | 42.6% | 25.9% |
| 2..5 | 60 | 17 | 28 | 15 | 28.3% | 46.7% | 25.0% |
| >=6 | 79 | 17 | 27 | 35 | 21.5% | 34.2% | 44.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 47 | 16 | 19 | 12 | 34.0% | 40.4% | 25.5% |
| -1..0 | 56 | 16 | 21 | 19 | 28.6% | 37.5% | 33.9% |
| 0 | 96 | 39 | 34 | 23 | 40.6% | 35.4% | 24.0% |
| 1..2 | 72 | 21 | 29 | 22 | 29.2% | 40.3% | 30.6% |
| >2 | 40 | 15 | 13 | 12 | 37.5% | 32.5% | 30.0% |
| unknown | 11 | 2 | 6 | 3 | 18.2% | 54.5% | 27.3% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **29.0%** home win (72/248)
- `>= 0.5` tier: **50.0%** home win (37/74)
- Home-win gap (>= split minus < split): **+21.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 248 | 72 | 101 | 75 | 29.0% |
| high | >= 0.5 | 74 | 37 | 21 | 16 | 50.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.890 | -0.148 | -3.330 | 6.220 |
| position_difference | -2.798 | 0.369 | 2.802 | 5.600 |
| home_points_before_match | 21.358 | 18.369 | 16.714 | 4.644 |
| home_rest_days | 12.215 | 8.500 | 9.511 | 3.715 |
| home_position_before_match | 9.945 | 11.918 | 13.516 | 3.572 |
| rest_days_difference | 2.570 | -0.517 | -0.148 | 3.087 |
| away_position_before_match | 12.743 | 11.549 | 10.714 | 2.029 |
| away_points_before_match | 18.468 | 18.516 | 20.044 | 1.576 |
| home_team_points_last_5 | 6.670 | 5.598 | 5.187 | 1.483 |
| home_team_goals_scored_last_5 | 5.248 | 4.287 | 3.956 | 1.292 |
| away_team_goals_scored_last_5 | 4.138 | 4.402 | 4.802 | 0.665 |
| away_rest_days | 9.602 | 9.017 | 9.659 | 0.642 |
| home_team_goals_conceded_last_5 | 4.330 | 4.443 | 4.846 | 0.516 |
| home_team_wins_last_5 | 1.615 | 1.287 | 1.198 | 0.417 |
| away_team_goals_conceded_last_5 | 4.596 | 4.180 | 4.516 | 0.416 |
| home_team_home_goals_avg | 0.995 | 0.793 | 0.800 | 0.202 |
| home_team_home_conceded_avg | 0.812 | 0.861 | 1.007 | 0.195 |
| away_team_points_last_5 | 5.872 | 5.943 | 6.066 | 0.194 |
| away_team_away_goals_avg | 0.773 | 0.852 | 0.927 | 0.154 |
| home_team_home_win_rate | 0.356 | 0.237 | 0.231 | 0.125 |
| away_team_wins_last_5 | 1.367 | 1.393 | 1.451 | 0.084 |
| away_team_away_conceded_avg | 0.908 | 0.854 | 0.904 | 0.054 |
| away_team_away_win_rate | 0.255 | 0.268 | 0.269 | 0.015 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\egypt\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\egypt\charts\relationships_home_win_pct_by_position.png)

