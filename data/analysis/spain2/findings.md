# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:48:21+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: LaLiga2 (Spain)
- Scope: league `spain2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\spain2\database_profile.json | yes | yes | 32.73 |
| matches_analysis | E:\football_data_analysis\data\analysis\spain2\matches_analysis.json | yes | yes | 11.92 |
| goals_analysis | E:\football_data_analysis\data\analysis\spain2\goals_analysis.json | yes | yes | 6.32 |
| teams_analysis | E:\football_data_analysis\data\analysis\spain2\teams_analysis.json | yes | yes | 39.66 |
| season_trends | E:\football_data_analysis\data\analysis\spain2\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\spain2\scoreline_analysis.json | yes | yes | 95.40 |
| relationships | E:\football_data_analysis\data\analysis\spain2\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 575 matches: home wins 43.5%, draws 24.9%, away wins 31.7% (250H / 143D / 182A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 18 home and 13 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 141 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 575 matches produced 1498 goals (avg 2.605 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.5% vs away 45.5% of 1498 goals in total (home/away ratio 1.20)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 315 of 575 matches (54.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 180 scoring matches, 34.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.36, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Castellon leads with 95 points across 2 seasons (1 title(s), GD 32)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 15 teams present in every one of the 2 seasons (Albacete, Almeria, Andorra, Burgos CF, Cadiz CF...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Almeria earns 26 more points at home than away (59 home vs 33 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Racing Santander won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Castellon beat Eibar by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.153 per match): first half 2.623 vs last half 2.47 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 7.909)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.182)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 72 matches (12.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (62 of 250 home matches, 24.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (72 of 143 draw matches, 50.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (53 of 182 away matches, 29.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 9 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.1013 (n=575 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.04: home 2.452, draw -0.846, away -3.588
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 575 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 575 |
| Average goals per match | 2.605 |
| Home win rate | 43.5% |
| Draw rate | 24.9% |
| Away win rate | 31.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Castellon |
| Champion with most titles | Racing Santander |
| BTTS rate | 54.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.73 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 11.92 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.32 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.66 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 95.40 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 509 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 23 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 66 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 22 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 10.6% vs overall 8.2% (deviation 2.4 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 37.9% vs overall 31.7%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=29, fgte=29 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=23 positions=1..23 teams=23
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=23 positions=1..23 teams=23
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=23 positions=1..23 teams=23
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=22 positions=1..22 teams=22
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=22 positions=1..22 teams=22
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=22 positions=1..22 teams=22

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
