# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:43:24+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Liga Portugal 2 (Portugal)
- Scope: league `portugal2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/portugal2/database_profile.json | yes | yes | 47.23 |
| matches_analysis | data/analysis/portugal2/matches_analysis.json | yes | yes | 26.76 |
| goals_analysis | data/analysis/portugal2/goals_analysis.json | yes | yes | 12.50 |
| teams_analysis | data/analysis/portugal2/teams_analysis.json | yes | yes | 50.32 |
| season_trends | data/analysis/portugal2/season_trends.json | yes | yes | 10.48 |
| scoreline_analysis | data/analysis/portugal2/scoreline_analysis.json | yes | yes | 280.33 |
| relationships | data/analysis/portugal2/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1908 matches: home wins 40.3%, draws 27.6%, away wins 32.2% (768H / 526D / 614A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 62 home and 42 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 434 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1908 matches produced 4739 goals (avg 2.484 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.1% vs away 46.9% of 4739 goals in total (home/away ratio 1.13)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 998 of 1908 matches (52.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 545 scoring matches, 31.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.76, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Benfica B leads with 297 points across 7 seasons (0 title(s), GD 37)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 7 seasons (Benfica B, FC Porto B, Feirense, Leixoes, Penafiel)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Academico Viseu earns 39 more points at home than away (156 home vs 117 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Estoril won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2024-2025: Tondela beat Alverca by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.075 per match): first half 2.514 vs last half 2.439 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023-2024 (goals view, avg abs position diff 6.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.444)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 248 matches (13.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (206 of 768 home matches, 26.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (248 of 526 draw matches, 47.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (172 of 614 away matches, 28.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 22 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.0476 (n=1840 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.791: home 2.222, draw -0.650, away -2.569
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (38)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1908 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1908 |
| Average goals per match | 2.484 |
| Home win rate | 40.3% |
| Draw rate | 27.6% |
| Away win rate | 32.2% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Benfica B |
| Champion with most titles | Estoril |
| BTTS rate | 52.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 47.23 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 26.76 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.50 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 50.32 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.48 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 280.33 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 306 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 18 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 306 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 18 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 306 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 18 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 310 matches, expected 380
- **12.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 68 matches, expected 380
- **13.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **14.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **15.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 10.6% vs overall 8.6% (deviation 2.0 pp)
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 20.6% vs overall 27.6%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 36.8% vs overall 32.2%
- **18.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **19.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **20.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=397, fgte=397 rows)
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=18 positions=1..18 teams=18
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=18 positions=1..18 teams=18
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=18 positions=1..18 teams=18
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=18 positions=1..18 teams=18
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=18 positions=1..18 teams=18
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=18 positions=1..18 teams=18
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=18 positions=1..18 teams=18
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=18 positions=1..18 teams=18
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=18 positions=1..18 teams=18
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..18 teams=18
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..18 teams=18
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..18 teams=18
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=18 positions=1..18 teams=18
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=18 positions=1..18 teams=18
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=18 positions=1..18 teams=18
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
