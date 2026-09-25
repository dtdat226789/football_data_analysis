# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:56:41+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: 3. CFL - Group A (Czech Republic)
- Scope: league `czech3a`

- Matches analysed: **330** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_rest_days | -0.044 | -0.129 | -0.123 |
| away_rest_days | -0.040 | -0.123 | -0.115 |
| away_team_goals_scored_last_5 | -0.024 | 0.193 | 0.115 |
| home_team_goals_scored_last_5 | 0.225 | -0.083 | 0.114 |
| home_team_points_last_5 | 0.195 | -0.052 | 0.113 |
| home_position_before_match | -0.219 | 0.084 | -0.109 |
| away_team_goals_conceded_last_5 | 0.128 | -0.014 | 0.087 |
| home_team_wins_last_5 | 0.144 | -0.033 | 0.087 |
| away_team_wins_last_5 | -0.048 | 0.127 | 0.051 |
| away_position_before_match | 0.115 | -0.195 | -0.047 |
| position_difference | -0.238 | 0.200 | -0.044 |
| rest_days_difference | -0.021 | -0.038 | -0.042 |
| away_points_before_match | -0.076 | 0.136 | 0.035 |
| home_team_home_win_rate | 0.057 | -0.013 | 0.034 |
| home_points_before_match | 0.077 | -0.037 | 0.033 |
| away_team_points_last_5 | -0.049 | 0.093 | 0.026 |
| home_team_home_conceded_avg | 0.057 | -0.033 | 0.021 |
| home_team_home_goals_avg | 0.159 | -0.150 | 0.018 |
| away_team_away_win_rate | -0.154 | 0.158 | -0.009 |
| points_difference | 0.221 | -0.252 | -0.005 |
| away_team_away_conceded_avg | 0.134 | -0.142 | 0.004 |
| away_team_away_goals_avg | -0.133 | 0.143 | -0.003 |
| home_team_goals_conceded_last_5 | -0.022 | 0.026 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 40 | 12 | 7 | 21 | 30.0% | 17.5% | 52.5% |
| -4..-2 | 73 | 30 | 11 | 32 | 41.1% | 15.1% | 43.8% |
| -1..1 | 109 | 57 | 23 | 29 | 52.3% | 21.1% | 26.6% |
| 2..4 | 61 | 26 | 21 | 14 | 42.6% | 34.4% | 23.0% |
| >4 | 47 | 22 | 12 | 13 | 46.8% | 25.5% | 27.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 74 | 39 | 13 | 22 | 52.7% | 17.6% | 29.7% |
| -5..-2 | 71 | 34 | 23 | 14 | 47.9% | 32.4% | 19.7% |
| -1..1 | 48 | 25 | 14 | 9 | 52.1% | 29.2% | 18.8% |
| 2..5 | 59 | 30 | 7 | 22 | 50.8% | 11.9% | 37.3% |
| >=6 | 78 | 19 | 17 | 42 | 24.4% | 21.8% | 53.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 20 | 5 | 8 | 7 | 25.0% | 40.0% | 35.0% |
| -1..0 | 63 | 33 | 13 | 17 | 52.4% | 20.6% | 27.0% |
| 0 | 147 | 60 | 31 | 56 | 40.8% | 21.1% | 38.1% |
| 1..2 | 58 | 30 | 13 | 15 | 51.7% | 22.4% | 25.9% |
| >2 | 25 | 11 | 4 | 10 | 44.0% | 16.0% | 40.0% |
| unknown | 17 | 8 | 5 | 4 | 47.1% | 29.4% | 23.5% |
- *17 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.7%** home win (36/93)
- `>= 0.5` tier: **46.8%** home win (111/237)
- Home-win gap (>= split minus < split): **+8.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 93 | 36 | 19 | 38 | 38.7% |
| high | >= 0.5 | 237 | 111 | 55 | 71 | 46.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.884 | 0.581 | -4.156 | 6.040 |
| position_difference | -1.381 | 0.000 | 2.064 | 3.445 |
| away_points_before_match | 17.701 | 18.527 | 20.725 | 3.024 |
| home_points_before_match | 19.585 | 19.108 | 16.569 | 3.016 |
| away_position_before_match | 9.728 | 9.243 | 7.817 | 1.911 |
| home_team_goals_scored_last_5 | 7.340 | 6.892 | 5.651 | 1.689 |
| home_rest_days | 9.576 | 10.304 | 8.642 | 1.663 |
| home_position_before_match | 8.347 | 9.243 | 9.881 | 1.534 |
| away_team_goals_scored_last_5 | 6.585 | 5.946 | 7.257 | 1.311 |
| home_team_points_last_5 | 6.395 | 6.095 | 5.183 | 1.211 |
| away_team_goals_conceded_last_5 | 7.020 | 5.865 | 6.422 | 1.156 |
| away_rest_days | 9.273 | 9.348 | 8.438 | 0.910 |
| away_team_points_last_5 | 5.959 | 5.351 | 6.220 | 0.869 |
| rest_days_difference | 0.302 | 0.957 | 0.219 | 0.737 |
| home_team_goals_conceded_last_5 | 6.782 | 6.230 | 6.954 | 0.724 |
| away_team_away_goals_avg | 1.204 | 1.169 | 1.600 | 0.431 |
| home_team_home_goals_avg | 1.688 | 1.610 | 1.264 | 0.424 |
| away_team_away_conceded_avg | 1.704 | 1.442 | 1.351 | 0.352 |
| home_team_wins_last_5 | 2.694 | 2.581 | 2.450 | 0.244 |
| away_team_away_win_rate | 0.423 | 0.476 | 0.617 | 0.194 |
| away_team_wins_last_5 | 2.558 | 2.541 | 2.716 | 0.175 |
| home_team_home_conceded_avg | 1.400 | 1.270 | 1.272 | 0.130 |
| home_team_home_win_rate | 0.599 | 0.610 | 0.570 | 0.040 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\czech3a\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\czech3a\charts\relationships_home_win_pct_by_position.png)

