# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:49:38+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Veikkausliiga (Finland)
- Scope: league `finland1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\finland1\database_profile.json | yes | yes | 31.98 |
| matches_analysis | E:\football_data_analysis\data\analysis\finland1\matches_analysis.json | yes | yes | 9.60 |
| goals_analysis | E:\football_data_analysis\data\analysis\finland1\goals_analysis.json | yes | yes | 6.36 |
| teams_analysis | E:\football_data_analysis\data\analysis\finland1\teams_analysis.json | yes | yes | 22.54 |
| season_trends | E:\football_data_analysis\data\analysis\finland1\season_trends.json | yes | yes | 3.87 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\finland1\scoreline_analysis.json | yes | yes | 48.33 |
| relationships | E:\football_data_analysis\data\analysis\finland1\relationships.json | yes | yes | 14.32 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 273 matches: home wins 43.6%, draws 24.5%, away wins 31.9% (119H / 67D / 87A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 11 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 69 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 273 matches produced 789 goals (avg 2.890 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.4% vs away 46.6% of 789 goals in total (home/away ratio 1.14)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 152 of 273 matches (55.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 85 scoring matches, 33.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.95, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Inter Turku leads with 94 points across 2 seasons (1 title(s), GD 40)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 10 teams present in every one of the 2 seasons (AC Oulu, Gnistan, HJK, Ilves, Inter Turku...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Ilves earns 20 more points at home than away (45 home vs 25 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Inter Turku won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026: KuPS beat Inter Turku by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.755 per match): first half 3.28 vs last half 2.525 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026 (goals view, avg abs position diff 5.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 2.167)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 32 matches (11.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (26 of 119 home matches, 21.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (32 of 67 draw matches, 47.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (22 of 87 away matches, 25.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 6 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_rest_days |corr| = 0.1563 (n=126 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 8.329: home 3.839, draw -1.655, away -4.489
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 273 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 273 |
| Average goals per match | 2.89 |
| Home win rate | 43.6% |
| Draw rate | 24.5% |
| Away win rate | 31.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Inter Turku |
| Champion with most titles | Inter Turku |
| BTTS rate | 55.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.98 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.60 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.36 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 22.54 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.87 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 48.33 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.32 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 132 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 141 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 12 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2025 avg goals 3.28 vs overall 2.89 (deviation 0.390)
- **7.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026 avg goals 2.525 vs overall 2.89 (deviation 0.365)
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=12 positions=1..12 teams=12
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=12 positions=1..12 teams=12
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=12 positions=1..12 teams=12
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=12 positions=1..12 teams=12
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=12 positions=1..12 teams=12
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
