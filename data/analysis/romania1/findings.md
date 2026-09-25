# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:43:18+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Superliga (Romania)
- Scope: league `romania1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\romania1\database_profile.json | yes | yes | 31.58 |
| matches_analysis | E:\football_data_analysis\data\analysis\romania1\matches_analysis.json | yes | yes | 9.05 |
| goals_analysis | E:\football_data_analysis\data\analysis\romania1\goals_analysis.json | yes | yes | 6.16 |
| teams_analysis | E:\football_data_analysis\data\analysis\romania1\teams_analysis.json | yes | yes | 30.97 |
| season_trends | E:\football_data_analysis\data\analysis\romania1\season_trends.json | yes | yes | 3.97 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\romania1\scoreline_analysis.json | yes | yes | 70.31 |
| relationships | E:\football_data_analysis\data\analysis\romania1\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 429 matches: home wins 46.4%, draws 27.3%, away wins 26.3% (199H / 117D / 113A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 11 home and 4 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 123 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 429 matches produced 1095 goals (avg 2.552 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 58.9% vs away 41.1% of 1095 goals in total (home/away ratio 1.43)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 217 of 429 matches (50.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 112 scoring matches, 28.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.53, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Univ. Craiova leads with 102 points across 2 seasons (1 title(s), GD 47)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 14 teams present in every one of the 2 seasons (CFR Cluj, Csikszereda M. Ciuc, Dinamo Bucuresti, FC Arges, FC Botosani...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Univ. Craiova earns 26 more points at home than away (64 home vs 38 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Univ. Craiova won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Dinamo Bucuresti beat FC Rapid Bucuresti by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.099 per match): first half 2.534 vs last half 2.633 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 7.684)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 56 matches (13.1%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (51 of 199 home matches, 25.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (56 of 117 draw matches, 47.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (42 of 113 away matches, 37.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 4 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_position_before_match |corr| = 0.1688 (n=429 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.623: home 2.774, draw -0.419, away -3.850
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 429 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 429 |
| Average goals per match | 2.552 |
| Home win rate | 46.4% |
| Draw rate | 27.3% |
| Away win rate | 26.3% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Univ. Craiova |
| Champion with most titles | Univ. Craiova |
| BTTS rate | 50.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.58 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.05 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.16 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 30.97 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.97 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 70.31 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 350 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 79 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 55.7% vs overall 46.4%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 17.7% vs overall 26.3%
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
