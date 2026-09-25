# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:51:01+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premiere Ligue Women (France)
- Scope: league `wfrance1`

- Matches analysed: **153** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_goals_avg | -0.060 | 0.368 | 0.250 |
| away_position_before_match | 0.096 | -0.298 | -0.164 |
| home_position_before_match | -0.411 | 0.234 | -0.144 |
| home_team_home_conceded_avg | -0.275 | 0.125 | -0.122 |
| away_team_goals_conceded_last_5 | 0.024 | -0.172 | -0.120 |
| away_team_goals_scored_last_5 | -0.086 | 0.226 | 0.114 |
| home_team_goals_conceded_last_5 | -0.260 | 0.133 | -0.104 |
| away_team_away_win_rate | -0.108 | 0.177 | 0.056 |
| rest_days_difference | 0.140 | -0.075 | 0.056 |
| home_team_home_win_rate | 0.139 | -0.207 | -0.055 |
| home_team_wins_last_5 | 0.161 | -0.226 | -0.052 |
| away_team_wins_last_5 | -0.163 | 0.099 | -0.052 |
| home_team_home_goals_avg | 0.203 | -0.268 | -0.052 |
| away_rest_days | 0.056 | -0.119 | -0.049 |
| points_difference | 0.409 | -0.353 | 0.046 |
| home_team_points_last_5 | 0.224 | -0.268 | -0.035 |
| home_rest_days | 0.094 | -0.139 | -0.034 |
| home_points_before_match | 0.254 | -0.231 | 0.019 |
| away_points_before_match | -0.091 | 0.067 | -0.019 |
| position_difference | -0.382 | 0.406 | 0.019 |
| away_team_away_conceded_avg | 0.017 | -0.001 | 0.013 |
| away_team_points_last_5 | -0.120 | 0.128 | 0.007 |
| home_team_goals_scored_last_5 | 0.271 | -0.278 | -0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 27 | 2 | 8 | 17 | 7.4% | 29.6% | 63.0% |
| -4..-2 | 27 | 8 | 4 | 15 | 29.6% | 14.8% | 55.6% |
| -1..1 | 46 | 19 | 8 | 19 | 41.3% | 17.4% | 41.3% |
| 2..4 | 22 | 13 | 3 | 6 | 59.1% | 13.6% | 27.3% |
| >4 | 31 | 20 | 5 | 6 | 64.5% | 16.1% | 19.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 18 | 14 | 4 | 0 | 77.8% | 22.2% | 0.0% |
| -5..-2 | 42 | 23 | 7 | 12 | 54.8% | 16.7% | 28.6% |
| -1..1 | 31 | 15 | 3 | 13 | 48.4% | 9.7% | 41.9% |
| 2..5 | 47 | 10 | 11 | 26 | 21.3% | 23.4% | 55.3% |
| >=6 | 15 | 0 | 3 | 12 | 0.0% | 20.0% | 80.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 4 | 1 | 1 | 2 | 25.0% | 25.0% | 50.0% |
| -1..0 | 15 | 6 | 4 | 5 | 40.0% | 26.7% | 33.3% |
| 0 | 96 | 36 | 17 | 43 | 37.5% | 17.7% | 44.8% |
| 1..2 | 24 | 11 | 4 | 9 | 45.8% | 16.7% | 37.5% |
| >2 | 2 | 1 | 1 | 0 | 50.0% | 50.0% | 0.0% |
| unknown | 12 | 7 | 1 | 4 | 58.3% | 8.3% | 33.3% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.9%** home win (21/62)
- `>= 0.5` tier: **45.1%** home win (41/91)
- Home-win gap (>= split minus < split): **+11.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 62 | 21 | 8 | 33 | 33.9% |
| high | >= 0.5 | 91 | 41 | 20 | 30 | 45.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 6.645 | -1.964 | -5.317 | 11.963 |
| away_points_before_match | 10.468 | 15.607 | 16.524 | 6.056 |
| home_points_before_match | 17.113 | 13.643 | 11.206 | 5.907 |
| position_difference | -2.597 | -0.071 | 2.333 | 4.930 |
| home_position_before_match | 4.613 | 6.857 | 7.524 | 2.911 |
| home_team_goals_scored_last_5 | 7.774 | 5.000 | 4.952 | 2.822 |
| home_rest_days | 12.436 | 9.667 | 10.610 | 2.770 |
| home_team_goals_conceded_last_5 | 4.290 | 6.750 | 6.937 | 2.646 |
| away_rest_days | 12.164 | 9.593 | 10.695 | 2.571 |
| away_team_points_last_5 | 4.516 | 5.929 | 6.698 | 2.182 |
| home_team_points_last_5 | 6.839 | 5.000 | 4.730 | 2.109 |
| away_team_goals_scored_last_5 | 4.903 | 6.321 | 6.968 | 2.065 |
| away_position_before_match | 7.210 | 6.929 | 5.190 | 2.019 |
| away_team_goals_conceded_last_5 | 6.355 | 6.500 | 5.270 | 1.230 |
| away_team_wins_last_5 | 1.935 | 2.357 | 2.794 | 0.858 |
| away_team_away_goals_avg | 1.093 | 1.443 | 1.731 | 0.638 |
| home_team_home_conceded_avg | 0.965 | 1.544 | 1.553 | 0.588 |
| home_team_home_goals_avg | 1.727 | 1.254 | 1.145 | 0.583 |
| home_team_wins_last_5 | 2.677 | 2.214 | 2.159 | 0.519 |
| rest_days_difference | 0.273 | 0.074 | -0.085 | 0.357 |
| away_team_away_win_rate | 0.398 | 0.456 | 0.562 | 0.164 |
| away_team_away_conceded_avg | 1.309 | 1.433 | 1.451 | 0.142 |
| home_team_home_win_rate | 0.590 | 0.495 | 0.457 | 0.134 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\wfrance1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\wfrance1\charts\relationships_home_win_pct_by_position.png)

