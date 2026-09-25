# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:02:05+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie B (Italy)
- Scope: league `italy2`

- Matches analysed: **440** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_wins_last_5 | 0.056 | 0.112 | 0.120 |
| away_team_goals_conceded_last_5 | 0.051 | -0.194 | -0.094 |
| away_team_points_last_5 | 0.017 | 0.114 | 0.092 |
| away_team_away_win_rate | 0.000 | 0.126 | 0.087 |
| home_position_before_match | -0.162 | 0.066 | -0.080 |
| home_points_before_match | 0.136 | -0.065 | 0.060 |
| home_rest_days | -0.053 | -0.022 | -0.056 |
| home_team_wins_last_5 | 0.147 | -0.085 | 0.055 |
| away_team_goals_scored_last_5 | 0.033 | 0.042 | 0.055 |
| away_rest_days | -0.053 | -0.009 | -0.047 |
| home_team_goals_conceded_last_5 | -0.073 | 0.014 | -0.047 |
| points_difference | 0.229 | -0.198 | 0.041 |
| away_team_away_conceded_avg | 0.090 | -0.156 | -0.038 |
| away_position_before_match | 0.123 | -0.191 | -0.036 |
| away_points_before_match | -0.009 | 0.061 | 0.035 |
| position_difference | -0.211 | 0.188 | -0.033 |
| home_team_points_last_5 | 0.131 | -0.100 | 0.032 |
| rest_days_difference | 0.001 | -0.046 | -0.031 |
| away_team_away_goals_avg | 0.016 | 0.019 | 0.026 |
| home_team_goals_scored_last_5 | 0.110 | -0.105 | 0.013 |
| home_team_home_conceded_avg | -0.016 | 0.035 | 0.012 |
| home_team_home_win_rate | 0.078 | -0.076 | 0.008 |
| home_team_home_goals_avg | 0.085 | -0.085 | 0.007 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 73 | 23 | 22 | 28 | 31.5% | 30.1% | 38.4% |
| -4..-2 | 89 | 29 | 35 | 25 | 32.6% | 39.3% | 28.1% |
| -1..1 | 135 | 69 | 35 | 31 | 51.1% | 25.9% | 23.0% |
| 2..4 | 95 | 46 | 31 | 18 | 48.4% | 32.6% | 18.9% |
| >4 | 48 | 29 | 11 | 8 | 60.4% | 22.9% | 16.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 113 | 66 | 27 | 20 | 58.4% | 23.9% | 17.7% |
| -5..-2 | 65 | 32 | 21 | 12 | 49.2% | 32.3% | 18.5% |
| -1..1 | 60 | 24 | 19 | 17 | 40.0% | 31.7% | 28.3% |
| 2..5 | 90 | 38 | 29 | 23 | 42.2% | 32.2% | 25.6% |
| >=6 | 112 | 36 | 38 | 38 | 32.1% | 33.9% | 33.9% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 8 | 4 | 3 | 1 | 50.0% | 37.5% | 12.5% |
| -1..0 | 87 | 38 | 30 | 19 | 43.7% | 34.5% | 21.8% |
| 0 | 229 | 99 | 68 | 62 | 43.2% | 29.7% | 27.1% |
| 1..2 | 93 | 44 | 29 | 20 | 47.3% | 31.2% | 21.5% |
| >2 | 3 | 2 | 1 | 0 | 66.7% | 33.3% | 0.0% |
| unknown | 20 | 9 | 3 | 8 | 45.0% | 15.0% | 40.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **38.6%** home win (27/70)
- `>= 0.5` tier: **45.7%** home win (169/370)
- Home-win gap (>= split minus < split): **+7.1 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 70 | 27 | 22 | 21 | 38.6% |
| high | >= 0.5 | 370 | 169 | 112 | 89 | 45.7% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.260 | -2.216 | -3.918 | 7.178 |
| home_points_before_match | 25.628 | 21.037 | 20.391 | 5.237 |
| position_difference | -1.719 | 1.127 | 2.645 | 4.365 |
| away_position_before_match | 11.495 | 10.157 | 8.709 | 2.786 |
| away_points_before_match | 22.367 | 23.254 | 24.309 | 1.942 |
| home_position_before_match | 9.776 | 11.284 | 11.355 | 1.579 |
| home_team_points_last_5 | 6.245 | 5.388 | 4.845 | 1.399 |
| away_team_goals_conceded_last_5 | 5.816 | 5.440 | 4.645 | 1.171 |
| home_team_goals_scored_last_5 | 5.908 | 5.261 | 4.818 | 1.090 |
| away_team_points_last_5 | 5.776 | 5.985 | 6.355 | 0.579 |
| home_team_wins_last_5 | 3.010 | 2.627 | 2.482 | 0.528 |
| home_team_goals_conceded_last_5 | 5.408 | 5.918 | 5.818 | 0.510 |
| away_rest_days | 6.797 | 7.053 | 7.000 | 0.257 |
| away_team_away_conceded_avg | 1.387 | 1.272 | 1.140 | 0.248 |
| away_team_goals_scored_last_5 | 5.551 | 5.754 | 5.655 | 0.203 |
| home_rest_days | 6.824 | 6.985 | 6.971 | 0.161 |
| home_team_home_goals_avg | 1.330 | 1.308 | 1.171 | 0.159 |
| away_team_wins_last_5 | 2.847 | 2.836 | 2.991 | 0.155 |
| home_team_home_conceded_avg | 0.941 | 1.060 | 1.004 | 0.119 |
| rest_days_difference | 0.027 | -0.069 | -0.029 | 0.095 |
| away_team_away_goals_avg | 0.958 | 1.052 | 0.968 | 0.094 |
| home_team_home_win_rate | 0.705 | 0.687 | 0.624 | 0.082 |
| away_team_away_win_rate | 0.502 | 0.551 | 0.553 | 0.050 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\italy2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\italy2\charts\relationships_home_win_pct_by_position.png)

