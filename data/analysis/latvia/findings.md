# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T02:01:44+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Virsliga (Latvia)
- Scope: league `latvia`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/latvia/database_profile.json | yes | yes | 45.70 |
| matches_analysis | data/analysis/latvia/matches_analysis.json | yes | yes | 14.69 |
| goals_analysis | data/analysis/latvia/goals_analysis.json | yes | yes | 11.06 |
| teams_analysis | data/analysis/latvia/teams_analysis.json | yes | yes | 25.50 |
| season_trends | data/analysis/latvia/season_trends.json | yes | yes | 8.85 |
| scoreline_analysis | data/analysis/latvia/scoreline_analysis.json | yes | yes | 169.39 |
| relationships | data/analysis/latvia/relationships.json | yes | yes | 13.69 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1023 matches: home wins 43.8%, draws 20.4%, away wins 35.8% (448H / 209D / 366A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 23 home and 18 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 291 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1023 matches produced 3033 goals (avg 2.965 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.2% vs away 45.8% of 3033 goals in total (home/away ratio 1.18)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 501 of 1023 matches (49.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 332 scoring matches, 35.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.40, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — RFS leads with 498 points across 6 seasons (4 title(s), GD 372)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 4 teams present in every one of the 6 seasons (BFC Daugavpils, FK Liepaja, RFS, Riga FC)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — BFC Daugavpils earns 62 more points at home than away (154 home vs 92 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — RFS won 4 of 6 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2023: RFS beat Riga FC by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.003 per match): first half 2.963 vs last half 2.966 across 6 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2023 (goals view, avg abs position diff 4.545)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2021 (luck view, avg abs position diff 0.889)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 102 matches (10.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (80 of 448 home matches, 17.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (102 of 209 draw matches, 48.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (87 of 366 away matches, 23.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 42 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.0742 (n=854 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 21.178: home 9.630, draw -1.491, away -11.547
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (37)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 6 of 6 registered seasons populated (100.0%); 1023 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1023 |
| Average goals per match | 2.965 |
| Home win rate | 43.8% |
| Draw rate | 20.4% |
| Away win rate | 35.8% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | RFS |
| Champion with most titles | RFS |
| BTTS rate | 49.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 45.70 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 14.69 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 11.06 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 25.50 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 8.85 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 169.39 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.69 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 126 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 9 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 182 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 11 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 182 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 11 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 182 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 11 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 182 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 11 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 169 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **13.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **14.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021 goalless share 3.2% vs overall 5.9% (deviation 2.7 pp)
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021 draw outcome share 15.9% vs overall 20.4%
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025 away outcome share 30.8% vs overall 35.8%
- **17.** `HIGH_SCORING_MATCHES` *(warning)* — 11 match(es) with >= 8 total goals (extreme scorelines)
- **18.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **19.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=385, fgte=385 rows)
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=9 positions=1..9 teams=9
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=9 positions=1..9 teams=9
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=9 positions=1..9 teams=9
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=11 positions=1..11 teams=11
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=11 positions=1..11 teams=11
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=11 positions=1..11 teams=11
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=11 positions=1..11 teams=11
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=11 positions=1..11 teams=11
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=11 positions=1..11 teams=11
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=11 positions=1..11 teams=11
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=11 positions=1..11 teams=11
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=11 positions=1..11 teams=11
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=11 positions=1..11 teams=11
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=11 positions=1..11 teams=11
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=11 positions=1..11 teams=11
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
