# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:50:07+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Ligue 1 (France)
- Scope: league `france1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\france1\database_profile.json | yes | yes | 32.85 |
| matches_analysis | E:\football_data_analysis\data\analysis\france1\matches_analysis.json | yes | yes | 8.85 |
| goals_analysis | E:\football_data_analysis\data\analysis\france1\goals_analysis.json | yes | yes | 6.31 |
| teams_analysis | E:\football_data_analysis\data\analysis\france1\teams_analysis.json | yes | yes | 32.05 |
| season_trends | E:\football_data_analysis\data\analysis\france1\season_trends.json | yes | yes | 3.90 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\france1\scoreline_analysis.json | yes | yes | 63.33 |
| relationships | E:\football_data_analysis\data\analysis\france1\relationships.json | yes | yes | 14.32 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 355 matches: home wins 45.4%, draws 25.1%, away wins 29.6% (161H / 89D / 105A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 7 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 98 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 355 matches produced 1002 goals (avg 2.823 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.0% vs away 44.0% of 1002 goals in total (home/away ratio 1.27)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 184 of 355 matches (51.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 110 scoring matches, 33.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.32, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — PSG leads with 84 points across 2 seasons (1 title(s), GD 46)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 16 teams present in every one of the 2 seasons (Angers, Auxerre, Brest, Le Havre, Lens...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Marseille earns 18 more points at home than away (40 home vs 22 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — PSG won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Monaco beat Lyon by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.025 per match): first half 2.819 vs last half 2.844 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 6.333)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.556)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 40 matches (11.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (40 of 161 home matches, 24.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (32 of 89 draw matches, 36.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (27 of 105 away matches, 25.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 16 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_conceded_last_5 |corr| = -0.1251 (n=310 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 8.628: home 3.189, draw -0.039, away -5.440
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 355 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 355 |
| Average goals per match | 2.823 |
| Home win rate | 45.4% |
| Draw rate | 25.1% |
| Away win rate | 29.6% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | PSG |
| Champion with most titles | PSG |
| BTTS rate | 51.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.85 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.85 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.31 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 32.05 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.90 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 63.33 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.32 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 310 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 21 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 45 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 40.0% vs overall 45.4%
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 7 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=21 positions=1..21 teams=21
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=21 positions=1..21 teams=21
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=21 positions=1..21 teams=21
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
