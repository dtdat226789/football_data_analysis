# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:31:20+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: League Two (England)
- Scope: league `eng2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/eng2/database_profile.json | yes | yes | 50.95 |
| matches_analysis | data/analysis/eng2/matches_analysis.json | yes | yes | 37.21 |
| goals_analysis | data/analysis/eng2/goals_analysis.json | yes | yes | 12.53 |
| teams_analysis | data/analysis/eng2/teams_analysis.json | yes | yes | 56.58 |
| season_trends | data/analysis/eng2/season_trends.json | yes | yes | 10.48 |
| scoreline_analysis | data/analysis/eng2/scoreline_analysis.json | yes | yes | 507.89 |
| relationships | data/analysis/eng2/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 3466 matches: home wins 42.3%, draws 27.2%, away wins 30.5% (1466H / 943D / 1057A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 89 home and 74 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 857 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 3466 matches produced 8797 goals (avg 2.538 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.6% vs away 45.4% of 8797 goals in total (home/away ratio 1.20)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1774 of 3466 matches (51.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 1029 scoring matches, 32.4% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.51, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Salford leads with 446 points across 7 seasons (1 title(s), GD 61)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 7 seasons (Colchester, Newport, Salford, Tranmere, Walsall)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Tranmere earns 77 more points at home than away (224 home vs 147 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Cheltenham won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2021-2022: Forest Green beat Exeter by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.162 per match): first half 2.389 vs last half 2.551 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022-2023 (goals view, avg abs position diff 9.250)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2021-2022 (luck view, avg abs position diff 2.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 443 matches (12.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (394 of 1466 home matches, 26.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (443 of 943 draw matches, 47.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (296 of 1057 away matches, 28.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 60 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_scored_last_5 |corr| = 0.0677 (n=3317 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.502: home 1.979, draw -0.742, away -2.523
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (46)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 3466 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 3466 |
| Average goals per match | 2.538 |
| Home win rate | 42.3% |
| Draw rate | 27.2% |
| Away win rate | 30.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Salford |
| Champion with most titles | Cheltenham |
| BTTS rate | 51.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.95 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 37.21 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.53 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 56.58 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.48 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 507.89 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

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
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 557 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 24 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 149 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 10.3% vs overall 8.3% (deviation 2.0 pp)
- **17.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2023-2024 avg goals 2.98 vs overall 2.538 (deviation 0.442)
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 4.9% vs overall 8.3% (deviation 3.4 pp)
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 6.6% vs overall 8.3% (deviation 1.7 pp)
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 47.0% vs overall 42.3%
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 34.9% vs overall 27.2%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 18.1% vs overall 30.5%
- **23.** `HIGH_SCORING_MATCHES` *(warning)* — 26 match(es) with >= 8 total goals (extreme scorelines)
- **24.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **25.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=312, fgte=312 rows)
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=24 positions=1..24 teams=24
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=24 positions=1..24 teams=24
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=24 positions=1..24 teams=24
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=24 positions=1..24 teams=24
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=24 positions=1..24 teams=24
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=24 positions=1..24 teams=24
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=24 positions=1..24 teams=24
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=24 positions=1..24 teams=24
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=24 positions=1..24 teams=24
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=24 positions=1..24 teams=24
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=24 positions=1..24 teams=24
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=24 positions=1..24 teams=24
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=24 positions=1..24 teams=24
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=24 positions=1..24 teams=24
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=24 positions=1..24 teams=24
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=24 positions=1..24 teams=24
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=24 positions=1..24 teams=24
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=24 positions=1..24 teams=24
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=24 positions=1..24 teams=24
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=24 positions=1..24 teams=24
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=24 positions=1..24 teams=24

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
