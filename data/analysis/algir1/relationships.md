# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:54:31+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Ligue 1 (Algeria)
- Scope: league `algir1`

- Matches analysed: **262** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_rest_days | 0.202 | 0.184 | 0.261 |
| away_team_goals_conceded_last_5 | 0.202 | 0.024 | 0.160 |
| rest_days_difference | -0.165 | -0.062 | -0.157 |
| home_team_goals_conceded_last_5 | -0.022 | 0.243 | 0.133 |
| away_team_away_conceded_avg | 0.143 | 0.013 | 0.111 |
| home_points_before_match | 0.162 | -0.040 | 0.092 |
| away_points_before_match | 0.017 | 0.104 | 0.076 |
| home_rest_days | 0.011 | 0.100 | 0.070 |
| away_position_before_match | 0.195 | -0.119 | 0.068 |
| home_position_before_match | -0.029 | 0.129 | 0.059 |
| away_team_wins_last_5 | -0.100 | 0.033 | -0.052 |
| away_team_points_last_5 | -0.101 | 0.037 | -0.050 |
| home_team_home_conceded_avg | 0.038 | 0.035 | 0.049 |
| home_team_home_win_rate | -0.009 | -0.059 | -0.042 |
| away_team_away_win_rate | -0.105 | 0.056 | -0.041 |
| home_team_home_goals_avg | 0.022 | -0.079 | -0.032 |
| home_team_goals_scored_last_5 | 0.066 | -0.025 | 0.032 |
| points_difference | 0.220 | -0.219 | 0.024 |
| away_team_away_goals_avg | -0.042 | 0.030 | -0.011 |
| home_team_points_last_5 | 0.099 | -0.128 | -0.007 |
| position_difference | -0.162 | 0.179 | -0.007 |
| away_team_goals_scored_last_5 | -0.031 | 0.031 | -0.004 |
| home_team_wins_last_5 | 0.069 | -0.082 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 44 | 14 | 18 | 12 | 31.8% | 40.9% | 27.3% |
| -4..-2 | 49 | 25 | 10 | 14 | 51.0% | 20.4% | 28.6% |
| -1..1 | 103 | 45 | 35 | 23 | 43.7% | 34.0% | 22.3% |
| 2..4 | 41 | 30 | 10 | 1 | 73.2% | 24.4% | 2.4% |
| >4 | 25 | 16 | 4 | 5 | 64.0% | 16.0% | 20.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 48 | 31 | 12 | 5 | 64.6% | 25.0% | 10.4% |
| -5..-2 | 50 | 26 | 19 | 5 | 52.0% | 38.0% | 10.0% |
| -1..1 | 45 | 23 | 13 | 9 | 51.1% | 28.9% | 20.0% |
| 2..5 | 58 | 28 | 15 | 15 | 48.3% | 25.9% | 25.9% |
| >=6 | 61 | 22 | 18 | 21 | 36.1% | 29.5% | 34.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 43 | 23 | 11 | 9 | 53.5% | 25.6% | 20.9% |
| -1..0 | 39 | 26 | 7 | 6 | 66.7% | 17.9% | 15.4% |
| 0 | 71 | 34 | 20 | 17 | 47.9% | 28.2% | 23.9% |
| 1..2 | 45 | 20 | 15 | 10 | 44.4% | 33.3% | 22.2% |
| >2 | 43 | 20 | 14 | 9 | 46.5% | 32.6% | 20.9% |
| unknown | 21 | 7 | 10 | 4 | 33.3% | 47.6% | 19.0% |
- *21 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **46.2%** home win (24/52)
- `>= 0.5` tier: **50.5%** home win (106/210)
- Home-win gap (>= split minus < split): **+4.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 52 | 24 | 16 | 12 | 46.2% |
| high | >= 0.5 | 210 | 106 | 61 | 43 | 50.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.600 | -1.130 | -4.745 | 6.345 |
| home_points_before_match | 20.054 | 16.597 | 14.636 | 5.417 |
| position_difference | -0.577 | 0.675 | 3.164 | 3.741 |
| away_position_before_match | 9.177 | 7.883 | 6.891 | 2.286 |
| away_points_before_match | 18.454 | 17.727 | 19.382 | 1.655 |
| home_team_points_last_5 | 6.023 | 5.000 | 4.509 | 1.514 |
| home_position_before_match | 8.600 | 8.558 | 10.055 | 1.496 |
| rest_days_difference | 0.024 | 1.493 | 0.725 | 1.468 |
| away_rest_days | 9.833 | 8.507 | 9.608 | 1.326 |
| home_team_goals_conceded_last_5 | 4.662 | 4.455 | 5.727 | 1.273 |
| away_team_goals_conceded_last_5 | 4.985 | 3.961 | 4.109 | 1.024 |
| away_team_points_last_5 | 5.708 | 6.286 | 6.455 | 0.747 |
| home_team_goals_scored_last_5 | 4.823 | 4.182 | 4.291 | 0.641 |
| home_rest_days | 9.927 | 9.957 | 10.333 | 0.406 |
| home_team_wins_last_5 | 2.792 | 2.403 | 2.473 | 0.390 |
| away_team_goals_scored_last_5 | 4.762 | 4.857 | 5.091 | 0.329 |
| away_team_wins_last_5 | 2.723 | 2.857 | 3.000 | 0.277 |
| home_team_home_goals_avg | 1.104 | 1.020 | 0.954 | 0.149 |
| away_team_away_conceded_avg | 1.085 | 0.939 | 0.943 | 0.146 |
| home_team_home_conceded_avg | 0.767 | 0.671 | 0.788 | 0.117 |
| away_team_away_win_rate | 0.465 | 0.502 | 0.558 | 0.093 |
| home_team_home_win_rate | 0.711 | 0.684 | 0.651 | 0.061 |
| away_team_away_goals_avg | 0.732 | 0.787 | 0.765 | 0.055 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\algir1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\algir1\charts\relationships_home_win_pct_by_position.png)

