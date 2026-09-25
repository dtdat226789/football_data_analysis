# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:49:12+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super League (Switzerland)
- Scope: league `swiss1`

- Matches analysed: **284** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_points_before_match | -0.136 | 0.012 | -0.095 |
| points_difference | 0.262 | -0.153 | 0.088 |
| home_team_wins_last_5 | 0.047 | -0.151 | -0.074 |
| away_team_goals_conceded_last_5 | 0.062 | -0.154 | -0.065 |
| home_team_points_last_5 | 0.054 | -0.112 | -0.040 |
| home_points_before_match | 0.034 | -0.089 | -0.039 |
| rest_days_difference | -0.066 | 0.119 | 0.037 |
| home_team_home_conceded_avg | 0.000 | 0.050 | 0.037 |
| home_team_goals_scored_last_5 | 0.086 | -0.051 | 0.029 |
| away_team_goals_scored_last_5 | -0.104 | 0.072 | -0.027 |
| away_team_wins_last_5 | -0.157 | 0.128 | -0.026 |
| home_team_home_goals_avg | 0.044 | -0.020 | 0.019 |
| away_rest_days | -0.004 | -0.021 | -0.018 |
| away_position_before_match | 0.204 | -0.193 | 0.015 |
| position_difference | -0.232 | 0.225 | -0.013 |
| away_team_away_goals_avg | -0.070 | 0.092 | 0.013 |
| away_team_away_win_rate | -0.095 | 0.085 | -0.010 |
| away_team_away_conceded_avg | 0.108 | -0.108 | 0.004 |
| away_team_points_last_5 | -0.156 | 0.159 | -0.004 |
| home_team_home_win_rate | 0.053 | -0.059 | -0.003 |
| home_position_before_match | -0.108 | 0.109 | -0.003 |
| home_rest_days | -0.055 | 0.061 | 0.002 |
| home_team_goals_conceded_last_5 | -0.078 | 0.079 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 41 | 12 | 7 | 22 | 29.3% | 17.1% | 53.7% |
| -4..-2 | 67 | 17 | 21 | 29 | 25.4% | 31.3% | 43.3% |
| -1..1 | 71 | 33 | 13 | 25 | 46.5% | 18.3% | 35.2% |
| 2..4 | 62 | 29 | 15 | 18 | 46.8% | 24.2% | 29.0% |
| >4 | 43 | 23 | 11 | 9 | 53.5% | 25.6% | 20.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 35 | 24 | 7 | 4 | 68.6% | 20.0% | 11.4% |
| -5..-2 | 77 | 39 | 17 | 21 | 50.6% | 22.1% | 27.3% |
| -1..1 | 65 | 20 | 14 | 31 | 30.8% | 21.5% | 47.7% |
| 2..5 | 71 | 23 | 18 | 30 | 32.4% | 25.4% | 42.3% |
| >=6 | 36 | 8 | 11 | 17 | 22.2% | 30.6% | 47.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 16 | 6 | 5 | 5 | 37.5% | 31.2% | 31.2% |
| -1..0 | 61 | 30 | 18 | 13 | 49.2% | 29.5% | 21.3% |
| 0 | 117 | 50 | 18 | 49 | 42.7% | 15.4% | 41.9% |
| 1..2 | 60 | 19 | 18 | 23 | 31.7% | 30.0% | 38.3% |
| >2 | 17 | 3 | 6 | 8 | 17.6% | 35.3% | 47.1% |
| unknown | 13 | 6 | 2 | 5 | 46.2% | 15.4% | 38.5% |
- *13 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **43.8%** home win (32/73)
- `>= 0.5` tier: **38.9%** home win (82/211)
- Home-win gap (>= split minus < split): **-4.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 73 | 32 | 13 | 28 | 43.8% |
| high | >= 0.5 | 211 | 82 | 54 | 75 | 38.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.658 | -1.373 | -3.330 | 6.988 |
| away_points_before_match | 19.640 | 24.000 | 22.466 | 4.360 |
| home_points_before_match | 23.298 | 22.627 | 19.136 | 4.162 |
| position_difference | -1.500 | 0.388 | 1.447 | 2.947 |
| away_position_before_match | 7.605 | 6.269 | 5.641 | 1.964 |
| away_team_points_last_5 | 5.035 | 6.448 | 6.748 | 1.712 |
| home_rest_days | 7.463 | 7.369 | 8.745 | 1.376 |
| away_team_goals_scored_last_5 | 6.535 | 7.866 | 7.563 | 1.331 |
| away_rest_days | 7.713 | 6.864 | 8.000 | 1.136 |
| away_team_goals_conceded_last_5 | 7.754 | 7.343 | 6.718 | 1.036 |
| rest_days_difference | -0.250 | 0.431 | 0.745 | 0.995 |
| home_position_before_match | 6.105 | 6.657 | 7.087 | 0.982 |
| home_team_points_last_5 | 6.132 | 6.537 | 5.583 | 0.955 |
| home_team_goals_conceded_last_5 | 6.772 | 7.239 | 7.709 | 0.937 |
| home_team_goals_scored_last_5 | 7.377 | 7.761 | 6.864 | 0.897 |
| away_team_wins_last_5 | 2.333 | 2.896 | 2.883 | 0.562 |
| home_team_wins_last_5 | 2.833 | 2.896 | 2.495 | 0.400 |
| away_team_away_goals_avg | 1.258 | 1.525 | 1.491 | 0.267 |
| away_team_away_conceded_avg | 1.737 | 1.707 | 1.556 | 0.181 |
| home_team_home_conceded_avg | 1.357 | 1.490 | 1.430 | 0.133 |
| away_team_away_win_rate | 0.473 | 0.575 | 0.560 | 0.103 |
| home_team_home_goals_avg | 1.646 | 1.700 | 1.667 | 0.053 |
| home_team_home_win_rate | 0.570 | 0.588 | 0.580 | 0.019 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\swiss1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\swiss1\charts\relationships_home_win_pct_by_position.png)

