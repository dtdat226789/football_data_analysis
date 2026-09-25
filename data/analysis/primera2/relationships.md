# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:42:57+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

- Matches analysed: **419** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.154 | 0.046 | 0.140 |
| home_points_before_match | 0.142 | 0.046 | 0.132 |
| home_team_home_goals_avg | 0.096 | 0.076 | 0.118 |
| away_points_before_match | 0.062 | 0.088 | 0.102 |
| home_position_before_match | -0.087 | -0.035 | -0.085 |
| rest_days_difference | 0.084 | 0.014 | 0.070 |
| home_team_points_last_5 | 0.067 | 0.032 | 0.069 |
| position_difference | -0.131 | 0.040 | -0.068 |
| home_rest_days | 0.045 | 0.049 | 0.064 |
| away_team_away_conceded_avg | 0.051 | 0.035 | 0.059 |
| points_difference | 0.149 | -0.080 | 0.056 |
| home_team_home_win_rate | 0.057 | 0.014 | 0.050 |
| home_team_goals_conceded_last_5 | 0.044 | 0.010 | 0.038 |
| away_team_goals_scored_last_5 | 0.014 | 0.037 | 0.034 |
| away_team_points_last_5 | 0.017 | 0.034 | 0.034 |
| home_team_wins_last_5 | 0.045 | -0.006 | 0.029 |
| home_team_home_conceded_avg | -0.002 | 0.045 | 0.028 |
| away_team_away_win_rate | -0.012 | -0.028 | -0.027 |
| away_team_wins_last_5 | -0.006 | 0.024 | 0.011 |
| away_team_goals_conceded_last_5 | -0.003 | -0.011 | -0.009 |
| away_rest_days | -0.026 | 0.040 | 0.007 |
| away_position_before_match | 0.091 | -0.091 | 0.006 |
| away_team_away_goals_avg | -0.039 | 0.051 | 0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 49 | 19 | 16 | 14 | 38.8% | 32.7% | 28.6% |
| -4..-2 | 107 | 46 | 33 | 28 | 43.0% | 30.8% | 26.2% |
| -1..1 | 147 | 75 | 39 | 33 | 51.0% | 26.5% | 22.4% |
| 2..4 | 78 | 34 | 24 | 20 | 43.6% | 30.8% | 25.6% |
| >4 | 38 | 18 | 12 | 8 | 47.4% | 31.6% | 21.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 93 | 45 | 31 | 17 | 48.4% | 33.3% | 18.3% |
| -5..-2 | 80 | 40 | 22 | 18 | 50.0% | 27.5% | 22.5% |
| -1..1 | 67 | 32 | 18 | 17 | 47.8% | 26.9% | 25.4% |
| 2..5 | 73 | 35 | 20 | 18 | 47.9% | 27.4% | 24.7% |
| >=6 | 106 | 40 | 33 | 33 | 37.7% | 31.1% | 31.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 30 | 14 | 7 | 9 | 46.7% | 23.3% | 30.0% |
| -1..0 | 81 | 44 | 19 | 18 | 54.3% | 23.5% | 22.2% |
| 0 | 159 | 70 | 48 | 41 | 44.0% | 30.2% | 25.8% |
| 1..2 | 112 | 48 | 37 | 27 | 42.9% | 33.0% | 24.1% |
| >2 | 17 | 9 | 6 | 2 | 52.9% | 35.3% | 11.8% |
| unknown | 20 | 7 | 7 | 6 | 35.0% | 35.0% | 30.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **46.9%** home win (23/49)
- `>= 0.5` tier: **45.7%** home win (169/370)
- Home-win gap (>= split minus < split): **-1.2 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 49 | 23 | 17 | 9 | 46.9% |
| high | >= 0.5 | 370 | 169 | 107 | 94 | 45.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| away_points_before_match | 22.635 | 20.911 | 25.233 | 4.322 |
| points_difference | 1.010 | -0.524 | -2.718 | 3.729 |
| home_points_before_match | 23.646 | 20.387 | 22.515 | 3.259 |
| position_difference | -0.500 | 0.419 | 2.175 | 2.675 |
| away_position_before_match | 11.443 | 10.177 | 9.563 | 1.880 |
| home_position_before_match | 10.943 | 10.597 | 11.738 | 1.141 |
| away_team_goals_scored_last_5 | 4.818 | 4.597 | 5.311 | 0.714 |
| away_team_goals_conceded_last_5 | 4.719 | 4.298 | 5.010 | 0.711 |
| home_team_goals_conceded_last_5 | 4.990 | 4.468 | 5.107 | 0.639 |
| home_team_goals_scored_last_5 | 4.891 | 4.452 | 4.466 | 0.439 |
| away_rest_days | 7.108 | 6.915 | 7.320 | 0.405 |
| rest_days_difference | 0.076 | 0.282 | -0.093 | 0.375 |
| away_team_points_last_5 | 5.922 | 5.952 | 6.146 | 0.224 |
| away_team_away_goals_avg | 0.766 | 0.747 | 0.902 | 0.155 |
| home_team_home_conceded_avg | 0.797 | 0.744 | 0.887 | 0.144 |
| home_team_points_last_5 | 5.724 | 5.581 | 5.631 | 0.143 |
| away_team_wins_last_5 | 2.807 | 2.855 | 2.942 | 0.134 |
| away_team_away_conceded_avg | 1.102 | 1.028 | 1.135 | 0.107 |
| home_team_wins_last_5 | 2.797 | 2.726 | 2.718 | 0.078 |
| home_team_home_goals_avg | 1.111 | 1.051 | 1.085 | 0.060 |
| home_rest_days | 7.184 | 7.197 | 7.227 | 0.043 |
| away_team_away_win_rate | 0.514 | 0.487 | 0.528 | 0.041 |
| home_team_home_win_rate | 0.712 | 0.705 | 0.708 | 0.006 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\primera2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\primera2\charts\relationships_home_win_pct_by_position.png)

