# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T02:32:38+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Allsvenskan (Sweden)
- Scope: league `sweden1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/sweden1/database_profile.json | yes | yes | 50.21 |
| matches_analysis | data/analysis/sweden1/matches_analysis.json | yes | yes | 21.83 |
| goals_analysis | data/analysis/sweden1/goals_analysis.json | yes | yes | 12.33 |
| teams_analysis | data/analysis/sweden1/teams_analysis.json | yes | yes | 34.56 |
| season_trends | data/analysis/sweden1/season_trends.json | yes | yes | 10.23 |
| scoreline_analysis | data/analysis/sweden1/scoreline_analysis.json | yes | yes | 251.51 |
| relationships | data/analysis/sweden1/relationships.json | yes | yes | 13.77 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1640 matches: home wins 42.7%, draws 24.1%, away wins 33.2% (700H / 395D / 545A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 44 home and 36 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 425 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1640 matches produced 4586 goals (avg 2.796 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.8% vs away 45.2% of 4586 goals in total (home/away ratio 1.21)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 865 of 1640 matches (52.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 519 scoring matches, 33.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.79, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Malmo FF leads with 380 points across 7 seasons (4 title(s), GD 166)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 7 seasons (AIK, Djurgarden, Elfsborg, Goteborg, Hacken...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Hammarby earns 69 more points at home than away (214 home vs 145 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Malmo FF won 4 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2021: Malmo FF beat AIK by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.125 per match): first half 2.741 vs last half 2.866 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025 (goals view, avg abs position diff 7.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 2.750)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 187 matches (11.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (133 of 700 home matches, 19.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (187 of 395 draw matches, 47.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (141 of 545 away matches, 25.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 44 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1128 (n=1440 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.31: home 2.363, draw 0.135, away -3.947
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (46)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1640 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1640 |
| Average goals per match | 2.796 |
| Home win rate | 42.7% |
| Draw rate | 24.1% |
| Away win rate | 33.2% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Malmo FF |
| Champion with most titles | Malmo FF |
| BTTS rate | 52.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.21 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 21.83 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.33 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 34.56 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.23 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 251.51 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.77 |

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
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 200 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 16 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 home outcome share 37.1% vs overall 42.7%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 draw outcome share 32.1% vs overall 24.1%
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021 goalless share 7.9% vs overall 6.2% (deviation 1.7 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023 draw outcome share 19.6% vs overall 24.1%
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024 goalless share 4.6% vs overall 6.2% (deviation 1.6 pp)
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025 away outcome share 37.9% vs overall 33.2%
- **22.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 4.0% vs overall 6.2% (deviation 2.2 pp)
- **23.** `HIGH_SCORING_MATCHES` *(warning)* — 11 match(es) with >= 8 total goals (extreme scorelines)
- **24.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **25.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=440, fgte=440 rows)
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=16 positions=1..16 teams=16
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=16 positions=1..16 teams=16
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=16 positions=1..16 teams=16
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=16 positions=1..16 teams=16
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=16 positions=1..16 teams=16
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=16 positions=1..16 teams=16
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=16 positions=1..16 teams=16
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=16 positions=1..16 teams=16
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=16 positions=1..16 teams=16
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=16 positions=1..16 teams=16
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=16 positions=1..16 teams=16
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=16 positions=1..16 teams=16
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
