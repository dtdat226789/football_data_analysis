# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:53:03+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 2. Bundesliga (Germany)
- Scope: league `germany2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/germany2/database_profile.json | yes | yes | 48.15 |
| matches_analysis | data/analysis/germany2/matches_analysis.json | yes | yes | 26.97 |
| goals_analysis | data/analysis/germany2/goals_analysis.json | yes | yes | 12.50 |
| teams_analysis | data/analysis/germany2/teams_analysis.json | yes | yes | 45.00 |
| season_trends | data/analysis/germany2/season_trends.json | yes | yes | 10.47 |
| scoreline_analysis | data/analysis/germany2/scoreline_analysis.json | yes | yes | 298.95 |
| relationships | data/analysis/germany2/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1921 matches: home wins 43.9%, draws 25.4%, away wins 30.7% (844H / 487D / 590A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 55 home and 48 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 490 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1921 matches produced 5721 goals (avg 2.978 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.0% vs away 45.0% of 5721 goals in total (home/away ratio 1.22)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1119 of 1921 matches (58.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 652 scoring matches, 36.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.43, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Paderborn leads with 326 points across 6 seasons (0 title(s), GD 69)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 3 teams present in every one of the 7 seasons (Hannover, Karlsruher SC, Nurnberg)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Braunschweig earns 61 more points at home than away (124 home vs 63 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Schalke won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2022-2023: Heidenheim beat Darmstadt by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.045 per match): first half 2.942 vs last half 2.987 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 5.400)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2022-2023 (luck view, avg abs position diff 2.111)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 215 matches (11.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (175 of 844 home matches, 20.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (215 of 487 draw matches, 44.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (152 of 590 away matches, 25.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 69 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.0942 (n=1840 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 3.93: home 1.705, draw -1.114, away -2.225
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (38)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1921 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1921 |
| Average goals per match | 2.978 |
| Home win rate | 43.9% |
| Draw rate | 25.4% |
| Away win rate | 30.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Paderborn |
| Champion with most titles | Schalke |
| BTTS rate | 58.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 48.15 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 26.97 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.50 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 45.00 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.47 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 298.95 |
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
- **12.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 81 matches, expected 380
- **13.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **14.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 home outcome share 38.9% vs overall 43.9%
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 29.6% vs overall 25.4%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 24.7% vs overall 30.7%
- **18.** `HIGH_SCORING_MATCHES` *(warning)* — 20 match(es) with >= 8 total goals (extreme scorelines)
- **19.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **20.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=327, fgte=327 rows)
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
