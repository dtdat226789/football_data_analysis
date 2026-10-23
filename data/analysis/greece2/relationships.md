# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:52:17+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super League 2 (Greece)
- Scope: league `greece2`

- Matches analysed: **265** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_conceded_last_5 | 0.249 | -0.112 | 0.131 |
| away_position_before_match | 0.330 | -0.237 | 0.110 |
| away_team_away_conceded_avg | 0.240 | -0.136 | 0.106 |
| away_team_away_win_rate | -0.269 | 0.182 | -0.099 |
| away_points_before_match | -0.206 | 0.108 | -0.097 |
| away_team_points_last_5 | -0.284 | 0.203 | -0.096 |
| position_difference | -0.445 | 0.398 | -0.096 |
| away_team_away_goals_avg | -0.272 | 0.192 | -0.094 |
| away_team_wins_last_5 | -0.288 | 0.217 | -0.090 |
| away_rest_days | -0.032 | -0.088 | -0.088 |
| home_team_home_conceded_avg | -0.171 | 0.096 | -0.076 |
| home_rest_days | -0.024 | -0.068 | -0.067 |
| rest_days_difference | 0.025 | 0.059 | 0.062 |
| points_difference | 0.382 | -0.376 | 0.058 |
| home_team_home_win_rate | 0.208 | -0.181 | 0.048 |
| home_points_before_match | 0.124 | -0.217 | -0.047 |
| home_team_goals_scored_last_5 | 0.199 | -0.182 | 0.039 |
| home_team_goals_conceded_last_5 | -0.183 | 0.198 | -0.015 |
| home_team_points_last_5 | 0.193 | -0.210 | 0.015 |
| away_team_goals_scored_last_5 | -0.205 | 0.267 | 0.014 |
| home_position_before_match | -0.231 | 0.263 | -0.010 |
| home_team_wins_last_5 | 0.171 | -0.218 | -0.009 |
| home_team_home_goals_avg | 0.182 | -0.208 | 0.008 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 53 | 7 | 9 | 37 | 13.2% | 17.0% | 69.8% |
| -4..-2 | 52 | 17 | 13 | 22 | 32.7% | 25.0% | 42.3% |
| -1..1 | 68 | 29 | 24 | 15 | 42.6% | 35.3% | 22.1% |
| 2..4 | 36 | 21 | 7 | 8 | 58.3% | 19.4% | 22.2% |
| >4 | 56 | 43 | 8 | 5 | 76.8% | 14.3% | 8.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 61 | 48 | 10 | 3 | 78.7% | 16.4% | 4.9% |
| -5..-2 | 42 | 22 | 13 | 7 | 52.4% | 31.0% | 16.7% |
| -1..1 | 43 | 19 | 14 | 10 | 44.2% | 32.6% | 23.3% |
| 2..5 | 55 | 20 | 15 | 20 | 36.4% | 27.3% | 36.4% |
| >=6 | 64 | 8 | 9 | 47 | 12.5% | 14.1% | 73.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 5 | 2 | 2 | 1 | 40.0% | 40.0% | 20.0% |
| -1..0 | 39 | 14 | 9 | 16 | 35.9% | 23.1% | 41.0% |
| 0 | 167 | 80 | 35 | 52 | 47.9% | 21.0% | 31.1% |
| 1..2 | 40 | 14 | 10 | 16 | 35.0% | 25.0% | 40.0% |
| >2 | 4 | 2 | 1 | 1 | 50.0% | 25.0% | 25.0% |
| unknown | 10 | 5 | 4 | 1 | 50.0% | 40.0% | 10.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.7%** home win (65/168)
- `>= 0.5` tier: **53.6%** home win (52/97)
- Home-win gap (>= split minus < split): **+14.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 168 | 65 | 38 | 65 | 38.7% |
| high | >= 0.5 | 97 | 52 | 23 | 22 | 53.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 5.624 | 0.443 | -8.264 | 13.888 |
| position_difference | -3.547 | -0.131 | 5.563 | 9.110 |
| home_points_before_match | 20.316 | 17.852 | 11.851 | 8.466 |
| away_points_before_match | 14.692 | 17.410 | 20.115 | 5.423 |
| away_position_before_match | 12.821 | 10.082 | 8.092 | 4.729 |
| home_position_before_match | 9.274 | 9.951 | 13.655 | 4.382 |
| away_team_points_last_5 | 4.726 | 6.787 | 7.724 | 2.998 |
| home_team_points_last_5 | 7.274 | 6.328 | 4.471 | 2.802 |
| away_team_goals_scored_last_5 | 3.991 | 5.492 | 6.264 | 2.273 |
| home_team_goals_conceded_last_5 | 4.239 | 4.803 | 6.322 | 2.083 |
| home_team_goals_scored_last_5 | 5.735 | 5.016 | 3.736 | 1.999 |
| away_team_goals_conceded_last_5 | 5.726 | 4.426 | 4.103 | 1.623 |
| home_rest_days | 8.223 | 9.053 | 7.779 | 1.274 |
| away_rest_days | 8.214 | 8.930 | 7.837 | 1.093 |
| away_team_wins_last_5 | 1.222 | 1.918 | 2.230 | 1.008 |
| home_team_wins_last_5 | 2.051 | 1.852 | 1.149 | 0.902 |
| away_team_away_goals_avg | 0.683 | 1.028 | 1.123 | 0.440 |
| home_team_home_goals_avg | 1.333 | 1.295 | 0.894 | 0.439 |
| away_team_away_conceded_avg | 1.395 | 1.242 | 0.989 | 0.406 |
| home_team_home_conceded_avg | 0.832 | 0.911 | 1.053 | 0.221 |
| away_team_away_win_rate | 0.227 | 0.317 | 0.414 | 0.187 |
| rest_days_difference | 0.009 | 0.123 | -0.058 | 0.181 |
| home_team_home_win_rate | 0.439 | 0.409 | 0.282 | 0.157 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\greece2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\greece2\charts\relationships_home_win_pct_by_position.png)

