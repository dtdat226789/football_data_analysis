# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:48:01+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 3. CFL - Group A (Czech Republic)
- Scope: league `czech3a`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/czech3a/database_profile.json | yes | yes | 43.75 |
| matches_analysis | data/analysis/czech3a/matches_analysis.json | yes | yes | 17.54 |
| goals_analysis | data/analysis/czech3a/goals_analysis.json | yes | yes | 9.91 |
| teams_analysis | data/analysis/czech3a/teams_analysis.json | yes | yes | 38.16 |
| season_trends | data/analysis/czech3a/season_trends.json | yes | yes | 7.81 |
| scoreline_analysis | data/analysis/czech3a/scoreline_analysis.json | yes | yes | 182.95 |
| relationships | data/analysis/czech3a/relationships.json | yes | yes | 13.74 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1089 matches: home wins 46.3%, draws 22.0%, away wins 31.7% (504H / 240D / 345A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 35 home and 21 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 319 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1089 matches produced 3505 goals (avg 3.219 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.4% vs away 44.6% of 3505 goals in total (home/away ratio 1.24)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 635 of 1089 matches (58.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 430 scoring matches, 41.9% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 26.54, median 20.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Domazlice leads with 282 points across 5 seasons (2 title(s), GD 140)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 8 teams present in every one of the 5 seasons (Admira Prague, Bohemians 1905 B, Domazlice, Dukla Prague B, Loko Praha...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Plzen B earns 46 more points at home than away (143 home vs 97 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Domazlice won 2 of 5 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Kraluv Dvur beat Ceske Budejovice by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.167 per match): first half 3.204 vs last half 3.37 across 5 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022-2023 (goals view, avg abs position diff 6.375)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.375)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 96 matches (8.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (88 of 504 home matches, 17.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (96 of 240 draw matches, 40.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (69 of 345 away matches, 20.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 59 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.071 (n=992 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.913: home 1.705, draw -0.199, away -3.208
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (34)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 5 of 5 registered seasons populated (100.0%); 1089 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1089 |
| Average goals per match | 3.219 |
| Home win rate | 46.3% |
| Draw rate | 22.0% |
| Away win rate | 31.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Domazlice |
| Champion with most titles | Domazlice |
| BTTS rate | 58.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 43.75 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 17.54 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 9.91 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 38.16 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 7.81 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 182.95 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.74 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 240 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 16 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 240 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 17 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 272 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 17 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 97 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **11.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **12.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 home outcome share 50.4% vs overall 46.3%
- **13.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 away outcome share 36.7% vs overall 31.7%
- **14.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 8.2% vs overall 5.6% (deviation 2.6 pp)
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 41.2% vs overall 46.3%
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 29.9% vs overall 22.0%
- **17.** `HIGH_SCORING_MATCHES` *(warning)* — 23 match(es) with >= 8 total goals (extreme scorelines)
- **18.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (3 extra rows)
- **19.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=307, fgte=307 rows)
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=16 positions=1..16 teams=16
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=16 positions=1..16 teams=16
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=16 positions=1..16 teams=16
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=16 positions=1..16 teams=16
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=16 positions=1..16 teams=16
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=16 positions=1..16 teams=16
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=17 positions=1..17 teams=17
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=17 positions=1..17 teams=17
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=17 positions=1..17 teams=17
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=17 positions=1..17 teams=17
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=17 positions=1..17 teams=17
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=17 positions=1..17 teams=17
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
