# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:41:12+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Jupiler Pro League (Belgium)
- Scope: league `belgium1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/belgium1/database_profile.json | yes | yes | 50.31 |
| matches_analysis | data/analysis/belgium1/matches_analysis.json | yes | yes | 24.53 |
| goals_analysis | data/analysis/belgium1/goals_analysis.json | yes | yes | 12.43 |
| teams_analysis | data/analysis/belgium1/teams_analysis.json | yes | yes | 36.91 |
| season_trends | data/analysis/belgium1/season_trends.json | yes | yes | 10.51 |
| scoreline_analysis | data/analysis/belgium1/scoreline_analysis.json | yes | yes | 281.03 |
| relationships | data/analysis/belgium1/relationships.json | yes | yes | 13.79 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1799 matches: home wins 43.2%, draws 24.2%, away wins 32.6% (777H / 436D / 586A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 43 home and 48 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 488 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1799 matches produced 5179 goals (avg 2.879 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.8% vs away 45.2% of 5179 goals in total (home/away ratio 1.21)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 988 of 1799 matches (54.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 568 scoring matches, 33.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.49, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Club Brugge KV leads with 429 points across 7 seasons (2 title(s), GD 231)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 11 teams present in every one of the 7 seasons (Anderlecht, Antwerp, Cercle Brugge KSV, Charleroi, Club Brugge KV...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Genk earns 59 more points at home than away (215 home vs 156 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Club Brugge KV won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2022-2023: Genk beat Royale Union SG by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.132 per match): first half 2.988 vs last half 2.856 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 6.556)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.667)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 212 matches (11.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (155 of 777 home matches, 19.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (212 of 436 draw matches, 48.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (135 of 586 away matches, 23.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 46 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0806 (n=1719 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.548: home 3.386, draw -1.090, away -4.162
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1799 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1799 |
| Average goals per match | 2.879 |
| Home win rate | 43.2% |
| Draw rate | 24.2% |
| Away win rate | 32.6% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Club Brugge KV |
| Champion with most titles | Club Brugge KV |
| BTTS rate | 54.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.31 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 24.53 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.43 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 36.91 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.51 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 281.03 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.79 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 306 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 18 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 306 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 18 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 240 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 16 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 240 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 16 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 321 matches, expected 380
- **12.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 80 matches, expected 380
- **13.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **14.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 36.9% vs overall 32.6%
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 3.9% vs overall 5.7% (deviation 1.8 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 away outcome share 27.9% vs overall 32.6%
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 9.2% vs overall 5.7% (deviation 3.5 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 draw outcome share 28.8% vs overall 24.2%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 away outcome share 25.4% vs overall 32.6%
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 7.8% vs overall 5.7% (deviation 2.1 pp)
- **22.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.8% vs overall 5.7% (deviation 1.9 pp)
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 51.2% vs overall 43.2%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 18.8% vs overall 24.2%
- **25.** `HIGH_SCORING_MATCHES` *(warning)* — 16 match(es) with >= 8 total goals (extreme scorelines)
- **26.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **27.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=15, fgte=15 rows)
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=18 positions=1..18 teams=18
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=18 positions=1..18 teams=18
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=18 positions=1..18 teams=18
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=18 positions=1..18 teams=18
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=18 positions=1..18 teams=18
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=18 positions=1..18 teams=18
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=18 positions=1..18 teams=18
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=18 positions=1..18 teams=18
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=18 positions=1..18 teams=18
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=16 positions=1..16 teams=16
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=16 positions=1..16 teams=16
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=16 positions=1..16 teams=16
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=16 positions=1..16 teams=16
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
