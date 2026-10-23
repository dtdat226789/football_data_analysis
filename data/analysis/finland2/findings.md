# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:49:52+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Ykkosliiga (Finland)
- Scope: league `finland2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\finland2\database_profile.json | yes | yes | 31.28 |
| matches_analysis | E:\football_data_analysis\data\analysis\finland2\matches_analysis.json | yes | yes | 8.92 |
| goals_analysis | E:\football_data_analysis\data\analysis\finland2\goals_analysis.json | yes | yes | 6.35 |
| teams_analysis | E:\football_data_analysis\data\analysis\finland2\teams_analysis.json | yes | yes | 26.81 |
| season_trends | E:\football_data_analysis\data\analysis\finland2\season_trends.json | yes | yes | 3.83 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\finland2\scoreline_analysis.json | yes | yes | 47.10 |
| relationships | E:\football_data_analysis\data\analysis\finland2\relationships.json | yes | yes | 14.32 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 260 matches: home wins 42.3%, draws 24.6%, away wins 33.1% (110H / 64D / 86A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 8 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 70 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 260 matches produced 764 goals (avg 2.938 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.5% vs away 47.5% of 764 goals in total (home/away ratio 1.10)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 150 of 260 matches (57.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 93 scoring matches, 37.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.53, median 20.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — PK-35 leads with 91 points across 2 seasons (0 title(s), GD 32)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 7 teams present in every one of the 2 seasons (Ekenas, JaPS, Jippo, KaPa, Klubi 04...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — JaPS earns 15 more points at home than away (41 home vs 26 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Lahti won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025: Lahti beat TPS by 7 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.713 per match): first half 3.281 vs last half 2.568 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025 (luck view, avg abs position diff 5.700)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026 (luck view, avg abs position diff 1.600)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 30 matches (11.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (23 of 110 home matches, 20.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (30 of 64 draw matches, 46.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (22 of 86 away matches, 25.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 10 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.1562 (n=135 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 8.173: home 4.483, draw -1.314, away -3.690
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (13)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 260 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 260 |
| Average goals per match | 2.938 |
| Home win rate | 42.3% |
| Draw rate | 24.6% |
| Away win rate | 33.1% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | PK-35 |
| Champion with most titles | Lahti |
| BTTS rate | 57.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.28 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.92 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.35 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 26.81 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.83 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 47.10 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.32 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 135 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 125 matches, expected 380
- **3.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **4.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025 goalless share 3.7% vs overall 5.4% (deviation 1.7 pp)
- **6.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026 avg goals 2.568 vs overall 2.938 (deviation 0.370)
- **7.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 7.2% vs overall 5.4% (deviation 1.8 pp)
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
