# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:58:56+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Ligue 2 (France)
- Scope: league `france2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\france2\database_profile.json | yes | yes | 31.84 |
| matches_analysis | E:\football_data_analysis\data\analysis\france2\matches_analysis.json | yes | yes | 9.77 |
| goals_analysis | E:\football_data_analysis\data\analysis\france2\goals_analysis.json | yes | yes | 6.23 |
| teams_analysis | E:\football_data_analysis\data\analysis\france2\teams_analysis.json | yes | yes | 32.05 |
| season_trends | E:\football_data_analysis\data\analysis\france2\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\france2\scoreline_analysis.json | yes | yes | 60.17 |
| relationships | E:\football_data_analysis\data\analysis\france2\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 373 matches: home wins 37.0%, draws 31.6%, away wins 31.4% (138H / 118D / 117A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 12 home and 8 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 72 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 373 matches produced 946 goals (avg 2.536 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 51.9% vs away 48.1% of 946 goals in total (home/away ratio 1.08)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 197 of 373 matches (52.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 106 scoring matches, 31.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.13, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — St Etienne leads with 79 points across 2 seasons (1 title(s), GD 33)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 14 teams present in every one of the 2 seasons (Annecy, Boulogne, Clermont, Dunkerque, Grenoble...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Troyes earns 19 more points at home than away (43 home vs 24 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Troyes won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: St Etienne beat Red Star by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.042 per match): first half 2.529 vs last half 2.571 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 5.778)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.667)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 49 matches (13.1%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (48 of 138 home matches, 34.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (49 of 118 draw matches, 41.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (33 of 117 away matches, 28.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 11 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_conceded_last_5 |corr| = 0.0883 (n=373 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.421: home 2.036, draw -0.737, away -2.385
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 373 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 373 |
| Average goals per match | 2.536 |
| Home win rate | 37.0% |
| Draw rate | 31.6% |
| Away win rate | 31.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | St Etienne |
| Champion with most titles | Troyes |
| BTTS rate | 52.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.84 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.77 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.23 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 32.05 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 60.17 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 310 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 63 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 36.5% vs overall 31.6%
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
