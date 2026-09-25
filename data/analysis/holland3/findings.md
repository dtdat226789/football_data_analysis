# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:00:50+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Tweede Divisie (Netherlands)
- Scope: league `holland3`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\holland3\database_profile.json | yes | yes | 33.15 |
| matches_analysis | E:\football_data_analysis\data\analysis\holland3\matches_analysis.json | yes | yes | 11.29 |
| goals_analysis | E:\football_data_analysis\data\analysis\holland3\goals_analysis.json | yes | yes | 6.34 |
| teams_analysis | E:\football_data_analysis\data\analysis\holland3\teams_analysis.json | yes | yes | 36.81 |
| season_trends | E:\football_data_analysis\data\analysis\holland3\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\holland3\scoreline_analysis.json | yes | yes | 70.76 |
| relationships | E:\football_data_analysis\data\analysis\holland3\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 376 matches: home wins 45.5%, draws 20.5%, away wins 34.0% (171H / 77D / 128A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 13 home and 14 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 103 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 376 matches produced 1255 goals (avg 3.338 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.3% vs away 45.7% of 1255 goals in total (home/away ratio 1.19)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 234 of 376 matches (62.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 122 scoring matches, 33.4% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.11, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Quick Boys leads with 82 points across 2 seasons (2 title(s), GD 47)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 16 teams present in every one of the 2 seasons (AFC, Barendrecht, De Treffers, GVVV, HFC...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — HFC earns 22 more points at home than away (33 home vs 11 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Quick Boys won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Quick Boys beat Kozakken Boys by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.124 per match): first half 3.32 vs last half 3.444 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (luck view, avg abs position diff 6.400)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 37 matches (9.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (31 of 171 home matches, 18.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (37 of 77 draw matches, 48.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (31 of 128 away matches, 24.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 20 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_conceded_avg |corr| = 0.0917 (n=376 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 4.1: home 21.725, draw 20.260, away 17.625
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (18)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 376 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 376 |
| Average goals per match | 3.338 |
| Home win rate | 45.5% |
| Draw rate | 20.5% |
| Away win rate | 34.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Quick Boys |
| Champion with most titles | Quick Boys |
| BTTS rate | 62.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 33.15 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 11.29 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.34 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 36.81 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 70.76 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 322 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 25 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 54 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 0.0% vs overall 2.7% (deviation 2.7 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 33.3% vs overall 45.5%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 25.9% vs overall 20.5%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 40.7% vs overall 34.0%
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **11.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **12.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=7, fgte=7 rows)
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=25 positions=1..25 teams=25
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=25 positions=1..25 teams=25
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=25 positions=1..25 teams=25
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
