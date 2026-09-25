# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:03:51+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: National League (England)
- Scope: league `national`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\national\database_profile.json | yes | yes | 32.80 |
| matches_analysis | E:\football_data_analysis\data\analysis\national\matches_analysis.json | yes | yes | 12.36 |
| goals_analysis | E:\football_data_analysis\data\analysis\national\goals_analysis.json | yes | yes | 6.36 |
| teams_analysis | E:\football_data_analysis\data\analysis\national\teams_analysis.json | yes | yes | 40.03 |
| season_trends | E:\football_data_analysis\data\analysis\national\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\national\scoreline_analysis.json | yes | yes | 113.66 |
| relationships | E:\football_data_analysis\data\analysis\national\relationships.json | yes | yes | 14.38 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 665 matches: home wins 44.1%, draws 22.4%, away wins 33.5% (293H / 149D / 223A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 16 home and 17 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 179 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 665 matches produced 1951 goals (avg 2.934 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.2% vs away 45.8% of 1951 goals in total (home/away ratio 1.18)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 385 of 665 matches (57.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 205 scoring matches, 32.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.63, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Boreham Wood leads with 119 points across 2 seasons (1 title(s), GD 50)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 18 teams present in every one of the 2 seasons (Aldershot, Altrincham, Boreham Wood, Boston Utd, Carlisle...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Altrincham earns 26 more points at home than away (49 home vs 23 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Rochdale won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Boreham Wood beat Southend by 3 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.090 per match): first half 2.919 vs last half 3.009 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 7.083)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 2.833)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 77 matches (11.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (65 of 293 home matches, 22.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (77 of 149 draw matches, 51.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (56 of 223 away matches, 25.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 16 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_conceded_avg |corr| = 0.1027 (n=665 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 11.247: home 5.184, draw -1.745, away -6.063
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 665 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 665 |
| Average goals per match | 2.934 |
| Home win rate | 44.1% |
| Draw rate | 22.4% |
| Away win rate | 33.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Boreham Wood |
| Champion with most titles | Rochdale |
| BTTS rate | 57.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.80 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 12.36 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.36 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 40.03 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 113.66 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.38 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 557 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 24 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 108 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 0.9% vs overall 4.4% (deviation 3.5 pp)
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 7 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=19, fgte=19 rows)
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
