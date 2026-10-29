# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T01:53:14+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: A-League (Australia)
- Scope: league `australia`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/australia/database_profile.json | yes | yes | 47.11 |
| matches_analysis | data/analysis/australia/matches_analysis.json | yes | yes | 16.39 |
| goals_analysis | data/analysis/australia/goals_analysis.json | yes | yes | 11.06 |
| teams_analysis | data/analysis/australia/teams_analysis.json | yes | yes | 22.41 |
| season_trends | data/analysis/australia/season_trends.json | yes | yes | 9.18 |
| scoreline_analysis | data/analysis/australia/scoreline_analysis.json | yes | yes | 155.24 |
| relationships | data/analysis/australia/relationships.json | yes | yes | 13.69 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 962 matches: home wins 41.8%, draws 25.1%, away wins 33.2% (402H / 241D / 319A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 28 home and 18 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 243 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 962 matches produced 2949 goals (avg 3.065 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.2% vs away 45.8% of 2949 goals in total (home/away ratio 1.18)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 582 of 962 matches (60.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 319 scoring matches, 34.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.40, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Melbourne City leads with 278 points across 6 seasons (3 title(s), GD 103)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 11 teams present in every one of the 6 seasons (Adelaide United, Brisbane Roar, Central Coast Mariners, Macarthur FC, Melbourne City...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Perth Glory earns 45 more points at home than away (98 home vs 53 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Melbourne City won 3 of 6 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2021-2022: Melbourne City beat Melbourne Victory by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.180 per match): first half 2.972 vs last half 3.152 across 6 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023-2024 (goals view, avg abs position diff 4.833)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2021-2022 (luck view, avg abs position diff 1.667)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 104 matches (10.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (85 of 402 home matches, 21.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (104 of 241 draw matches, 43.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (83 of 319 away matches, 26.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 40 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1222 (n=962 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 3.01: home 1.214, draw -0.635, away -1.796
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (40)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_REGISTERED_NO_DATA, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 6 of 7 registered seasons populated (85.7%); 962 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 962 |
| Average goals per match | 3.065 |
| Home win rate | 41.8% |
| Draw rate | 25.1% |
| Away win rate | 33.2% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Melbourne City |
| Champion with most titles | Melbourne City |
| BTTS rate | 60.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 47.11 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 16.39 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 11.06 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 22.41 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 9.18 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 155.24 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.69 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 156 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 156 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 12 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 156 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 12 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 162 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 12 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 169 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 13 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 163 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 12 teams, expected 20
- **13.** `SEASON_REGISTERED_NO_DATA` *(warning)* — Season 2026-2027 is registered but has no match data (declared_by_api=True, state=unknown)
- **14.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 0 matches, expected 380
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 home outcome share 46.8% vs overall 41.8%
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 away outcome share 28.8% vs overall 33.2%
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 2.6% vs overall 4.5% (deviation 1.9 pp)
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 home outcome share 34.9% vs overall 41.8%
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 away outcome share 39.1% vs overall 33.2%
- **20.** `HIGH_SCORING_MATCHES` *(warning)* — 16 match(es) with >= 8 total goals (extreme scorelines)
- **21.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **22.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=12 positions=1..12 teams=12
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=12 positions=1..12 teams=12
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=12 positions=1..12 teams=12
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=12 positions=1..12 teams=12
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=12 positions=1..12 teams=12
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=12 positions=1..12 teams=12
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=12 positions=1..12 teams=12
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=12 positions=1..12 teams=12
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=12 positions=1..12 teams=12
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=12 positions=1..12 teams=12
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=12 positions=1..12 teams=12
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=12 positions=1..12 teams=12
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=13 positions=1..13 teams=13
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=13 positions=1..13 teams=13
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=13 positions=1..13 teams=13
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=12 positions=1..12 teams=12
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=12 positions=1..12 teams=12
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
