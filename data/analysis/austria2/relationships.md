# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:55:00+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 2. Liga (Austria)
- Scope: league `austria2`

- Matches analysed: **279** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_points_before_match | -0.109 | -0.096 | -0.152 |
| home_points_before_match | -0.029 | -0.166 | -0.136 |
| away_team_points_last_5 | -0.077 | -0.105 | -0.133 |
| away_team_away_win_rate | -0.083 | -0.086 | -0.124 |
| away_team_wins_last_5 | -0.058 | -0.083 | -0.103 |
| away_position_before_match | 0.124 | -0.007 | 0.094 |
| away_team_away_goals_avg | -0.017 | -0.106 | -0.086 |
| home_team_wins_last_5 | 0.028 | -0.141 | -0.074 |
| home_team_home_conceded_avg | -0.085 | 0.001 | -0.067 |
| home_position_before_match | -0.049 | 0.151 | 0.063 |
| away_team_goals_scored_last_5 | 0.041 | -0.122 | -0.050 |
| home_rest_days | -0.019 | -0.054 | -0.050 |
| home_team_points_last_5 | 0.056 | -0.129 | -0.043 |
| away_rest_days | -0.008 | -0.051 | -0.040 |
| home_team_home_win_rate | 0.072 | -0.143 | -0.040 |
| position_difference | -0.122 | 0.111 | -0.022 |
| away_team_away_conceded_avg | 0.061 | -0.101 | -0.020 |
| points_difference | 0.119 | -0.111 | 0.020 |
| away_team_goals_conceded_last_5 | 0.116 | -0.120 | 0.011 |
| rest_days_difference | -0.013 | 0.003 | -0.009 |
| home_team_goals_conceded_last_5 | -0.031 | 0.025 | -0.008 |
| home_team_goals_scored_last_5 | 0.057 | -0.077 | -0.007 |
| home_team_home_goals_avg | 0.093 | -0.117 | -0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 38 | 15 | 7 | 16 | 39.5% | 18.4% | 42.1% |
| -4..-2 | 64 | 29 | 10 | 25 | 45.3% | 15.6% | 39.1% |
| -1..1 | 78 | 32 | 21 | 25 | 41.0% | 26.9% | 32.1% |
| 2..4 | 67 | 30 | 18 | 19 | 44.8% | 26.9% | 28.4% |
| >4 | 32 | 15 | 10 | 7 | 46.9% | 31.2% | 21.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 59 | 37 | 12 | 10 | 62.7% | 20.3% | 16.9% |
| -5..-2 | 59 | 23 | 16 | 20 | 39.0% | 27.1% | 33.9% |
| -1..1 | 45 | 17 | 9 | 19 | 37.8% | 20.0% | 42.2% |
| 2..5 | 62 | 27 | 16 | 19 | 43.5% | 25.8% | 30.6% |
| >=6 | 54 | 17 | 13 | 24 | 31.5% | 24.1% | 44.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 22 | 7 | 4 | 11 | 31.8% | 18.2% | 50.0% |
| -1..0 | 55 | 24 | 13 | 18 | 43.6% | 23.6% | 32.7% |
| 0 | 112 | 58 | 27 | 27 | 51.8% | 24.1% | 24.1% |
| 1..2 | 64 | 23 | 18 | 23 | 35.9% | 28.1% | 35.9% |
| >2 | 10 | 5 | 2 | 3 | 50.0% | 20.0% | 30.0% |
| unknown | 16 | 4 | 2 | 10 | 25.0% | 12.5% | 62.5% |
- *16 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **39.1%** home win (34/87)
- `>= 0.5` tier: **45.3%** home win (87/192)
- Home-win gap (>= split minus < split): **+6.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 87 | 34 | 13 | 40 | 39.1% |
| high | >= 0.5 | 192 | 87 | 53 | 52 | 45.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 17.636 | 15.439 | 14.261 | 3.375 |
| points_difference | 1.826 | -0.697 | -1.533 | 3.359 |
| position_difference | -1.256 | 0.106 | 1.272 | 2.528 |
| away_rest_days | 10.795 | 10.188 | 8.463 | 2.331 |
| home_rest_days | 10.179 | 10.344 | 8.537 | 1.807 |
| home_position_before_match | 7.570 | 8.303 | 8.946 | 1.375 |
| home_team_points_last_5 | 6.025 | 6.136 | 4.967 | 1.169 |
| away_position_before_match | 8.826 | 8.197 | 7.674 | 1.153 |
| away_team_goals_conceded_last_5 | 5.992 | 6.015 | 4.924 | 1.091 |
| home_team_goals_scored_last_5 | 5.777 | 6.227 | 5.174 | 1.053 |
| rest_days_difference | -0.615 | 0.156 | 0.073 | 0.772 |
| away_team_goals_scored_last_5 | 6.058 | 5.636 | 5.391 | 0.667 |
| home_team_wins_last_5 | 2.686 | 2.742 | 2.315 | 0.427 |
| home_team_goals_conceded_last_5 | 5.471 | 5.879 | 5.815 | 0.408 |
| home_team_home_goals_avg | 1.438 | 1.461 | 1.097 | 0.363 |
| away_points_before_match | 15.810 | 16.136 | 15.793 | 0.343 |
| away_team_points_last_5 | 5.818 | 5.515 | 5.728 | 0.303 |
| away_team_away_goals_avg | 1.224 | 1.412 | 1.148 | 0.264 |
| away_team_away_conceded_avg | 1.391 | 1.351 | 1.135 | 0.256 |
| home_team_home_win_rate | 0.610 | 0.682 | 0.478 | 0.204 |
| home_team_home_conceded_avg | 1.203 | 1.190 | 1.304 | 0.114 |
| away_team_away_win_rate | 0.514 | 0.616 | 0.536 | 0.102 |
| away_team_wins_last_5 | 2.628 | 2.636 | 2.576 | 0.060 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\austria2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\austria2\charts\relationships_home_win_pct_by_position.png)

