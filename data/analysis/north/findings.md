# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:02:31+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: National League North (England)
- Scope: league `north`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\north\database_profile.json | yes | yes | 32.66 |
| matches_analysis | E:\football_data_analysis\data\analysis\north\matches_analysis.json | yes | yes | 13.51 |
| goals_analysis | E:\football_data_analysis\data\analysis\north\goals_analysis.json | yes | yes | 6.44 |
| teams_analysis | E:\football_data_analysis\data\analysis\north\teams_analysis.json | yes | yes | 40.21 |
| season_trends | E:\football_data_analysis\data\analysis\north\season_trends.json | yes | yes | 3.98 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\north\scoreline_analysis.json | yes | yes | 116.27 |
| relationships | E:\football_data_analysis\data\analysis\north\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 680 matches: home wins 43.7%, draws 22.4%, away wins 34.0% (297H / 152D / 231A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 21 home and 18 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 177 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 680 matches produced 2035 goals (avg 2.993 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.6% vs away 45.4% of 2035 goals in total (home/away ratio 1.21)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 410 of 680 matches (60.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 225 scoring matches, 34.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.14, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — South Shields leads with 119 points across 2 seasons (0 title(s), GD 58)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 18 teams present in every one of the 2 seasons (AFC Telford, Bedford, Buxton, Chester, Chorley...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Chorley earns 25 more points at home than away (48 home vs 23 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — AFC Fylde won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: AFC Fylde beat South Shields by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.315 per match): first half 3.048 vs last half 2.733 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 8.917)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.417)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 77 matches (11.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (77 of 297 home matches, 25.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (76 of 152 draw matches, 50.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (60 of 231 away matches, 26.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 17 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1365 (n=560 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.509: home 2.699, draw -0.095, away -3.810
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 680 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 680 |
| Average goals per match | 2.993 |
| Home win rate | 43.7% |
| Draw rate | 22.4% |
| Away win rate | 34.0% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | South Shields |
| Champion with most titles | AFC Fylde |
| BTTS rate | 60.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.66 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 13.51 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.44 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 40.21 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.98 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 116.27 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 560 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 24 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 120 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 48.3% vs overall 43.7%
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
