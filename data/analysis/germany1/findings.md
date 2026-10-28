# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:49:16+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Bundesliga (Germany)
- Scope: league `germany1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/germany1/database_profile.json | yes | yes | 50.63 |
| matches_analysis | data/analysis/germany1/matches_analysis.json | yes | yes | 25.04 |
| goals_analysis | data/analysis/germany1/goals_analysis.json | yes | yes | 12.33 |
| teams_analysis | data/analysis/germany1/teams_analysis.json | yes | yes | 36.15 |
| season_trends | data/analysis/germany1/season_trends.json | yes | yes | 10.53 |
| scoreline_analysis | data/analysis/germany1/scoreline_analysis.json | yes | yes | 267.62 |
| relationships | data/analysis/germany1/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1690 matches: home wins 43.8%, draws 24.7%, away wins 31.5% (741H / 417D / 532A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 57 home and 36 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 467 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1690 matches produced 5309 goals (avg 3.141 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.6% vs away 44.4% of 5309 goals in total (home/away ratio 1.25)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1006 of 1690 matches (59.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 577 scoring matches, 36.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.31, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Bayern Munich leads with 463 points across 7 seasons (6 title(s), GD 375)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 11 teams present in every one of the 7 seasons (Augsburg, Bayer Leverkusen, Bayern Munich, Dortmund, Eintracht Frankfurt...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — RB Leipzig earns 63 more points at home than away (211 home vs 148 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Bayern Munich won 6 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2022-2023: Bayern Munich beat Dortmund by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.190 per match): first half 3.077 vs last half 3.267 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022-2023 (goals view, avg abs position diff 4.824)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 2.222)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 199 matches (11.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (144 of 741 home matches, 19.4%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (199 of 417 draw matches, 47.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (101 of 532 away matches, 19.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 68 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.1375 (n=1634 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 9.604: home 3.747, draw 0.218, away -5.857
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (46)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1690 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1690 |
| Average goals per match | 3.141 |
| Home win rate | 43.8% |
| Draw rate | 24.7% |
| Away win rate | 31.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Bayern Munich |
| Champion with most titles | Bayern Munich |
| BTTS rate | 59.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.63 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 25.04 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.33 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 36.15 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.53 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 267.62 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 272 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 17 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 272 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 17 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 272 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 17 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 272 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 17 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 272 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 17 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 274 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 56 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 17 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 7.7% vs overall 5.2% (deviation 2.5 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 home outcome share 37.9% vs overall 43.8%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 away outcome share 36.0% vs overall 31.5%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 2.9% vs overall 5.2% (deviation 2.3 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 8.9% vs overall 5.2% (deviation 3.7 pp)
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 51.8% vs overall 43.8%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 25.0% vs overall 31.5%
- **23.** `HIGH_SCORING_MATCHES` *(warning)* — 14 match(es) with >= 8 total goals (extreme scorelines)
- **24.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **25.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=327, fgte=327 rows)
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=17 positions=1..17 teams=17
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=17 positions=1..17 teams=17
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=17 positions=1..17 teams=17
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=17 positions=1..17 teams=17
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=17 positions=1..17 teams=17
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=17 positions=1..17 teams=17
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=17 positions=1..17 teams=17
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=17 positions=1..17 teams=17
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=17 positions=1..17 teams=17
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=17 positions=1..17 teams=17
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=17 positions=1..17 teams=17
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=17 positions=1..17 teams=17
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=17 positions=1..17 teams=17
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=17 positions=1..17 teams=17
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=17 positions=1..17 teams=17
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=17 positions=1..17 teams=17
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=17 positions=1..17 teams=17
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=17 positions=1..17 teams=17

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
