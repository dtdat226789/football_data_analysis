# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:15:46+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Mozzart Bet Super Liga (Serbia)
- Scope: league `serbia1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/serbia1/database_profile.json | yes | yes | 50.07 |
| matches_analysis | data/analysis/serbia1/matches_analysis.json | yes | yes | 20.10 |
| goals_analysis | data/analysis/serbia1/goals_analysis.json | yes | yes | 12.36 |
| teams_analysis | data/analysis/serbia1/teams_analysis.json | yes | yes | 39.01 |
| season_trends | data/analysis/serbia1/season_trends.json | yes | yes | 10.52 |
| scoreline_analysis | data/analysis/serbia1/scoreline_analysis.json | yes | yes | 270.76 |
| relationships | data/analysis/serbia1/relationships.json | yes | yes | 13.80 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1726 matches: home wins 45.2%, draws 23.3%, away wins 31.5% (781H / 402D / 543A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 42 home and 24 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 489 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1726 matches produced 4576 goals (avg 2.651 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.8% vs away 44.2% of 4576 goals in total (home/away ratio 1.26)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 835 of 1726 matches (48.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 509 scoring matches, 32.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.54, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Crvena zvezda leads with 557 points across 7 seasons (7 title(s), GD 460)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 7 teams present in every one of the 7 seasons (Crvena zvezda, Cukaricki, Mladost, Novi Pazar, Partizan...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Novi Pazar earns 80 more points at home than away (174 home vs 94 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Crvena zvezda won 7 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2021-2022: Crvena zvezda beat Partizan by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.111 per match): first half 2.573 vs last half 2.685 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021-2022 (goals view, avg abs position diff 4.875)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.286)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 188 matches (10.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (188 of 781 home matches, 24.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (178 of 402 draw matches, 44.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (128 of 543 away matches, 23.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 31 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.1177 (n=1637 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 12.661: home 5.061, draw -0.132, away -7.600
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1726 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1726 |
| Average goals per match | 2.651 |
| Home win rate | 45.2% |
| Draw rate | 23.3% |
| Away win rate | 31.5% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Crvena zvezda |
| Champion with most titles | Crvena zvezda |
| BTTS rate | 48.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.07 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 20.10 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.36 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.01 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.52 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 270.76 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.80 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 240 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 16 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 240 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 16 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 240 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 16 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 297 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 89 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 14 teams, expected 20
- **13.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **14.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 6.6% vs overall 8.3% (deviation 1.7 pp)
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 50.5% vs overall 45.2%
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 19.2% vs overall 23.3%
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 10.0% vs overall 8.3% (deviation 1.7 pp)
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 4.6% vs overall 8.3% (deviation 3.7 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 home outcome share 40.8% vs overall 45.2%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 away outcome share 35.8% vs overall 31.5%
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 12.1% vs overall 8.3% (deviation 3.8 pp)
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 draw outcome share 29.0% vs overall 23.3%
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 49.4% vs overall 45.2%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 25.8% vs overall 31.5%
- **25.** `HIGH_SCORING_MATCHES` *(warning)* — 12 match(es) with >= 8 total goals (extreme scorelines)
- **26.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (31 extra rows)
- **27.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=434, fgte=434 rows)
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=16 positions=1..16 teams=16
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=16 positions=1..16 teams=16
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=16 positions=1..16 teams=16
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=16 positions=1..16 teams=16
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=16 positions=1..16 teams=16
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=16 positions=1..16 teams=16
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=16 positions=1..16 teams=16
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=14 positions=1..14 teams=14
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=14 positions=1..14 teams=14
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=14 positions=1..14 teams=14

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
