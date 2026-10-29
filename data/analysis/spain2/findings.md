# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:17:03+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: LaLiga2 (Spain)
- Scope: league `spain2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/spain2/database_profile.json | yes | yes | 50.31 |
| matches_analysis | data/analysis/spain2/matches_analysis.json | yes | yes | 31.70 |
| goals_analysis | data/analysis/spain2/goals_analysis.json | yes | yes | 12.36 |
| teams_analysis | data/analysis/spain2/teams_analysis.json | yes | yes | 55.39 |
| season_trends | data/analysis/spain2/season_trends.json | yes | yes | 10.47 |
| scoreline_analysis | data/analysis/spain2/scoreline_analysis.json | yes | yes | 417.97 |
| relationships | data/analysis/spain2/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2940 matches: home wins 44.7%, draws 28.8%, away wins 26.5% (1314H / 847D / 779A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 73 home and 59 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 757 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2940 matches produced 6873 goals (avg 2.338 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.2% vs away 42.8% of 6873 goals in total (home/away ratio 1.34)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1429 of 2940 matches (48.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 770 scoring matches, 29.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.08, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Eibar leads with 370 points across 6 seasons (0 title(s), GD 70)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 1 teams present in every one of the 7 seasons (Gijon)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Gijon earns 91 more points at home than away (227 home vs 136 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Espanyol won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: Espanyol beat Mallorca by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.452 per match): first half 2.167 vs last half 2.618 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022-2023 (goals view, avg abs position diff 8.909)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.727)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 396 matches (13.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (396 of 1314 home matches, 30.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (391 of 847 draw matches, 46.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (265 of 779 away matches, 34.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 23 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.083 (n=2819 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.07: home 1.730, draw -0.644, away -3.341
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (47)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2940 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2940 |
| Average goals per match | 2.338 |
| Home win rate | 44.7% |
| Draw rate | 28.8% |
| Away win rate | 26.5% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Eibar |
| Champion with most titles | Espanyol |
| BTTS rate | 48.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.31 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 31.70 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.36 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 55.39 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.47 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 417.97 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 462 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 22 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 462 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 22 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 462 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 22 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 462 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 22 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 462 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 22 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 509 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 23 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 121 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 22 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 14.7% vs overall 10.3% (deviation 4.4 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 draw outcome share 33.3% vs overall 28.8%
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 7.9% vs overall 10.3% (deviation 2.4 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 away outcome share 30.8% vs overall 26.5%
- **20.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 2.702 vs overall 2.338 (deviation 0.364)
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 7.4% vs overall 10.3% (deviation 2.9 pp)
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 21.5% vs overall 28.8%
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 32.2% vs overall 26.5%
- **24.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **25.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **26.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=440, fgte=440 rows)
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=22 positions=1..22 teams=22
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=22 positions=1..22 teams=22
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=22 positions=1..22 teams=22
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=22 positions=1..22 teams=22
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=22 positions=1..22 teams=22
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=22 positions=1..22 teams=22
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=22 positions=1..22 teams=22
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=22 positions=1..22 teams=22
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=22 positions=1..22 teams=22
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=22 positions=1..22 teams=22
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=22 positions=1..22 teams=22
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=22 positions=1..22 teams=22
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=22 positions=1..22 teams=22
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=22 positions=1..22 teams=22
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=22 positions=1..22 teams=22
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=23 positions=1..23 teams=23
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=23 positions=1..23 teams=23
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=23 positions=1..23 teams=23
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=22 positions=1..22 teams=22
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=22 positions=1..22 teams=22
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=22 positions=1..22 teams=22

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
