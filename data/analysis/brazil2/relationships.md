# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:55:41+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie B (Brazil)
- Scope: league `brazil2`

- Matches analysed: **669** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_position_before_match | 0.153 | 0.001 | 0.113 |
| away_team_goals_conceded_last_5 | 0.124 | 0.001 | 0.091 |
| position_difference | -0.176 | 0.063 | -0.086 |
| points_difference | 0.188 | -0.079 | 0.083 |
| away_team_points_last_5 | -0.069 | -0.026 | -0.068 |
| away_team_wins_last_5 | -0.069 | -0.011 | -0.058 |
| home_rest_days | -0.079 | 0.000 | -0.057 |
| away_team_away_conceded_avg | 0.131 | -0.065 | 0.051 |
| home_team_points_last_5 | 0.110 | -0.044 | 0.050 |
| home_points_before_match | 0.077 | -0.015 | 0.046 |
| rest_days_difference | -0.026 | -0.033 | -0.042 |
| home_team_wins_last_5 | 0.081 | -0.039 | 0.033 |
| away_team_away_goals_avg | 0.043 | 0.002 | 0.033 |
| away_team_away_win_rate | -0.078 | 0.036 | -0.033 |
| away_rest_days | -0.059 | 0.028 | -0.024 |
| home_team_home_goals_avg | 0.047 | -0.017 | 0.022 |
| home_team_goals_conceded_last_5 | -0.080 | 0.055 | -0.021 |
| away_team_goals_scored_last_5 | -0.003 | -0.027 | -0.020 |
| home_team_goals_scored_last_5 | 0.034 | -0.013 | 0.016 |
| home_team_home_win_rate | 0.058 | -0.048 | 0.009 |
| home_team_home_conceded_avg | -0.025 | 0.017 | -0.007 |
| home_position_before_match | -0.089 | 0.088 | -0.004 |
| away_points_before_match | -0.032 | 0.031 | -0.002 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 99 | 34 | 33 | 32 | 34.3% | 33.3% | 32.3% |
| -4..-2 | 147 | 63 | 46 | 38 | 42.9% | 31.3% | 25.9% |
| -1..1 | 204 | 94 | 52 | 58 | 46.1% | 25.5% | 28.4% |
| 2..4 | 131 | 67 | 39 | 25 | 51.1% | 29.8% | 19.1% |
| >4 | 88 | 46 | 25 | 17 | 52.3% | 28.4% | 19.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 150 | 82 | 40 | 28 | 54.7% | 26.7% | 18.7% |
| -5..-2 | 111 | 57 | 34 | 20 | 51.4% | 30.6% | 18.0% |
| -1..1 | 102 | 50 | 26 | 26 | 49.0% | 25.5% | 25.5% |
| 2..5 | 121 | 49 | 35 | 37 | 40.5% | 28.9% | 30.6% |
| >=6 | 185 | 66 | 60 | 59 | 35.7% | 32.4% | 31.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 114 | 56 | 30 | 28 | 49.1% | 26.3% | 24.6% |
| -1..0 | 119 | 49 | 40 | 30 | 41.2% | 33.6% | 25.2% |
| 0 | 157 | 78 | 39 | 40 | 49.7% | 24.8% | 25.5% |
| 1..2 | 207 | 90 | 65 | 52 | 43.5% | 31.4% | 25.1% |
| >2 | 52 | 21 | 16 | 15 | 40.4% | 30.8% | 28.8% |
| unknown | 20 | 10 | 5 | 5 | 50.0% | 25.0% | 25.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.3%** home win (32/96)
- `>= 0.5` tier: **47.5%** home win (272/573)
- Home-win gap (>= split minus < split): **+14.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 96 | 32 | 31 | 33 | 33.3% |
| high | >= 0.5 | 573 | 272 | 164 | 137 | 47.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.398 | -1.021 | -2.424 | 3.822 |
| position_difference | -0.921 | 1.067 | 2.071 | 2.992 |
| home_points_before_match | 22.961 | 22.292 | 20.800 | 2.161 |
| home_position_before_match | 10.441 | 11.159 | 12.218 | 1.777 |
| away_points_before_match | 21.562 | 23.313 | 23.224 | 1.750 |
| away_position_before_match | 11.362 | 10.092 | 10.147 | 1.270 |
| home_team_points_last_5 | 6.375 | 6.067 | 5.318 | 1.057 |
| home_team_goals_conceded_last_5 | 4.947 | 5.056 | 5.712 | 0.764 |
| away_rest_days | 6.252 | 6.084 | 6.691 | 0.607 |
| home_rest_days | 6.221 | 6.279 | 6.776 | 0.555 |
| away_team_goals_conceded_last_5 | 5.362 | 4.856 | 4.882 | 0.505 |
| away_team_points_last_5 | 6.171 | 6.549 | 6.241 | 0.378 |
| home_team_wins_last_5 | 3.039 | 2.908 | 2.682 | 0.357 |
| home_team_goals_scored_last_5 | 5.076 | 5.113 | 4.847 | 0.266 |
| away_team_goals_scored_last_5 | 5.332 | 5.221 | 5.106 | 0.226 |
| rest_days_difference | -0.031 | 0.195 | 0.085 | 0.225 |
| away_team_away_conceded_avg | 1.256 | 1.119 | 1.122 | 0.137 |
| away_team_wins_last_5 | 2.928 | 3.021 | 3.041 | 0.114 |
| away_team_away_goals_avg | 0.911 | 0.833 | 0.863 | 0.079 |
| home_team_home_goals_avg | 1.216 | 1.151 | 1.138 | 0.078 |
| home_team_home_win_rate | 0.735 | 0.681 | 0.670 | 0.065 |
| home_team_home_conceded_avg | 0.862 | 0.862 | 0.914 | 0.051 |
| away_team_away_win_rate | 0.511 | 0.518 | 0.539 | 0.028 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\brazil2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\brazil2\charts\relationships_home_win_pct_by_position.png)

