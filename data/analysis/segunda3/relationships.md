# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:46:07+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Segunda RFEF - Group 3 (Spain)
- Scope: league `segunda3`

- Matches analysed: **337** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.161 | 0.164 | 0.211 |
| rest_days_difference | -0.133 | -0.101 | -0.154 |
| home_team_home_goals_avg | 0.152 | 0.049 | 0.136 |
| away_team_goals_conceded_last_5 | 0.146 | 0.053 | 0.134 |
| away_team_away_win_rate | -0.112 | -0.086 | -0.131 |
| away_rest_days | 0.050 | 0.077 | 0.081 |
| away_position_before_match | 0.154 | -0.044 | 0.080 |
| home_team_goals_scored_last_5 | 0.111 | -0.002 | 0.076 |
| home_team_home_conceded_avg | 0.018 | 0.091 | 0.067 |
| away_team_away_goals_avg | 0.024 | 0.081 | 0.065 |
| away_team_goals_scored_last_5 | 0.008 | 0.087 | 0.059 |
| home_team_home_win_rate | 0.080 | 0.004 | 0.058 |
| home_team_goals_conceded_last_5 | 0.007 | 0.081 | 0.054 |
| position_difference | -0.166 | 0.106 | -0.051 |
| home_rest_days | -0.062 | -0.007 | -0.048 |
| points_difference | 0.150 | -0.113 | 0.036 |
| home_team_wins_last_5 | 0.072 | -0.028 | 0.033 |
| home_team_points_last_5 | 0.079 | -0.045 | 0.028 |
| home_points_before_match | 0.052 | -0.024 | 0.022 |
| away_team_wins_last_5 | -0.052 | 0.032 | -0.018 |
| away_team_points_last_5 | -0.041 | 0.034 | -0.008 |
| home_position_before_match | -0.082 | 0.104 | 0.006 |
| away_points_before_match | -0.039 | 0.045 | -0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 55 | 19 | 19 | 17 | 34.5% | 34.5% | 30.9% |
| -4..-2 | 66 | 24 | 20 | 22 | 36.4% | 30.3% | 33.3% |
| -1..1 | 115 | 53 | 40 | 22 | 46.1% | 34.8% | 19.1% |
| 2..4 | 65 | 36 | 17 | 12 | 55.4% | 26.2% | 18.5% |
| >4 | 36 | 21 | 10 | 5 | 58.3% | 27.8% | 13.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 70 | 39 | 21 | 10 | 55.7% | 30.0% | 14.3% |
| -5..-2 | 64 | 33 | 18 | 13 | 51.6% | 28.1% | 20.3% |
| -1..1 | 59 | 31 | 19 | 9 | 52.5% | 32.2% | 15.3% |
| 2..5 | 47 | 16 | 16 | 15 | 34.0% | 34.0% | 31.9% |
| >=6 | 97 | 34 | 32 | 31 | 35.1% | 33.0% | 32.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 8 | 4 | 3 | 1 | 50.0% | 37.5% | 12.5% |
| -1..0 | 42 | 18 | 9 | 15 | 42.9% | 21.4% | 35.7% |
| 0 | 212 | 96 | 70 | 46 | 45.3% | 33.0% | 21.7% |
| 1..2 | 46 | 22 | 15 | 9 | 47.8% | 32.6% | 19.6% |
| >2 | 7 | 2 | 2 | 3 | 28.6% | 28.6% | 42.9% |
| unknown | 22 | 11 | 7 | 4 | 50.0% | 31.8% | 18.2% |
- *22 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **42.6%** home win (20/47)
- `>= 0.5` tier: **45.9%** home win (133/290)
- Home-win gap (>= split minus < split): **+3.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 47 | 20 | 18 | 9 | 42.6% |
| high | >= 0.5 | 290 | 133 | 88 | 69 | 45.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 18.732 | 19.925 | 24.218 | 5.486 |
| points_difference | 1.438 | -1.453 | -3.205 | 4.643 |
| position_difference | -0.876 | 1.208 | 2.731 | 3.607 |
| home_points_before_match | 20.170 | 18.472 | 21.013 | 2.541 |
| away_position_before_match | 10.020 | 8.972 | 8.013 | 2.007 |
| home_position_before_match | 9.144 | 10.179 | 10.744 | 1.600 |
| away_team_points_last_5 | 5.529 | 5.972 | 6.449 | 0.919 |
| away_team_goals_scored_last_5 | 5.150 | 4.953 | 5.782 | 0.829 |
| home_team_goals_conceded_last_5 | 4.856 | 5.340 | 5.654 | 0.798 |
| home_team_points_last_5 | 5.693 | 5.406 | 4.987 | 0.706 |
| away_team_goals_conceded_last_5 | 5.222 | 4.604 | 4.859 | 0.618 |
| home_team_goals_scored_last_5 | 5.000 | 4.953 | 4.641 | 0.359 |
| away_team_wins_last_5 | 2.771 | 2.915 | 3.115 | 0.344 |
| home_rest_days | 7.099 | 7.242 | 7.432 | 0.334 |
| away_rest_days | 7.141 | 7.162 | 7.405 | 0.265 |
| home_team_wins_last_5 | 2.869 | 2.651 | 2.679 | 0.218 |
| rest_days_difference | -0.042 | 0.081 | 0.027 | 0.123 |
| home_team_home_conceded_avg | 0.810 | 0.865 | 0.907 | 0.097 |
| away_team_away_goals_avg | 0.827 | 0.822 | 0.918 | 0.097 |
| away_team_away_conceded_avg | 1.249 | 1.218 | 1.279 | 0.061 |
| home_team_home_goals_avg | 1.260 | 1.249 | 1.219 | 0.041 |
| away_team_away_win_rate | 0.432 | 0.446 | 0.459 | 0.027 |
| home_team_home_win_rate | 0.739 | 0.717 | 0.729 | 0.022 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\segunda3\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\segunda3\charts\relationships_home_win_pct_by_position.png)

