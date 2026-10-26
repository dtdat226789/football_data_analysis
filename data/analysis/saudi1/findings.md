# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:45:31+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Saudi Professional League (Saudi Arabia)
- Scope: league `saudi1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/saudi1/database_profile.json | yes | yes | 50.83 |
| matches_analysis | data/analysis/saudi1/matches_analysis.json | yes | yes | 23.83 |
| goals_analysis | data/analysis/saudi1/goals_analysis.json | yes | yes | 12.45 |
| teams_analysis | data/analysis/saudi1/teams_analysis.json | yes | yes | 38.82 |
| season_trends | data/analysis/saudi1/season_trends.json | yes | yes | 10.54 |
| scoreline_analysis | data/analysis/saudi1/scoreline_analysis.json | yes | yes | 275.99 |
| relationships | data/analysis/saudi1/relationships.json | yes | yes | 13.80 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1737 matches: home wins 43.2%, draws 23.2%, away wins 33.6% (751H / 403D / 583A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 44 home and 44 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 448 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1737 matches produced 5045 goals (avg 2.904 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.1% vs away 46.9% of 5045 goals in total (home/away ratio 1.13)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 963 of 1737 matches (55.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 510 scoring matches, 31.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.37, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Al Hilal leads with 470 points across 7 seasons (4 title(s), GD 304)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 7 teams present in every one of the 7 seasons (Al Ettifaq, Al Fateh, Al Hilal, Al Ittihad, Al Nassr...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Abha earns 62 more points at home than away (100 home vs 38 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Al Hilal won 4 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Al Nassr beat Al Hilal by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.115 per match): first half 2.821 vs last half 2.936 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2020-2021 (luck view, avg abs position diff 9.312)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.444)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 197 matches (11.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (174 of 751 home matches, 23.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (197 of 403 draw matches, 48.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (129 of 583 away matches, 22.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 49 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_goals_avg |corr| = 0.1029 (n=1646 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 11.338: home 4.894, draw -0.710, away -6.444
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (47)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1737 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1737 |
| Average goals per match | 2.904 |
| Home win rate | 43.2% |
| Draw rate | 23.2% |
| Away win rate | 33.6% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Al Hilal |
| Champion with most titles | Al Hilal |
| BTTS rate | 55.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.83 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 23.83 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.45 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 38.82 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.54 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 275.99 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.80 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 240 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 16 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 240 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 16 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 306 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 18 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 314 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 91 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 3.8% vs overall 5.8% (deviation 2.0 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 38.8% vs overall 43.2%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 draw outcome share 27.9% vs overall 23.2%
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 away outcome share 26.7% vs overall 33.6%
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 7.8% vs overall 5.8% (deviation 2.0 pp)
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 3.9% vs overall 5.8% (deviation 1.9 pp)
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 draw outcome share 18.6% vs overall 23.2%
- **23.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 11.0% vs overall 5.8% (deviation 5.2 pp)
- **24.** `HIGH_SCORING_MATCHES` *(warning)* — 12 match(es) with >= 8 total goals (extreme scorelines)
- **25.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (18 extra rows)
- **26.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=418, fgte=418 rows)
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=16 positions=1..16 teams=16
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=16 positions=6..26 teams=16
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=16 positions=1..32 teams=16
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=16 positions=1..17 teams=16
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=16 positions=5..26 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=16 positions=1..32 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..18 teams=18
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..18 teams=18
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..18 teams=18
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=18 positions=1..18 teams=18
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=18 positions=1..18 teams=18
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=18 positions=1..18 teams=18
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..19 teams=18
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..19 teams=18
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..19 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
