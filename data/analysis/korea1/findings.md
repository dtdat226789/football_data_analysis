# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:02:53+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: K League 1 (South Korea)
- Scope: league `korea1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\korea1\database_profile.json | yes | yes | 32.07 |
| matches_analysis | E:\football_data_analysis\data\analysis\korea1\matches_analysis.json | yes | yes | 9.00 |
| goals_analysis | E:\football_data_analysis\data\analysis\korea1\goals_analysis.json | yes | yes | 6.20 |
| teams_analysis | E:\football_data_analysis\data\analysis\korea1\teams_analysis.json | yes | yes | 22.98 |
| season_trends | E:\football_data_analysis\data\analysis\korea1\season_trends.json | yes | yes | 3.89 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\korea1\scoreline_analysis.json | yes | yes | 59.73 |
| relationships | E:\football_data_analysis\data\analysis\korea1\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 377 matches: home wins 36.3%, draws 29.7%, away wins 34.0% (137H / 112D / 128A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 12 home and 4 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — level at HT -> draw occurred 74 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 377 matches produced 952 goals (avg 2.525 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 50.8% vs away 49.2% of 952 goals in total (home/away ratio 1.03)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 207 of 377 matches (54.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 92 scoring matches, 27.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 35.26, median 32.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Jeonbuk leads with 115 points across 2 seasons (1 title(s), GD 40)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 10 teams present in every one of the 2 seasons (Anyang, Daejeon, Gangwon, Gimcheon Sangmu, Gwangju FC...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Suwon FC earns 12 more points at home than away (25 home vs 13 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Jeonbuk won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026: Seoul beat Ulsan HD by 15 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.128 per match): first half 2.586 vs last half 2.458 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026 (goals view, avg abs position diff 4.167)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 1.667)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 54 matches (14.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (33 of 137 home matches, 24.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (54 of 112 draw matches, 48.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (38 of 128 away matches, 29.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 5 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.1314 (n=377 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 4.731: home 23.270, draw 19.321, away 18.539
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 377 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 377 |
| Average goals per match | 2.525 |
| Home win rate | 36.3% |
| Draw rate | 29.7% |
| Away win rate | 34.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Jeonbuk |
| Champion with most titles | Jeonbuk |
| BTTS rate | 54.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.07 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.00 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.20 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 22.98 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.89 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 59.73 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 198 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 179 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 12 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025 home outcome share 41.9% vs overall 36.3%
- **7.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 11.2% vs overall 9.5% (deviation 1.7 pp)
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 home outcome share 30.2% vs overall 36.3%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=12 positions=1..12 teams=12
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=12 positions=1..12 teams=12
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=12 positions=1..12 teams=12
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=12 positions=1..12 teams=12
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=12 positions=1..12 teams=12
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
