# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:04:52+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie A (Italy)
- Scope: league `italy1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/italy1/database_profile.json | yes | yes | 40.23 |
| matches_analysis | data/analysis/italy1/matches_analysis.json | yes | yes | 29.13 |
| goals_analysis | data/analysis/italy1/goals_analysis.json | yes | yes | 12.42 |
| teams_analysis | data/analysis/italy1/teams_analysis.json | yes | yes | 38.84 |
| season_trends | data/analysis/italy1/season_trends.json | yes | yes | 10.40 |
| scoreline_analysis | data/analysis/italy1/scoreline_analysis.json | yes | yes | 353.67 |
| relationships | data/analysis/italy1/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2363 matches: home wins 40.7%, draws 26.5%, away wins 32.8% (962H / 627D / 774A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 63 home and 57 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 566 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2363 matches produced 6372 goals (avg 2.697 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.4% vs away 46.6% of 6372 goals in total (home/away ratio 1.15)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1251 of 2363 matches (52.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 727 scoring matches, 33.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.04, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Inter leads with 531 points across 7 seasons (3 title(s), GD 313)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 11 teams present in every one of the 7 seasons (AC Milan, AS Roma, Atalanta, Bologna, Fiorentina...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — AS Roma earns 88 more points at home than away (251 home vs 163 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Inter won 3 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2024-2025: Napoli beat Inter by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.128 per match): first half 2.83 vs last half 2.702 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021-2022 (goals view, avg abs position diff 6.700)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.100)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 297 matches (12.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (228 of 962 home matches, 23.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (297 of 627 draw matches, 47.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (186 of 774 away matches, 24.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 49 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.0725 (n=2280 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 13.045: home 5.543, draw 0.259, away -7.503
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (13)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2363 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2363 |
| Average goals per match | 2.697 |
| Home win rate | 40.7% |
| Draw rate | 26.5% |
| Away win rate | 32.8% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Inter |
| Champion with most titles | Inter |
| BTTS rate | 52.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 40.23 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 29.13 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.42 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 38.84 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.40 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 353.67 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 83 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2020-2021 avg goals 3.061 vs overall 2.697 (deviation 0.364)
- **4.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 5.0% vs overall 6.6% (deviation 1.6 pp)
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 away outcome share 28.7% vs overall 32.8%
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 9.5% vs overall 6.6% (deviation 2.9 pp)
- **7.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.12 vs overall 2.697 (deviation 0.423)
- **8.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 1.2% vs overall 6.6% (deviation 5.4 pp)
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 47.0% vs overall 40.7%
- **10.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 16.9% vs overall 26.5%
- **11.** `HIGH_SCORING_MATCHES` *(warning)* — 11 match(es) with >= 8 total goals (extreme scorelines)
- **12.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **13.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=349, fgte=349 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
