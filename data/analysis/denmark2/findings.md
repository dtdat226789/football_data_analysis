# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:45:11+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 1st Division (Denmark)
- Scope: league `denmark2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/denmark2/database_profile.json | yes | yes | 51.68 |
| matches_analysis | data/analysis/denmark2/matches_analysis.json | yes | yes | 14.53 |
| goals_analysis | data/analysis/denmark2/goals_analysis.json | yes | yes | 12.31 |
| teams_analysis | data/analysis/denmark2/teams_analysis.json | yes | yes | 34.94 |
| season_trends | data/analysis/denmark2/season_trends.json | yes | yes | 10.43 |
| scoreline_analysis | data/analysis/denmark2/scoreline_analysis.json | yes | yes | 136.29 |
| relationships | data/analysis/denmark2/relationships.json | yes | yes | 13.72 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 848 matches: home wins 41.2%, draws 24.2%, away wins 34.7% (349H / 205D / 294A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 21 home and 15 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 223 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 848 matches produced 2427 goals (avg 2.862 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.7% vs away 47.3% of 2427 goals in total (home/away ratio 1.11)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 460 of 848 matches (54.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 307 scoring matches, 38.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.40, median 21.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Hvidovre IF leads with 213 points across 6 seasons (1 title(s), GD 39)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 2 teams present in every one of the 7 seasons (Hobro, Koge)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Vendsyssel earns 33 more points at home than away (82 home vs 49 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Viborg won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2023-2024: Aalborg beat Sonderjyske by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.176 per match): first half 2.914 vs last half 2.738 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2020-2021 (goals view, avg abs position diff 4.833)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020-2021 (luck view, avg abs position diff 1.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 93 matches (11.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (70 of 349 home matches, 20.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (93 of 205 draw matches, 45.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (66 of 294 away matches, 22.4%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 16 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_points_before_match |corr| = -0.0819 (n=776 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.121: home 2.614, draw -0.112, away -3.507
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (52)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 848 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 848 |
| Average goals per match | 2.862 |
| Home win rate | 41.2% |
| Draw rate | 24.2% |
| Away win rate | 34.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Hvidovre IF |
| Champion with most titles | Viborg |
| BTTS rate | 54.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 51.68 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 14.53 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.31 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 34.94 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.43 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 136.29 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.72 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 132 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 132 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 12 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 132 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 12 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 110 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 11 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 110 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 11 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 160 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 11 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 72 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 4.5% vs overall 6.1% (deviation 1.6 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 19.7% vs overall 24.2%
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 3.8% vs overall 6.1% (deviation 2.3 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 home outcome share 46.2% vs overall 41.2%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 draw outcome share 18.9% vs overall 24.2%
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 home outcome share 36.4% vs overall 41.2%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 draw outcome share 20.0% vs overall 24.2%
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 away outcome share 40.0% vs overall 34.7%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 away outcome share 30.6% vs overall 34.7%
- **25.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 11.1% vs overall 6.1% (deviation 5.0 pp)
- **26.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 34.7% vs overall 41.2%
- **27.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 37.5% vs overall 24.2%
- **28.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 27.8% vs overall 34.7%
- **29.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **30.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **31.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=310, fgte=310 rows)
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=12 positions=1..12 teams=12
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=12 positions=1..12 teams=12
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=12 positions=1..12 teams=12
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=12 positions=1..12 teams=12
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=12 positions=1..12 teams=12
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=12 positions=1..12 teams=12
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=12 positions=1..12 teams=12
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=12 positions=1..12 teams=12
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=12 positions=1..12 teams=12
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=11 positions=1..11 teams=11
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=11 positions=1..11 teams=11
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=11 positions=1..11 teams=11
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=11 positions=1..11 teams=11
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=11 positions=1..11 teams=11
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=11 positions=1..11 teams=11
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=11 positions=1..11 teams=11
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=11 positions=1..11 teams=11
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=11 positions=1..11 teams=11
- **50.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **51.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **52.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
