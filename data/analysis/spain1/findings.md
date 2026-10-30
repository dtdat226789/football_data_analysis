# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T04:13:30+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: LaLiga (Spain)
- Scope: league `spain1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/spain1/database_profile.json | yes | yes | 39.87 |
| matches_analysis | data/analysis/spain1/matches_analysis.json | yes | yes | 27.22 |
| goals_analysis | data/analysis/spain1/goals_analysis.json | yes | yes | 12.35 |
| teams_analysis | data/analysis/spain1/teams_analysis.json | yes | yes | 41.28 |
| season_trends | data/analysis/spain1/season_trends.json | yes | yes | 10.48 |
| scoreline_analysis | data/analysis/spain1/scoreline_analysis.json | yes | yes | 356.71 |
| relationships | data/analysis/spain1/relationships.json | yes | yes | 13.79 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2380 matches: home wins 45.0%, draws 26.6%, away wins 28.4% (1071H / 634D / 675A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 52 home and 55 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 621 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2380 matches produced 6181 goals (avg 2.597 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.5% vs away 43.5% of 6181 goals in total (home/away ratio 1.30)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1240 of 2380 matches (52.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 695 scoring matches, 31.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.08, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Real Madrid leads with 537 points across 7 seasons (2 title(s), GD 285)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 7 seasons (Ath Bilbao, Atl. Madrid, Barcelona, Betis, Celta Vigo...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Atl. Madrid earns 90 more points at home than away (285 home vs 195 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Barcelona won 4 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: Atl. Madrid beat Real Madrid by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.256 per match): first half 2.508 vs last half 2.764 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022-2023 (goals view, avg abs position diff 7.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2023-2024 (luck view, avg abs position diff 2.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 327 matches (13.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (290 of 1071 home matches, 27.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (327 of 634 draw matches, 51.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (184 of 675 away matches, 27.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 55 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.1141 (n=2280 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 10.388: home 4.323, draw -1.469, away -6.065
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (10)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2380 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2380 |
| Average goals per match | 2.597 |
| Home win rate | 45.0% |
| Draw rate | 26.6% |
| Away win rate | 28.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Real Madrid |
| Champion with most titles | Barcelona |
| BTTS rate | 52.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 39.87 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 27.22 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.35 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 41.28 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.48 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 356.71 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.79 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 100 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 11.3% vs overall 7.4% (deviation 3.9 pp)
- **4.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 5.5% vs overall 7.4% (deviation 1.9 pp)
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 3.9% vs overall 7.4% (deviation 3.5 pp)
- **6.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 2.98 vs overall 2.597 (deviation 0.383)
- **7.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 10.0% vs overall 7.4% (deviation 2.6 pp)
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 12 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=439, fgte=439 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
