# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:18:32+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Thai League 1 (Thailand)
- Scope: league `thai1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/thai1/database_profile.json | yes | yes | 47.04 |
| matches_analysis | data/analysis/thai1/matches_analysis.json | yes | yes | 21.14 |
| goals_analysis | data/analysis/thai1/goals_analysis.json | yes | yes | 11.22 |
| teams_analysis | data/analysis/thai1/teams_analysis.json | yes | yes | 37.70 |
| season_trends | data/analysis/thai1/season_trends.json | yes | yes | 9.12 |
| scoreline_analysis | data/analysis/thai1/scoreline_analysis.json | yes | yes | 191.63 |
| relationships | data/analysis/thai1/relationships.json | yes | yes | 13.77 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1248 matches: home wins 46.5%, draws 27.0%, away wins 26.5% (580H / 337D / 331A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 37 home and 36 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 353 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1248 matches produced 3514 goals (avg 2.816 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 58.1% vs away 41.9% of 3514 goals in total (home/away ratio 1.38)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 710 of 1248 matches (56.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 379 scoring matches, 32.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.33, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Buriram leads with 358 points across 6 seasons (5 title(s), GD 241)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 7 teams present in every one of the 6 seasons (Bangkok Utd, Buriram, Chiangrai Utd, Pathum United, Port MTI FC...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Muang Thong Utd earns 74 more points at home than away (148 home vs 74 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Buriram won 5 of 6 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2024-2025: Buriram beat Bangkok Utd by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.119 per match): first half 2.775 vs last half 2.894 across 6 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 5.500)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 2.125)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 168 matches (13.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (129 of 580 home matches, 22.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (168 of 337 draw matches, 49.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (88 of 331 away matches, 26.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 38 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.1186 (n=1200 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.908: home 2.934, draw -1.471, away -4.974
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (39)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 6 of 6 registered seasons populated (100.0%); 1248 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1248 |
| Average goals per match | 2.816 |
| Home win rate | 46.5% |
| Draw rate | 27.0% |
| Away win rate | 26.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Buriram |
| Champion with most titles | Buriram |
| BTTS rate | 56.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 47.04 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 21.14 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 11.22 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 37.70 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 9.12 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 191.63 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.77 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 240 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 16 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 240 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 16 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 240 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 16 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 240 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 48 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **13.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **14.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 draw outcome share 31.2% vs overall 27.0%
- **15.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.2% vs overall 6.9% (deviation 2.7 pp)
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 41.7% vs overall 46.5%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 16.7% vs overall 27.0%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 41.7% vs overall 26.5%
- **19.** `HIGH_SCORING_MATCHES` *(warning)* — 14 match(es) with >= 8 total goals (extreme scorelines)
- **20.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **21.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=443, fgte=443 rows)
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=16 positions=1..16 teams=16
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=16 positions=1..16 teams=16
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=16 positions=1..16 teams=16
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=16 positions=1..16 teams=16
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=16 positions=1..16 teams=16
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=16 positions=1..16 teams=16
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=16 positions=1..16 teams=16
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=16 positions=1..16 teams=16
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=16 positions=1..16 teams=16
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
