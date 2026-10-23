# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:43:43+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Ligue 1 (Algeria)
- Scope: league `algir1`

- Matches analysed: **240** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_rest_days | 0.217 | 0.185 | 0.270 |
| away_team_goals_conceded_last_5 | 0.254 | 0.041 | 0.207 |
| home_team_goals_conceded_last_5 | 0.004 | 0.290 | 0.182 |
| away_team_away_conceded_avg | 0.226 | 0.021 | 0.175 |
| rest_days_difference | -0.172 | -0.068 | -0.165 |
| home_points_before_match | 0.216 | -0.046 | 0.126 |
| away_points_before_match | 0.047 | 0.118 | 0.106 |
| home_team_goals_scored_last_5 | 0.131 | -0.024 | 0.079 |
| home_team_home_conceded_avg | 0.049 | 0.068 | 0.077 |
| home_rest_days | 0.020 | 0.098 | 0.075 |
| away_position_before_match | 0.187 | -0.116 | 0.062 |
| away_team_points_last_5 | -0.095 | 0.045 | -0.040 |
| home_position_before_match | -0.087 | 0.166 | 0.040 |
| away_team_wins_last_5 | -0.079 | 0.040 | -0.032 |
| points_difference | 0.240 | -0.234 | 0.027 |
| home_team_home_win_rate | 0.098 | -0.072 | 0.025 |
| home_team_home_goals_avg | 0.113 | -0.095 | 0.022 |
| away_team_away_goals_avg | -0.015 | 0.051 | 0.020 |
| position_difference | -0.197 | 0.202 | -0.016 |
| home_team_points_last_5 | 0.151 | -0.152 | 0.014 |
| away_team_goals_scored_last_5 | -0.022 | 0.045 | 0.012 |
| away_team_away_win_rate | -0.059 | 0.052 | -0.010 |
| home_team_wins_last_5 | 0.145 | -0.172 | -0.003 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 43 | 13 | 18 | 12 | 30.2% | 41.9% | 27.9% |
| -4..-2 | 44 | 22 | 9 | 13 | 50.0% | 20.5% | 29.5% |
| -1..1 | 89 | 40 | 30 | 19 | 44.9% | 33.7% | 21.3% |
| 2..4 | 39 | 29 | 9 | 1 | 74.4% | 23.1% | 2.6% |
| >4 | 25 | 16 | 4 | 5 | 64.0% | 16.0% | 20.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 45 | 29 | 11 | 5 | 64.4% | 24.4% | 11.1% |
| -5..-2 | 50 | 26 | 19 | 5 | 52.0% | 38.0% | 10.0% |
| -1..1 | 36 | 21 | 8 | 7 | 58.3% | 22.2% | 19.4% |
| 2..5 | 54 | 25 | 15 | 14 | 46.3% | 27.8% | 25.9% |
| >=6 | 55 | 19 | 17 | 19 | 34.5% | 30.9% | 34.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 40 | 21 | 11 | 8 | 52.5% | 27.5% | 20.0% |
| -1..0 | 36 | 24 | 7 | 5 | 66.7% | 19.4% | 13.9% |
| 0 | 70 | 33 | 20 | 17 | 47.1% | 28.6% | 24.3% |
| 1..2 | 43 | 19 | 15 | 9 | 44.2% | 34.9% | 20.9% |
| >2 | 42 | 20 | 13 | 9 | 47.6% | 31.0% | 21.4% |
| unknown | 9 | 3 | 4 | 2 | 33.3% | 44.4% | 22.2% |
- *9 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **47.7%** home win (61/128)
- `>= 0.5` tier: **52.7%** home win (59/112)
- Home-win gap (>= split minus < split): **+5.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 128 | 61 | 36 | 31 | 47.7% |
| high | >= 0.5 | 112 | 59 | 34 | 19 | 52.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.825 | -1.243 | -5.100 | 6.925 |
| home_points_before_match | 21.667 | 18.200 | 15.980 | 5.687 |
| position_difference | -0.817 | 0.771 | 3.100 | 3.917 |
| away_position_before_match | 9.233 | 8.014 | 7.240 | 1.993 |
| home_position_before_match | 8.417 | 8.786 | 10.340 | 1.923 |
| away_points_before_match | 19.842 | 19.443 | 21.080 | 1.637 |
| home_team_points_last_5 | 6.467 | 5.443 | 4.840 | 1.627 |
| away_rest_days | 9.966 | 8.515 | 9.750 | 1.451 |
| rest_days_difference | 0.111 | 1.424 | 0.812 | 1.313 |
| home_team_goals_conceded_last_5 | 4.892 | 4.900 | 6.040 | 1.148 |
| away_team_goals_conceded_last_5 | 5.283 | 4.329 | 4.400 | 0.955 |
| away_team_points_last_5 | 6.033 | 6.857 | 6.860 | 0.827 |
| home_team_wins_last_5 | 1.750 | 1.414 | 1.100 | 0.650 |
| home_team_goals_scored_last_5 | 5.142 | 4.586 | 4.520 | 0.622 |
| home_rest_days | 10.103 | 9.940 | 10.562 | 0.622 |
| away_team_goals_scored_last_5 | 5.008 | 5.300 | 5.380 | 0.372 |
| away_team_wins_last_5 | 1.583 | 1.871 | 1.840 | 0.288 |
| home_team_home_goals_avg | 1.187 | 1.122 | 0.990 | 0.198 |
| away_team_away_conceded_avg | 1.159 | 1.033 | 0.978 | 0.181 |
| home_team_home_win_rate | 0.462 | 0.437 | 0.365 | 0.097 |
| away_team_away_goals_avg | 0.768 | 0.852 | 0.782 | 0.084 |
| home_team_home_conceded_avg | 0.798 | 0.738 | 0.807 | 0.069 |
| away_team_away_win_rate | 0.192 | 0.239 | 0.201 | 0.047 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\algir1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\algir1\charts\relationships_home_win_pct_by_position.png)

