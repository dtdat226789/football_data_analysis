# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:47:29+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 3. CFL - Group A (Czech Republic)
- Scope: league `czech3a`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\czech3a\database_profile.json | yes | yes | 33.17 |
| matches_analysis | E:\football_data_analysis\data\analysis\czech3a\matches_analysis.json | yes | yes | 9.03 |
| goals_analysis | E:\football_data_analysis\data\analysis\czech3a\goals_analysis.json | yes | yes | 6.34 |
| teams_analysis | E:\football_data_analysis\data\analysis\czech3a\teams_analysis.json | yes | yes | 30.62 |
| season_trends | E:\football_data_analysis\data\analysis\czech3a\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\czech3a\scoreline_analysis.json | yes | yes | 63.50 |
| relationships | E:\football_data_analysis\data\analysis\czech3a\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 337 matches: home wins 44.2%, draws 22.6%, away wins 33.2% (149H / 76D / 112A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 11 home and 4 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 87 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 337 matches produced 1085 goals (avg 3.220 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.7% vs away 46.3% of 1085 goals in total (home/away ratio 1.16)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 192 of 337 matches (57.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 130 scoring matches, 41.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 26.37, median 19.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Domazlice leads with 88 points across 2 seasons (1 title(s), GD 48)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (Admira Prague, Aritma Prague, Bohemians 1905 B, Domazlice, Dukla Prague B...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Bohemians 1905 B earns 20 more points at home than away (33 home vs 13 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — SK Kladno won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Domazlice beat Kraluv Dvur by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.128 per match): first half 3.195 vs last half 3.323 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.471)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.875)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 27 matches (8.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (25 of 149 home matches, 16.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (27 of 76 draw matches, 35.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (19 of 112 away matches, 17.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 22 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_rest_days |corr| = -0.1361 (n=264 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.87: home 2.177, draw 0.491, away -4.692
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 337 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 337 |
| Average goals per match | 3.22 |
| Home win rate | 44.2% |
| Draw rate | 22.6% |
| Away win rate | 33.2% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Domazlice |
| Champion with most titles | SK Kladno |
| BTTS rate | 57.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 33.17 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.03 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 30.62 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 63.50 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 272 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 17 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 65 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 10.8% vs overall 7.1% (deviation 3.7 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 38.5% vs overall 44.2%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 29.2% vs overall 22.6%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 8 match(es) with >= 8 total goals (extreme scorelines)
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
