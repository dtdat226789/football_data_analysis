# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:46:48+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: League One (Scotland)
- Scope: league `scot1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/scot1/database_profile.json | yes | yes | 49.04 |
| matches_analysis | data/analysis/scot1/matches_analysis.json | yes | yes | 14.99 |
| goals_analysis | data/analysis/scot1/goals_analysis.json | yes | yes | 12.30 |
| teams_analysis | data/analysis/scot1/teams_analysis.json | yes | yes | 34.29 |
| season_trends | data/analysis/scot1/season_trends.json | yes | yes | 10.42 |
| scoreline_analysis | data/analysis/scot1/scoreline_analysis.json | yes | yes | 167.33 |
| relationships | data/analysis/scot1/relationships.json | yes | yes | 13.74 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1060 matches: home wins 42.0%, draws 25.0%, away wins 33.0% (445H / 265D / 350A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 18 home and 20 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 263 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1060 matches produced 2990 goals (avg 2.821 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.9% vs away 47.1% of 2990 goals in total (home/away ratio 1.12)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 561 of 1060 matches (52.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 344 scoring matches, 34.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.75, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Montrose leads with 288 points across 7 seasons (0 title(s), GD -17)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 1 teams present in every one of the 7 seasons (Montrose)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Peterhead earns 36 more points at home than away (85 home vs 49 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Partick Thistle won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Ross County beat Hamilton by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.013 per match): first half 2.722 vs last half 2.735 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.571)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2024-2025 (luck view, avg abs position diff 0.800)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 134 matches (12.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (96 of 445 home matches, 21.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (134 of 265 draw matches, 50.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-2 (68 of 350 away matches, 19.4%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 25 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.1081 (n=1001 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 9.701: home 4.144, draw -0.601, away -5.558
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (42)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1060 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1060 |
| Average goals per match | 2.821 |
| Home win rate | 42.0% |
| Draw rate | 25.0% |
| Away win rate | 33.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Montrose |
| Champion with most titles | Partick Thistle |
| BTTS rate | 52.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.04 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 14.99 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.30 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 34.29 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.42 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 167.33 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.74 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 90 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 180 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 10 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 180 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 10 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 180 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 10 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 180 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 10 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 191 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 14 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 59 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 10 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2020-2021 avg goals 2.389 vs overall 2.821 (deviation 0.432)
- **17.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2023-2024 avg goals 3.172 vs overall 2.821 (deviation 0.351)
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 20.3% vs overall 25.0%
- **19.** `HIGH_SCORING_MATCHES` *(warning)* — 7 match(es) with >= 8 total goals (extreme scorelines)
- **20.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows)
- **21.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=426, fgte=426 rows)
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=10 positions=1..10 teams=10
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=10 positions=1..10 teams=10
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=10 positions=1..10 teams=10
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=10 positions=1..10 teams=10
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=10 positions=1..10 teams=10
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=10 positions=1..10 teams=10
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=10 positions=1..10 teams=10
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=10 positions=1..10 teams=10
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=10 positions=1..10 teams=10
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=10 positions=1..10 teams=10
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=10 positions=1..10 teams=10
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=10 positions=1..10 teams=10
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=10 positions=1..10 teams=10
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=10 positions=1..10 teams=10
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=10 positions=1..10 teams=10
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=14 positions=1..14 teams=14
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=14 positions=1..14 teams=14
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=14 positions=1..14 teams=14
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=10 positions=1..10 teams=10
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=10 positions=1..10 teams=10
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
