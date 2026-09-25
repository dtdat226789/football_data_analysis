# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:56:02+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Championship (England)
- Scope: league `cha`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\cha\database_profile.json | yes | yes | 31.69 |
| matches_analysis | E:\football_data_analysis\data\analysis\cha\matches_analysis.json | yes | yes | 13.38 |
| goals_analysis | E:\football_data_analysis\data\analysis\cha\goals_analysis.json | yes | yes | 6.25 |
| teams_analysis | E:\football_data_analysis\data\analysis\cha\teams_analysis.json | yes | yes | 39.70 |
| season_trends | E:\football_data_analysis\data\analysis\cha\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\cha\scoreline_analysis.json | yes | yes | 104.08 |
| relationships | E:\football_data_analysis\data\analysis\cha\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 654 matches: home wins 41.6%, draws 27.2%, away wins 31.2% (272H / 178D / 204A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 24 home and 15 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 172 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 654 matches produced 1722 goals (avg 2.633 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.2% vs away 45.8% of 1722 goals in total (home/away ratio 1.18)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 380 of 654 matches (58.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 215 scoring matches, 35.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.57, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Southampton leads with 98 points across 2 seasons (0 title(s), GD 36)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 18 teams present in every one of the 2 seasons (Birmingham, Blackburn, Bristol City, Charlton, Derby...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Watford earns 23 more points at home than away (44 home vs 21 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Coventry won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Swansea beat West Ham by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.331 per match): first half 2.585 vs last half 2.916 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 6.750)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 3.417)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 94 matches (14.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (73 of 272 home matches, 26.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (94 of 178 draw matches, 52.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (59 of 204 away matches, 28.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 8 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_conceded_avg |corr| = -0.0622 (n=654 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.102: home 2.489, draw -1.416, away -2.613
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 654 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 654 |
| Average goals per match | 2.633 |
| Home win rate | 41.6% |
| Draw rate | 27.2% |
| Away win rate | 31.2% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Southampton |
| Champion with most titles | Coventry |
| BTTS rate | 58.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.69 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 13.38 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.25 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.70 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 104.08 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 559 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 24 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 95 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=4, fgte=4 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=24 positions=1..24 teams=24
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=24 positions=1..24 teams=24
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=24 positions=1..24 teams=24
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=24 positions=1..24 teams=24
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=24 positions=1..24 teams=24
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=24 positions=1..24 teams=24

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
