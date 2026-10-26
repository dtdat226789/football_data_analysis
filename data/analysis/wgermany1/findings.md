# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:53:21+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Bundesliga Women (Germany)
- Scope: league `wgermany1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/wgermany1/database_profile.json | yes | yes | 49.90 |
| matches_analysis | data/analysis/wgermany1/matches_analysis.json | yes | yes | 16.73 |
| goals_analysis | data/analysis/wgermany1/goals_analysis.json | yes | yes | 12.54 |
| teams_analysis | data/analysis/wgermany1/teams_analysis.json | yes | yes | 29.83 |
| season_trends | data/analysis/wgermany1/season_trends.json | yes | yes | 10.56 |
| scoreline_analysis | data/analysis/wgermany1/scoreline_analysis.json | yes | yes | 163.81 |
| relationships | data/analysis/wgermany1/relationships.json | yes | yes | 13.73 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 893 matches: home wins 46.0%, draws 15.5%, away wins 38.5% (411H / 138D / 344A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 22 home and 24 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 287 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 893 matches produced 2989 goals (avg 3.347 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.3% vs away 45.7% of 2989 goals in total (home/away ratio 1.19)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 428 of 893 matches (47.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 329 scoring matches, 38.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 26.60, median 21.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Bayern Munich W leads with 392 points across 7 seasons (6 title(s), GD 390)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 7 teams present in every one of the 7 seasons (Bayer Leverkusen W, Bayern Munich W, Eintracht Frankfurt W, Freiburg W, Hoffenheim W...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Eintracht Frankfurt W earns 32 more points at home than away (162 home vs 130 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Bayern Munich W won 6 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: Bayern Munich W beat Wolfsburg W by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.071 per match): first half 3.414 vs last half 3.343 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023-2024 (goals view, avg abs position diff 4.500)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.286)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 65 matches (7.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (65 of 411 home matches, 15.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (61 of 138 draw matches, 44.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (57 of 344 away matches, 16.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 48 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.1372 (n=842 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 15.852: home 6.731, draw 0.000, away -9.121
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (42)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 893 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 893 |
| Average goals per match | 3.347 |
| Home win rate | 46.0% |
| Draw rate | 15.5% |
| Away win rate | 38.5% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | Bayern Munich W |
| Champion with most titles | Bayern Munich W |
| BTTS rate | 47.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.90 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 16.73 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.54 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 29.83 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.56 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 163.81 |
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
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 182 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 14 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 51 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 14 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 6.8% vs overall 5.2% (deviation 1.6 pp)
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 7.6% vs overall 5.2% (deviation 2.4 pp)
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 0.0% vs overall 5.2% (deviation 5.2 pp)
- **19.** `HIGH_SCORING_MATCHES` *(warning)* — 27 match(es) with >= 8 total goals (extreme scorelines)
- **20.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **21.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=511, fgte=511 rows)
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=12 positions=1..12 teams=12
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=12 positions=1..12 teams=12
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=12 positions=1..12 teams=12
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=12 positions=1..12 teams=12
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=12 positions=1..12 teams=12
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=12 positions=1..12 teams=12
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=12 positions=1..12 teams=12
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=12 positions=1..12 teams=12
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=12 positions=1..12 teams=12
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=12 positions=1..12 teams=12
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=12 positions=1..12 teams=12
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=12 positions=1..12 teams=12
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=12 positions=1..12 teams=12
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=12 positions=1..12 teams=12
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=12 positions=1..12 teams=12
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=14 positions=1..14 teams=14
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=14 positions=1..14 teams=14
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=14 positions=1..14 teams=14
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=14 positions=1..14 teams=14
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=14 positions=1..14 teams=14
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=14 positions=1..14 teams=14

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
