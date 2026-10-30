# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:55:27+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Tweede Divisie (Netherlands)
- Scope: league `holland3`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/holland3/database_profile.json | yes | yes | 50.74 |
| matches_analysis | data/analysis/holland3/matches_analysis.json | yes | yes | 24.68 |
| goals_analysis | data/analysis/holland3/goals_analysis.json | yes | yes | 12.50 |
| teams_analysis | data/analysis/holland3/teams_analysis.json | yes | yes | 43.20 |
| season_trends | data/analysis/holland3/season_trends.json | yes | yes | 10.47 |
| scoreline_analysis | data/analysis/holland3/scoreline_analysis.json | yes | yes | 281.55 |
| relationships | data/analysis/holland3/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1693 matches: home wins 44.9%, draws 20.6%, away wins 34.5% (760H / 349D / 584A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 49 home and 42 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 476 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1693 matches produced 5463 goals (avg 3.227 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.9% vs away 46.1% of 5463 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1006 of 1693 matches (59.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 585 scoring matches, 35.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.65, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Quick Boys leads with 348 points across 7 seasons (3 title(s), GD 141)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 7 seasons (AFC, De Treffers, HFC, Hardenberg, Jong Sparta Rotterdam...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Excelsior Maassluis earns 64 more points at home than away (133 home vs 69 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Quick Boys won 3 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: AFC beat ASWH by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.280 per match): first half 3.104 vs last half 3.383 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022-2023 (goals view, avg abs position diff 6.778)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020-2021 (luck view, avg abs position diff 1.667)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 160 matches (9.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (145 of 760 home matches, 19.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (160 of 349 draw matches, 45.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (111 of 584 away matches, 19.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 69 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0671 (n=1593 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.436: home 2.844, draw -0.520, away -3.592
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1693 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1693 |
| Average goals per match | 3.227 |
| Home win rate | 44.9% |
| Draw rate | 20.6% |
| Away win rate | 34.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Quick Boys |
| Champion with most titles | Quick Boys |
| BTTS rate | 59.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.74 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 24.68 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.50 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 43.20 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.47 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 281.55 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 47 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 306 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 18 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 306 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 18 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 306 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 18 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 322 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 25 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 100 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 31.9% vs overall 20.6%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 25.5% vs overall 34.5%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 home outcome share 50.3% vs overall 44.9%
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 away outcome share 30.1% vs overall 34.5%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 home outcome share 38.9% vs overall 44.9%
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 1.0% vs overall 3.4% (deviation 2.4 pp)
- **22.** `HIGH_SCORING_MATCHES` *(warning)* — 22 match(es) with >= 8 total goals (extreme scorelines)
- **23.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **24.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=339, fgte=339 rows)
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=18 positions=1..18 teams=18
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=18 positions=1..18 teams=18
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=18 positions=1..18 teams=18
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=18 positions=1..18 teams=18
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=18 positions=1..18 teams=18
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=18 positions=1..18 teams=18
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=18 positions=1..18 teams=18
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=18 positions=1..18 teams=18
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=18 positions=1..18 teams=18
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..18 teams=18
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..18 teams=18
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..18 teams=18
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=18 positions=1..18 teams=18
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=18 positions=1..18 teams=18
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=18 positions=1..18 teams=18
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=25 positions=1..25 teams=25
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=25 positions=1..25 teams=25
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=25 positions=1..25 teams=25
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
