# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:50:58+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Super League (Switzerland)
- Scope: league `swiss1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/swiss1/database_profile.json | yes | yes | 51.43 |
| matches_analysis | data/analysis/swiss1/matches_analysis.json | yes | yes | 19.98 |
| goals_analysis | data/analysis/swiss1/goals_analysis.json | yes | yes | 12.48 |
| teams_analysis | data/analysis/swiss1/teams_analysis.json | yes | yes | 24.96 |
| season_trends | data/analysis/swiss1/season_trends.json | yes | yes | 10.45 |
| scoreline_analysis | data/analysis/swiss1/scoreline_analysis.json | yes | yes | 189.86 |
| relationships | data/analysis/swiss1/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1229 matches: home wins 43.4%, draws 26.7%, away wins 29.9% (533H / 328D / 368A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 39 home and 28 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 312 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1229 matches produced 3760 goals (avg 3.059 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.2% vs away 44.8% of 3760 goals in total (home/away ratio 1.23)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 765 of 1229 matches (62.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 446 scoring matches, 38.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.50, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Young Boys leads with 416 points across 7 seasons (3 title(s), GD 197)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 7 teams present in every one of the 7 seasons (Basel, Lugano, Luzern, Servette, St. Gallen...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Young Boys earns 90 more points at home than away (253 home vs 163 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Young Boys won 3 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Lugano beat Young Boys by 3 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.260 per match): first half 3.031 vs last half 3.291 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.769)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 159 matches (12.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (118 of 533 home matches, 22.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (159 of 328 draw matches, 48.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (85 of 368 away matches, 23.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 36 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — points_difference |corr| = 0.0642 (n=1166 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.518: home 2.349, draw -0.830, away -3.169
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (49)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1229 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1229 |
| Average goals per match | 3.059 |
| Home win rate | 43.4% |
| Draw rate | 26.7% |
| Away win rate | 29.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Young Boys |
| Champion with most titles | Young Boys |
| BTTS rate | 62.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 51.43 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 19.98 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.48 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 24.96 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.45 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 189.86 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 180 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 180 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 10 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 180 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 10 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 198 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 12 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 198 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 12 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 230 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 13 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 63 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 6.7% vs overall 4.4% (deviation 2.3 pp)
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 2.2% vs overall 4.4% (deviation 2.2 pp)
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 draw outcome share 32.2% vs overall 26.7%
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 home outcome share 50.0% vs overall 43.4%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 away outcome share 25.3% vs overall 29.9%
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 away outcome share 34.8% vs overall 29.9%
- **22.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.746 vs overall 3.059 (deviation 0.687)
- **23.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 1.6% vs overall 4.4% (deviation 2.8 pp)
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 15.9% vs overall 26.7%
- **25.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 38.1% vs overall 29.9%
- **26.** `HIGH_SCORING_MATCHES` *(warning)* — 8 match(es) with >= 8 total goals (extreme scorelines)
- **27.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **28.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=442, fgte=442 rows)
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=10 positions=1..10 teams=10
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=10 positions=1..10 teams=10
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=10 positions=1..10 teams=10
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=10 positions=1..10 teams=10
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=10 positions=1..10 teams=10
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=10 positions=1..10 teams=10
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=10 positions=1..10 teams=10
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=10 positions=1..10 teams=10
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=10 positions=1..10 teams=10
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=12 positions=1..12 teams=12
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=12 positions=1..12 teams=12
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=12 positions=1..12 teams=12
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=12 positions=1..12 teams=12
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=12 positions=1..12 teams=12
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=12 positions=1..12 teams=12
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=13 positions=1..13 teams=13
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=13 positions=1..13 teams=13
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=13 positions=1..13 teams=13
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
