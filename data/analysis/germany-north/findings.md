# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:48:56+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Regionalliga North (Germany)
- Scope: league `germany-north`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/germany-north/database_profile.json | yes | yes | 52.07 |
| matches_analysis | data/analysis/germany-north/matches_analysis.json | yes | yes | 24.48 |
| goals_analysis | data/analysis/germany-north/goals_analysis.json | yes | yes | 12.52 |
| teams_analysis | data/analysis/germany-north/teams_analysis.json | yes | yes | 44.46 |
| season_trends | data/analysis/germany-north/season_trends.json | yes | yes | 10.57 |
| scoreline_analysis | data/analysis/germany-north/scoreline_analysis.json | yes | yes | 280.90 |
| relationships | data/analysis/germany-north/relationships.json | yes | yes | 13.80 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1699 matches: home wins 42.7%, draws 22.5%, away wins 34.7% (726H / 383D / 590A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 52 home and 37 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 467 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1699 matches produced 5641 goals (avg 3.320 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.4% vs away 46.6% of 5641 goals in total (home/away ratio 1.15)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1016 of 1699 matches (59.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 626 scoring matches, 38.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 27.43, median 21.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Drochtersen/Assel leads with 320 points across 7 seasons (0 title(s), GD 109)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 7 teams present in every one of the 7 seasons (Drochtersen/Assel, Hamburger SV II, Jeddeloh, Norderstedt, Phonix Lubeck...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Drochtersen/Assel earns 54 more points at home than away (187 home vs 133 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — TSV Havelse won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: TSV Havelse beat Werder Bremen II by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.550 per match): first half 3.03 vs last half 3.581 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023-2024 (goals view, avg abs position diff 21.444)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 3.053)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 175 matches (10.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (118 of 726 home matches, 16.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (175 of 383 draw matches, 45.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (97 of 590 away matches, 16.4%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 95 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — position_difference |corr| = -0.0642 (n=1569 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.247: home 3.276, draw -1.615, away -3.971
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (47)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1699 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1699 |
| Average goals per match | 3.32 |
| Home win rate | 42.7% |
| Draw rate | 22.5% |
| Away win rate | 34.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Drochtersen/Assel |
| Champion with most titles | TSV Havelse |
| BTTS rate | 59.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 52.07 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 24.48 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.52 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 44.46 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.57 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 280.90 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.80 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 98 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 22 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 200 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 21 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 342 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 19 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 306 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 18 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 317 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 130 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 19 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2020-2021 avg goals 2.847 vs overall 3.32 (deviation 0.473)
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 2.0% vs overall 4.6% (deviation 2.6 pp)
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 13.3% vs overall 22.5%
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 41.8% vs overall 34.7%
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 6.5% vs overall 4.6% (deviation 1.9 pp)
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 2.5% vs overall 4.6% (deviation 2.1 pp)
- **22.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.892 vs overall 3.32 (deviation 0.572)
- **23.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 2.3% vs overall 4.6% (deviation 2.3 pp)
- **24.** `HIGH_SCORING_MATCHES` *(warning)* — 49 match(es) with >= 8 total goals (extreme scorelines)
- **25.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **26.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=326, fgte=326 rows)
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=22 positions=1..24 teams=22
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=22 positions=3..26 teams=22
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=22 positions=1..27 teams=22
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=21 positions=1..22 teams=21
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=21 positions=5..29 teams=21
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=21 positions=1..32 teams=21
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=19 positions=1..20 teams=19
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=19 positions=7..31 teams=19
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=19 positions=1..38 teams=19
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..39 teams=18
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=19..43 teams=18
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..51 teams=18
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=18 positions=1..19 teams=18
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=18 positions=7..29 teams=18
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=18 positions=1..36 teams=18
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=19 positions=1..19 teams=19
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=19 positions=1..19 teams=19
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=19 positions=1..19 teams=19

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
