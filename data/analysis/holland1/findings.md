# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:00:29+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Eredivisie (Netherlands)
- Scope: league `holland1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\holland1\database_profile.json | yes | yes | 32.52 |
| matches_analysis | E:\football_data_analysis\data\analysis\holland1\matches_analysis.json | yes | yes | 9.67 |
| goals_analysis | E:\football_data_analysis\data\analysis\holland1\goals_analysis.json | yes | yes | 6.42 |
| teams_analysis | E:\football_data_analysis\data\analysis\holland1\teams_analysis.json | yes | yes | 35.38 |
| season_trends | E:\football_data_analysis\data\analysis\holland1\season_trends.json | yes | yes | 3.95 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\holland1\scoreline_analysis.json | yes | yes | 66.98 |
| relationships | E:\football_data_analysis\data\analysis\holland1\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 384 matches: home wins 42.2%, draws 26.0%, away wins 31.8% (162H / 100D / 122A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 114 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 384 matches produced 1256 goals (avg 3.271 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.5% vs away 45.5% of 1256 goals in total (home/away ratio 1.20)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 246 of 384 matches (64.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 139 scoring matches, 37.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 27.94, median 21.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — PSV leads with 100 points across 2 seasons (1 title(s), GD 70)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 16 teams present in every one of the 2 seasons (AZ Alkmaar, Ajax, Excelsior, Feyenoord, G.A. Eagles...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — G.A. Eagles earns 16 more points at home than away (32 home vs 16 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — PSV won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: AZ Alkmaar beat Feyenoord by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.645 per match): first half 3.165 vs last half 3.81 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (luck view, avg abs position diff 6.833)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.556)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-2 in 41 matches (10.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (35 of 162 home matches, 21.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 2-2 (41 of 100 draw matches, 41.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (29 of 122 away matches, 23.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 16 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.1246 (n=384 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.46: home 3.222, draw -0.500, away -4.238
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 384 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 384 |
| Average goals per match | 3.271 |
| Home win rate | 42.2% |
| Draw rate | 26.0% |
| Away win rate | 31.8% |
| Most common scoreline | 2-2 |
| Dominant team (lifetime points) | PSV |
| Champion with most titles | PSV |
| BTTS rate | 64.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.52 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.67 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.42 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 35.38 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.95 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 66.98 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 321 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 24 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 63 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.81 vs overall 3.271 (deviation 0.539)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 30.2% vs overall 42.2%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 42.9% vs overall 31.8%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=24 positions=1..24 teams=24
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=24 positions=1..24 teams=24
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=24 positions=1..24 teams=24
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
