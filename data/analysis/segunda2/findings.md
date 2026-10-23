# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:07:12+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Segunda RFEF - Group 2 (Spain)
- Scope: league `segunda2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\segunda2\database_profile.json | yes | yes | 32.11 |
| matches_analysis | E:\football_data_analysis\data\analysis\segunda2\matches_analysis.json | yes | yes | 9.12 |
| goals_analysis | E:\football_data_analysis\data\analysis\segunda2\goals_analysis.json | yes | yes | 6.41 |
| teams_analysis | E:\football_data_analysis\data\analysis\segunda2\teams_analysis.json | yes | yes | 39.71 |
| season_trends | E:\football_data_analysis\data\analysis\segunda2\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\segunda2\scoreline_analysis.json | yes | yes | 56.66 |
| relationships | E:\football_data_analysis\data\analysis\segunda2\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 342 matches: home wins 42.7%, draws 28.4%, away wins 28.9% (146H / 97D / 99A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 12 home and 4 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 89 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 342 matches produced 864 goals (avg 2.526 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.5% vs away 42.5% of 864 goals in total (home/away ratio 1.35)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 173 of 342 matches (50.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 98 scoring matches, 31.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.67, median 27.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — R. Union leads with 69 points across 1 seasons (1 title(s), GD 29)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 5 teams present in every one of the 2 seasons (Ebro, Naxara, SD Logrones, Tudelano, Utebo FC)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — UD Logrones earns 15 more points at home than away (38 home vs 23 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — R. Union won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Barcelona B beat Espanyol B by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.126 per match): first half 2.513 vs last half 2.639 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 5.556)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 2.778)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 49 matches (14.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (33 of 146 home matches, 22.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (49 of 97 draw matches, 50.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (33 of 99 away matches, 33.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.1116 (n=306 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.643: home 1.908, draw -0.348, away -3.736
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 342 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 342 |
| Average goals per match | 2.526 |
| Home win rate | 42.7% |
| Draw rate | 28.4% |
| Away win rate | 28.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | R. Union |
| Champion with most titles | R. Union |
| BTTS rate | 50.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.11 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.12 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.41 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.71 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 56.66 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 36 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 11.1% vs overall 9.4% (deviation 1.7 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 22.2% vs overall 28.4%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 33.3% vs overall 28.9%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=27, fgte=27 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
