# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:55:11+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier League (Azerbaijan)
- Scope: league `azer`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\azer\database_profile.json | yes | yes | 31.85 |
| matches_analysis | E:\football_data_analysis\data\analysis\azer\matches_analysis.json | yes | yes | 7.42 |
| goals_analysis | E:\football_data_analysis\data\analysis\azer\goals_analysis.json | yes | yes | 6.23 |
| teams_analysis | E:\football_data_analysis\data\analysis\azer\teams_analysis.json | yes | yes | 22.80 |
| season_trends | E:\football_data_analysis\data\analysis\azer\season_trends.json | yes | yes | 3.94 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\azer\scoreline_analysis.json | yes | yes | 43.16 |
| relationships | E:\football_data_analysis\data\analysis\azer\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 234 matches: home wins 39.7%, draws 23.9%, away wins 36.3% (93H / 56D / 85A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 4 home and 3 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 57 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 234 matches produced 600 goals (avg 2.564 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.0% vs away 48.0% of 600 goals in total (home/away ratio 1.08)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 106 of 234 matches (45.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 58 scoring matches, 27.4% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.83, median 32.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Sabah Baku leads with 93 points across 2 seasons (1 title(s), GD 63)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 11 teams present in every one of the 2 seasons (Araz, Gabala, Imisli FK, Kapaz, Neftci Baku...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Zira earns 15 more points at home than away (39 home vs 24 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Sabah Baku won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Neftci Baku beat Sabah Baku by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.075 per match): first half 2.575 vs last half 2.5 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 2.923)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 25 matches (10.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (25 of 93 home matches, 26.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (24 of 56 draw matches, 42.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (22 of 85 away matches, 25.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_points_last_5 |corr| = 0.1919 (n=234 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 12.364: home 6.129, draw -1.464, away -6.235
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 234 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 234 |
| Average goals per match | 2.564 |
| Home win rate | 39.7% |
| Draw rate | 23.9% |
| Away win rate | 36.3% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Sabah Baku |
| Champion with most titles | Sabah Baku |
| BTTS rate | 45.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.85 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 7.42 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.23 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 22.80 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.94 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 43.16 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 200 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 13 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 34 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 52.9% vs overall 39.7%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 26.5% vs overall 36.3%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=2, fgte=2 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=13 positions=1..13 teams=13
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=13 positions=1..13 teams=13
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=13 positions=1..13 teams=13
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
