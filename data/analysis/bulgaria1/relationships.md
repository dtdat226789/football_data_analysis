# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:55:51+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: efbet League (Bulgaria)
- Scope: league `bulgaria1`

- Matches analysed: **363** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_goals_scored_last_5 | 0.201 | -0.088 | 0.094 |
| home_team_points_last_5 | 0.202 | -0.106 | 0.081 |
| home_team_home_goals_avg | 0.173 | -0.091 | 0.069 |
| home_team_goals_conceded_last_5 | -0.158 | 0.086 | -0.061 |
| home_points_before_match | 0.031 | -0.114 | -0.059 |
| away_team_goals_conceded_last_5 | 0.022 | -0.093 | -0.052 |
| away_points_before_match | -0.118 | 0.063 | -0.047 |
| home_team_wins_last_5 | 0.137 | -0.086 | 0.045 |
| home_position_before_match | -0.220 | 0.175 | -0.045 |
| rest_days_difference | 0.028 | -0.080 | -0.038 |
| away_team_away_conceded_avg | 0.078 | -0.133 | -0.037 |
| away_rest_days | 0.011 | 0.018 | 0.021 |
| position_difference | -0.268 | 0.259 | -0.021 |
| points_difference | 0.240 | -0.284 | -0.020 |
| away_team_wins_last_5 | -0.105 | 0.085 | -0.020 |
| away_position_before_match | 0.133 | -0.166 | -0.018 |
| home_team_home_win_rate | 0.082 | -0.066 | 0.016 |
| away_team_away_win_rate | -0.128 | 0.116 | -0.015 |
| home_team_home_conceded_avg | -0.124 | 0.113 | -0.015 |
| home_rest_days | 0.016 | -0.002 | 0.011 |
| away_team_points_last_5 | -0.093 | 0.107 | 0.006 |
| away_team_away_goals_avg | -0.078 | 0.081 | -0.002 |
| away_team_goals_scored_last_5 | -0.091 | 0.097 | -0.000 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 61 | 12 | 18 | 31 | 19.7% | 29.5% | 50.8% |
| -4..-2 | 76 | 25 | 21 | 30 | 32.9% | 27.6% | 39.5% |
| -1..1 | 98 | 50 | 32 | 16 | 51.0% | 32.7% | 16.3% |
| 2..4 | 66 | 29 | 17 | 20 | 43.9% | 25.8% | 30.3% |
| >4 | 62 | 40 | 11 | 11 | 64.5% | 17.7% | 17.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 68 | 45 | 13 | 10 | 66.2% | 19.1% | 14.7% |
| -5..-2 | 86 | 45 | 24 | 17 | 52.3% | 27.9% | 19.8% |
| -1..1 | 68 | 28 | 27 | 13 | 41.2% | 39.7% | 19.1% |
| 2..5 | 72 | 24 | 18 | 30 | 33.3% | 25.0% | 41.7% |
| >=6 | 69 | 14 | 17 | 38 | 20.3% | 24.6% | 55.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 46 | 17 | 16 | 13 | 37.0% | 34.8% | 28.3% |
| -1..0 | 85 | 38 | 18 | 29 | 44.7% | 21.2% | 34.1% |
| 0 | 95 | 46 | 21 | 28 | 48.4% | 22.1% | 29.5% |
| 1..2 | 104 | 40 | 31 | 33 | 38.5% | 29.8% | 31.7% |
| >2 | 17 | 8 | 4 | 5 | 47.1% | 23.5% | 29.4% |
| unknown | 16 | 7 | 9 | 0 | 43.8% | 56.2% | 0.0% |
- *16 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **32.3%** home win (21/65)
- `>= 0.5` tier: **45.3%** home win (135/298)
- Home-win gap (>= split minus < split): **+13.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 65 | 21 | 24 | 20 | 32.3% |
| high | >= 0.5 | 298 | 135 | 75 | 88 | 45.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.744 | -0.646 | -5.009 | 8.753 |
| position_difference | -2.051 | 0.323 | 2.981 | 5.033 |
| away_points_before_match | 19.173 | 19.242 | 23.657 | 4.484 |
| home_points_before_match | 22.917 | 18.596 | 18.648 | 4.321 |
| home_position_before_match | 7.365 | 8.970 | 10.194 | 2.829 |
| away_position_before_match | 9.417 | 8.646 | 7.213 | 2.204 |
| home_team_points_last_5 | 6.756 | 5.313 | 5.176 | 1.580 |
| away_team_points_last_5 | 5.481 | 5.939 | 6.889 | 1.408 |
| home_team_goals_scored_last_5 | 5.859 | 4.677 | 4.528 | 1.331 |
| home_team_goals_conceded_last_5 | 4.750 | 5.182 | 6.009 | 1.259 |
| away_team_goals_scored_last_5 | 4.821 | 5.091 | 5.981 | 1.161 |
| home_rest_days | 8.113 | 8.256 | 8.861 | 0.748 |
| away_rest_days | 8.067 | 8.222 | 8.778 | 0.711 |
| away_team_goals_conceded_last_5 | 5.333 | 5.212 | 4.806 | 0.528 |
| home_team_wins_last_5 | 3.013 | 2.505 | 2.565 | 0.508 |
| away_team_wins_last_5 | 2.635 | 2.788 | 3.130 | 0.495 |
| home_team_home_goals_avg | 1.406 | 1.055 | 1.084 | 0.351 |
| home_team_home_conceded_avg | 0.882 | 0.889 | 1.153 | 0.271 |
| away_team_away_conceded_avg | 1.338 | 1.165 | 1.123 | 0.215 |
| away_team_away_goals_avg | 0.893 | 0.955 | 1.067 | 0.174 |
| away_team_away_win_rate | 0.466 | 0.538 | 0.600 | 0.134 |
| home_team_home_win_rate | 0.724 | 0.616 | 0.653 | 0.108 |
| rest_days_difference | 0.060 | 0.033 | 0.083 | 0.050 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\bulgaria1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\bulgaria1\charts\relationships_home_win_pct_by_position.png)

