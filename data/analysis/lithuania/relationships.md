# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:01:34+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: TOPLYGA (Lithuania)
- Scope: league `lithuania`

- Matches analysed: **180** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_away_win_rate | -0.213 | -0.111 | -0.248 |
| away_team_away_goals_avg | -0.144 | -0.158 | -0.225 |
| position_difference | -0.361 | 0.160 | -0.177 |
| points_difference | 0.374 | -0.189 | 0.167 |
| away_position_before_match | 0.229 | -0.065 | 0.138 |
| away_team_wins_last_5 | -0.152 | -0.012 | -0.130 |
| home_position_before_match | -0.298 | 0.169 | -0.120 |
| away_team_points_last_5 | -0.154 | 0.011 | -0.115 |
| home_team_home_goals_avg | 0.181 | -0.076 | 0.091 |
| home_points_before_match | 0.188 | -0.086 | 0.090 |
| home_team_goals_conceded_last_5 | -0.184 | 0.099 | -0.079 |
| away_team_goals_scored_last_5 | -0.143 | 0.054 | -0.076 |
| away_rest_days | 0.010 | -0.092 | -0.055 |
| home_rest_days | 0.053 | -0.141 | -0.054 |
| home_team_goals_scored_last_5 | 0.118 | -0.205 | -0.049 |
| away_points_before_match | -0.118 | 0.069 | -0.046 |
| home_team_wins_last_5 | 0.141 | -0.213 | -0.036 |
| home_team_home_win_rate | 0.165 | -0.225 | -0.025 |
| home_team_home_conceded_avg | -0.158 | 0.152 | -0.021 |
| home_team_points_last_5 | 0.167 | -0.220 | -0.019 |
| rest_days_difference | 0.061 | -0.085 | -0.008 |
| away_team_goals_conceded_last_5 | 0.104 | -0.110 | 0.006 |
| away_team_away_conceded_avg | 0.074 | -0.078 | 0.005 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 33 | 7 | 9 | 17 | 21.2% | 27.3% | 51.5% |
| -4..-2 | 43 | 15 | 12 | 16 | 34.9% | 27.9% | 37.2% |
| -1..1 | 50 | 22 | 12 | 16 | 44.0% | 24.0% | 32.0% |
| 2..4 | 29 | 11 | 7 | 11 | 37.9% | 24.1% | 37.9% |
| >4 | 25 | 18 | 4 | 3 | 72.0% | 16.0% | 12.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 18 | 11 | 5 | 2 | 61.1% | 27.8% | 11.1% |
| -5..-2 | 52 | 26 | 14 | 12 | 50.0% | 26.9% | 23.1% |
| -1..1 | 42 | 19 | 9 | 14 | 45.2% | 21.4% | 33.3% |
| 2..5 | 49 | 13 | 11 | 25 | 26.5% | 22.4% | 51.0% |
| >=6 | 19 | 4 | 5 | 10 | 21.1% | 26.3% | 52.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 20 | 10 | 7 | 3 | 50.0% | 35.0% | 15.0% |
| -1..0 | 34 | 12 | 10 | 12 | 35.3% | 29.4% | 35.3% |
| 0 | 58 | 26 | 11 | 21 | 44.8% | 19.0% | 36.2% |
| 1..2 | 48 | 18 | 9 | 21 | 37.5% | 18.8% | 43.8% |
| >2 | 15 | 5 | 7 | 3 | 33.3% | 46.7% | 20.0% |
| unknown | 5 | 2 | 0 | 3 | 40.0% | 0.0% | 60.0% |
- *5 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **37.2%** home win (45/121)
- `>= 0.5` tier: **47.5%** home win (28/59)
- Home-win gap (>= split minus < split): **+10.3 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 121 | 45 | 26 | 50 | 37.2% |
| high | >= 0.5 | 59 | 28 | 18 | 13 | 47.5% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 4.795 | -0.386 | -5.857 | 10.652 |
| home_points_before_match | 26.877 | 26.227 | 19.778 | 7.099 |
| away_points_before_match | 22.082 | 26.614 | 25.635 | 4.531 |
| position_difference | -1.274 | -0.295 | 1.841 | 3.115 |
| home_position_before_match | 4.822 | 5.409 | 6.651 | 1.829 |
| home_team_points_last_5 | 6.877 | 5.841 | 5.270 | 1.607 |
| away_position_before_match | 6.096 | 5.705 | 4.810 | 1.286 |
| away_team_points_last_5 | 5.959 | 7.227 | 6.921 | 1.268 |
| away_team_goals_scored_last_5 | 5.630 | 6.841 | 6.635 | 1.211 |
| home_rest_days | 7.352 | 7.977 | 6.833 | 1.144 |
| away_rest_days | 6.817 | 7.864 | 6.750 | 1.114 |
| home_team_goals_scored_last_5 | 6.233 | 5.409 | 5.206 | 1.027 |
| home_team_goals_conceded_last_5 | 5.589 | 6.045 | 6.603 | 1.014 |
| away_team_goals_conceded_last_5 | 6.370 | 5.614 | 5.540 | 0.830 |
| home_team_wins_last_5 | 1.932 | 1.636 | 1.397 | 0.535 |
| rest_days_difference | 0.535 | 0.114 | 0.083 | 0.452 |
| away_team_wins_last_5 | 1.630 | 2.045 | 1.905 | 0.415 |
| home_team_home_conceded_avg | 1.017 | 1.277 | 1.313 | 0.296 |
| home_team_home_goals_avg | 1.403 | 1.417 | 1.145 | 0.273 |
| home_team_home_win_rate | 0.454 | 0.394 | 0.287 | 0.167 |
| away_team_away_goals_avg | 1.159 | 1.291 | 1.178 | 0.131 |
| away_team_away_conceded_avg | 1.413 | 1.362 | 1.327 | 0.086 |
| away_team_away_win_rate | 0.309 | 0.361 | 0.357 | 0.052 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\lithuania\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\lithuania\charts\relationships_home_win_pct_by_position.png)

