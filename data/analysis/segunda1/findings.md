# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:45:33+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Segunda RFEF - Group 1 (Spain)
- Scope: league `segunda1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\segunda1\database_profile.json | yes | yes | 32.21 |
| matches_analysis | E:\football_data_analysis\data\analysis\segunda1\matches_analysis.json | yes | yes | 8.26 |
| goals_analysis | E:\football_data_analysis\data\analysis\segunda1\goals_analysis.json | yes | yes | 6.33 |
| teams_analysis | E:\football_data_analysis\data\analysis\segunda1\teams_analysis.json | yes | yes | 39.18 |
| season_trends | E:\football_data_analysis\data\analysis\segunda1\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\segunda1\scoreline_analysis.json | yes | yes | 57.60 |
| relationships | E:\football_data_analysis\data\analysis\segunda1\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 333 matches: home wins 41.7%, draws 26.7%, away wins 31.5% (139H / 89D / 105A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 5 home and 6 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 74 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 333 matches produced 847 goals (avg 2.544 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.4% vs away 45.6% of 847 goals in total (home/away ratio 1.19)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 167 of 333 matches (50.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 106 scoring matches, 35.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.49, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Dep. Fabril leads with 69 points across 1 seasons (1 title(s), GD 37)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 6 teams present in every one of the 2 seasons (Atl. Astorga, Bergantinos, Coruxo FC, Marino de Luanco, Oviedo B...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Gimnastica Segoviana earns 15 more points at home than away (33 home vs 18 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Dep. Fabril won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Gernika beat Bergantinos by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.094 per match): first half 2.536 vs last half 2.63 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 7.667)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 0.778)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 44 matches (13.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (44 of 139 home matches, 31.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (39 of 89 draw matches, 43.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (30 of 105 away matches, 28.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 9 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_conceded_last_5 |corr| = 0.1231 (n=333 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.023: home 1.547, draw 0.090, away -2.476
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 333 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 333 |
| Average goals per match | 2.544 |
| Home win rate | 41.7% |
| Draw rate | 26.7% |
| Away win rate | 31.5% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Dep. Fabril |
| Champion with most titles | Dep. Fabril |
| BTTS rate | 50.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.21 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.26 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.33 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.18 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 57.60 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 27 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.7% vs overall 8.7% (deviation 5.0 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 18.5% vs overall 26.7%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 37.0% vs overall 31.5%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=27, fgte=27 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
