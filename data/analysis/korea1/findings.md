# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T04:00:45+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: K League 1 (South Korea)
- Scope: league `korea1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/korea1/database_profile.json | yes | yes | 49.72 |
| matches_analysis | data/analysis/korea1/matches_analysis.json | yes | yes | 20.12 |
| goals_analysis | data/analysis/korea1/goals_analysis.json | yes | yes | 12.25 |
| teams_analysis | data/analysis/korea1/teams_analysis.json | yes | yes | 25.91 |
| season_trends | data/analysis/korea1/season_trends.json | yes | yes | 10.24 |
| scoreline_analysis | data/analysis/korea1/scoreline_analysis.json | yes | yes | 190.87 |
| relationships | data/analysis/korea1/relationships.json | yes | yes | 13.75 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1320 matches: home wins 39.2%, draws 28.5%, away wins 32.3% (518H / 376D / 426A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 42 home and 28 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 258 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1320 matches produced 3367 goals (avg 2.551 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.5% vs away 47.5% of 3367 goals in total (home/away ratio 1.11)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 709 of 1320 matches (53.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 304 scoring matches, 25.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 36.21, median 31.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Ulsan HD leads with 399 points across 7 seasons (4 title(s), GD 107)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 7 seasons (Gangwon, Jeonbuk, Pohang, Seoul, Ulsan HD)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Daegu earns 41 more points at home than away (135 home vs 94 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Ulsan HD won 4 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2021: Jeonbuk beat Ulsan HD by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.074 per match): first half 2.52 vs last half 2.594 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022 (goals view, avg abs position diff 4.833)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2023 (luck view, avg abs position diff 1.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 172 matches (13.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (140 of 518 home matches, 27.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (172 of 376 draw matches, 45.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (127 of 426 away matches, 29.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 22 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.0829 (n=1122 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 3.921: home 1.767, draw -0.828, away -2.154
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (47)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1320 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1320 |
| Average goals per match | 2.551 |
| Home win rate | 39.2% |
| Draw rate | 28.5% |
| Away win rate | 32.3% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Ulsan HD |
| Champion with most titles | Ulsan HD |
| BTTS rate | 53.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.72 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 20.12 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.25 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 25.91 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.24 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 190.87 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.75 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 132 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 198 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 12 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 198 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 12 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 198 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 12 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 198 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 12 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 198 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 12 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 198 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 12 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021 goalless share 11.6% vs overall 8.6% (deviation 3.0 pp)
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022 goalless share 6.6% vs overall 8.6% (deviation 2.0 pp)
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024 goalless share 6.1% vs overall 8.6% (deviation 2.5 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024 home outcome share 46.0% vs overall 39.2%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024 draw outcome share 23.2% vs overall 28.5%
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 11.1% vs overall 8.6% (deviation 2.5 pp)
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 home outcome share 31.8% vs overall 39.2%
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 draw outcome share 33.8% vs overall 28.5%
- **24.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **25.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **26.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=367, fgte=367 rows)
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=12 positions=1..12 teams=12
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=12 positions=1..12 teams=12
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=12 positions=1..12 teams=12
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=12 positions=1..12 teams=12
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=12 positions=1..12 teams=12
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=12 positions=1..12 teams=12
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=12 positions=1..12 teams=12
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=12 positions=1..12 teams=12
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=12 positions=1..12 teams=12
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=12 positions=1..12 teams=12
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=12 positions=1..12 teams=12
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=12 positions=1..12 teams=12
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=12 positions=1..12 teams=12
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=12 positions=1..12 teams=12
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=12 positions=1..12 teams=12
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=12 positions=1..12 teams=12
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=12 positions=1..12 teams=12
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=12 positions=1..12 teams=12
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=12 positions=1..12 teams=12
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=12 positions=1..12 teams=12
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
