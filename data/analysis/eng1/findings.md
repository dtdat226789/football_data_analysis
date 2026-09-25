# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:57:46+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: League One (England)
- Scope: league `eng1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\eng1\database_profile.json | yes | yes | 32.46 |
| matches_analysis | E:\football_data_analysis\data\analysis\eng1\matches_analysis.json | yes | yes | 11.77 |
| goals_analysis | E:\football_data_analysis\data\analysis\eng1\goals_analysis.json | yes | yes | 6.33 |
| teams_analysis | E:\football_data_analysis\data\analysis\eng1\teams_analysis.json | yes | yes | 40.83 |
| season_trends | E:\football_data_analysis\data\analysis\eng1\season_trends.json | yes | yes | 3.95 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\eng1\scoreline_analysis.json | yes | yes | 104.24 |
| relationships | E:\football_data_analysis\data\analysis\eng1\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 640 matches: home wins 44.7%, draws 25.9%, away wins 29.4% (286H / 166D / 188A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 19 home and 11 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 169 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 640 matches produced 1705 goals (avg 2.664 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.8% vs away 44.2% of 1705 goals in total (home/away ratio 1.26)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 341 of 640 matches (53.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 196 scoring matches, 32.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.74, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Lincoln leads with 103 points across 1 seasons (1 title(s), GD 48)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 17 teams present in every one of the 2 seasons (AFC Wimbledon, Barnsley, Blackpool, Bradford City, Burton...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Blackpool earns 24 more points at home than away (46 home vs 22 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Lincoln won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Bradford City beat Sheffield Wed by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.303 per match): first half 2.625 vs last half 2.928 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 7.083)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.833)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 79 matches (12.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (77 of 286 home matches, 26.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (79 of 166 draw matches, 47.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (53 of 188 away matches, 28.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 11 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.094 (n=640 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.745: home 2.336, draw -1.922, away -3.410
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 640 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 640 |
| Average goals per match | 2.664 |
| Home win rate | 44.7% |
| Draw rate | 25.9% |
| Away win rate | 29.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Lincoln |
| Champion with most titles | Lincoln |
| BTTS rate | 53.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.46 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 11.77 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.33 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 40.83 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.95 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 104.24 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 557 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 24 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 83 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 24 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 9.6% vs overall 6.4% (deviation 3.2 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 34.9% vs overall 44.7%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 32.5% vs overall 25.9%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=24 positions=1..24 teams=24
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=24 positions=1..24 teams=24
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=24 positions=1..24 teams=24
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=24 positions=1..24 teams=24
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=24 positions=1..24 teams=24
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=24 positions=1..24 teams=24

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
