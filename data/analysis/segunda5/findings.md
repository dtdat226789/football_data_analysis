# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:15:29+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Segunda RFEF - Group 5 (Spain)
- Scope: league `segunda5`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/segunda5/database_profile.json | yes | yes | 49.58 |
| matches_analysis | data/analysis/segunda5/matches_analysis.json | yes | yes | 21.67 |
| goals_analysis | data/analysis/segunda5/goals_analysis.json | yes | yes | 12.29 |
| teams_analysis | data/analysis/segunda5/teams_analysis.json | yes | yes | 85.13 |
| season_trends | data/analysis/segunda5/season_trends.json | yes | yes | 10.58 |
| scoreline_analysis | data/analysis/segunda5/scoreline_analysis.json | yes | yes | 258.33 |
| relationships | data/analysis/segunda5/relationships.json | yes | yes | 13.79 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1789 matches: home wins 43.2%, draws 29.0%, away wins 27.9% (772H / 518D / 499A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 35 home and 39 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 439 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1789 matches produced 4108 goals (avg 2.296 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.0% vs away 43.0% of 4108 goals in total (home/away ratio 1.33)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 795 of 1789 matches (44.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 454 scoring matches, 28.9% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.11, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Navalcarnero leads with 236 points across 6 seasons (0 title(s), GD 16)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 0 teams present in every one of the 7 seasons
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Atl. Paso earns 61 more points at home than away (94 home vs 33 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — San Sebastian Reyes won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2023-2024: San Sebastian Reyes beat Gimnastica Segoviana by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.482 per match): first half 2.108 vs last half 2.59 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 6.667)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2024-2025 (luck view, avg abs position diff 1.667)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 223 matches (12.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (223 of 772 home matches, 28.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 0-0 (219 of 518 draw matches, 42.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (165 of 499 away matches, 33.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 19 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_conceded_last_5 |corr| = 0.0837 (n=1710 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.511: home 1.711, draw -0.557, away -2.800
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1789 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1789 |
| Average goals per match | 2.296 |
| Home win rate | 43.2% |
| Draw rate | 29.0% |
| Away win rate | 27.9% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Navalcarnero |
| Champion with most titles | San Sebastian Reyes |
| BTTS rate | 44.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.58 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 21.67 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.29 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 85.13 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.58 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 258.33 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.79 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 180 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 306 matches, expected 380
- **3.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 18 teams, expected 20
- **4.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 306 matches, expected 380
- **5.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 19 teams, expected 20
- **6.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **7.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **8.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 306 matches, expected 380
- **9.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 18 teams, expected 20
- **10.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 306 matches, expected 380
- **11.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **12.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 79 matches, expected 380
- **13.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **14.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **15.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 15.6% vs overall 12.2% (deviation 3.4 pp)
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 38.9% vs overall 43.2%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 33.9% vs overall 29.0%
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 16.7% vs overall 12.2% (deviation 4.5 pp)
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 9.5% vs overall 12.2% (deviation 2.7 pp)
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 home outcome share 47.7% vs overall 43.2%
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 8.8% vs overall 12.2% (deviation 3.4 pp)
- **22.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 2.747 vs overall 2.296 (deviation 0.451)
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 48.1% vs overall 43.2%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 19.0% vs overall 27.9%
- **25.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **26.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (31 extra rows)
- **27.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=430, fgte=430 rows)
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=18 positions=1..18 teams=18
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=18 positions=1..18 teams=18
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=18 positions=1..18 teams=18
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=19 positions=1..19 teams=19
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=19 positions=1..19 teams=19
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=19 positions=1..19 teams=19
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..18 teams=18
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..18 teams=18
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..18 teams=18
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=18 positions=1..18 teams=18
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=18 positions=1..18 teams=18
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=18 positions=1..18 teams=18
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
