# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:47:45+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: ChNL (Czech Republic)
- Scope: league `czech2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/czech2/database_profile.json | yes | yes | 50.89 |
| matches_analysis | data/analysis/czech2/matches_analysis.json | yes | yes | 20.15 |
| goals_analysis | data/analysis/czech2/goals_analysis.json | yes | yes | 12.34 |
| teams_analysis | data/analysis/czech2/teams_analysis.json | yes | yes | 37.37 |
| season_trends | data/analysis/czech2/season_trends.json | yes | yes | 10.46 |
| scoreline_analysis | data/analysis/czech2/scoreline_analysis.json | yes | yes | 225.65 |
| relationships | data/analysis/czech2/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1478 matches: home wins 44.2%, draws 26.4%, away wins 29.4% (653H / 390D / 435A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 46 home and 21 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 389 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1478 matches produced 4022 goals (avg 2.721 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.4% vs away 43.6% of 4022 goals in total (home/away ratio 1.29)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 801 of 1478 matches (54.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 446 scoring matches, 32.4% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.22, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Artis Brno leads with 276 points across 6 seasons (0 title(s), GD 51)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 4 teams present in every one of the 7 seasons (Jihlava, Prostejov, Taborsko, Vlasim)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Vlasim earns 62 more points at home than away (163 home vs 101 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Brno won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2023-2024: Dukla Prague beat Sigma Olomouc B by 3 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.069 per match): first half 2.695 vs last half 2.765 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023-2024 (goals view, avg abs position diff 6.750)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2021-2022 (luck view, avg abs position diff 1.875)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 174 matches (11.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (155 of 653 home matches, 23.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (174 of 390 draw matches, 44.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (117 of 435 away matches, 26.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 34 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_position_before_match |corr| = 0.0587 (n=1382 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 3.385: home 1.324, draw -0.914, away -2.061
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (48)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1478 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1478 |
| Average goals per match | 2.721 |
| Home win rate | 44.2% |
| Draw rate | 26.4% |
| Away win rate | 29.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Artis Brno |
| Champion with most titles | Brno |
| BTTS rate | 54.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 50.89 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 20.15 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 37.37 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.46 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 225.65 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 182 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 14 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 240 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 16 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 240 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 16 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 240 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 16 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 240 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 16 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 240 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 96 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 37.4% vs overall 44.2%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 36.8% vs overall 29.4%
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 9.6% vs overall 6.9% (deviation 2.7 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 draw outcome share 31.2% vs overall 26.4%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 draw outcome share 20.8% vs overall 26.4%
- **21.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.094 vs overall 2.721 (deviation 0.373)
- **22.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.2% vs overall 6.9% (deviation 2.7 pp)
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 39.6% vs overall 44.2%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 32.3% vs overall 26.4%
- **25.** `HIGH_SCORING_MATCHES` *(warning)* — 14 match(es) with >= 8 total goals (extreme scorelines)
- **26.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **27.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=306, fgte=306 rows)
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=14 positions=1..14 teams=14
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=14 positions=1..14 teams=14
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=14 positions=1..14 teams=14
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=16 positions=1..16 teams=16
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=16 positions=1..16 teams=16
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=16 positions=1..16 teams=16
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=16 positions=1..16 teams=16
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=16 positions=1..16 teams=16
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=16 positions=1..16 teams=16
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=16 positions=1..16 teams=16
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
