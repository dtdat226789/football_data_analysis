# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:44:51+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Superliga (Romania)
- Scope: league `romania1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/romania1/database_profile.json | yes | yes | 50.86 |
| matches_analysis | data/analysis/romania1/matches_analysis.json | yes | yes | 19.22 |
| goals_analysis | data/analysis/romania1/goals_analysis.json | yes | yes | 12.42 |
| teams_analysis | data/analysis/romania1/teams_analysis.json | yes | yes | 39.17 |
| season_trends | data/analysis/romania1/season_trends.json | yes | yes | 10.47 |
| scoreline_analysis | data/analysis/romania1/scoreline_analysis.json | yes | yes | 238.94 |
| relationships | data/analysis/romania1/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1651 matches: home wins 42.3%, draws 29.3%, away wins 28.5% (698H / 483D / 470A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 36 home and 24 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 399 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1651 matches produced 3956 goals (avg 2.396 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.4% vs away 43.6% of 3956 goals in total (home/away ratio 1.29)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 798 of 1651 matches (48.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 450 scoring matches, 30.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.15, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — CFR Cluj leads with 395 points across 7 seasons (1 title(s), GD 142)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 7 seasons (CFR Cluj, FC Botosani, FCSB, UTA Arad, Univ. Craiova)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Univ. Craiova earns 67 more points at home than away (221 home vs 154 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — FCSB won 3 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: FCSB beat CFR Cluj by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.233 per match): first half 2.267 vs last half 2.5 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 7.684)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.375)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 234 matches (14.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (203 of 698 home matches, 29.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (234 of 483 draw matches, 48.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (167 of 470 away matches, 35.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 22 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_position_before_match |corr| = 0.1064 (n=1550 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.033: home 3.276, draw -1.453, away -3.756
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (49)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1651 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1651 |
| Average goals per match | 2.396 |
| Home win rate | 42.3% |
| Draw rate | 29.3% |
| Away win rate | 28.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | CFR Cluj |
| Champion with most titles | FCSB |
| BTTS rate | 48.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.86 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 19.22 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.42 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.17 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.47 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 238.94 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 240 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 16 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 240 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 16 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 240 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 16 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 240 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 16 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 350 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 101 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 34.6% vs overall 42.3%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 34.6% vs overall 28.5%
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 11.7% vs overall 9.6% (deviation 2.1 pp)
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 7.1% vs overall 9.6% (deviation 2.5 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 12.5% vs overall 9.6% (deviation 2.9 pp)
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 7.1% vs overall 9.6% (deviation 2.5 pp)
- **22.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 6.9% vs overall 9.6% (deviation 2.7 pp)
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 53.5% vs overall 42.3%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 23.8% vs overall 29.3%
- **25.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 22.8% vs overall 28.5%
- **26.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **27.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **28.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=414, fgte=414 rows)
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=16 positions=1..16 teams=16
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=16 positions=1..16 teams=16
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=16 positions=1..16 teams=16
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=16 positions=1..16 teams=16
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=16 positions=1..16 teams=16
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=16 positions=1..16 teams=16
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=16 positions=1..16 teams=16
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
