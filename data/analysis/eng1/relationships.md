# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:48:53+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: League One (England)
- Scope: league `eng1`

- Matches analysed: **557** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.144 | -0.011 | 0.104 |
| home_points_before_match | 0.080 | 0.052 | 0.097 |
| home_position_before_match | -0.186 | 0.079 | -0.091 |
| home_team_home_goals_avg | 0.104 | -0.003 | 0.079 |
| away_points_before_match | -0.037 | 0.153 | 0.074 |
| home_team_points_last_5 | 0.127 | -0.049 | 0.066 |
| away_team_away_win_rate | 0.017 | 0.075 | 0.063 |
| home_team_wins_last_5 | 0.120 | -0.061 | 0.052 |
| away_team_away_goals_avg | -0.008 | 0.085 | 0.051 |
| away_rest_days | 0.021 | 0.048 | 0.048 |
| rest_days_difference | -0.027 | -0.040 | -0.048 |
| position_difference | -0.158 | 0.119 | -0.043 |
| points_difference | 0.194 | -0.171 | 0.037 |
| away_team_goals_conceded_last_5 | 0.026 | 0.022 | 0.035 |
| home_team_home_conceded_avg | -0.003 | 0.049 | 0.031 |
| away_position_before_match | 0.037 | -0.087 | -0.030 |
| away_team_away_conceded_avg | -0.022 | -0.009 | -0.024 |
| home_team_goals_conceded_last_5 | -0.085 | 0.068 | -0.021 |
| home_team_home_win_rate | 0.061 | -0.041 | 0.020 |
| away_team_goals_scored_last_5 | -0.059 | 0.096 | 0.018 |
| home_rest_days | -0.001 | 0.015 | 0.009 |
| away_team_points_last_5 | -0.089 | 0.114 | 0.007 |
| away_team_wins_last_5 | -0.081 | 0.099 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 101 | 33 | 27 | 41 | 32.7% | 26.7% | 40.6% |
| -4..-2 | 125 | 47 | 36 | 42 | 37.6% | 28.8% | 33.6% |
| -1..1 | 147 | 77 | 33 | 37 | 52.4% | 22.4% | 25.2% |
| 2..4 | 105 | 52 | 31 | 22 | 49.5% | 29.5% | 21.0% |
| >4 | 79 | 48 | 12 | 19 | 60.8% | 15.2% | 24.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 159 | 96 | 29 | 34 | 60.4% | 18.2% | 21.4% |
| -5..-2 | 63 | 24 | 22 | 17 | 38.1% | 34.9% | 27.0% |
| -1..1 | 63 | 32 | 14 | 17 | 50.8% | 22.2% | 27.0% |
| 2..5 | 94 | 40 | 27 | 27 | 42.6% | 28.7% | 28.7% |
| >=6 | 178 | 65 | 47 | 66 | 36.5% | 26.4% | 37.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 62 | 23 | 21 | 18 | 37.1% | 33.9% | 29.0% |
| -1..0 | 13 | 4 | 4 | 5 | 30.8% | 30.8% | 38.5% |
| 0 | 396 | 183 | 97 | 116 | 46.2% | 24.5% | 29.3% |
| 1..2 | 22 | 13 | 6 | 3 | 59.1% | 27.3% | 13.6% |
| >2 | 52 | 24 | 11 | 17 | 46.2% | 21.2% | 32.7% |
| unknown | 12 | 10 | 0 | 2 | 83.3% | 0.0% | 16.7% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **42.5%** home win (122/287)
- `>= 0.5` tier: **50.0%** home win (135/270)
- Home-win gap (>= split minus < split): **+7.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 287 | 122 | 62 | 103 | 42.5% |
| high | >= 0.5 | 270 | 135 | 77 | 58 | 50.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.720 | -2.432 | -3.975 | 6.695 |
| away_points_before_match | 28.887 | 34.727 | 33.708 | 5.839 |
| position_difference | -1.529 | 1.626 | 2.870 | 4.399 |
| home_position_before_match | 11.323 | 13.173 | 14.509 | 3.186 |
| home_points_before_match | 31.607 | 32.295 | 29.733 | 2.562 |
| away_position_before_match | 12.852 | 11.547 | 11.640 | 1.305 |
| away_team_points_last_5 | 6.070 | 7.288 | 6.944 | 1.218 |
| home_team_points_last_5 | 6.607 | 6.410 | 5.540 | 1.067 |
| away_team_goals_scored_last_5 | 5.860 | 6.777 | 6.342 | 0.917 |
| home_team_goals_scored_last_5 | 6.210 | 5.964 | 5.491 | 0.719 |
| home_team_goals_conceded_last_5 | 5.848 | 6.453 | 6.553 | 0.705 |
| home_rest_days | 6.142 | 5.662 | 6.327 | 0.665 |
| rest_days_difference | 0.028 | -0.259 | 0.189 | 0.448 |
| home_team_wins_last_5 | 1.813 | 1.741 | 1.422 | 0.391 |
| away_team_wins_last_5 | 1.654 | 2.036 | 1.919 | 0.382 |
| away_team_goals_conceded_last_5 | 6.051 | 5.892 | 5.807 | 0.243 |
| away_rest_days | 6.113 | 5.921 | 6.138 | 0.218 |
| home_team_home_goals_avg | 1.438 | 1.470 | 1.325 | 0.144 |
| away_team_away_goals_avg | 0.976 | 1.054 | 1.023 | 0.078 |
| home_team_home_win_rate | 0.482 | 0.509 | 0.434 | 0.074 |
| home_team_home_conceded_avg | 0.981 | 1.041 | 1.023 | 0.060 |
| away_team_away_conceded_avg | 1.410 | 1.409 | 1.422 | 0.013 |
| away_team_away_win_rate | 0.268 | 0.279 | 0.272 | 0.011 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\eng1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\eng1\charts\relationships_home_win_pct_by_position.png)

