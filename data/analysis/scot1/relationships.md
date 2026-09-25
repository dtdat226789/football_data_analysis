# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:44:58+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: League One (Scotland)
- Scope: league `scot1`

- Matches analysed: **230** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_conceded_avg | 0.214 | 0.018 | 0.195 |
| position_difference | -0.338 | 0.127 | -0.195 |
| away_position_before_match | 0.198 | 0.003 | 0.171 |
| points_difference | 0.242 | -0.104 | 0.130 |
| away_team_away_goals_avg | -0.113 | -0.019 | -0.110 |
| away_team_away_win_rate | -0.087 | -0.032 | -0.098 |
| home_position_before_match | -0.261 | 0.176 | -0.094 |
| home_points_before_match | 0.110 | -0.014 | 0.084 |
| away_team_goals_conceded_last_5 | 0.076 | 0.017 | 0.078 |
| home_team_points_last_5 | 0.215 | -0.147 | 0.076 |
| home_team_home_win_rate | 0.215 | -0.147 | 0.076 |
| home_team_home_goals_avg | 0.184 | -0.115 | 0.073 |
| away_team_goals_scored_last_5 | -0.071 | -0.005 | -0.065 |
| away_rest_days | -0.092 | 0.031 | -0.055 |
| home_team_wins_last_5 | 0.215 | -0.178 | 0.053 |
| away_team_wins_last_5 | -0.057 | 0.010 | -0.041 |
| home_team_goals_conceded_last_5 | -0.140 | 0.216 | 0.038 |
| away_team_points_last_5 | -0.054 | 0.015 | -0.035 |
| rest_days_difference | 0.112 | -0.089 | 0.031 |
| away_points_before_match | -0.086 | 0.070 | -0.022 |
| home_team_goals_scored_last_5 | 0.109 | -0.102 | 0.018 |
| home_rest_days | 0.006 | -0.031 | -0.018 |
| home_team_home_conceded_avg | -0.086 | 0.105 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 43 | 16 | 11 | 16 | 37.2% | 25.6% | 37.2% |
| -4..-2 | 43 | 14 | 15 | 14 | 32.6% | 34.9% | 32.6% |
| -1..1 | 72 | 32 | 16 | 24 | 44.4% | 22.2% | 33.3% |
| 2..4 | 40 | 18 | 13 | 9 | 45.0% | 32.5% | 22.5% |
| >4 | 32 | 19 | 6 | 7 | 59.4% | 18.8% | 21.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 23 | 18 | 3 | 2 | 78.3% | 13.0% | 8.7% |
| -5..-2 | 58 | 32 | 13 | 13 | 55.2% | 22.4% | 22.4% |
| -1..1 | 55 | 22 | 16 | 17 | 40.0% | 29.1% | 30.9% |
| 2..5 | 71 | 22 | 22 | 27 | 31.0% | 31.0% | 38.0% |
| >=6 | 23 | 5 | 7 | 11 | 21.7% | 30.4% | 47.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 21 | 8 | 7 | 6 | 38.1% | 33.3% | 28.6% |
| -1..0 | 2 | 0 | 2 | 0 | 0.0% | 100.0% | 0.0% |
| 0 | 170 | 73 | 44 | 53 | 42.9% | 25.9% | 31.2% |
| 1..2 | 1 | 0 | 1 | 0 | 0.0% | 100.0% | 0.0% |
| >2 | 23 | 13 | 5 | 5 | 56.5% | 21.7% | 21.7% |
| unknown | 13 | 5 | 2 | 6 | 38.5% | 15.4% | 46.2% |
- *13 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.3%** home win (23/69)
- `>= 0.5` tier: **47.2%** home win (76/161)
- Home-win gap (>= split minus < split): **+13.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 69 | 23 | 17 | 29 | 33.3% |
| high | >= 0.5 | 161 | 76 | 44 | 41 | 47.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.646 | -3.574 | -4.343 | 8.989 |
| away_points_before_match | 18.263 | 26.230 | 21.714 | 7.967 |
| home_points_before_match | 22.909 | 22.656 | 17.371 | 5.538 |
| position_difference | -1.424 | 1.033 | 1.543 | 2.967 |
| home_position_before_match | 4.626 | 5.984 | 6.486 | 1.859 |
| home_team_points_last_5 | 6.182 | 6.148 | 4.514 | 1.668 |
| home_team_goals_conceded_last_5 | 5.293 | 5.410 | 6.514 | 1.221 |
| home_team_goals_scored_last_5 | 5.707 | 5.934 | 4.714 | 1.220 |
| away_position_before_match | 6.051 | 4.951 | 4.943 | 1.108 |
| away_rest_days | 7.096 | 7.576 | 8.108 | 1.012 |
| away_team_points_last_5 | 5.717 | 6.721 | 5.914 | 1.004 |
| away_team_goals_scored_last_5 | 5.505 | 6.492 | 5.671 | 0.987 |
| home_team_wins_last_5 | 2.889 | 2.934 | 2.057 | 0.877 |
| home_rest_days | 7.326 | 7.475 | 7.906 | 0.580 |
| rest_days_difference | 0.277 | -0.102 | -0.281 | 0.558 |
| away_team_wins_last_5 | 2.687 | 3.049 | 2.686 | 0.363 |
| home_team_home_goals_avg | 1.356 | 1.243 | 1.058 | 0.298 |
| away_team_goals_conceded_last_5 | 5.495 | 5.623 | 5.371 | 0.252 |
| away_team_away_goals_avg | 0.990 | 1.205 | 1.079 | 0.215 |
| away_team_away_conceded_avg | 1.323 | 1.192 | 1.187 | 0.136 |
| home_team_home_win_rate | 0.622 | 0.606 | 0.490 | 0.132 |
| home_team_home_conceded_avg | 1.014 | 1.070 | 1.138 | 0.123 |
| away_team_away_win_rate | 0.490 | 0.551 | 0.493 | 0.061 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\scot1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\scot1\charts\relationships_home_win_pct_by_position.png)

