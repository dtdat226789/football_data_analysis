# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:54:02+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: NB II. (Hungary)
- Scope: league `hungary2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/hungary2/database_profile.json | yes | yes | 45.33 |
| matches_analysis | data/analysis/hungary2/matches_analysis.json | yes | yes | 24.10 |
| goals_analysis | data/analysis/hungary2/goals_analysis.json | yes | yes | 12.41 |
| teams_analysis | data/analysis/hungary2/teams_analysis.json | yes | yes | 45.86 |
| season_trends | data/analysis/hungary2/season_trends.json | yes | yes | 10.43 |
| scoreline_analysis | data/analysis/hungary2/scoreline_analysis.json | yes | yes | 304.81 |
| relationships | data/analysis/hungary2/relationships.json | yes | yes | 13.77 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2013 matches: home wins 43.4%, draws 26.1%, away wins 30.5% (873H / 526D / 614A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 49 home and 40 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 520 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2013 matches produced 5205 goals (avg 2.586 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.9% vs away 45.1% of 5205 goals in total (home/away ratio 1.22)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1031 of 2013 matches (51.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 588 scoring matches, 31.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.02, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Vasas leads with 346 points across 5 seasons (2 title(s), GD 172)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 4 teams present in every one of the 7 seasons (Ajka, Csakvari, Soroksar, Szeged)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Soroksar earns 77 more points at home than away (192 home vs 115 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Vasas won 2 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Soroksar beat Tiszakecske by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.163 per match): first half 2.576 vs last half 2.739 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (luck view, avg abs position diff 18.250)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.750)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 262 matches (13.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (225 of 873 home matches, 25.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (262 of 526 draw matches, 49.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (198 of 614 away matches, 32.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 45 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_conceded_last_5 |corr| = 0.0527 (n=1926 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.679: home 2.258, draw -0.721, away -3.421
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (28)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2013 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2013 |
| Average goals per match | 2.586 |
| Home win rate | 43.4% |
| Draw rate | 26.1% |
| Away win rate | 30.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Vasas |
| Champion with most titles | Vasas |
| BTTS rate | 51.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 45.33 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 24.10 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.41 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 45.86 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.43 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 304.81 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.77 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023-2024 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 240 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 16 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 240 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 87 matches, expected 380
- **8.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **9.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **10.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 8.9% vs overall 7.3% (deviation 1.6 pp)
- **11.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 2.989 vs overall 2.586 (deviation 0.403)
- **12.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 2.3% vs overall 7.3% (deviation 5.0 pp)
- **13.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 48.3% vs overall 43.4%
- **14.** `HIGH_SCORING_MATCHES` *(warning)* — 12 match(es) with >= 8 total goals (extreme scorelines)
- **15.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **16.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=344, fgte=344 rows)
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/classic rows=18 positions=1..19 teams=18
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/goals rows=18 positions=1..26 teams=18
- **19.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023-2024/luck rows=18 positions=1..36 teams=18
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=16 positions=1..17 teams=16
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=16 positions=7..28 teams=16
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=16 positions=1..46 teams=16
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=16 positions=1..16 teams=16
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=16 positions=1..16 teams=16
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=16 positions=1..16 teams=16
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
