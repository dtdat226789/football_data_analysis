# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:00:40+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Eerste Divisie (Netherlands)
- Scope: league `holland2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\holland2\database_profile.json | yes | yes | 31.44 |
| matches_analysis | E:\football_data_analysis\data\analysis\holland2\matches_analysis.json | yes | yes | 10.99 |
| goals_analysis | E:\football_data_analysis\data\analysis\holland2\goals_analysis.json | yes | yes | 6.43 |
| teams_analysis | E:\football_data_analysis\data\analysis\holland2\teams_analysis.json | yes | yes | 32.67 |
| season_trends | E:\football_data_analysis\data\analysis\holland2\season_trends.json | yes | yes | 3.95 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\holland2\scoreline_analysis.json | yes | yes | 85.22 |
| relationships | E:\football_data_analysis\data\analysis\holland2\relationships.json | yes | yes | 14.37 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 466 matches: home wins 44.2%, draws 20.8%, away wins 35.0% (206H / 97D / 163A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 16 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 128 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 466 matches produced 1527 goals (avg 3.277 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.6% vs away 45.4% of 1527 goals in total (home/away ratio 1.20)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 296 of 466 matches (63.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 165 scoring matches, 36.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 27.66, median 22.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Den Haag leads with 89 points across 1 seasons (1 title(s), GD 53)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 18 teams present in every one of the 2 seasons (Almere City, De Graafschap, Den Bosch, Dordrecht, Eindhoven FC...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Helmond earns 27 more points at home than away (37 home vs 10 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Den Haag won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Heracles beat Almere City by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.586 per match): first half 3.184 vs last half 3.77 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 6.500)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 43 matches (9.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (41 of 206 home matches, 19.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (43 of 97 draw matches, 44.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (38 of 163 away matches, 23.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 22 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_rest_days |corr| = 0.126 (n=447 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.061: home 1.583, draw 0.320, away -2.479
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (13)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 466 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 466 |
| Average goals per match | 3.277 |
| Home win rate | 44.2% |
| Draw rate | 20.8% |
| Away win rate | 35.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Den Haag |
| Champion with most titles | Den Haag |
| BTTS rate | 63.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.44 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 10.99 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.43 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 32.67 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.95 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 85.22 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.37 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 392 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 21 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 74 matches, expected 380
- **4.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **5.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.77 vs overall 3.277 (deviation 0.493)
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 52.7% vs overall 44.2%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 16.2% vs overall 20.8%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=21 positions=1..21 teams=21
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=21 positions=1..21 teams=21
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=21 positions=1..21 teams=21

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
