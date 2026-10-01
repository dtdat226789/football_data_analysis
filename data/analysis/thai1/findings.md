# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:10:24+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Thai League 1 (Thailand)
- Scope: league `thai1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\thai1\database_profile.json | yes | yes | 32.73 |
| matches_analysis | E:\football_data_analysis\data\analysis\thai1\matches_analysis.json | yes | yes | 9.20 |
| goals_analysis | E:\football_data_analysis\data\analysis\thai1\goals_analysis.json | yes | yes | 6.31 |
| teams_analysis | E:\football_data_analysis\data\analysis\thai1\teams_analysis.json | yes | yes | 28.62 |
| season_trends | E:\football_data_analysis\data\analysis\thai1\season_trends.json | yes | yes | 3.94 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\thai1\scoreline_analysis.json | yes | yes | 45.33 |
| relationships | E:\football_data_analysis\data\analysis\thai1\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 264 matches: home wins 43.2%, draws 29.9%, away wins 26.9% (114H / 79D / 71A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 8 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 70 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 264 matches produced 704 goals (avg 2.667 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 58.1% vs away 41.9% of 704 goals in total (home/away ratio 1.39)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 148 of 264 matches (56.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 81 scoring matches, 32.9% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.55, median 27.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Buriram leads with 77 points across 2 seasons (2 title(s), GD 48)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (Ayutthaya Utd, Bangkok Utd, Buriram, Chiangrai Utd, Chonburi...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Sukhothai earns 23 more points at home than away (27 home vs 4 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Buriram won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Buriram beat Rayong FC by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.092 per match): first half 2.675 vs last half 2.583 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 4.875)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 2.125)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 46 matches (17.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (26 of 114 home matches, 22.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (46 of 79 draw matches, 58.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (21 of 71 away matches, 29.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 7 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_rest_days |corr| = -0.1222 (n=232 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 9.484: home 3.615, draw -1.933, away -5.869
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 264 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 264 |
| Average goals per match | 2.667 |
| Home win rate | 43.2% |
| Draw rate | 29.9% |
| Away win rate | 26.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Buriram |
| Champion with most titles | Buriram |
| BTTS rate | 56.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.73 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.20 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.31 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 28.62 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.94 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 45.33 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.2% vs overall 6.8% (deviation 2.6 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 16.7% vs overall 29.9%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 41.7% vs overall 26.9%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 3 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=30, fgte=30 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=16 positions=1..16 teams=16
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=16 positions=1..16 teams=16
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=16 positions=1..16 teams=16
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
