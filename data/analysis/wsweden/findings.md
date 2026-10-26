# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:53:42+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Allsvenskan Women (Sweden)
- Scope: league `wsweden`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/wsweden/database_profile.json | yes | yes | 50.31 |
| matches_analysis | data/analysis/wsweden/matches_analysis.json | yes | yes | 17.69 |
| goals_analysis | data/analysis/wsweden/goals_analysis.json | yes | yes | 12.69 |
| teams_analysis | data/analysis/wsweden/teams_analysis.json | yes | yes | 30.42 |
| season_trends | data/analysis/wsweden/season_trends.json | yes | yes | 10.28 |
| scoreline_analysis | data/analysis/wsweden/scoreline_analysis.json | yes | yes | 197.74 |
| relationships | data/analysis/wsweden/relationships.json | yes | yes | 13.73 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1151 matches: home wins 46.6%, draws 17.2%, away wins 36.2% (536H / 198D / 417A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 23 home and 31 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 365 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1151 matches produced 3497 goals (avg 3.038 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.6% vs away 45.4% of 3497 goals in total (home/away ratio 1.21)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 541 of 1151 matches (47.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 413 scoring matches, 37.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.36, median 22.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Hacken W leads with 357 points across 6 seasons (2 title(s), GD 307)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 7 seasons (Djurgarden W, Kristianstad W, Pitea W, Rosengard W, Vittsjo W)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Djurgarden W earns 43 more points at home than away (123 home vs 80 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Rosengard W won 3 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2023: Hammarby W beat Hacken W by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.232 per match): first half 2.887 vs last half 3.119 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023 (goals view, avg abs position diff 5.429)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2022 (luck view, avg abs position diff 2.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 114 matches (9.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (114 of 536 home matches, 21.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (89 of 198 draw matches, 44.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (88 of 417 away matches, 21.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 51 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.09 (n=992 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 14.109: home 6.423, draw -1.941, away -7.686
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1151 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1151 |
| Average goals per match | 3.038 |
| Home win rate | 46.6% |
| Draw rate | 17.2% |
| Away win rate | 36.2% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Hacken W |
| Champion with most titles | Rosengard W |
| BTTS rate | 47.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.31 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 17.69 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.69 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 30.42 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.28 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 197.74 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.73 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 132 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 132 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 12 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 182 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 14 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 182 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 14 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 182 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 14 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 182 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 14 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 159 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 14 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021 goalless share 8.3% vs overall 5.0% (deviation 3.3 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021 draw outcome share 22.7% vs overall 17.2%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021 away outcome share 28.0% vs overall 36.2%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024 goalless share 8.8% vs overall 5.0% (deviation 3.8 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025 goalless share 2.2% vs overall 5.0% (deviation 2.8 pp)
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 2.5% vs overall 5.0% (deviation 2.5 pp)
- **22.** `HIGH_SCORING_MATCHES` *(warning)* — 22 match(es) with >= 8 total goals (extreme scorelines)
- **23.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **24.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=511, fgte=511 rows)
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=12 positions=1..12 teams=12
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=12 positions=1..12 teams=12
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=12 positions=1..12 teams=12
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=12 positions=1..12 teams=12
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=12 positions=1..12 teams=12
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=12 positions=1..12 teams=12
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=14 positions=1..14 teams=14
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=14 positions=1..14 teams=14
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=14 positions=1..14 teams=14
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=14 positions=1..14 teams=14
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=14 positions=1..14 teams=14
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=14 positions=1..14 teams=14
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=14 positions=1..14 teams=14
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=14 positions=1..14 teams=14
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=14 positions=1..14 teams=14
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=14 positions=1..14 teams=14
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=14 positions=1..14 teams=14
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=14 positions=1..14 teams=14
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=14 positions=1..14 teams=14
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=14 positions=1..14 teams=14
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=14 positions=1..14 teams=14

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
