# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:57:57+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: League Two (England)
- Scope: league `eng2`

- Matches analysed: **641** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_wins_last_5 | 0.122 | -0.059 | 0.053 |
| home_team_home_win_rate | 0.101 | -0.036 | 0.052 |
| points_difference | 0.193 | -0.143 | 0.049 |
| home_rest_days | 0.033 | 0.034 | 0.048 |
| away_rest_days | 0.052 | 0.008 | 0.045 |
| home_team_goals_scored_last_5 | 0.085 | -0.030 | 0.044 |
| home_team_goals_conceded_last_5 | -0.121 | 0.070 | -0.044 |
| away_team_away_win_rate | -0.051 | 0.118 | 0.042 |
| home_team_points_last_5 | 0.108 | -0.061 | 0.041 |
| away_team_wins_last_5 | -0.052 | 0.113 | 0.037 |
| away_team_points_last_5 | -0.060 | 0.120 | 0.036 |
| away_team_goals_scored_last_5 | -0.049 | 0.106 | 0.035 |
| away_team_goals_conceded_last_5 | 0.015 | -0.063 | -0.031 |
| home_team_home_goals_avg | 0.086 | -0.052 | 0.029 |
| home_team_home_conceded_avg | -0.060 | 0.026 | -0.027 |
| away_team_away_goals_avg | -0.036 | 0.074 | 0.023 |
| position_difference | -0.182 | 0.177 | -0.018 |
| away_points_before_match | -0.081 | 0.066 | -0.017 |
| home_position_before_match | -0.145 | 0.140 | -0.015 |
| home_points_before_match | 0.034 | -0.020 | 0.012 |
| away_position_before_match | 0.101 | -0.100 | 0.009 |
| rest_days_difference | -0.035 | 0.047 | 0.005 |
| away_team_away_conceded_avg | 0.054 | -0.064 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 91 | 26 | 23 | 42 | 28.6% | 25.3% | 46.2% |
| -4..-2 | 146 | 62 | 39 | 45 | 42.5% | 26.7% | 30.8% |
| -1..1 | 186 | 75 | 52 | 59 | 40.3% | 28.0% | 31.7% |
| 2..4 | 117 | 54 | 30 | 33 | 46.2% | 25.6% | 28.2% |
| >4 | 101 | 59 | 25 | 17 | 58.4% | 24.8% | 16.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 171 | 90 | 45 | 36 | 52.6% | 26.3% | 21.1% |
| -5..-2 | 94 | 46 | 25 | 23 | 48.9% | 26.6% | 24.5% |
| -1..1 | 82 | 43 | 17 | 22 | 52.4% | 20.7% | 26.8% |
| 2..5 | 99 | 38 | 30 | 31 | 38.4% | 30.3% | 31.3% |
| >=6 | 195 | 59 | 52 | 84 | 30.3% | 26.7% | 43.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 39 | 20 | 7 | 12 | 51.3% | 17.9% | 30.8% |
| -1..0 | 13 | 4 | 5 | 4 | 30.8% | 38.5% | 30.8% |
| 0 | 513 | 216 | 139 | 158 | 42.1% | 27.1% | 30.8% |
| 1..2 | 21 | 13 | 4 | 4 | 61.9% | 19.0% | 19.0% |
| >2 | 31 | 12 | 7 | 12 | 38.7% | 22.6% | 38.7% |
| unknown | 24 | 11 | 7 | 6 | 45.8% | 29.2% | 25.0% |
- *24 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.9%** home win (58/149)
- `>= 0.5` tier: **44.3%** home win (218/492)
- Home-win gap (>= split minus < split): **+5.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 149 | 58 | 30 | 61 | 38.9% |
| high | >= 0.5 | 492 | 218 | 139 | 135 | 44.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.511 | 0.112 | -4.153 | 6.664 |
| away_points_before_match | 26.000 | 26.686 | 31.316 | 5.316 |
| position_difference | -1.804 | 0.355 | 3.286 | 5.090 |
| home_position_before_match | 11.417 | 11.680 | 14.485 | 3.068 |
| away_position_before_match | 13.221 | 11.325 | 11.199 | 2.022 |
| home_points_before_match | 28.511 | 26.799 | 27.163 | 1.712 |
| home_team_points_last_5 | 6.475 | 6.118 | 5.480 | 0.995 |
| home_team_goals_conceded_last_5 | 5.272 | 5.533 | 6.240 | 0.968 |
| away_team_points_last_5 | 5.775 | 6.160 | 6.684 | 0.908 |
| away_team_goals_scored_last_5 | 5.533 | 5.716 | 6.179 | 0.646 |
| home_team_goals_scored_last_5 | 5.826 | 5.651 | 5.240 | 0.586 |
| away_team_goals_conceded_last_5 | 5.928 | 5.355 | 5.582 | 0.573 |
| home_team_wins_last_5 | 2.931 | 2.864 | 2.520 | 0.411 |
| away_team_wins_last_5 | 2.652 | 2.822 | 3.000 | 0.348 |
| home_team_home_goals_avg | 1.326 | 1.336 | 1.161 | 0.176 |
| away_team_away_conceded_avg | 1.356 | 1.208 | 1.249 | 0.149 |
| home_team_home_conceded_avg | 1.087 | 1.021 | 1.149 | 0.129 |
| rest_days_difference | -0.064 | 0.037 | 0.016 | 0.101 |
| home_rest_days | 5.992 | 6.080 | 6.079 | 0.088 |
| home_team_home_win_rate | 0.647 | 0.663 | 0.581 | 0.082 |
| away_team_away_goals_avg | 1.063 | 1.100 | 1.126 | 0.063 |
| away_team_away_win_rate | 0.508 | 0.560 | 0.566 | 0.058 |
| away_rest_days | 6.057 | 6.043 | 6.063 | 0.020 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\eng2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\eng2\charts\relationships_home_win_pct_by_position.png)

