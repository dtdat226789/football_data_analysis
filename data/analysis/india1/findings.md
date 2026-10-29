# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:03:59+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: ISL (India)
- Scope: league `india1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/india1/database_profile.json | yes | yes | 52.01 |
| matches_analysis | data/analysis/india1/matches_analysis.json | yes | yes | 16.64 |
| goals_analysis | data/analysis/india1/goals_analysis.json | yes | yes | 12.41 |
| teams_analysis | data/analysis/india1/teams_analysis.json | yes | yes | 25.22 |
| season_trends | data/analysis/india1/season_trends.json | yes | yes | 10.40 |
| scoreline_analysis | data/analysis/india1/scoreline_analysis.json | yes | yes | 115.01 |
| relationships | data/analysis/india1/relationships.json | yes | yes | 13.67 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 726 matches: home wins 40.8%, draws 26.6%, away wins 32.6% (296H / 193D / 237A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 25 home and 22 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 158 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 726 matches produced 2042 goals (avg 2.813 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.1% vs away 47.9% of 2042 goals in total (home/away ratio 1.09)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 405 of 726 matches (55.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 244 scoring matches, 36.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.96, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Mohun Bagan leads with 247 points across 7 seasons (2 title(s), GD 98)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 7 seasons (Bengaluru FC, Chennaiyin, East Bengal, Goa, Kerala Blasters...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Kerala Blasters earns 43 more points at home than away (104 home vs 61 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Mumbai City won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: Mumbai City beat Mohun Bagan by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.252 per match): first half 2.921 vs last half 2.669 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.714)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2023-2024 (luck view, avg abs position diff 0.833)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 90 matches (12.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (70 of 296 home matches, 23.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (90 of 193 draw matches, 46.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (51 of 237 away matches, 21.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 16 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_conceded_last_5 |corr| = 0.085 (n=709 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.849: home 2.685, draw -1.165, away -3.164
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (52)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 726 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 726 |
| Average goals per match | 2.813 |
| Home win rate | 40.8% |
| Draw rate | 26.6% |
| Away win rate | 32.6% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Mohun Bagan |
| Champion with most titles | Mumbai City |
| BTTS rate | 55.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 52.01 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 16.64 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.41 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 25.22 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.40 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 115.01 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.67 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 110 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 11 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 110 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 11 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 110 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 11 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 132 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 12 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 156 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 13 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 91 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 14 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 17 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 13 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 11.8% vs overall 7.3% (deviation 4.5 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 29.1% vs overall 40.8%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 38.2% vs overall 26.6%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 4.5% vs overall 7.3% (deviation 2.8 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 2.7% vs overall 7.3% (deviation 4.6 pp)
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 home outcome share 47.3% vs overall 40.8%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 draw outcome share 14.5% vs overall 26.6%
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 away outcome share 38.2% vs overall 32.6%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 home outcome share 45.5% vs overall 40.8%
- **25.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2025-2026 avg goals 2.429 vs overall 2.813 (deviation 0.384)
- **26.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 11.0% vs overall 7.3% (deviation 3.7 pp)
- **27.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 draw outcome share 31.9% vs overall 26.6%
- **28.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 11.8% vs overall 7.3% (deviation 4.5 pp)
- **29.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **30.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **31.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=345, fgte=345 rows)
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=11 positions=1..11 teams=11
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=11 positions=1..11 teams=11
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=11 positions=1..11 teams=11
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=11 positions=1..11 teams=11
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=11 positions=1..11 teams=11
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=11 positions=1..11 teams=11
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=11 positions=1..11 teams=11
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=11 positions=1..11 teams=11
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=11 positions=1..11 teams=11
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=12 positions=1..12 teams=12
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=12 positions=1..12 teams=12
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=12 positions=1..12 teams=12
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=13 positions=1..13 teams=13
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=13 positions=1..13 teams=13
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=13 positions=1..13 teams=13
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=14 positions=1..14 teams=14
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=14 positions=1..14 teams=14
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=14 positions=1..14 teams=14
- **50.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=13 positions=1..13 teams=13
- **51.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=13 positions=1..13 teams=13
- **52.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=13 positions=1..13 teams=13

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
