# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:02:52+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: K League 1 (South Korea)
- Scope: league `korea1`

- Matches analysed: **377** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_points_before_match | 0.191 | 0.000 | 0.131 |
| away_points_before_match | 0.092 | 0.085 | 0.123 |
| away_team_goals_scored_last_5 | 0.067 | 0.065 | 0.092 |
| away_team_goals_conceded_last_5 | 0.144 | -0.022 | 0.083 |
| home_team_wins_last_5 | 0.106 | -0.011 | 0.065 |
| away_rest_days | 0.076 | 0.016 | 0.064 |
| rest_days_difference | -0.025 | -0.040 | -0.045 |
| home_rest_days | 0.064 | 0.001 | 0.045 |
| home_team_home_win_rate | -0.004 | 0.065 | 0.043 |
| away_team_points_last_5 | 0.017 | 0.043 | 0.042 |
| home_team_goals_conceded_last_5 | -0.033 | 0.083 | 0.036 |
| away_team_away_conceded_avg | 0.116 | -0.065 | 0.034 |
| away_team_away_goals_avg | -0.050 | 0.097 | 0.034 |
| home_team_goals_scored_last_5 | 0.081 | -0.032 | 0.033 |
| home_team_home_conceded_avg | -0.031 | -0.015 | -0.032 |
| away_position_before_match | 0.102 | -0.061 | 0.027 |
| home_team_points_last_5 | 0.092 | -0.056 | 0.024 |
| position_difference | -0.135 | 0.103 | -0.021 |
| away_team_away_win_rate | -0.041 | 0.060 | 0.014 |
| home_team_home_goals_avg | 0.023 | -0.003 | 0.013 |
| away_team_wins_last_5 | -0.012 | 0.024 | 0.009 |
| points_difference | 0.139 | -0.124 | 0.009 |
| home_position_before_match | -0.090 | 0.085 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 59 | 22 | 17 | 20 | 37.3% | 28.8% | 33.9% |
| -4..-2 | 73 | 25 | 24 | 24 | 34.2% | 32.9% | 32.9% |
| -1..1 | 117 | 44 | 27 | 46 | 37.6% | 23.1% | 39.3% |
| 2..4 | 77 | 24 | 29 | 24 | 31.2% | 37.7% | 31.2% |
| >4 | 51 | 22 | 15 | 14 | 43.1% | 29.4% | 27.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 52 | 23 | 15 | 14 | 44.2% | 28.8% | 26.9% |
| -5..-2 | 96 | 42 | 29 | 25 | 43.8% | 30.2% | 26.0% |
| -1..1 | 77 | 25 | 19 | 33 | 32.5% | 24.7% | 42.9% |
| 2..5 | 93 | 30 | 28 | 35 | 32.3% | 30.1% | 37.6% |
| >=6 | 59 | 17 | 21 | 21 | 28.8% | 35.6% | 35.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 22 | 9 | 3 | 10 | 40.9% | 13.6% | 45.5% |
| -1..0 | 100 | 37 | 30 | 33 | 37.0% | 30.0% | 33.0% |
| 0 | 151 | 49 | 45 | 57 | 32.5% | 29.8% | 37.7% |
| 1..2 | 80 | 33 | 24 | 23 | 41.2% | 30.0% | 28.8% |
| >2 | 12 | 5 | 6 | 1 | 41.7% | 50.0% | 8.3% |
| unknown | 12 | 4 | 4 | 4 | 33.3% | 33.3% | 33.3% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **34.8%** home win (23/66)
- `>= 0.5` tier: **36.7%** home win (114/311)
- Home-win gap (>= split minus < split): **+1.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 66 | 23 | 24 | 19 | 34.8% |
| high | >= 0.5 | 311 | 114 | 88 | 109 | 36.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 23.270 | 19.321 | 18.539 | 4.731 |
| points_difference | 1.686 | -0.955 | -1.859 | 3.546 |
| position_difference | -0.774 | 0.455 | 0.695 | 1.469 |
| away_points_before_match | 21.584 | 20.277 | 20.398 | 1.307 |
| home_rest_days | 7.496 | 7.824 | 6.661 | 1.163 |
| home_position_before_match | 6.124 | 7.223 | 6.781 | 1.099 |
| home_team_points_last_5 | 6.547 | 5.670 | 6.023 | 0.878 |
| away_team_points_last_5 | 6.496 | 5.661 | 6.242 | 0.836 |
| away_team_goals_scored_last_5 | 5.949 | 5.134 | 5.695 | 0.815 |
| rest_days_difference | -0.128 | 0.361 | -0.452 | 0.813 |
| away_position_before_match | 6.898 | 6.768 | 6.086 | 0.812 |
| home_team_goals_scored_last_5 | 6.088 | 5.304 | 5.594 | 0.784 |
| away_rest_days | 7.624 | 7.463 | 7.113 | 0.511 |
| away_team_goals_conceded_last_5 | 5.839 | 5.652 | 5.344 | 0.496 |
| home_team_goals_conceded_last_5 | 5.540 | 5.661 | 5.883 | 0.343 |
| home_team_wins_last_5 | 3.029 | 2.723 | 2.914 | 0.306 |
| away_team_wins_last_5 | 2.993 | 2.750 | 2.992 | 0.243 |
| away_team_away_goals_avg | 1.035 | 1.062 | 1.171 | 0.136 |
| away_team_away_conceded_avg | 1.107 | 1.125 | 0.997 | 0.128 |
| home_team_home_goals_avg | 1.109 | 1.039 | 1.139 | 0.100 |
| away_team_away_win_rate | 0.617 | 0.585 | 0.652 | 0.067 |
| home_team_home_win_rate | 0.592 | 0.601 | 0.643 | 0.051 |
| home_team_home_conceded_avg | 1.086 | 1.108 | 1.089 | 0.022 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\korea1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\korea1\charts\relationships_home_win_pct_by_position.png)

