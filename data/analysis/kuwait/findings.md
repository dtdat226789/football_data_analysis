# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:01:04+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier League (Kuwait)
- Scope: league `kuwait`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\kuwait\database_profile.json | yes | yes | 31.37 |
| matches_analysis | E:\football_data_analysis\data\analysis\kuwait\matches_analysis.json | yes | yes | 6.49 |
| goals_analysis | E:\football_data_analysis\data\analysis\kuwait\goals_analysis.json | yes | yes | 6.21 |
| teams_analysis | E:\football_data_analysis\data\analysis\kuwait\teams_analysis.json | yes | yes | 21.00 |
| season_trends | E:\football_data_analysis\data\analysis\kuwait\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\kuwait\scoreline_analysis.json | yes | yes | 24.46 |
| relationships | E:\football_data_analysis\data\analysis\kuwait\relationships.json | yes | yes | 14.24 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 116 matches: home wins 41.4%, draws 25.0%, away wins 33.6% (48H / 29D / 39A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 2 home and 0 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 33 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 116 matches produced 311 goals (avg 2.681 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.9% vs away 44.1% of 311 goals in total (home/away ratio 1.27)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 58 of 116 matches (50.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 30 scoring matches, 27.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.19, median 30.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Al Kuwait leads with 56 points across 2 seasons (1 title(s), GD 41)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 10 teams present in every one of the 2 seasons (Al Arabi, Al Jahra, Al Kuwait, Al Naser, Al Qadisiya...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Al Kuwait earns 16 more points at home than away (36 home vs 20 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Al Kuwait won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Kazma SC beat Al Kuwait by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.378 per match): first half 2.622 vs last half 3.0 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 5.167)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 17 matches (14.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (12 of 48 home matches, 25.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (17 of 29 draw matches, 58.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (10 of 39 away matches, 25.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 1 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.2423 (n=98 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.96: home 4.400, draw -2.560, away -2.182
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 116 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 116 |
| Average goals per match | 2.681 |
| Home win rate | 41.4% |
| Draw rate | 25.0% |
| Away win rate | 33.6% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Al Kuwait |
| Champion with most titles | Al Kuwait |
| BTTS rate | 50.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.37 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 6.49 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.21 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 21.00 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 24.46 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.24 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 98 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=10 positions=1..10 teams=10
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=10 positions=1..10 teams=10
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=10 positions=1..10 teams=10
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
