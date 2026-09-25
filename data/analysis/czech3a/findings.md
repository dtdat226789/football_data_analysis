# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:56:42+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 3. CFL - Group A (Czech Republic)
- Scope: league `czech3a`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\czech3a\database_profile.json | yes | yes | 32.96 |
| matches_analysis | E:\football_data_analysis\data\analysis\czech3a\matches_analysis.json | yes | yes | 9.03 |
| goals_analysis | E:\football_data_analysis\data\analysis\czech3a\goals_analysis.json | yes | yes | 6.34 |
| teams_analysis | E:\football_data_analysis\data\analysis\czech3a\teams_analysis.json | yes | yes | 30.63 |
| season_trends | E:\football_data_analysis\data\analysis\czech3a\season_trends.json | yes | yes | 3.98 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\czech3a\scoreline_analysis.json | yes | yes | 62.30 |
| relationships | E:\football_data_analysis\data\analysis\czech3a\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 330 matches: home wins 44.5%, draws 22.4%, away wins 33.0% (147H / 74D / 109A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 11 home and 4 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 85 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 330 matches produced 1056 goals (avg 3.200 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.9% vs away 46.1% of 1056 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 187 of 330 matches (56.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 127 scoring matches, 41.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 26.65, median 19.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Domazlice leads with 85 points across 2 seasons (0 title(s), GD 45)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (Admira Prague, Aritma Prague, Bohemians 1905 B, Domazlice, Dukla Prague B...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Bohemians 1905 B earns 21 more points at home than away (33 home vs 12 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — SK Kladno won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Ceske Budejovice beat Kraluv Dvur by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.029 per match): first half 3.195 vs last half 3.224 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.471)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.125)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 26 matches (7.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (25 of 147 home matches, 17.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (26 of 74 draw matches, 35.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (19 of 109 away matches, 17.4%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 21 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_rest_days |corr| = -0.1227 (n=314 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.04: home 1.884, draw 0.581, away -4.156
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 330 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 330 |
| Average goals per match | 3.2 |
| Home win rate | 44.5% |
| Draw rate | 22.4% |
| Away win rate | 33.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Domazlice |
| Champion with most titles | SK Kladno |
| BTTS rate | 56.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.96 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.03 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 30.63 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.98 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 62.30 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 272 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 17 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 58 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 12.1% vs overall 7.3% (deviation 4.8 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 39.7% vs overall 44.5%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 29.3% vs overall 22.4%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 7 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (3 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=17 positions=1..17 teams=17
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=17 positions=1..17 teams=17
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=17 positions=1..17 teams=17
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
