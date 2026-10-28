# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T02:31:39+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: National League South (England)
- Scope: league `south`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/south/database_profile.json | yes | yes | 51.02 |
| matches_analysis | data/analysis/south/matches_analysis.json | yes | yes | 39.60 |
| goals_analysis | data/analysis/south/goals_analysis.json | yes | yes | 12.46 |
| teams_analysis | data/analysis/south/teams_analysis.json | yes | yes | 105.85 |
| season_trends | data/analysis/south/season_trends.json | yes | yes | 10.52 |
| scoreline_analysis | data/analysis/south/scoreline_analysis.json | yes | yes | 467.18 |
| relationships | data/analysis/south/relationships.json | yes | yes | 13.81 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 3000 matches: home wins 43.3%, draws 23.8%, away wins 32.9% (1299H / 714D / 987A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 93 home and 81 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 772 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 3000 matches produced 8520 goals (avg 2.840 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.3% vs away 45.7% of 8520 goals in total (home/away ratio 1.19)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1675 of 3000 matches (55.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 937 scoring matches, 33.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.74, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Maidstone leads with 373 points across 6 seasons (2 title(s), GD 132)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 7 seasons (Chelmsford, Hampton & Richmond, Hemel Hempstead, Slough, Tonbridge)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Slough earns 56 more points at home than away (174 home vs 118 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Maidstone won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2024-2025: Truro beat Torquay by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.081 per match): first half 2.91 vs last half 2.828 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 21.083)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.583)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 346 matches (11.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (295 of 1299 home matches, 22.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (346 of 714 draw matches, 48.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (253 of 987 away matches, 25.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 88 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0699 (n=2841 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.219: home 2.863, draw -0.735, away -3.356
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 3000 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 3000 |
| Average goals per match | 2.84 |
| Home win rate | 43.3% |
| Draw rate | 23.8% |
| Away win rate | 32.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Maidstone |
| Champion with most titles | Maidstone |
| BTTS rate | 55.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 51.02 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 39.60 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.46 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 105.85 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.52 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 467.18 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.81 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 165 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 21 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 420 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 21 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 552 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 24 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 550 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 24 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 549 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 24 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 605 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 72 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 159 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 37.6% vs overall 43.3%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 40.6% vs overall 32.9%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 home outcome share 47.8% vs overall 43.3%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.4% vs overall 6.1% (deviation 1.7 pp)
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 36.5% vs overall 43.3%
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 37.1% vs overall 32.9%
- **22.** `HIGH_SCORING_MATCHES` *(warning)* — 25 match(es) with >= 8 total goals (extreme scorelines)
- **23.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **24.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=439, fgte=439 rows)
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=21 positions=1..21 teams=21
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=21 positions=1..21 teams=21
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=21 positions=1..21 teams=21
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=21 positions=1..21 teams=21
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=21 positions=1..21 teams=21
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=21 positions=1..21 teams=21
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=24 positions=1..24 teams=24
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=24 positions=1..24 teams=24
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=24 positions=1..24 teams=24
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=24 positions=1..24 teams=24
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=24 positions=1..24 teams=24
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=24 positions=1..24 teams=24
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=24 positions=1..24 teams=24
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=24 positions=1..24 teams=24
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=24 positions=1..24 teams=24
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=72 positions=1..72 teams=72
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=72 positions=1..72 teams=72
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=72 positions=1..72 teams=72
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=24 positions=1..24 teams=24
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=24 positions=1..24 teams=24
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=24 positions=1..24 teams=24

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
