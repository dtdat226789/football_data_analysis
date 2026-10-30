# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T04:03:20+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: National League North (England)
- Scope: league `north`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/north/database_profile.json | yes | yes | 51.88 |
| matches_analysis | data/analysis/north/matches_analysis.json | yes | yes | 33.46 |
| goals_analysis | data/analysis/north/goals_analysis.json | yes | yes | 12.47 |
| teams_analysis | data/analysis/north/teams_analysis.json | yes | yes | 56.99 |
| season_trends | data/analysis/north/season_trends.json | yes | yes | 10.55 |
| scoreline_analysis | data/analysis/north/scoreline_analysis.json | yes | yes | 456.36 |
| relationships | data/analysis/north/relationships.json | yes | yes | 13.81 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 3004 matches: home wins 43.5%, draws 24.6%, away wins 31.8% (1308H / 740D / 956A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 78 home and 62 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 830 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 3004 matches produced 8109 goals (avg 2.699 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.4% vs away 44.6% of 8109 goals in total (home/away ratio 1.24)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1545 of 3004 matches (51.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 939 scoring matches, 33.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.54, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Chester leads with 414 points across 7 seasons (0 title(s), GD 94)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 6 teams present in every one of the 7 seasons (Chester, Chorley, Darlington, Hereford, Southport...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Chorley earns 95 more points at home than away (244 home vs 149 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — AFC Fylde won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Oxford City beat South Shields by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.139 per match): first half 2.645 vs last half 2.784 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023-2024 (goals view, avg abs position diff 9.250)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020-2021 (luck view, avg abs position diff 2.909)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 339 matches (11.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (283 of 1308 home matches, 21.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (339 of 740 draw matches, 45.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (250 of 956 away matches, 26.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 52 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_conceded_last_5 |corr| = 0.0577 (n=2843 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.258: home 3.121, draw -0.993, away -4.137
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (49)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 3004 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 3004 |
| Average goals per match | 2.699 |
| Home win rate | 43.5% |
| Draw rate | 24.6% |
| Away win rate | 31.8% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Chester |
| Champion with most titles | AFC Fylde |
| BTTS rate | 51.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 51.88 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 33.46 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.47 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 56.99 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.55 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 456.36 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.81 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 165 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 22 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 462 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 22 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 552 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 24 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 552 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 24 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 552 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 24 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 560 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 24 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 161 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 4.8% vs overall 7.0% (deviation 2.2 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 39.4% vs overall 43.5%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 30.3% vs overall 24.6%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 8.7% vs overall 7.0% (deviation 1.7 pp)
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 away outcome share 27.5% vs overall 31.8%
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 9.4% vs overall 7.0% (deviation 2.4 pp)
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 draw outcome share 29.2% vs overall 24.6%
- **23.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 4.1% vs overall 7.0% (deviation 2.9 pp)
- **24.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.7% vs overall 7.0% (deviation 3.3 pp)
- **25.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 49.1% vs overall 43.5%
- **26.** `HIGH_SCORING_MATCHES` *(warning)* — 14 match(es) with >= 8 total goals (extreme scorelines)
- **27.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **28.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=393, fgte=393 rows)
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=22 positions=1..22 teams=22
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=22 positions=1..22 teams=22
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=22 positions=1..22 teams=22
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=22 positions=1..22 teams=22
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=22 positions=1..22 teams=22
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=22 positions=1..22 teams=22
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=24 positions=1..24 teams=24
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=24 positions=1..24 teams=24
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=24 positions=1..24 teams=24
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=24 positions=1..24 teams=24
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=24 positions=1..24 teams=24
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=24 positions=1..24 teams=24
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=24 positions=1..24 teams=24
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=24 positions=1..24 teams=24
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=24 positions=1..24 teams=24
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=24 positions=1..24 teams=24
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=24 positions=1..24 teams=24
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=24 positions=1..24 teams=24
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=24 positions=1..24 teams=24
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=24 positions=1..24 teams=24
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=24 positions=1..24 teams=24

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
