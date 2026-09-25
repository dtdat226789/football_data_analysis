# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:46:28+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\segunda4\database_profile.json | yes | yes | 31.53 |
| matches_analysis | E:\football_data_analysis\data\analysis\segunda4\matches_analysis.json | yes | yes | 9.39 |
| goals_analysis | E:\football_data_analysis\data\analysis\segunda4\goals_analysis.json | yes | yes | 6.17 |
| teams_analysis | E:\football_data_analysis\data\analysis\segunda4\teams_analysis.json | yes | yes | 40.29 |
| season_trends | E:\football_data_analysis\data\analysis\segunda4\season_trends.json | yes | yes | 3.98 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\segunda4\scoreline_analysis.json | yes | yes | 58.89 |
| relationships | E:\football_data_analysis\data\analysis\segunda4\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 350 matches: home wins 48.9%, draws 26.3%, away wins 24.9% (171H / 92D / 87A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 7 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 95 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 350 matches produced 804 goals (avg 2.297 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 58.5% vs away 41.5% of 804 goals in total (home/away ratio 1.41)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 177 of 350 matches (50.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 86 scoring matches, 27.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.94, median 30.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Deportiva Minera leads with 66 points across 1 seasons (1 title(s), GD 19)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 6 teams present in every one of the 2 seasons (Antoniano, CD Estepona, Linares, Puente Genil, Recreativo Huelva...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Antoniano earns 31 more points at home than away (40 home vs 9 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Deportiva Minera won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Deportiva Minera beat CD Extremadura by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.159 per match): first half 2.285 vs last half 2.444 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.632)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.889)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 60 matches (17.1%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (60 of 171 home matches, 35.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (50 of 92 draw matches, 54.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (27 of 87 away matches, 31.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 1 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_conceded_avg |corr| = 0.0853 (n=350 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 8.046: home 24.977, draw 19.283, away 16.931
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 350 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 350 |
| Average goals per match | 2.297 |
| Home win rate | 48.9% |
| Draw rate | 26.3% |
| Away win rate | 24.9% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Deportiva Minera |
| Champion with most titles | Deportiva Minera |
| BTTS rate | 50.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.53 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.39 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.17 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 40.29 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.98 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 58.89 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 323 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 27 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 11.1% vs overall 8.9% (deviation 2.2 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 33.3% vs overall 48.9%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 37.0% vs overall 24.9%
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (24 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=27, fgte=27 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
