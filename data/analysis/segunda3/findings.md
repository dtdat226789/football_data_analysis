# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:48:02+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Segunda RFEF - Group 3 (Spain)
- Scope: league `segunda3`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/segunda3/database_profile.json | yes | yes | 50.17 |
| matches_analysis | data/analysis/segunda3/matches_analysis.json | yes | yes | 22.32 |
| goals_analysis | data/analysis/segunda3/goals_analysis.json | yes | yes | 12.43 |
| teams_analysis | data/analysis/segunda3/teams_analysis.json | yes | yes | 70.84 |
| season_trends | data/analysis/segunda3/season_trends.json | yes | yes | 10.50 |
| scoreline_analysis | data/analysis/segunda3/scoreline_analysis.json | yes | yes | 253.35 |
| relationships | data/analysis/segunda3/relationships.json | yes | yes | 13.79 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1795 matches: home wins 43.2%, draws 30.4%, away wins 26.5% (775H / 545D / 475A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 43 home and 36 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 431 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1795 matches produced 4138 goals (avg 2.305 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.1% vs away 42.9% of 4138 goals in total (home/away ratio 1.33)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 864 of 1795 matches (48.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 461 scoring matches, 28.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.51, median 30.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Espanyol B leads with 274 points across 6 seasons (0 title(s), GD 6)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 0 teams present in every one of the 7 seasons
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Espanyol B earns 46 more points at home than away (160 home vs 114 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — UD Ibiza won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Baleares beat Sant Andreu by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.287 per match): first half 2.161 vs last half 2.448 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2020-2021 (goals view, avg abs position diff 7.429)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2024-2025 (luck view, avg abs position diff 2.111)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 256 matches (14.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (256 of 775 home matches, 33.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (253 of 545 draw matches, 46.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (172 of 475 away matches, 36.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 14 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.0847 (n=1730 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.194: home 1.556, draw -0.758, away -2.638
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (46)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1795 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1795 |
| Average goals per match | 2.305 |
| Home win rate | 43.2% |
| Draw rate | 30.4% |
| Away win rate | 26.5% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Espanyol B |
| Champion with most titles | UD Ibiza |
| BTTS rate | 48.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.17 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 22.32 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.43 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 70.84 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.50 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 253.35 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.79 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 200 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 21 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 306 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 18 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 306 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 18 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 306 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 18 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 306 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 65 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 12.5% vs overall 10.6% (deviation 1.9 pp)
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 13.7% vs overall 10.6% (deviation 3.1 pp)
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 8.8% vs overall 10.6% (deviation 1.8 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 home outcome share 37.3% vs overall 43.2%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 away outcome share 33.7% vs overall 26.5%
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.1% vs overall 10.6% (deviation 7.5 pp)
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 24.6% vs overall 30.4%
- **23.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **24.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (24 extra rows)
- **25.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=427, fgte=427 rows)
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=21 positions=1..21 teams=21
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=21 positions=1..21 teams=21
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=21 positions=1..21 teams=21
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=18 positions=1..18 teams=18
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=18 positions=1..18 teams=18
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=18 positions=1..18 teams=18
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=18 positions=1..18 teams=18
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=18 positions=1..18 teams=18
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=18 positions=1..18 teams=18
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..18 teams=18
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..18 teams=18
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..18 teams=18
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=18 positions=1..18 teams=18
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=18 positions=1..18 teams=18
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=18 positions=1..18 teams=18
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
