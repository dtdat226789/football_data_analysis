# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:49:50+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Thai League 1 (Thailand)
- Scope: league `thai1`

- Matches analysed: **264** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_rest_days | -0.104 | -0.042 | -0.115 |
| rest_days_difference | 0.085 | 0.028 | 0.089 |
| home_position_before_match | -0.191 | 0.113 | -0.085 |
| points_difference | 0.259 | -0.221 | 0.072 |
| away_team_away_conceded_avg | 0.017 | -0.116 | -0.060 |
| position_difference | -0.250 | 0.229 | -0.059 |
| home_points_before_match | 0.170 | -0.133 | 0.055 |
| away_team_goals_conceded_last_5 | 0.139 | -0.100 | 0.051 |
| away_team_wins_last_5 | -0.070 | 0.017 | -0.047 |
| home_team_home_conceded_avg | -0.066 | 0.015 | -0.045 |
| home_team_goals_scored_last_5 | 0.159 | -0.140 | 0.041 |
| away_team_goals_scored_last_5 | -0.045 | 0.116 | 0.037 |
| home_team_points_last_5 | 0.164 | -0.161 | 0.032 |
| home_team_home_goals_avg | 0.162 | -0.161 | 0.030 |
| home_team_wins_last_5 | 0.143 | -0.144 | 0.025 |
| home_team_goals_conceded_last_5 | -0.077 | 0.068 | -0.020 |
| away_team_away_win_rate | -0.047 | 0.033 | -0.018 |
| home_rest_days | -0.012 | -0.011 | -0.017 |
| home_team_home_win_rate | 0.088 | -0.092 | 0.013 |
| away_team_away_goals_avg | -0.114 | 0.130 | -0.011 |
| away_team_points_last_5 | -0.084 | 0.093 | -0.009 |
| away_position_before_match | 0.160 | -0.212 | -0.004 |
| away_points_before_match | -0.039 | 0.044 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 39 | 9 | 13 | 17 | 23.1% | 33.3% | 43.6% |
| -4..-2 | 49 | 18 | 11 | 20 | 36.7% | 22.4% | 40.8% |
| -1..1 | 94 | 43 | 35 | 16 | 45.7% | 37.2% | 17.0% |
| 2..4 | 48 | 20 | 16 | 12 | 41.7% | 33.3% | 25.0% |
| >4 | 34 | 24 | 4 | 6 | 70.6% | 11.8% | 17.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 48 | 32 | 9 | 7 | 66.7% | 18.8% | 14.6% |
| -5..-2 | 57 | 28 | 19 | 10 | 49.1% | 33.3% | 17.5% |
| -1..1 | 42 | 19 | 12 | 11 | 45.2% | 28.6% | 26.2% |
| 2..5 | 61 | 22 | 21 | 18 | 36.1% | 34.4% | 29.5% |
| >=6 | 56 | 13 | 18 | 25 | 23.2% | 32.1% | 44.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 33 | 15 | 6 | 12 | 45.5% | 18.2% | 36.4% |
| -1..0 | 52 | 23 | 18 | 11 | 44.2% | 34.6% | 21.2% |
| 0 | 70 | 31 | 22 | 17 | 44.3% | 31.4% | 24.3% |
| 1..2 | 69 | 27 | 21 | 21 | 39.1% | 30.4% | 30.4% |
| >2 | 24 | 11 | 7 | 6 | 45.8% | 29.2% | 25.0% |
| unknown | 16 | 7 | 5 | 4 | 43.8% | 31.2% | 25.0% |
- *16 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.9%** home win (22/58)
- `>= 0.5` tier: **44.7%** home win (92/206)
- Home-win gap (>= split minus < split): **+6.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 58 | 22 | 17 | 19 | 37.9% |
| high | >= 0.5 | 206 | 92 | 62 | 52 | 44.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.246 | -1.797 | -5.042 | 8.288 |
| home_points_before_match | 20.219 | 16.190 | 14.676 | 5.543 |
| position_difference | -1.965 | 1.051 | 2.831 | 4.796 |
| away_position_before_match | 9.693 | 8.481 | 6.873 | 2.820 |
| away_points_before_match | 16.974 | 17.987 | 19.718 | 2.745 |
| home_position_before_match | 7.728 | 9.532 | 9.704 | 1.976 |
| home_team_goals_conceded_last_5 | 4.939 | 6.418 | 5.817 | 1.479 |
| away_team_goals_scored_last_5 | 5.316 | 5.443 | 6.704 | 1.388 |
| away_team_goals_conceded_last_5 | 6.184 | 5.481 | 4.831 | 1.353 |
| away_team_points_last_5 | 5.175 | 5.861 | 6.465 | 1.289 |
| home_team_points_last_5 | 6.149 | 5.228 | 4.901 | 1.248 |
| home_team_goals_scored_last_5 | 5.947 | 5.633 | 4.718 | 1.229 |
| home_rest_days | 8.897 | 9.635 | 9.209 | 0.738 |
| home_team_wins_last_5 | 2.956 | 2.595 | 2.451 | 0.505 |
| away_rest_days | 8.729 | 9.162 | 8.955 | 0.433 |
| away_team_away_goals_avg | 0.900 | 0.981 | 1.305 | 0.404 |
| home_team_home_goals_avg | 1.496 | 1.439 | 1.105 | 0.391 |
| away_team_wins_last_5 | 2.614 | 2.873 | 2.944 | 0.330 |
| rest_days_difference | 0.168 | 0.473 | 0.254 | 0.305 |
| home_team_home_conceded_avg | 0.924 | 1.158 | 1.024 | 0.234 |
| away_team_away_conceded_avg | 1.419 | 1.430 | 1.273 | 0.156 |
| away_team_away_win_rate | 0.492 | 0.533 | 0.560 | 0.068 |
| home_team_home_win_rate | 0.676 | 0.631 | 0.622 | 0.054 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\thai1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\thai1\charts\relationships_home_win_pct_by_position.png)

