# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T01:53:30+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Bundesliga (Austria)
- Scope: league `austria1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/austria1/database_profile.json | yes | yes | 50.49 |
| matches_analysis | data/analysis/austria1/matches_analysis.json | yes | yes | 15.95 |
| goals_analysis | data/analysis/austria1/goals_analysis.json | yes | yes | 12.37 |
| teams_analysis | data/analysis/austria1/teams_analysis.json | yes | yes | 24.97 |
| season_trends | data/analysis/austria1/season_trends.json | yes | yes | 10.41 |
| scoreline_analysis | data/analysis/austria1/scoreline_analysis.json | yes | yes | 144.56 |
| relationships | data/analysis/austria1/relationships.json | yes | yes | 13.71 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 915 matches: home wins 41.4%, draws 25.5%, away wins 33.1% (379H / 233D / 303A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 23 home and 21 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 239 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 915 matches produced 2604 goals (avg 2.846 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.7% vs away 46.3% of 2604 goals in total (home/away ratio 1.16)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 503 of 915 matches (55.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 311 scoring matches, 36.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.68, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Salzburg leads with 322 points across 7 seasons (4 title(s), GD 194)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 7 seasons (Altach, Austria Vienna, Hartberg, LASK, SK Rapid...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Ried earns 48 more points at home than away (87 home vs 39 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Salzburg won 4 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2024-2025: Sturm Graz beat Austria Vienna by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.083 per match): first half 2.982 vs last half 2.899 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023-2024 (goals view, avg abs position diff 5.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.167)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 114 matches (12.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (83 of 379 home matches, 21.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (114 of 233 draw matches, 48.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (61 of 303 away matches, 20.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 20 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_points_before_match |corr| = -0.0612 (n=855 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.498: home 2.879, draw -1.665, away -2.619
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (49)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 915 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 915 |
| Average goals per match | 2.846 |
| Home win rate | 41.4% |
| Draw rate | 25.5% |
| Away win rate | 33.1% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Salzburg |
| Champion with most titles | Salzburg |
| BTTS rate | 55.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.49 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 15.95 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.37 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 24.97 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.41 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 144.56 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.71 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 132 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 132 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 12 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 132 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 12 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 132 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 12 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 132 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 12 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 195 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 12 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 60 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 37.9% vs overall 33.1%
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 3.8% vs overall 6.1% (deviation 2.3 pp)
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 draw outcome share 31.1% vs overall 25.5%
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 draw outcome share 21.2% vs overall 25.5%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 away outcome share 40.2% vs overall 33.1%
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 9.1% vs overall 6.1% (deviation 3.0 pp)
- **22.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.3% vs overall 6.1% (deviation 2.8 pp)
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 51.7% vs overall 41.4%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 20.0% vs overall 25.5%
- **25.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 28.3% vs overall 33.1%
- **26.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **27.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **28.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=12 positions=1..12 teams=12
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=12 positions=1..12 teams=12
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=12 positions=1..12 teams=12
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=12 positions=1..12 teams=12
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=12 positions=1..12 teams=12
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=12 positions=1..12 teams=12
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=12 positions=1..12 teams=12
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=12 positions=1..12 teams=12
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=12 positions=1..12 teams=12
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=12 positions=1..12 teams=12
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=12 positions=1..12 teams=12
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=12 positions=1..12 teams=12
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=12 positions=1..12 teams=12
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=12 positions=1..12 teams=12
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=12 positions=1..12 teams=12
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=12 positions=1..12 teams=12
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=12 positions=1..12 teams=12
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=12 positions=1..12 teams=12
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
