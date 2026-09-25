# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:45:16+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: League Two (Scotland)
- Scope: league `scot2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\scot2\database_profile.json | yes | yes | 32.62 |
| matches_analysis | E:\football_data_analysis\data\analysis\scot2\matches_analysis.json | yes | yes | 8.01 |
| goals_analysis | E:\football_data_analysis\data\analysis\scot2\goals_analysis.json | yes | yes | 6.38 |
| teams_analysis | E:\football_data_analysis\data\analysis\scot2\teams_analysis.json | yes | yes | 21.99 |
| season_trends | E:\football_data_analysis\data\analysis\scot2\season_trends.json | yes | yes | 3.92 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\scot2\scoreline_analysis.json | yes | yes | 41.11 |
| relationships | E:\football_data_analysis\data\analysis\scot2\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 228 matches: home wins 43.4%, draws 27.2%, away wins 29.4% (99H / 62D / 67A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 5 home and 5 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 67 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 228 matches produced 691 goals (avg 3.031 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.8% vs away 46.2% of 691 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 138 of 228 matches (60.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 70 scoring matches, 32.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.22, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Clyde leads with 78 points across 2 seasons (1 title(s), GD 27)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 2 seasons (Annan, Clyde, Dumbarton, Edinburgh City, Elgin City...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Forfar Athletic earns 21 more points at home than away (41 home vs 20 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — East Kilbride won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Clyde beat Stranraer by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.539 per match): first half 2.936 vs last half 3.475 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.167)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.200)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 36 matches (15.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (19 of 99 home matches, 19.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (36 of 62 draw matches, 58.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (14 of 67 away matches, 20.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 5 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_win_rate |corr| = 0.1849 (n=228 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — away_points_before_match spreads group means over 3.704: home 21.323, draw 22.629, away 18.925
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (19)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 228 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 228 |
| Average goals per match | 3.031 |
| Home win rate | 43.4% |
| Draw rate | 27.2% |
| Away win rate | 29.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Clyde |
| Champion with most titles | East Kilbride |
| BTTS rate | 60.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.62 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.01 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.38 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 21.99 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.92 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 41.11 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 188 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 40 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 10 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.475 vs overall 3.031 (deviation 0.444)
- **7.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 0.0% vs overall 3.9% (deviation 3.9 pp)
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 60.0% vs overall 43.4%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 17.5% vs overall 27.2%
- **10.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 22.5% vs overall 29.4%
- **11.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **12.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows)
- **13.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=26, fgte=26 rows)
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=12 positions=1..12 teams=12
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=12 positions=1..12 teams=12
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=12 positions=1..12 teams=12
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=10 positions=1..10 teams=10
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=10 positions=1..10 teams=10
- **19.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
