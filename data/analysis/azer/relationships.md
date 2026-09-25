# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:55:10+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premier League (Azerbaijan)
- Scope: league `azer`

- Matches analysed: **234** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_points_last_5 | 0.253 | -0.023 | 0.192 |
| home_team_goals_scored_last_5 | 0.242 | -0.033 | 0.176 |
| home_points_before_match | 0.190 | -0.031 | 0.134 |
| home_team_home_goals_avg | 0.184 | -0.028 | 0.132 |
| home_team_wins_last_5 | 0.197 | -0.043 | 0.131 |
| home_position_before_match | -0.308 | 0.175 | -0.128 |
| home_team_home_win_rate | 0.185 | -0.041 | 0.123 |
| away_points_before_match | -0.059 | 0.234 | 0.119 |
| away_team_wins_last_5 | -0.104 | 0.283 | 0.117 |
| away_team_points_last_5 | -0.134 | 0.291 | 0.098 |
| away_team_away_goals_avg | -0.090 | 0.239 | 0.097 |
| away_team_away_win_rate | -0.135 | 0.280 | 0.090 |
| away_team_goals_scored_last_5 | -0.112 | 0.250 | 0.087 |
| home_team_home_conceded_avg | -0.207 | 0.117 | -0.087 |
| away_rest_days | 0.060 | 0.049 | 0.084 |
| home_rest_days | 0.012 | 0.097 | 0.080 |
| position_difference | -0.328 | 0.304 | -0.052 |
| away_position_before_match | 0.169 | -0.262 | -0.049 |
| points_difference | 0.289 | -0.314 | 0.013 |
| away_team_away_conceded_avg | 0.167 | -0.174 | 0.013 |
| away_team_goals_conceded_last_5 | 0.108 | -0.136 | -0.008 |
| home_team_goals_conceded_last_5 | -0.123 | 0.152 | 0.008 |
| rest_days_difference | -0.139 | 0.150 | -0.008 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 39 | 7 | 9 | 23 | 17.9% | 23.1% | 59.0% |
| -4..-2 | 55 | 14 | 17 | 24 | 25.5% | 30.9% | 43.6% |
| -1..1 | 53 | 20 | 12 | 21 | 37.7% | 22.6% | 39.6% |
| 2..4 | 45 | 25 | 9 | 11 | 55.6% | 20.0% | 24.4% |
| >4 | 42 | 27 | 9 | 6 | 64.3% | 21.4% | 14.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 35 | 25 | 5 | 5 | 71.4% | 14.3% | 14.3% |
| -5..-2 | 58 | 30 | 14 | 14 | 51.7% | 24.1% | 24.1% |
| -1..1 | 49 | 21 | 14 | 14 | 42.9% | 28.6% | 28.6% |
| 2..5 | 59 | 15 | 15 | 29 | 25.4% | 25.4% | 49.2% |
| >=6 | 33 | 2 | 8 | 23 | 6.1% | 24.2% | 69.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 34 | 17 | 9 | 8 | 50.0% | 26.5% | 23.5% |
| -1..0 | 48 | 28 | 6 | 14 | 58.3% | 12.5% | 29.2% |
| 0 | 47 | 15 | 14 | 18 | 31.9% | 29.8% | 38.3% |
| 1..2 | 81 | 24 | 21 | 36 | 29.6% | 25.9% | 44.4% |
| >2 | 10 | 3 | 2 | 5 | 30.0% | 20.0% | 50.0% |
| unknown | 14 | 6 | 4 | 4 | 42.9% | 28.6% | 28.6% |
- *14 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **29.6%** home win (24/81)
- `>= 0.5` tier: **45.1%** home win (69/153)
- Home-win gap (>= split minus < split): **+15.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 81 | 24 | 16 | 41 | 29.6% |
| high | >= 0.5 | 153 | 69 | 40 | 44 | 45.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 6.129 | -1.464 | -6.235 | 12.364 |
| away_points_before_match | 16.151 | 19.250 | 23.082 | 6.932 |
| home_points_before_match | 22.280 | 17.786 | 16.847 | 5.433 |
| position_difference | -2.452 | 0.714 | 2.318 | 4.769 |
| home_position_before_match | 5.430 | 6.732 | 7.882 | 2.452 |
| away_position_before_match | 7.882 | 6.018 | 5.565 | 2.317 |
| away_team_points_last_5 | 4.527 | 6.250 | 6.788 | 2.261 |
| away_team_goals_conceded_last_5 | 6.484 | 4.679 | 4.824 | 1.805 |
| home_team_points_last_5 | 6.774 | 5.625 | 4.976 | 1.798 |
| home_team_goals_scored_last_5 | 6.301 | 4.696 | 4.588 | 1.713 |
| away_team_goals_scored_last_5 | 4.505 | 5.571 | 6.212 | 1.706 |
| home_rest_days | 7.920 | 9.423 | 8.573 | 1.503 |
| home_team_goals_conceded_last_5 | 4.731 | 4.875 | 5.976 | 1.245 |
| away_rest_days | 8.161 | 9.269 | 8.207 | 1.108 |
| away_team_wins_last_5 | 2.204 | 2.786 | 2.953 | 0.749 |
| home_team_wins_last_5 | 3.011 | 2.661 | 2.294 | 0.717 |
| rest_days_difference | -0.230 | 0.154 | 0.333 | 0.563 |
| away_team_away_conceded_avg | 1.358 | 1.003 | 0.865 | 0.493 |
| home_team_home_goals_avg | 1.277 | 0.995 | 0.956 | 0.321 |
| away_team_away_goals_avg | 0.948 | 1.151 | 1.235 | 0.287 |
| home_team_home_conceded_avg | 0.964 | 1.052 | 1.249 | 0.284 |
| away_team_away_win_rate | 0.508 | 0.625 | 0.667 | 0.159 |
| home_team_home_win_rate | 0.606 | 0.556 | 0.450 | 0.156 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\azer\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\azer\charts\relationships_home_win_pct_by_position.png)

