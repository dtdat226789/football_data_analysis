# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:05:08+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Premier League (Russia)
- Scope: league `russia`

- Matches analysed: **244** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.232 | 0.054 | 0.211 |
| home_team_wins_last_5 | 0.266 | -0.053 | 0.162 |
| home_team_points_last_5 | 0.259 | -0.073 | 0.143 |
| points_difference | 0.311 | -0.169 | 0.115 |
| home_position_before_match | -0.259 | 0.113 | -0.115 |
| home_team_home_goals_avg | 0.245 | -0.105 | 0.110 |
| position_difference | -0.344 | 0.221 | -0.104 |
| home_team_home_win_rate | 0.227 | -0.115 | 0.090 |
| away_points_before_match | -0.138 | 0.021 | -0.089 |
| away_team_away_win_rate | -0.047 | 0.138 | 0.061 |
| away_team_goals_conceded_last_5 | 0.192 | -0.136 | 0.049 |
| away_position_before_match | 0.229 | -0.201 | 0.031 |
| away_rest_days | 0.081 | -0.042 | 0.031 |
| away_team_away_conceded_avg | 0.206 | -0.179 | 0.029 |
| home_rest_days | 0.080 | -0.046 | 0.027 |
| home_team_home_conceded_avg | -0.008 | -0.027 | -0.025 |
| away_team_goals_scored_last_5 | -0.073 | 0.106 | 0.019 |
| home_team_goals_conceded_last_5 | -0.077 | 0.057 | -0.018 |
| rest_days_difference | 0.051 | -0.076 | -0.015 |
| away_team_wins_last_5 | -0.071 | 0.095 | 0.013 |
| away_team_points_last_5 | -0.087 | 0.111 | 0.013 |
| home_points_before_match | 0.135 | -0.129 | 0.011 |
| away_team_away_goals_avg | -0.062 | 0.078 | 0.008 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 43 | 13 | 10 | 20 | 30.2% | 23.3% | 46.5% |
| -4..-2 | 51 | 16 | 19 | 16 | 31.4% | 37.3% | 31.4% |
| -1..1 | 72 | 31 | 22 | 19 | 43.1% | 30.6% | 26.4% |
| 2..4 | 41 | 25 | 11 | 5 | 61.0% | 26.8% | 12.2% |
| >4 | 37 | 25 | 5 | 7 | 67.6% | 13.5% | 18.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 56 | 38 | 10 | 8 | 67.9% | 17.9% | 14.3% |
| -5..-2 | 45 | 26 | 12 | 7 | 57.8% | 26.7% | 15.6% |
| -1..1 | 35 | 17 | 12 | 6 | 48.6% | 34.3% | 17.1% |
| 2..5 | 55 | 18 | 15 | 22 | 32.7% | 27.3% | 40.0% |
| >=6 | 53 | 11 | 18 | 24 | 20.8% | 34.0% | 45.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 8 | 3 | 3 | 2 | 37.5% | 37.5% | 25.0% |
| -1..0 | 54 | 24 | 10 | 20 | 44.4% | 18.5% | 37.0% |
| 0 | 93 | 40 | 31 | 22 | 43.0% | 33.3% | 23.7% |
| 1..2 | 79 | 40 | 20 | 19 | 50.6% | 25.3% | 24.1% |
| >2 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 10 | 3 | 3 | 4 | 30.0% | 30.0% | 40.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **36.4%** home win (47/129)
- `>= 0.5` tier: **54.8%** home win (63/115)
- Home-win gap (>= split minus < split): **+18.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 129 | 47 | 33 | 49 | 36.4% |
| high | >= 0.5 | 115 | 63 | 34 | 18 | 54.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.055 | -1.597 | -6.179 | 10.234 |
| position_difference | -2.518 | 0.970 | 3.463 | 5.981 |
| away_points_before_match | 17.473 | 20.254 | 22.896 | 5.423 |
| home_rest_days | 12.692 | 7.828 | 9.048 | 4.863 |
| away_rest_days | 12.542 | 7.703 | 8.892 | 4.839 |
| home_points_before_match | 21.527 | 18.657 | 16.716 | 4.811 |
| home_position_before_match | 7.782 | 8.746 | 11.075 | 3.293 |
| away_position_before_match | 10.300 | 7.776 | 7.612 | 2.688 |
| home_team_points_last_5 | 6.718 | 5.851 | 4.657 | 2.061 |
| away_team_goals_conceded_last_5 | 6.227 | 5.448 | 4.821 | 1.406 |
| home_team_goals_conceded_last_5 | 5.200 | 5.896 | 6.597 | 1.397 |
| away_team_goals_scored_last_5 | 5.100 | 6.493 | 6.045 | 1.393 |
| away_team_points_last_5 | 5.555 | 6.776 | 6.612 | 1.222 |
| home_team_goals_scored_last_5 | 5.864 | 5.627 | 5.149 | 0.714 |
| home_team_wins_last_5 | 1.800 | 1.567 | 1.104 | 0.696 |
| home_team_home_goals_avg | 1.501 | 1.342 | 1.052 | 0.450 |
| away_team_wins_last_5 | 1.455 | 1.881 | 1.701 | 0.426 |
| away_team_away_conceded_avg | 1.544 | 1.214 | 1.165 | 0.379 |
| rest_days_difference | 0.150 | 0.125 | -0.032 | 0.181 |
| home_team_home_win_rate | 0.477 | 0.440 | 0.299 | 0.178 |
| away_team_away_goals_avg | 1.011 | 1.156 | 1.170 | 0.159 |
| away_team_away_win_rate | 0.194 | 0.263 | 0.262 | 0.069 |
| home_team_home_conceded_avg | 1.082 | 1.094 | 1.136 | 0.053 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\russia\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\russia\charts\relationships_home_win_pct_by_position.png)

