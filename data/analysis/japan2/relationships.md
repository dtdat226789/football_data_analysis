# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:02:42+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: J2 League (Japan)
- Scope: league `japan2`

- Matches analysed: **760** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_points_last_5 | 0.164 | -0.049 | 0.088 |
| position_difference | -0.209 | 0.138 | -0.063 |
| home_team_goals_conceded_last_5 | -0.102 | 0.021 | -0.062 |
| home_points_before_match | 0.115 | -0.042 | 0.057 |
| away_position_before_match | 0.148 | -0.083 | 0.054 |
| home_team_goals_scored_last_5 | 0.124 | -0.058 | 0.053 |
| home_team_wins_last_5 | 0.115 | -0.054 | 0.049 |
| points_difference | 0.198 | -0.148 | 0.048 |
| rest_days_difference | 0.062 | -0.003 | 0.044 |
| home_team_home_goals_avg | 0.106 | -0.054 | 0.043 |
| away_team_goals_conceded_last_5 | 0.080 | -0.032 | 0.038 |
| away_team_away_goals_avg | -0.056 | 0.007 | -0.037 |
| away_team_wins_last_5 | -0.077 | 0.035 | -0.034 |
| home_position_before_match | -0.143 | 0.109 | -0.034 |
| away_team_away_conceded_avg | 0.086 | -0.052 | 0.029 |
| home_rest_days | 0.004 | 0.036 | 0.027 |
| away_points_before_match | -0.024 | 0.062 | 0.024 |
| away_rest_days | -0.021 | 0.037 | 0.009 |
| away_team_points_last_5 | -0.069 | 0.068 | -0.006 |
| away_team_goals_scored_last_5 | -0.066 | 0.065 | -0.006 |
| home_team_home_conceded_avg | -0.040 | 0.037 | -0.005 |
| away_team_away_win_rate | -0.007 | 0.014 | 0.004 |
| home_team_home_win_rate | 0.057 | -0.057 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 107 | 33 | 20 | 54 | 30.8% | 18.7% | 50.5% |
| -4..-2 | 168 | 64 | 37 | 67 | 38.1% | 22.0% | 39.9% |
| -1..1 | 226 | 77 | 69 | 80 | 34.1% | 30.5% | 35.4% |
| 2..4 | 133 | 55 | 38 | 40 | 41.4% | 28.6% | 30.1% |
| >4 | 126 | 69 | 33 | 24 | 54.8% | 26.2% | 19.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 188 | 104 | 49 | 35 | 55.3% | 26.1% | 18.6% |
| -5..-2 | 134 | 57 | 28 | 49 | 42.5% | 20.9% | 36.6% |
| -1..1 | 106 | 42 | 24 | 40 | 39.6% | 22.6% | 37.7% |
| 2..5 | 136 | 40 | 43 | 53 | 29.4% | 31.6% | 39.0% |
| >=6 | 196 | 55 | 53 | 88 | 28.1% | 27.0% | 44.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 14 | 3 | 3 | 8 | 21.4% | 21.4% | 57.1% |
| -1..0 | 108 | 42 | 33 | 33 | 38.9% | 30.6% | 30.6% |
| 0 | 489 | 202 | 114 | 173 | 41.3% | 23.3% | 35.4% |
| 1..2 | 117 | 40 | 37 | 40 | 34.2% | 31.6% | 34.2% |
| >2 | 12 | 3 | 6 | 3 | 25.0% | 50.0% | 25.0% |
| unknown | 20 | 8 | 4 | 8 | 40.0% | 20.0% | 40.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.0%** home win (64/173)
- `>= 0.5` tier: **39.9%** home win (234/587)
- Home-win gap (>= split minus < split): **+2.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 173 | 64 | 38 | 71 | 37.0% |
| high | >= 0.5 | 587 | 234 | 159 | 194 | 39.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.587 | -0.604 | -3.517 | 7.104 |
| position_difference | -2.161 | 0.305 | 2.464 | 4.625 |
| home_points_before_match | 27.614 | 23.939 | 23.630 | 3.984 |
| away_points_before_match | 24.027 | 24.543 | 27.147 | 3.120 |
| home_position_before_match | 9.433 | 10.797 | 12.023 | 2.590 |
| away_position_before_match | 11.594 | 10.492 | 9.558 | 2.035 |
| home_team_points_last_5 | 6.822 | 6.548 | 5.592 | 1.230 |
| away_team_points_last_5 | 6.003 | 6.020 | 6.838 | 0.834 |
| home_team_goals_scored_last_5 | 6.017 | 5.685 | 5.211 | 0.805 |
| home_team_goals_conceded_last_5 | 5.423 | 5.442 | 6.128 | 0.705 |
| away_team_goals_scored_last_5 | 5.436 | 5.645 | 6.136 | 0.700 |
| away_team_goals_conceded_last_5 | 5.728 | 6.091 | 5.408 | 0.684 |
| home_team_wins_last_5 | 3.023 | 2.995 | 2.702 | 0.322 |
| away_team_wins_last_5 | 2.795 | 2.863 | 3.034 | 0.239 |
| rest_days_difference | 0.017 | 0.114 | -0.074 | 0.188 |
| home_rest_days | 7.338 | 7.513 | 7.339 | 0.175 |
| home_team_home_goals_avg | 1.310 | 1.224 | 1.145 | 0.165 |
| away_team_away_goals_avg | 1.012 | 1.125 | 1.102 | 0.113 |
| home_team_home_conceded_avg | 1.029 | 1.046 | 1.139 | 0.111 |
| away_rest_days | 7.321 | 7.399 | 7.412 | 0.092 |
| away_team_away_conceded_avg | 1.256 | 1.234 | 1.173 | 0.083 |
| home_team_home_win_rate | 0.642 | 0.639 | 0.586 | 0.056 |
| away_team_away_win_rate | 0.565 | 0.587 | 0.586 | 0.023 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\japan2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\japan2\charts\relationships_home_win_pct_by_position.png)

