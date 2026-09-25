# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:46:45+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Segunda RFEF - Group 5 (Spain)
- Scope: league `segunda5`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\segunda5\database_profile.json | yes | yes | 31.02 |
| matches_analysis | E:\football_data_analysis\data\analysis\segunda5\matches_analysis.json | yes | yes | 9.26 |
| goals_analysis | E:\football_data_analysis\data\analysis\segunda5\goals_analysis.json | yes | yes | 6.17 |
| teams_analysis | E:\football_data_analysis\data\analysis\segunda5\teams_analysis.json | yes | yes | 39.47 |
| season_trends | E:\football_data_analysis\data\analysis\segunda5\season_trends.json | yes | yes | 4.00 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\segunda5\scoreline_analysis.json | yes | yes | 59.04 |
| relationships | E:\football_data_analysis\data\analysis\segunda5\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 339 matches: home wins 45.4%, draws 25.1%, away wins 29.5% (154H / 85D / 100A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 9 home and 7 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 93 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 339 matches produced 872 goals (avg 2.572 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.9% vs away 43.1% of 872 goals in total (home/away ratio 1.32)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 171 of 339 matches (50.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 98 scoring matches, 31.9% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.38, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — San Sebastian Reyes leads with 80 points across 2 seasons (1 title(s), GD 29)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 6 teams present in every one of the 2 seasons (Conquense, Getafe B, Navalcarnero, RSD Alcala, Real Madrid C...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Navalcarnero earns 33 more points at home than away (40 home vs 7 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Rayo Majadahonda won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Rayo Majadahonda beat San Sebastian Reyes by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.138 per match): first half 2.559 vs last half 2.697 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.444)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 38 matches (11.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (37 of 154 home matches, 24.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (38 of 85 draw matches, 44.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (25 of 100 away matches, 25.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 6 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_conceded_avg |corr| = 0.1173 (n=339 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — away_points_before_match spreads group means over 5.126: home 18.714, draw 20.376, away 23.840
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 339 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 339 |
| Average goals per match | 2.572 |
| Home win rate | 45.4% |
| Draw rate | 25.1% |
| Away win rate | 29.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | San Sebastian Reyes |
| Champion with most titles | Rayo Majadahonda |
| BTTS rate | 50.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.02 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.26 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.17 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.47 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 4.00 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 59.04 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 33 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 15.2% vs overall 9.4% (deviation 5.8 pp)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (31 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=27, fgte=27 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
