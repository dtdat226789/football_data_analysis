# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T15:57:45+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie B (Italy)
- Scope: league `italy2`

- Matches analysed: **390** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_points_last_5 | 0.005 | 0.146 | 0.103 |
| away_team_goals_conceded_last_5 | 0.046 | -0.194 | -0.096 |
| home_position_before_match | -0.185 | 0.086 | -0.084 |
| home_points_before_match | 0.147 | -0.054 | 0.076 |
| away_team_goals_scored_last_5 | 0.022 | 0.077 | 0.069 |
| away_team_wins_last_5 | -0.020 | 0.123 | 0.068 |
| home_rest_days | -0.062 | -0.026 | -0.065 |
| away_rest_days | -0.063 | -0.007 | -0.053 |
| away_team_away_win_rate | -0.056 | 0.136 | 0.050 |
| home_team_goals_conceded_last_5 | -0.099 | 0.043 | -0.047 |
| away_points_before_match | -0.020 | 0.092 | 0.047 |
| away_team_away_goals_avg | -0.009 | 0.077 | 0.046 |
| points_difference | 0.242 | -0.211 | 0.043 |
| rest_days_difference | 0.006 | -0.069 | -0.042 |
| home_team_home_win_rate | 0.100 | -0.052 | 0.042 |
| position_difference | -0.230 | 0.203 | -0.039 |
| home_team_points_last_5 | 0.139 | -0.106 | 0.035 |
| away_position_before_match | 0.132 | -0.195 | -0.031 |
| away_team_away_conceded_avg | 0.105 | -0.162 | -0.030 |
| home_team_goals_scored_last_5 | 0.113 | -0.103 | 0.017 |
| home_team_wins_last_5 | 0.112 | -0.110 | 0.011 |
| home_team_home_conceded_avg | -0.068 | 0.064 | -0.009 |
| home_team_home_goals_avg | 0.074 | -0.071 | 0.008 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 73 | 23 | 22 | 28 | 31.5% | 30.1% | 38.4% |
| -4..-2 | 74 | 23 | 30 | 21 | 31.1% | 40.5% | 28.4% |
| -1..1 | 112 | 59 | 31 | 22 | 52.7% | 27.7% | 19.6% |
| 2..4 | 86 | 43 | 27 | 16 | 50.0% | 31.4% | 18.6% |
| >4 | 45 | 27 | 11 | 7 | 60.0% | 24.4% | 15.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 99 | 60 | 23 | 16 | 60.6% | 23.2% | 16.2% |
| -5..-2 | 61 | 31 | 19 | 11 | 50.8% | 31.1% | 18.0% |
| -1..1 | 49 | 20 | 18 | 11 | 40.8% | 36.7% | 22.4% |
| 2..5 | 79 | 32 | 26 | 21 | 40.5% | 32.9% | 26.6% |
| >=6 | 102 | 32 | 35 | 35 | 31.4% | 34.3% | 34.3% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 6 | 3 | 2 | 1 | 50.0% | 33.3% | 16.7% |
| -1..0 | 78 | 32 | 28 | 18 | 41.0% | 35.9% | 23.1% |
| 0 | 217 | 96 | 62 | 59 | 44.2% | 28.6% | 27.2% |
| 1..2 | 76 | 37 | 26 | 13 | 48.7% | 34.2% | 17.1% |
| >2 | 3 | 2 | 1 | 0 | 66.7% | 33.3% | 0.0% |
| unknown | 10 | 5 | 2 | 3 | 50.0% | 20.0% | 30.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **40.3%** home win (106/263)
- `>= 0.5` tier: **54.3%** home win (69/127)
- Home-win gap (>= split minus < split): **+14.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 263 | 106 | 85 | 72 | 40.3% |
| high | >= 0.5 | 127 | 69 | 36 | 22 | 54.3% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.634 | -2.463 | -4.596 | 8.230 |
| home_points_before_match | 28.366 | 22.884 | 23.511 | 5.481 |
| position_difference | -1.874 | 1.256 | 3.074 | 4.949 |
| away_points_before_match | 24.731 | 25.347 | 28.106 | 3.375 |
| away_position_before_match | 11.606 | 10.124 | 8.660 | 2.946 |
| home_position_before_match | 9.731 | 11.380 | 11.734 | 2.003 |
| home_team_points_last_5 | 6.657 | 5.554 | 5.319 | 1.338 |
| away_team_goals_conceded_last_5 | 6.160 | 5.669 | 5.106 | 1.054 |
| away_team_points_last_5 | 6.149 | 6.223 | 7.096 | 0.947 |
| home_team_goals_scored_last_5 | 6.291 | 5.479 | 5.351 | 0.940 |
| home_team_goals_conceded_last_5 | 5.726 | 6.248 | 6.500 | 0.774 |
| home_team_wins_last_5 | 1.720 | 1.413 | 1.277 | 0.443 |
| away_team_goals_scored_last_5 | 5.886 | 5.983 | 6.309 | 0.423 |
| away_team_wins_last_5 | 1.554 | 1.620 | 1.872 | 0.318 |
| away_rest_days | 6.753 | 7.067 | 7.055 | 0.314 |
| away_team_away_conceded_avg | 1.438 | 1.322 | 1.216 | 0.221 |
| home_rest_days | 6.788 | 7.000 | 6.956 | 0.212 |
| home_team_home_conceded_avg | 0.953 | 1.054 | 1.095 | 0.142 |
| rest_days_difference | 0.035 | -0.067 | -0.099 | 0.134 |
| away_team_away_goals_avg | 0.973 | 1.037 | 1.080 | 0.107 |
| home_team_home_goals_avg | 1.392 | 1.329 | 1.312 | 0.080 |
| away_team_away_win_rate | 0.199 | 0.223 | 0.268 | 0.069 |
| home_team_home_win_rate | 0.431 | 0.375 | 0.377 | 0.056 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\italy2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\italy2\charts\relationships_home_win_pct_by_position.png)

