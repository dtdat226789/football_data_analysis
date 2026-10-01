# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:08:26+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Prva liga (Slovenia)
- Scope: league `slovenia1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\slovenia1\database_profile.json | yes | yes | 33.07 |
| matches_analysis | E:\football_data_analysis\data\analysis\slovenia1\matches_analysis.json | yes | yes | 9.81 |
| goals_analysis | E:\football_data_analysis\data\analysis\slovenia1\goals_analysis.json | yes | yes | 6.23 |
| teams_analysis | E:\football_data_analysis\data\analysis\slovenia1\teams_analysis.json | yes | yes | 20.71 |
| season_trends | E:\football_data_analysis\data\analysis\slovenia1\season_trends.json | yes | yes | 3.92 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\slovenia1\scoreline_analysis.json | yes | yes | 41.54 |
| relationships | E:\football_data_analysis\data\analysis\slovenia1\relationships.json | yes | yes | 14.31 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 216 matches: home wins 45.8%, draws 21.3%, away wins 32.9% (99H / 46D / 71A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 10 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 70 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 216 matches produced 635 goals (avg 2.940 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.5% vs away 46.5% of 635 goals in total (home/away ratio 1.15)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 122 of 216 matches (56.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 77 scoring matches, 38.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 25.33, median 21.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Celje leads with 86 points across 2 seasons (1 title(s), GD 53)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 2 seasons (Aluminij, Bravo, Celje, Koper, Maribor...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Primorje earns 17 more points at home than away (20 home vs 3 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Celje won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Maribor beat Bravo by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.478 per match): first half 3.055 vs last half 2.577 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 4.600)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (goals view, avg abs position diff 1.636)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 25 matches (11.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (25 of 99 home matches, 25.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (19 of 46 draw matches, 41.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (17 of 71 away matches, 23.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_points_last_5 |corr| = 0.1964 (n=164 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 10.44: home 4.025, draw 0.100, away -6.415
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (19)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 216 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 216 |
| Average goals per match | 2.94 |
| Home win rate | 45.8% |
| Draw rate | 21.3% |
| Away win rate | 32.9% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | Celje |
| Champion with most titles | Celje |
| BTTS rate | 56.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 33.07 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.81 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.23 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 20.71 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.92 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 41.54 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.31 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 164 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 11 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 52 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 10 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 4.9% vs overall 6.5% (deviation 1.6 pp)
- **7.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 2.577 vs overall 2.94 (deviation 0.363)
- **8.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 11.5% vs overall 6.5% (deviation 5.0 pp)
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 34.6% vs overall 45.8%
- **10.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 30.8% vs overall 21.3%
- **11.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **12.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (34 extra rows)
- **13.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=29, fgte=29 rows)
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=11 positions=1..11 teams=11
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=11 positions=1..11 teams=11
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=11 positions=1..11 teams=11
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=10 positions=1..10 teams=10
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=10 positions=1..10 teams=10
- **19.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
