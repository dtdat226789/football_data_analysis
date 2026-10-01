# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:50:05+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Ligue 1 (France)
- Scope: league `france1`

- Matches analysed: **310** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_conceded_last_5 | -0.040 | -0.141 | -0.125 |
| home_team_home_win_rate | 0.149 | 0.013 | 0.114 |
| away_team_wins_last_5 | -0.018 | 0.184 | 0.113 |
| away_team_points_last_5 | -0.040 | 0.189 | 0.101 |
| home_team_home_goals_avg | 0.113 | 0.030 | 0.101 |
| away_position_before_match | 0.085 | -0.226 | -0.095 |
| away_team_away_win_rate | -0.023 | 0.161 | 0.094 |
| home_position_before_match | -0.186 | 0.091 | -0.069 |
| home_rest_days | 0.024 | 0.070 | 0.065 |
| home_team_wins_last_5 | 0.126 | -0.048 | 0.056 |
| rest_days_difference | 0.040 | 0.036 | 0.053 |
| away_points_before_match | -0.100 | 0.177 | 0.050 |
| away_rest_days | 0.009 | 0.060 | 0.048 |
| home_team_points_last_5 | 0.115 | -0.050 | 0.047 |
| home_points_before_match | 0.051 | 0.006 | 0.040 |
| home_team_goals_scored_last_5 | 0.092 | -0.038 | 0.039 |
| away_team_away_goals_avg | -0.052 | 0.107 | 0.037 |
| home_team_home_conceded_avg | -0.062 | 0.028 | -0.025 |
| away_team_away_conceded_avg | 0.011 | -0.044 | -0.022 |
| position_difference | -0.196 | 0.230 | 0.018 |
| home_team_goals_conceded_last_5 | -0.092 | 0.072 | -0.016 |
| points_difference | 0.184 | -0.207 | -0.011 |
| away_team_goals_scored_last_5 | -0.096 | 0.109 | 0.006 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 53 | 22 | 8 | 23 | 41.5% | 15.1% | 43.4% |
| -4..-2 | 70 | 31 | 21 | 18 | 44.3% | 30.0% | 25.7% |
| -1..1 | 83 | 27 | 25 | 31 | 32.5% | 30.1% | 37.3% |
| 2..4 | 54 | 29 | 11 | 14 | 53.7% | 20.4% | 25.9% |
| >4 | 50 | 34 | 11 | 5 | 68.0% | 22.0% | 10.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 72 | 46 | 18 | 8 | 63.9% | 25.0% | 11.1% |
| -5..-2 | 54 | 23 | 16 | 15 | 42.6% | 29.6% | 27.8% |
| -1..1 | 53 | 26 | 12 | 15 | 49.1% | 22.6% | 28.3% |
| 2..5 | 51 | 23 | 11 | 17 | 45.1% | 21.6% | 33.3% |
| >=6 | 80 | 25 | 19 | 36 | 31.2% | 23.8% | 45.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 25 | 8 | 8 | 9 | 32.0% | 32.0% | 36.0% |
| -1..0 | 74 | 33 | 14 | 27 | 44.6% | 18.9% | 36.5% |
| 0 | 104 | 54 | 29 | 21 | 51.9% | 27.9% | 20.2% |
| 1..2 | 88 | 40 | 24 | 24 | 45.5% | 27.3% | 27.3% |
| >2 | 8 | 3 | 0 | 5 | 37.5% | 0.0% | 62.5% |
| unknown | 11 | 5 | 1 | 5 | 45.5% | 9.1% | 45.5% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.3%** home win (54/141)
- `>= 0.5` tier: **52.7%** home win (89/169)
- Home-win gap (>= split minus < split): **+14.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 141 | 54 | 40 | 47 | 38.3% |
| high | >= 0.5 | 169 | 89 | 36 | 44 | 52.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.189 | -0.039 | -5.440 | 8.628 |
| away_points_before_match | 20.441 | 21.947 | 27.209 | 6.768 |
| position_difference | -1.685 | 0.250 | 3.220 | 4.905 |
| away_position_before_match | 10.140 | 11.211 | 7.648 | 3.562 |
| home_position_before_match | 8.455 | 11.461 | 10.868 | 3.006 |
| away_team_goals_conceded_last_5 | 6.133 | 7.592 | 5.527 | 2.065 |
| away_team_points_last_5 | 6.126 | 5.421 | 7.484 | 2.062 |
| home_points_before_match | 23.629 | 21.908 | 21.769 | 1.860 |
| home_team_goals_conceded_last_5 | 5.748 | 7.250 | 6.615 | 1.502 |
| home_team_points_last_5 | 6.664 | 5.487 | 5.791 | 1.177 |
| away_team_goals_scored_last_5 | 6.140 | 6.066 | 7.231 | 1.165 |
| away_team_wins_last_5 | 1.706 | 1.382 | 2.110 | 0.728 |
| home_team_goals_scored_last_5 | 6.580 | 5.987 | 5.934 | 0.646 |
| home_team_wins_last_5 | 1.874 | 1.434 | 1.560 | 0.440 |
| away_team_away_conceded_avg | 1.559 | 1.774 | 1.461 | 0.312 |
| home_team_home_conceded_avg | 0.972 | 1.266 | 1.079 | 0.294 |
| away_rest_days | 8.115 | 8.373 | 8.291 | 0.258 |
| away_team_away_goals_avg | 1.050 | 0.988 | 1.178 | 0.191 |
| rest_days_difference | 0.101 | -0.067 | 0.105 | 0.171 |
| home_team_home_goals_avg | 1.634 | 1.617 | 1.470 | 0.164 |
| home_rest_days | 8.254 | 8.307 | 8.395 | 0.142 |
| away_team_away_win_rate | 0.253 | 0.215 | 0.290 | 0.075 |
| home_team_home_win_rate | 0.520 | 0.472 | 0.457 | 0.063 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\france1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\france1\charts\relationships_home_win_pct_by_position.png)

