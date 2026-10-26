# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:30:46+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier League (Egypt)
- Scope: league `egypt`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/egypt/database_profile.json | yes | yes | 49.12 |
| matches_analysis | data/analysis/egypt/matches_analysis.json | yes | yes | 18.26 |
| goals_analysis | data/analysis/egypt/goals_analysis.json | yes | yes | 12.27 |
| teams_analysis | data/analysis/egypt/teams_analysis.json | yes | yes | 77.24 |
| season_trends | data/analysis/egypt/season_trends.json | yes | yes | 10.47 |
| scoreline_analysis | data/analysis/egypt/scoreline_analysis.json | yes | yes | 238.81 |
| relationships | data/analysis/egypt/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1769 matches: home wins 35.8%, draws 33.7%, away wins 30.5% (634H / 596D / 539A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 36 home and 19 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — level at HT -> draw occurred 406 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1769 matches produced 3955 goals (avg 2.236 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.1% vs away 47.9% of 3955 goals in total (home/away ratio 1.09)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 836 of 1769 matches (47.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 413 scoring matches, 27.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 35.17, median 31.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Al Ahly leads with 417 points across 7 seasons (2 title(s), GD 226)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 10 teams present in every one of the 7 seasons (Al Ahly, Al Ittihad, Al Masry, Ceramica Cleopatra, El Gaish...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Ghazl El Mahallah earns 42 more points at home than away (101 home vs 59 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Zamalek won 3 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Zamalek beat Pyramids by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.141 per match): first half 2.282 vs last half 2.141 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2020-2021 (luck view, avg abs position diff 16.906)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2023-2024 (luck view, avg abs position diff 1.778)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 257 matches (14.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (213 of 634 home matches, 33.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (257 of 596 draw matches, 43.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (168 of 539 away matches, 31.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 16 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0966 (n=1699 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.549: home 3.590, draw -0.286, away -3.959
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1769 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1769 |
| Average goals per match | 2.236 |
| Home win rate | 35.8% |
| Draw rate | 33.7% |
| Away win rate | 30.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Al Ahly |
| Champion with most titles | Zamalek |
| BTTS rate | 47.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.12 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 18.26 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.27 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 77.24 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.47 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 238.81 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 53 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 306 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 18 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 306 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 18 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 153 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 18 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 322 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 21 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 70 matches, expected 380
- **14.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **15.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 10.5% vs overall 13.5% (deviation 3.0 pp)
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 31.0% vs overall 35.8%
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 17.0% vs overall 13.5% (deviation 3.5 pp)
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 10.8% vs overall 13.5% (deviation 2.7 pp)
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 15.7% vs overall 13.5% (deviation 2.2 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 15.8% vs overall 13.5% (deviation 2.3 pp)
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 draw outcome share 37.9% vs overall 33.7%
- **22.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 7.1% vs overall 13.5% (deviation 6.4 pp)
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 22.9% vs overall 33.7%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 38.6% vs overall 30.5%
- **25.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **26.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **27.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=312, fgte=312 rows)
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=53 positions=1..53 teams=53
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=53 positions=1..53 teams=53
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=53 positions=1..53 teams=53
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=18 positions=1..18 teams=18
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=18 positions=1..18 teams=18
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=18 positions=1..18 teams=18
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=18 positions=1..18 teams=18
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=18 positions=1..18 teams=18
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=18 positions=1..18 teams=18
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..18 teams=18
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..18 teams=18
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..18 teams=18
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=18 positions=1..18 teams=18
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=18 positions=1..18 teams=18
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=18 positions=1..18 teams=18
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=21 positions=1..21 teams=21
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=21 positions=1..21 teams=21
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=21 positions=1..21 teams=21

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
