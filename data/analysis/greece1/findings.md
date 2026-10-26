# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:34:35+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Super League (Greece)
- Scope: league `greece1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/greece1/database_profile.json | yes | yes | 49.40 |
| matches_analysis | data/analysis/greece1/matches_analysis.json | yes | yes | 17.67 |
| goals_analysis | data/analysis/greece1/goals_analysis.json | yes | yes | 12.25 |
| teams_analysis | data/analysis/greece1/teams_analysis.json | yes | yes | 31.62 |
| season_trends | data/analysis/greece1/season_trends.json | yes | yes | 10.49 |
| scoreline_analysis | data/analysis/greece1/scoreline_analysis.json | yes | yes | 183.94 |
| relationships | data/analysis/greece1/relationships.json | yes | yes | 13.75 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1207 matches: home wins 42.7%, draws 25.8%, away wins 31.5% (515H / 312D / 380A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 30 home and 23 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 326 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1207 matches produced 3008 goals (avg 2.492 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.2% vs away 44.8% of 3008 goals in total (home/away ratio 1.23)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 550 of 1207 matches (45.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 328 scoring matches, 29.9% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.74, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Olympiacos Piraeus leads with 390 points across 7 seasons (3 title(s), GD 227)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 7 seasons (Aris, Asteras Tripolis, Atromitos, OFI Crete, Olympiacos Piraeus...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Asteras Tripolis earns 54 more points at home than away (132 home vs 78 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Olympiacos Piraeus won 3 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2023-2024: PAOK beat AEK Athens FC by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.238 per match): first half 2.315 vs last half 2.553 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 5.429)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2023-2024 (luck view, avg abs position diff 1.429)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 138 matches (11.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (121 of 515 home matches, 23.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (138 of 312 draw matches, 44.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (99 of 380 away matches, 26.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 10 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1208 (n=1156 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 11.0: home 4.621, draw -1.628, away -6.379
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (46)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1207 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1207 |
| Average goals per match | 2.492 |
| Home win rate | 42.7% |
| Draw rate | 25.8% |
| Away win rate | 31.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Olympiacos Piraeus |
| Champion with most titles | Olympiacos Piraeus |
| BTTS rate | 45.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.40 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 17.67 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.25 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 31.62 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.49 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 183.94 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.75 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 182 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 14 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 182 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 14 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 182 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 14 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 182 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 14 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 182 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 14 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 246 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 15 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 51 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 14 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 11.5% vs overall 8.9% (deviation 2.6 pp)
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 12.1% vs overall 8.9% (deviation 3.2 pp)
- **18.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2023-2024 avg goals 2.995 vs overall 2.492 (deviation 0.503)
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 4.4% vs overall 8.9% (deviation 4.5 pp)
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 away outcome share 36.8% vs overall 31.5%
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 47.1% vs overall 42.7%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 21.6% vs overall 25.8%
- **23.** `HIGH_SCORING_MATCHES` *(warning)* — 3 match(es) with >= 8 total goals (extreme scorelines)
- **24.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **25.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=330, fgte=330 rows)
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=14 positions=1..14 teams=14
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=14 positions=1..14 teams=14
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=14 positions=1..14 teams=14
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=14 positions=1..14 teams=14
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=14 positions=1..14 teams=14
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=14 positions=1..14 teams=14
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=14 positions=1..14 teams=14
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=14 positions=1..14 teams=14
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=14 positions=1..14 teams=14
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=14 positions=1..14 teams=14
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=14 positions=1..14 teams=14
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=14 positions=1..14 teams=14
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=14 positions=1..14 teams=14
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=14 positions=1..14 teams=14
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=14 positions=1..14 teams=14
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=15 positions=1..15 teams=15
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=15 positions=1..15 teams=15
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=15 positions=1..15 teams=15
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=14 positions=1..14 teams=14
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=14 positions=1..14 teams=14
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=14 positions=1..14 teams=14

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
