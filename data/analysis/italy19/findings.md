# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:05:10+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Primavera 1 (Italy)
- Scope: league `italy19`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/italy19/database_profile.json | yes | yes | 46.80 |
| matches_analysis | data/analysis/italy19/matches_analysis.json | yes | yes | 24.81 |
| goals_analysis | data/analysis/italy19/goals_analysis.json | yes | yes | 12.34 |
| teams_analysis | data/analysis/italy19/teams_analysis.json | yes | yes | 59.92 |
| season_trends | data/analysis/italy19/season_trends.json | yes | yes | 10.53 |
| scoreline_analysis | data/analysis/italy19/scoreline_analysis.json | yes | yes | 310.28 |
| relationships | data/analysis/italy19/relationships.json | yes | yes | 13.79 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2000 matches: home wins 42.9%, draws 25.6%, away wins 31.4% (858H / 513D / 629A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 41 home and 50 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 518 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2000 matches produced 5992 goals (avg 2.996 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.9% vs away 45.1% of 5992 goals in total (home/away ratio 1.22)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1203 of 2000 matches (60.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 708 scoring matches, 37.4% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.49, median 22.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — AS Roma U19 leads with 246 points across 4 seasons (1 title(s), GD 102)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 0 teams present in every one of the 7 seasons
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Sassuolo U19 earns 47 more points at home than away (125 home vs 78 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Sampdoria U19 won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020-2021: Sampdoria U19 beat Juventus U19 by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.038 per match): first half 3.0 vs last half 3.038 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023-2024 (goals view, avg abs position diff 6.667)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020-2021 (luck view, avg abs position diff 1.750)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 247 matches (12.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (179 of 858 home matches, 20.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (247 of 513 draw matches, 48.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (154 of 629 away matches, 24.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 75 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.0969 (n=1920 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.092: home 2.654, draw -0.811, away -3.438
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (33)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2000 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2000 |
| Average goals per match | 2.996 |
| Home win rate | 42.9% |
| Draw rate | 25.6% |
| Away win rate | 31.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | AS Roma U19 |
| Champion with most titles | Sampdoria U19 |
| BTTS rate | 60.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 46.80 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 24.81 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 59.92 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.53 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 310.28 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.79 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020-2021 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 306 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021-2022 has 18 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 306 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022-2023 has 18 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 382 matches, expected 380
- **10.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 80 matches, expected 380
- **11.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **12.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023-2024 away outcome share 27.1% vs overall 31.4%
- **13.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 away outcome share 35.8% vs overall 31.4%
- **14.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 7.6% vs overall 4.8% (deviation 2.8 pp)
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 draw outcome share 30.6% vs overall 25.6%
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 2.5% vs overall 4.8% (deviation 2.3 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 36.2% vs overall 42.9%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 33.8% vs overall 25.6%
- **19.** `HIGH_SCORING_MATCHES` *(warning)* — 23 match(es) with >= 8 total goals (extreme scorelines)
- **20.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **21.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=360, fgte=360 rows)
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/classic rows=16 positions=1..16 teams=16
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/goals rows=16 positions=1..16 teams=16
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020-2021/luck rows=16 positions=1..16 teams=16
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/classic rows=18 positions=1..18 teams=18
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/goals rows=18 positions=1..18 teams=18
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021-2022/luck rows=18 positions=1..18 teams=18
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/classic rows=18 positions=1..18 teams=18
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/goals rows=18 positions=1..18 teams=18
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022-2023/luck rows=18 positions=1..18 teams=18
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..18 teams=18
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..18 teams=18
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
