# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T01:59:14+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Veikkausliiga (Finland)
- Scope: league `finland1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/finland1/database_profile.json | yes | yes | 49.41 |
| matches_analysis | data/analysis/finland1/matches_analysis.json | yes | yes | 17.90 |
| goals_analysis | data/analysis/finland1/goals_analysis.json | yes | yes | 12.22 |
| teams_analysis | data/analysis/finland1/teams_analysis.json | yes | yes | 26.57 |
| season_trends | data/analysis/finland1/season_trends.json | yes | yes | 10.16 |
| scoreline_analysis | data/analysis/finland1/scoreline_analysis.json | yes | yes | 147.93 |
| relationships | data/analysis/finland1/relationships.json | yes | yes | 13.72 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 945 matches: home wins 42.8%, draws 23.8%, away wins 33.4% (404H / 225D / 316A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 34 home and 25 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 244 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 945 matches produced 2616 goals (avg 2.768 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.1% vs away 46.9% of 2616 goals in total (home/away ratio 1.13)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 499 of 945 matches (52.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 292 scoring matches, 33.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.08, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — HJK leads with 329 points across 7 seasons (3 title(s), GD 163)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 6 teams present in every one of the 7 seasons (HJK, Ilves, Inter Turku, KuPS, Mariehamn...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Ilves earns 49 more points at home than away (136 home vs 87 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — HJK won 3 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2021: KuPS beat HJK by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.255 per match): first half 2.692 vs last half 2.947 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026 (goals view, avg abs position diff 4.667)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2022 (luck view, avg abs position diff 1.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 107 matches (11.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (86 of 404 home matches, 21.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (107 of 225 draw matches, 47.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (79 of 316 away matches, 25.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 18 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_rest_days |corr| = 0.0791 (n=756 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.859: home 2.848, draw -0.541, away -4.011
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (47)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 945 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 945 |
| Average goals per match | 2.768 |
| Home win rate | 42.8% |
| Draw rate | 23.8% |
| Away win rate | 33.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | HJK |
| Champion with most titles | HJK |
| BTTS rate | 52.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.41 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 17.90 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.22 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 26.57 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.16 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 147.93 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.72 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 132 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 132 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 12 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 132 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 12 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 132 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 12 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 132 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 12 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 132 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 12 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 153 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 12 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2021 avg goals 2.348 vs overall 2.768 (deviation 0.420)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021 draw outcome share 18.9% vs overall 23.8%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2021 away outcome share 37.9% vs overall 33.4%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022 goalless share 4.5% vs overall 6.6% (deviation 2.1 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023 goalless share 8.3% vs overall 6.6% (deviation 1.7 pp)
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024 home outcome share 47.0% vs overall 42.8%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024 away outcome share 28.0% vs overall 33.4%
- **23.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2025 avg goals 3.28 vs overall 2.768 (deviation 0.512)
- **24.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **25.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **26.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=313, fgte=313 rows)
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=12 positions=1..12 teams=12
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=12 positions=1..12 teams=12
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=12 positions=1..12 teams=12
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=12 positions=1..12 teams=12
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=12 positions=1..12 teams=12
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=12 positions=1..12 teams=12
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=12 positions=1..12 teams=12
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=12 positions=1..12 teams=12
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=12 positions=1..12 teams=12
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=12 positions=1..12 teams=12
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=12 positions=1..12 teams=12
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=12 positions=1..12 teams=12
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=12 positions=1..12 teams=12
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=12 positions=1..12 teams=12
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=12 positions=1..12 teams=12
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=12 positions=1..12 teams=12
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=12 positions=1..12 teams=12
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=12 positions=1..12 teams=12
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=12 positions=1..12 teams=12
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=12 positions=1..12 teams=12
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
