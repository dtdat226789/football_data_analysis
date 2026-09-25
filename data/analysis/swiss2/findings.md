# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:49:34+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Challenge League (Switzerland)
- Scope: league `swiss2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\swiss2\database_profile.json | yes | yes | 32.41 |
| matches_analysis | E:\football_data_analysis\data\analysis\swiss2\matches_analysis.json | yes | yes | 7.27 |
| goals_analysis | E:\football_data_analysis\data\analysis\swiss2\goals_analysis.json | yes | yes | 6.32 |
| teams_analysis | E:\football_data_analysis\data\analysis\swiss2\teams_analysis.json | yes | yes | 21.90 |
| season_trends | E:\football_data_analysis\data\analysis\swiss2\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\swiss2\scoreline_analysis.json | yes | yes | 44.51 |
| relationships | E:\football_data_analysis\data\analysis\swiss2\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 231 matches: home wins 44.6%, draws 22.5%, away wins 32.9% (103H / 52D / 76A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 4 home and 2 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 60 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 231 matches produced 702 goals (avg 3.039 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.4% vs away 45.6% of 702 goals in total (home/away ratio 1.19)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 132 of 231 matches (57.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 100 scoring matches, 46.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 27.17, median 19.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Aarau leads with 92 points across 2 seasons (0 title(s), GD 28)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 8 teams present in every one of the 2 seasons (Aarau, Etoile-Carouge, Lausanne Ouchy, Rapperswil-Jona, Stade Nyonnais...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Vaduz earns 13 more points at home than away (47 home vs 34 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Vaduz won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Vaduz beat Aarau by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (-0.021 per match): first half 3.043 vs last half 3.022 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 4.400)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 27 matches (11.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (27 of 103 home matches, 26.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (20 of 52 draw matches, 38.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (17 of 76 away matches, 22.4%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 9 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.1339 (n=231 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 11.216: home 4.466, draw -0.519, away -6.750
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 231 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 231 |
| Average goals per match | 3.039 |
| Home win rate | 44.6% |
| Draw rate | 22.5% |
| Away win rate | 32.9% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | Aarau |
| Champion with most titles | Vaduz |
| BTTS rate | 57.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.41 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 7.27 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.32 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 21.90 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 44.51 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 186 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 11 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 45 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 10 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.4% vs overall 6.1% (deviation 1.7 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 26.7% vs overall 22.5%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=30, fgte=30 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=11 positions=1..11 teams=11
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=11 positions=1..11 teams=11
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=11 positions=1..11 teams=11
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=10 positions=1..10 teams=10
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=10 positions=1..10 teams=10
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
