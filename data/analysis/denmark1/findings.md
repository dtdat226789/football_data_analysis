# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:57:07+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Superliga (Denmark)
- Scope: league `denmark1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\denmark1\database_profile.json | yes | yes | 32.23 |
| matches_analysis | E:\football_data_analysis\data\analysis\denmark1\matches_analysis.json | yes | yes | 8.93 |
| goals_analysis | E:\football_data_analysis\data\analysis\denmark1\goals_analysis.json | yes | yes | 6.24 |
| teams_analysis | E:\football_data_analysis\data\analysis\denmark1\teams_analysis.json | yes | yes | 22.96 |
| season_trends | E:\football_data_analysis\data\analysis\denmark1\season_trends.json | yes | yes | 3.95 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\denmark1\scoreline_analysis.json | yes | yes | 45.54 |
| relationships | E:\football_data_analysis\data\analysis\denmark1\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 248 matches: home wins 41.9%, draws 24.6%, away wins 33.5% (104H / 61D / 83A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 7 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 64 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 248 matches produced 763 goals (avg 3.077 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.9% vs away 47.1% of 763 goals in total (home/away ratio 1.12)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 148 of 248 matches (59.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 96 scoring matches, 40.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.05, median 21.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Midtjylland leads with 79 points across 2 seasons (0 title(s), GD 44)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 10 teams present in every one of the 2 seasons (Aarhus, Brondby, FC Copenhagen, Midtjylland, Nordsjaelland...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Nordsjaelland earns 17 more points at home than away (42 home vs 25 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Aarhus won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: FC Copenhagen beat Midtjylland by 5 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.122 per match): first half 3.104 vs last half 2.982 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 4.167)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.833)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 27 matches (10.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (25 of 104 home matches, 24.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (27 of 61 draw matches, 44.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (21 of 83 away matches, 25.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 6 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — rest_days_difference |corr| = -0.1448 (n=236 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 4.15: home 1.596, draw -0.590, away -2.554
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 248 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 248 |
| Average goals per match | 3.077 |
| Home win rate | 41.9% |
| Draw rate | 24.6% |
| Away win rate | 33.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Midtjylland |
| Champion with most titles | Aarhus |
| BTTS rate | 59.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.23 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.93 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.24 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 22.96 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.95 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 45.54 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 193 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 55 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 1.8% vs overall 4.8% (deviation 3.0 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 29.1% vs overall 24.6%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 27.3% vs overall 33.5%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=12 positions=1..12 teams=12
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=12 positions=1..12 teams=12
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=12 positions=1..12 teams=12
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
