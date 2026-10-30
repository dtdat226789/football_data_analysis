# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:46:30+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: efbet League (Bulgaria)
- Scope: league `bulgaria1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/bulgaria1/database_profile.json | yes | yes | 49.24 |
| matches_analysis | data/analysis/bulgaria1/matches_analysis.json | yes | yes | 16.76 |
| goals_analysis | data/analysis/bulgaria1/goals_analysis.json | yes | yes | 12.34 |
| teams_analysis | data/analysis/bulgaria1/teams_analysis.json | yes | yes | 32.84 |
| season_trends | data/analysis/bulgaria1/season_trends.json | yes | yes | 10.50 |
| scoreline_analysis | data/analysis/bulgaria1/scoreline_analysis.json | yes | yes | 224.53 |
| relationships | data/analysis/bulgaria1/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1461 matches: home wins 45.3%, draws 24.6%, away wins 30.0% (662H / 360D / 439A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 19 home and 28 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 406 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1461 matches produced 3506 goals (avg 2.400 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.0% vs away 44.0% of 3506 goals in total (home/away ratio 1.27)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 628 of 1461 matches (43.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 380 scoring matches, 28.9% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.34, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Ludogorets leads with 449 points across 7 seasons (5 title(s), GD 293)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 10 teams present in every one of the 7 seasons (Arda, Botev Plovdiv, Botev Vratsa, CSKA 1948 Sofia, CSKA Sofia...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Arda earns 60 more points at home than away (170 home vs 110 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Ludogorets won 5 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2022-2023: Ludogorets beat CSKA Sofia by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.062 per match): first half 2.397 vs last half 2.458 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.235)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 204 matches (14.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (204 of 662 home matches, 30.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (157 of 360 draw matches, 43.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (120 of 439 away matches, 27.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 14 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_conceded_avg |corr| = -0.047 (n=1378 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 10.363: home 4.174, draw -0.900, away -6.188
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1461 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1461 |
| Average goals per match | 2.4 |
| Home win rate | 45.3% |
| Draw rate | 24.6% |
| Away win rate | 30.0% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Ludogorets |
| Champion with most titles | Ludogorets |
| BTTS rate | 43.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.24 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 16.76 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 32.84 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.50 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 224.53 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 182 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 14 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 182 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 14 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 240 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 16 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 240 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 16 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 240 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 16 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 294 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 17 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 83 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 14 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 12.1% vs overall 9.9% (deviation 2.2 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 home outcome share 50.5% vs overall 45.3%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 away outcome share 24.2% vs overall 30.0%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 7.1% vs overall 9.9% (deviation 2.8 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 12.2% vs overall 9.9% (deviation 2.3 pp)
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.8% vs overall 9.9% (deviation 5.1 pp)
- **22.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **23.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **24.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=295, fgte=295 rows)
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=14 positions=1..14 teams=14
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=14 positions=1..14 teams=14
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=14 positions=1..14 teams=14
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=14 positions=1..14 teams=14
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=14 positions=1..14 teams=14
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=14 positions=1..14 teams=14
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=16 positions=1..16 teams=16
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=17 positions=1..17 teams=17
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=17 positions=1..17 teams=17
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=17 positions=1..17 teams=17
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=14 positions=1..14 teams=14
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=14 positions=1..14 teams=14
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=14 positions=1..14 teams=14

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
