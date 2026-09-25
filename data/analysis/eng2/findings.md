# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:57:59+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: League Two (England)
- Scope: league `eng2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\eng2\database_profile.json | yes | yes | 32.98 |
| matches_analysis | E:\football_data_analysis\data\analysis\eng2\matches_analysis.json | yes | yes | 11.72 |
| goals_analysis | E:\football_data_analysis\data\analysis\eng2\goals_analysis.json | yes | yes | 6.25 |
| teams_analysis | E:\football_data_analysis\data\analysis\eng2\teams_analysis.json | yes | yes | 39.72 |
| season_trends | E:\football_data_analysis\data\analysis\eng2\season_trends.json | yes | yes | 3.92 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\eng2\scoreline_analysis.json | yes | yes | 103.26 |
| relationships | E:\football_data_analysis\data\analysis\eng2\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 641 matches: home wins 43.1%, draws 26.4%, away wins 30.6% (276H / 169D / 196A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 20 home and 10 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 143 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 641 matches produced 1646 goals (avg 2.568 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.5% vs away 45.5% of 1646 goals in total (home/away ratio 1.20)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 335 of 641 matches (52.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 189 scoring matches, 31.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.36, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Salford leads with 95 points across 2 seasons (0 title(s), GD 7)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 18 teams present in every one of the 2 seasons (Accrington, Barnet, Bristol Rovers, Cheltenham, Chesterfield...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Shrewsbury earns 22 more points at home than away (39 home vs 17 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Notts Co won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Notts Co beat Bromley by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.051 per match): first half 2.575 vs last half 2.524 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 7.333)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 2.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 78 matches (12.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (77 of 276 home matches, 27.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (78 of 169 draw matches, 46.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (52 of 196 away matches, 26.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 8 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_wins_last_5 |corr| = 0.0526 (n=641 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.664: home 2.511, draw 0.112, away -4.153
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (18)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 641 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 641 |
| Average goals per match | 2.568 |
| Home win rate | 43.1% |
| Draw rate | 26.4% |
| Away win rate | 30.6% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Salford |
| Champion with most titles | Notts Co |
| BTTS rate | 52.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.98 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 11.72 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.25 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.72 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.92 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 103.26 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 557 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 24 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 84 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 9.5% vs overall 7.0% (deviation 2.5 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 51.2% vs overall 43.1%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 35.7% vs overall 26.4%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 13.1% vs overall 30.6%
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **11.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **12.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=24 positions=1..24 teams=24
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=24 positions=1..24 teams=24
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=24 positions=1..24 teams=24
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=24 positions=1..24 teams=24
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=24 positions=1..24 teams=24
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=24 positions=1..24 teams=24

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
