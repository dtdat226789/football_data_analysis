# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-30T03:59:21+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie C - Group A (Italy)
- Scope: league `italy3a`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/italy3a/database_profile.json | yes | yes | 38.59 |
| matches_analysis | data/analysis/italy3a/matches_analysis.json | yes | yes | 24.07 |
| goals_analysis | data/analysis/italy3a/goals_analysis.json | yes | yes | 12.37 |
| teams_analysis | data/analysis/italy3a/teams_analysis.json | yes | yes | 58.82 |
| season_trends | data/analysis/italy3a/season_trends.json | yes | yes | 10.46 |
| scoreline_analysis | data/analysis/italy3a/scoreline_analysis.json | yes | yes | 336.49 |
| relationships | data/analysis/italy3a/relationships.json | yes | yes | 13.80 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2390 matches: home wins 39.1%, draws 29.7%, away wins 31.2% (935H / 710D / 745A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 50 home and 38 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 554 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2390 matches produced 5459 goals (avg 2.284 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.9% vs away 46.1% of 5459 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1149 of 2390 matches (48.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 641 scoring matches, 29.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.34, median 28.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Renate leads with 354 points across 7 seasons (0 title(s), GD 18)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 4 teams present in every one of the 7 seasons (AlbinoLeffe, Pergolettese, Pro Vercelli, Renate)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Lecco earns 80 more points at home than away (189 home vs 109 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Como won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2023-2024: Mantova beat Padova by 3 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.089 per match): first half 2.266 vs last half 2.354 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 8.100)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2021-2022 (luck view, avg abs position diff 1.600)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 342 matches (14.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (291 of 935 home matches, 31.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (342 of 710 draw matches, 48.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (242 of 745 away matches, 32.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 14 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_points_last_5 |corr| = -0.0389 (n=2280 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.919: home 2.507, draw -0.189, away -3.412
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (9)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2390 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2390 |
| Average goals per match | 2.284 |
| Home win rate | 39.1% |
| Draw rate | 29.7% |
| Away win rate | 31.2% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Renate |
| Champion with most titles | Como |
| BTTS rate | 48.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 38.59 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 24.07 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.37 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 58.82 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.46 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 336.49 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.80 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 110 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 8.4% vs overall 10.1% (deviation 1.7 pp)
- **4.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024-2025 home outcome share 43.7% vs overall 39.1%
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 14.5% vs overall 10.1% (deviation 4.4 pp)
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 35.5% vs overall 29.7%
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 3 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=362, fgte=362 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
