# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T04:12:28+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/segunda4/database_profile.json | yes | yes | 49.25 |
| matches_analysis | data/analysis/segunda4/matches_analysis.json | yes | yes | 21.41 |
| goals_analysis | data/analysis/segunda4/goals_analysis.json | yes | yes | 12.36 |
| teams_analysis | data/analysis/segunda4/teams_analysis.json | yes | yes | 70.13 |
| season_trends | data/analysis/segunda4/season_trends.json | yes | yes | 10.52 |
| scoreline_analysis | data/analysis/segunda4/scoreline_analysis.json | yes | yes | 260.71 |
| relationships | data/analysis/segunda4/relationships.json | yes | yes | 13.79 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1799 matches: home wins 45.2%, draws 28.3%, away wins 26.5% (813H / 510D / 476A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 44 home and 29 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 450 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1799 matches produced 3995 goals (avg 2.221 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.9% vs away 42.1% of 3995 goals in total (home/away ratio 1.37)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 802 of 1799 matches (44.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 433 scoring matches, 27.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 35.12, median 30.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — UCAM Murcia leads with 249 points across 5 seasons (1 title(s), GD 64)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 0 teams present in every one of the 7 seasons
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — UCAM Murcia earns 67 more points at home than away (158 home vs 91 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — UCAM Murcia won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: UCAM Murcia beat Linares by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.059 per match): first half 2.267 vs last half 2.327 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2020-2021 (goals view, avg abs position diff 8.900)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2021-2022 (luck view, avg abs position diff 1.778)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 267 matches (14.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (267 of 813 home matches, 32.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (239 of 510 draw matches, 46.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (172 of 476 away matches, 36.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 13 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_position_before_match |corr| = 0.1104 (n=1727 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.475: home 2.142, draw -1.176, away -3.333
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (44)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1799 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1799 |
| Average goals per match | 2.221 |
| Home win rate | 45.2% |
| Draw rate | 28.3% |
| Away win rate | 26.5% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | UCAM Murcia |
| Champion with most titles | UCAM Murcia |
| BTTS rate | 44.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.25 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 21.41 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.36 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 70.13 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.52 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 260.71 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.79 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 180 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 306 matches, expected 380
- **3.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 18 teams, expected 20
- **4.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 306 matches, expected 380
- **5.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 18 teams, expected 20
- **6.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **7.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **8.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 306 matches, expected 380
- **9.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 18 teams, expected 20
- **10.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 323 matches, expected 380
- **11.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **12.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 72 matches, expected 380
- **13.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **14.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **15.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 13.3% vs overall 11.2% (deviation 2.1 pp)
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 36.1% vs overall 45.2%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 32.8% vs overall 28.3%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 31.1% vs overall 26.5%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 15.0% vs overall 11.2% (deviation 3.8 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 8.7% vs overall 11.2% (deviation 2.5 pp)
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 home outcome share 50.2% vs overall 45.2%
- **22.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 2.639 vs overall 2.221 (deviation 0.418)
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 22.2% vs overall 26.5%
- **24.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **25.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (24 extra rows)
- **26.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=429, fgte=429 rows)
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=18 positions=1..18 teams=18
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=18 positions=1..18 teams=18
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=18 positions=1..18 teams=18
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=18 positions=1..18 teams=18
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=18 positions=1..18 teams=18
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=18 positions=1..18 teams=18
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..18 teams=18
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..18 teams=18
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..18 teams=18
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=18 positions=1..18 teams=18
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=18 positions=1..18 teams=18
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=18 positions=1..18 teams=18
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
