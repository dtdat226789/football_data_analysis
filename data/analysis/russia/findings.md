# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:43:36+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier League (Russia)
- Scope: league `russia`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\russia\database_profile.json | yes | yes | 32.05 |
| matches_analysis | E:\football_data_analysis\data\analysis\russia\matches_analysis.json | yes | yes | 9.18 |
| goals_analysis | E:\football_data_analysis\data\analysis\russia\goals_analysis.json | yes | yes | 6.24 |
| teams_analysis | E:\football_data_analysis\data\analysis\russia\teams_analysis.json | yes | yes | 29.74 |
| season_trends | E:\football_data_analysis\data\analysis\russia\season_trends.json | yes | yes | 3.94 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\russia\scoreline_analysis.json | yes | yes | 53.02 |
| relationships | E:\football_data_analysis\data\analysis\russia\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 320 matches: home wins 42.8%, draws 29.1%, away wins 28.1% (137H / 93D / 90A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 12 home and 4 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 77 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 320 matches produced 827 goals (avg 2.584 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.3% vs away 44.7% of 827 goals in total (home/away ratio 1.24)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 174 of 320 matches (54.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 102 scoring matches, 34.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.51, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Krasnodar leads with 88 points across 2 seasons (0 title(s), GD 44)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 14 teams present in every one of the 2 seasons (Akhmat Grozny, Akron Togliatti, Baltika, CSKA Moscow, Dynamo Makhachkala...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Spartak Moscow earns 21 more points at home than away (46 home vs 25 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Zenit won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: CSKA Moscow beat Krasnodar by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.269 per match): first half 2.52 vs last half 2.789 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 5.500)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.750)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 48 matches (15.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (33 of 137 home matches, 24.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (48 of 93 draw matches, 51.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (27 of 90 away matches, 30.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1213 (n=320 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 8.513: home 3.613, draw -1.376, away -4.900
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 320 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 320 |
| Average goals per match | 2.584 |
| Home win rate | 42.8% |
| Draw rate | 29.1% |
| Away win rate | 28.1% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Krasnodar |
| Champion with most titles | Zenit |
| BTTS rate | 54.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.05 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.18 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.24 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 29.74 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.94 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 53.02 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 244 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 76 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 35.5% vs overall 42.8%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 34.2% vs overall 29.1%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (18 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
