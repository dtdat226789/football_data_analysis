# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:19:42+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premiere Ligue Women (France)
- Scope: league `wfrance1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/wfrance1/database_profile.json | yes | yes | 52.18 |
| matches_analysis | data/analysis/wfrance1/matches_analysis.json | yes | yes | 13.02 |
| goals_analysis | data/analysis/wfrance1/goals_analysis.json | yes | yes | 12.70 |
| teams_analysis | data/analysis/wfrance1/teams_analysis.json | yes | yes | 31.17 |
| season_trends | data/analysis/wfrance1/season_trends.json | yes | yes | 10.41 |
| scoreline_analysis | data/analysis/wfrance1/scoreline_analysis.json | yes | yes | 153.82 |
| relationships | data/analysis/wfrance1/relationships.json | yes | yes | 13.73 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 829 matches: home wins 44.1%, draws 16.5%, away wins 39.3% (366H / 137D / 326A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 15 home and 12 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 251 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 829 matches produced 2684 goals (avg 3.238 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.3% vs away 46.7% of 2684 goals in total (home/away ratio 1.14)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 364 of 829 matches (43.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 309 scoring matches, 39.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 27.08, median 21.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Lyon W leads with 375 points across 6 seasons (5 title(s), GD 435)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 4 teams present in every one of the 7 seasons (Fleury 91 W, Montpellier W, PSG W, Paris FC W)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Guingamp W earns 25 more points at home than away (61 home vs 36 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Lyon W won 5 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: PSG W beat Lyon W by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.089 per match): first half 3.164 vs last half 3.253 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022-2023 (goals view, avg abs position diff 4.167)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2024-2025 (luck view, avg abs position diff 1.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 0-1 in 63 matches (7.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (61 of 366 home matches, 16.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (56 of 137 draw matches, 40.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (63 of 326 away matches, 19.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 60 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.1043 (n=795 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 15.099: home 7.217, draw -1.589, away -7.883
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (50)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 829 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 829 |
| Average goals per match | 3.238 |
| Home win rate | 44.1% |
| Draw rate | 16.5% |
| Away win rate | 39.3% |
| Most common scoreline | 0-1 |
| Dominant team (lifetime points) | Lyon W |
| Champion with most titles | Lyon W |
| BTTS rate | 43.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 52.18 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 13.02 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.70 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 31.17 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.41 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 153.82 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.73 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 132 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 132 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 12 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 132 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 12 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 132 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 12 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 132 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 12 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 135 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 12 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 34 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 7.6% vs overall 5.3% (deviation 2.3 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 48.5% vs overall 44.1%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 11.4% vs overall 16.5%
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 draw outcome share 11.4% vs overall 16.5%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 away outcome share 45.5% vs overall 39.3%
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 2.3% vs overall 5.3% (deviation 3.0 pp)
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 away outcome share 33.3% vs overall 39.3%
- **23.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 9.1% vs overall 5.3% (deviation 3.8 pp)
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 home outcome share 39.3% vs overall 44.1%
- **25.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 23.5% vs overall 16.5%
- **26.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 32.4% vs overall 39.3%
- **27.** `HIGH_SCORING_MATCHES` *(warning)* — 27 match(es) with >= 8 total goals (extreme scorelines)
- **28.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **29.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=511, fgte=511 rows)
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=12 positions=1..12 teams=12
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=12 positions=1..12 teams=12
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=12 positions=1..12 teams=12
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=12 positions=1..12 teams=12
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=12 positions=1..12 teams=12
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=12 positions=1..12 teams=12
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=12 positions=1..12 teams=12
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=12 positions=1..12 teams=12
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=12 positions=1..12 teams=12
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=12 positions=1..12 teams=12
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=12 positions=1..12 teams=12
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=12 positions=1..12 teams=12
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=12 positions=1..12 teams=12
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=12 positions=1..12 teams=12
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=12 positions=1..12 teams=12
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=12 positions=1..12 teams=12
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=12 positions=1..12 teams=12
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=12 positions=1..12 teams=12
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **50.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
