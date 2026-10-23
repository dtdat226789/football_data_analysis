# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:04:53+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Superliga (Romania)
- Scope: league `romania1`

- Matches analysed: **350** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_position_before_match | 0.251 | -0.062 | 0.158 |
| away_team_points_last_5 | -0.213 | 0.031 | -0.148 |
| away_team_wins_last_5 | -0.196 | 0.048 | -0.124 |
| away_team_goals_scored_last_5 | -0.146 | -0.006 | -0.118 |
| home_team_home_goals_avg | -0.003 | -0.175 | -0.112 |
| away_points_before_match | -0.094 | -0.059 | -0.111 |
| home_team_home_conceded_avg | -0.144 | 0.018 | -0.102 |
| away_team_away_goals_avg | -0.128 | 0.016 | -0.091 |
| home_position_before_match | -0.045 | 0.200 | 0.090 |
| away_team_away_win_rate | -0.149 | 0.047 | -0.088 |
| points_difference | 0.226 | -0.144 | 0.087 |
| away_team_goals_conceded_last_5 | 0.195 | -0.119 | 0.078 |
| home_team_points_last_5 | 0.115 | -0.266 | -0.077 |
| home_team_wins_last_5 | 0.120 | -0.264 | -0.072 |
| home_team_home_win_rate | 0.055 | -0.172 | -0.065 |
| home_team_goals_scored_last_5 | 0.087 | -0.199 | -0.057 |
| home_rest_days | -0.081 | 0.013 | -0.056 |
| away_team_away_conceded_avg | 0.138 | -0.083 | 0.056 |
| position_difference | -0.237 | 0.208 | -0.056 |
| rest_days_difference | -0.005 | -0.075 | -0.051 |
| home_points_before_match | 0.060 | -0.157 | -0.051 |
| home_team_goals_conceded_last_5 | -0.117 | 0.085 | -0.038 |
| away_rest_days | -0.082 | 0.060 | -0.027 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 60 | 17 | 12 | 31 | 28.3% | 20.0% | 51.7% |
| -4..-2 | 75 | 25 | 20 | 30 | 33.3% | 26.7% | 40.0% |
| -1..1 | 109 | 42 | 43 | 24 | 38.5% | 39.4% | 22.0% |
| 2..4 | 46 | 26 | 10 | 10 | 56.5% | 21.7% | 21.7% |
| >4 | 60 | 45 | 11 | 4 | 75.0% | 18.3% | 6.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 58 | 38 | 13 | 7 | 65.5% | 22.4% | 12.1% |
| -5..-2 | 92 | 51 | 21 | 20 | 55.4% | 22.8% | 21.7% |
| -1..1 | 57 | 15 | 24 | 18 | 26.3% | 42.1% | 31.6% |
| 2..5 | 84 | 34 | 26 | 24 | 40.5% | 31.0% | 28.6% |
| >=6 | 59 | 17 | 12 | 30 | 28.8% | 20.3% | 50.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 60 | 25 | 13 | 22 | 41.7% | 21.7% | 36.7% |
| -1..0 | 77 | 35 | 22 | 20 | 45.5% | 28.6% | 26.0% |
| 0 | 55 | 28 | 14 | 13 | 50.9% | 25.5% | 23.6% |
| 1..2 | 124 | 56 | 34 | 34 | 45.2% | 27.4% | 27.4% |
| >2 | 23 | 9 | 6 | 8 | 39.1% | 26.1% | 34.8% |
| unknown | 11 | 2 | 7 | 2 | 18.2% | 63.6% | 18.2% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **43.0%** home win (89/207)
- `>= 0.5` tier: **46.2%** home win (66/143)
- Home-win gap (>= split minus < split): **+3.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 207 | 89 | 50 | 68 | 43.0% |
| high | >= 0.5 | 143 | 66 | 46 | 31 | 46.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.310 | -0.156 | -4.162 | 7.471 |
| home_points_before_match | 30.174 | 25.052 | 23.909 | 6.265 |
| position_difference | -1.748 | 0.083 | 2.475 | 4.223 |
| away_points_before_match | 26.865 | 25.208 | 28.071 | 2.862 |
| away_position_before_match | 10.471 | 8.969 | 7.970 | 2.501 |
| home_team_points_last_5 | 7.129 | 6.042 | 4.899 | 2.230 |
| away_team_points_last_5 | 5.781 | 6.302 | 7.586 | 1.805 |
| home_position_before_match | 8.723 | 9.052 | 10.444 | 1.722 |
| home_team_goals_scored_last_5 | 6.406 | 5.500 | 4.949 | 1.457 |
| home_team_goals_conceded_last_5 | 5.684 | 5.396 | 6.768 | 1.372 |
| away_team_goals_conceded_last_5 | 6.277 | 5.344 | 5.131 | 1.146 |
| away_team_goals_scored_last_5 | 5.516 | 5.906 | 6.535 | 1.019 |
| home_team_wins_last_5 | 1.974 | 1.604 | 1.202 | 0.772 |
| away_team_wins_last_5 | 1.523 | 1.719 | 2.131 | 0.609 |
| away_rest_days | 7.647 | 7.867 | 8.072 | 0.425 |
| away_team_away_conceded_avg | 1.460 | 1.231 | 1.343 | 0.229 |
| rest_days_difference | 0.307 | 0.112 | 0.082 | 0.225 |
| home_rest_days | 7.942 | 8.011 | 8.155 | 0.213 |
| home_team_home_goals_avg | 1.438 | 1.300 | 1.238 | 0.200 |
| home_team_home_conceded_avg | 1.081 | 1.037 | 1.224 | 0.188 |
| away_team_away_goals_avg | 1.082 | 1.070 | 1.217 | 0.147 |
| home_team_home_win_rate | 0.405 | 0.368 | 0.326 | 0.080 |
| away_team_away_win_rate | 0.245 | 0.270 | 0.294 | 0.048 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\romania1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\romania1\charts\relationships_home_win_pct_by_position.png)

