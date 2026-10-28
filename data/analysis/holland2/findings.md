# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:52:18+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Eerste Divisie (Netherlands)
- Scope: league `holland2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/holland2/database_profile.json | yes | yes | 41.90 |
| matches_analysis | data/analysis/holland2/matches_analysis.json | yes | yes | 33.25 |
| goals_analysis | data/analysis/holland2/goals_analysis.json | yes | yes | 12.69 |
| teams_analysis | data/analysis/holland2/teams_analysis.json | yes | yes | 39.07 |
| season_trends | data/analysis/holland2/season_trends.json | yes | yes | 10.46 |
| scoreline_analysis | data/analysis/holland2/scoreline_analysis.json | yes | yes | 390.53 |
| relationships | data/analysis/holland2/relationships.json | yes | yes | 13.80 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2412 matches: home wins 44.7%, draws 22.0%, away wins 33.3% (1079H / 530D / 803A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 76 home and 65 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 668 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2412 matches produced 7543 goals (avg 3.127 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.2% vs away 44.8% of 7543 goals in total (home/away ratio 1.23)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1406 of 2412 matches (58.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 856 scoring matches, 37.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.26, median 22.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — De Graafschap leads with 389 points across 7 seasons (0 title(s), GD 74)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 7 seasons (De Graafschap, Den Bosch, Dordrecht, Eindhoven FC, Helmond...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Helmond earns 74 more points at home than away (169 home vs 95 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Heracles won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2022-2023: Heracles beat Zwolle by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.142 per match): first half 3.122 vs last half 3.264 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2020-2021 (goals view, avg abs position diff 7.100)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.400)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 232 matches (9.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (196 of 1079 home matches, 18.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (232 of 530 draw matches, 43.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (180 of 803 away matches, 22.4%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 96 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.0622 (n=2292 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.667: home 3.467, draw -1.352, away -4.201
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2412 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2412 |
| Average goals per match | 3.127 |
| Home win rate | 44.7% |
| Draw rate | 22.0% |
| Away win rate | 33.3% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | De Graafschap |
| Champion with most titles | Heracles |
| BTTS rate | 58.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 41.90 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 33.25 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.69 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.07 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.46 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 390.53 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.80 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 392 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 21 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 120 matches, expected 380
- **4.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **5.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.592 vs overall 3.127 (deviation 0.465)
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 1.7% vs overall 4.6% (deviation 2.9 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 50.8% vs overall 44.7%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 29.2% vs overall 33.3%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 39 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=338, fgte=338 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=21 positions=1..21 teams=21
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=21 positions=1..21 teams=21
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=21 positions=1..21 teams=21

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
