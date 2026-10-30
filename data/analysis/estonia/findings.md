# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:50:28+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Meistriliiga (Estonia)
- Scope: league `estonia`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/estonia/database_profile.json | yes | yes | 52.71 |
| matches_analysis | data/analysis/estonia/matches_analysis.json | yes | yes | 17.93 |
| goals_analysis | data/analysis/estonia/goals_analysis.json | yes | yes | 12.30 |
| teams_analysis | data/analysis/estonia/teams_analysis.json | yes | yes | 21.72 |
| season_trends | data/analysis/estonia/season_trends.json | yes | yes | 10.14 |
| scoreline_analysis | data/analysis/estonia/scoreline_analysis.json | yes | yes | 196.62 |
| relationships | data/analysis/estonia/relationships.json | yes | yes | 13.75 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1171 matches: home wins 43.3%, draws 18.8%, away wins 37.9% (507H / 220D / 444A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 32 home and 25 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 328 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1171 matches produced 3540 goals (avg 3.023 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.6% vs away 46.4% of 3540 goals in total (home/away ratio 1.16)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 606 of 1171 matches (51.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 391 scoring matches, 35.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.97, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Levadia leads with 533 points across 7 seasons (3 title(s), GD 346)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 7 teams present in every one of the 7 seasons (Flora, Kalju, Kuressaare, Levadia, Narva...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Kuressaare earns 29 more points at home than away (136 home vs 107 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Flora won 4 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2023: Flora beat Levadia by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.064 per match): first half 3.151 vs last half 3.087 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022 (goals view, avg abs position diff 4.200)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2024 (luck view, avg abs position diff 1.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 103 matches (8.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (94 of 507 home matches, 18.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (103 of 220 draw matches, 46.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (98 of 444 away matches, 22.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 47 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.056 (n=1001 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 18.448: home 8.713, draw -0.447, away -9.735
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (53)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1171 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1171 |
| Average goals per match | 3.023 |
| Home win rate | 43.3% |
| Draw rate | 18.8% |
| Away win rate | 37.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Levadia |
| Champion with most titles | Flora |
| BTTS rate | 51.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 52.71 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 17.93 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.30 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 21.72 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.14 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 196.62 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.75 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 147 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 134 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 10 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 180 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 10 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 180 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 10 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 180 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 10 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 180 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 10 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 170 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020 goalless share 6.8% vs overall 4.9% (deviation 1.9 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 home outcome share 38.1% vs overall 43.3%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 away outcome share 42.9% vs overall 37.9%
- **19.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2021 avg goals 3.396 vs overall 3.023 (deviation 0.373)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022 goalless share 3.3% vs overall 4.9% (deviation 1.6 pp)
- **21.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2023 avg goals 2.544 vs overall 3.023 (deviation 0.479)
- **22.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023 goalless share 9.4% vs overall 4.9% (deviation 4.5 pp)
- **23.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023 home outcome share 37.2% vs overall 43.3%
- **24.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2023 draw outcome share 27.8% vs overall 18.8%
- **25.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025 goalless share 2.2% vs overall 4.9% (deviation 2.7 pp)
- **26.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025 draw outcome share 13.3% vs overall 18.8%
- **27.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 2.9% vs overall 4.9% (deviation 2.0 pp)
- **28.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 home outcome share 48.2% vs overall 43.3%
- **29.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 draw outcome share 12.4% vs overall 18.8%
- **30.** `HIGH_SCORING_MATCHES` *(warning)* — 25 match(es) with >= 8 total goals (extreme scorelines)
- **31.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **32.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=312, fgte=312 rows)
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=10 positions=1..10 teams=10
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=10 positions=1..10 teams=10
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=10 positions=1..10 teams=10
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=10 positions=1..10 teams=10
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=10 positions=1..10 teams=10
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=10 positions=1..10 teams=10
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=10 positions=1..10 teams=10
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=10 positions=1..10 teams=10
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=10 positions=1..10 teams=10
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=10 positions=1..10 teams=10
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=10 positions=1..10 teams=10
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=10 positions=1..10 teams=10
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=10 positions=1..10 teams=10
- **46.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=10 positions=1..10 teams=10
- **47.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=10 positions=1..10 teams=10
- **48.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=10 positions=1..10 teams=10
- **49.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=10 positions=1..10 teams=10
- **50.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=10 positions=1..10 teams=10
- **51.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **52.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **53.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
