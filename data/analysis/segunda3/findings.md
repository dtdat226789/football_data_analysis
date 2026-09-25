# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:46:09+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Segunda RFEF - Group 3 (Spain)
- Scope: league `segunda3`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\segunda3\database_profile.json | yes | yes | 32.31 |
| matches_analysis | E:\football_data_analysis\data\analysis\segunda3\matches_analysis.json | yes | yes | 8.98 |
| goals_analysis | E:\football_data_analysis\data\analysis\segunda3\goals_analysis.json | yes | yes | 6.42 |
| teams_analysis | E:\football_data_analysis\data\analysis\segunda3\teams_analysis.json | yes | yes | 40.01 |
| season_trends | E:\football_data_analysis\data\analysis\segunda3\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\segunda3\scoreline_analysis.json | yes | yes | 53.84 |
| relationships | E:\football_data_analysis\data\analysis\segunda3\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 337 matches: home wins 45.4%, draws 31.5%, away wins 23.1% (153H / 106D / 78A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 6 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 81 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 337 matches produced 810 goals (avg 2.404 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 58.3% vs away 41.7% of 810 goals in total (home/away ratio 1.40)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 176 of 337 matches (52.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 96 scoring matches, 31.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.56, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Baleares leads with 67 points across 2 seasons (1 title(s), GD 15)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 2 seasons (Alcoyano, Baleares, Castellon B, Poblense, Valencia B)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Andratx earns 23 more points at home than away (28 home vs 5 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Baleares won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Baleares beat Sant Andreu by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.231 per match): first half 2.425 vs last half 2.194 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.556)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 57 matches (16.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (57 of 153 home matches, 37.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (48 of 106 draw matches, 45.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (27 of 78 away matches, 34.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.211 (n=337 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — away_points_before_match spreads group means over 5.486: home 18.732, draw 19.925, away 24.218
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 337 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 337 |
| Average goals per match | 2.404 |
| Home win rate | 45.4% |
| Draw rate | 31.5% |
| Away win rate | 23.1% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Baleares |
| Champion with most titles | Baleares |
| BTTS rate | 52.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.31 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.98 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.42 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 40.01 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 53.84 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 31 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 6.5% vs overall 10.4% (deviation 3.9 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 29.0% vs overall 23.1%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 3 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (24 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=27, fgte=27 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
