# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:59:20+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Regionalliga North (Germany)
- Scope: league `germany-north`

- Matches analysed: **408** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.208 | -0.077 | 0.121 |
| home_team_points_last_5 | 0.222 | -0.111 | 0.110 |
| home_team_home_goals_avg | 0.159 | -0.036 | 0.109 |
| position_difference | -0.283 | 0.205 | -0.096 |
| away_team_wins_last_5 | -0.148 | 0.058 | -0.085 |
| home_position_before_match | -0.216 | 0.153 | -0.076 |
| away_points_before_match | -0.140 | 0.067 | -0.071 |
| points_difference | 0.265 | -0.222 | 0.069 |
| away_rest_days | -0.074 | -0.006 | -0.068 |
| away_position_before_match | 0.168 | -0.125 | 0.054 |
| away_team_points_last_5 | -0.140 | 0.095 | -0.051 |
| home_team_wins_last_5 | 0.158 | -0.118 | 0.051 |
| home_team_home_win_rate | 0.103 | -0.052 | 0.050 |
| rest_days_difference | 0.043 | 0.012 | 0.045 |
| away_team_goals_scored_last_5 | -0.120 | 0.090 | -0.039 |
| away_team_away_conceded_avg | 0.149 | -0.126 | 0.037 |
| away_team_goals_conceded_last_5 | 0.124 | -0.099 | 0.036 |
| home_team_goals_conceded_last_5 | -0.102 | 0.075 | -0.034 |
| home_rest_days | -0.033 | 0.007 | -0.024 |
| home_points_before_match | 0.067 | -0.108 | -0.019 |
| away_team_away_win_rate | -0.089 | 0.089 | -0.013 |
| home_team_home_conceded_avg | -0.061 | 0.089 | 0.010 |
| away_team_away_goals_avg | -0.053 | 0.060 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 78 | 21 | 17 | 40 | 26.9% | 21.8% | 51.3% |
| -4..-2 | 85 | 29 | 26 | 30 | 34.1% | 30.6% | 35.3% |
| -1..1 | 109 | 50 | 16 | 43 | 45.9% | 14.7% | 39.4% |
| 2..4 | 67 | 33 | 16 | 18 | 49.3% | 23.9% | 26.9% |
| >4 | 69 | 39 | 14 | 16 | 56.5% | 20.3% | 23.2% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 94 | 60 | 15 | 19 | 63.8% | 16.0% | 20.2% |
| -5..-2 | 74 | 41 | 12 | 21 | 55.4% | 16.2% | 28.4% |
| -1..1 | 67 | 21 | 13 | 33 | 31.3% | 19.4% | 49.3% |
| 2..5 | 78 | 25 | 22 | 31 | 32.1% | 28.2% | 39.7% |
| >=6 | 95 | 25 | 27 | 43 | 26.3% | 28.4% | 45.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 71 | 24 | 23 | 24 | 33.8% | 32.4% | 33.8% |
| -1..0 | 78 | 29 | 16 | 33 | 37.2% | 20.5% | 42.3% |
| 0 | 108 | 44 | 19 | 45 | 40.7% | 17.6% | 41.7% |
| 1..2 | 77 | 45 | 16 | 16 | 58.4% | 20.8% | 20.8% |
| >2 | 52 | 23 | 10 | 19 | 44.2% | 19.2% | 36.5% |
| unknown | 22 | 7 | 5 | 10 | 31.8% | 22.7% | 45.5% |
- *22 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.7%** home win (46/122)
- `>= 0.5` tier: **44.1%** home win (126/286)
- Home-win gap (>= split minus < split): **+6.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 122 | 46 | 29 | 47 | 37.7% |
| high | >= 0.5 | 286 | 126 | 60 | 100 | 44.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.099 | -2.921 | -4.497 | 8.595 |
| position_difference | -2.436 | 2.011 | 2.252 | 4.688 |
| away_points_before_match | 17.076 | 21.483 | 21.639 | 4.564 |
| away_rest_days | 6.952 | 11.118 | 7.920 | 4.166 |
| home_points_before_match | 21.174 | 18.562 | 17.143 | 4.032 |
| home_position_before_match | 8.314 | 11.281 | 10.898 | 2.967 |
| home_rest_days | 7.179 | 9.512 | 8.219 | 2.333 |
| away_position_before_match | 10.750 | 9.270 | 8.646 | 2.104 |
| rest_days_difference | 0.242 | -1.738 | 0.292 | 2.030 |
| home_team_goals_scored_last_5 | 8.779 | 6.854 | 7.109 | 1.925 |
| home_team_points_last_5 | 6.738 | 5.157 | 5.231 | 1.581 |
| away_team_goals_scored_last_5 | 7.256 | 7.483 | 8.707 | 1.452 |
| away_team_points_last_5 | 5.628 | 5.888 | 6.844 | 1.216 |
| away_team_goals_conceded_last_5 | 8.140 | 7.933 | 6.966 | 1.174 |
| home_team_goals_conceded_last_5 | 7.326 | 8.472 | 8.327 | 1.146 |
| home_team_wins_last_5 | 2.843 | 2.371 | 2.388 | 0.472 |
| away_team_wins_last_5 | 2.500 | 2.674 | 2.871 | 0.371 |
| away_team_away_conceded_avg | 1.976 | 1.721 | 1.657 | 0.319 |
| home_team_home_goals_avg | 1.947 | 1.666 | 1.674 | 0.281 |
| home_team_home_conceded_avg | 1.464 | 1.684 | 1.668 | 0.220 |
| away_team_away_goals_avg | 1.504 | 1.562 | 1.680 | 0.176 |
| away_team_away_win_rate | 0.468 | 0.538 | 0.543 | 0.076 |
| home_team_home_win_rate | 0.596 | 0.557 | 0.556 | 0.041 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\germany-north\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\germany-north\charts\relationships_home_win_pct_by_position.png)

