# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:06:10+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premiership (Scotland)
- Scope: league `scot-premier`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\scot-premier\database_profile.json | yes | yes | 32.91 |
| matches_analysis | E:\football_data_analysis\data\analysis\scot-premier\matches_analysis.json | yes | yes | 9.48 |
| goals_analysis | E:\football_data_analysis\data\analysis\scot-premier\goals_analysis.json | yes | yes | 6.32 |
| teams_analysis | E:\football_data_analysis\data\analysis\scot-premier\teams_analysis.json | yes | yes | 25.12 |
| season_trends | E:\football_data_analysis\data\analysis\scot-premier\season_trends.json | yes | yes | 3.92 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\scot-premier\scoreline_analysis.json | yes | yes | 48.58 |
| relationships | E:\football_data_analysis\data\analysis\scot-premier\relationships.json | yes | yes | 14.32 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 276 matches: home wins 43.8%, draws 26.4%, away wins 29.7% (121H / 73D / 82A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 9 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 78 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 276 matches produced 750 goals (avg 2.717 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.7% vs away 44.3% of 750 goals in total (home/away ratio 1.26)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 143 of 276 matches (51.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 80 scoring matches, 31.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.15, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Celtic leads with 100 points across 2 seasons (2 title(s), GD 42)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 11 teams present in every one of the 2 seasons (Aberdeen, Celtic, Dundee FC, Dundee Utd, Falkirk...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Dundee FC earns 24 more points at home than away (38 home vs 14 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Celtic won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Celtic beat Hearts by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.200 per match): first half 2.748 vs last half 2.548 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 4.500)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.667)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 31 matches (11.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (29 of 121 home matches, 24.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (31 of 73 draw matches, 42.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (23 of 82 away matches, 28.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 5 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_points_before_match |corr| = 0.163 (n=234 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 12.566: home 29.848, draw 17.281, away 22.600
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (18)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 276 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 276 |
| Average goals per match | 2.717 |
| Home win rate | 43.8% |
| Draw rate | 26.4% |
| Away win rate | 29.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Celtic |
| Champion with most titles | Celtic |
| BTTS rate | 51.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.91 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.48 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.32 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 25.12 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.92 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 48.58 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.32 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 234 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 15 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 42 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.8% vs overall 6.9% (deviation 2.1 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 38.1% vs overall 43.8%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 21.4% vs overall 26.4%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 40.5% vs overall 29.7%
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **11.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows)
- **12.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=26, fgte=26 rows)
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=15 positions=1..15 teams=15
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=15 positions=1..15 teams=15
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=15 positions=1..15 teams=15
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
