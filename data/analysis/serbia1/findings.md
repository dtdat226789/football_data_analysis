# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:47:04+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Mozzart Bet Super Liga (Serbia)
- Scope: league `serbia1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\serbia1\database_profile.json | yes | yes | 32.93 |
| matches_analysis | E:\football_data_analysis\data\analysis\serbia1\matches_analysis.json | yes | yes | 9.16 |
| goals_analysis | E:\football_data_analysis\data\analysis\serbia1\goals_analysis.json | yes | yes | 6.34 |
| teams_analysis | E:\football_data_analysis\data\analysis\serbia1\teams_analysis.json | yes | yes | 27.57 |
| season_trends | E:\football_data_analysis\data\analysis\serbia1\season_trends.json | yes | yes | 3.98 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\serbia1\scoreline_analysis.json | yes | yes | 61.03 |
| relationships | E:\football_data_analysis\data\analysis\serbia1\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 365 matches: home wins 43.6%, draws 28.5%, away wins 27.9% (159H / 104D / 102A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 7 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 109 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 365 matches produced 972 goals (avg 2.663 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.3% vs away 42.7% of 972 goals in total (home/away ratio 1.34)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 189 of 365 matches (51.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 95 scoring matches, 29.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.28, median 25.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Crvena zvezda leads with 114 points across 2 seasons (2 title(s), GD 90)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (Crvena zvezda, Cukaricki, IMT Novi Beograd, Mladost, Novi Pazar...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Zeleznicar Pancevo earns 29 more points at home than away (51 home vs 22 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Crvena zvezda won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Crvena zvezda beat Vojvodina by 6 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.016 per match): first half 2.66 vs last half 2.676 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 4.714)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.857)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 0-0 in 42 matches (11.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (39 of 159 home matches, 24.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 0-0 (42 of 104 draw matches, 40.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (25 of 102 away matches, 24.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 9 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.1144 (n=365 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 9.654: home 4.409, draw -1.058, away -5.245
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 365 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 365 |
| Average goals per match | 2.663 |
| Home win rate | 43.6% |
| Draw rate | 28.5% |
| Away win rate | 27.9% |
| Most common scoreline | 0-0 |
| Dominant team (lifetime points) | Crvena zvezda |
| Champion with most titles | Crvena zvezda |
| BTTS rate | 51.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.93 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.16 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 27.57 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.98 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 61.03 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 297 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 68 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 14 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 8.8% vs overall 11.5% (deviation 2.7 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 51.5% vs overall 43.6%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 22.1% vs overall 27.9%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (31 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=28, fgte=28 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=16 positions=1..16 teams=16
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=16 positions=1..16 teams=16
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=16 positions=1..16 teams=16
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=14 positions=1..14 teams=14
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=14 positions=1..14 teams=14
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=14 positions=1..14 teams=14

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
