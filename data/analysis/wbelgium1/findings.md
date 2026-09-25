# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:50:45+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Super League Women (Belgium)
- Scope: league `wbelgium1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\wbelgium1\database_profile.json | yes | yes | 31.98 |
| matches_analysis | E:\football_data_analysis\data\analysis\wbelgium1\matches_analysis.json | yes | yes | 6.90 |
| goals_analysis | E:\football_data_analysis\data\analysis\wbelgium1\goals_analysis.json | yes | yes | 6.14 |
| teams_analysis | E:\football_data_analysis\data\analysis\wbelgium1\teams_analysis.json | yes | yes | 17.89 |
| season_trends | E:\football_data_analysis\data\analysis\wbelgium1\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\wbelgium1\scoreline_analysis.json | yes | yes | 26.26 |
| relationships | E:\football_data_analysis\data\analysis\wbelgium1\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 120 matches: home wins 43.3%, draws 21.7%, away wins 35.0% (52H / 26D / 42A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 4 home and 0 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 30 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 120 matches produced 359 goals (avg 2.992 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 51.0% vs away 49.0% of 359 goals in total (home/away ratio 1.04)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 67 of 120 matches (55.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 41 scoring matches, 36.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.28, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Leuven W leads with 77 points across 2 seasons (1 title(s), GD 52)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 7 teams present in every one of the 2 seasons (Club Brugge W, Genk W, Gent W, Leuven W, RSC Anderlecht W...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — St. Liege W earns 12 more points at home than away (22 home vs 10 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Leuven W won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: RSC Anderlecht W beat Club Brugge W by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.083 per match): first half 3.0 vs last half 2.917 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 3.250)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.250)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-0 in 15 matches (12.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-0 (15 of 52 home matches, 28.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (12 of 26 draw matches, 46.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-2 (8 of 42 away matches, 19.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = -0.1703 (n=120 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 13.287: home 7.096, draw -0.846, away -6.190
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 120 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 120 |
| Average goals per match | 2.992 |
| Home win rate | 43.3% |
| Draw rate | 21.7% |
| Away win rate | 35.0% |
| Most common scoreline | 2-0 |
| Dominant team (lifetime points) | Leuven W |
| Champion with most titles | Leuven W |
| BTTS rate | 55.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.98 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 6.90 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.14 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 17.89 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 26.26 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 108 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 8 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 8 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 8.3% vs overall 5.8% (deviation 2.5 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 66.7% vs overall 43.3%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 8.3% vs overall 21.7%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 25.0% vs overall 35.0%
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=31, fgte=31 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=8 positions=1..8 teams=8
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=8 positions=1..8 teams=8
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=8 positions=1..8 teams=8
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=8 positions=1..8 teams=8
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=8 positions=1..8 teams=8
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=8 positions=1..8 teams=8

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
