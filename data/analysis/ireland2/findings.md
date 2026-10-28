# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:55:30+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Division 1 (Ireland)
- Scope: league `ireland2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/ireland2/database_profile.json | yes | yes | 50.55 |
| matches_analysis | data/analysis/ireland2/matches_analysis.json | yes | yes | 18.62 |
| goals_analysis | data/analysis/ireland2/goals_analysis.json | yes | yes | 12.22 |
| teams_analysis | data/analysis/ireland2/teams_analysis.json | yes | yes | 25.86 |
| season_trends | data/analysis/ireland2/season_trends.json | yes | yes | 10.18 |
| scoreline_analysis | data/analysis/ireland2/scoreline_analysis.json | yes | yes | 168.93 |
| relationships | data/analysis/ireland2/relationships.json | yes | yes | 13.70 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1086 matches: home wins 42.0%, draws 24.2%, away wins 33.8% (456H / 263D / 367A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 30 home and 31 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 275 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1086 matches produced 3082 goals (avg 2.838 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.2% vs away 46.8% of 3082 goals in total (home/away ratio 1.14)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 575 of 1086 matches (52.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 352 scoring matches, 34.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.08, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Bray leads with 313 points across 7 seasons (0 title(s), GD 7)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 4 teams present in every one of the 7 seasons (Athlone, Bray, Cobh Ramblers, Wexford)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Bray earns 43 more points at home than away (178 home vs 135 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Cork City won 3 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020: Drogheda beat Bray by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.130 per match): first half 2.874 vs last half 2.744 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021 (goals view, avg abs position diff 4.200)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2024 (luck view, avg abs position diff 1.200)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 110 matches (10.1%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (96 of 456 home matches, 21.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (110 of 263 draw matches, 41.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (90 of 367 away matches, 24.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 27 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.0593 (n=906 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 10.731: home 5.131, draw -0.548, away -5.601
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (50)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1086 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1086 |
| Average goals per match | 2.838 |
| Home win rate | 42.0% |
| Draw rate | 24.2% |
| Away win rate | 33.8% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Bray |
| Champion with most titles | Cork City |
| BTTS rate | 52.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.55 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 18.62 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.22 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 25.86 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.18 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 168.93 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.70 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 88 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 135 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 10 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 144 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 9 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 180 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 10 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 180 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 10 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 179 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 10 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 180 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 home outcome share 35.2% vs overall 42.0%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 draw outcome share 17.0% vs overall 24.2%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 away outcome share 47.7% vs overall 33.8%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021 goalless share 9.6% vs overall 6.3% (deviation 3.3 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022 goalless share 8.3% vs overall 6.3% (deviation 2.0 pp)
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022 home outcome share 36.8% vs overall 42.0%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022 away outcome share 38.9% vs overall 33.8%
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024 draw outcome share 30.0% vs overall 24.2%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024 away outcome share 29.4% vs overall 33.8%
- **25.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 home outcome share 49.4% vs overall 42.0%
- **26.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 away outcome share 27.2% vs overall 33.8%
- **27.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **28.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **29.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=348, fgte=348 rows)
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=10 positions=1..10 teams=10
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=10 positions=1..10 teams=10
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=10 positions=1..10 teams=10
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=10 positions=1..10 teams=10
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=10 positions=1..10 teams=10
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=10 positions=1..10 teams=10
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=9 positions=1..9 teams=9
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=9 positions=1..9 teams=9
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=9 positions=1..9 teams=9
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=10 positions=1..10 teams=10
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=10 positions=1..10 teams=10
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=10 positions=1..10 teams=10
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=10 positions=1..10 teams=10
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=10 positions=1..10 teams=10
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=10 positions=1..10 teams=10
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=10 positions=1..10 teams=10
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=10 positions=1..10 teams=10
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=10 positions=1..10 teams=10
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **50.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
