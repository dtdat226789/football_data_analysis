# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T02:34:32+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 1. Lig (Turkey)
- Scope: league `turkey2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/turkey2/database_profile.json | yes | yes | 46.36 |
| matches_analysis | data/analysis/turkey2/matches_analysis.json | yes | yes | 26.88 |
| goals_analysis | data/analysis/turkey2/goals_analysis.json | yes | yes | 12.50 |
| teams_analysis | data/analysis/turkey2/teams_analysis.json | yes | yes | 57.87 |
| season_trends | data/analysis/turkey2/season_trends.json | yes | yes | 10.51 |
| scoreline_analysis | data/analysis/turkey2/scoreline_analysis.json | yes | yes | 339.89 |
| relationships | data/analysis/turkey2/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2179 matches: home wins 44.1%, draws 23.9%, away wins 32.0% (962H / 520D / 697A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 59 home and 44 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 539 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2179 matches produced 5858 goals (avg 2.688 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.8% vs away 45.2% of 5858 goals in total (home/away ratio 1.21)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1066 of 2179 matches (48.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 610 scoring matches, 30.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.96, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Bandirmaspor leads with 347 points across 7 seasons (0 title(s), GD 60)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 3 teams present in every one of the 7 seasons (Bandirmaspor, Boluspor, Keciorengucu)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Bandirmaspor earns 63 more points at home than away (205 home vs 142 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Adana Demirspor won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: Adana Demirspor beat Giresunspor by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.074 per match): first half 2.703 vs last half 2.777 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 8.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020-2021 (luck view, avg abs position diff 1.889)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 257 matches (11.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (209 of 962 home matches, 21.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (257 of 520 draw matches, 49.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (177 of 697 away matches, 25.4%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 55 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_conceded_last_5 |corr| = 0.1405 (n=2060 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 9.866: home 3.969, draw -0.752, away -5.898
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (31)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2179 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2179 |
| Average goals per match | 2.688 |
| Home win rate | 44.1% |
| Draw rate | 23.9% |
| Away win rate | 32.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Bandirmaspor |
| Champion with most titles | Adana Demirspor |
| BTTS rate | 48.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 46.36 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 26.88 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.50 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 57.87 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.51 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 339.89 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 342 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 19 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 341 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 19 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 385 matches, expected 380
- **10.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 119 matches, expected 380
- **11.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **12.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 home outcome share 48.8% vs overall 44.1%
- **13.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 9.2% vs overall 7.4% (deviation 1.8 pp)
- **14.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 33.6% vs overall 44.1%
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 30.3% vs overall 23.9%
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 36.1% vs overall 32.0%
- **17.** `HIGH_SCORING_MATCHES` *(warning)* — 15 match(es) with >= 8 total goals (extreme scorelines)
- **18.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **19.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=506, fgte=506 rows)
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=18 positions=1..18 teams=18
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=18 positions=1..18 teams=18
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=18 positions=1..18 teams=18
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=19 positions=1..19 teams=19
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=19 positions=1..19 teams=19
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=19 positions=1..19 teams=19
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=19 positions=1..19 teams=19
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=19 positions=1..19 teams=19
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=19 positions=1..19 teams=19
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..18 teams=18
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..18 teams=18
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
