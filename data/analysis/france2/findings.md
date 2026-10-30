# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:51:44+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Ligue 2 (France)
- Scope: league `france2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/france2/database_profile.json | yes | yes | 44.60 |
| matches_analysis | data/analysis/france2/matches_analysis.json | yes | yes | 27.07 |
| goals_analysis | data/analysis/france2/goals_analysis.json | yes | yes | 12.35 |
| teams_analysis | data/analysis/france2/teams_analysis.json | yes | yes | 49.71 |
| season_trends | data/analysis/france2/season_trends.json | yes | yes | 10.42 |
| scoreline_analysis | data/analysis/france2/scoreline_analysis.json | yes | yes | 321.03 |
| relationships | data/analysis/france2/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2226 matches: home wins 42.0%, draws 28.8%, away wins 29.3% (934H / 640D / 652A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 56 home and 52 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 513 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2226 matches produced 5441 goals (avg 2.444 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.9% vs away 45.1% of 5441 goals in total (home/away ratio 1.22)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1082 of 2226 matches (48.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 644 scoring matches, 32.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.55, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Paris FC leads with 317 points across 5 seasons (0 title(s), GD 66)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 4 teams present in every one of the 7 seasons (Grenoble, Guingamp, Pau FC, Rodez)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — AC Ajaccio earns 67 more points at home than away (138 home vs 71 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Troyes won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2024-2025: Lorient beat Paris FC by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.232 per match): first half 2.363 vs last half 2.595 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2022-2023 (goals view, avg abs position diff 6.400)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.444)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 282 matches (12.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (282 of 934 home matches, 30.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (277 of 640 draw matches, 43.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (204 of 652 away matches, 31.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 29 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0734 (n=2136 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.73: home 1.908, draw -0.825, away -2.822
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (27)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2226 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2226 |
| Average goals per match | 2.444 |
| Home win rate | 42.0% |
| Draw rate | 28.8% |
| Away win rate | 29.3% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Paris FC |
| Champion with most titles | Troyes |
| BTTS rate | 48.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 44.60 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 27.07 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.35 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 49.71 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.42 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 321.03 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 19 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 310 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 90 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **7.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 draw outcome share 33.4% vs overall 28.8%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 24.7% vs overall 29.3%
- **10.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 11.8% vs overall 9.7% (deviation 2.1 pp)
- **11.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 6.2% vs overall 9.7% (deviation 3.5 pp)
- **12.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 home outcome share 48.7% vs overall 42.0%
- **13.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 draw outcome share 23.5% vs overall 28.8%
- **14.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 home outcome share 37.7% vs overall 42.0%
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 35.6% vs overall 42.0%
- **16.** `HIGH_SCORING_MATCHES` *(warning)* — 12 match(es) with >= 8 total goals (extreme scorelines)
- **17.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **18.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=317, fgte=317 rows)
- **19.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=19 positions=1..19 teams=19
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=19 positions=1..19 teams=19
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=19 positions=1..19 teams=19
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
