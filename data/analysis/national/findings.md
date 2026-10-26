# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:41:41+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: National League (England)
- Scope: league `national`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/national/database_profile.json | yes | yes | 46.56 |
| matches_analysis | data/analysis/national/matches_analysis.json | yes | yes | 38.37 |
| goals_analysis | data/analysis/national/goals_analysis.json | yes | yes | 11.35 |
| teams_analysis | data/analysis/national/teams_analysis.json | yes | yes | 58.29 |
| season_trends | data/analysis/national/season_trends.json | yes | yes | 9.15 |
| scoreline_analysis | data/analysis/national/scoreline_analysis.json | yes | yes | 442.23 |
| relationships | data/analysis/national/relationships.json | yes | yes | 13.80 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2885 matches: home wins 43.4%, draws 24.7%, away wins 31.9% (1251H / 713D / 921A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 98 home and 73 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 748 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2885 matches produced 8180 goals (avg 2.835 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.9% vs away 45.1% of 8180 goals in total (home/away ratio 1.22)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1607 of 2885 matches (55.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 908 scoring matches, 33.4% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.61, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Southend leads with 379 points across 6 seasons (0 title(s), GD 78)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 8 teams present in every one of the 6 seasons (Aldershot, Altrincham, Eastleigh, FC Halifax, Solihull Moors...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Altrincham earns 74 more points at home than away (205 home vs 131 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Stockport County won 1 of 6 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2022-2023: Wrexham beat Notts Co by 4 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.087 per match): first half 2.823 vs last half 2.91 across 6 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 8.500)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.917)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 361 matches (12.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (265 of 1251 home matches, 21.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (361 of 713 draw matches, 50.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (214 of 921 away matches, 23.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 75 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.0815 (n=2719 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 9.973: home 4.416, draw -0.722, away -5.557
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (37)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 6 of 6 registered seasons populated (100.0%); 2885 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2885 |
| Average goals per match | 2.835 |
| Home win rate | 43.4% |
| Draw rate | 24.7% |
| Away win rate | 31.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Southend |
| Champion with most titles | Stockport County |
| BTTS rate | 55.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 46.56 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 38.37 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 11.35 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 58.29 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 9.15 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 442.23 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.80 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 506 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 23 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 552 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 24 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 552 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 24 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 552 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 24 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 557 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 24 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 166 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **13.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **14.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 1.2% vs overall 5.6% (deviation 4.4 pp)
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 17.5% vs overall 24.7%
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 36.7% vs overall 31.9%
- **17.** `HIGH_SCORING_MATCHES` *(warning)* — 25 match(es) with >= 8 total goals (extreme scorelines)
- **18.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **19.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=390, fgte=390 rows)
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=23 positions=1..23 teams=23
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=23 positions=1..23 teams=23
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=23 positions=1..23 teams=23
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=24 positions=1..24 teams=24
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=24 positions=1..24 teams=24
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=24 positions=1..24 teams=24
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=24 positions=1..24 teams=24
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=24 positions=1..24 teams=24
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=24 positions=1..24 teams=24
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=24 positions=1..24 teams=24
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=24 positions=1..24 teams=24
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=24 positions=1..24 teams=24
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=24 positions=1..24 teams=24
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=24 positions=1..24 teams=24
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=24 positions=1..24 teams=24
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=24 positions=1..24 teams=24
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=24 positions=1..24 teams=24
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=24 positions=1..24 teams=24

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
