# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:03:20+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Virsliga (Latvia)
- Scope: league `latvia`

- Matches analysed: **336** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_win_rate | 0.194 | -0.005 | 0.148 |
| home_team_wins_last_5 | 0.250 | -0.074 | 0.144 |
| home_team_goals_scored_last_5 | 0.279 | -0.125 | 0.131 |
| home_team_home_conceded_avg | -0.211 | 0.064 | -0.120 |
| home_team_points_last_5 | 0.274 | -0.141 | 0.115 |
| away_rest_days | -0.033 | 0.200 | 0.114 |
| home_team_home_goals_avg | 0.207 | -0.081 | 0.105 |
| points_difference | 0.399 | -0.315 | 0.091 |
| home_points_before_match | 0.214 | -0.111 | 0.089 |
| away_team_goals_scored_last_5 | -0.156 | 0.296 | 0.086 |
| home_rest_days | 0.007 | 0.112 | 0.084 |
| home_position_before_match | -0.271 | 0.186 | -0.081 |
| position_difference | -0.402 | 0.337 | -0.077 |
| away_team_away_conceded_avg | 0.189 | -0.115 | 0.067 |
| away_team_away_goals_avg | -0.225 | 0.344 | 0.065 |
| home_team_goals_conceded_last_5 | -0.175 | 0.114 | -0.057 |
| away_team_wins_last_5 | -0.148 | 0.238 | 0.052 |
| rest_days_difference | 0.072 | -0.143 | -0.045 |
| away_team_points_last_5 | -0.198 | 0.260 | 0.028 |
| away_position_before_match | 0.295 | -0.289 | 0.028 |
| away_team_goals_conceded_last_5 | 0.128 | -0.105 | 0.026 |
| away_team_away_win_rate | -0.227 | 0.217 | -0.025 |
| away_points_before_match | -0.168 | 0.188 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 73 | 14 | 17 | 42 | 19.2% | 23.3% | 57.5% |
| -4..-2 | 53 | 13 | 18 | 22 | 24.5% | 34.0% | 41.5% |
| -1..1 | 84 | 40 | 17 | 27 | 47.6% | 20.2% | 32.1% |
| 2..4 | 61 | 32 | 16 | 13 | 52.5% | 26.2% | 21.3% |
| >4 | 65 | 48 | 12 | 5 | 73.8% | 18.5% | 7.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 34 | 30 | 3 | 1 | 88.2% | 8.8% | 2.9% |
| -5..-2 | 83 | 48 | 17 | 18 | 57.8% | 20.5% | 21.7% |
| -1..1 | 89 | 36 | 30 | 23 | 40.4% | 33.7% | 25.8% |
| 2..5 | 98 | 29 | 24 | 45 | 29.6% | 24.5% | 45.9% |
| >=6 | 32 | 4 | 6 | 22 | 12.5% | 18.8% | 68.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 24 | 5 | 5 | 14 | 20.8% | 20.8% | 58.3% |
| -1..0 | 84 | 37 | 25 | 22 | 44.0% | 29.8% | 26.2% |
| 0 | 99 | 44 | 20 | 35 | 44.4% | 20.2% | 35.4% |
| 1..2 | 111 | 51 | 27 | 33 | 45.9% | 24.3% | 29.7% |
| >2 | 7 | 3 | 1 | 3 | 42.9% | 14.3% | 42.9% |
| unknown | 11 | 7 | 2 | 2 | 63.6% | 18.2% | 18.2% |
- *11 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.5%** home win (27/72)
- `>= 0.5` tier: **45.5%** home win (120/264)
- Home-win gap (>= split minus < split): **+8.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 72 | 27 | 21 | 24 | 37.5% |
| high | >= 0.5 | 264 | 120 | 59 | 85 | 45.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 7.565 | -0.225 | -10.541 | 18.106 |
| away_points_before_match | 17.687 | 23.025 | 29.110 | 11.423 |
| home_points_before_match | 25.252 | 22.800 | 18.569 | 6.683 |
| position_difference | -1.782 | 0.500 | 2.431 | 4.214 |
| away_team_goals_scored_last_5 | 5.599 | 6.338 | 8.817 | 3.218 |
| away_team_points_last_5 | 5.088 | 6.150 | 8.202 | 3.113 |
| away_position_before_match | 6.639 | 5.812 | 3.862 | 2.777 |
| home_team_goals_scored_last_5 | 7.578 | 6.025 | 5.560 | 2.019 |
| home_team_points_last_5 | 7.327 | 5.662 | 5.321 | 2.005 |
| away_team_goals_conceded_last_5 | 7.531 | 6.662 | 5.835 | 1.696 |
| home_position_before_match | 4.857 | 6.312 | 6.294 | 1.455 |
| home_team_goals_conceded_last_5 | 5.884 | 7.225 | 7.156 | 1.341 |
| away_rest_days | 6.479 | 6.462 | 7.542 | 1.081 |
| away_team_wins_last_5 | 2.395 | 2.700 | 3.339 | 0.945 |
| away_team_away_goals_avg | 0.887 | 1.071 | 1.618 | 0.731 |
| home_rest_days | 6.757 | 6.557 | 7.224 | 0.667 |
| rest_days_difference | 0.279 | 0.038 | -0.318 | 0.596 |
| home_team_wins_last_5 | 3.014 | 2.638 | 2.514 | 0.500 |
| away_team_away_conceded_avg | 1.787 | 1.568 | 1.317 | 0.470 |
| home_team_home_goals_avg | 1.684 | 1.532 | 1.378 | 0.306 |
| away_team_away_win_rate | 0.418 | 0.481 | 0.642 | 0.224 |
| home_team_home_conceded_avg | 1.076 | 1.224 | 1.297 | 0.221 |
| home_team_home_win_rate | 0.671 | 0.597 | 0.613 | 0.073 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\latvia\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\latvia\charts\relationships_home_win_pct_by_position.png)

