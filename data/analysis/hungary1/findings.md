# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:03:25+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: NB I. (Hungary)
- Scope: league `hungary1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/hungary1/database_profile.json | yes | yes | 51.27 |
| matches_analysis | data/analysis/hungary1/matches_analysis.json | yes | yes | 20.16 |
| goals_analysis | data/analysis/hungary1/goals_analysis.json | yes | yes | 12.46 |
| teams_analysis | data/analysis/hungary1/teams_analysis.json | yes | yes | 28.08 |
| season_trends | data/analysis/hungary1/season_trends.json | yes | yes | 10.45 |
| scoreline_analysis | data/analysis/hungary1/scoreline_analysis.json | yes | yes | 196.74 |
| relationships | data/analysis/hungary1/relationships.json | yes | yes | 13.75 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1253 matches: home wins 42.7%, draws 25.7%, away wins 31.6% (535H / 322D / 396A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 32 home and 35 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 320 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1253 matches produced 3634 goals (avg 2.900 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.8% vs away 45.2% of 3634 goals in total (home/away ratio 1.21)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 722 of 1253 matches (57.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 391 scoring matches, 33.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.46, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Ferencvaros leads with 440 points across 7 seasons (5 title(s), GD 232)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 7 seasons (Ferencvaros, Paks, Puskas Academy, Ujpest, Zalaegerszegi)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Ujpest earns 54 more points at home than away (157 home vs 103 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Ferencvaros won 5 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Gyor beat Puskas Academy by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.088 per match): first half 2.843 vs last half 2.931 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021-2022 (luck view, avg abs position diff 8.667)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2024-2025 (luck view, avg abs position diff 1.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 143 matches (11.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (118 of 535 home matches, 22.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (143 of 322 draw matches, 44.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (104 of 396 away matches, 26.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 42 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_goals_avg |corr| = 0.0618 (n=1188 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.151: home 2.041, draw -1.026, away -3.109
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (48)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1253 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1253 |
| Average goals per match | 2.9 |
| Home win rate | 42.7% |
| Draw rate | 25.7% |
| Away win rate | 31.6% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Ferencvaros |
| Champion with most titles | Ferencvaros |
| BTTS rate | 57.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 51.27 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 20.16 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.46 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 28.08 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.45 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 196.74 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.75 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 198 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 198 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 12 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 198 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 12 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 198 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 12 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 198 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 12 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 198 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 12 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 65 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 9.1% vs overall 7.1% (deviation 2.0 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 draw outcome share 29.8% vs overall 25.7%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 away outcome share 26.8% vs overall 31.6%
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 home outcome share 48.5% vs overall 42.7%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 draw outcome share 19.7% vs overall 25.7%
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 10.1% vs overall 7.1% (deviation 3.0 pp)
- **22.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 4.0% vs overall 7.1% (deviation 3.1 pp)
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 away outcome share 35.9% vs overall 31.6%
- **24.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.1% vs overall 7.1% (deviation 4.0 pp)
- **25.** `HIGH_SCORING_MATCHES` *(warning)* — 15 match(es) with >= 8 total goals (extreme scorelines)
- **26.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **27.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=340, fgte=340 rows)
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=12 positions=1..13 teams=12
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=12 positions=3..20 teams=12
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=12 positions=1..24 teams=12
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=12 positions=1..12 teams=12
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=12 positions=2..18 teams=12
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=12 positions=1..24 teams=12
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=12 positions=1..13 teams=12
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=12 positions=5..19 teams=12
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=12 positions=1..24 teams=12
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=12 positions=1..12 teams=12
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=12 positions=4..20 teams=12
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=12 positions=1..24 teams=12
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=12 positions=1..12 teams=12
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=12 positions=1..12 teams=12
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=12 positions=1..12 teams=12
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=12 positions=1..12 teams=12
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=12 positions=1..12 teams=12
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=12 positions=1..12 teams=12
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
