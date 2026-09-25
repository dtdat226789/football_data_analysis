# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:01:28+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier Division (Ireland)
- Scope: league `ireland1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\ireland1\database_profile.json | yes | yes | 31.31 |
| matches_analysis | E:\football_data_analysis\data\analysis\ireland1\matches_analysis.json | yes | yes | 11.08 |
| goals_analysis | E:\football_data_analysis\data\analysis\ireland1\goals_analysis.json | yes | yes | 6.29 |
| teams_analysis | E:\football_data_analysis\data\analysis\ireland1\teams_analysis.json | yes | yes | 20.03 |
| season_trends | E:\football_data_analysis\data\analysis\ireland1\season_trends.json | yes | yes | 3.90 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\ireland1\scoreline_analysis.json | yes | yes | 54.03 |
| relationships | E:\football_data_analysis\data\analysis\ireland1\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 338 matches: home wins 40.5%, draws 30.5%, away wins 29.0% (137H / 103D / 98A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 17 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 85 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 338 matches produced 875 goals (avg 2.589 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.2% vs away 44.8% of 875 goals in total (home/away ratio 1.23)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 190 of 338 matches (56.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 99 scoring matches, 32.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.01, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Shamrock Rovers leads with 125 points across 2 seasons (1 title(s), GD 41)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 2 seasons (Bohemians, Derry City, Drogheda, Galway, Shamrock Rovers...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Shamrock Rovers earns 25 more points at home than away (75 home vs 50 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Shamrock Rovers won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026: St. Patricks beat Shamrock Rovers by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.344 per match): first half 2.428 vs last half 2.772 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025 (goals view, avg abs position diff 4.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 2.600)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 46 matches (13.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (35 of 137 home matches, 25.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (46 of 103 draw matches, 44.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (30 of 98 away matches, 30.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 6 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.1342 (n=338 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.125: home 2.635, draw -1.709, away -2.490
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 338 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 338 |
| Average goals per match | 2.589 |
| Home win rate | 40.5% |
| Draw rate | 30.5% |
| Away win rate | 29.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Shamrock Rovers |
| Champion with most titles | Shamrock Rovers |
| BTTS rate | 56.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.31 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 11.08 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.29 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 20.03 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.90 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 54.03 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 180 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 158 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=7, fgte=7 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=10 positions=1..10 teams=10
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=10 positions=1..10 teams=10
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=10 positions=1..10 teams=10
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
