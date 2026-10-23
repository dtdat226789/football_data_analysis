# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:46:19+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Championship (England)
- Scope: league `cha`

- Matches analysed: **559** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_wins_last_5 | -0.039 | 0.136 | 0.067 |
| home_team_home_conceded_avg | -0.134 | 0.053 | -0.065 |
| away_team_away_win_rate | -0.077 | -0.008 | -0.065 |
| away_team_goals_conceded_last_5 | 0.030 | -0.109 | -0.054 |
| away_team_points_last_5 | -0.049 | 0.126 | 0.052 |
| rest_days_difference | -0.034 | -0.033 | -0.050 |
| away_team_goals_scored_last_5 | -0.041 | 0.104 | 0.043 |
| home_team_points_last_5 | 0.050 | -0.112 | -0.041 |
| home_team_wins_last_5 | 0.038 | -0.095 | -0.038 |
| home_points_before_match | 0.075 | -0.034 | 0.033 |
| away_rest_days | -0.017 | 0.061 | 0.030 |
| away_points_before_match | -0.028 | 0.065 | 0.025 |
| points_difference | 0.168 | -0.161 | 0.015 |
| home_position_before_match | -0.090 | 0.080 | -0.012 |
| away_team_away_conceded_avg | -0.036 | 0.024 | -0.011 |
| home_team_goals_scored_last_5 | 0.110 | -0.133 | -0.010 |
| home_team_home_goals_avg | 0.088 | -0.082 | 0.009 |
| home_team_home_win_rate | 0.069 | -0.087 | -0.009 |
| away_team_away_goals_avg | -0.092 | 0.089 | -0.008 |
| home_rest_days | -0.034 | 0.046 | 0.006 |
| position_difference | -0.135 | 0.138 | -0.005 |
| away_position_before_match | 0.095 | -0.110 | -0.005 |
| home_team_goals_conceded_last_5 | 0.005 | -0.009 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 87 | 33 | 24 | 30 | 37.9% | 27.6% | 34.5% |
| -4..-2 | 111 | 40 | 24 | 47 | 36.0% | 21.6% | 42.3% |
| -1..1 | 169 | 64 | 52 | 53 | 37.9% | 30.8% | 31.4% |
| 2..4 | 124 | 64 | 28 | 32 | 51.6% | 22.6% | 25.8% |
| >4 | 68 | 32 | 21 | 15 | 47.1% | 30.9% | 22.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 157 | 77 | 41 | 39 | 49.0% | 26.1% | 24.8% |
| -5..-2 | 89 | 46 | 18 | 25 | 51.7% | 20.2% | 28.1% |
| -1..1 | 59 | 23 | 17 | 19 | 39.0% | 28.8% | 32.2% |
| 2..5 | 90 | 33 | 29 | 28 | 36.7% | 32.2% | 31.1% |
| >=6 | 164 | 54 | 44 | 66 | 32.9% | 26.8% | 40.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 26 | 12 | 8 | 6 | 46.2% | 30.8% | 23.1% |
| -1..0 | 62 | 25 | 12 | 25 | 40.3% | 19.4% | 40.3% |
| 0 | 361 | 143 | 111 | 107 | 39.6% | 30.7% | 29.6% |
| 1..2 | 76 | 39 | 11 | 26 | 51.3% | 14.5% | 34.2% |
| >2 | 22 | 8 | 4 | 10 | 36.4% | 18.2% | 45.5% |
| unknown | 12 | 6 | 3 | 3 | 50.0% | 25.0% | 25.0% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **39.7%** home win (143/360)
- `>= 0.5` tier: **45.2%** home win (90/199)
- Home-win gap (>= split minus < split): **+5.5 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 360 | 143 | 88 | 129 | 39.7% |
| high | >= 0.5 | 199 | 90 | 61 | 48 | 45.2% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.961 | -1.725 | -2.944 | 5.905 |
| away_points_before_match | 29.481 | 32.027 | 33.203 | 3.723 |
| position_difference | -1.562 | 1.107 | 2.153 | 3.715 |
| home_points_before_match | 32.442 | 30.302 | 30.260 | 2.182 |
| away_position_before_match | 13.494 | 11.919 | 11.531 | 1.962 |
| home_position_before_match | 11.931 | 13.027 | 13.684 | 1.752 |
| home_team_goals_scored_last_5 | 6.446 | 5.966 | 5.497 | 0.949 |
| away_team_points_last_5 | 6.206 | 6.463 | 6.915 | 0.709 |
| home_team_points_last_5 | 6.528 | 6.463 | 5.944 | 0.584 |
| away_team_goals_scored_last_5 | 5.824 | 6.000 | 6.356 | 0.532 |
| away_team_goals_conceded_last_5 | 6.120 | 6.007 | 5.638 | 0.482 |
| away_rest_days | 5.634 | 6.082 | 6.011 | 0.448 |
| home_rest_days | 5.722 | 5.959 | 6.109 | 0.387 |
| away_team_wins_last_5 | 1.639 | 1.745 | 1.893 | 0.253 |
| rest_days_difference | 0.088 | -0.123 | 0.098 | 0.221 |
| home_team_home_conceded_avg | 1.097 | 1.172 | 1.282 | 0.184 |
| home_team_wins_last_5 | 1.734 | 1.752 | 1.576 | 0.175 |
| away_team_away_goals_avg | 1.093 | 1.244 | 1.242 | 0.152 |
| home_team_home_goals_avg | 1.354 | 1.300 | 1.204 | 0.150 |
| home_team_goals_conceded_last_5 | 6.094 | 6.067 | 5.977 | 0.117 |
| home_team_home_win_rate | 0.407 | 0.409 | 0.348 | 0.061 |
| away_team_away_conceded_avg | 1.259 | 1.293 | 1.320 | 0.060 |
| away_team_away_win_rate | 0.292 | 0.342 | 0.312 | 0.050 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\cha\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\cha\charts\relationships_home_win_pct_by_position.png)

