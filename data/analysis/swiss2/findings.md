# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:18:15+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Challenge League (Switzerland)
- Scope: league `swiss2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/swiss2/database_profile.json | yes | yes | 48.76 |
| matches_analysis | data/analysis/swiss2/matches_analysis.json | yes | yes | 17.53 |
| goals_analysis | data/analysis/swiss2/goals_analysis.json | yes | yes | 12.33 |
| teams_analysis | data/analysis/swiss2/teams_analysis.json | yes | yes | 28.93 |
| season_trends | data/analysis/swiss2/season_trends.json | yes | yes | 10.40 |
| scoreline_analysis | data/analysis/swiss2/scoreline_analysis.json | yes | yes | 183.36 |
| relationships | data/analysis/swiss2/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1141 matches: home wins 43.9%, draws 24.9%, away wins 31.2% (501H / 284D / 356A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 27 home and 26 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 310 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1141 matches produced 3442 goals (avg 3.017 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.6% vs away 45.4% of 3442 goals in total (home/away ratio 1.21)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 665 of 1141 matches (58.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 425 scoring matches, 39.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 27.87, median 21.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Aarau leads with 373 points across 7 seasons (0 title(s), GD 68)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 3 teams present in every one of the 7 seasons (Aarau, Wil, Xamax)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Xamax earns 55 more points at home than away (160 home vs 105 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Grasshoppers won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2021-2022: Winterthur beat Schaffhausen by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (-0.033 per match): first half 3.059 vs last half 3.026 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 4.600)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 0.800)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 131 matches (11.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (115 of 501 home matches, 23.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (131 of 284 draw matches, 46.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (73 of 356 away matches, 20.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 47 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.0785 (n=1086 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.303: home 3.203, draw -1.045, away -4.100
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (41)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1141 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1141 |
| Average goals per match | 3.017 |
| Home win rate | 43.9% |
| Draw rate | 24.9% |
| Away win rate | 31.2% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Aarau |
| Champion with most titles | Grasshoppers |
| BTTS rate | 58.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 48.76 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 17.53 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.33 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 28.93 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.40 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 183.36 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 180 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 180 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 10 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 180 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 10 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 180 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 10 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 180 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 11 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 186 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 11 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 55 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 10 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 home outcome share 49.4% vs overall 43.9%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 draw outcome share 20.6% vs overall 24.9%
- **18.** `HIGH_SCORING_MATCHES` *(warning)* — 11 match(es) with >= 8 total goals (extreme scorelines)
- **19.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **20.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=443, fgte=443 rows)
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=10 positions=1..10 teams=10
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=10 positions=1..10 teams=10
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=10 positions=1..10 teams=10
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=10 positions=1..10 teams=10
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=10 positions=1..10 teams=10
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=10 positions=1..10 teams=10
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=10 positions=1..10 teams=10
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=10 positions=1..10 teams=10
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=10 positions=1..10 teams=10
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=10 positions=1..10 teams=10
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=10 positions=1..10 teams=10
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=10 positions=1..10 teams=10
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=11 positions=1..11 teams=11
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=11 positions=1..11 teams=11
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=11 positions=1..11 teams=11
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=11 positions=1..11 teams=11
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=11 positions=1..11 teams=11
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=11 positions=1..11 teams=11
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=10 positions=1..10 teams=10
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=10 positions=1..10 teams=10
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
