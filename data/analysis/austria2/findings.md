# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:44:32+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 2. Liga (Austria)
- Scope: league `austria2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\austria2\database_profile.json | yes | yes | 32.44 |
| matches_analysis | E:\football_data_analysis\data\analysis\austria2\matches_analysis.json | yes | yes | 8.22 |
| goals_analysis | E:\football_data_analysis\data\analysis\austria2\goals_analysis.json | yes | yes | 6.23 |
| teams_analysis | E:\football_data_analysis\data\analysis\austria2\teams_analysis.json | yes | yes | 28.38 |
| season_trends | E:\football_data_analysis\data\analysis\austria2\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\austria2\scoreline_analysis.json | yes | yes | 51.14 |
| relationships | E:\football_data_analysis\data\analysis\austria2\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 279 matches: home wins 43.4%, draws 23.7%, away wins 33.0% (121H / 66D / 92A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 7 home and 4 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 80 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 279 matches produced 784 goals (avg 2.810 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.2% vs away 45.8% of 784 goals in total (home/away ratio 1.18)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 143 of 279 matches (51.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 95 scoring matches, 36.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.59, median 22.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — St. Polten leads with 65 points across 2 seasons (1 title(s), GD 20)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (A. Salzburg, Admira, Amstetten, Austria Vienna (Am), Bregenz...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — St. Polten earns 17 more points at home than away (41 home vs 24 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — St. Polten won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: St. Polten beat A. Lustenau by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.618 per match): first half 2.686 vs last half 3.304 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.875)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.125)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 28 matches (10.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (25 of 121 home matches, 20.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (28 of 66 draw matches, 42.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-2 (23 of 92 away matches, 25.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 8 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_win_rate |corr| = -0.1769 (n=223 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 4.805: home 21.685, draw 16.879, away 17.247
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (18)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 279 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 279 |
| Average goals per match | 2.81 |
| Home win rate | 43.4% |
| Draw rate | 23.7% |
| Away win rate | 33.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | St. Polten |
| Champion with most titles | St. Polten |
| BTTS rate | 51.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.44 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.22 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.23 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 28.38 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 51.14 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 223 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 56 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.304 vs overall 2.81 (deviation 0.494)
- **7.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 1.8% vs overall 6.8% (deviation 5.0 pp)
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 51.8% vs overall 43.4%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 14.3% vs overall 23.7%
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **11.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **12.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=1, fgte=1 rows)
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=16 positions=1..16 teams=16
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=16 positions=1..16 teams=16
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=16 positions=1..16 teams=16
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
