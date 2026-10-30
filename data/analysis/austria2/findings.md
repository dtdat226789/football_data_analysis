# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:44:55+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 2. Liga (Austria)
- Scope: league `austria2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/austria2/database_profile.json | yes | yes | 49.88 |
| matches_analysis | data/analysis/austria2/matches_analysis.json | yes | yes | 21.18 |
| goals_analysis | data/analysis/austria2/goals_analysis.json | yes | yes | 12.40 |
| teams_analysis | data/analysis/austria2/teams_analysis.json | yes | yes | 36.41 |
| season_trends | data/analysis/austria2/season_trends.json | yes | yes | 10.42 |
| scoreline_analysis | data/analysis/austria2/scoreline_analysis.json | yes | yes | 243.70 |
| relationships | data/analysis/austria2/relationships.json | yes | yes | 13.77 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1503 matches: home wins 43.2%, draws 22.0%, away wins 34.7% (650H / 331D / 522A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 41 home and 31 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 389 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1503 matches produced 4438 goals (avg 2.953 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.4% vs away 46.6% of 4438 goals in total (home/away ratio 1.15)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 814 of 1503 matches (54.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 514 scoring matches, 36.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.06, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Liefering leads with 298 points across 7 seasons (0 title(s), GD 63)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 4 teams present in every one of the 7 seasons (Amstetten, Floridsdorfer AC, Kapfenberg, Liefering)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — BW Linz earns 39 more points at home than away (121 home vs 82 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — BW Linz won 3 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: BW Linz beat Liefering by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.087 per match): first half 3.006 vs last half 2.919 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022-2023 (goals view, avg abs position diff 7.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.375)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 147 matches (9.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (120 of 650 home matches, 18.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (147 of 331 draw matches, 44.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (108 of 522 away matches, 20.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 44 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = 0.0658 (n=1423 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.309: home 2.319, draw 0.038, away -2.990
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (44)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1503 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1503 |
| Average goals per match | 2.953 |
| Home win rate | 43.2% |
| Draw rate | 22.0% |
| Away win rate | 34.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Liefering |
| Champion with most titles | BW Linz |
| BTTS rate | 54.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.88 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 21.18 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.40 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 36.41 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.42 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 243.70 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.77 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 240 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 16 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 240 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 16 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 240 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 16 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 240 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 16 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 223 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 80 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 38.8% vs overall 34.7%
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 8.1% vs overall 6.1% (deviation 2.0 pp)
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.8% vs overall 6.1% (deviation 2.3 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 48.8% vs overall 43.2%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 17.5% vs overall 22.0%
- **21.** `HIGH_SCORING_MATCHES` *(warning)* — 11 match(es) with >= 8 total goals (extreme scorelines)
- **22.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **23.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=8, fgte=8 rows)
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=16 positions=1..16 teams=16
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=16 positions=1..16 teams=16
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=16 positions=1..16 teams=16
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=16 positions=1..16 teams=16
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=16 positions=1..16 teams=16
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=16 positions=1..16 teams=16
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=16 positions=1..16 teams=16
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=16 positions=1..16 teams=16
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=16 positions=1..16 teams=16
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=16 positions=1..16 teams=16
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
