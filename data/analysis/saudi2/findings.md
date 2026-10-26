# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:45:48+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Division 1 (Saudi Arabia)
- Scope: league `saudi2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/saudi2/database_profile.json | yes | yes | 50.83 |
| matches_analysis | data/analysis/saudi2/matches_analysis.json | yes | yes | 23.27 |
| goals_analysis | data/analysis/saudi2/goals_analysis.json | yes | yes | 12.43 |
| teams_analysis | data/analysis/saudi2/teams_analysis.json | yes | yes | 56.22 |
| season_trends | data/analysis/saudi2/season_trends.json | yes | yes | 10.03 |
| scoreline_analysis | data/analysis/saudi2/scoreline_analysis.json | yes | yes | 297.16 |
| relationships | data/analysis/saudi2/relationships.json | yes | yes | 13.79 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2054 matches: home wins 39.8%, draws 28.4%, away wins 31.8% (817H / 584D / 653A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 45 home and 40 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 433 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2054 matches produced 5108 goals (avg 2.487 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.3% vs away 46.7% of 5108 goals in total (home/away ratio 1.14)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1081 of 2054 matches (52.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 530 scoring matches, 28.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.36, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Al Jabalain leads with 358 points across 7 seasons (0 title(s), GD 65)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 2 teams present in every one of the 7 seasons (Al Jabalain, Jeddah)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Al Jabalain earns 48 more points at home than away (203 home vs 155 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Al Hazem won 1 of 4 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2022-2023: Al Hazem beat Al Okhdood by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.347 per match): first half 2.278 vs last half 2.625 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021-2022 (luck view, avg abs position diff 44.100)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 3.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 271 matches (13.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (221 of 817 home matches, 27.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (271 of 584 draw matches, 46.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (191 of 653 away matches, 29.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 21 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0753 (n=1987 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 8.543: home 3.703, draw 0.034, away -4.841
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (46)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2054 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2054 |
| Average goals per match | 2.487 |
| Home win rate | 39.8% |
| Draw rate | 28.4% |
| Away win rate | 31.8% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Al Jabalain |
| Champion with most titles | Al Hazem |
| BTTS rate | 52.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.83 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 23.27 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.43 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 56.22 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.03 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 297.16 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.79 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 306 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 18 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 309 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 67 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **11.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **12.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 11.1% vs overall 9.3% (deviation 1.8 pp)
- **13.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 13.4% vs overall 9.3% (deviation 4.1 pp)
- **14.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 draw outcome share 33.7% vs overall 28.4%
- **15.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 7.5% vs overall 9.3% (deviation 1.8 pp)
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 7.5% vs overall 9.3% (deviation 1.8 pp)
- **17.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2025-2026 avg goals 2.968 vs overall 2.487 (deviation 0.481)
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 5.2% vs overall 9.3% (deviation 4.1 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 draw outcome share 23.3% vs overall 28.4%
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 16.4% vs overall 9.3% (deviation 7.1 pp)
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 29.9% vs overall 39.8%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 41.8% vs overall 28.4%
- **23.** `HIGH_SCORING_MATCHES` *(warning)* — 7 match(es) with >= 8 total goals (extreme scorelines)
- **24.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (18 extra rows)
- **25.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=425, fgte=425 rows)
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=20 positions=2..21 teams=20
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=20 positions=12..59 teams=20
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=20 positions=1..85 teams=20
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=20 positions=2..21 teams=20
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=20 positions=25..66 teams=20
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=20 positions=1..85 teams=20
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=18 positions=1..19 teams=18
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=18 positions=33..63 teams=18
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=18 positions=1..74 teams=18
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..19 teams=18
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=13..39 teams=18
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..51 teams=18
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=18 positions=1..18 teams=18
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=18 positions=5..26 teams=18
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=18 positions=1..36 teams=18
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=2..19 teams=18
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..19 teams=18
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=2..19 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
