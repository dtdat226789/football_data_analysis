# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T13:48:54+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Superettan (Sweden)
- Scope: league `sweden2`

- Matches analysed: **440** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| points_difference | 0.235 | -0.114 | 0.103 |
| rest_days_difference | 0.154 | -0.024 | 0.101 |
| home_team_goals_conceded_last_5 | -0.140 | 0.019 | -0.094 |
| away_team_away_conceded_avg | 0.091 | 0.025 | 0.086 |
| home_team_points_last_5 | 0.097 | -0.007 | 0.069 |
| away_team_away_win_rate | -0.123 | 0.040 | -0.068 |
| away_team_goals_scored_last_5 | -0.057 | 0.161 | 0.064 |
| home_rest_days | 0.074 | 0.001 | 0.057 |
| away_points_before_match | -0.095 | 0.027 | -0.055 |
| home_team_wins_last_5 | 0.081 | -0.018 | 0.050 |
| position_difference | -0.191 | 0.146 | -0.048 |
| away_position_before_match | 0.135 | -0.102 | 0.035 |
| away_team_goals_conceded_last_5 | 0.088 | -0.052 | 0.032 |
| home_position_before_match | -0.123 | 0.096 | -0.030 |
| home_team_home_goals_avg | 0.040 | -0.012 | 0.023 |
| away_rest_days | 0.021 | 0.010 | 0.022 |
| home_points_before_match | 0.079 | -0.057 | 0.022 |
| away_team_wins_last_5 | -0.101 | 0.148 | 0.022 |
| home_team_goals_scored_last_5 | 0.060 | -0.048 | 0.013 |
| home_team_home_conceded_avg | -0.053 | 0.080 | 0.013 |
| away_team_points_last_5 | -0.101 | 0.133 | 0.011 |
| home_team_home_win_rate | 0.074 | -0.070 | 0.010 |
| away_team_away_goals_avg | -0.084 | 0.090 | -0.004 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 65 | 21 | 16 | 28 | 32.3% | 24.6% | 43.1% |
| -4..-2 | 95 | 33 | 31 | 31 | 34.7% | 32.6% | 32.6% |
| -1..1 | 134 | 49 | 38 | 47 | 36.6% | 28.4% | 35.1% |
| 2..4 | 90 | 36 | 23 | 31 | 40.0% | 25.6% | 34.4% |
| >4 | 56 | 39 | 11 | 6 | 69.6% | 19.6% | 10.7% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 83 | 50 | 18 | 15 | 60.2% | 21.7% | 18.1% |
| -5..-2 | 90 | 40 | 26 | 24 | 44.4% | 28.9% | 26.7% |
| -1..1 | 89 | 32 | 24 | 33 | 36.0% | 27.0% | 37.1% |
| 2..5 | 90 | 30 | 23 | 37 | 33.3% | 25.6% | 41.1% |
| >=6 | 88 | 26 | 28 | 34 | 29.5% | 31.8% | 38.6% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 44 | 11 | 15 | 18 | 25.0% | 34.1% | 40.9% |
| -1..0 | 93 | 35 | 30 | 28 | 37.6% | 32.3% | 30.1% |
| 0 | 141 | 57 | 39 | 45 | 40.4% | 27.7% | 31.9% |
| 1..2 | 132 | 58 | 28 | 46 | 43.9% | 21.2% | 34.8% |
| >2 | 14 | 10 | 2 | 2 | 71.4% | 14.3% | 14.3% |
| unknown | 16 | 7 | 5 | 4 | 43.8% | 31.2% | 25.0% |
- *16 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **29.6%** home win (29/98)
- `>= 0.5` tier: **43.6%** home win (149/342)
- Home-win gap (>= split minus < split): **+14.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 98 | 29 | 33 | 36 | 29.6% |
| high | >= 0.5 | 342 | 149 | 86 | 107 | 43.6% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 2.854 | -1.563 | -2.762 | 5.616 |
| away_points_before_match | 16.753 | 18.202 | 20.182 | 3.429 |
| position_difference | -1.618 | 0.840 | 1.713 | 3.331 |
| home_points_before_match | 19.607 | 16.639 | 17.420 | 2.968 |
| away_position_before_match | 9.567 | 8.387 | 7.860 | 1.707 |
| home_position_before_match | 7.949 | 9.227 | 9.573 | 1.624 |
| away_team_points_last_5 | 5.601 | 6.227 | 6.748 | 1.147 |
| home_rest_days | 7.749 | 6.614 | 7.547 | 1.135 |
| away_team_goals_conceded_last_5 | 6.787 | 6.168 | 5.860 | 0.926 |
| home_team_goals_conceded_last_5 | 5.938 | 6.655 | 6.832 | 0.894 |
| away_team_goals_scored_last_5 | 6.056 | 6.555 | 6.881 | 0.825 |
| away_rest_days | 7.491 | 6.789 | 7.590 | 0.800 |
| home_team_goals_scored_last_5 | 6.612 | 6.269 | 5.881 | 0.731 |
| home_team_points_last_5 | 6.410 | 5.798 | 5.685 | 0.725 |
| away_team_wins_last_5 | 2.601 | 2.950 | 3.126 | 0.525 |
| rest_days_difference | 0.257 | -0.175 | -0.043 | 0.433 |
| home_team_wins_last_5 | 2.949 | 2.739 | 2.664 | 0.285 |
| away_team_away_conceded_avg | 1.533 | 1.280 | 1.420 | 0.254 |
| home_team_home_conceded_avg | 1.151 | 1.292 | 1.258 | 0.140 |
| away_team_away_goals_avg | 1.165 | 1.255 | 1.289 | 0.124 |
| home_team_home_win_rate | 0.693 | 0.574 | 0.609 | 0.119 |
| home_team_home_goals_avg | 1.494 | 1.378 | 1.401 | 0.116 |
| away_team_away_win_rate | 0.522 | 0.580 | 0.585 | 0.063 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\sweden2\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\sweden2\charts\relationships_home_win_pct_by_position.png)

