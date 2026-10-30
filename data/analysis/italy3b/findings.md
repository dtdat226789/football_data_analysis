# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:59:42+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie C - Group B (Italy)
- Scope: league `italy3b`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/italy3b/database_profile.json | yes | yes | 40.03 |
| matches_analysis | data/analysis/italy3b/matches_analysis.json | yes | yes | 24.65 |
| goals_analysis | data/analysis/italy3b/goals_analysis.json | yes | yes | 12.37 |
| teams_analysis | data/analysis/italy3b/teams_analysis.json | yes | yes | 68.74 |
| season_trends | data/analysis/italy3b/season_trends.json | yes | yes | 10.43 |
| scoreline_analysis | data/analysis/italy3b/scoreline_analysis.json | yes | yes | 330.27 |
| relationships | data/analysis/italy3b/relationships.json | yes | yes | 13.79 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2368 matches: home wins 40.5%, draws 30.5%, away wins 29.0% (958H / 723D / 687A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 47 home and 46 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 571 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2368 matches produced 5603 goals (avg 2.366 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.3% vs away 44.7% of 5603 goals in total (home/away ratio 1.24)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1151 of 2368 matches (48.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 636 scoring matches, 30.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.85, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Gubbio leads with 326 points across 7 seasons (0 title(s), GD 11)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 2 teams present in every one of the 7 seasons (Gubbio, Vis Pesaro)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Carrarese earns 70 more points at home than away (125 home vs 55 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Padova won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: Padova beat Perugia by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.004 per match): first half 2.376 vs last half 2.38 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 7.800)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020-2021 (luck view, avg abs position diff 1.100)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 341 matches (14.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (258 of 958 home matches, 26.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (341 of 723 draw matches, 47.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (217 of 687 away matches, 31.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 17 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_rest_days |corr| = 0.0499 (n=2197 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 8.433: home 3.655, draw -0.779, away -4.778
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (12)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2368 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2368 |
| Average goals per match | 2.366 |
| Home win rate | 40.5% |
| Draw rate | 30.5% |
| Away win rate | 29.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Gubbio |
| Champion with most titles | Padova |
| BTTS rate | 48.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 40.03 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 24.65 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.37 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 68.74 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.43 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 330.27 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.79 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 357 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 111 matches, expected 380
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **4.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 12.9% vs overall 10.7% (deviation 2.2 pp)
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 away outcome share 24.7% vs overall 29.0%
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 home outcome share 35.5% vs overall 40.5%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 home outcome share 45.3% vs overall 40.5%
- **8.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 8.1% vs overall 10.7% (deviation 2.6 pp)
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 45.9% vs overall 40.5%
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **11.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **12.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=365, fgte=365 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
