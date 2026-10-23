# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:50:51+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Regionalliga North (Germany)
- Scope: league `germany-north`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\germany-north\database_profile.json | yes | yes | 33.27 |
| matches_analysis | E:\football_data_analysis\data\analysis\germany-north\matches_analysis.json | yes | yes | 12.08 |
| goals_analysis | E:\football_data_analysis\data\analysis\germany-north\goals_analysis.json | yes | yes | 6.43 |
| teams_analysis | E:\football_data_analysis\data\analysis\germany-north\teams_analysis.json | yes | yes | 32.80 |
| season_trends | E:\football_data_analysis\data\analysis\germany-north\season_trends.json | yes | yes | 3.98 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\germany-north\scoreline_analysis.json | yes | yes | 78.86 |
| relationships | E:\football_data_analysis\data\analysis\germany-north\relationships.json | yes | yes | 14.38 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 415 matches: home wins 41.9%, draws 21.7%, away wins 36.4% (174H / 90D / 151A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 20 home and 11 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 101 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 415 matches produced 1535 goals (avg 3.699 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.9% vs away 47.1% of 1535 goals in total (home/away ratio 1.12)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 264 of 415 matches (63.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 171 scoring matches, 42.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 26.52, median 19.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — VfB Oldenburg leads with 94 points across 2 seasons (0 title(s), GD 60)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 15 teams present in every one of the 2 seasons (Bremer, Drochtersen/Assel, Emden, Hamburger SV II, Hannover II...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Drochtersen/Assel earns 16 more points at home than away (54 home vs 38 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Meppen won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: SC Weiche-08 beat Schoningen by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.274 per match): first half 3.634 vs last half 3.908 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.421)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.632)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 41 matches (9.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (22 of 174 home matches, 12.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (41 of 90 draw matches, 45.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-2 (22 of 151 away matches, 14.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 35 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_wins_last_5 |corr| = 0.1402 (n=317 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 10.401: home 4.852, draw -3.536, away -5.549
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 415 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 415 |
| Average goals per match | 3.699 |
| Home win rate | 41.9% |
| Draw rate | 21.7% |
| Away win rate | 36.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | VfB Oldenburg |
| Champion with most titles | Meppen |
| BTTS rate | 63.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 33.27 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 12.08 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.43 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 32.80 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.98 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 78.86 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.38 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 317 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 98 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 19 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 20 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=19 positions=1..19 teams=19
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=19 positions=1..19 teams=19
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=19 positions=1..19 teams=19

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
