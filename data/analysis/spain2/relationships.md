# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:09:10+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: LaLiga2 (Spain)
- Scope: league `spain2`

- Matches analysed: **509** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.214 | 0.046 | -0.125 |
| points_difference | 0.216 | -0.093 | 0.096 |
| position_difference | -0.203 | 0.082 | -0.094 |
| home_team_wins_last_5 | 0.107 | 0.022 | 0.092 |
| home_points_before_match | 0.123 | -0.004 | 0.087 |
| home_team_points_last_5 | 0.122 | -0.007 | 0.084 |
| home_team_home_goals_avg | 0.156 | -0.059 | 0.075 |
| home_team_goals_scored_last_5 | 0.115 | -0.019 | 0.071 |
| home_team_goals_conceded_last_5 | -0.100 | 0.003 | -0.071 |
| home_team_home_win_rate | 0.142 | -0.054 | 0.068 |
| rest_days_difference | 0.008 | 0.077 | 0.056 |
| home_rest_days | 0.016 | 0.047 | 0.042 |
| away_team_goals_conceded_last_5 | 0.063 | -0.022 | 0.032 |
| away_points_before_match | -0.003 | 0.050 | 0.030 |
| away_team_points_last_5 | -0.058 | 0.024 | -0.026 |
| away_team_away_conceded_avg | 0.012 | 0.013 | 0.017 |
| away_team_away_goals_avg | -0.054 | 0.039 | -0.014 |
| away_position_before_match | 0.075 | -0.070 | 0.009 |
| away_team_goals_scored_last_5 | -0.036 | 0.027 | -0.009 |
| away_team_wins_last_5 | -0.019 | 0.025 | 0.003 |
| home_team_home_conceded_avg | -0.026 | 0.032 | 0.002 |
| away_team_away_win_rate | -0.008 | 0.007 | -0.001 |
| away_rest_days | 0.010 | -0.013 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 81 | 30 | 22 | 29 | 37.0% | 27.2% | 35.8% |
| -4..-2 | 114 | 46 | 32 | 36 | 40.4% | 28.1% | 31.6% |
| -1..1 | 139 | 65 | 36 | 38 | 46.8% | 25.9% | 27.3% |
| 2..4 | 97 | 42 | 19 | 36 | 43.3% | 19.6% | 37.1% |
| >4 | 78 | 40 | 20 | 18 | 51.3% | 25.6% | 23.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 135 | 79 | 30 | 26 | 58.5% | 22.2% | 19.3% |
| -5..-2 | 93 | 42 | 23 | 28 | 45.2% | 24.7% | 30.1% |
| -1..1 | 50 | 26 | 12 | 12 | 52.0% | 24.0% | 24.0% |
| 2..5 | 79 | 28 | 25 | 26 | 35.4% | 31.6% | 32.9% |
| >=6 | 152 | 48 | 39 | 65 | 31.6% | 25.7% | 42.8% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 44 | 21 | 9 | 14 | 47.7% | 20.5% | 31.8% |
| -1..0 | 120 | 56 | 31 | 33 | 46.7% | 25.8% | 27.5% |
| 0 | 171 | 71 | 42 | 58 | 41.5% | 24.6% | 33.9% |
| 1..2 | 147 | 64 | 39 | 44 | 43.5% | 26.5% | 29.9% |
| >2 | 15 | 5 | 4 | 6 | 33.3% | 26.7% | 40.0% |
| unknown | 12 | 6 | 4 | 2 | 50.0% | 33.3% | 16.7% |
- *12 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **40.6%** home win (125/308)
- `>= 0.5` tier: **48.8%** home win (98/201)
- Home-win gap (>= split minus < split): **+8.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 308 | 125 | 70 | 113 | 40.6% |
| high | >= 0.5 | 201 | 98 | 59 | 44 | 48.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.717 | -0.922 | -3.962 | 6.679 |
| position_difference | -1.874 | 0.775 | 2.720 | 4.594 |
| home_points_before_match | 31.816 | 27.341 | 28.057 | 4.475 |
| away_points_before_match | 29.099 | 28.264 | 32.019 | 3.756 |
| home_position_before_match | 11.291 | 12.729 | 13.752 | 2.460 |
| away_position_before_match | 13.166 | 11.953 | 11.032 | 2.134 |
| home_team_points_last_5 | 6.713 | 5.899 | 6.153 | 0.814 |
| away_team_goals_conceded_last_5 | 6.031 | 6.558 | 5.783 | 0.775 |
| home_team_goals_scored_last_5 | 6.435 | 5.744 | 5.898 | 0.691 |
| home_team_goals_conceded_last_5 | 6.018 | 5.930 | 6.592 | 0.662 |
| away_team_points_last_5 | 6.498 | 6.240 | 6.707 | 0.467 |
| home_team_wins_last_5 | 1.830 | 1.566 | 1.682 | 0.264 |
| home_team_home_goals_avg | 1.438 | 1.342 | 1.210 | 0.228 |
| away_team_goals_scored_last_5 | 6.103 | 6.264 | 6.293 | 0.190 |
| rest_days_difference | -0.065 | 0.088 | 0.103 | 0.168 |
| home_team_home_conceded_avg | 1.131 | 1.068 | 1.184 | 0.115 |
| away_team_away_goals_avg | 1.081 | 1.191 | 1.168 | 0.110 |
| away_rest_days | 7.018 | 6.928 | 6.929 | 0.090 |
| home_rest_days | 6.954 | 7.016 | 7.032 | 0.078 |
| home_team_home_win_rate | 0.426 | 0.416 | 0.349 | 0.076 |
| away_team_wins_last_5 | 1.780 | 1.721 | 1.777 | 0.059 |
| away_team_away_conceded_avg | 1.353 | 1.333 | 1.308 | 0.045 |
| away_team_away_win_rate | 0.282 | 0.320 | 0.285 | 0.038 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\spain2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\spain2\charts\relationships_home_win_pct_by_position.png)

