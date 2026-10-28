# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:59:36+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: J2 League (Japan)
- Scope: league `japan2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/japan2/database_profile.json | yes | yes | 41.76 |
| matches_analysis | data/analysis/japan2/matches_analysis.json | yes | yes | 27.24 |
| goals_analysis | data/analysis/japan2/goals_analysis.json | yes | yes | 11.04 |
| teams_analysis | data/analysis/japan2/teams_analysis.json | yes | yes | 46.97 |
| season_trends | data/analysis/japan2/season_trends.json | yes | yes | 8.97 |
| scoreline_analysis | data/analysis/japan2/scoreline_analysis.json | yes | yes | 370.39 |
| relationships | data/analysis/japan2/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2608 matches: home wins 38.1%, draws 27.6%, away wins 34.2% (994H / 721D / 893A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 48 home and 64 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 577 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2608 matches produced 6416 goals (avg 2.460 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.6% vs away 47.4% of 6416 goals in total (home/away ratio 1.11)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1302 of 2608 matches (49.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 710 scoring matches, 30.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.05, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — V-Varen Nagasaki leads with 424 points across 6 seasons (0 title(s), GD 116)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 6 teams present in every one of the 6 seasons (Chiba, Kofu, Mito, Montedio Yamagata, Renofa Yamaguchi...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Renofa Yamaguchi earns 51 more points at home than away (155 home vs 104 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Tokushima won 1 of 6 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020: Tokushima beat Avispa Fukuoka by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.078 per match): first half 2.422 vs last half 2.5 across 6 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2020 (goals view, avg abs position diff 7.909)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 1.400)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 319 matches (12.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (294 of 994 home matches, 29.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (319 of 721 draw matches, 44.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (290 of 893 away matches, 32.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 35 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.04 (n=2608 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.088: home 3.059, draw -0.494, away -3.029
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (24)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 6 of 6 registered seasons populated (100.0%); 2608 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2608 |
| Average goals per match | 2.46 |
| Home win rate | 38.1% |
| Draw rate | 27.6% |
| Away win rate | 34.2% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | V-Varen Nagasaki |
| Champion with most titles | Tokushima |
| BTTS rate | 49.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 41.76 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 27.24 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 11.04 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 46.97 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 8.97 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 370.39 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 462 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 22 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 462 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 22 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 462 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 22 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 462 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 22 teams, expected 20
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024 draw outcome share 23.4% vs overall 27.6%
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 8 match(es) with >= 8 total goals (extreme scorelines)
- **11.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **12.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=366, fgte=366 rows)
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=22 positions=1..22 teams=22
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=22 positions=1..22 teams=22
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=22 positions=1..22 teams=22
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=22 positions=1..22 teams=22
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=22 positions=1..22 teams=22
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=22 positions=1..22 teams=22
- **19.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=22 positions=1..22 teams=22
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=22 positions=1..22 teams=22
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=22 positions=1..22 teams=22
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=22 positions=1..22 teams=22
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=22 positions=1..22 teams=22
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=22 positions=1..22 teams=22

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
