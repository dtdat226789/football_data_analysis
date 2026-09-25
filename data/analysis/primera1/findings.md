# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:42:39+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Primera RFEF - Group 1 (Spain)
- Scope: league `primera1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\primera1\database_profile.json | yes | yes | 30.69 |
| matches_analysis | E:\football_data_analysis\data\analysis\primera1\matches_analysis.json | yes | yes | 8.83 |
| goals_analysis | E:\football_data_analysis\data\analysis\primera1\goals_analysis.json | yes | yes | 6.34 |
| teams_analysis | E:\football_data_analysis\data\analysis\primera1\teams_analysis.json | yes | yes | 38.67 |
| season_trends | E:\football_data_analysis\data\analysis\primera1\season_trends.json | yes | yes | 3.97 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\primera1\scoreline_analysis.json | yes | yes | 71.52 |
| relationships | E:\football_data_analysis\data\analysis\primera1\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 438 matches: home wins 46.1%, draws 27.9%, away wins 26.0% (202H / 122D / 114A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 7 home and 7 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 119 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 438 matches produced 1079 goals (avg 2.463 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.9% vs away 43.1% of 1079 goals in total (home/away ratio 1.32)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 219 of 438 matches (50.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 109 scoring matches, 27.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.09, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Tenerife leads with 79 points across 1 seasons (1 title(s), GD 41)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (AD Merida, Arenas Getxo, Ath Bilbao B, Barakaldo, Cacereno...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Barakaldo earns 28 more points at home than away (45 home vs 17 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Tenerife won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: UD Logrones beat Cacereno by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.178 per match): first half 2.447 vs last half 2.625 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.857)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 58 matches (13.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (58 of 202 home matches, 28.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (56 of 122 draw matches, 45.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (31 of 114 away matches, 27.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 6 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_scored_last_5 |corr| = 0.0921 (n=438 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — away_points_before_match spreads group means over 3.924: home 21.772, draw 25.697, away 24.377
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (12)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 438 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 438 |
| Average goals per match | 2.463 |
| Home win rate | 46.1% |
| Draw rate | 27.9% |
| Away win rate | 26.0% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Tenerife |
| Champion with most titles | Tenerife |
| BTTS rate | 50.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 30.69 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.83 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 38.67 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.97 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 71.52 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 398 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 21 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 40 matches, expected 380
- **4.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 5.0% vs overall 9.4% (deviation 4.4 pp)
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 22.5% vs overall 27.9%
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=21 positions=1..21 teams=21
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=21 positions=1..21 teams=21
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=21 positions=1..21 teams=21

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
