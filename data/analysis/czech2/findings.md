# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:47:14+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: ChNL (Czech Republic)
- Scope: league `czech2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\czech2\database_profile.json | yes | yes | 32.00 |
| matches_analysis | E:\football_data_analysis\data\analysis\czech2\matches_analysis.json | yes | yes | 8.75 |
| goals_analysis | E:\football_data_analysis\data\analysis\czech2\goals_analysis.json | yes | yes | 6.32 |
| teams_analysis | E:\football_data_analysis\data\analysis\czech2\teams_analysis.json | yes | yes | 30.10 |
| season_trends | E:\football_data_analysis\data\analysis\czech2\season_trends.json | yes | yes | 3.94 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\czech2\scoreline_analysis.json | yes | yes | 55.99 |
| relationships | E:\football_data_analysis\data\analysis\czech2\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 312 matches: home wins 45.5%, draws 23.7%, away wins 30.8% (142H / 74D / 96A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 9 home and 5 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 88 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 312 matches produced 861 goals (avg 2.760 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.3% vs away 43.7% of 861 goals in total (home/away ratio 1.29)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 168 of 312 matches (53.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 98 scoring matches, 33.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.50, median 23.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Brno leads with 76 points across 1 seasons (1 title(s), GD 40)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 11 teams present in every one of the 2 seasons (Jihlava, Kromeriz, Opava, Ostrava B, Pribram...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Opava earns 20 more points at home than away (37 home vs 17 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Brno won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Karvina beat Usti nad Labem by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.349 per match): first half 2.679 vs last half 3.028 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.250)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.750)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 34 matches (10.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (34 of 142 home matches, 23.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (29 of 74 draw matches, 39.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (25 of 96 away matches, 26.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 7 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_scored_last_5 |corr| = -0.1001 (n=240 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 5.053: home 22.243, draw 20.480, away 17.190
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 312 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 312 |
| Average goals per match | 2.76 |
| Home win rate | 45.5% |
| Draw rate | 23.7% |
| Away win rate | 30.8% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | Brno |
| Champion with most titles | Brno |
| BTTS rate | 53.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.00 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.75 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.32 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 30.10 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.94 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 55.99 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 72 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 33.3% vs overall 23.7%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 23.6% vs overall 30.8%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=16 positions=1..16 teams=16
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=16 positions=1..16 teams=16
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=16 positions=1..16 teams=16
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
