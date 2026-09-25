# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-23T10:56:11+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Super League (China)
- Scope: league `china`

- Matches analysed: **448** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| away_team_goals_scored_last_5 | -0.010 | 0.175 | 0.114 |
| away_team_away_goals_avg | -0.019 | 0.160 | 0.097 |
| away_team_wins_last_5 | -0.068 | 0.204 | 0.091 |
| away_points_before_match | -0.032 | 0.162 | 0.089 |
| away_team_away_win_rate | -0.073 | 0.196 | 0.083 |
| home_points_before_match | 0.105 | 0.010 | 0.083 |
| away_team_points_last_5 | -0.064 | 0.182 | 0.080 |
| away_position_before_match | 0.073 | -0.189 | -0.078 |
| home_team_home_goals_avg | 0.061 | 0.030 | 0.065 |
| home_position_before_match | -0.144 | 0.062 | -0.062 |
| away_team_away_conceded_avg | 0.024 | -0.110 | -0.058 |
| home_team_goals_scored_last_5 | 0.085 | -0.010 | 0.055 |
| home_rest_days | 0.019 | 0.045 | 0.045 |
| away_rest_days | 0.003 | 0.059 | 0.044 |
| home_team_home_conceded_avg | 0.016 | 0.039 | 0.038 |
| home_team_home_win_rate | 0.039 | 0.005 | 0.032 |
| home_team_points_last_5 | 0.065 | -0.034 | 0.024 |
| away_team_goals_conceded_last_5 | 0.052 | -0.081 | -0.018 |
| home_team_goals_conceded_last_5 | -0.034 | 0.060 | 0.017 |
| position_difference | -0.155 | 0.179 | 0.012 |
| points_difference | 0.170 | -0.192 | -0.009 |
| rest_days_difference | 0.046 | -0.038 | 0.006 |
| home_team_wins_last_5 | 0.046 | -0.046 | 0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 66 | 22 | 11 | 33 | 33.3% | 16.7% | 50.0% |
| -4..-2 | 87 | 36 | 25 | 26 | 41.4% | 28.7% | 29.9% |
| -1..1 | 153 | 69 | 45 | 39 | 45.1% | 29.4% | 25.5% |
| 2..4 | 90 | 51 | 21 | 18 | 56.7% | 23.3% | 20.0% |
| >4 | 52 | 29 | 16 | 7 | 55.8% | 30.8% | 13.5% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 85 | 49 | 20 | 16 | 57.6% | 23.5% | 18.8% |
| -5..-2 | 84 | 48 | 22 | 14 | 57.1% | 26.2% | 16.7% |
| -1..1 | 79 | 38 | 24 | 17 | 48.1% | 30.4% | 21.5% |
| 2..5 | 98 | 39 | 30 | 29 | 39.8% | 30.6% | 29.6% |
| >=6 | 102 | 33 | 22 | 47 | 32.4% | 21.6% | 46.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 24 | 12 | 6 | 6 | 50.0% | 25.0% | 25.0% |
| -1..0 | 95 | 42 | 18 | 35 | 44.2% | 18.9% | 36.8% |
| 0 | 185 | 83 | 51 | 51 | 44.9% | 27.6% | 27.6% |
| 1..2 | 103 | 49 | 33 | 21 | 47.6% | 32.0% | 20.4% |
| >2 | 25 | 13 | 5 | 7 | 52.0% | 20.0% | 28.0% |
| unknown | 16 | 8 | 5 | 3 | 50.0% | 31.2% | 18.8% |
- *16 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **47.9%** home win (35/73)
- `>= 0.5` tier: **45.9%** home win (172/375)
- Home-win gap (>= split minus < split): **-2.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 73 | 35 | 17 | 21 | 47.9% |
| high | >= 0.5 | 375 | 172 | 101 | 102 | 45.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 1.986 | -0.364 | -4.715 | 6.701 |
| away_points_before_match | 16.836 | 19.958 | 21.431 | 4.595 |
| position_difference | -1.043 | 0.127 | 2.789 | 3.832 |
| home_points_before_match | 18.821 | 19.593 | 16.715 | 2.878 |
| away_position_before_match | 9.406 | 8.525 | 7.130 | 2.276 |
| away_team_points_last_5 | 5.614 | 6.212 | 7.382 | 1.769 |
| home_position_before_match | 8.362 | 8.653 | 9.919 | 1.556 |
| away_team_goals_scored_last_5 | 6.671 | 6.932 | 8.122 | 1.450 |
| home_team_points_last_5 | 6.101 | 6.364 | 5.488 | 0.877 |
| away_team_goals_conceded_last_5 | 7.242 | 6.797 | 6.447 | 0.794 |
| home_rest_days | 8.834 | 8.062 | 8.608 | 0.772 |
| away_rest_days | 8.573 | 7.814 | 8.567 | 0.759 |
| home_team_goals_conceded_last_5 | 7.058 | 6.924 | 7.618 | 0.694 |
| home_team_goals_scored_last_5 | 7.155 | 7.059 | 6.496 | 0.659 |
| away_team_wins_last_5 | 2.580 | 2.856 | 3.236 | 0.656 |
| home_team_wins_last_5 | 2.787 | 2.958 | 2.512 | 0.445 |
| away_team_away_goals_avg | 1.150 | 1.204 | 1.435 | 0.285 |
| rest_days_difference | 0.261 | 0.248 | 0.042 | 0.220 |
| away_team_away_win_rate | 0.444 | 0.472 | 0.597 | 0.154 |
| away_team_away_conceded_avg | 1.712 | 1.606 | 1.567 | 0.146 |
| home_team_home_conceded_avg | 1.222 | 1.161 | 1.262 | 0.101 |
| home_team_home_goals_avg | 1.669 | 1.611 | 1.635 | 0.059 |
| home_team_home_win_rate | 0.672 | 0.689 | 0.672 | 0.017 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\china\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\china\charts\relationships_home_win_pct_by_position.png)

