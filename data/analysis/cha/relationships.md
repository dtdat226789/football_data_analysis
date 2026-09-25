# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:56:01+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Championship (England)
- Scope: league `cha`

- Matches analysed: **654** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_home_conceded_avg | -0.108 | 0.031 | -0.062 |
| home_team_points_last_5 | 0.032 | -0.119 | -0.058 |
| away_team_goals_conceded_last_5 | 0.012 | -0.096 | -0.057 |
| home_team_wins_last_5 | 0.038 | -0.115 | -0.050 |
| home_team_home_goals_avg | 0.109 | -0.067 | 0.038 |
| away_team_goals_scored_last_5 | -0.028 | 0.084 | 0.036 |
| away_team_points_last_5 | -0.042 | 0.092 | 0.031 |
| home_team_home_win_rate | 0.112 | -0.082 | 0.030 |
| away_rest_days | -0.021 | 0.062 | 0.027 |
| away_team_away_conceded_avg | -0.035 | 0.002 | -0.026 |
| rest_days_difference | -0.011 | -0.020 | -0.022 |
| home_team_goals_conceded_last_5 | -0.004 | -0.026 | -0.021 |
| home_rest_days | -0.026 | 0.052 | 0.016 |
| away_position_before_match | 0.072 | -0.100 | -0.013 |
| away_points_before_match | -0.053 | 0.042 | -0.012 |
| away_team_away_win_rate | 0.014 | 0.001 | 0.011 |
| home_team_goals_scored_last_5 | 0.105 | -0.134 | -0.011 |
| position_difference | -0.108 | 0.137 | 0.011 |
| away_team_away_goals_avg | -0.061 | 0.053 | -0.011 |
| away_team_wins_last_5 | -0.050 | 0.044 | -0.009 |
| points_difference | 0.149 | -0.154 | 0.008 |
| home_points_before_match | 0.029 | -0.044 | -0.007 |
| home_position_before_match | -0.075 | 0.087 | 0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 96 | 38 | 26 | 32 | 39.6% | 27.1% | 33.3% |
| -4..-2 | 131 | 48 | 29 | 54 | 36.6% | 22.1% | 41.2% |
| -1..1 | 205 | 76 | 65 | 64 | 37.1% | 31.7% | 31.2% |
| 2..4 | 148 | 75 | 35 | 38 | 50.7% | 23.6% | 25.7% |
| >4 | 74 | 35 | 23 | 16 | 47.3% | 31.1% | 21.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 180 | 87 | 49 | 44 | 48.3% | 27.2% | 24.4% |
| -5..-2 | 99 | 52 | 19 | 28 | 52.5% | 19.2% | 28.3% |
| -1..1 | 80 | 29 | 23 | 28 | 36.2% | 28.8% | 35.0% |
| 2..5 | 102 | 39 | 34 | 29 | 38.2% | 33.3% | 28.4% |
| >=6 | 193 | 65 | 53 | 75 | 33.7% | 27.5% | 38.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 34 | 15 | 10 | 9 | 44.1% | 29.4% | 26.5% |
| -1..0 | 71 | 29 | 13 | 29 | 40.8% | 18.3% | 40.8% |
| 0 | 413 | 161 | 129 | 123 | 39.0% | 31.2% | 29.8% |
| 1..2 | 88 | 48 | 14 | 26 | 54.5% | 15.9% | 29.5% |
| >2 | 24 | 9 | 5 | 10 | 37.5% | 20.8% | 41.7% |
| unknown | 24 | 10 | 7 | 7 | 41.7% | 29.2% | 29.2% |
- *24 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.8%** home win (47/139)
- `>= 0.5` tier: **43.7%** home win (225/515)
- Home-win gap (>= split minus < split): **+9.9 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 139 | 47 | 38 | 54 | 33.8% |
| high | >= 0.5 | 515 | 225 | 140 | 150 | 43.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.489 | -1.416 | -2.613 | 5.102 |
| away_points_before_match | 25.963 | 27.607 | 29.387 | 3.424 |
| position_difference | -1.309 | 0.944 | 2.044 | 3.353 |
| home_points_before_match | 28.452 | 26.191 | 26.775 | 2.261 |
| away_position_before_match | 13.316 | 11.865 | 11.627 | 1.689 |
| home_position_before_match | 12.007 | 12.809 | 13.672 | 1.664 |
| home_team_goals_scored_last_5 | 6.210 | 5.646 | 5.294 | 0.915 |
| away_team_points_last_5 | 5.938 | 6.124 | 6.534 | 0.597 |
| home_team_points_last_5 | 6.202 | 6.112 | 5.657 | 0.545 |
| away_team_goals_scored_last_5 | 5.647 | 5.820 | 6.098 | 0.451 |
| away_team_goals_conceded_last_5 | 5.882 | 5.725 | 5.480 | 0.402 |
| away_rest_days | 5.557 | 5.942 | 5.919 | 0.384 |
| home_rest_days | 5.634 | 5.825 | 5.944 | 0.311 |
| home_team_wins_last_5 | 2.901 | 2.831 | 2.667 | 0.234 |
| rest_days_difference | 0.076 | -0.117 | 0.025 | 0.193 |
| away_team_wins_last_5 | 2.820 | 2.798 | 2.985 | 0.188 |
| home_team_home_conceded_avg | 1.088 | 1.126 | 1.260 | 0.172 |
| home_team_goals_conceded_last_5 | 5.912 | 5.753 | 5.809 | 0.159 |
| home_team_home_goals_avg | 1.338 | 1.261 | 1.184 | 0.154 |
| away_team_away_goals_avg | 1.084 | 1.203 | 1.208 | 0.124 |
| home_team_home_win_rate | 0.663 | 0.639 | 0.579 | 0.084 |
| away_team_away_conceded_avg | 1.244 | 1.271 | 1.291 | 0.047 |
| away_team_away_win_rate | 0.554 | 0.560 | 0.555 | 0.006 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\cha\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\cha\charts\relationships_home_win_pct_by_position.png)

