# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:51:39+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Allsvenskan Women (Sweden)
- Scope: league `wsweden`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\wsweden\database_profile.json | yes | yes | 31.73 |
| matches_analysis | E:\football_data_analysis\data\analysis\wsweden\matches_analysis.json | yes | yes | 9.66 |
| goals_analysis | E:\football_data_analysis\data\analysis\wsweden\goals_analysis.json | yes | yes | 6.28 |
| teams_analysis | E:\football_data_analysis\data\analysis\wsweden\teams_analysis.json | yes | yes | 25.47 |
| season_trends | E:\football_data_analysis\data\analysis\wsweden\season_trends.json | yes | yes | 3.89 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\wsweden\scoreline_analysis.json | yes | yes | 60.26 |
| relationships | E:\football_data_analysis\data\analysis\wsweden\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 315 matches: home wins 46.0%, draws 16.5%, away wins 37.5% (145H / 52D / 118A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 7 home and 12 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 104 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 315 matches produced 987 goals (avg 3.133 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.2% vs away 46.8% of 987 goals in total (home/away ratio 1.14)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 159 of 315 matches (50.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 122 scoring matches, 39.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 26.99, median 20.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Hacken W leads with 116 points across 2 seasons (2 title(s), GD 111)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (AIK W, Djurgarden W, Hacken W, Hammarby W, IF Brommapojkarna W...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Hammarby W earns 19 more points at home than away (63 home vs 44 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Hacken W won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025: Hacken W beat Hammarby W by 4 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.465 per match): first half 3.33 vs last half 2.865 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025 (goals view, avg abs position diff 5.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026 (luck view, avg abs position diff 2.429)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 29 matches (9.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (29 of 145 home matches, 20.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (25 of 52 draw matches, 48.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (27 of 118 away matches, 22.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 10 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.096 (n=315 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 10.831: home 4.848, draw -1.288, away -5.983
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 315 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 315 |
| Average goals per match | 3.133 |
| Home win rate | 46.0% |
| Draw rate | 16.5% |
| Away win rate | 37.5% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | Hacken W |
| Champion with most titles | Hacken W |
| BTTS rate | 50.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.73 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.66 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.28 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 25.47 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.89 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 60.26 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 182 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 14 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 133 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 14 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 3 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=35, fgte=35 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=14 positions=1..14 teams=14
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=14 positions=1..14 teams=14
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=14 positions=1..14 teams=14
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=14 positions=1..14 teams=14
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=14 positions=1..14 teams=14
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=14 positions=1..14 teams=14

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
