# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:44:55+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premier League (Azerbaijan)
- Scope: league `azer`

- Matches analysed: **200** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_wins_last_5 | 0.277 | -0.025 | 0.209 |
| home_team_points_last_5 | 0.279 | -0.053 | 0.191 |
| home_team_goals_scored_last_5 | 0.262 | -0.064 | 0.169 |
| home_points_before_match | 0.239 | -0.073 | 0.143 |
| home_position_before_match | -0.295 | 0.155 | -0.129 |
| away_points_before_match | -0.046 | 0.228 | 0.127 |
| home_team_home_win_rate | 0.191 | -0.042 | 0.126 |
| away_team_away_goals_avg | -0.051 | 0.231 | 0.125 |
| home_rest_days | 0.043 | 0.110 | 0.115 |
| away_rest_days | 0.086 | 0.045 | 0.103 |
| home_team_home_goals_avg | 0.134 | -0.029 | 0.089 |
| away_team_points_last_5 | -0.142 | 0.281 | 0.086 |
| away_team_goals_scored_last_5 | -0.098 | 0.222 | 0.080 |
| away_position_before_match | 0.190 | -0.314 | -0.071 |
| away_team_wins_last_5 | -0.149 | 0.263 | 0.068 |
| home_team_home_conceded_avg | -0.182 | 0.114 | -0.067 |
| away_team_away_win_rate | -0.160 | 0.249 | 0.049 |
| rest_days_difference | -0.138 | 0.224 | 0.049 |
| away_team_away_conceded_avg | 0.251 | -0.234 | 0.037 |
| position_difference | -0.331 | 0.325 | -0.036 |
| away_team_goals_conceded_last_5 | 0.149 | -0.195 | -0.019 |
| points_difference | 0.304 | -0.328 | 0.013 |
| home_team_goals_conceded_last_5 | -0.091 | 0.115 | 0.008 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 34 | 7 | 7 | 20 | 20.6% | 20.6% | 58.8% |
| -4..-2 | 49 | 10 | 17 | 22 | 20.4% | 34.7% | 44.9% |
| -1..1 | 41 | 14 | 9 | 18 | 34.1% | 22.0% | 43.9% |
| 2..4 | 38 | 20 | 8 | 10 | 52.6% | 21.1% | 26.3% |
| >4 | 38 | 24 | 8 | 6 | 63.2% | 21.1% | 15.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 31 | 21 | 5 | 5 | 67.7% | 16.1% | 16.1% |
| -5..-2 | 49 | 26 | 12 | 11 | 53.1% | 24.5% | 22.4% |
| -1..1 | 40 | 15 | 12 | 13 | 37.5% | 30.0% | 32.5% |
| 2..5 | 53 | 12 | 13 | 28 | 22.6% | 24.5% | 52.8% |
| >=6 | 27 | 1 | 7 | 19 | 3.7% | 25.9% | 70.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 31 | 16 | 8 | 7 | 51.6% | 25.8% | 22.6% |
| -1..0 | 42 | 24 | 6 | 12 | 57.1% | 14.3% | 28.6% |
| 0 | 39 | 11 | 12 | 16 | 28.2% | 30.8% | 41.0% |
| 1..2 | 72 | 20 | 19 | 33 | 27.8% | 26.4% | 45.8% |
| >2 | 8 | 2 | 1 | 5 | 25.0% | 12.5% | 62.5% |
| unknown | 8 | 2 | 3 | 3 | 25.0% | 37.5% | 37.5% |
- *8 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **30.8%** home win (41/133)
- `>= 0.5` tier: **50.7%** home win (34/67)
- Home-win gap (>= split minus < split): **+19.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 133 | 41 | 33 | 59 | 30.8% |
| high | >= 0.5 | 67 | 34 | 16 | 17 | 50.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 7.307 | -1.592 | -6.697 | 14.004 |
| home_points_before_match | 26.640 | 19.939 | 18.605 | 8.035 |
| away_points_before_match | 19.333 | 21.531 | 25.303 | 5.969 |
| position_difference | -2.733 | 0.653 | 2.289 | 5.023 |
| away_position_before_match | 8.240 | 5.959 | 5.526 | 2.714 |
| away_team_goals_conceded_last_5 | 7.280 | 4.898 | 5.171 | 2.382 |
| home_position_before_match | 5.507 | 6.612 | 7.816 | 2.309 |
| away_team_points_last_5 | 4.920 | 6.673 | 7.079 | 2.159 |
| home_team_points_last_5 | 7.413 | 6.041 | 5.329 | 2.084 |
| home_team_goals_scored_last_5 | 7.040 | 5.082 | 5.000 | 2.040 |
| home_rest_days | 8.095 | 9.674 | 8.622 | 1.579 |
| away_rest_days | 8.452 | 9.565 | 8.135 | 1.430 |
| away_team_goals_scored_last_5 | 5.067 | 5.959 | 6.395 | 1.328 |
| home_team_goals_conceded_last_5 | 5.480 | 4.980 | 6.303 | 1.323 |
| rest_days_difference | -0.342 | 0.109 | 0.452 | 0.795 |
| away_team_wins_last_5 | 1.253 | 1.857 | 1.987 | 0.734 |
| home_team_wins_last_5 | 2.040 | 1.571 | 1.434 | 0.606 |
| away_team_away_conceded_avg | 1.400 | 0.972 | 0.878 | 0.523 |
| home_team_home_conceded_avg | 1.118 | 1.097 | 1.335 | 0.238 |
| home_team_home_goals_avg | 1.270 | 1.045 | 1.034 | 0.236 |
| away_team_away_goals_avg | 1.088 | 1.219 | 1.312 | 0.223 |
| away_team_away_win_rate | 0.309 | 0.435 | 0.451 | 0.142 |
| home_team_home_win_rate | 0.372 | 0.289 | 0.253 | 0.119 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\azer\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\azer\charts\relationships_home_win_pct_by_position.png)

