# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:06:09+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premiership (Scotland)
- Scope: league `scot-premier`

- Matches analysed: **234** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_points_before_match | 0.034 | 0.198 | 0.163 |
| home_points_before_match | 0.219 | -0.047 | 0.127 |
| away_position_before_match | 0.101 | -0.246 | -0.097 |
| away_team_goals_scored_last_5 | 0.006 | 0.127 | 0.093 |
| home_team_goals_conceded_last_5 | -0.060 | 0.187 | 0.086 |
| home_team_home_goals_avg | 0.161 | -0.057 | 0.078 |
| home_position_before_match | -0.255 | 0.157 | -0.077 |
| home_team_home_win_rate | 0.193 | -0.105 | 0.069 |
| away_team_goals_conceded_last_5 | 0.178 | -0.099 | 0.061 |
| home_team_goals_scored_last_5 | 0.160 | -0.082 | 0.060 |
| away_team_away_goals_avg | -0.060 | 0.147 | 0.058 |
| points_difference | 0.239 | -0.320 | -0.048 |
| away_team_points_last_5 | -0.069 | 0.135 | 0.043 |
| away_team_away_win_rate | -0.094 | 0.157 | 0.041 |
| away_team_wins_last_5 | -0.078 | 0.138 | 0.039 |
| away_team_away_conceded_avg | 0.079 | -0.138 | -0.038 |
| home_rest_days | -0.033 | -0.010 | -0.031 |
| home_team_home_conceded_avg | -0.073 | 0.114 | 0.026 |
| home_team_points_last_5 | 0.210 | -0.188 | 0.022 |
| rest_days_difference | 0.024 | -0.056 | -0.021 |
| home_team_wins_last_5 | 0.198 | -0.178 | 0.021 |
| away_rest_days | -0.052 | 0.029 | -0.018 |
| position_difference | -0.280 | 0.314 | 0.013 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 44 | 7 | 13 | 24 | 15.9% | 29.5% | 54.5% |
| -4..-2 | 42 | 20 | 11 | 11 | 47.6% | 26.2% | 26.2% |
| -1..1 | 69 | 30 | 22 | 17 | 43.5% | 31.9% | 24.6% |
| 2..4 | 39 | 23 | 9 | 7 | 59.0% | 23.1% | 17.9% |
| >4 | 40 | 25 | 9 | 6 | 62.5% | 22.5% | 15.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 31 | 23 | 6 | 2 | 74.2% | 19.4% | 6.5% |
| -5..-2 | 60 | 33 | 13 | 14 | 55.0% | 21.7% | 23.3% |
| -1..1 | 48 | 26 | 14 | 8 | 54.2% | 29.2% | 16.7% |
| 2..5 | 67 | 18 | 23 | 26 | 26.9% | 34.3% | 38.8% |
| >=6 | 28 | 5 | 8 | 15 | 17.9% | 28.6% | 53.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 19 | 7 | 5 | 7 | 36.8% | 26.3% | 36.8% |
| -1..0 | 40 | 18 | 12 | 10 | 45.0% | 30.0% | 25.0% |
| 0 | 104 | 48 | 25 | 31 | 46.2% | 24.0% | 29.8% |
| 1..2 | 42 | 16 | 12 | 14 | 38.1% | 28.6% | 33.3% |
| >2 | 21 | 13 | 6 | 2 | 61.9% | 28.6% | 9.5% |
| unknown | 8 | 3 | 4 | 1 | 37.5% | 50.0% | 12.5% |
- *8 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.7%** home win (65/168)
- `>= 0.5` tier: **60.6%** home win (40/66)
- Home-win gap (>= split minus < split): **+21.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 168 | 65 | 50 | 53 | 38.7% |
| high | >= 0.5 | 66 | 40 | 14 | 12 | 60.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 29.848 | 17.281 | 22.600 | 12.566 |
| points_difference | 5.495 | -2.672 | -6.569 | 12.064 |
| away_points_before_match | 24.352 | 19.953 | 29.169 | 9.216 |
| position_difference | -1.781 | 0.781 | 2.323 | 4.104 |
| home_team_points_last_5 | 7.305 | 5.109 | 5.000 | 2.305 |
| home_position_before_match | 5.657 | 7.578 | 7.800 | 2.143 |
| away_position_before_match | 7.438 | 6.797 | 5.477 | 1.961 |
| home_team_goals_scored_last_5 | 6.762 | 5.250 | 5.708 | 1.512 |
| away_team_points_last_5 | 6.171 | 5.625 | 7.123 | 1.498 |
| home_team_goals_conceded_last_5 | 5.867 | 5.922 | 7.354 | 1.487 |
| away_team_goals_scored_last_5 | 6.314 | 5.703 | 6.985 | 1.281 |
| away_team_goals_conceded_last_5 | 6.752 | 5.547 | 5.600 | 1.206 |
| away_rest_days | 7.167 | 7.600 | 8.281 | 1.115 |
| rest_days_difference | 0.304 | 0.450 | -0.344 | 0.794 |
| home_team_wins_last_5 | 2.000 | 1.312 | 1.262 | 0.738 |
| away_team_wins_last_5 | 1.590 | 1.469 | 1.985 | 0.516 |
| home_rest_days | 7.471 | 7.984 | 7.938 | 0.513 |
| home_team_home_goals_avg | 1.474 | 1.230 | 1.340 | 0.243 |
| away_team_away_goals_avg | 1.020 | 1.108 | 1.199 | 0.179 |
| home_team_home_conceded_avg | 1.015 | 1.103 | 1.190 | 0.175 |
| away_team_away_conceded_avg | 1.459 | 1.284 | 1.307 | 0.175 |
| home_team_home_win_rate | 0.411 | 0.294 | 0.313 | 0.117 |
| away_team_away_win_rate | 0.230 | 0.241 | 0.329 | 0.099 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\scot-premier\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\scot-premier\charts\relationships_home_win_pct_by_position.png)

