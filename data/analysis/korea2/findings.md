# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:00:47+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: K League 2 (South Korea)
- Scope: league `korea2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\korea2\database_profile.json | yes | yes | 31.14 |
| matches_analysis | E:\football_data_analysis\data\analysis\korea2\matches_analysis.json | yes | yes | 10.57 |
| goals_analysis | E:\football_data_analysis\data\analysis\korea2\goals_analysis.json | yes | yes | 6.21 |
| teams_analysis | E:\football_data_analysis\data\analysis\korea2\teams_analysis.json | yes | yes | 36.23 |
| season_trends | E:\football_data_analysis\data\analysis\korea2\season_trends.json | yes | yes | 3.90 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\korea2\scoreline_analysis.json | yes | yes | 74.64 |
| relationships | E:\football_data_analysis\data\analysis\korea2\relationships.json | yes | yes | 14.32 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 493 matches: home wins 35.1%, draws 31.0%, away wins 33.9% (173H / 153D / 167A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 11 home and 13 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — level at HT -> draw occurred 96 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 493 matches produced 1274 goals (avg 2.584 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.0% vs away 48.0% of 1274 goals in total (home/away ratio 1.08)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 269 of 493 matches (54.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 134 scoring matches, 29.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.81, median 30.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Suwon Bluewings leads with 128 points across 2 seasons (1 title(s), GD 47)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (Ansan Greeners, Asan, Busan, Cheonan City, Cheongju...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Asan earns 21 more points at home than away (54 home vs 33 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Incheon won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025: Incheon beat Suwon Bluewings by 7 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.160 per match): first half 2.513 vs last half 2.673 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025 (goals view, avg abs position diff 10.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026 (luck view, avg abs position diff 2.706)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 64 matches (13.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (41 of 173 home matches, 23.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (64 of 153 draw matches, 41.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (56 of 167 away matches, 33.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 6 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_points_last_5 |corr| = 0.1405 (n=273 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 9.368: home 4.698, draw -0.200, away -4.670
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 493 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 493 |
| Average goals per match | 2.584 |
| Home win rate | 35.1% |
| Draw rate | 31.0% |
| Away win rate | 33.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Suwon Bluewings |
| Champion with most titles | Incheon |
| BTTS rate | 54.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.14 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 10.57 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.21 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 36.23 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.90 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 74.64 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.32 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 273 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 28 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 220 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 17 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=28 positions=1..28 teams=28
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=28 positions=1..28 teams=28
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=28 positions=1..28 teams=28
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=17 positions=1..17 teams=17
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=17 positions=1..17 teams=17
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=17 positions=1..17 teams=17

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
