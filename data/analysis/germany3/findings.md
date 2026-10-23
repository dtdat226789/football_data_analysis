# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:51:32+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 3. Liga (Germany)
- Scope: league `germany3`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\germany3\database_profile.json | yes | yes | 29.60 |
| matches_analysis | E:\football_data_analysis\data\analysis\germany3\matches_analysis.json | yes | yes | 11.92 |
| goals_analysis | E:\football_data_analysis\data\analysis\germany3\goals_analysis.json | yes | yes | 6.25 |
| teams_analysis | E:\football_data_analysis\data\analysis\germany3\teams_analysis.json | yes | yes | 35.61 |
| season_trends | E:\football_data_analysis\data\analysis\germany3\season_trends.json | yes | yes | 3.94 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\germany3\scoreline_analysis.json | yes | yes | 80.78 |
| relationships | E:\football_data_analysis\data\analysis\germany3\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 450 matches: home wins 45.3%, draws 22.9%, away wins 31.8% (204H / 103D / 143A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 19 home and 12 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 125 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 450 matches produced 1448 goals (avg 3.218 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.3% vs away 45.7% of 1448 goals in total (home/away ratio 1.19)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 289 of 450 matches (64.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 143 scoring matches, 33.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.22, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Duisburg leads with 86 points across 2 seasons (1 title(s), GD 29)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 14 teams present in every one of the 2 seasons (Alemannia Aachen, Duisburg, Hansa Rostock, Hoffenheim II, Ingolstadt...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Duisburg earns 26 more points at home than away (56 home vs 30 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — VfL Osnabruck won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Duisburg beat Viktoria Koln by 3 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.063 per match): first half 3.208 vs last half 3.271 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 7.200)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 2.100)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 47 matches (10.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (47 of 204 home matches, 23.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (46 of 103 draw matches, 44.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (27 of 143 away matches, 18.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 22 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_position_before_match |corr| = 0.1155 (n=380 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.47: home 2.771, draw -0.315, away -4.698
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (7)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 450 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 450 |
| Average goals per match | 3.218 |
| Home win rate | 45.3% |
| Draw rate | 22.9% |
| Away win rate | 31.8% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | Duisburg |
| Champion with most titles | VfL Osnabruck |
| BTTS rate | 64.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 29.60 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 11.92 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.25 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 35.61 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.94 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 80.78 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 70 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 2.9% vs overall 5.6% (deviation 2.7 pp)
- **4.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 38.6% vs overall 31.8%
- **5.** `HIGH_SCORING_MATCHES` *(warning)* — 7 match(es) with >= 8 total goals (extreme scorelines)
- **6.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **7.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
