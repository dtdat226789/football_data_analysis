# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:02:06+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie B (Italy)
- Scope: league `italy2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\italy2\database_profile.json | yes | yes | 29.30 |
| matches_analysis | E:\football_data_analysis\data\analysis\italy2\matches_analysis.json | yes | yes | 10.54 |
| goals_analysis | E:\football_data_analysis\data\analysis\italy2\goals_analysis.json | yes | yes | 6.15 |
| teams_analysis | E:\football_data_analysis\data\analysis\italy2\teams_analysis.json | yes | yes | 36.07 |
| season_trends | E:\football_data_analysis\data\analysis\italy2\season_trends.json | yes | yes | 3.90 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\italy2\scoreline_analysis.json | yes | yes | 69.29 |
| relationships | E:\football_data_analysis\data\analysis\italy2\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 440 matches: home wins 44.5%, draws 30.5%, away wins 25.0% (196H / 134D / 110A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 12 home and 12 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 105 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 440 matches produced 1125 goals (avg 2.557 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.6% vs away 42.4% of 1125 goals in total (home/away ratio 1.36)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 240 of 440 matches (54.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 113 scoring matches, 27.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.59, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Palermo leads with 88 points across 2 seasons (1 title(s), GD 32)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (Avellino, Carrarese, Catanzaro, Cesena, Empoli...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Palermo earns 28 more points at home than away (58 home vs 30 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Monza won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Monza beat Venezia by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.094 per match): first half 2.546 vs last half 2.64 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.300)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 69 matches (15.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (49 of 196 home matches, 25.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (69 of 134 draw matches, 51.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (32 of 110 away matches, 29.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 5 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_wins_last_5 |corr| = 0.1202 (n=440 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.178: home 3.260, draw -2.216, away -3.918
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (8)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 440 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 440 |
| Average goals per match | 2.557 |
| Home win rate | 44.5% |
| Draw rate | 30.5% |
| Away win rate | 25.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Palermo |
| Champion with most titles | Monza |
| BTTS rate | 54.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 29.30 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 10.54 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.15 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 36.07 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.90 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 69.29 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 390 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 50 matches, expected 380
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **4.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 2.0% vs overall 7.0% (deviation 5.0 pp)
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 26.0% vs overall 30.5%
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 32.0% vs overall 25.0%
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
