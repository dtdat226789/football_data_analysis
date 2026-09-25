# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:41:43+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Liga Portugal (Portugal)
- Scope: league `portugal1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\portugal1\database_profile.json | yes | yes | 31.42 |
| matches_analysis | E:\football_data_analysis\data\analysis\portugal1\matches_analysis.json | yes | yes | 8.59 |
| goals_analysis | E:\football_data_analysis\data\analysis\portugal1\goals_analysis.json | yes | yes | 6.25 |
| teams_analysis | E:\football_data_analysis\data\analysis\portugal1\teams_analysis.json | yes | yes | 30.58 |
| season_trends | E:\football_data_analysis\data\analysis\portugal1\season_trends.json | yes | yes | 3.95 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\portugal1\scoreline_analysis.json | yes | yes | 61.28 |
| relationships | E:\football_data_analysis\data\analysis\portugal1\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 370 matches: home wins 40.8%, draws 27.6%, away wins 31.6% (151H / 102D / 117A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 5 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 87 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 370 matches produced 993 goals (avg 2.684 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.6% vs away 45.4% of 993 goals in total (home/away ratio 1.20)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 178 of 370 matches (48.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 120 scoring matches, 34.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.21, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — FC Porto leads with 109 points across 2 seasons (2 title(s), GD 63)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 16 teams present in every one of the 2 seasons (Alverca, Arouca, Benfica, Braga, Casa Pia...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Vitoria Guimaraes earns 19 more points at home than away (33 home vs 14 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — FC Porto won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: FC Porto beat Benfica by 5 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.070 per match): first half 2.672 vs last half 2.742 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 5.111)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 3.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 36 matches (9.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (34 of 151 home matches, 22.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (36 of 102 draw matches, 35.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (34 of 117 away matches, 29.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1102 (n=370 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 13.9: home 6.609, draw -1.451, away -7.291
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 370 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 370 |
| Average goals per match | 2.684 |
| Home win rate | 40.8% |
| Draw rate | 27.6% |
| Away win rate | 31.6% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | FC Porto |
| Champion with most titles | FC Porto |
| BTTS rate | 48.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.42 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.59 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.25 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 30.58 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.95 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 61.28 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 308 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 62 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
