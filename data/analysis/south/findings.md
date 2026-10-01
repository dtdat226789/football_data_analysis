# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:08:42+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: National League South (England)
- Scope: league `south`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\south\database_profile.json | yes | yes | 32.81 |
| matches_analysis | E:\football_data_analysis\data\analysis\south\matches_analysis.json | yes | yes | 12.96 |
| goals_analysis | E:\football_data_analysis\data\analysis\south\goals_analysis.json | yes | yes | 6.36 |
| teams_analysis | E:\football_data_analysis\data\analysis\south\teams_analysis.json | yes | yes | 89.73 |
| season_trends | E:\football_data_analysis\data\analysis\south\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\south\scoreline_analysis.json | yes | yes | 123.48 |
| relationships | E:\football_data_analysis\data\analysis\south\relationships.json | yes | yes | 14.37 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 728 matches: home wins 45.7%, draws 23.1%, away wins 31.2% (333H / 168D / 227A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 17 home and 19 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 200 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 728 matches produced 2063 goals (avg 2.834 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.4% vs away 44.6% of 2063 goals in total (home/away ratio 1.24)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 399 of 728 matches (54.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 244 scoring matches, 35.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.58, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Maidstone leads with 99 points across 2 seasons (1 title(s), GD 30)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 18 teams present in every one of the 2 seasons (AFC Totton, Chelmsford, Chesham, Dag & Red, Dorking...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Weston-super earns 48 more points at home than away (48 home vs 0 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Worthing won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Worthing beat Hornchurch by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.053 per match): first half 2.825 vs last half 2.878 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 21.083)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 3.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 85 matches (11.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (85 of 333 home matches, 25.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (77 of 168 draw matches, 45.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (74 of 227 away matches, 32.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 21 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.1412 (n=605 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.397: home 2.474, draw -1.126, away -2.923
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 728 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 728 |
| Average goals per match | 2.834 |
| Home win rate | 45.7% |
| Draw rate | 23.1% |
| Away win rate | 31.2% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Maidstone |
| Champion with most titles | Worthing |
| BTTS rate | 54.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.81 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 12.96 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.36 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 89.73 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 123.48 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.37 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 605 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 72 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 123 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 35.8% vs overall 45.7%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 37.4% vs overall 31.2%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 8 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=29, fgte=29 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=72 positions=1..72 teams=72
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=72 positions=1..72 teams=72
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=72 positions=1..72 teams=72
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=24 positions=1..24 teams=24
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=24 positions=1..24 teams=24
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=24 positions=1..24 teams=24

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
