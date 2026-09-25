# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:58:43+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Ligue 1 (France)
- Scope: league `france1`

- Matches analysed: **355** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_conceded_last_5 | -0.021 | -0.134 | -0.106 |
| away_team_points_last_5 | -0.026 | 0.146 | 0.081 |
| home_team_home_win_rate | 0.068 | 0.039 | 0.074 |
| away_position_before_match | 0.071 | -0.182 | -0.074 |
| home_rest_days | 0.026 | 0.067 | 0.066 |
| home_position_before_match | -0.179 | 0.095 | -0.062 |
| home_team_home_goals_avg | 0.081 | 0.003 | 0.059 |
| home_team_home_conceded_avg | -0.060 | -0.011 | -0.050 |
| rest_days_difference | 0.036 | 0.036 | 0.050 |
| away_rest_days | 0.013 | 0.056 | 0.048 |
| away_team_away_win_rate | -0.068 | 0.137 | 0.045 |
| away_points_before_match | -0.083 | 0.145 | 0.040 |
| away_team_wins_last_5 | -0.054 | 0.113 | 0.039 |
| home_team_points_last_5 | 0.111 | -0.061 | 0.036 |
| home_points_before_match | 0.049 | -0.003 | 0.032 |
| home_team_goals_conceded_last_5 | -0.083 | 0.046 | -0.028 |
| home_team_goals_scored_last_5 | 0.079 | -0.049 | 0.023 |
| home_team_wins_last_5 | 0.074 | -0.053 | 0.016 |
| away_team_away_conceded_avg | 0.032 | -0.014 | 0.013 |
| points_difference | 0.175 | -0.196 | -0.010 |
| position_difference | -0.185 | 0.204 | 0.008 |
| away_team_goals_scored_last_5 | -0.075 | 0.072 | -0.004 |
| away_team_away_goals_avg | -0.048 | 0.054 | 0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 54 | 23 | 8 | 23 | 42.6% | 14.8% | 42.6% |
| -4..-2 | 80 | 36 | 23 | 21 | 45.0% | 28.8% | 26.2% |
| -1..1 | 108 | 35 | 33 | 40 | 32.4% | 30.6% | 37.0% |
| 2..4 | 62 | 32 | 14 | 16 | 51.6% | 22.6% | 25.8% |
| >4 | 51 | 35 | 11 | 5 | 68.6% | 21.6% | 9.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 79 | 48 | 21 | 10 | 60.8% | 26.6% | 12.7% |
| -5..-2 | 59 | 26 | 17 | 16 | 44.1% | 28.8% | 27.1% |
| -1..1 | 69 | 33 | 17 | 19 | 47.8% | 24.6% | 27.5% |
| 2..5 | 62 | 26 | 15 | 21 | 41.9% | 24.2% | 33.9% |
| >=6 | 86 | 28 | 19 | 39 | 32.6% | 22.1% | 45.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 29 | 9 | 11 | 9 | 31.0% | 37.9% | 31.0% |
| -1..0 | 79 | 36 | 14 | 29 | 45.6% | 17.7% | 36.7% |
| 0 | 118 | 59 | 33 | 26 | 50.0% | 28.0% | 22.0% |
| 1..2 | 100 | 46 | 26 | 28 | 46.0% | 26.0% | 28.0% |
| >2 | 9 | 4 | 0 | 5 | 44.4% | 0.0% | 55.6% |
| unknown | 20 | 7 | 5 | 8 | 35.0% | 25.0% | 40.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.2%** home win (29/78)
- `>= 0.5` tier: **47.7%** home win (132/277)
- Home-win gap (>= split minus < split): **+10.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 78 | 29 | 19 | 30 | 37.2% |
| high | >= 0.5 | 277 | 132 | 70 | 75 | 47.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.826 | 0.000 | -4.771 | 7.598 |
| away_points_before_match | 18.553 | 19.022 | 23.886 | 5.333 |
| position_difference | -1.416 | 0.022 | 2.990 | 4.407 |
| away_position_before_match | 10.000 | 10.888 | 7.905 | 2.983 |
| home_points_before_match | 21.379 | 19.022 | 19.114 | 2.356 |
| home_position_before_match | 8.584 | 10.910 | 10.895 | 2.326 |
| away_team_points_last_5 | 5.839 | 4.910 | 6.790 | 1.880 |
| away_team_goals_conceded_last_5 | 5.901 | 6.798 | 5.086 | 1.712 |
| home_team_points_last_5 | 6.311 | 5.000 | 5.267 | 1.311 |
| away_team_goals_scored_last_5 | 5.907 | 5.506 | 6.581 | 1.075 |
| home_team_goals_conceded_last_5 | 5.522 | 6.483 | 6.076 | 0.961 |
| home_team_goals_scored_last_5 | 6.224 | 5.438 | 5.486 | 0.785 |
| away_team_wins_last_5 | 2.609 | 2.393 | 3.000 | 0.607 |
| home_team_wins_last_5 | 2.795 | 2.393 | 2.448 | 0.402 |
| away_team_away_conceded_avg | 1.515 | 1.633 | 1.355 | 0.277 |
| rest_days_difference | 0.117 | -0.107 | 0.134 | 0.241 |
| away_rest_days | 7.994 | 8.226 | 8.134 | 0.233 |
| home_team_home_conceded_avg | 0.978 | 1.154 | 1.035 | 0.176 |
| home_team_home_goals_avg | 1.563 | 1.476 | 1.407 | 0.156 |
| home_rest_days | 8.143 | 8.119 | 8.268 | 0.149 |
| away_team_away_goals_avg | 1.035 | 0.995 | 1.104 | 0.109 |
| away_team_away_win_rate | 0.426 | 0.401 | 0.506 | 0.105 |
| home_team_home_win_rate | 0.668 | 0.626 | 0.624 | 0.043 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\france1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\france1\charts\relationships_home_win_pct_by_position.png)

