# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T04:01:30+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier League (Kuwait)
- Scope: league `kuwait`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/kuwait/database_profile.json | yes | yes | 51.73 |
| matches_analysis | data/analysis/kuwait/matches_analysis.json | yes | yes | 12.96 |
| goals_analysis | data/analysis/kuwait/goals_analysis.json | yes | yes | 12.33 |
| teams_analysis | data/analysis/kuwait/teams_analysis.json | yes | yes | 23.99 |
| season_trends | data/analysis/kuwait/season_trends.json | yes | yes | 10.45 |
| scoreline_analysis | data/analysis/kuwait/scoreline_analysis.json | yes | yes | 99.91 |
| relationships | data/analysis/kuwait/relationships.json | yes | yes | 13.70 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 594 matches: home wins 40.2%, draws 23.6%, away wins 36.2% (239H / 140D / 215A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 17 home and 10 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 152 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 594 matches produced 1713 goals (avg 2.884 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.0% vs away 48.0% of 1713 goals in total (home/away ratio 1.08)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 318 of 594 matches (53.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 179 scoring matches, 32.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.03, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Al Kuwait leads with 256 points across 7 seasons (6 title(s), GD 178)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 7 teams present in every one of the 7 seasons (Al Arabi, Al Kuwait, Al Naser, Al Qadisiya, Al Salmiya...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Al Kuwait earns 32 more points at home than away (144 home vs 112 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Al Kuwait won 6 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: Al Naser beat Al Qadisiya by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.106 per match): first half 2.866 vs last half 2.972 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022-2023 (luck view, avg abs position diff 8.700)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.583)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 72 matches (12.1%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (53 of 239 home matches, 22.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (72 of 140 draw matches, 51.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (44 of 215 away matches, 20.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 17 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — points_difference |corr| = 0.0765 (n=563 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.324: home 3.621, draw -1.657, away -3.703
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (50)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 594 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 594 |
| Average goals per match | 2.884 |
| Home win rate | 40.2% |
| Draw rate | 23.6% |
| Away win rate | 36.2% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Al Kuwait |
| Champion with most titles | Al Kuwait |
| BTTS rate | 53.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 51.73 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 12.96 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.33 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 23.99 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.45 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 99.91 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.70 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 105 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 15 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 90 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 10 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 90 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 10 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 90 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 10 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 90 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 10 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 98 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 10 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 31 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 8.6% vs overall 6.4% (deviation 2.2 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 32.4% vs overall 40.2%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 44.8% vs overall 36.2%
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 home outcome share 44.4% vs overall 40.2%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 draw outcome share 31.1% vs overall 23.6%
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 away outcome share 31.1% vs overall 36.2%
- **22.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 4.4% vs overall 6.4% (deviation 2.0 pp)
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 home outcome share 46.7% vs overall 40.2%
- **24.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.2% vs overall 6.4% (deviation 3.2 pp)
- **25.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 19.4% vs overall 23.6%
- **26.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 41.9% vs overall 36.2%
- **27.** `HIGH_SCORING_MATCHES` *(warning)* — 8 match(es) with >= 8 total goals (extreme scorelines)
- **28.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **29.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=368, fgte=368 rows)
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=15 positions=1..16 teams=15
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=15 positions=1..22 teams=15
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=15 positions=1..24 teams=15
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=10 positions=1..11 teams=10
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=10 positions=4..15 teams=10
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=10 positions=1..20 teams=10
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=10 positions=1..11 teams=10
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=10 positions=6..16 teams=10
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=10 positions=2..20 teams=10
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=10 positions=1..11 teams=10
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=10 positions=4..16 teams=10
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=10 positions=1..20 teams=10
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=10 positions=1..11 teams=10
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=10 positions=6..18 teams=10
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=10 positions=1..20 teams=10
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=10 positions=1..10 teams=10
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=10 positions=1..10 teams=10
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=10 positions=1..10 teams=10
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..13 teams=12
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..13 teams=12
- **50.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..13 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
