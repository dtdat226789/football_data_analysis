# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:47:02+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Mozzart Bet Super Liga (Serbia)
- Scope: league `serbia1`

- Matches analysed: **365** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.260 | 0.113 | -0.114 |
| home_team_goals_conceded_last_5 | -0.207 | 0.065 | -0.108 |
| home_team_home_goals_avg | 0.214 | -0.074 | 0.107 |
| home_team_home_win_rate | 0.139 | -0.006 | 0.098 |
| home_team_goals_scored_last_5 | 0.163 | -0.049 | 0.086 |
| points_difference | 0.285 | -0.180 | 0.086 |
| position_difference | -0.274 | 0.174 | -0.082 |
| home_team_home_conceded_avg | -0.192 | 0.090 | -0.080 |
| rest_days_difference | -0.004 | -0.094 | -0.067 |
| away_points_before_match | -0.137 | 0.059 | -0.060 |
| away_team_away_goals_avg | -0.091 | 0.174 | 0.052 |
| home_team_points_last_5 | 0.142 | -0.082 | 0.049 |
| home_team_wins_last_5 | 0.093 | -0.032 | 0.047 |
| away_team_goals_scored_last_5 | -0.080 | 0.146 | 0.041 |
| away_team_wins_last_5 | -0.119 | 0.074 | -0.037 |
| home_rest_days | -0.040 | -0.003 | -0.031 |
| away_team_away_win_rate | -0.056 | 0.086 | 0.018 |
| away_team_points_last_5 | -0.105 | 0.134 | 0.014 |
| away_position_before_match | 0.093 | -0.112 | -0.008 |
| away_rest_days | -0.038 | 0.029 | -0.008 |
| away_team_goals_conceded_last_5 | 0.087 | -0.083 | 0.007 |
| away_team_away_conceded_avg | -0.027 | 0.022 | -0.004 |
| home_points_before_match | 0.060 | -0.064 | 0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 49 | 11 | 16 | 22 | 22.4% | 32.7% | 44.9% |
| -4..-2 | 79 | 30 | 22 | 27 | 38.0% | 27.8% | 34.2% |
| -1..1 | 111 | 52 | 29 | 30 | 46.8% | 26.1% | 27.0% |
| 2..4 | 73 | 33 | 22 | 18 | 45.2% | 30.1% | 24.7% |
| >4 | 53 | 33 | 15 | 5 | 62.3% | 28.3% | 9.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 61 | 38 | 15 | 8 | 62.3% | 24.6% | 13.1% |
| -5..-2 | 83 | 37 | 27 | 19 | 44.6% | 32.5% | 22.9% |
| -1..1 | 76 | 40 | 23 | 13 | 52.6% | 30.3% | 17.1% |
| 2..5 | 76 | 32 | 17 | 27 | 42.1% | 22.4% | 35.5% |
| >=6 | 69 | 12 | 22 | 35 | 17.4% | 31.9% | 50.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 25 | 11 | 6 | 8 | 44.0% | 24.0% | 32.0% |
| -1..0 | 77 | 27 | 28 | 22 | 35.1% | 36.4% | 28.6% |
| 0 | 135 | 61 | 38 | 36 | 45.2% | 28.1% | 26.7% |
| 1..2 | 95 | 45 | 23 | 27 | 47.4% | 24.2% | 28.4% |
| >2 | 17 | 7 | 4 | 6 | 41.2% | 23.5% | 35.3% |
| unknown | 16 | 8 | 5 | 3 | 50.0% | 31.2% | 18.8% |
- *16 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **30.7%** home win (23/75)
- `>= 0.5` tier: **46.9%** home win (136/290)
- Home-win gap (>= split minus < split): **+16.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 75 | 23 | 22 | 30 | 30.7% |
| high | >= 0.5 | 290 | 136 | 82 | 72 | 46.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.409 | -1.058 | -5.245 | 9.654 |
| away_points_before_match | 17.107 | 24.115 | 24.853 | 7.746 |
| position_difference | -1.648 | 0.433 | 2.539 | 4.187 |
| home_points_before_match | 21.516 | 23.058 | 19.608 | 3.450 |
| home_position_before_match | 7.491 | 8.981 | 9.725 | 2.235 |
| away_position_before_match | 9.138 | 8.548 | 7.186 | 1.952 |
| away_team_points_last_5 | 5.440 | 5.846 | 6.980 | 1.540 |
| away_team_goals_scored_last_5 | 5.252 | 5.615 | 6.735 | 1.484 |
| away_team_goals_conceded_last_5 | 6.182 | 5.673 | 5.000 | 1.182 |
| home_team_goals_scored_last_5 | 6.384 | 5.240 | 5.569 | 1.143 |
| home_team_points_last_5 | 6.528 | 5.731 | 5.431 | 1.097 |
| home_team_goals_conceded_last_5 | 5.434 | 5.885 | 6.490 | 1.056 |
| away_rest_days | 7.901 | 8.500 | 8.525 | 0.625 |
| home_rest_days | 8.000 | 8.480 | 8.556 | 0.556 |
| away_team_wins_last_5 | 2.610 | 2.808 | 3.078 | 0.468 |
| away_team_away_goals_avg | 0.942 | 1.085 | 1.352 | 0.410 |
| home_team_home_goals_avg | 1.665 | 1.274 | 1.354 | 0.391 |
| home_team_home_conceded_avg | 0.961 | 1.076 | 1.230 | 0.269 |
| home_team_wins_last_5 | 2.881 | 2.788 | 2.667 | 0.214 |
| rest_days_difference | 0.099 | -0.030 | 0.030 | 0.130 |
| away_team_away_win_rate | 0.476 | 0.472 | 0.569 | 0.097 |
| home_team_home_win_rate | 0.708 | 0.641 | 0.627 | 0.080 |
| away_team_away_conceded_avg | 1.478 | 1.416 | 1.434 | 0.062 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\serbia1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\serbia1\charts\relationships_home_win_pct_by_position.png)

