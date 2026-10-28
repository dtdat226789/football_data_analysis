# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:54:59+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier Division (Ireland)
- Scope: league `ireland1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/ireland1/database_profile.json | yes | yes | 48.59 |
| matches_analysis | data/analysis/ireland1/matches_analysis.json | yes | yes | 20.22 |
| goals_analysis | data/analysis/ireland1/goals_analysis.json | yes | yes | 12.16 |
| teams_analysis | data/analysis/ireland1/teams_analysis.json | yes | yes | 22.95 |
| season_trends | data/analysis/ireland1/season_trends.json | yes | yes | 10.25 |
| scoreline_analysis | data/analysis/ireland1/scoreline_analysis.json | yes | yes | 171.18 |
| relationships | data/analysis/ireland1/relationships.json | yes | yes | 13.73 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1164 matches: home wins 42.9%, draws 27.1%, away wins 30.0% (499H / 316D / 349A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 33 home and 36 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 311 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1164 matches produced 2904 goals (avg 2.495 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.1% vs away 43.9% of 2904 goals in total (home/away ratio 1.28)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 587 of 1164 matches (50.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 322 scoring matches, 30.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.76, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Shamrock Rovers leads with 472 points across 7 seasons (6 title(s), GD 208)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 7 seasons (Bohemians, Derry City, Shamrock Rovers, Sligo Rovers, St. Patricks)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Shamrock Rovers earns 74 more points at home than away (273 home vs 199 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Shamrock Rovers won 6 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2024: Shelbourne beat Shamrock Rovers by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.075 per match): first half 2.416 vs last half 2.491 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022 (goals view, avg abs position diff 4.400)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020 (goals view, avg abs position diff 2.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 153 matches (13.1%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (129 of 499 home matches, 25.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (153 of 316 draw matches, 48.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (104 of 349 away matches, 29.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 13 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_position_before_match |corr| = 0.1493 (n=989 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 8.921: home 3.694, draw -1.015, away -5.227
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (44)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1164 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1164 |
| Average goals per match | 2.495 |
| Home win rate | 42.9% |
| Draw rate | 27.1% |
| Away win rate | 30.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Shamrock Rovers |
| Champion with most titles | Shamrock Rovers |
| BTTS rate | 50.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 48.59 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 20.22 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.16 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 22.95 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.25 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 171.18 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.73 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 90 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 180 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 10 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 179 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 10 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 180 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 10 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 180 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 10 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 180 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 10 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 175 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020 goalless share 11.1% vs overall 8.2% (deviation 2.9 pp)
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 draw outcome share 21.1% vs overall 27.1%
- **18.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 away outcome share 34.4% vs overall 30.0%
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021 goalless share 2.2% vs overall 8.2% (deviation 6.0 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024 goalless share 12.2% vs overall 8.2% (deviation 4.0 pp)
- **21.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **22.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **23.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=346, fgte=346 rows)
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=10 positions=1..10 teams=10
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=10 positions=1..10 teams=10
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=10 positions=1..10 teams=10
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=10 positions=1..10 teams=10
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=10 positions=1..10 teams=10
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=10 positions=1..10 teams=10
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=10 positions=1..10 teams=10
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=10 positions=1..10 teams=10
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=10 positions=1..10 teams=10
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=10 positions=1..10 teams=10
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=10 positions=1..10 teams=10
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=10 positions=1..10 teams=10
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=10 positions=1..10 teams=10
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=10 positions=1..10 teams=10
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=10 positions=1..10 teams=10
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=10 positions=1..10 teams=10
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=10 positions=1..10 teams=10
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=10 positions=1..10 teams=10
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
