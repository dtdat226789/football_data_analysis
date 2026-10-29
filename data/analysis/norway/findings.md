# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:09:22+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Eliteserien (Norway)
- Scope: league `norway`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/norway/database_profile.json | yes | yes | 50.04 |
| matches_analysis | data/analysis/norway/matches_analysis.json | yes | yes | 22.77 |
| goals_analysis | data/analysis/norway/goals_analysis.json | yes | yes | 12.24 |
| teams_analysis | data/analysis/norway/teams_analysis.json | yes | yes | 32.32 |
| season_trends | data/analysis/norway/season_trends.json | yes | yes | 10.23 |
| scoreline_analysis | data/analysis/norway/scoreline_analysis.json | yes | yes | 258.67 |
| relationships | data/analysis/norway/relationships.json | yes | yes | 13.76 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1632 matches: home wins 46.7%, draws 22.4%, away wins 30.9% (762H / 365D / 505A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 52 home and 33 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 475 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1632 matches produced 5079 goals (avg 3.112 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.7% vs away 43.3% of 5079 goals in total (home/away ratio 1.31)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 953 of 1632 matches (58.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 549 scoring matches, 35.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.37, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Bodo/Glimt leads with 462 points across 7 seasons (4 title(s), GD 324)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 6 teams present in every one of the 7 seasons (Bodo/Glimt, Molde, Rosenborg, Sandefjord, Sarpsborg 08...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Rosenborg earns 82 more points at home than away (206 home vs 124 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Bodo/Glimt won 4 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025: Viking beat Bodo/Glimt by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.079 per match): first half 3.154 vs last half 3.075 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026 (goals view, avg abs position diff 5.375)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020 (luck view, avg abs position diff 2.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 168 matches (10.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (141 of 762 home matches, 18.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (168 of 365 draw matches, 46.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (115 of 505 away matches, 22.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 61 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.1526 (n=1440 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 8.708: home 3.381, draw -0.823, away -5.327
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1632 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1632 |
| Average goals per match | 3.112 |
| Home win rate | 46.7% |
| Draw rate | 22.4% |
| Away win rate | 30.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Bodo/Glimt |
| Champion with most titles | Bodo/Glimt |
| BTTS rate | 58.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.04 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 22.77 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.24 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 32.32 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.23 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 258.67 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.76 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 240 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 16 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 240 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 16 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 240 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 16 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 240 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 16 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 240 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 16 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 192 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 16 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021 draw outcome share 27.1% vs overall 22.4%
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022 goalless share 2.9% vs overall 4.7% (deviation 1.8 pp)
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023 home outcome share 50.8% vs overall 46.7%
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023 draw outcome share 17.5% vs overall 22.4%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024 home outcome share 41.7% vs overall 46.7%
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 3.1% vs overall 4.7% (deviation 1.6 pp)
- **22.** `HIGH_SCORING_MATCHES` *(warning)* — 21 match(es) with >= 8 total goals (extreme scorelines)
- **23.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **24.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=394, fgte=394 rows)
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=16 positions=1..16 teams=16
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=16 positions=1..16 teams=16
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=16 positions=1..16 teams=16
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=16 positions=1..16 teams=16
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=16 positions=1..16 teams=16
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=16 positions=1..16 teams=16
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=16 positions=1..16 teams=16
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=16 positions=1..16 teams=16
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=16 positions=1..16 teams=16
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=16 positions=1..16 teams=16
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=16 positions=1..16 teams=16
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=16 positions=1..16 teams=16
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
