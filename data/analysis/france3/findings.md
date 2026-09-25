# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:59:09+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\france3\database_profile.json | yes | yes | 31.02 |
| matches_analysis | E:\football_data_analysis\data\analysis\france3\matches_analysis.json | yes | yes | 8.41 |
| goals_analysis | E:\football_data_analysis\data\analysis\france3\goals_analysis.json | yes | yes | 6.23 |
| teams_analysis | E:\football_data_analysis\data\analysis\france3\teams_analysis.json | yes | yes | 65.47 |
| season_trends | E:\football_data_analysis\data\analysis\france3\season_trends.json | yes | yes | 3.92 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\france3\scoreline_analysis.json | yes | yes | 58.03 |
| relationships | E:\football_data_analysis\data\analysis\france3\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 371 matches: home wins 36.4%, draws 32.3%, away wins 31.3% (135H / 120D / 116A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 4 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 85 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 371 matches produced 899 goals (avg 2.423 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.1% vs away 47.9% of 899 goals in total (home/away ratio 1.09)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 188 of 371 matches (50.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 115 scoring matches, 34.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.50, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Rouen leads with 72 points across 2 seasons (1 title(s), GD 25)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (Aubagne, Bourg en Bresse, Caen, Concarneau, Fleury-Merogis...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Le Puy-en earns 22 more points at home than away (22 home vs 0 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Dijon won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Rouen beat La Roche by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.068 per match): first half 2.436 vs last half 2.368 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 17.800)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 57 matches (15.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (33 of 135 home matches, 24.4%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (57 of 120 draw matches, 47.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (30 of 116 away matches, 25.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 4 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_position_before_match |corr| = 0.1107 (n=371 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — position_difference spreads group means over 3.974: home -1.630, draw 0.242, away 2.345
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 371 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 371 |
| Average goals per match | 2.423 |
| Home win rate | 36.4% |
| Draw rate | 32.3% |
| Away win rate | 31.3% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Rouen |
| Champion with most titles | Dijon |
| BTTS rate | 50.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.02 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.41 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.23 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 65.47 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.92 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 58.03 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 303 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 50 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 68 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=50 positions=1..50 teams=50
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=50 positions=1..50 teams=50
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=50 positions=1..50 teams=50
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
