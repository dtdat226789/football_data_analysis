# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:00:45+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: K League 2 (South Korea)
- Scope: league `korea2`

- Matches analysed: **273** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_points_last_5 | 0.194 | -0.007 | 0.141 |
| home_team_wins_last_5 | 0.170 | -0.003 | 0.125 |
| home_team_goals_scored_last_5 | 0.140 | 0.022 | 0.118 |
| away_team_points_last_5 | -0.080 | 0.266 | 0.107 |
| away_team_goals_scored_last_5 | -0.065 | 0.238 | 0.100 |
| away_team_wins_last_5 | -0.072 | 0.238 | 0.095 |
| home_position_before_match | -0.212 | 0.102 | -0.095 |
| home_team_home_win_rate | 0.149 | -0.061 | 0.073 |
| home_team_home_conceded_avg | -0.170 | 0.087 | -0.073 |
| away_team_away_win_rate | -0.026 | 0.146 | 0.072 |
| away_position_before_match | 0.129 | -0.268 | -0.071 |
| home_rest_days | 0.096 | -0.004 | 0.069 |
| away_rest_days | 0.122 | -0.038 | 0.067 |
| away_team_away_goals_avg | -0.063 | 0.171 | 0.060 |
| home_team_goals_conceded_last_5 | -0.129 | 0.060 | -0.059 |
| home_team_home_goals_avg | 0.107 | -0.035 | 0.058 |
| home_points_before_match | 0.090 | -0.057 | 0.032 |
| away_points_before_match | -0.086 | 0.137 | 0.021 |
| away_team_away_conceded_avg | 0.075 | -0.061 | 0.018 |
| position_difference | -0.234 | 0.256 | -0.016 |
| points_difference | 0.217 | -0.238 | 0.013 |
| rest_days_difference | -0.086 | 0.113 | 0.006 |
| away_team_goals_conceded_last_5 | 0.094 | -0.104 | 0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 38 | 3 | 17 | 18 | 7.9% | 44.7% | 47.4% |
| -4..-2 | 60 | 16 | 19 | 25 | 26.7% | 31.7% | 41.7% |
| -1..1 | 75 | 30 | 20 | 25 | 40.0% | 26.7% | 33.3% |
| 2..4 | 55 | 22 | 12 | 21 | 40.0% | 21.8% | 38.2% |
| >4 | 45 | 25 | 12 | 8 | 55.6% | 26.7% | 17.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 52 | 26 | 14 | 12 | 50.0% | 26.9% | 23.1% |
| -5..-2 | 59 | 25 | 21 | 13 | 42.4% | 35.6% | 22.0% |
| -1..1 | 46 | 18 | 15 | 13 | 39.1% | 32.6% | 28.3% |
| 2..5 | 65 | 21 | 14 | 30 | 32.3% | 21.5% | 46.2% |
| >=6 | 51 | 6 | 16 | 29 | 11.8% | 31.4% | 56.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 1 | 1 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| -1..0 | 33 | 16 | 10 | 7 | 48.5% | 30.3% | 21.2% |
| 0 | 190 | 65 | 59 | 66 | 34.2% | 31.1% | 34.7% |
| 1..2 | 42 | 10 | 10 | 22 | 23.8% | 23.8% | 52.4% |
| >2 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 7 | 4 | 1 | 2 | 57.1% | 14.3% | 28.6% |
- *7 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **31.4%** home win (59/188)
- `>= 0.5` tier: **43.5%** home win (37/85)
- Home-win gap (>= split minus < split): **+12.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 188 | 59 | 55 | 74 | 31.4% |
| high | >= 0.5 | 85 | 37 | 25 | 23 | 43.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.698 | -0.200 | -4.670 | 9.368 |
| away_points_before_match | 21.708 | 27.325 | 28.784 | 7.075 |
| position_difference | -2.146 | 0.175 | 2.216 | 4.362 |
| home_points_before_match | 26.406 | 27.125 | 24.113 | 3.012 |
| away_position_before_match | 8.698 | 7.400 | 6.495 | 2.203 |
| home_position_before_match | 6.552 | 7.575 | 8.711 | 2.159 |
| away_team_points_last_5 | 5.021 | 6.775 | 6.742 | 1.754 |
| away_team_goals_scored_last_5 | 5.021 | 6.138 | 6.381 | 1.361 |
| home_team_points_last_5 | 6.906 | 6.225 | 5.876 | 1.030 |
| home_team_goals_conceded_last_5 | 5.333 | 5.688 | 6.289 | 0.955 |
| away_team_goals_conceded_last_5 | 6.490 | 5.588 | 5.557 | 0.933 |
| away_rest_days | 7.467 | 7.253 | 6.832 | 0.636 |
| home_team_goals_scored_last_5 | 6.188 | 5.588 | 5.701 | 0.600 |
| away_team_wins_last_5 | 1.250 | 1.825 | 1.753 | 0.575 |
| home_rest_days | 7.380 | 7.266 | 7.032 | 0.349 |
| home_team_wins_last_5 | 1.812 | 1.663 | 1.505 | 0.307 |
| rest_days_difference | -0.087 | 0.013 | 0.200 | 0.287 |
| home_team_home_conceded_avg | 1.001 | 1.114 | 1.240 | 0.240 |
| away_team_away_goals_avg | 1.007 | 1.140 | 1.195 | 0.188 |
| home_team_home_goals_avg | 1.384 | 1.270 | 1.213 | 0.171 |
| away_team_away_conceded_avg | 1.341 | 1.254 | 1.229 | 0.112 |
| home_team_home_win_rate | 0.408 | 0.367 | 0.316 | 0.092 |
| away_team_away_win_rate | 0.277 | 0.354 | 0.328 | 0.077 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\korea2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\korea2\charts\relationships_home_win_pct_by_position.png)

