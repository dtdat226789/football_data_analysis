# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:01:37+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Division 1 (Ireland)
- Scope: league `ireland2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\ireland2\database_profile.json | yes | yes | 31.01 |
| matches_analysis | E:\football_data_analysis\data\analysis\ireland2\matches_analysis.json | yes | yes | 9.91 |
| goals_analysis | E:\football_data_analysis\data\analysis\ireland2\goals_analysis.json | yes | yes | 6.28 |
| teams_analysis | E:\football_data_analysis\data\analysis\ireland2\teams_analysis.json | yes | yes | 19.85 |
| season_trends | E:\football_data_analysis\data\analysis\ireland2\season_trends.json | yes | yes | 3.87 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\ireland2\scoreline_analysis.json | yes | yes | 59.48 |
| relationships | E:\football_data_analysis\data\analysis\ireland2\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 339 matches: home wins 47.8%, draws 23.3%, away wins 28.9% (162H / 79D / 98A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 16 home and 5 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 97 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 339 matches produced 941 goals (avg 2.776 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.5% vs away 42.5% of 941 goals in total (home/away ratio 1.35)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 180 of 339 matches (53.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 112 scoring matches, 35.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.94, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Cobh Ramblers leads with 114 points across 2 seasons (0 title(s), GD 25)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 2 seasons (Athlone, Bray, Cobh Ramblers, Finn Harps, Kerry...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Bray earns 36 more points at home than away (74 home vs 38 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Dundalk won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025: Dundalk beat Cobh Ramblers by 10 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.060 per match): first half 2.804 vs last half 2.744 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025 (goals view, avg abs position diff 2.200)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 1.200)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 39 matches (11.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (39 of 162 home matches, 24.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (36 of 79 draw matches, 45.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (34 of 98 away matches, 34.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 9 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.3125 (n=339 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.371: home 3.463, draw -2.430, away -3.908
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 339 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 339 |
| Average goals per match | 2.776 |
| Home win rate | 47.8% |
| Draw rate | 23.3% |
| Away win rate | 28.9% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | Cobh Ramblers |
| Champion with most titles | Dundalk |
| BTTS rate | 53.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.01 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.91 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.28 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 19.85 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.87 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 59.48 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 179 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 160 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=8, fgte=8 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=10 positions=1..10 teams=10
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=10 positions=1..10 teams=10
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=10 positions=1..10 teams=10
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
