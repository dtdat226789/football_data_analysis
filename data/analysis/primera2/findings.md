# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:44:30+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/primera2/database_profile.json | yes | yes | 37.93 |
| matches_analysis | data/analysis/primera2/matches_analysis.json | yes | yes | 20.14 |
| goals_analysis | data/analysis/primera2/goals_analysis.json | yes | yes | 11.11 |
| teams_analysis | data/analysis/primera2/teams_analysis.json | yes | yes | 69.07 |
| season_trends | data/analysis/primera2/season_trends.json | yes | yes | 9.12 |
| scoreline_analysis | data/analysis/primera2/scoreline_analysis.json | yes | yes | 281.74 |
| relationships | data/analysis/primera2/relationships.json | yes | yes | 13.79 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1985 matches: home wins 44.4%, draws 29.9%, away wins 25.7% (882H / 593D / 510A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 42 home and 27 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 520 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1985 matches produced 4568 goals (avg 2.301 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 58.1% vs away 41.9% of 4568 goals in total (home/away ratio 1.38)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 911 of 1985 matches (45.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 521 scoring matches, 29.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.88, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Murcia leads with 246 points across 5 seasons (0 title(s), GD 38)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 0 teams present in every one of the 6 seasons
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Gimnastic earns 58 more points at home than away (115 home vs 57 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Eldense won 2 of 6 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2022-2023: Eldense beat Amorebieta by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.144 per match): first half 2.269 vs last half 2.414 across 6 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022-2023 (goals view, avg abs position diff 6.700)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2023-2024 (luck view, avg abs position diff 2.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 277 matches (14.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (277 of 882 home matches, 31.4%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (259 of 593 draw matches, 43.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (175 of 510 away matches, 34.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 22 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.067 (n=1900 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.195: home 1.394, draw -0.596, away -2.800
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (11)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 6 of 6 registered seasons populated (100.0%); 1985 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1985 |
| Average goals per match | 2.301 |
| Home win rate | 44.4% |
| Draw rate | 29.9% |
| Away win rate | 25.7% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Murcia |
| Champion with most titles | Eldense |
| BTTS rate | 45.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 37.93 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 20.14 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 11.11 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 69.07 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 9.12 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 281.74 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.79 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 85 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 9.7% vs overall 11.5% (deviation 1.8 pp)
- **4.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021-2022 draw outcome share 25.3% vs overall 29.9%
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 13.9% vs overall 11.5% (deviation 2.4 pp)
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 draw outcome share 25.5% vs overall 29.9%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 draw outcome share 34.7% vs overall 29.9%
- **8.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 7.1% vs overall 11.5% (deviation 4.4 pp)
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=413, fgte=413 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
