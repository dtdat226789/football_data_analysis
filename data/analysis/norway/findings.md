# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:02:50+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Eliteserien (Norway)
- Scope: league `norway`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\norway\database_profile.json | yes | yes | 32.69 |
| matches_analysis | E:\football_data_analysis\data\analysis\norway\matches_analysis.json | yes | yes | 9.72 |
| goals_analysis | E:\football_data_analysis\data\analysis\norway\goals_analysis.json | yes | yes | 6.36 |
| teams_analysis | E:\football_data_analysis\data\analysis\norway\teams_analysis.json | yes | yes | 28.31 |
| season_trends | E:\football_data_analysis\data\analysis\norway\season_trends.json | yes | yes | 3.87 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\norway\scoreline_analysis.json | yes | yes | 74.15 |
| relationships | E:\football_data_analysis\data\analysis\norway\relationships.json | yes | yes | 14.31 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 408 matches: home wins 50.0%, draws 19.1%, away wins 30.9% (204H / 78D / 126A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 11 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 143 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 408 matches produced 1293 goals (avg 3.169 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.5% vs away 42.5% of 1293 goals in total (home/away ratio 1.35)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 234 of 408 matches (57.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 160 scoring matches, 41.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 26.31, median 22.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Viking leads with 121 points across 2 seasons (2 title(s), GD 75)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (Bodo/Glimt, Brann, Fredrikstad, HamKam, KFUM Oslo...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Rosenborg earns 25 more points at home than away (50 home vs 25 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Viking won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026: Viking beat Bodo/Glimt by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (-0.014 per match): first half 3.175 vs last half 3.161 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026 (goals view, avg abs position diff 5.250)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 2.750)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 39 matches (9.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (39 of 204 home matches, 19.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (39 of 78 draw matches, 50.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (26 of 126 away matches, 20.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 14 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_rest_days |corr| = 0.1743 (n=232 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 11.228: home 4.085, draw -0.756, away -7.143
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 408 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 408 |
| Average goals per match | 3.169 |
| Home win rate | 50.0% |
| Draw rate | 19.1% |
| Away win rate | 30.9% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | Viking |
| Champion with most titles | Viking |
| BTTS rate | 57.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.69 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.72 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.36 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 28.31 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.87 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 74.15 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.31 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 168 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 9 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=23, fgte=23 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=16 positions=1..16 teams=16
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=16 positions=1..16 teams=16
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=16 positions=1..16 teams=16
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=16 positions=1..16 teams=16
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=16 positions=1..16 teams=16
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
