# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:53:20+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Eerste Divisie (Netherlands)
- Scope: league `holland2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\holland2\database_profile.json | yes | yes | 31.75 |
| matches_analysis | E:\football_data_analysis\data\analysis\holland2\matches_analysis.json | yes | yes | 10.99 |
| goals_analysis | E:\football_data_analysis\data\analysis\holland2\goals_analysis.json | yes | yes | 6.43 |
| teams_analysis | E:\football_data_analysis\data\analysis\holland2\teams_analysis.json | yes | yes | 32.67 |
| season_trends | E:\football_data_analysis\data\analysis\holland2\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\holland2\scoreline_analysis.json | yes | yes | 86.83 |
| relationships | E:\football_data_analysis\data\analysis\holland2\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 474 matches: home wins 45.1%, draws 20.5%, away wins 34.4% (214H / 97D / 163A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 16 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 134 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 474 matches produced 1551 goals (avg 3.272 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.9% vs away 45.1% of 1551 goals in total (home/away ratio 1.22)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 299 of 474 matches (63.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 170 scoring matches, 37.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 27.48, median 22.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Den Haag leads with 89 points across 1 seasons (1 title(s), GD 53)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 18 teams present in every one of the 2 seasons (Almere City, De Graafschap, Den Bosch, Dordrecht, Eindhoven FC...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Helmond earns 27 more points at home than away (37 home vs 10 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Den Haag won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Heracles beat Almere City by 5 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.511 per match): first half 3.184 vs last half 3.695 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 5.905)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.200)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 43 matches (9.1%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (41 of 214 home matches, 19.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (43 of 97 draw matches, 44.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (38 of 163 away matches, 23.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 22 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_rest_days |corr| = 0.1401 (n=383 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.764: home 1.928, draw 0.388, away -2.836
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 474 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 474 |
| Average goals per match | 3.272 |
| Home win rate | 45.1% |
| Draw rate | 20.5% |
| Away win rate | 34.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Den Haag |
| Champion with most titles | Den Haag |
| BTTS rate | 63.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.75 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 10.99 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.43 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 32.67 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 86.83 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 392 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 21 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 82 matches, expected 380
- **4.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **5.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.695 vs overall 3.272 (deviation 0.423)
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 57.3% vs overall 45.1%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 14.6% vs overall 20.5%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 28.0% vs overall 34.4%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=21 positions=1..21 teams=21
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=21 positions=1..21 teams=21
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=21 positions=1..21 teams=21

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
