# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:53:24+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 3. Liga (Germany)
- Scope: league `germany3`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/germany3/database_profile.json | yes | yes | 40.30 |
| matches_analysis | data/analysis/germany3/matches_analysis.json | yes | yes | 32.51 |
| goals_analysis | data/analysis/germany3/goals_analysis.json | yes | yes | 12.44 |
| teams_analysis | data/analysis/germany3/teams_analysis.json | yes | yes | 56.80 |
| season_trends | data/analysis/germany3/season_trends.json | yes | yes | 10.49 |
| scoreline_analysis | data/analysis/germany3/scoreline_analysis.json | yes | yes | 368.22 |
| relationships | data/analysis/germany3/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2383 matches: home wins 43.3%, draws 25.3%, away wins 31.4% (1032H / 603D / 748A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 73 home and 62 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 618 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2383 matches produced 6905 goals (avg 2.898 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.0% vs away 46.0% of 6905 goals in total (home/away ratio 1.18)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1373 of 2383 matches (57.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 790 scoring matches, 35.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.40, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Saarbrucken leads with 373 points across 7 seasons (0 title(s), GD 81)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 4 teams present in every one of the 7 seasons (Mannheim, Saarbrucken, Verl, Viktoria Koln)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Mannheim earns 81 more points at home than away (207 home vs 126 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — SG Dynamo Dresden won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2022-2023: Elversberg beat Freiburg II by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.365 per match): first half 2.781 vs last half 3.146 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023-2024 (goals view, avg abs position diff 7.500)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 2.100)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 300 matches (12.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (218 of 1032 home matches, 21.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (300 of 603 draw matches, 49.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (156 of 748 away matches, 20.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 82 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0568 (n=2273 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.843: home 1.804, draw 0.059, away -3.039
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (11)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2383 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2383 |
| Average goals per match | 2.898 |
| Home win rate | 43.3% |
| Draw rate | 25.3% |
| Away win rate | 31.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Saarbrucken |
| Champion with most titles | SG Dynamo Dresden |
| BTTS rate | 57.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 40.30 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 32.51 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.44 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 56.80 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.49 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 368.22 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 373 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 110 matches, expected 380
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **4.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 37.6% vs overall 43.3%
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 7.8% vs overall 6.0% (deviation 1.8 pp)
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 4.2% vs overall 6.0% (deviation 1.8 pp)
- **7.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.327 vs overall 2.898 (deviation 0.429)
- **8.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.6% vs overall 6.0% (deviation 2.4 pp)
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 28 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=328, fgte=328 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
