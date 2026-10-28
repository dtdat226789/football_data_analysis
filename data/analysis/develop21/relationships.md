# Relationships Analysis
- Report: `relationships`
- Generated: 2026-10-27T01:45:25+00:00
- Script: `backend/scripts/analyze_relationships.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

- Matches analysed: **0** (23 leakage-safe pre-match features).
- **Warning:** No matches found for league 'develop21'; report sections are empty.

## 1. Correlation matrix
_Pearson correlation of each pre-match feature with observed goals; sorted by |corr(total goals)|._

| feature | corr(home) | corr(away) | corr(total) |
|---|---|---|---|
| home_team_points_last_5 | - | - | - |
| away_team_points_last_5 | - | - | - |
| home_team_wins_last_5 | - | - | - |
| away_team_wins_last_5 | - | - | - |
| home_team_goals_scored_last_5 | - | - | - |
| away_team_goals_scored_last_5 | - | - | - |
| home_team_goals_conceded_last_5 | - | - | - |
| away_team_goals_conceded_last_5 | - | - | - |
| home_team_home_win_rate | - | - | - |
| home_team_home_goals_avg | - | - | - |
| home_team_home_conceded_avg | - | - | - |
| away_team_away_win_rate | - | - | - |
| away_team_away_goals_avg | - | - | - |
| away_team_away_conceded_avg | - | - | - |
| home_position_before_match | - | - | - |
| away_position_before_match | - | - | - |
| position_difference | - | - | - |
| home_points_before_match | - | - | - |
| away_points_before_match | - | - | - |
| points_difference | - | - | - |
| home_rest_days | - | - | - |
| away_rest_days | - | - | - |
| rest_days_difference | - | - | - |

## 2. Form vs outcome
_Home win/draw/away % per bucket of `home_team_points_last_5 - away_team_points_last_5`._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-4 | 0 | 0 | 0 | 0 | - | - | - |
| -4..-2 | 0 | 0 | 0 | 0 | - | - | - |
| -1..1 | 0 | 0 | 0 | 0 | - | - | - |
| 2..4 | 0 | 0 | 0 | 0 | - | - | - |
| >4 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 3. Position vs outcome
_Home win/draw/away % per bucket of `position_difference` (home position - away position; negative favours the home team)._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <=-6 | 0 | 0 | 0 | 0 | - | - | - |
| -5..-2 | 0 | 0 | 0 | 0 | - | - | - |
| -1..1 | 0 | 0 | 0 | 0 | - | - | - |
| 2..5 | 0 | 0 | 0 | 0 | - | - | - |
| >=6 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 4. Rest advantage
_Home win/draw/away % per bucket of `rest_days_difference` (home rest - away rest). Matches with unknown rest are bucketed separately._

| bucket | matches | home | draw | away | home % | draw % | away % |
|---|---|---|---|---|---|---|---|
| <-1 | 0 | 0 | 0 | 0 | - | - | - |
| -1..0 | 0 | 0 | 0 | 0 | - | - | - |
| 0 | 0 | 0 | 0 | 0 | - | - | - |
| 1..2 | 0 | 0 | 0 | 0 | - | - | - |
| >2 | 0 | 0 | 0 | 0 | - | - | - |
| unknown | 0 | 0 | 0 | 0 | - | - | - |

## 5. Home team quality
_Home win rate by `home_team_home_win_rate` tier (split at 0.5)._

- `< 0.5` tier: **-** home win (0/0)
- `>= 0.5` tier: **-** home win (0/0)

| tier | label | matches | home | draw | away | home % |
|---|---|---|---|---|---|---|
| low | < 0.5 | 0 | 0 | 0 | 0 | - |
| high | >= 0.5 | 0 | 0 | 0 | 0 | - |

## 6. Feature averages by result
_Mean feature value per outcome; `range` is home-minus-away spread of the group means._

| feature | home mean | draw mean | away mean | range |
|---|---|---|---|---|
| home_team_points_last_5 | - | - | - | - |
| away_team_points_last_5 | - | - | - | - |
| home_team_wins_last_5 | - | - | - | - |
| away_team_wins_last_5 | - | - | - | - |
| home_team_goals_scored_last_5 | - | - | - | - |
| away_team_goals_scored_last_5 | - | - | - | - |
| home_team_goals_conceded_last_5 | - | - | - | - |
| away_team_goals_conceded_last_5 | - | - | - | - |
| home_team_home_win_rate | - | - | - | - |
| home_team_home_goals_avg | - | - | - | - |
| home_team_home_conceded_avg | - | - | - | - |
| away_team_away_win_rate | - | - | - | - |
| away_team_away_goals_avg | - | - | - | - |
| away_team_away_conceded_avg | - | - | - | - |
| home_position_before_match | - | - | - | - |
| away_position_before_match | - | - | - | - |
| position_difference | - | - | - | - |
| home_points_before_match | - | - | - | - |
| away_points_before_match | - | - | - | - |
| points_difference | - | - | - | - |
| home_rest_days | - | - | - | - |
| away_rest_days | - | - | - | - |
| rest_days_difference | - | - | - | - |

---
*All features are leakage-safe pre-match values built by `ml.features.build_features.build_rows` from strictly prior matches. Run with `python backend/scripts/analyze_relationships.py` to regenerate.*
