# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:49:37+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Veikkausliiga (Finland)
- Scope: league `finland1`

- Matches analysed: **132** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_rest_days | 0.015 | 0.209 | 0.156 |
| home_points_before_match | 0.248 | -0.064 | 0.152 |
| rest_days_difference | 0.047 | 0.090 | 0.100 |
| away_rest_days | -0.028 | 0.163 | 0.091 |
| away_team_away_goals_avg | -0.029 | -0.096 | -0.088 |
| away_team_away_conceded_avg | 0.090 | -0.233 | -0.086 |
| points_difference | 0.354 | -0.287 | 0.085 |
| away_points_before_match | -0.062 | 0.183 | 0.074 |
| home_team_home_conceded_avg | -0.194 | 0.125 | -0.069 |
| away_team_points_last_5 | -0.123 | 0.212 | 0.046 |
| home_team_goals_conceded_last_5 | -0.109 | 0.074 | -0.036 |
| away_team_goals_scored_last_5 | -0.108 | 0.179 | 0.035 |
| away_team_wins_last_5 | -0.149 | 0.215 | 0.028 |
| home_team_goals_scored_last_5 | 0.129 | -0.127 | 0.016 |
| home_team_home_win_rate | 0.160 | -0.211 | -0.016 |
| home_team_points_last_5 | 0.147 | -0.149 | 0.016 |
| home_team_home_goals_avg | 0.109 | -0.150 | -0.015 |
| position_difference | -0.290 | 0.322 | -0.012 |
| home_position_before_match | -0.220 | 0.242 | -0.011 |
| home_team_wins_last_5 | 0.138 | -0.149 | 0.009 |
| away_position_before_match | 0.187 | -0.210 | 0.006 |
| away_team_away_win_rate | 0.010 | -0.016 | -0.003 |
| away_team_goals_conceded_last_5 | 0.127 | -0.152 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 26 | 6 | 5 | 15 | 23.1% | 19.2% | 57.7% |
| -4..-2 | 23 | 8 | 4 | 11 | 34.8% | 17.4% | 47.8% |
| -1..1 | 31 | 15 | 6 | 10 | 48.4% | 19.4% | 32.3% |
| 2..4 | 30 | 14 | 9 | 7 | 46.7% | 30.0% | 23.3% |
| >4 | 22 | 13 | 5 | 4 | 59.1% | 22.7% | 18.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 17 | 11 | 3 | 3 | 64.7% | 17.6% | 17.6% |
| -5..-2 | 39 | 21 | 7 | 11 | 53.8% | 17.9% | 28.2% |
| -1..1 | 22 | 12 | 3 | 7 | 54.5% | 13.6% | 31.8% |
| 2..5 | 34 | 9 | 11 | 14 | 26.5% | 32.4% | 41.2% |
| >=6 | 20 | 3 | 5 | 12 | 15.0% | 25.0% | 60.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 11 | 3 | 3 | 5 | 27.3% | 27.3% | 45.5% |
| -1..0 | 26 | 11 | 8 | 7 | 42.3% | 30.8% | 26.9% |
| 0 | 45 | 26 | 5 | 14 | 57.8% | 11.1% | 31.1% |
| 1..2 | 33 | 9 | 8 | 16 | 27.3% | 24.2% | 48.5% |
| >2 | 11 | 4 | 4 | 3 | 36.4% | 36.4% | 27.3% |
| unknown | 6 | 3 | 1 | 2 | 50.0% | 16.7% | 33.3% |
- *6 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.3%** home win (26/78)
- `>= 0.5` tier: **55.6%** home win (30/54)
- Home-win gap (>= split minus < split): **+22.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 78 | 26 | 17 | 35 | 33.3% |
| high | >= 0.5 | 54 | 30 | 12 | 12 | 55.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.839 | -1.655 | -4.489 | 8.329 |
| home_points_before_match | 16.429 | 14.138 | 12.191 | 4.237 |
| away_points_before_match | 12.589 | 15.793 | 16.681 | 4.092 |
| position_difference | -1.911 | 1.138 | 1.787 | 3.698 |
| away_team_points_last_5 | 5.179 | 5.862 | 7.234 | 2.055 |
| home_position_before_match | 5.571 | 6.897 | 7.617 | 2.046 |
| away_position_before_match | 7.482 | 5.759 | 5.830 | 1.724 |
| away_team_goals_scored_last_5 | 6.304 | 6.897 | 8.021 | 1.718 |
| home_team_points_last_5 | 6.286 | 6.517 | 4.979 | 1.539 |
| home_team_goals_conceded_last_5 | 6.071 | 7.552 | 7.234 | 1.480 |
| away_team_goals_conceded_last_5 | 7.304 | 7.552 | 6.170 | 1.382 |
| home_team_goals_scored_last_5 | 7.071 | 7.241 | 5.979 | 1.263 |
| away_team_wins_last_5 | 1.393 | 1.621 | 2.085 | 0.692 |
| home_team_wins_last_5 | 1.714 | 1.862 | 1.319 | 0.543 |
| away_rest_days | 6.906 | 6.643 | 7.156 | 0.513 |
| home_rest_days | 7.226 | 6.821 | 7.289 | 0.467 |
| away_team_away_conceded_avg | 1.662 | 1.362 | 1.280 | 0.383 |
| home_team_home_conceded_avg | 1.202 | 1.520 | 1.577 | 0.375 |
| home_team_home_goals_avg | 1.508 | 1.400 | 1.260 | 0.248 |
| away_team_away_goals_avg | 1.551 | 1.304 | 1.385 | 0.247 |
| rest_days_difference | 0.321 | 0.179 | 0.133 | 0.187 |
| home_team_home_win_rate | 0.454 | 0.364 | 0.309 | 0.145 |
| away_team_away_win_rate | 0.335 | 0.345 | 0.331 | 0.014 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\finland1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\finland1\charts\relationships_home_win_pct_by_position.png)

