# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:52:21+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Super League 2 (Greece)
- Scope: league `greece2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\greece2\database_profile.json | yes | yes | 29.91 |
| matches_analysis | E:\football_data_analysis\data\analysis\greece2\matches_analysis.json | yes | yes | 7.49 |
| goals_analysis | E:\football_data_analysis\data\analysis\greece2\goals_analysis.json | yes | yes | 6.16 |
| teams_analysis | E:\football_data_analysis\data\analysis\greece2\teams_analysis.json | yes | yes | 35.32 |
| season_trends | E:\football_data_analysis\data\analysis\greece2\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\greece2\scoreline_analysis.json | yes | yes | 53.42 |
| relationships | E:\football_data_analysis\data\analysis\greece2\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 297 matches: home wins 46.5%, draws 22.9%, away wins 30.6% (138H / 68D / 91A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 4 home and 3 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 82 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 297 matches produced 676 goals (avg 2.276 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 58.0% vs away 42.0% of 676 goals in total (home/away ratio 1.38)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 119 of 297 matches (40.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 84 scoring matches, 30.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.59, median 31.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Kalamata leads with 66 points across 1 seasons (1 title(s), GD 40)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 10 teams present in every one of the 2 seasons (Asteras Tripolis B, Athens Kallithea, Chrisoupolis, Ellas Syrou, Karditsa...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Giannina earns 15 more points at home than away (18 home vs 3 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Kalamata won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Marko beat AEL Larissa by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.135 per match): first half 2.291 vs last half 2.156 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 7.500)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 49 matches (16.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (49 of 138 home matches, 35.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (35 of 68 draw matches, 51.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (31 of 91 away matches, 34.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_conceded_last_5 |corr| = 0.1305 (n=265 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 13.888: home 5.624, draw 0.443, away -8.264
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (11)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 297 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 297 |
| Average goals per match | 2.276 |
| Home win rate | 46.5% |
| Draw rate | 22.9% |
| Away win rate | 30.6% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Kalamata |
| Champion with most titles | Kalamata |
| BTTS rate | 40.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 29.91 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 7.49 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.16 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 35.32 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 53.42 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 265 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 32 matches, expected 380
- **3.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **4.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 65.6% vs overall 46.5%
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 12.5% vs overall 30.6%
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
