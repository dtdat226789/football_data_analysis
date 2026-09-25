# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:00:07+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Super League (Greece)
- Scope: league `greece1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\greece1\database_profile.json | yes | yes | 31.10 |
| matches_analysis | E:\football_data_analysis\data\analysis\greece1\matches_analysis.json | yes | yes | 8.37 |
| goals_analysis | E:\football_data_analysis\data\analysis\greece1\goals_analysis.json | yes | yes | 6.14 |
| teams_analysis | E:\football_data_analysis\data\analysis\greece1\teams_analysis.json | yes | yes | 26.28 |
| season_trends | E:\football_data_analysis\data\analysis\greece1\season_trends.json | yes | yes | 3.95 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\greece1\scoreline_analysis.json | yes | yes | 48.38 |
| relationships | E:\football_data_analysis\data\analysis\greece1\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 281 matches: home wins 41.3%, draws 27.4%, away wins 31.3% (116H / 77D / 88A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 7 home and 5 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 79 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 281 matches produced 712 goals (avg 2.534 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.0% vs away 44.0% of 712 goals in total (home/away ratio 1.27)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 134 of 281 matches (47.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 75 scoring matches, 29.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.10, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — AEK Athens leads with 83 points across 2 seasons (1 title(s), GD 47)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (AEK Athens, Aris, Asteras Tripolis, Atromitos, Kifisia...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — PAOK earns 13 more points at home than away (46 home vs 33 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — AEK Athens won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: AEK Athens beat Olympiacos Piraeus by 3 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (-0.023 per match): first half 2.537 vs last half 2.514 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.667)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.429)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 41 matches (14.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (23 of 116 home matches, 19.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (41 of 77 draw matches, 53.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (24 of 88 away matches, 27.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0962 (n=281 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 9.518: home 3.836, draw -1.571, away -5.682
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 281 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 281 |
| Average goals per match | 2.534 |
| Home win rate | 41.3% |
| Draw rate | 27.4% |
| Away win rate | 31.3% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | AEK Athens |
| Champion with most titles | AEK Athens |
| BTTS rate | 47.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.10 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.37 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.14 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 26.28 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.95 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 48.38 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 246 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 15 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 35 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 14 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 5.7% vs overall 8.5% (deviation 2.8 pp)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=15 positions=1..15 teams=15
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=15 positions=1..15 teams=15
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=15 positions=1..15 teams=15
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=14 positions=1..14 teams=14
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=14 positions=1..14 teams=14
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=14 positions=1..14 teams=14

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
