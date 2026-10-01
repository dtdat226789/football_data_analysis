# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:50:36+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\france3\database_profile.json | yes | yes | 31.03 |
| matches_analysis | E:\football_data_analysis\data\analysis\france3\matches_analysis.json | yes | yes | 8.60 |
| goals_analysis | E:\football_data_analysis\data\analysis\france3\goals_analysis.json | yes | yes | 6.23 |
| teams_analysis | E:\football_data_analysis\data\analysis\france3\teams_analysis.json | yes | yes | 66.49 |
| season_trends | E:\football_data_analysis\data\analysis\france3\season_trends.json | yes | yes | 3.92 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\france3\scoreline_analysis.json | yes | yes | 60.44 |
| relationships | E:\football_data_analysis\data\analysis\france3\relationships.json | yes | yes | 14.32 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 388 matches: home wins 36.1%, draws 32.5%, away wins 31.4% (140H / 126D / 122A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 5 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 89 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 388 matches produced 943 goals (avg 2.430 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.1% vs away 47.9% of 943 goals in total (home/away ratio 1.09)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 201 of 388 matches (51.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 121 scoring matches, 35.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.41, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Rouen leads with 72 points across 2 seasons (0 title(s), GD 24)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (Aubagne, Bourg en Bresse, Caen, Concarneau, Fleury-Merogis...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Le Puy-en earns 22 more points at home than away (22 home vs 0 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Dijon won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: La Roche beat Rouen by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (-0.024 per match): first half 2.436 vs last half 2.412 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 17.800)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.368)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 61 matches (15.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (34 of 140 home matches, 24.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (61 of 126 draw matches, 48.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (35 of 122 away matches, 28.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 5 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_position_before_match |corr| = 0.13 (n=303 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.737: home 1.917, draw 0.530, away -2.819
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 388 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 388 |
| Average goals per match | 2.43 |
| Home win rate | 36.1% |
| Draw rate | 32.5% |
| Away win rate | 31.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Rouen |
| Champion with most titles | Dijon |
| BTTS rate | 51.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.03 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.60 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.23 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 66.49 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.92 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 60.44 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.32 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 303 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 50 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 85 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 19 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=50 positions=1..50 teams=50
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=50 positions=1..50 teams=50
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=50 positions=1..50 teams=50
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=19 positions=1..19 teams=19
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=19 positions=1..19 teams=19
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=19 positions=1..19 teams=19

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
