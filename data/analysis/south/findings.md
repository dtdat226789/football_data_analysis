# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:47:44+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: National League South (England)
- Scope: league `south`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\south\database_profile.json | yes | yes | 33.46 |
| matches_analysis | E:\football_data_analysis\data\analysis\south\matches_analysis.json | yes | yes | 12.78 |
| goals_analysis | E:\football_data_analysis\data\analysis\south\goals_analysis.json | yes | yes | 6.36 |
| teams_analysis | E:\football_data_analysis\data\analysis\south\teams_analysis.json | yes | yes | 89.73 |
| season_trends | E:\football_data_analysis\data\analysis\south\season_trends.json | yes | yes | 3.97 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\south\scoreline_analysis.json | yes | yes | 121.27 |
| relationships | E:\football_data_analysis\data\analysis\south\relationships.json | yes | yes | 14.38 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 716 matches: home wins 45.7%, draws 23.2%, away wins 31.1% (327H / 166D / 223A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 17 home and 18 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 196 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 716 matches produced 2027 goals (avg 2.831 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.5% vs away 44.5% of 2027 goals in total (home/away ratio 1.25)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 394 of 716 matches (55.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 240 scoring matches, 35.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.67, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Maidstone leads with 99 points across 2 seasons (1 title(s), GD 31)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 18 teams present in every one of the 2 seasons (AFC Totton, Chelmsford, Chesham, Dag & Red, Dorking...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Weston-super earns 48 more points at home than away (48 home vs 0 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Worthing won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Worthing beat Hornchurch by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.040 per match): first half 2.825 vs last half 2.865 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 21.083)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 3.417)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 84 matches (11.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (84 of 327 home matches, 25.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (77 of 166 draw matches, 46.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (72 of 223 away matches, 32.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 20 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_conceded_last_5 |corr| = 0.1373 (n=716 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 5.886: home 29.211, draw 23.325, away 23.516
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (18)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 716 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 716 |
| Average goals per match | 2.831 |
| Home win rate | 45.7% |
| Draw rate | 23.2% |
| Away win rate | 31.1% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Maidstone |
| Champion with most titles | Worthing |
| BTTS rate | 55.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 33.46 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 12.78 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.36 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 89.73 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.97 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 121.27 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.38 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 605 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 72 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 111 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.5% vs overall 6.1% (deviation 1.6 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 34.2% vs overall 45.7%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 27.9% vs overall 23.2%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 37.8% vs overall 31.1%
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 8 match(es) with >= 8 total goals (extreme scorelines)
- **11.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **12.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=29, fgte=29 rows)
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=72 positions=1..72 teams=72
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=72 positions=1..72 teams=72
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=72 positions=1..72 teams=72
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=24 positions=1..24 teams=24
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=24 positions=1..24 teams=24
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=24 positions=1..24 teams=24

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
