# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T02:00:40+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: K League 2 (South Korea)
- Scope: league `korea2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/korea2/database_profile.json | yes | yes | 49.87 |
| matches_analysis | data/analysis/korea2/matches_analysis.json | yes | yes | 21.08 |
| goals_analysis | data/analysis/korea2/goals_analysis.json | yes | yes | 12.25 |
| teams_analysis | data/analysis/korea2/teams_analysis.json | yes | yes | 33.47 |
| season_trends | data/analysis/korea2/season_trends.json | yes | yes | 10.37 |
| scoreline_analysis | data/analysis/korea2/scoreline_analysis.json | yes | yes | 217.22 |
| relationships | data/analysis/korea2/relationships.json | yes | yes | 13.76 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1513 matches: home wins 36.7%, draws 28.6%, away wins 34.6% (556H / 433D / 524A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 30 home and 44 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 301 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1513 matches produced 3866 goals (avg 2.555 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 51.7% vs away 48.3% of 3866 goals in total (home/away ratio 1.07)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 804 of 1513 matches (53.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 364 scoring matches, 26.4% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 35.61, median 32.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Seoul E-Land leads with 333 points across 7 seasons (0 title(s), GD 41)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 7 seasons (Ansan Greeners, Asan, Gyeongnam, Jeonnam, Seoul E-Land)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Asan earns 49 more points at home than away (177 home vs 128 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Gimcheon Sangmu won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2023: Gimcheon Sangmu beat Busan by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.168 per match): first half 2.453 vs last half 2.621 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024 (goals view, avg abs position diff 8.846)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020 (luck view, avg abs position diff 1.400)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 197 matches (13.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (143 of 556 home matches, 25.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (197 of 433 draw matches, 45.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (149 of 524 away matches, 28.4%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 26 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0782 (n=1269 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.686: home 3.191, draw 0.110, away -3.496
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (47)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1513 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1513 |
| Average goals per match | 2.555 |
| Home win rate | 36.7% |
| Draw rate | 28.6% |
| Away win rate | 34.6% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Seoul E-Land |
| Champion with most titles | Gimcheon Sangmu |
| BTTS rate | 53.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.87 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 21.08 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.25 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 33.47 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.37 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 217.22 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.76 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 135 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 173 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 10 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 220 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 11 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 234 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 13 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 234 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 13 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 273 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 14 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 244 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 17 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 home outcome share 31.9% vs overall 36.7%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 away outcome share 42.2% vs overall 34.6%
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021 goalless share 11.0% vs overall 9.0% (deviation 2.0 pp)
- **19.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022 home outcome share 42.3% vs overall 36.7%
- **20.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022 away outcome share 28.2% vs overall 34.6%
- **21.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023 home outcome share 42.3% vs overall 36.7%
- **22.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023 draw outcome share 24.4% vs overall 28.6%
- **23.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 7.0% vs overall 9.0% (deviation 2.0 pp)
- **24.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **25.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **26.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=367, fgte=367 rows)
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=10 positions=1..10 teams=10
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=10 positions=1..10 teams=10
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=10 positions=1..10 teams=10
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=10 positions=1..11 teams=10
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=10 positions=2..19 teams=10
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=10 positions=1..19 teams=10
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=11 positions=1..12 teams=11
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=11 positions=4..21 teams=11
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=11 positions=1..22 teams=11
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=13 positions=1..13 teams=13
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=13 positions=5..22 teams=13
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=13 positions=1..26 teams=13
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=13 positions=1..14 teams=13
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=13 positions=4..22 teams=13
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=13 positions=1..26 teams=13
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=14 positions=1..15 teams=14
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=14 positions=6..22 teams=14
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=14 positions=1..28 teams=14
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=17 positions=1..17 teams=17
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=17 positions=1..17 teams=17
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=17 positions=1..17 teams=17

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
