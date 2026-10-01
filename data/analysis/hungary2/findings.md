# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:54:50+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: NB II. (Hungary)
- Scope: league `hungary2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\hungary2\database_profile.json | yes | yes | 32.12 |
| matches_analysis | E:\football_data_analysis\data\analysis\hungary2\matches_analysis.json | yes | yes | 7.65 |
| goals_analysis | E:\football_data_analysis\data\analysis\hungary2\goals_analysis.json | yes | yes | 6.23 |
| teams_analysis | E:\football_data_analysis\data\analysis\hungary2\teams_analysis.json | yes | yes | 29.24 |
| season_trends | E:\football_data_analysis\data\analysis\hungary2\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\hungary2\scoreline_analysis.json | yes | yes | 53.77 |
| relationships | E:\football_data_analysis\data\analysis\hungary2\relationships.json | yes | yes | 14.32 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 301 matches: home wins 45.5%, draws 24.6%, away wins 29.9% (137H / 74D / 90A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 6 home and 2 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 80 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 301 matches produced 774 goals (avg 2.571 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.0% vs away 45.0% of 774 goals in total (home/away ratio 1.22)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 149 of 301 matches (49.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 95 scoring matches, 33.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.85, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Kecskemeti TE leads with 68 points across 2 seasons (0 title(s), GD 17)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (Ajka, BVSC-Zuglo, Csakvari, Karcagi, Kecskemeti TE...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Soroksar earns 21 more points at home than away (37 home vs 16 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Vasas won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Soroksar beat Kecskemeti TE by 3 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.312 per match): first half 2.508 vs last half 2.82 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.375)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 39 matches (13.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (35 of 137 home matches, 25.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (39 of 74 draw matches, 52.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (27 of 90 away matches, 30.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 7 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_rest_days |corr| = 0.1261 (n=232 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 5.38: home 19.743, draw 16.567, away 21.947
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 301 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 301 |
| Average goals per match | 2.571 |
| Home win rate | 45.5% |
| Draw rate | 24.6% |
| Away win rate | 29.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Kecskemeti TE |
| Champion with most titles | Vasas |
| BTTS rate | 49.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.12 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 7.65 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.23 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 29.24 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 53.77 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.32 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 61 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.3% vs overall 5.6% (deviation 2.3 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 52.5% vs overall 45.5%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 24.6% vs overall 29.9%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=7, fgte=7 rows)
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
