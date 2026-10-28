# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T02:25:12+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Liga Portugal (Portugal)
- Scope: league `portugal1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/portugal1/database_profile.json | yes | yes | 31.31 |
| matches_analysis | data/analysis/portugal1/matches_analysis.json | yes | yes | 8.51 |
| goals_analysis | data/analysis/portugal1/goals_analysis.json | yes | yes | 5.95 |
| teams_analysis | data/analysis/portugal1/teams_analysis.json | yes | yes | 29.12 |
| season_trends | data/analysis/portugal1/season_trends.json | yes | yes | 3.74 |
| scoreline_analysis | data/analysis/portugal1/scoreline_analysis.json | yes | yes | 62.25 |
| relationships | data/analysis/portugal1/relationships.json | yes | yes | 13.69 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 388 matches: home wins 40.5%, draws 26.3%, away wins 33.2% (157H / 102D / 129A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 7 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 92 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 388 matches produced 1042 goals (avg 2.686 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.9% vs away 46.1% of 1042 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 186 of 388 matches (47.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 123 scoring matches, 33.9% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.42, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — FC Porto leads with 115 points across 2 seasons (2 title(s), GD 65)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 16 teams present in every one of the 2 seasons (Alverca, Arouca, Benfica, Braga, Casa Pia...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Vitoria Guimaraes earns 22 more points at home than away (36 home vs 14 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — FC Porto won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: FC Porto beat Sporting CP by 6 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.065 per match): first half 2.672 vs last half 2.737 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 5.889)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 3.368)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 0-1 in 38 matches (9.8%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (36 of 157 home matches, 22.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (36 of 102 draw matches, 35.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (38 of 129 away matches, 29.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1311 (n=308 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 16.064: home 7.559, draw -1.524, away -8.505
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 388 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 388 |
| Average goals per match | 2.686 |
| Home win rate | 40.5% |
| Draw rate | 26.3% |
| Away win rate | 33.2% |
| Most common scoreline | 0-1 |
| Dominant team (lifetime points) | FC Porto |
| Champion with most titles | FC Porto |
| BTTS rate | 47.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.31 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.51 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 5.95 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 29.12 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.74 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 62.25 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.69 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 308 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 19 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 80 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 40.0% vs overall 33.2%
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=397, fgte=397 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=19 positions=1..19 teams=19
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=19 positions=1..19 teams=19
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=19 positions=1..19 teams=19
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
