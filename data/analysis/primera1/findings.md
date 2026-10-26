# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:44:09+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Primera RFEF - Group 1 (Spain)
- Scope: league `primera1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/primera1/database_profile.json | yes | yes | 39.75 |
| matches_analysis | data/analysis/primera1/matches_analysis.json | yes | yes | 22.50 |
| goals_analysis | data/analysis/primera1/goals_analysis.json | yes | yes | 11.11 |
| teams_analysis | data/analysis/primera1/teams_analysis.json | yes | yes | 69.59 |
| season_trends | data/analysis/primera1/season_trends.json | yes | yes | 9.18 |
| scoreline_analysis | data/analysis/primera1/scoreline_analysis.json | yes | yes | 291.04 |
| relationships | data/analysis/primera1/relationships.json | yes | yes | 13.79 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2007 matches: home wins 44.8%, draws 28.2%, away wins 27.0% (900H / 565D / 542A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 43 home and 38 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 513 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2007 matches produced 4720 goals (avg 2.352 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.0% vs away 43.0% of 4720 goals in total (home/away ratio 1.32)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 965 of 2007 matches (48.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 525 scoring matches, 29.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.19, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Celta Vigo B leads with 306 points across 5 seasons (0 title(s), GD 72)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 1 teams present in every one of the 6 seasons (Unionistas)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Unionistas earns 92 more points at home than away (191 home vs 99 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Racing Santander won 1 of 6 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2024-2025: Ponferradina beat Cultural Leonesa by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.234 per match): first half 2.267 vs last half 2.5 across 6 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 7.600)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.600)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 282 matches (14.1%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (275 of 900 home matches, 30.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (282 of 565 draw matches, 49.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (167 of 542 away matches, 30.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 20 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.1207 (n=1918 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.168: home 1.457, draw -0.670, away -2.710
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 6 of 6 registered seasons populated (100.0%); 2007 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2007 |
| Average goals per match | 2.352 |
| Home win rate | 44.8% |
| Draw rate | 28.2% |
| Away win rate | 27.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Celta Vigo B |
| Champion with most titles | Racing Santander |
| BTTS rate | 48.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 39.75 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 22.50 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 11.11 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 69.59 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 9.18 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 291.04 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.79 |

## 5. Notable anomalies
- **1.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 21 teams, expected 20
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 398 matches, expected 380
- **3.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 21 teams, expected 20
- **4.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 89 matches, expected 380
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 13.2% vs overall 9.2% (deviation 4.0 pp)
- **7.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 6.6% vs overall 9.2% (deviation 2.6 pp)
- **8.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 5.6% vs overall 9.2% (deviation 3.6 pp)
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=413, fgte=413 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=21 positions=1..21 teams=21
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=21 positions=1..21 teams=21
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=21 positions=1..21 teams=21
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=21 positions=1..21 teams=21
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=21 positions=1..21 teams=21
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=21 positions=1..21 teams=21

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
