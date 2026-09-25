# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:51:03+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premiere Ligue Women (France)
- Scope: league `wfrance1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\wfrance1\database_profile.json | yes | yes | 32.91 |
| matches_analysis | E:\football_data_analysis\data\analysis\wfrance1\matches_analysis.json | yes | yes | 7.27 |
| goals_analysis | E:\football_data_analysis\data\analysis\wfrance1\goals_analysis.json | yes | yes | 6.31 |
| teams_analysis | E:\football_data_analysis\data\analysis\wfrance1\teams_analysis.json | yes | yes | 24.00 |
| season_trends | E:\football_data_analysis\data\analysis\wfrance1\season_trends.json | yes | yes | 3.95 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\wfrance1\scoreline_analysis.json | yes | yes | 34.41 |
| relationships | E:\football_data_analysis\data\analysis\wfrance1\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 153 matches: home wins 40.5%, draws 18.3%, away wins 41.2% (62H / 28D / 63A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 4 home and 2 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — away lead at HT -> away win occurred 45 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 153 matches produced 471 goals (avg 3.078 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 49.5% vs away 50.5% of 471 goals in total (home/away ratio 0.98)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 70 of 153 matches (45.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 55 scoring matches, 39.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 27.11, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Lyon W leads with 66 points across 1 seasons (1 title(s), GD 78)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 2 seasons (Fleury 91 W, Le Havre W, Lens W, Marseille W, Montpellier W...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Lyon W earns 12 more points at home than away (39 home vs 27 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Lyon W won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: OL Lyonnes W beat PSG W by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.352 per match): first half 3.037 vs last half 3.389 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 3.667)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.833)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-2 in 12 matches (7.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (12 of 62 home matches, 19.4%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (11 of 28 draw matches, 39.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (12 of 63 away matches, 19.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 13 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_goals_avg |corr| = 0.25 (n=153 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 11.963: home 6.645, draw -1.964, away -5.317
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 153 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 153 |
| Average goals per match | 3.078 |
| Home win rate | 40.5% |
| Draw rate | 18.3% |
| Away win rate | 41.2% |
| Most common scoreline | 1-2 |
| Dominant team (lifetime points) | Lyon W |
| Champion with most titles | Lyon W |
| BTTS rate | 45.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.91 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 7.27 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.31 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 24.00 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.95 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 34.41 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 135 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 50.0% vs overall 40.5%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 33.3% vs overall 41.2%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 7 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=35, fgte=35 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=12 positions=1..12 teams=12
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=12 positions=1..12 teams=12
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=12 positions=1..12 teams=12
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
