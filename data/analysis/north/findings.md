# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:04:01+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: National League North (England)
- Scope: league `north`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\north\database_profile.json | yes | yes | 32.66 |
| matches_analysis | E:\football_data_analysis\data\analysis\north\matches_analysis.json | yes | yes | 13.51 |
| goals_analysis | E:\football_data_analysis\data\analysis\north\goals_analysis.json | yes | yes | 6.44 |
| teams_analysis | E:\football_data_analysis\data\analysis\north\teams_analysis.json | yes | yes | 40.22 |
| season_trends | E:\football_data_analysis\data\analysis\north\season_trends.json | yes | yes | 3.98 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\north\scoreline_analysis.json | yes | yes | 114.87 |
| relationships | E:\football_data_analysis\data\analysis\north\relationships.json | yes | yes | 14.37 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 668 matches: home wins 43.7%, draws 22.0%, away wins 34.3% (292H / 147D / 229A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 21 home and 18 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 173 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 668 matches produced 1997 goals (avg 2.990 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.6% vs away 45.4% of 1997 goals in total (home/away ratio 1.20)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 401 of 668 matches (60.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 223 scoring matches, 35.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.15, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — South Shields leads with 116 points across 2 seasons (0 title(s), GD 54)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 18 teams present in every one of the 2 seasons (AFC Telford, Bedford, Buxton, Chester, Chorley...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Chorley earns 22 more points at home than away (45 home vs 23 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — AFC Fylde won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: AFC Fylde beat South Shields by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.363 per match): first half 3.048 vs last half 2.685 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 9.333)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 76 matches (11.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (76 of 292 home matches, 26.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (72 of 147 draw matches, 49.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (59 of 229 away matches, 25.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 17 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1406 (n=668 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.568: home 2.205, draw -0.122, away -3.362
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 668 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 668 |
| Average goals per match | 2.99 |
| Home win rate | 43.7% |
| Draw rate | 22.0% |
| Away win rate | 34.3% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | South Shields |
| Champion with most titles | AFC Fylde |
| BTTS rate | 60.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.66 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 13.51 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.44 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 40.22 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.98 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 114.87 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.37 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 560 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 24 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 108 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 49.1% vs overall 43.7%
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=22, fgte=22 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=24 positions=1..24 teams=24
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=24 positions=1..24 teams=24
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=24 positions=1..24 teams=24
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=24 positions=1..24 teams=24
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=24 positions=1..24 teams=24
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=24 positions=1..24 teams=24

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
