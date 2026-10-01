# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:04:39+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\primera2\database_profile.json | yes | yes | 29.26 |
| matches_analysis | E:\football_data_analysis\data\analysis\primera2\matches_analysis.json | yes | yes | 8.43 |
| goals_analysis | E:\football_data_analysis\data\analysis\primera2\goals_analysis.json | yes | yes | 6.34 |
| teams_analysis | E:\football_data_analysis\data\analysis\primera2\teams_analysis.json | yes | yes | 36.58 |
| season_trends | E:\football_data_analysis\data\analysis\primera2\season_trends.json | yes | yes | 3.95 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\primera2\scoreline_analysis.json | yes | yes | 68.71 |
| relationships | E:\football_data_analysis\data\analysis\primera2\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 429 matches: home wins 45.2%, draws 29.4%, away wins 25.4% (194H / 126D / 109A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 2 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 120 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 429 matches produced 979 goals (avg 2.282 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 58.0% vs away 42.0% of 979 goals in total (home/away ratio 1.38)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 191 of 429 matches (44.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 114 scoring matches, 30.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.98, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Villarreal B leads with 76 points across 2 seasons (1 title(s), GD 29)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (Alcorcon, Algeciras, Antequera, Atl. Madrid B, CE Europa...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Eldense earns 27 more points at home than away (48 home vs 21 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Eldense won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Eldense beat Sabadell by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.257 per match): first half 2.253 vs last half 2.51 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 5.100)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.600)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 58 matches (13.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (58 of 194 home matches, 29.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 0-0 (50 of 126 draw matches, 39.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (39 of 109 away matches, 35.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 5 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1769 (n=380 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — away_points_before_match spreads group means over 4.792: home 24.890, draw 22.708, away 27.500
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (7)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 429 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 429 |
| Average goals per match | 2.282 |
| Home win rate | 45.2% |
| Draw rate | 29.4% |
| Away win rate | 25.4% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Villarreal B |
| Champion with most titles | Eldense |
| BTTS rate | 44.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 29.26 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.43 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 36.58 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.95 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 68.71 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 49 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 8.2% vs overall 11.7% (deviation 3.5 pp)
- **4.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 30.6% vs overall 25.4%
- **5.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **6.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **7.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
