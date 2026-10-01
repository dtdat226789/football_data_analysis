# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:05:55+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Championship (Scotland)
- Scope: league `scot-champ`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\scot-champ\database_profile.json | yes | yes | 31.95 |
| matches_analysis | E:\football_data_analysis\data\analysis\scot-champ\matches_analysis.json | yes | yes | 8.22 |
| goals_analysis | E:\football_data_analysis\data\analysis\scot-champ\goals_analysis.json | yes | yes | 6.16 |
| teams_analysis | E:\football_data_analysis\data\analysis\scot-champ\teams_analysis.json | yes | yes | 23.97 |
| season_trends | E:\football_data_analysis\data\analysis\scot-champ\season_trends.json | yes | yes | 3.97 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\scot-champ\scoreline_analysis.json | yes | yes | 38.56 |
| relationships | E:\football_data_analysis\data\analysis\scot-champ\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 231 matches: home wins 40.3%, draws 32.0%, away wins 27.7% (93H / 74D / 64A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 1 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 60 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 231 matches produced 540 goals (avg 2.338 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.2% vs away 44.8% of 540 goals in total (home/away ratio 1.23)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 107 of 231 matches (46.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 60 scoring matches, 29.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.51, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Partick Thistle leads with 85 points across 2 seasons (0 title(s), GD 22)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 8 teams present in every one of the 2 seasons (Arbroath, Ayr, Dunfermline, Morton, Partick Thistle...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Partick Thistle earns 27 more points at home than away (56 home vs 29 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — St Johnstone won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: St Johnstone beat Partick Thistle by 7 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.470 per match): first half 2.421 vs last half 1.951 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 4.200)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.400)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 33 matches (14.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (22 of 93 home matches, 23.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (33 of 74 draw matches, 44.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (20 of 64 away matches, 31.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 1 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_conceded_avg |corr| = -0.118 (n=190 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 7.523: home 26.446, draw 22.828, away 18.923
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 231 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 231 |
| Average goals per match | 2.338 |
| Home win rate | 40.3% |
| Draw rate | 32.0% |
| Away win rate | 27.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Partick Thistle |
| Champion with most titles | St Johnstone |
| BTTS rate | 46.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.95 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.22 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.16 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 23.97 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.97 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 38.56 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 190 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 13 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 41 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 10 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 1.951 vs overall 2.338 (deviation 0.387)
- **7.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 9.8% vs overall 12.6% (deviation 2.8 pp)
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 46.3% vs overall 40.3%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 24.4% vs overall 32.0%
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=26, fgte=26 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=13 positions=1..13 teams=13
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=13 positions=1..13 teams=13
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=13 positions=1..13 teams=13
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=10 positions=1..10 teams=10
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=10 positions=1..10 teams=10
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
