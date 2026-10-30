# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:52:06+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/france3/database_profile.json | yes | yes | 50.14 |
| matches_analysis | data/analysis/france3/matches_analysis.json | yes | yes | 21.12 |
| goals_analysis | data/analysis/france3/goals_analysis.json | yes | yes | 12.34 |
| teams_analysis | data/analysis/france3/teams_analysis.json | yes | yes | 108.38 |
| season_trends | data/analysis/france3/season_trends.json | yes | yes | 10.44 |
| scoreline_analysis | data/analysis/france3/scoreline_analysis.json | yes | yes | 269.21 |
| relationships | data/analysis/france3/relationships.json | yes | yes | 13.75 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1902 matches: home wins 40.6%, draws 30.7%, away wins 28.8% (772H / 583D / 547A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 42 home and 31 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 478 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1902 matches produced 4638 goals (avg 2.438 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.8% vs away 45.2% of 4638 goals in total (home/away ratio 1.21)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 972 of 1902 matches (51.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 525 scoring matches, 30.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.38, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Orleans leads with 288 points across 7 seasons (0 title(s), GD 7)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 2 teams present in every one of the 7 seasons (Orleans, Villefranche)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Villefranche earns 44 more points at home than away (164 home vs 120 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Bastia won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2021-2022: Laval beat Annecy by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.018 per match): first half 2.414 vs last half 2.432 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 17.800)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.474)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 280 matches (14.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (212 of 772 home matches, 27.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (280 of 583 draw matches, 48.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (159 of 547 away matches, 29.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 28 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_conceded_last_5 |corr| = 0.0653 (n=1799 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 3.143: home 1.545, draw -0.233, away -1.599
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (46)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1902 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1902 |
| Average goals per match | 2.438 |
| Home win rate | 40.6% |
| Draw rate | 30.7% |
| Away win rate | 28.8% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Orleans |
| Champion with most titles | Bastia |
| BTTS rate | 51.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.14 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 21.12 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 108.38 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.44 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 269.21 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.75 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 36 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 306 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 18 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 306 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 18 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 272 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 17 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 303 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 50 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 103 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 19 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 14.7% vs overall 10.0% (deviation 4.7 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 36.3% vs overall 30.7%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 draw outcome share 26.1% vs overall 30.7%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 7.2% vs overall 10.0% (deviation 2.8 pp)
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 home outcome share 45.1% vs overall 40.6%
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 draw outcome share 26.5% vs overall 30.7%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 home outcome share 36.0% vs overall 40.6%
- **23.** `HIGH_SCORING_MATCHES` *(warning)* — 7 match(es) with >= 8 total goals (extreme scorelines)
- **24.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **25.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=323, fgte=323 rows)
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=36 positions=1..36 teams=36
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=36 positions=1..36 teams=36
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=36 positions=1..36 teams=36
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=18 positions=1..18 teams=18
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=18 positions=1..18 teams=18
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=18 positions=1..18 teams=18
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=18 positions=1..18 teams=18
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=18 positions=1..18 teams=18
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=18 positions=1..18 teams=18
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..18 teams=18
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..18 teams=18
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..18 teams=18
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=17 positions=1..17 teams=17
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=17 positions=1..17 teams=17
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=17 positions=1..17 teams=17
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=50 positions=1..50 teams=50
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=50 positions=1..50 teams=50
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=50 positions=1..50 teams=50
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=19 positions=1..19 teams=19
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=19 positions=1..19 teams=19
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=19 positions=1..19 teams=19

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
