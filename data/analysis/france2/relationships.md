# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:58:54+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Ligue 2 (France)
- Scope: league `france2`

- Matches analysed: **373** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_conceded_last_5 | 0.045 | 0.089 | 0.088 |
| home_team_home_goals_avg | 0.131 | -0.006 | 0.085 |
| away_team_away_goals_avg | 0.083 | 0.013 | 0.065 |
| home_position_before_match | -0.171 | 0.088 | -0.060 |
| home_points_before_match | 0.111 | -0.028 | 0.057 |
| home_team_goals_scored_last_5 | 0.126 | -0.046 | 0.056 |
| points_difference | 0.176 | -0.108 | 0.051 |
| home_rest_days | -0.021 | -0.049 | -0.047 |
| away_rest_days | -0.017 | -0.048 | -0.043 |
| home_team_points_last_5 | 0.110 | -0.053 | 0.040 |
| away_team_wins_last_5 | -0.054 | -0.003 | -0.039 |
| away_team_away_conceded_avg | 0.013 | 0.039 | 0.034 |
| position_difference | -0.149 | 0.112 | -0.029 |
| home_team_home_win_rate | 0.048 | -0.011 | 0.026 |
| away_points_before_match | 0.000 | 0.039 | 0.025 |
| home_team_home_conceded_avg | -0.053 | 0.018 | -0.024 |
| away_team_points_last_5 | -0.026 | -0.009 | -0.024 |
| away_position_before_match | 0.029 | -0.062 | -0.021 |
| home_team_goals_conceded_last_5 | -0.016 | 0.048 | 0.020 |
| home_team_wins_last_5 | 0.062 | -0.037 | 0.019 |
| away_team_away_win_rate | 0.007 | 0.018 | 0.016 |
| rest_days_difference | -0.014 | -0.008 | -0.015 |
| away_team_goals_scored_last_5 | -0.018 | 0.041 | 0.015 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 50 | 11 | 22 | 17 | 22.0% | 44.0% | 34.0% |
| -4..-2 | 72 | 26 | 20 | 26 | 36.1% | 27.8% | 36.1% |
| -1..1 | 130 | 43 | 41 | 46 | 33.1% | 31.5% | 35.4% |
| 2..4 | 78 | 34 | 25 | 19 | 43.6% | 32.1% | 24.4% |
| >4 | 43 | 24 | 10 | 9 | 55.8% | 23.3% | 20.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 80 | 38 | 22 | 20 | 47.5% | 27.5% | 25.0% |
| -5..-2 | 71 | 30 | 19 | 22 | 42.3% | 26.8% | 31.0% |
| -1..1 | 54 | 18 | 22 | 14 | 33.3% | 40.7% | 25.9% |
| 2..5 | 80 | 33 | 22 | 25 | 41.2% | 27.5% | 31.2% |
| >=6 | 88 | 19 | 33 | 36 | 21.6% | 37.5% | 40.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 32 | 14 | 6 | 12 | 43.8% | 18.8% | 37.5% |
| -1..0 | 61 | 24 | 23 | 14 | 39.3% | 37.7% | 23.0% |
| 0 | 165 | 61 | 47 | 57 | 37.0% | 28.5% | 34.5% |
| 1..2 | 80 | 27 | 24 | 29 | 33.8% | 30.0% | 36.2% |
| >2 | 15 | 6 | 7 | 2 | 40.0% | 46.7% | 13.3% |
| unknown | 20 | 6 | 11 | 3 | 30.0% | 55.0% | 15.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **32.0%** home win (31/97)
- `>= 0.5` tier: **38.8%** home win (107/276)
- Home-win gap (>= split minus < split): **+6.8 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 97 | 31 | 32 | 34 | 32.0% |
| high | >= 0.5 | 276 | 107 | 86 | 83 | 38.8% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.036 | -0.737 | -2.385 | 4.421 |
| home_points_before_match | 21.565 | 18.085 | 17.462 | 4.104 |
| position_difference | -1.167 | 0.729 | 1.778 | 2.944 |
| home_position_before_match | 8.725 | 9.763 | 10.607 | 1.882 |
| home_team_goals_scored_last_5 | 5.848 | 4.669 | 5.154 | 1.178 |
| home_team_points_last_5 | 6.326 | 5.254 | 5.393 | 1.072 |
| away_position_before_match | 9.891 | 9.034 | 8.829 | 1.062 |
| home_team_goals_conceded_last_5 | 5.188 | 4.831 | 5.863 | 1.033 |
| away_points_before_match | 19.529 | 18.822 | 19.846 | 1.024 |
| away_team_goals_scored_last_5 | 5.181 | 5.008 | 5.786 | 0.778 |
| away_team_goals_conceded_last_5 | 5.362 | 4.822 | 5.590 | 0.768 |
| away_team_points_last_5 | 5.500 | 5.788 | 6.051 | 0.551 |
| home_team_wins_last_5 | 3.036 | 2.661 | 2.709 | 0.375 |
| home_rest_days | 7.992 | 8.168 | 7.807 | 0.361 |
| away_team_wins_last_5 | 2.732 | 2.805 | 3.009 | 0.277 |
| away_rest_days | 8.129 | 8.073 | 7.868 | 0.260 |
| rest_days_difference | -0.121 | 0.093 | -0.061 | 0.215 |
| home_team_home_goals_avg | 1.263 | 1.057 | 1.143 | 0.206 |
| home_team_home_conceded_avg | 1.101 | 0.981 | 1.151 | 0.170 |
| away_team_away_goals_avg | 1.120 | 0.961 | 1.131 | 0.170 |
| away_team_away_conceded_avg | 1.171 | 1.098 | 1.212 | 0.114 |
| away_team_away_win_rate | 0.582 | 0.535 | 0.620 | 0.086 |
| home_team_home_win_rate | 0.634 | 0.606 | 0.614 | 0.028 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\france2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\france2\charts\relationships_home_win_pct_by_position.png)

