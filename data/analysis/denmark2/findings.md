# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:57:15+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 1st Division (Denmark)
- Scope: league `denmark2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\denmark2\database_profile.json | yes | yes | 24.13 |
| matches_analysis | E:\football_data_analysis\data\analysis\denmark2\matches_analysis.json | yes | yes | 5.13 |
| goals_analysis | E:\football_data_analysis\data\analysis\denmark2\goals_analysis.json | yes | yes | 2.84 |
| teams_analysis | E:\football_data_analysis\data\analysis\denmark2\teams_analysis.json | yes | yes | 1.01 |
| season_trends | E:\football_data_analysis\data\analysis\denmark2\season_trends.json | yes | yes | 0.90 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\denmark2\scoreline_analysis.json | yes | yes | 3.87 |
| relationships | E:\football_data_analysis\data\analysis\denmark2\relationships.json | yes | yes | 12.14 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 0 matches: home wins -%, draws -%, away wins -% (0H / 0D / 0A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 0 home and 0 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 0 times
- **F4** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 0 scoring matches, -% of scoring)
- **F5** · `teams_analysis` · *[medium]* — **Team consistency** — 0 teams present in every one of the 0 seasons
- **F6** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 0 match(es) with >= 7 total goals
- **F7** · `database_profile` · *[high]* — **Data-quality warnings (8)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, MATCH_COUNT_UNEXPECTED, SEASON_REGISTERED_NO_DATA, TEAM_COUNT_UNEXPECTED
- **F8** · `database_profile` · *[medium]* — **Data coverage** — 0 of 2 registered seasons populated (0.0%); 0 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 0 |
| Average goals per match | - |
| Home win rate | -% |
| Draw rate | -% |
| Away win rate | -% |
| Most common scoreline | - |
| Dominant team (lifetime points) | - |
| Champion with most titles | - |
| BTTS rate | -% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 24.13 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 5.13 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 2.84 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 1.01 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 0.90 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 3.87 |
| relationships | relationships | n_matches, feature_count, data_warning, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 12.14 |

## 5. Notable anomalies
- **1.** `SEASON_REGISTERED_NO_DATA` *(warning)* — Season 2025-2026 is registered but has no match data (declared_by_api=True, state=complete)
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 0 matches, expected 380
- **3.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 11 teams, expected 20
- **4.** `SEASON_REGISTERED_NO_DATA` *(warning)* — Season 2026-2027 is registered but has no match data (declared_by_api=True, state=in_progress)
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 0 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
