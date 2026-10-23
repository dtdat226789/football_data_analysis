# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:01:36+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: TOPLYGA (Lithuania)
- Scope: league `lithuania`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\lithuania\database_profile.json | yes | yes | 31.43 |
| matches_analysis | E:\football_data_analysis\data\analysis\lithuania\matches_analysis.json | yes | yes | 8.71 |
| goals_analysis | E:\football_data_analysis\data\analysis\lithuania\goals_analysis.json | yes | yes | 6.12 |
| teams_analysis | E:\football_data_analysis\data\analysis\lithuania\teams_analysis.json | yes | yes | 21.02 |
| season_trends | E:\football_data_analysis\data\analysis\lithuania\season_trends.json | yes | yes | 3.87 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\lithuania\scoreline_analysis.json | yes | yes | 54.81 |
| relationships | E:\football_data_analysis\data\analysis\lithuania\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 324 matches: home wins 40.1%, draws 25.9%, away wins 34.0% (130H / 84D / 110A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 7 home and 7 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 84 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 324 matches produced 860 goals (avg 2.654 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.0% vs away 46.0% of 860 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 160 of 324 matches (49.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 87 scoring matches, 29.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.58, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Kauno Zalgiris leads with 132 points across 2 seasons (2 title(s), GD 82)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 8 teams present in every one of the 2 seasons (Banga, Dziugas Telsiai, FK Panevezys, Hegelmann, Kauno Zalgiris...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Zalgiris earns 16 more points at home than away (63 home vs 47 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Kauno Zalgiris won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026: Kauno Zalgiris beat Suduva by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (-0.015 per match): first half 2.661 vs last half 2.646 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025 (goals view, avg abs position diff 4.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 1.600)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 34 matches (10.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (27 of 130 home matches, 20.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (34 of 84 draw matches, 40.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (27 of 110 away matches, 24.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 5 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_win_rate |corr| = -0.2476 (n=180 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 10.652: home 4.795, draw -0.386, away -5.857
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 324 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 324 |
| Average goals per match | 2.654 |
| Home win rate | 40.1% |
| Draw rate | 25.9% |
| Away win rate | 34.0% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Kauno Zalgiris |
| Champion with most titles | Kauno Zalgiris |
| BTTS rate | 49.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.43 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.71 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.12 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 21.02 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.87 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 54.81 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 180 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 144 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025 goalless share 7.2% vs overall 9.0% (deviation 1.8 pp)
- **7.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 11.1% vs overall 9.0% (deviation 2.1 pp)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=18, fgte=18 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=10 positions=1..10 teams=10
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=10 positions=1..10 teams=10
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=10 positions=1..10 teams=10
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
