# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T02:22:43+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: TOPLYGA (Lithuania)
- Scope: league `lithuania`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/lithuania/database_profile.json | yes | yes | 48.78 |
| matches_analysis | data/analysis/lithuania/matches_analysis.json | yes | yes | 15.36 |
| goals_analysis | data/analysis/lithuania/goals_analysis.json | yes | yes | 12.07 |
| teams_analysis | data/analysis/lithuania/teams_analysis.json | yes | yes | 22.98 |
| season_trends | data/analysis/lithuania/season_trends.json | yes | yes | 10.22 |
| scoreline_analysis | data/analysis/lithuania/scoreline_analysis.json | yes | yes | 165.90 |
| relationships | data/analysis/lithuania/relationships.json | yes | yes | 13.71 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1112 matches: home wins 40.1%, draws 26.2%, away wins 33.7% (446H / 291D / 375A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 26 home and 15 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 279 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1112 matches produced 2858 goals (avg 2.570 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.4% vs away 46.6% of 2858 goals in total (home/away ratio 1.15)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 517 of 1112 matches (46.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 307 scoring matches, 30.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.13, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Zalgiris leads with 478 points across 7 seasons (4 title(s), GD 246)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 7 seasons (Banga, FK Panevezys, Kauno Zalgiris, Suduva, Zalgiris)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Suduva earns 49 more points at home than away (203 home vs 154 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Zalgiris won 4 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2020: Zalgiris beat Suduva by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.094 per match): first half 2.652 vs last half 2.558 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021 (goals view, avg abs position diff 4.200)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020 (luck view, avg abs position diff 0.667)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 126 matches (11.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (97 of 446 home matches, 21.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (126 of 291 draw matches, 43.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (113 of 375 away matches, 30.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 12 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.0802 (n=960 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 14.117: home 6.172, draw -0.257, away -7.945
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (45)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1112 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1112 |
| Average goals per match | 2.57 |
| Home win rate | 40.1% |
| Draw rate | 26.2% |
| Away win rate | 33.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Zalgiris |
| Champion with most titles | Zalgiris |
| BTTS rate | 46.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 48.78 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 15.36 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.07 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 22.98 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.22 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 165.90 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.71 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 60 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 6 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 180 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 10 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 180 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 10 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 180 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 10 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 180 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 10 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 180 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 10 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 152 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020 goalless share 3.3% vs overall 9.1% (deviation 5.8 pp)
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021 goalless share 5.6% vs overall 9.1% (deviation 3.5 pp)
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023 goalless share 11.7% vs overall 9.1% (deviation 2.6 pp)
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024 goalless share 12.8% vs overall 9.1% (deviation 3.7 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025 goalless share 7.2% vs overall 9.1% (deviation 1.9 pp)
- **21.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 11.2% vs overall 9.1% (deviation 2.1 pp)
- **22.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **23.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **24.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=388, fgte=388 rows)
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=6 positions=1..6 teams=6
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=6 positions=1..6 teams=6
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=6 positions=1..6 teams=6
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=10 positions=1..10 teams=10
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=10 positions=1..10 teams=10
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=10 positions=1..10 teams=10
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=10 positions=1..10 teams=10
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=10 positions=1..10 teams=10
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=10 positions=1..10 teams=10
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=10 positions=1..10 teams=10
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=10 positions=1..10 teams=10
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=10 positions=1..10 teams=10
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=10 positions=1..10 teams=10
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=10 positions=1..10 teams=10
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=10 positions=1..10 teams=10
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=10 positions=1..10 teams=10
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=10 positions=1..10 teams=10
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=10 positions=1..10 teams=10
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **45.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
