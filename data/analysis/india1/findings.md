# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:01:19+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: ISL (India)
- Scope: league `india1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\india1\database_profile.json | yes | yes | 31.28 |
| matches_analysis | E:\football_data_analysis\data\analysis\india1\matches_analysis.json | yes | yes | 9.53 |
| goals_analysis | E:\football_data_analysis\data\analysis\india1\goals_analysis.json | yes | yes | 6.14 |
| teams_analysis | E:\football_data_analysis\data\analysis\india1\teams_analysis.json | yes | yes | 24.21 |
| season_trends | E:\football_data_analysis\data\analysis\india1\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\india1\scoreline_analysis.json | yes | yes | 43.54 |
| relationships | E:\football_data_analysis\data\analysis\india1\relationships.json | yes | yes | 14.30 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 247 matches: home wins 40.9%, draws 27.1%, away wins 32.0% (101H / 67D / 79A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 10 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 58 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 247 matches produced 669 goals (avg 2.709 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.2% vs away 46.8% of 669 goals in total (home/away ratio 1.14)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 131 of 247 matches (53.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 82 scoring matches, 36.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.38, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Mohun Bagan leads with 82 points across 2 seasons (1 title(s), GD 45)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (Bengaluru FC, Chennaiyin, East Bengal, Goa, Jamshedpur...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Mohun Bagan earns 26 more points at home than away (54 home vs 28 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Mohun Bagan won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: East Bengal beat Mohun Bagan by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.443 per match): first half 2.872 vs last half 2.429 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.714)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2024-2025 (luck view, avg abs position diff 1.692)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 32 matches (13.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (24 of 101 home matches, 23.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (32 of 67 draw matches, 47.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (19 of 79 away matches, 24.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — points_difference |corr| = -0.0891 (n=247 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.288: home 2.604, draw -1.537, away -2.684
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 247 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 247 |
| Average goals per match | 2.709 |
| Home win rate | 40.9% |
| Draw rate | 27.1% |
| Away win rate | 32.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Mohun Bagan |
| Champion with most titles | Mohun Bagan |
| BTTS rate | 53.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.28 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.53 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.14 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 24.21 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 43.54 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.30 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 156 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 13 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 91 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 14 teams, expected 20
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 11.0% vs overall 8.5% (deviation 2.5 pp)
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 draw outcome share 31.9% vs overall 27.1%
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=7, fgte=7 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=13 positions=1..13 teams=13
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=13 positions=1..13 teams=13
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=13 positions=1..13 teams=13
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=14 positions=1..14 teams=14
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=14 positions=1..14 teams=14
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=14 positions=1..14 teams=14

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
