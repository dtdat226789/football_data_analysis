# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:32:22+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Ligue 1 (France)
- Scope: league `france1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/france1/database_profile.json | yes | yes | 46.03 |
| matches_analysis | data/analysis/france1/matches_analysis.json | yes | yes | 29.72 |
| goals_analysis | data/analysis/france1/goals_analysis.json | yes | yes | 12.34 |
| teams_analysis | data/analysis/france1/teams_analysis.json | yes | yes | 39.50 |
| season_trends | data/analysis/france1/season_trends.json | yes | yes | 10.38 |
| scoreline_analysis | data/analysis/france1/scoreline_analysis.json | yes | yes | 329.98 |
| relationships | data/analysis/france1/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2127 matches: home wins 42.4%, draws 24.6%, away wins 33.0% (902H / 523D / 702A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 73 home and 51 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 556 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2127 matches produced 5992 goals (avg 2.817 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.9% vs away 46.1% of 5992 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1175 of 2127 matches (55.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 667 scoring matches, 33.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.04, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — PSG leads with 503 points across 7 seasons (5 title(s), GD 316)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 10 teams present in every one of the 7 seasons (Brest, Lens, Lille, Lyon, Marseille...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Rennes earns 81 more points at home than away (216 home vs 135 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — PSG won 5 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Lyon beat PSG by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.155 per match): first half 2.792 vs last half 2.947 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 7.333)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2023-2024 (luck view, avg abs position diff 3.111)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 247 matches (11.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (186 of 902 home matches, 20.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (247 of 523 draw matches, 47.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (157 of 702 away matches, 22.4%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 59 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.0551 (n=2062 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 9.179: home 4.179, draw -0.917, away -5.000
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (30)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2127 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2127 |
| Average goals per match | 2.817 |
| Home win rate | 42.4% |
| Draw rate | 24.6% |
| Away win rate | 33.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | PSG |
| Champion with most titles | PSG |
| BTTS rate | 55.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 46.03 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 29.72 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.50 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.38 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 329.98 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 306 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 18 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 310 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 21 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 65 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **9.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **10.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 37.4% vs overall 42.4%
- **11.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 37.6% vs overall 33.0%
- **12.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 8.8% vs overall 6.9% (deviation 1.9 pp)
- **13.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 4.6% vs overall 6.9% (deviation 2.3 pp)
- **14.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 home outcome share 46.7% vs overall 42.4%
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 draw outcome share 20.3% vs overall 24.6%
- **16.** `HIGH_SCORING_MATCHES` *(warning)* — 18 match(es) with >= 8 total goals (extreme scorelines)
- **17.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **18.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=313, fgte=313 rows)
- **19.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..18 teams=18
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..18 teams=18
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..18 teams=18
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=18 positions=1..18 teams=18
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=18 positions=1..18 teams=18
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=18 positions=1..18 teams=18
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=21 positions=1..21 teams=21
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=21 positions=1..21 teams=21
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=21 positions=1..21 teams=21
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
