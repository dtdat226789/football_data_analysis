# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:48:38+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier League (Egypt)
- Scope: league `egypt`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\egypt\database_profile.json | yes | yes | 30.49 |
| matches_analysis | E:\football_data_analysis\data\analysis\egypt\matches_analysis.json | yes | yes | 8.81 |
| goals_analysis | E:\football_data_analysis\data\analysis\egypt\goals_analysis.json | yes | yes | 6.16 |
| teams_analysis | E:\football_data_analysis\data\analysis\egypt\teams_analysis.json | yes | yes | 33.79 |
| season_trends | E:\football_data_analysis\data\analysis\egypt\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\egypt\scoreline_analysis.json | yes | yes | 55.25 |
| relationships | E:\football_data_analysis\data\analysis\egypt\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 372 matches: home wins 34.4%, draws 35.5%, away wins 30.1% (128H / 132D / 112A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 9 home and 5 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — level at HT -> draw occurred 91 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 372 matches produced 754 goals (avg 2.027 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 50.9% vs away 49.1% of 754 goals in total (home/away ratio 1.04)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 169 of 372 matches (45.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 79 scoring matches, 25.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 37.30, median 35.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Pyramids leads with 69 points across 2 seasons (1 title(s), GD 30)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 17 teams present in every one of the 2 seasons (Al Ahly, Al Ittihad, Al Masry, Arab Contractors, Ceramica Cleopatra...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Ghazl El Mahallah earns 11 more points at home than away (25 home vs 14 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Zamalek won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Zamalek beat Pyramids by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.038 per match): first half 2.022 vs last half 2.06 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.762)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.700)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 59 matches (15.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (51 of 128 home matches, 39.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (59 of 132 draw matches, 44.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (35 of 112 away matches, 31.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 1 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_goals_avg |corr| = 0.1917 (n=322 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.22: home 2.890, draw -0.148, away -3.330
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (12)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 372 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 372 |
| Average goals per match | 2.027 |
| Home win rate | 34.4% |
| Draw rate | 35.5% |
| Away win rate | 30.1% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Pyramids |
| Champion with most titles | Zamalek |
| BTTS rate | 45.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 30.49 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.81 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.16 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 33.79 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 55.25 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 322 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 21 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 50 matches, expected 380
- **4.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 10.0% vs overall 15.1% (deviation 5.1 pp)
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 20.0% vs overall 35.5%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 42.0% vs overall 30.1%
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=21 positions=1..21 teams=21
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=21 positions=1..21 teams=21
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=21 positions=1..21 teams=21

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
