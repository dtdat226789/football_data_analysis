# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:17:40+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Superettan (Sweden)
- Scope: league `sweden2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/sweden2/database_profile.json | yes | yes | 47.05 |
| matches_analysis | data/analysis/sweden2/matches_analysis.json | yes | yes | 24.03 |
| goals_analysis | data/analysis/sweden2/goals_analysis.json | yes | yes | 12.17 |
| teams_analysis | data/analysis/sweden2/teams_analysis.json | yes | yes | 42.53 |
| season_trends | data/analysis/sweden2/season_trends.json | yes | yes | 10.24 |
| scoreline_analysis | data/analysis/sweden2/scoreline_analysis.json | yes | yes | 243.92 |
| relationships | data/analysis/sweden2/relationships.json | yes | yes | 13.77 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 1664 matches: home wins 43.6%, draws 26.9%, away wins 29.5% (726H / 447D / 491A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 57 home and 35 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 428 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 1664 matches produced 4602 goals (avg 2.766 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.6% vs away 44.4% of 4602 goals in total (home/away ratio 1.25)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 926 of 1664 matches (55.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 527 scoring matches, 34.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.24, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Oster leads with 295 points across 6 seasons (0 title(s), GD 71)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 1 teams present in every one of the 7 seasons (Brage)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Ostersund earns 59 more points at home than away (124 home vs 65 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Vasteras SK won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2024: Degerfors beat Oster by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.089 per match): first half 2.717 vs last half 2.805 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021 (goals view, avg abs position diff 5.750)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2020 (luck view, avg abs position diff 1.750)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 193 matches (11.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (156 of 726 home matches, 21.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (193 of 447 draw matches, 43.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (126 of 491 away matches, 25.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 31 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0803 (n=1440 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 3.39: home 1.378, draw -1.207, away -2.012
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (39)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 1664 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 1664 |
| Average goals per match | 2.766 |
| Home win rate | 43.6% |
| Draw rate | 26.9% |
| Away win rate | 29.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Oster |
| Champion with most titles | Vasteras SK |
| BTTS rate | 55.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 47.05 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 24.03 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.17 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 42.53 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.24 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 243.92 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.77 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 240 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 16 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 240 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 16 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 240 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 16 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 240 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 16 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 240 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 16 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 224 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 16 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **17.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **18.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=441, fgte=441 rows)
- **19.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=16 positions=1..16 teams=16
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=16 positions=1..16 teams=16
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=16 positions=1..16 teams=16
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=16 positions=1..16 teams=16
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=16 positions=1..16 teams=16
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=16 positions=1..16 teams=16
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=16 positions=1..16 teams=16
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=16 positions=1..16 teams=16
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=16 positions=1..16 teams=16
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=16 positions=1..16 teams=16
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=16 positions=1..16 teams=16
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=16 positions=1..16 teams=16
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=16 positions=1..16 teams=16
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=16 positions=1..16 teams=16
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=16 positions=1..16 teams=16
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=16 positions=1..16 teams=16
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=16 positions=1..16 teams=16
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=16 positions=1..16 teams=16
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=16 positions=1..16 teams=16
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=16 positions=1..16 teams=16
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
