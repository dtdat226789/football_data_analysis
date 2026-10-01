# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:05:40+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Division 1 (Saudi Arabia)
- Scope: league `saudi2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\saudi2\database_profile.json | yes | yes | 33.78 |
| matches_analysis | E:\football_data_analysis\data\analysis\saudi2\matches_analysis.json | yes | yes | 9.67 |
| goals_analysis | E:\football_data_analysis\data\analysis\saudi2\goals_analysis.json | yes | yes | 6.33 |
| teams_analysis | E:\football_data_analysis\data\analysis\saudi2\teams_analysis.json | yes | yes | 33.21 |
| season_trends | E:\football_data_analysis\data\analysis\saudi2\season_trends.json | yes | yes | 3.94 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\saudi2\scoreline_analysis.json | yes | yes | 61.83 |
| relationships | E:\football_data_analysis\data\analysis\saudi2\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 362 matches: home wins 39.8%, draws 26.5%, away wins 33.7% (144H / 96D / 122A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 11 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 82 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 362 matches produced 1029 goals (avg 2.843 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.4% vs away 46.6% of 1029 goals in total (home/away ratio 1.14)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 215 of 362 matches (59.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 101 scoring matches, 30.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.97, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Al-Ula leads with 89 points across 2 seasons (1 title(s), GD 48)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (Al Adalah, Al Anwar, Al Bukiryah, Al Jabalain, Al Jandal...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Al Diriyah earns 20 more points at home than away (49 home vs 29 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Abha won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Abha beat Al Diriyah by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.855 per match): first half 2.968 vs last half 2.113 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 6.222)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.889)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 45 matches (12.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (36 of 144 home matches, 25.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (45 of 96 draw matches, 46.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (32 of 122 away matches, 26.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 8 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_goals_avg |corr| = -0.1019 (n=309 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 14.66: home 7.211, draw -1.125, away -7.450
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (20)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 362 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 362 |
| Average goals per match | 2.843 |
| Home win rate | 39.8% |
| Draw rate | 26.5% |
| Away win rate | 33.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Al-Ula |
| Champion with most titles | Abha |
| BTTS rate | 59.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 33.78 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.67 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.33 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 33.21 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.94 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 61.83 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 309 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 53 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025-2026 goalless share 5.2% vs overall 7.5% (deviation 2.3 pp)
- **7.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 2.113 vs overall 2.843 (deviation 0.730)
- **8.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 20.8% vs overall 7.5% (deviation 13.3 pp)
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 30.2% vs overall 39.8%
- **10.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 45.3% vs overall 26.5%
- **11.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 24.5% vs overall 33.7%
- **12.** `HIGH_SCORING_MATCHES` *(warning)* — 3 match(es) with >= 8 total goals (extreme scorelines)
- **13.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (18 extra rows)
- **14.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=26, fgte=26 rows)
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **19.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
