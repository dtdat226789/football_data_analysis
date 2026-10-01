# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:46:04+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: efbet League (Bulgaria)
- Scope: league `bulgaria1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\bulgaria1\database_profile.json | yes | yes | 31.62 |
| matches_analysis | E:\football_data_analysis\data\analysis\bulgaria1\matches_analysis.json | yes | yes | 9.01 |
| goals_analysis | E:\football_data_analysis\data\analysis\bulgaria1\goals_analysis.json | yes | yes | 6.33 |
| teams_analysis | E:\football_data_analysis\data\analysis\bulgaria1\teams_analysis.json | yes | yes | 27.51 |
| season_trends | E:\football_data_analysis\data\analysis\bulgaria1\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\bulgaria1\scoreline_analysis.json | yes | yes | 60.48 |
| relationships | E:\football_data_analysis\data\analysis\bulgaria1\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 363 matches: home wins 43.0%, draws 27.3%, away wins 29.8% (156H / 99D / 108A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 6 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 89 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 363 matches produced 861 goals (avg 2.372 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.7% vs away 45.3% of 861 goals in total (home/away ratio 1.21)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 165 of 363 matches (45.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 97 scoring matches, 30.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.35, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Levski Sofia leads with 106 points across 2 seasons (2 title(s), GD 63)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (Arda, Botev Plovdiv, Botev Vratsa, CSKA 1948 Sofia, CSKA Sofia...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Lok. Plovdiv earns 20 more points at home than away (41 home vs 21 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Levski Sofia won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Levski Sofia beat CSKA Sofia by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.364 per match): first half 2.303 vs last half 2.667 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.235)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 45 matches (12.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (43 of 156 home matches, 27.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (45 of 99 draw matches, 45.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (29 of 108 away matches, 26.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — rest_days_difference |corr| = -0.1124 (n=285 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 9.299: home 3.920, draw -0.390, away -5.379
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 363 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 363 |
| Average goals per match | 2.372 |
| Home win rate | 43.0% |
| Draw rate | 27.3% |
| Away win rate | 29.8% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Levski Sofia |
| Champion with most titles | Levski Sofia |
| BTTS rate | 45.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.62 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.01 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.33 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 27.51 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 60.48 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 294 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 17 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 69 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 14 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.3% vs overall 10.7% (deviation 6.4 pp)
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=3, fgte=3 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=17 positions=1..17 teams=17
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=17 positions=1..17 teams=17
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=17 positions=1..17 teams=17
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=14 positions=1..14 teams=14
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=14 positions=1..14 teams=14
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=14 positions=1..14 teams=14

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
