# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:41:20+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Botola Pro (Morocco)
- Scope: league `morocco`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/morocco/database_profile.json | yes | yes | 49.39 |
| matches_analysis | data/analysis/morocco/matches_analysis.json | yes | yes | 18.28 |
| goals_analysis | data/analysis/morocco/goals_analysis.json | yes | yes | 12.40 |
| teams_analysis | data/analysis/morocco/teams_analysis.json | yes | yes | 36.18 |
| season_trends | data/analysis/morocco/season_trends.json | yes | yes | 10.47 |
| scoreline_analysis | data/analysis/morocco/scoreline_analysis.json | yes | yes | 206.71 |
| relationships | data/analysis/morocco/relationships.json | yes | yes | 13.77 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1481 matches: home wins 40.0%, draws 32.0%, away wins 28.0% (592H / 474D / 415A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 32 home and 22 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 318 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1481 matches produced 3284 goals (avg 2.217 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.0% vs away 46.0% of 3284 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 708 of 1481 matches (47.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 357 scoring matches, 27.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.92, median 31.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — FAR Rabat leads with 353 points across 7 seasons (1 title(s), GD 141)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 7 teams present in every one of the 7 seasons (Berkane, FAR Rabat, FUS Rabat, Hassania Agadir, IR Tanger...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Raja Casablanca earns 55 more points at home than away (200 home vs 145 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Wydad won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2022-2023: FAR Rabat beat Wydad by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.172 per match): first half 2.182 vs last half 2.354 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.706)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 216 matches (14.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (178 of 592 home matches, 30.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (216 of 474 draw matches, 45.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (133 of 415 away matches, 32.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 16 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.0743 (n=1448 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.904: home 2.822, draw -0.664, away -4.082
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1481 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1481 |
| Average goals per match | 2.217 |
| Home win rate | 40.0% |
| Draw rate | 32.0% |
| Away win rate | 28.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | FAR Rabat |
| Champion with most titles | Wydad |
| BTTS rate | 47.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.39 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 18.28 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.40 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 36.18 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.47 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 206.71 |
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
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 248 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 17 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 33 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 16.7% vs overall 13.1% (deviation 3.6 pp)
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 9.2% vs overall 13.1% (deviation 3.9 pp)
- **18.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 2.576 vs overall 2.217 (deviation 0.359)
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 15.2% vs overall 13.1% (deviation 2.1 pp)
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 24.2% vs overall 40.0%
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 45.5% vs overall 28.0%
- **22.** `HIGH_SCORING_MATCHES` *(warning)* — 3 match(es) with >= 8 total goals (extreme scorelines)
- **23.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **24.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=388, fgte=388 rows)
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=16 positions=1..16 teams=16
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=16 positions=1..16 teams=16
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=16 positions=1..16 teams=16
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=16 positions=1..16 teams=16
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=16 positions=1..16 teams=16
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=16 positions=1..16 teams=16
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=16 positions=1..16 teams=16
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=17 positions=1..17 teams=17
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=17 positions=1..17 teams=17
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=17 positions=1..17 teams=17
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
