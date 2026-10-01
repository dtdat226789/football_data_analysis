# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:54:46+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: NB II. (Hungary)
- Scope: league `hungary2`

- Matches analysed: **240** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_rest_days | 0.095 | 0.074 | 0.126 |
| home_rest_days | 0.068 | 0.096 | 0.120 |
| away_team_wins_last_5 | -0.120 | 0.036 | -0.071 |
| away_team_away_win_rate | -0.076 | -0.014 | -0.071 |
| home_team_goals_conceded_last_5 | -0.060 | -0.009 | -0.055 |
| away_team_goals_conceded_last_5 | -0.025 | -0.044 | -0.050 |
| points_difference | 0.132 | -0.081 | 0.050 |
| home_team_points_last_5 | 0.087 | -0.048 | 0.037 |
| rest_days_difference | -0.151 | 0.124 | -0.037 |
| away_team_away_conceded_avg | 0.009 | -0.061 | -0.035 |
| home_team_home_win_rate | 0.052 | -0.111 | -0.035 |
| away_team_points_last_5 | -0.079 | 0.045 | -0.033 |
| home_position_before_match | -0.133 | 0.107 | -0.032 |
| position_difference | -0.121 | 0.095 | -0.032 |
| away_points_before_match | -0.085 | 0.057 | -0.029 |
| home_team_wins_last_5 | 0.089 | -0.068 | 0.025 |
| away_team_away_goals_avg | -0.001 | -0.017 | -0.013 |
| away_position_before_match | 0.038 | -0.027 | 0.012 |
| home_team_home_goals_avg | 0.085 | -0.081 | 0.012 |
| away_team_goals_scored_last_5 | -0.038 | 0.028 | -0.011 |
| home_team_home_conceded_avg | 0.029 | -0.022 | 0.008 |
| home_points_before_match | 0.008 | 0.000 | 0.006 |
| home_team_goals_scored_last_5 | 0.050 | -0.052 | 0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 38 | 14 | 11 | 13 | 36.8% | 28.9% | 34.2% |
| -4..-2 | 52 | 17 | 16 | 19 | 32.7% | 30.8% | 36.5% |
| -1..1 | 74 | 36 | 17 | 21 | 48.6% | 23.0% | 28.4% |
| 2..4 | 46 | 21 | 12 | 13 | 45.7% | 26.1% | 28.3% |
| >4 | 30 | 17 | 4 | 9 | 56.7% | 13.3% | 30.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 49 | 27 | 8 | 14 | 55.1% | 16.3% | 28.6% |
| -5..-2 | 43 | 16 | 12 | 15 | 37.2% | 27.9% | 34.9% |
| -1..1 | 47 | 26 | 8 | 13 | 55.3% | 17.0% | 27.7% |
| 2..5 | 47 | 20 | 12 | 15 | 42.6% | 25.5% | 31.9% |
| >=6 | 54 | 16 | 20 | 18 | 29.6% | 37.0% | 33.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 6 | 5 | 0 | 1 | 83.3% | 0.0% | 16.7% |
| -1..0 | 20 | 12 | 3 | 5 | 60.0% | 15.0% | 25.0% |
| 0 | 180 | 80 | 48 | 52 | 44.4% | 26.7% | 28.9% |
| 1..2 | 23 | 5 | 7 | 11 | 21.7% | 30.4% | 47.8% |
| >2 | 3 | 0 | 0 | 3 | 0.0% | 0.0% | 100.0% |
| unknown | 8 | 3 | 2 | 3 | 37.5% | 25.0% | 37.5% |
- *8 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **39.3%** home win (55/140)
- `>= 0.5` tier: **50.0%** home win (50/100)
- Home-win gap (>= split minus < split): **+10.7 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 140 | 55 | 38 | 47 | 39.3% |
| high | >= 0.5 | 100 | 50 | 22 | 28 | 50.0% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_points_before_match | 19.743 | 16.567 | 21.947 | 5.380 |
| away_points_before_match | 18.381 | 18.350 | 23.293 | 4.943 |
| points_difference | 1.362 | -1.783 | -1.347 | 3.145 |
| position_difference | -1.038 | 1.617 | 0.733 | 2.655 |
| home_position_before_match | 7.848 | 9.767 | 9.067 | 1.919 |
| away_rest_days | 10.735 | 8.983 | 10.222 | 1.753 |
| home_rest_days | 10.363 | 9.052 | 10.667 | 1.615 |
| home_team_points_last_5 | 6.429 | 5.333 | 5.907 | 1.095 |
| home_team_goals_scored_last_5 | 6.038 | 5.133 | 5.373 | 0.905 |
| rest_days_difference | -0.373 | 0.069 | 0.444 | 0.817 |
| away_position_before_match | 8.886 | 8.150 | 8.333 | 0.736 |
| away_team_points_last_5 | 6.048 | 6.417 | 6.627 | 0.579 |
| home_team_goals_conceded_last_5 | 5.705 | 6.033 | 5.693 | 0.340 |
| home_team_wins_last_5 | 1.743 | 1.433 | 1.560 | 0.310 |
| away_team_wins_last_5 | 1.562 | 1.783 | 1.840 | 0.278 |
| home_team_home_goals_avg | 1.426 | 1.167 | 1.266 | 0.259 |
| away_team_goals_scored_last_5 | 5.600 | 5.800 | 5.760 | 0.200 |
| away_team_goals_conceded_last_5 | 5.448 | 5.617 | 5.547 | 0.169 |
| away_team_away_goals_avg | 1.096 | 1.141 | 1.024 | 0.117 |
| home_team_home_conceded_avg | 1.136 | 1.026 | 1.031 | 0.110 |
| home_team_home_win_rate | 0.463 | 0.383 | 0.416 | 0.080 |
| away_team_away_conceded_avg | 1.331 | 1.278 | 1.288 | 0.053 |
| away_team_away_win_rate | 0.247 | 0.235 | 0.259 | 0.024 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\hungary2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\hungary2\charts\relationships_home_win_pct_by_position.png)

