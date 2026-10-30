# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:44:01+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Ligue 1 (Algeria)
- Scope: league `algir1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/algir1/database_profile.json | yes | yes | 49.69 |
| matches_analysis | data/analysis/algir1/matches_analysis.json | yes | yes | 17.20 |
| goals_analysis | data/analysis/algir1/goals_analysis.json | yes | yes | 12.41 |
| teams_analysis | data/analysis/algir1/teams_analysis.json | yes | yes | 40.57 |
| season_trends | data/analysis/algir1/season_trends.json | yes | yes | 10.43 |
| scoreline_analysis | data/analysis/algir1/scoreline_analysis.json | yes | yes | 249.52 |
| relationships | data/analysis/algir1/relationships.json | yes | yes | 13.77 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1697 matches: home wins 50.6%, draws 28.2%, away wins 21.2% (859H / 478D / 360A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 34 home and 17 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 488 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1697 matches produced 3795 goals (avg 2.236 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 61.1% vs away 38.9% of 3795 goals in total (home/away ratio 1.57)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 731 of 1697 matches (43.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 406 scoring matches, 27.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 35.97, median 31.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — CR Belouizdad leads with 389 points across 7 seasons (4 title(s), GD 166)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 7 seasons (ASO Chlef, CR Belouizdad, Constantine, ES Setif, Kabylie...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Saoura earns 119 more points at home than away (217 home vs 98 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — CR Belouizdad won 4 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: CR Belouizdad beat Oran by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.111 per match): first half 2.265 vs last half 2.154 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021-2022 (goals view, avg abs position diff 7.778)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.375)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 295 matches (17.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (295 of 859 home matches, 34.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 0-0 (207 of 478 draw matches, 43.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (132 of 360 away matches, 36.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 26 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_conceded_last_5 |corr| = 0.1359 (n=1645 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.676: home 1.897, draw -0.807, away -5.779
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (43)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1697 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1697 |
| Average goals per match | 2.236 |
| Home win rate | 50.6% |
| Draw rate | 28.2% |
| Away win rate | 21.2% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | CR Belouizdad |
| Champion with most titles | CR Belouizdad |
| BTTS rate | 43.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.69 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 17.20 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.41 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 40.57 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.43 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 249.52 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.77 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 379 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 306 matches, expected 380
- **3.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 18 teams, expected 20
- **4.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 240 matches, expected 380
- **5.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 16 teams, expected 20
- **6.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 240 matches, expected 380
- **7.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 16 teams, expected 20
- **8.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 240 matches, expected 380
- **9.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 16 teams, expected 20
- **10.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 240 matches, expected 380
- **11.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **12.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 52 matches, expected 380
- **13.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **14.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **15.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 9.8% vs overall 12.2% (deviation 2.4 pp)
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 14.1% vs overall 12.2% (deviation 1.9 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 home outcome share 57.1% vs overall 50.6%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 away outcome share 16.2% vs overall 21.2%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 17.5% vs overall 12.2% (deviation 5.3 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 8.3% vs overall 12.2% (deviation 3.9 pp)
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 42.3% vs overall 50.6%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 34.6% vs overall 28.2%
- **23.** `HIGH_SCORING_MATCHES` *(warning)* — 15 match(es) with >= 8 total goals (extreme scorelines)
- **24.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **25.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=3, fgte=3 rows)
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=18 positions=1..18 teams=18
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=18 positions=1..18 teams=18
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=18 positions=1..18 teams=18
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=16 positions=1..16 teams=16
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=16 positions=1..16 teams=16
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=16 positions=1..16 teams=16
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=16 positions=1..16 teams=16
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
