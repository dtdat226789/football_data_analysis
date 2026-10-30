# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T04:15:02+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Super Lig (Turkey)
- Scope: league `turkey1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/turkey1/database_profile.json | yes | yes | 47.80 |
| matches_analysis | data/analysis/turkey1/matches_analysis.json | yes | yes | 31.18 |
| goals_analysis | data/analysis/turkey1/goals_analysis.json | yes | yes | 12.36 |
| teams_analysis | data/analysis/turkey1/teams_analysis.json | yes | yes | 43.43 |
| season_trends | data/analysis/turkey1/season_trends.json | yes | yes | 10.49 |
| scoreline_analysis | data/analysis/turkey1/scoreline_analysis.json | yes | yes | 346.02 |
| relationships | data/analysis/turkey1/relationships.json | yes | yes | 13.79 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2251 matches: home wins 45.0%, draws 25.1%, away wins 29.9% (1013H / 565D / 673A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 67 home and 60 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 607 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2251 matches produced 6357 goals (avg 2.824 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.9% vs away 44.1% of 6357 goals in total (home/away ratio 1.27)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1244 of 2251 matches (55.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 653 scoring matches, 31.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.07, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Galatasaray leads with 520 points across 7 seasons (5 title(s), GD 278)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 7 seasons (Alanyaspor, Basaksehir, Besiktas, Fenerbahce, Galatasaray...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Antalyaspor earns 77 more points at home than away (173 home vs 96 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Galatasaray won 5 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: Besiktas beat Galatasaray by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (-0.022 per match): first half 2.852 vs last half 2.83 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021-2022 (goals view, avg abs position diff 6.300)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2023-2024 (luck view, avg abs position diff 2.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 275 matches (12.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (210 of 1013 home matches, 20.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (275 of 565 draw matches, 48.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (160 of 673 away matches, 23.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 60 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.1123 (n=2170 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 10.722: home 4.190, draw -0.405, away -6.532
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (35)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2251 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2251 |
| Average goals per match | 2.824 |
| Home win rate | 45.0% |
| Draw rate | 25.1% |
| Away win rate | 29.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Galatasaray |
| Champion with most titles | Galatasaray |
| BTTS rate | 55.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 47.80 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 31.18 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.36 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 43.43 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.49 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 346.02 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.79 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 420 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 21 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 342 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 19 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 342 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 19 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 306 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 81 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **11.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **12.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 9.0% vs overall 7.2% (deviation 1.8 pp)
- **13.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 4.7% vs overall 7.2% (deviation 2.5 pp)
- **14.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 9.2% vs overall 7.2% (deviation 2.0 pp)
- **15.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.9% vs overall 7.2% (deviation 2.3 pp)
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 17.3% vs overall 25.1%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 34.6% vs overall 29.9%
- **18.** `HIGH_SCORING_MATCHES` *(warning)* — 22 match(es) with >= 8 total goals (extreme scorelines)
- **19.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **20.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=474, fgte=474 rows)
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=21 positions=1..21 teams=21
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=21 positions=1..21 teams=21
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=21 positions=1..21 teams=21
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=19 positions=1..19 teams=19
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=19 positions=1..19 teams=19
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=19 positions=1..19 teams=19
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=19 positions=1..19 teams=19
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=19 positions=1..19 teams=19
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=19 positions=1..19 teams=19
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
