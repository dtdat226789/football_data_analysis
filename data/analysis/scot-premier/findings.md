# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:13:18+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premiership (Scotland)
- Scope: league `scot-premier`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/scot-premier/database_profile.json | yes | yes | 51.22 |
| matches_analysis | data/analysis/scot-premier/matches_analysis.json | yes | yes | 21.57 |
| goals_analysis | data/analysis/scot-premier/goals_analysis.json | yes | yes | 12.33 |
| teams_analysis | data/analysis/scot-premier/teams_analysis.json | yes | yes | 27.12 |
| season_trends | data/analysis/scot-premier/season_trends.json | yes | yes | 10.42 |
| scoreline_analysis | data/analysis/scot-premier/scoreline_analysis.json | yes | yes | 201.81 |
| relationships | data/analysis/scot-premier/relationships.json | yes | yes | 13.77 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1284 matches: home wins 44.7%, draws 23.9%, away wins 31.4% (574H / 307D / 403A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 33 home and 42 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 375 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1284 matches produced 3471 goals (avg 2.703 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.0% vs away 44.0% of 3471 goals in total (home/away ratio 1.27)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 628 of 1284 matches (48.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 400 scoring matches, 33.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.88, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Celtic leads with 511 points across 7 seasons (6 title(s), GD 359)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 6 teams present in every one of the 7 seasons (Aberdeen, Celtic, Hibernian, Motherwell, Rangers...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Aberdeen earns 78 more points at home than away (176 home vs 98 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Celtic won 6 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Celtic beat Hearts by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.230 per match): first half 2.608 vs last half 2.838 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2020-2021 (goals view, avg abs position diff 4.167)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.167)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 138 matches (10.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (133 of 574 home matches, 23.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (138 of 307 draw matches, 45.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (100 of 403 away matches, 24.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 21 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1214 (n=1224 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 12.064: home 5.659, draw -2.615, away -6.405
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (49)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1284 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1284 |
| Average goals per match | 2.703 |
| Home win rate | 44.7% |
| Draw rate | 23.9% |
| Away win rate | 31.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Celtic |
| Champion with most titles | Celtic |
| BTTS rate | 48.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 51.22 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 21.57 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.33 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 27.12 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.42 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 201.81 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.77 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 198 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 198 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 12 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 198 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 12 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 198 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 12 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 198 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 12 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 234 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 15 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 60 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 8.6% vs overall 6.5% (deviation 2.1 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 39.4% vs overall 44.7%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 35.9% vs overall 31.4%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 8.6% vs overall 6.5% (deviation 2.1 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 3.0% vs overall 6.5% (deviation 3.5 pp)
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 home outcome share 51.5% vs overall 44.7%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 draw outcome share 16.7% vs overall 23.9%
- **23.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.3% vs overall 6.5% (deviation 3.2 pp)
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 18.3% vs overall 23.9%
- **25.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 38.3% vs overall 31.4%
- **26.** `HIGH_SCORING_MATCHES` *(warning)* — 7 match(es) with >= 8 total goals (extreme scorelines)
- **27.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows)
- **28.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=425, fgte=425 rows)
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=12 positions=1..12 teams=12
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=12 positions=1..12 teams=12
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=12 positions=1..12 teams=12
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=12 positions=1..12 teams=12
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=12 positions=1..12 teams=12
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=12 positions=1..12 teams=12
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=12 positions=1..12 teams=12
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=12 positions=1..12 teams=12
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=12 positions=1..12 teams=12
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=12 positions=1..12 teams=12
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=12 positions=1..12 teams=12
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=12 positions=1..12 teams=12
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=12 positions=1..12 teams=12
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=12 positions=1..12 teams=12
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=12 positions=1..12 teams=12
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=15 positions=1..15 teams=15
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=15 positions=1..15 teams=15
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=15 positions=1..15 teams=15
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
