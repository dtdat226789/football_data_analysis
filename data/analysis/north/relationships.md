# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:04:00+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: National League North (England)
- Scope: league `north`

- Matches analysed: **668** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.183 | -0.009 | 0.141 |
| home_team_points_last_5 | 0.189 | -0.040 | 0.123 |
| home_team_home_goals_avg | 0.105 | 0.028 | 0.103 |
| home_team_wins_last_5 | 0.143 | -0.036 | 0.089 |
| home_team_home_win_rate | 0.088 | 0.015 | 0.081 |
| home_points_before_match | 0.103 | -0.003 | 0.080 |
| home_position_before_match | -0.137 | 0.053 | -0.073 |
| position_difference | -0.199 | 0.134 | -0.066 |
| points_difference | 0.212 | -0.153 | 0.062 |
| away_team_points_last_5 | -0.023 | 0.103 | 0.054 |
| away_team_wins_last_5 | -0.003 | 0.080 | 0.053 |
| away_team_away_goals_avg | -0.027 | 0.105 | 0.053 |
| away_team_away_win_rate | -0.002 | 0.072 | 0.049 |
| home_rest_days | 0.010 | 0.058 | 0.049 |
| away_team_goals_scored_last_5 | -0.037 | 0.106 | 0.045 |
| away_points_before_match | -0.025 | 0.089 | 0.043 |
| away_team_away_conceded_avg | 0.080 | -0.055 | 0.026 |
| rest_days_difference | -0.008 | 0.046 | 0.026 |
| away_rest_days | 0.016 | 0.018 | 0.026 |
| away_position_before_match | 0.130 | -0.128 | 0.014 |
| home_team_goals_conceded_last_5 | -0.051 | 0.051 | -0.005 |
| home_team_home_conceded_avg | -0.029 | 0.030 | -0.002 |
| away_team_goals_conceded_last_5 | 0.042 | -0.046 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 106 | 42 | 18 | 46 | 39.6% | 17.0% | 43.4% |
| -4..-2 | 136 | 48 | 30 | 58 | 35.3% | 22.1% | 42.6% |
| -1..1 | 197 | 90 | 42 | 65 | 45.7% | 21.3% | 33.0% |
| 2..4 | 131 | 57 | 36 | 38 | 43.5% | 27.5% | 29.0% |
| >4 | 98 | 55 | 21 | 22 | 56.1% | 21.4% | 22.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 190 | 96 | 46 | 48 | 50.5% | 24.2% | 25.3% |
| -5..-2 | 106 | 54 | 20 | 32 | 50.9% | 18.9% | 30.2% |
| -1..1 | 76 | 35 | 20 | 21 | 46.1% | 26.3% | 27.6% |
| 2..5 | 106 | 43 | 20 | 43 | 40.6% | 18.9% | 40.6% |
| >=6 | 190 | 64 | 41 | 85 | 33.7% | 21.6% | 44.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 75 | 29 | 21 | 25 | 38.7% | 28.0% | 33.3% |
| -1..0 | 4 | 0 | 2 | 2 | 0.0% | 50.0% | 50.0% |
| 0 | 490 | 220 | 100 | 170 | 44.9% | 20.4% | 34.7% |
| 1..2 | 8 | 3 | 2 | 3 | 37.5% | 25.0% | 37.5% |
| >2 | 67 | 28 | 17 | 22 | 41.8% | 25.4% | 32.8% |
| unknown | 24 | 12 | 5 | 7 | 50.0% | 20.8% | 29.2% |
- *24 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **48.0%** home win (59/123)
- `>= 0.5` tier: **42.8%** home win (233/545)
- Home-win gap (>= split minus < split): **-5.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 123 | 59 | 24 | 40 | 48.0% |
| high | >= 0.5 | 545 | 233 | 123 | 189 | 42.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.205 | -0.122 | -3.362 | 5.568 |
| away_points_before_match | 26.291 | 26.272 | 30.249 | 3.977 |
| position_difference | -1.336 | -0.163 | 2.581 | 3.916 |
| home_points_before_match | 28.497 | 26.150 | 26.886 | 2.347 |
| home_position_before_match | 11.199 | 12.456 | 13.214 | 2.015 |
| away_position_before_match | 12.534 | 12.619 | 10.633 | 1.986 |
| home_team_points_last_5 | 6.599 | 6.190 | 5.616 | 0.984 |
| home_team_goals_scored_last_5 | 7.072 | 6.415 | 6.284 | 0.788 |
| away_team_points_last_5 | 6.116 | 5.993 | 6.681 | 0.688 |
| away_team_goals_scored_last_5 | 6.568 | 6.442 | 7.105 | 0.663 |
| home_team_goals_conceded_last_5 | 6.469 | 6.660 | 7.127 | 0.657 |
| away_team_goals_conceded_last_5 | 6.606 | 6.803 | 6.384 | 0.418 |
| away_rest_days | 5.596 | 5.754 | 5.360 | 0.393 |
| away_team_wins_last_5 | 2.712 | 2.605 | 2.908 | 0.303 |
| home_team_wins_last_5 | 2.832 | 2.721 | 2.559 | 0.273 |
| home_rest_days | 5.511 | 5.613 | 5.365 | 0.248 |
| rest_days_difference | -0.086 | -0.141 | 0.005 | 0.145 |
| away_team_away_goals_avg | 1.260 | 1.228 | 1.351 | 0.123 |
| away_team_away_conceded_avg | 1.492 | 1.469 | 1.407 | 0.086 |
| home_team_home_conceded_avg | 1.242 | 1.301 | 1.316 | 0.074 |
| home_team_home_goals_avg | 1.469 | 1.478 | 1.449 | 0.028 |
| away_team_away_win_rate | 0.511 | 0.520 | 0.539 | 0.028 |
| home_team_home_win_rate | 0.622 | 0.634 | 0.607 | 0.027 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\north\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\north\charts\relationships_home_win_pct_by_position.png)

