# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:43:52+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Saudi Professional League (Saudi Arabia)
- Scope: league `saudi1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\saudi1\database_profile.json | yes | yes | 32.93 |
| matches_analysis | E:\football_data_analysis\data\analysis\saudi1\matches_analysis.json | yes | yes | 8.62 |
| goals_analysis | E:\football_data_analysis\data\analysis\saudi1\goals_analysis.json | yes | yes | 6.28 |
| teams_analysis | E:\football_data_analysis\data\analysis\saudi1\teams_analysis.json | yes | yes | 31.57 |
| season_trends | E:\football_data_analysis\data\analysis\saudi1\season_trends.json | yes | yes | 3.98 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\saudi1\scoreline_analysis.json | yes | yes | 66.45 |
| relationships | E:\football_data_analysis\data\analysis\saudi1\relationships.json | yes | yes | 14.39 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 377 matches: home wins 43.2%, draws 24.1%, away wins 32.6% (163H / 91D / 123A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 5 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 102 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 377 matches produced 1117 goals (avg 2.963 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.6% vs away 47.4% of 1117 goals in total (home/away ratio 1.11)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 213 of 377 matches (56.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 132 scoring matches, 37.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.23, median 22.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Al Hilal leads with 103 points across 2 seasons (1 title(s), GD 76)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 15 teams present in every one of the 2 seasons (Al Ahli SC, Al Ettifaq, Al Fateh, Al Fayha, Al Hazem...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Al Ahli SC earns 15 more points at home than away (54 home vs 39 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Al Nassr won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Al Nassr beat Al Hilal by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.241 per match): first half 3.003 vs last half 2.762 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.105)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 3.111)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 45 matches (11.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (34 of 163 home matches, 20.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (45 of 91 draw matches, 49.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (24 of 123 away matches, 19.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 11 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_position_before_match |corr| = -0.1105 (n=377 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 16.986: home 6.767, draw 0.187, away -10.220
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (18)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 377 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 377 |
| Average goals per match | 2.963 |
| Home win rate | 43.2% |
| Draw rate | 24.1% |
| Away win rate | 32.6% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Al Hilal |
| Champion with most titles | Al Nassr |
| BTTS rate | 56.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.93 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.62 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.28 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 31.57 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.98 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 66.45 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.39 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 314 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 63 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 5.1% vs overall 6.9% (deviation 1.8 pp)
- **7.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 15.9% vs overall 6.9% (deviation 9.0 pp)
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 38.1% vs overall 43.2%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 30.2% vs overall 24.1%
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **11.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (18 extra rows)
- **12.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows)
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
