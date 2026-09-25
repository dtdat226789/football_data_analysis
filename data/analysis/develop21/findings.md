# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:57:24+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\develop21\database_profile.json | yes | yes | 27.92 |
| matches_analysis | E:\football_data_analysis\data\analysis\develop21\matches_analysis.json | yes | yes | 6.26 |
| goals_analysis | E:\football_data_analysis\data\analysis\develop21\goals_analysis.json | yes | yes | 5.09 |
| teams_analysis | E:\football_data_analysis\data\analysis\develop21\teams_analysis.json | yes | yes | 26.48 |
| season_trends | E:\football_data_analysis\data\analysis\develop21\season_trends.json | yes | yes | 2.57 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\develop21\scoreline_analysis.json | yes | yes | 12.21 |
| relationships | E:\football_data_analysis\data\analysis\develop21\relationships.json | yes | yes | 14.25 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 34 matches: home wins 41.2%, draws 26.5%, away wins 32.4% (14H / 9D / 11A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 2 home and 1 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 10 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 34 matches produced 140 goals (avg 4.118 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.7% vs away 44.3% of 140 goals in total (home/away ratio 1.26)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 23 of 34 matches (67.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 16-30 (first goal in 13 scoring matches, 39.4% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 22.70, median 19.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Bolton U21 leads with 15 points across 1 seasons (1 title(s), GD 15)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 17 teams present in every one of the 1 seasons (Barnsley U21, Bolton U21, Bristol City U21, Cardiff U21, Charlton U21...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Sheffield Wed U21 earns 4 more points at home than away (5 home vs 1 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Bolton U21 won 1 of 1 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Bolton U21 beat Fleetwood U21 by 6 pts
- **F14** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 6.000)
- **F15** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.235)
- **F16** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-2 in 4 matches (11.8%)
- **F17** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 3-1 (4 of 14 home matches, 28.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 2-2 (4 of 9 draw matches, 44.4%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-2 (2 of 11 away matches, 18.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 5 match(es) with >= 7 total goals
- **F21** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.4016 (n=34 leakage-safe rows)
- **F22** · `relationships` · *[medium]* — **Most outcome-separating feature** — position_difference spreads group means over 3.535: home 0.357, draw -2.444, away 1.091
- **F23** · `database_profile` · *[high]* — **Data-quality warnings (9)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F24** · `database_profile` · *[medium]* — **Data coverage** — 1 of 1 registered seasons populated (100.0%); 34 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 34 |
| Average goals per match | 4.118 |
| Home win rate | 41.2% |
| Draw rate | 26.5% |
| Away win rate | 32.4% |
| Most common scoreline | 2-2 |
| Dominant team (lifetime points) | Bolton U21 |
| Champion with most titles | Bolton U21 |
| BTTS rate | 67.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 27.92 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 6.26 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 5.09 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 26.48 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 2.57 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 12.21 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.25 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 34 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 17 teams, expected 20
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **4.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **5.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **6.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **7.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=17 positions=1..17 teams=17
- **8.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=17 positions=1..17 teams=17
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=17 positions=1..17 teams=17

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
