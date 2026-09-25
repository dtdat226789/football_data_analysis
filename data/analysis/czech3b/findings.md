# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:56:53+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 3. CFL - Group B (Czech Republic)
- Scope: league `czech3b`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\czech3b\database_profile.json | yes | yes | 33.57 |
| matches_analysis | E:\football_data_analysis\data\analysis\czech3b\matches_analysis.json | yes | yes | 8.44 |
| goals_analysis | E:\football_data_analysis\data\analysis\czech3b\goals_analysis.json | yes | yes | 6.50 |
| teams_analysis | E:\football_data_analysis\data\analysis\czech3b\teams_analysis.json | yes | yes | 29.49 |
| season_trends | E:\football_data_analysis\data\analysis\czech3b\season_trends.json | yes | yes | 3.95 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\czech3b\scoreline_analysis.json | yes | yes | 60.71 |
| relationships | E:\football_data_analysis\data\analysis\czech3b\relationships.json | yes | yes | 14.37 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 326 matches: home wins 42.9%, draws 23.3%, away wins 33.7% (140H / 76D / 110A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 4 home and 8 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 103 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 326 matches produced 1079 goals (avg 3.310 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.5% vs away 45.5% of 1079 goals in total (home/away ratio 1.20)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 186 of 326 matches (57.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 121 scoring matches, 38.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 25.77, median 21.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Zapy leads with 91 points across 2 seasons (1 title(s), GD 56)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (Banik Most-Sous, Benatky n. Jiz., Brozany, Hradec Kralove B, Jablonec B...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Pardubice B earns 17 more points at home than away (36 home vs 19 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — FK Ceska Lipa won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Zapy beat Jablonec B by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.260 per match): first half 3.353 vs last half 3.093 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 5.529)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.125)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 36 matches (11.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-0 (22 of 140 home matches, 15.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (36 of 76 draw matches, 47.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (23 of 110 away matches, 20.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 19 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_conceded_last_5 |corr| = 0.0986 (n=326 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 10.24: home 4.086, draw 0.750, away -6.155
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 326 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 326 |
| Average goals per match | 3.31 |
| Home win rate | 42.9% |
| Draw rate | 23.3% |
| Away win rate | 33.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Zapy |
| Champion with most titles | FK Ceska Lipa |
| BTTS rate | 57.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 33.57 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.44 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.50 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 29.49 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.95 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 60.71 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.37 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 272 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 17 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 54 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 9.3% vs overall 3.7% (deviation 5.6 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 37.0% vs overall 42.9%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 29.6% vs overall 23.3%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 9 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (4 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=17 positions=1..17 teams=17
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=17 positions=1..17 teams=17
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=17 positions=1..17 teams=17
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
