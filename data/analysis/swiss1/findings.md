# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:49:14+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Super League (Switzerland)
- Scope: league `swiss1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\swiss1\database_profile.json | yes | yes | 33.36 |
| matches_analysis | E:\football_data_analysis\data\analysis\swiss1\matches_analysis.json | yes | yes | 10.91 |
| goals_analysis | E:\football_data_analysis\data\analysis\swiss1\goals_analysis.json | yes | yes | 6.48 |
| teams_analysis | E:\football_data_analysis\data\analysis\swiss1\teams_analysis.json | yes | yes | 22.92 |
| season_trends | E:\football_data_analysis\data\analysis\swiss1\season_trends.json | yes | yes | 3.94 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\swiss1\scoreline_analysis.json | yes | yes | 52.54 |
| relationships | E:\football_data_analysis\data\analysis\swiss1\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 284 matches: home wins 40.1%, draws 23.6%, away wins 36.3% (114H / 67D / 103A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 14 home and 12 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 66 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 284 matches produced 962 goals (avg 3.387 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.9% vs away 47.1% of 962 goals in total (home/away ratio 1.12)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 191 of 284 matches (67.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 120 scoring matches, 44.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 26.79, median 20.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Lugano leads with 92 points across 2 seasons (1 title(s), GD 37)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 11 teams present in every one of the 2 seasons (Basel, Grasshoppers, Lausanne, Lugano, Luzern...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Lugano earns 12 more points at home than away (52 home vs 40 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Thun won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Thun beat St. Gallen by 5 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.596 per match): first half 3.274 vs last half 3.87 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.769)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 29 matches (10.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (28 of 114 home matches, 24.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (29 of 67 draw matches, 43.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (28 of 103 away matches, 27.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 11 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_points_before_match |corr| = -0.0949 (n=284 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.988: home 3.658, draw -1.373, away -3.330
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (18)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 284 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 284 |
| Average goals per match | 3.387 |
| Home win rate | 40.1% |
| Draw rate | 23.6% |
| Away win rate | 36.3% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Lugano |
| Champion with most titles | Thun |
| BTTS rate | 67.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 33.36 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 10.91 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.48 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 22.92 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.94 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 52.54 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 230 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 13 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 54 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.87 vs overall 3.387 (deviation 0.483)
- **7.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 1.9% vs overall 3.9% (deviation 2.0 pp)
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 18.5% vs overall 23.6%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 42.6% vs overall 36.3%
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **11.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **12.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=30, fgte=30 rows)
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=13 positions=1..13 teams=13
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=13 positions=1..13 teams=13
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=13 positions=1..13 teams=13
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
