# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:42:37+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Championship (England)
- Scope: league `cha`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/cha/database_profile.json | yes | yes | 49.44 |
| matches_analysis | data/analysis/cha/matches_analysis.json | yes | yes | 41.94 |
| goals_analysis | data/analysis/cha/goals_analysis.json | yes | yes | 12.39 |
| teams_analysis | data/analysis/cha/teams_analysis.json | yes | yes | 56.59 |
| season_trends | data/analysis/cha/season_trends.json | yes | yes | 10.47 |
| scoreline_analysis | data/analysis/cha/scoreline_analysis.json | yes | yes | 513.05 |
| relationships | data/analysis/cha/relationships.json | yes | yes | 13.80 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 3463 matches: home wins 43.0%, draws 26.0%, away wins 31.0% (1490H / 901D / 1072A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 101 home and 89 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 875 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 3463 matches produced 8695 goals (avg 2.511 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.4% vs away 44.6% of 8695 goals in total (home/away ratio 1.24)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1757 of 3463 matches (50.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 1026 scoring matches, 32.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.77, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Middlesbrough leads with 448 points across 7 seasons (1 title(s), GD 89)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 8 teams present in every one of the 7 seasons (Blackburn, Bristol City, Middlesbrough, Millwall, Preston...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — West Brom earns 92 more points at home than away (219 home vs 127 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Norwich won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2024-2025: Leeds beat Burnley by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.226 per match): first half 2.416 vs last half 2.642 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 8.667)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020-2021 (luck view, avg abs position diff 3.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 444 matches (12.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (379 of 1490 home matches, 25.4%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (444 of 901 draw matches, 49.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (316 of 1072 away matches, 29.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 47 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.0435 (n=3319 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.767: home 2.596, draw -1.144, away -3.172
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (43)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 3463 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 3463 |
| Average goals per match | 2.511 |
| Home win rate | 43.0% |
| Draw rate | 26.0% |
| Away win rate | 31.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Middlesbrough |
| Champion with most titles | Norwich |
| BTTS rate | 50.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.44 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 41.94 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.39 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 56.59 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.47 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 513.05 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.80 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 552 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 24 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 552 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 24 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 552 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 24 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 552 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 24 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 552 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 24 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 559 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 24 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 144 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 9.6% vs overall 7.8% (deviation 1.8 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 away outcome share 25.9% vs overall 31.0%
- **18.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 2.889 vs overall 2.511 (deviation 0.378)
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 6.2% vs overall 7.8% (deviation 1.6 pp)
- **20.** `HIGH_SCORING_MATCHES` *(warning)* — 17 match(es) with >= 8 total goals (extreme scorelines)
- **21.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **22.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=296, fgte=296 rows)
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=24 positions=1..24 teams=24
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=24 positions=1..24 teams=24
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=24 positions=1..24 teams=24
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=24 positions=1..24 teams=24
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=24 positions=1..24 teams=24
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=24 positions=1..24 teams=24
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=24 positions=1..24 teams=24
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=24 positions=1..24 teams=24
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=24 positions=1..24 teams=24
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=24 positions=1..24 teams=24
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=24 positions=1..24 teams=24
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=24 positions=1..24 teams=24
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=24 positions=1..24 teams=24
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=24 positions=1..24 teams=24
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=24 positions=1..24 teams=24
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=24 positions=1..24 teams=24
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=24 positions=1..24 teams=24
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=24 positions=1..24 teams=24
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=24 positions=1..24 teams=24
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=24 positions=1..24 teams=24
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=24 positions=1..24 teams=24

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
