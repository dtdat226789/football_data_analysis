# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:47:35+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Ykkosliiga (Finland)
- Scope: league `finland2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/finland2/database_profile.json | yes | yes | 49.64 |
| matches_analysis | data/analysis/finland2/matches_analysis.json | yes | yes | 17.17 |
| goals_analysis | data/analysis/finland2/goals_analysis.json | yes | yes | 12.37 |
| teams_analysis | data/analysis/finland2/teams_analysis.json | yes | yes | 34.53 |
| season_trends | data/analysis/finland2/season_trends.json | yes | yes | 10.13 |
| scoreline_analysis | data/analysis/finland2/scoreline_analysis.json | yes | yes | 147.18 |
| relationships | data/analysis/finland2/relationships.json | yes | yes | 13.71 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 933 matches: home wins 42.7%, draws 25.0%, away wins 32.4% (398H / 233D / 302A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 26 home and 28 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 263 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 933 matches produced 2783 goals (avg 2.983 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.9% vs away 45.1% of 2783 goals in total (home/away ratio 1.22)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 519 of 933 matches (55.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 313 scoring matches, 35.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.56, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — TPS leads with 221 points across 5 seasons (2 title(s), GD 84)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 0 teams present in every one of the 7 seasons
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Ekenas earns 45 more points at home than away (132 home vs 87 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — TPS won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2021: TPS beat Rovaniemi by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.010 per match): first half 3.01 vs last half 3.02 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021 (goals view, avg abs position diff 8.583)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2023 (luck view, avg abs position diff 0.667)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 108 matches (11.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (78 of 398 home matches, 19.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (108 of 233 draw matches, 46.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (65 of 302 away matches, 21.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 35 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.1473 (n=798 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.642: home 2.997, draw -0.272, away -3.645
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (44)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 933 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 933 |
| Average goals per match | 2.983 |
| Home win rate | 42.7% |
| Draw rate | 25.0% |
| Away win rate | 32.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | TPS |
| Champion with most titles | TPS |
| BTTS rate | 55.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.64 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 17.17 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.37 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 34.53 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.13 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 147.18 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.71 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 132 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 132 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2021 has 12 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 132 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 12 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 132 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 12 teams, expected 20
- **9.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 135 matches, expected 380
- **10.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 10 teams, expected 20
- **11.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 135 matches, expected 380
- **12.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 10 teams, expected 20
- **13.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 135 matches, expected 380
- **14.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **15.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **16.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2020 avg goals 3.348 vs overall 2.983 (deviation 0.365)
- **17.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020 goalless share 4.5% vs overall 6.1% (deviation 1.6 pp)
- **18.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022 goalless share 3.8% vs overall 6.1% (deviation 2.3 pp)
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023 goalless share 8.3% vs overall 6.1% (deviation 2.2 pp)
- **20.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025 goalless share 3.7% vs overall 6.1% (deviation 2.4 pp)
- **21.** `HIGH_SCORING_MATCHES` *(warning)* — 19 match(es) with >= 8 total goals (extreme scorelines)
- **22.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **23.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=313, fgte=313 rows)
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=12 positions=1..12 teams=12
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=12 positions=1..12 teams=12
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=12 positions=1..12 teams=12
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=12 positions=1..13 teams=12
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=12 positions=6..21 teams=12
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=12 positions=1..24 teams=12
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=12 positions=1..13 teams=12
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=12 positions=6..20 teams=12
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=12 positions=1..24 teams=12
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=12 positions=1..12 teams=12
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=12 positions=1..12 teams=12
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=12 positions=1..12 teams=12
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=10 positions=1..11 teams=10
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=10 positions=2..14 teams=10
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=10 positions=1..20 teams=10
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=10 positions=1..11 teams=10
- **40.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=10 positions=2..15 teams=10
- **41.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=10 positions=1..20 teams=10
- **42.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **43.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **44.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
