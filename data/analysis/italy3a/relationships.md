# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T11:02:14+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Serie C - Group A (Italy)
- Scope: league `italy3a`

- Matches analysed: **440** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_wins_last_5 | 0.006 | -0.093 | -0.059 |
| away_team_points_last_5 | -0.149 | 0.075 | -0.057 |
| home_team_goals_conceded_last_5 | -0.059 | 0.146 | 0.056 |
| home_position_before_match | -0.068 | 0.153 | 0.053 |
| away_team_goals_scored_last_5 | -0.082 | 0.013 | -0.051 |
| home_team_points_last_5 | 0.023 | -0.095 | -0.047 |
| away_points_before_match | -0.050 | 0.109 | 0.037 |
| away_position_before_match | 0.146 | -0.105 | 0.035 |
| away_rest_days | 0.049 | -0.100 | -0.032 |
| away_team_away_win_rate | -0.107 | 0.069 | -0.032 |
| points_difference | 0.158 | -0.214 | -0.029 |
| home_rest_days | 0.055 | -0.095 | -0.025 |
| away_team_goals_conceded_last_5 | 0.097 | -0.070 | 0.023 |
| home_team_home_conceded_avg | -0.049 | 0.086 | 0.022 |
| home_team_home_win_rate | -0.019 | -0.011 | -0.021 |
| away_team_wins_last_5 | -0.112 | 0.090 | -0.021 |
| home_points_before_match | 0.056 | -0.035 | 0.018 |
| position_difference | -0.161 | 0.194 | 0.014 |
| rest_days_difference | 0.008 | 0.010 | 0.013 |
| home_team_home_goals_avg | 0.048 | -0.067 | -0.010 |
| home_team_goals_scored_last_5 | 0.007 | 0.007 | 0.010 |
| away_team_away_goals_avg | -0.025 | 0.014 | -0.009 |
| away_team_away_conceded_avg | 0.097 | -0.095 | 0.007 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 60 | 15 | 21 | 24 | 25.0% | 35.0% | 40.0% |
| -4..-2 | 98 | 26 | 30 | 42 | 26.5% | 30.6% | 42.9% |
| -1..1 | 125 | 49 | 41 | 35 | 39.2% | 32.8% | 28.0% |
| 2..4 | 96 | 48 | 25 | 23 | 50.0% | 26.0% | 24.0% |
| >4 | 61 | 26 | 21 | 14 | 42.6% | 34.4% | 23.0% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 102 | 52 | 32 | 18 | 51.0% | 31.4% | 17.6% |
| -5..-2 | 74 | 30 | 23 | 21 | 40.5% | 31.1% | 28.4% |
| -1..1 | 70 | 27 | 22 | 21 | 38.6% | 31.4% | 30.0% |
| 2..5 | 81 | 29 | 25 | 27 | 35.8% | 30.9% | 33.3% |
| >=6 | 113 | 26 | 36 | 51 | 23.0% | 31.9% | 45.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 25 | 8 | 6 | 11 | 32.0% | 24.0% | 44.0% |
| -1..0 | 84 | 34 | 24 | 26 | 40.5% | 28.6% | 31.0% |
| 0 | 203 | 73 | 67 | 63 | 36.0% | 33.0% | 31.0% |
| 1..2 | 101 | 38 | 35 | 28 | 37.6% | 34.7% | 27.7% |
| >2 | 7 | 2 | 1 | 4 | 28.6% | 14.3% | 57.1% |
| unknown | 20 | 9 | 5 | 6 | 45.0% | 25.0% | 30.0% |
- *20 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **33.7%** home win (29/86)
- `>= 0.5` tier: **38.1%** home win (135/354)
- Home-win gap (>= split minus < split): **+4.4 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 86 | 29 | 33 | 24 | 33.7% |
| high | >= 0.5 | 354 | 135 | 105 | 114 | 38.1% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.878 | 0.232 | -4.123 | 7.001 |
| away_points_before_match | 21.323 | 19.826 | 24.877 | 5.051 |
| position_difference | -1.909 | 0.181 | 2.630 | 4.539 |
| home_points_before_match | 24.201 | 20.058 | 20.754 | 4.143 |
| away_position_before_match | 11.451 | 11.051 | 8.949 | 2.502 |
| home_position_before_match | 9.543 | 11.232 | 11.580 | 2.037 |
| away_team_points_last_5 | 5.305 | 5.674 | 6.638 | 1.333 |
| away_team_goals_conceded_last_5 | 5.244 | 5.000 | 4.304 | 0.940 |
| home_team_goals_conceded_last_5 | 4.585 | 5.043 | 5.486 | 0.900 |
| home_rest_days | 6.845 | 6.414 | 6.205 | 0.641 |
| home_team_points_last_5 | 6.146 | 5.580 | 5.558 | 0.588 |
| away_team_wins_last_5 | 2.683 | 2.732 | 3.159 | 0.476 |
| away_rest_days | 6.787 | 6.398 | 6.318 | 0.469 |
| away_team_goals_scored_last_5 | 4.848 | 4.790 | 5.217 | 0.428 |
| home_team_wins_last_5 | 2.963 | 2.739 | 2.703 | 0.261 |
| home_team_goals_scored_last_5 | 5.018 | 4.797 | 5.007 | 0.221 |
| away_team_away_conceded_avg | 1.229 | 1.083 | 1.027 | 0.201 |
| home_team_home_goals_avg | 1.229 | 1.047 | 1.102 | 0.182 |
| rest_days_difference | 0.058 | 0.015 | -0.114 | 0.172 |
| home_team_home_conceded_avg | 0.890 | 0.993 | 1.043 | 0.153 |
| away_team_away_win_rate | 0.542 | 0.573 | 0.647 | 0.105 |
| away_team_away_goals_avg | 0.949 | 0.949 | 1.025 | 0.076 |
| home_team_home_win_rate | 0.638 | 0.590 | 0.641 | 0.051 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\italy3a\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\italy3a\charts\relationships_home_win_pct_by_position.png)

