# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-26T01:30:29+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/develop21/database_profile.json | yes | yes | 27.72 |
| matches_analysis | data/analysis/develop21/matches_analysis.json | yes | yes | 5.92 |
| goals_analysis | data/analysis/develop21/goals_analysis.json | yes | yes | 4.84 |
| teams_analysis | data/analysis/develop21/teams_analysis.json | yes | yes | 25.28 |
| season_trends | data/analysis/develop21/season_trends.json | yes | yes | 2.43 |
| scoreline_analysis | data/analysis/develop21/scoreline_analysis.json | yes | yes | 16.24 |
| relationships | data/analysis/develop21/relationships.json | yes | yes | 11.61 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 61 matches: home wins 42.6%, draws 23.0%, away wins 34.4% (26H / 14D / 21A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 2 home and 1 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 19 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 61 matches produced 237 goals (avg 3.885 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.6% vs away 46.4% of 237 goals in total (home/away ratio 1.16)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 42 of 61 matches (68.9%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 16-30 (first goal in 21 scoring matches, 35.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 24.40, median 21.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Bolton U21 leads with 21 points across 1 seasons (1 title(s), GD 16)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 17 teams present in every one of the 1 seasons (Barnsley U21, Bolton U21, Bristol City U21, Cardiff U21, Charlton U21...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Bristol City U21 earns 8 more points at home than away (10 home vs 2 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Bolton U21 won 1 of 1 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Bolton U21 beat Fleetwood U21 by 5 pts
- **F14** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 6.118)
- **F15** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.882)
- **F16** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-2 in 8 matches (13.1%)
- **F17** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 3-1 (7 of 26 home matches, 26.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 2-2 (8 of 14 draw matches, 57.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-2 (4 of 21 away matches, 19.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 7 match(es) with >= 7 total goals
- **F21** · `database_profile` · *[high]* — **Data-quality warnings (9)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F22** · `database_profile` · *[medium]* — **Data coverage** — 1 of 1 registered seasons populated (100.0%); 61 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 61 |
| Average goals per match | 3.885 |
| Home win rate | 42.6% |
| Draw rate | 23.0% |
| Away win rate | 34.4% |
| Most common scoreline | 2-2 |
| Dominant team (lifetime points) | Bolton U21 |
| Champion with most titles | Bolton U21 |
| BTTS rate | 68.9% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 27.72 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 5.92 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 4.84 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 25.28 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 2.43 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 16.24 |
| relationships | relationships | n_matches, feature_count, data_warning, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 11.61 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 61 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 17 teams, expected 20
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **4.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **5.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **6.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=310, fgte=310 rows)
- **7.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=17 positions=1..17 teams=17
- **8.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=17 positions=1..17 teams=17
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=17 positions=1..17 teams=17

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
