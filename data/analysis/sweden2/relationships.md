# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:09:39+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Superettan (Sweden)
- Scope: league `sweden2`

- Matches analysed: **240** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| points_difference | 0.279 | -0.078 | 0.168 |
| home_team_points_last_5 | 0.197 | -0.005 | 0.152 |
| home_team_wins_last_5 | 0.181 | 0.011 | 0.151 |
| away_team_away_conceded_avg | 0.154 | 0.020 | 0.134 |
| rest_days_difference | 0.230 | -0.073 | 0.133 |
| home_team_goals_conceded_last_5 | -0.134 | -0.030 | -0.126 |
| away_team_goals_scored_last_5 | -0.023 | 0.203 | 0.118 |
| position_difference | -0.258 | 0.137 | -0.111 |
| away_position_before_match | 0.203 | -0.089 | 0.100 |
| home_points_before_match | 0.168 | -0.055 | 0.095 |
| away_team_away_win_rate | -0.076 | -0.041 | -0.087 |
| home_team_home_win_rate | 0.166 | -0.083 | 0.074 |
| away_team_goals_conceded_last_5 | 0.118 | -0.030 | 0.072 |
| home_team_goals_scored_last_5 | 0.148 | -0.083 | 0.061 |
| away_team_away_goals_avg | -0.125 | 0.057 | -0.061 |
| home_team_home_goals_avg | 0.163 | -0.105 | 0.057 |
| home_position_before_match | -0.150 | 0.099 | -0.051 |
| away_points_before_match | -0.055 | 0.007 | -0.038 |
| away_rest_days | -0.076 | 0.051 | -0.026 |
| home_team_home_conceded_avg | -0.021 | 0.051 | 0.018 |
| away_team_points_last_5 | -0.080 | 0.119 | 0.018 |
| home_rest_days | -0.003 | 0.028 | 0.016 |
| away_team_wins_last_5 | -0.085 | 0.090 | -0.007 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 44 | 13 | 12 | 19 | 29.5% | 27.3% | 43.2% |
| -4..-2 | 46 | 17 | 16 | 13 | 37.0% | 34.8% | 28.3% |
| -1..1 | 68 | 23 | 21 | 24 | 33.8% | 30.9% | 35.3% |
| 2..4 | 47 | 23 | 10 | 14 | 48.9% | 21.3% | 29.8% |
| >4 | 35 | 25 | 6 | 4 | 71.4% | 17.1% | 11.4% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 46 | 28 | 11 | 7 | 60.9% | 23.9% | 15.2% |
| -5..-2 | 48 | 25 | 11 | 12 | 52.1% | 22.9% | 25.0% |
| -1..1 | 52 | 18 | 16 | 18 | 34.6% | 30.8% | 34.6% |
| 2..5 | 46 | 16 | 14 | 16 | 34.8% | 30.4% | 34.8% |
| >=6 | 48 | 14 | 13 | 21 | 29.2% | 27.1% | 43.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 19 | 4 | 6 | 9 | 21.1% | 31.6% | 47.4% |
| -1..0 | 51 | 16 | 19 | 16 | 31.4% | 37.3% | 31.4% |
| 0 | 85 | 34 | 23 | 28 | 40.0% | 27.1% | 32.9% |
| 1..2 | 70 | 38 | 14 | 18 | 54.3% | 20.0% | 25.7% |
| >2 | 7 | 6 | 0 | 1 | 85.7% | 0.0% | 14.3% |
| unknown | 8 | 3 | 3 | 2 | 37.5% | 37.5% | 25.0% |
- *8 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.5%** home win (65/169)
- `>= 0.5` tier: **50.7%** home win (36/71)
- Home-win gap (>= split minus < split): **+12.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 169 | 65 | 50 | 54 | 38.5% |
| high | >= 0.5 | 71 | 36 | 15 | 20 | 50.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.604 | -2.677 | -3.703 | 7.307 |
| home_points_before_match | 22.436 | 16.477 | 18.014 | 5.959 |
| position_difference | -1.980 | 1.169 | 2.122 | 4.102 |
| away_points_before_match | 18.832 | 19.154 | 21.716 | 2.885 |
| away_position_before_match | 9.723 | 8.092 | 7.662 | 2.061 |
| home_position_before_match | 7.743 | 9.262 | 9.784 | 2.041 |
| home_team_goals_scored_last_5 | 6.812 | 6.138 | 5.527 | 1.285 |
| away_team_points_last_5 | 5.653 | 6.585 | 6.757 | 1.103 |
| home_team_points_last_5 | 6.604 | 5.692 | 5.527 | 1.077 |
| away_team_goals_scored_last_5 | 5.881 | 6.862 | 6.919 | 1.038 |
| home_rest_days | 7.878 | 7.048 | 8.083 | 1.035 |
| away_rest_days | 7.469 | 7.290 | 8.264 | 0.974 |
| away_team_goals_conceded_last_5 | 6.703 | 6.000 | 5.811 | 0.892 |
| home_team_goals_conceded_last_5 | 6.010 | 6.877 | 6.716 | 0.867 |
| rest_days_difference | 0.408 | -0.242 | -0.181 | 0.650 |
| home_team_wins_last_5 | 1.772 | 1.492 | 1.459 | 0.313 |
| away_team_wins_last_5 | 1.505 | 1.769 | 1.811 | 0.306 |
| home_team_home_goals_avg | 1.508 | 1.284 | 1.205 | 0.303 |
| away_team_away_conceded_avg | 1.481 | 1.232 | 1.296 | 0.249 |
| away_team_away_goals_avg | 1.114 | 1.230 | 1.291 | 0.177 |
| home_team_home_conceded_avg | 1.141 | 1.254 | 1.201 | 0.114 |
| home_team_home_win_rate | 0.413 | 0.316 | 0.316 | 0.097 |
| away_team_away_win_rate | 0.294 | 0.313 | 0.313 | 0.019 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\sweden2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\sweden2\charts\relationships_home_win_pct_by_position.png)

