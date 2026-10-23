# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:06:25+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: League One (Scotland)
- Scope: league `scot1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\scot1\database_profile.json | yes | yes | 31.98 |
| matches_analysis | E:\football_data_analysis\data\analysis\scot1\matches_analysis.json | yes | yes | 7.83 |
| goals_analysis | E:\football_data_analysis\data\analysis\scot1\goals_analysis.json | yes | yes | 6.31 |
| teams_analysis | E:\football_data_analysis\data\analysis\scot1\teams_analysis.json | yes | yes | 25.02 |
| season_trends | E:\football_data_analysis\data\analysis\scot1\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\scot1\scoreline_analysis.json | yes | yes | 41.53 |
| relationships | E:\football_data_analysis\data\analysis\scot1\relationships.json | yes | yes | 14.32 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 230 matches: home wins 43.0%, draws 26.5%, away wins 30.4% (99H / 61D / 70A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 6 home and 3 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 62 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 230 matches produced 614 goals (avg 2.670 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.0% vs away 45.0% of 614 goals in total (home/away ratio 1.23)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 120 of 230 matches (52.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 74 scoring matches, 34.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.02, median 24.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Hamilton leads with 84 points across 2 seasons (0 title(s), GD 31)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 8 teams present in every one of the 2 seasons (Airdrieonians, Alloa, Cove Rangers, East Fife, Hamilton...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Hamilton earns 16 more points at home than away (50 home vs 34 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Inverness won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Ross County beat Hamilton by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (-0.034 per match): first half 2.675 vs last half 2.641 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.571)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 34 matches (14.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (21 of 99 home matches, 21.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (34 of 61 draw matches, 55.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-2 (17 of 70 away matches, 24.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 4 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_win_rate |corr| = -0.2566 (n=191 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 10.09: home 5.412, draw -3.750, away -4.678
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 230 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 230 |
| Average goals per match | 2.67 |
| Home win rate | 43.0% |
| Draw rate | 26.5% |
| Away win rate | 30.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Hamilton |
| Champion with most titles | Inverness |
| BTTS rate | 52.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.98 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 7.83 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.31 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 25.02 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 41.53 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.32 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 191 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 14 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 39 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 10 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 10.3% vs overall 6.1% (deviation 4.2 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 48.7% vs overall 43.0%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=26, fgte=26 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=14 positions=1..14 teams=14
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=14 positions=1..14 teams=14
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=14 positions=1..14 teams=14
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=10 positions=1..10 teams=10
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=10 positions=1..10 teams=10
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
