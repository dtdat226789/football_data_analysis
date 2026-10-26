# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:26:57+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier League (Azerbaijan)
- Scope: league `azer`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/azer/database_profile.json | yes | yes | 49.04 |
| matches_analysis | data/analysis/azer/matches_analysis.json | yes | yes | 15.58 |
| goals_analysis | data/analysis/azer/goals_analysis.json | yes | yes | 12.25 |
| teams_analysis | data/analysis/azer/teams_analysis.json | yes | yes | 24.64 |
| season_trends | data/analysis/azer/season_trends.json | yes | yes | 10.46 |
| scoreline_analysis | data/analysis/azer/scoreline_analysis.json | yes | yes | 158.56 |
| relationships | data/analysis/azer/relationships.json | yes | yes | 13.71 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1021 matches: home wins 40.5%, draws 25.7%, away wins 33.8% (414H / 262D / 345A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 25 home and 17 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 243 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1021 matches produced 2600 goals (avg 2.547 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.2% vs away 46.8% of 2600 goals in total (home/away ratio 1.14)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 465 of 1021 matches (45.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 259 scoring matches, 27.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.56, median 30.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Qarabag leads with 474 points across 7 seasons (4 title(s), GD 349)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 7 seasons (Neftci Baku, Qarabag, Sabah Baku, Sumqayit, Zira)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Sabail earns 36 more points at home than away (84 home vs 48 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Qarabag won 4 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Sabah FC beat Sabah Baku by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (-0.002 per match): first half 2.537 vs last half 2.536 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023-2024 (goals view, avg abs position diff 3.600)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2022-2023 (luck view, avg abs position diff 1.200)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 120 matches (11.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (106 of 414 home matches, 25.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (120 of 262 draw matches, 45.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (99 of 345 away matches, 28.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 15 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1556 (n=964 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 14.071: home 6.015, draw -0.498, away -8.055
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1021 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1021 |
| Average goals per match | 2.547 |
| Home win rate | 40.5% |
| Draw rate | 25.7% |
| Away win rate | 33.8% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Qarabag |
| Champion with most titles | Qarabag |
| BTTS rate | 45.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.04 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 15.58 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.25 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 24.64 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.46 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 158.56 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.71 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 112 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 8 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 112 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 8 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 180 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 10 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 180 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 10 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 180 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 10 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 200 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 13 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 57 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 13 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 12.5% vs overall 8.4% (deviation 4.1 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 33.9% vs overall 25.7%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 27.7% vs overall 33.8%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 6.1% vs overall 8.4% (deviation 2.3 pp)
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 away outcome share 38.0% vs overall 33.8%
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 45.6% vs overall 40.5%
- **22.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **23.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **24.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=9, fgte=9 rows)
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=8 positions=1..8 teams=8
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=8 positions=1..8 teams=8
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=8 positions=1..8 teams=8
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=8 positions=1..8 teams=8
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=8 positions=1..8 teams=8
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=8 positions=1..8 teams=8
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=10 positions=1..10 teams=10
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=10 positions=1..10 teams=10
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=10 positions=1..10 teams=10
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=10 positions=1..10 teams=10
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=10 positions=1..10 teams=10
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=10 positions=1..10 teams=10
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=10 positions=1..10 teams=10
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=10 positions=1..10 teams=10
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=10 positions=1..10 teams=10
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=13 positions=1..13 teams=13
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=13 positions=1..13 teams=13
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=13 positions=1..13 teams=13
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=13 positions=1..13 teams=13
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=13 positions=1..13 teams=13
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=13 positions=1..13 teams=13

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
