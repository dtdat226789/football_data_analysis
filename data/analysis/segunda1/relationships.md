# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:45:32+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Segunda RFEF - Group 1 (Spain)
- Scope: league `segunda1`

- Matches analysed: **333** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_conceded_last_5 | 0.188 | -0.028 | 0.123 |
| away_position_before_match | 0.188 | -0.057 | 0.104 |
| away_team_away_conceded_avg | 0.156 | -0.035 | 0.094 |
| home_team_goals_conceded_last_5 | 0.021 | 0.114 | 0.091 |
| home_team_home_conceded_avg | 0.021 | 0.109 | 0.087 |
| points_difference | 0.219 | -0.137 | 0.075 |
| away_team_wins_last_5 | -0.094 | -0.005 | -0.074 |
| away_team_points_last_5 | -0.114 | 0.020 | -0.072 |
| rest_days_difference | -0.067 | -0.030 | -0.070 |
| home_points_before_match | 0.105 | -0.039 | 0.053 |
| home_position_before_match | -0.044 | 0.124 | 0.048 |
| position_difference | -0.171 | 0.131 | -0.043 |
| away_team_goals_scored_last_5 | -0.051 | 0.002 | -0.037 |
| home_team_wins_last_5 | 0.055 | -0.114 | -0.034 |
| away_rest_days | 0.012 | 0.037 | 0.033 |
| away_team_away_win_rate | -0.076 | 0.041 | -0.030 |
| home_team_home_goals_avg | 0.036 | -0.085 | -0.029 |
| away_team_away_goals_avg | -0.068 | 0.037 | -0.027 |
| home_team_points_last_5 | 0.066 | -0.109 | -0.022 |
| home_team_goals_scored_last_5 | 0.119 | -0.108 | 0.018 |
| home_team_home_win_rate | 0.041 | -0.075 | -0.018 |
| home_rest_days | -0.026 | 0.020 | -0.006 |
| away_points_before_match | -0.039 | 0.051 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 51 | 15 | 13 | 23 | 29.4% | 25.5% | 45.1% |
| -4..-2 | 80 | 35 | 19 | 26 | 43.8% | 23.8% | 32.5% |
| -1..1 | 91 | 35 | 26 | 30 | 38.5% | 28.6% | 33.0% |
| 2..4 | 72 | 35 | 20 | 17 | 48.6% | 27.8% | 23.6% |
| >4 | 39 | 19 | 11 | 9 | 48.7% | 28.2% | 23.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 80 | 38 | 24 | 18 | 47.5% | 30.0% | 22.5% |
| -5..-2 | 54 | 26 | 15 | 13 | 48.1% | 27.8% | 24.1% |
| -1..1 | 60 | 25 | 16 | 19 | 41.7% | 26.7% | 31.7% |
| 2..5 | 61 | 21 | 15 | 25 | 34.4% | 24.6% | 41.0% |
| >=6 | 78 | 29 | 19 | 30 | 37.2% | 24.4% | 38.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 1 | 0 | 0 | 1 | 0.0% | 0.0% | 100.0% |
| -1..0 | 66 | 30 | 18 | 18 | 45.5% | 27.3% | 27.3% |
| 0 | 188 | 79 | 50 | 59 | 42.0% | 26.6% | 31.4% |
| 1..2 | 57 | 21 | 15 | 21 | 36.8% | 26.3% | 36.8% |
| >2 | 3 | 2 | 1 | 0 | 66.7% | 33.3% | 0.0% |
| unknown | 18 | 7 | 5 | 6 | 38.9% | 27.8% | 33.3% |
- *18 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.0%** home win (27/73)
- `>= 0.5` tier: **43.1%** home win (112/260)
- Home-win gap (>= split minus < split): **+6.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 73 | 27 | 18 | 28 | 37.0% |
| high | >= 0.5 | 260 | 112 | 71 | 77 | 43.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.547 | 0.090 | -2.476 | 4.023 |
| position_difference | -0.856 | -0.292 | 1.838 | 2.694 |
| home_points_before_match | 21.770 | 19.921 | 19.457 | 2.313 |
| away_points_before_match | 20.223 | 19.831 | 21.933 | 2.102 |
| home_position_before_match | 9.115 | 9.258 | 10.552 | 1.437 |
| away_position_before_match | 9.971 | 9.551 | 8.714 | 1.257 |
| home_team_goals_scored_last_5 | 5.475 | 5.337 | 4.629 | 0.846 |
| away_team_points_last_5 | 5.532 | 6.011 | 6.371 | 0.839 |
| away_team_goals_conceded_last_5 | 5.568 | 5.303 | 4.733 | 0.835 |
| home_team_points_last_5 | 5.921 | 5.865 | 5.152 | 0.768 |
| home_team_goals_conceded_last_5 | 5.086 | 5.517 | 5.590 | 0.504 |
| away_team_goals_scored_last_5 | 5.237 | 5.629 | 5.495 | 0.392 |
| home_team_wins_last_5 | 2.799 | 2.742 | 2.543 | 0.256 |
| away_team_wins_last_5 | 2.669 | 2.865 | 2.886 | 0.217 |
| home_rest_days | 7.129 | 7.310 | 7.222 | 0.181 |
| away_team_away_conceded_avg | 1.225 | 1.239 | 1.103 | 0.135 |
| away_rest_days | 7.144 | 7.274 | 7.253 | 0.130 |
| home_team_home_conceded_avg | 0.931 | 0.968 | 1.057 | 0.126 |
| away_team_away_goals_avg | 0.929 | 1.027 | 0.997 | 0.098 |
| home_team_home_goals_avg | 1.216 | 1.217 | 1.138 | 0.079 |
| rest_days_difference | -0.015 | 0.036 | -0.030 | 0.066 |
| home_team_home_win_rate | 0.637 | 0.654 | 0.609 | 0.045 |
| away_team_away_win_rate | 0.507 | 0.519 | 0.550 | 0.043 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\segunda1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\segunda1\charts\relationships_home_win_pct_by_position.png)

