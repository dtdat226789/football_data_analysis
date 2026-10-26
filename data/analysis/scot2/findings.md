# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:47:04+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: League Two (Scotland)
- Scope: league `scot2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/scot2/database_profile.json | yes | yes | 52.80 |
| matches_analysis | data/analysis/scot2/matches_analysis.json | yes | yes | 16.47 |
| goals_analysis | data/analysis/scot2/goals_analysis.json | yes | yes | 12.38 |
| teams_analysis | data/analysis/scot2/teams_analysis.json | yes | yes | 30.17 |
| season_trends | data/analysis/scot2/season_trends.json | yes | yes | 10.42 |
| scoreline_analysis | data/analysis/scot2/scoreline_analysis.json | yes | yes | 165.06 |
| relationships | data/analysis/scot2/relationships.json | yes | yes | 13.71 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1053 matches: home wins 42.6%, draws 25.3%, away wins 32.1% (449H / 266D / 338A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 28 home and 18 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 278 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1053 matches produced 2875 goals (avg 2.730 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.9% vs away 46.1% of 2875 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 553 of 1053 matches (52.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 325 scoring matches, 33.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.71, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Stranraer leads with 269 points across 7 seasons (1 title(s), GD -13)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 2 teams present in every one of the 7 seasons (Elgin City, Stranraer)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Elgin City earns 67 more points at home than away (165 home vs 98 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Queen's Park won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Stranraer beat Clyde by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.289 per match): first half 2.68 vs last half 2.969 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.167)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020-2021 (luck view, avg abs position diff 0.400)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 128 matches (12.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-0 (100 of 449 home matches, 22.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (128 of 266 draw matches, 48.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (81 of 338 away matches, 24.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 21 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0777 (n=998 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 4.254: home 24.666, draw 23.004, away 20.412
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (55)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1053 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1053 |
| Average goals per match | 2.73 |
| Home win rate | 42.6% |
| Draw rate | 25.3% |
| Away win rate | 32.1% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Stranraer |
| Champion with most titles | Queen's Park |
| BTTS rate | 52.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 52.80 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 16.47 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.38 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 30.17 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.42 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 165.06 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.71 |

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
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 188 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 12 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 55 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 10 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 20.0% vs overall 25.3%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 41.1% vs overall 32.1%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 home outcome share 37.8% vs overall 42.6%
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 away outcome share 37.2% vs overall 32.1%
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 4.4% vs overall 6.4% (deviation 2.0 pp)
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 9.4% vs overall 6.4% (deviation 3.0 pp)
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 draw outcome share 32.2% vs overall 25.3%
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 away outcome share 27.2% vs overall 32.1%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 home outcome share 50.0% vs overall 42.6%
- **25.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 draw outcome share 20.6% vs overall 25.3%
- **26.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 4.8% vs overall 6.4% (deviation 1.6 pp)
- **27.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.364 vs overall 2.73 (deviation 0.634)
- **28.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.6% vs overall 6.4% (deviation 2.8 pp)
- **29.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 54.5% vs overall 42.6%
- **30.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 18.2% vs overall 25.3%
- **31.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 27.3% vs overall 32.1%
- **32.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **33.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows)
- **34.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=426, fgte=426 rows)
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=10 positions=1..10 teams=10
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=10 positions=1..10 teams=10
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=10 positions=1..10 teams=10
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=10 positions=1..10 teams=10
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=10 positions=1..10 teams=10
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=10 positions=1..10 teams=10
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=10 positions=1..10 teams=10
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=10 positions=1..10 teams=10
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=10 positions=1..10 teams=10
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=10 positions=1..10 teams=10
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=10 positions=1..10 teams=10
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=10 positions=1..10 teams=10
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=10 positions=1..10 teams=10
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=10 positions=1..10 teams=10
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=10 positions=1..10 teams=10
- **50.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=12 positions=1..12 teams=12
- **51.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=12 positions=1..12 teams=12
- **52.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=12 positions=1..12 teams=12
- **53.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=10 positions=1..10 teams=10
- **54.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=10 positions=1..10 teams=10
- **55.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
