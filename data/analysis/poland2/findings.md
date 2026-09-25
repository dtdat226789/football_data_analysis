# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:41:23+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Division 1 (Poland)
- Scope: league `poland2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\poland2\database_profile.json | yes | yes | 31.63 |
| matches_analysis | E:\football_data_analysis\data\analysis\poland2\matches_analysis.json | yes | yes | 9.96 |
| goals_analysis | E:\football_data_analysis\data\analysis\poland2\goals_analysis.json | yes | yes | 6.32 |
| teams_analysis | E:\football_data_analysis\data\analysis\poland2\teams_analysis.json | yes | yes | 34.74 |
| season_trends | E:\football_data_analysis\data\analysis\poland2\season_trends.json | yes | yes | 3.95 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\poland2\scoreline_analysis.json | yes | yes | 68.62 |
| relationships | E:\football_data_analysis\data\analysis\poland2\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 408 matches: home wins 41.7%, draws 27.5%, away wins 30.9% (170H / 112D / 126A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 7 home and 13 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 107 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 408 matches produced 1211 goals (avg 2.968 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.1% vs away 45.9% of 1211 goals in total (home/away ratio 1.18)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 258 of 408 matches (63.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 131 scoring matches, 33.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.77, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Wisla leads with 72 points across 1 seasons (1 title(s), GD 40)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (Chrobry Glogow, Grodzisk M., LKS Lodz, Legnica, Odra Opole...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Legnica earns 21 more points at home than away (45 home vs 24 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Wisla won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Grodzisk M. beat Termalica B-B. by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.271 per match): first half 3.021 vs last half 2.75 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.526)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.222)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 59 matches (14.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (46 of 170 home matches, 27.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (59 of 112 draw matches, 52.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (38 of 126 away matches, 30.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 12 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.0673 (n=408 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 3.877: home 1.465, draw 0.884, away -2.413
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 408 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 408 |
| Average goals per match | 2.968 |
| Home win rate | 41.7% |
| Draw rate | 27.5% |
| Away win rate | 30.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Wisla |
| Champion with most titles | Wisla |
| BTTS rate | 63.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.63 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.96 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.32 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 34.74 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.95 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 68.62 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 328 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 80 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
