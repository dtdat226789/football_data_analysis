# Relationships Analysis
- Report: `relationships`
- Generated: 2026-09-29T16:08:55+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: LaLiga (Spain)
- Scope: league `spain1`

- Matches analysed: **380** (23 leakage-safe pre-match features).

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_position_before_match | -0.294 | 0.010 | -0.226 |
| home_team_home_goals_avg | 0.296 | -0.062 | 0.194 |
| home_team_goals_scored_last_5 | 0.247 | -0.013 | 0.187 |
| home_team_points_last_5 | 0.244 | -0.019 | 0.181 |
| home_team_wins_last_5 | 0.235 | -0.019 | 0.173 |
| points_difference | 0.304 | -0.112 | 0.168 |
| home_team_home_win_rate | 0.273 | -0.079 | 0.165 |
| position_difference | -0.293 | 0.108 | -0.162 |
| home_points_before_match | 0.221 | -0.024 | 0.160 |
| home_team_home_conceded_avg | -0.200 | 0.089 | -0.100 |
| home_team_goals_conceded_last_5 | -0.145 | 0.026 | -0.097 |
| rest_days_difference | -0.051 | -0.024 | -0.056 |
| home_rest_days | -0.047 | -0.029 | -0.055 |
| away_team_away_goals_avg | -0.057 | 0.122 | 0.034 |
| away_rest_days | -0.021 | -0.017 | -0.028 |
| away_points_before_match | -0.018 | 0.064 | 0.027 |
| away_team_goals_scored_last_5 | -0.063 | 0.119 | 0.027 |
| away_team_away_conceded_avg | 0.007 | -0.049 | -0.026 |
| away_team_away_win_rate | -0.045 | 0.084 | 0.019 |
| away_team_wins_last_5 | -0.084 | 0.082 | -0.014 |
| away_team_goals_conceded_last_5 | 0.003 | -0.000 | 0.002 |
| away_team_points_last_5 | -0.060 | 0.076 | 0.002 |
| away_position_before_match | 0.117 | -0.144 | -0.001 |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 66 | 25 | 21 | 20 | 37.9% | 31.8% | 30.3% |
| -4..-2 | 79 | 34 | 20 | 25 | 43.0% | 25.3% | 31.6% |
| -1..1 | 113 | 54 | 25 | 34 | 47.8% | 22.1% | 30.1% |
| 2..4 | 78 | 41 | 19 | 18 | 52.6% | 24.4% | 23.1% |
| >4 | 44 | 32 | 8 | 4 | 72.7% | 18.2% | 9.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 88 | 61 | 13 | 14 | 69.3% | 14.8% | 15.9% |
| -5..-2 | 68 | 40 | 13 | 15 | 58.8% | 19.1% | 22.1% |
| -1..1 | 45 | 17 | 14 | 14 | 37.8% | 31.1% | 31.1% |
| 2..5 | 70 | 25 | 22 | 23 | 35.7% | 31.4% | 32.9% |
| >=6 | 109 | 43 | 31 | 35 | 39.4% | 28.4% | 32.1% |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 35 | 20 | 9 | 6 | 57.1% | 25.7% | 17.1% |
| -1..0 | 97 | 46 | 27 | 24 | 47.4% | 27.8% | 24.7% |
| 0 | 105 | 49 | 26 | 30 | 46.7% | 24.8% | 28.6% |
| 1..2 | 122 | 61 | 26 | 35 | 50.0% | 21.3% | 28.7% |
| >2 | 11 | 5 | 3 | 3 | 45.5% | 27.3% | 27.3% |
| unknown | 10 | 5 | 2 | 3 | 50.0% | 20.0% | 30.0% |
- *10 match(es) had unknown rest difference (missing rest data on at least one side).*

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **41.9%** home win (93/222)
- `>= 0.5` tier: **58.9%** home win (93/158)
- Home-win gap (>= split minus < split): **+17.0 pp**

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 222 | 93 | 65 | 64 | 41.9% |
| high | >= 0.5 | 158 | 93 | 28 | 37 | 58.9% |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| points_difference | 3.339 | -3.022 | -4.683 | 8.022 |
| home_points_before_match | 28.344 | 20.495 | 23.743 | 7.849 |
| away_points_before_match | 25.005 | 23.516 | 28.426 | 4.910 |
| position_difference | -1.720 | 2.398 | 2.386 | 4.118 |
| home_position_before_match | 9.624 | 13.355 | 11.099 | 3.731 |
| away_position_before_match | 11.344 | 10.957 | 8.713 | 2.631 |
| home_team_points_last_5 | 6.817 | 5.032 | 6.040 | 1.785 |
| home_team_goals_scored_last_5 | 6.720 | 5.054 | 5.911 | 1.667 |
| away_team_points_last_5 | 6.258 | 6.065 | 7.337 | 1.272 |
| away_team_goals_scored_last_5 | 5.984 | 6.108 | 7.030 | 1.046 |
| home_team_goals_conceded_last_5 | 5.919 | 6.731 | 6.505 | 0.812 |
| home_team_wins_last_5 | 1.914 | 1.237 | 1.653 | 0.677 |
| away_team_goals_conceded_last_5 | 6.156 | 6.409 | 5.772 | 0.636 |
| away_rest_days | 7.348 | 7.879 | 7.459 | 0.531 |
| home_team_home_goals_avg | 1.647 | 1.149 | 1.313 | 0.498 |
| away_team_wins_last_5 | 1.667 | 1.656 | 2.109 | 0.453 |
| home_rest_days | 7.409 | 7.857 | 7.714 | 0.448 |
| rest_days_difference | 0.061 | -0.022 | 0.255 | 0.277 |
| away_team_away_goals_avg | 1.007 | 0.997 | 1.246 | 0.249 |
| home_team_home_conceded_avg | 0.963 | 1.168 | 1.170 | 0.207 |
| home_team_home_win_rate | 0.521 | 0.355 | 0.399 | 0.166 |
| away_team_away_conceded_avg | 1.442 | 1.470 | 1.367 | 0.104 |
| away_team_away_win_rate | 0.232 | 0.226 | 0.310 | 0.085 |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*

## Charts

![relationships_home_win_pct_by_form](E:\football_data_analysis\data\analysis\spain1\charts\relationships_home_win_pct_by_form.png)
![relationships_home_win_pct_by_position](E:\football_data_analysis\data\analysis\spain1\charts\relationships_home_win_pct_by_position.png)

