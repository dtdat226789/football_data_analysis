# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:42:59+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\primera2\database_profile.json | yes | yes | 28.96 |
| matches_analysis | E:\football_data_analysis\data\analysis\primera2\matches_analysis.json | yes | yes | 8.43 |
| goals_analysis | E:\football_data_analysis\data\analysis\primera2\goals_analysis.json | yes | yes | 6.34 |
| teams_analysis | E:\football_data_analysis\data\analysis\primera2\teams_analysis.json | yes | yes | 36.55 |
| season_trends | E:\football_data_analysis\data\analysis\primera2\season_trends.json | yes | yes | 3.95 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\primera2\scoreline_analysis.json | yes | yes | 67.10 |
| relationships | E:\football_data_analysis\data\analysis\primera2\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 419 matches: home wins 45.8%, draws 29.6%, away wins 24.6% (192H / 124D / 103A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 2 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 120 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 419 matches produced 956 goals (avg 2.282 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 58.5% vs away 41.5% of 956 goals in total (home/away ratio 1.41)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 185 of 419 matches (44.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 112 scoring matches, 30.4% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.72, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Atl. Madrid B leads with 75 points across 2 seasons (0 title(s), GD 26)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (Alcorcon, Algeciras, Antequera, Atl. Madrid B, CE Europa...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Eldense earns 27 more points at home than away (48 home vs 21 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Eldense won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Villarreal B beat Jaen by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.311 per match): first half 2.253 vs last half 2.564 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 5.100)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.800)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 57 matches (13.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (57 of 192 home matches, 29.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 0-0 (50 of 124 draw matches, 40.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (38 of 103 away matches, 36.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 5 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1399 (n=419 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — away_points_before_match spreads group means over 4.322: home 22.635, draw 20.911, away 25.233
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (6)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 419 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 419 |
| Average goals per match | 2.282 |
| Home win rate | 45.8% |
| Draw rate | 29.6% |
| Away win rate | 24.6% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Atl. Madrid B |
| Champion with most titles | Eldense |
| BTTS rate | 44.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 28.96 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.43 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 36.55 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.95 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 67.10 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 39 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 10.3% vs overall 11.9% (deviation 1.6 pp)
- **4.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **5.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **6.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
