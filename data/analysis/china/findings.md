# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:28:37+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Super League (China)
- Scope: league `china`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/china/database_profile.json | yes | yes | 50.33 |
| matches_analysis | data/analysis/china/matches_analysis.json | yes | yes | 23.11 |
| goals_analysis | data/analysis/china/goals_analysis.json | yes | yes | 12.16 |
| teams_analysis | data/analysis/china/teams_analysis.json | yes | yes | 39.65 |
| season_trends | data/analysis/china/season_trends.json | yes | yes | 10.32 |
| scoreline_analysis | data/analysis/china/scoreline_analysis.json | yes | yes | 228.98 |
| relationships | data/analysis/china/relationships.json | yes | yes | 13.77 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1482 matches: home wins 44.5%, draws 24.6%, away wins 30.9% (660H / 364D / 458A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 47 home and 33 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 427 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1482 matches produced 4414 goals (avg 2.978 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.4% vs away 44.6% of 4414 goals in total (home/away ratio 1.24)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 838 of 1482 matches (56.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 481 scoring matches, 34.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.62, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Shanghai Port leads with 379 points across 7 seasons (3 title(s), GD 207)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 6 teams present in every one of the 7 seasons (Beijing Guoan, Henan Songshan Longmen, Shandong Taishan, Shanghai Port, Shanghai Shenhua...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Qingdao Hainiu earns 57 more points at home than away (80 home vs 23 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Shanghai Port won 3 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2022: Wuhan Three Towns beat Shandong Taishan by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.357 per match): first half 2.804 vs last half 3.161 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022 (goals view, avg abs position diff 6.556)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 2.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 173 matches (11.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (133 of 660 home matches, 20.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (173 of 364 draw matches, 47.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (104 of 458 away matches, 22.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 52 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.156 (n=1250 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 11.793: home 5.109, draw -0.815, away -6.684
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (47)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1482 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1482 |
| Average goals per match | 2.978 |
| Home win rate | 44.5% |
| Draw rate | 24.6% |
| Away win rate | 30.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Shanghai Port |
| Champion with most titles | Shanghai Port |
| BTTS rate | 56.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.33 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 23.11 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.16 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.65 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.32 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 228.98 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.77 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 112 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 112 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 16 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 306 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 18 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 240 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 16 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 240 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 16 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 240 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 16 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 232 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 16 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 home outcome share 40.2% vs overall 44.5%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 away outcome share 35.7% vs overall 30.9%
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021 goalless share 11.6% vs overall 6.0% (deviation 5.6 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021 away outcome share 25.0% vs overall 30.9%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022 draw outcome share 20.3% vs overall 24.6%
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022 away outcome share 37.3% vs overall 30.9%
- **22.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025 goalless share 3.8% vs overall 6.0% (deviation 2.2 pp)
- **23.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 4.3% vs overall 6.0% (deviation 1.7 pp)
- **24.** `HIGH_SCORING_MATCHES` *(warning)* — 15 match(es) with >= 8 total goals (extreme scorelines)
- **25.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **26.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=305, fgte=305 rows)
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=16 positions=1..16 teams=16
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=16 positions=1..16 teams=16
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=16 positions=1..16 teams=16
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=16 positions=1..16 teams=16
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=18 positions=1..18 teams=18
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=18 positions=1..18 teams=18
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=18 positions=1..18 teams=18
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=16 positions=1..16 teams=16
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=16 positions=1..16 teams=16
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=16 positions=1..16 teams=16
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=16 positions=1..16 teams=16
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=16 positions=1..16 teams=16
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=16 positions=1..16 teams=16
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=16 positions=1..16 teams=16
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=16 positions=1..16 teams=16
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
