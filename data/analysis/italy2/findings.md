# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:05:29+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie B (Italy)
- Scope: league `italy2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/italy2/database_profile.json | yes | yes | 39.84 |
| matches_analysis | data/analysis/italy2/matches_analysis.json | yes | yes | 26.25 |
| goals_analysis | data/analysis/italy2/goals_analysis.json | yes | yes | 12.26 |
| teams_analysis | data/analysis/italy2/teams_analysis.json | yes | yes | 56.93 |
| season_trends | data/analysis/italy2/season_trends.json | yes | yes | 10.41 |
| scoreline_analysis | data/analysis/italy2/scoreline_analysis.json | yes | yes | 326.42 |
| relationships | data/analysis/italy2/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2377 matches: home wins 39.9%, draws 32.2%, away wins 27.9% (948H / 765D / 664A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 56 home and 47 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 551 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2377 matches produced 5866 goals (avg 2.468 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.0% vs away 45.0% of 5866 goals in total (home/away ratio 1.22)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1254 of 2377 matches (52.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 652 scoring matches, 30.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.48, median 26.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Frosinone leads with 312 points across 5 seasons (1 title(s), GD 75)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 0 teams present in every one of the 7 seasons
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Palermo earns 46 more points at home than away (150 home vs 104 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Empoli won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Monza beat Venezia by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.151 per match): first half 2.409 vs last half 2.56 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021-2022 (goals view, avg abs position diff 8.400)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2023-2024 (luck view, avg abs position diff 2.100)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 370 matches (15.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (251 of 948 home matches, 26.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (370 of 765 draw matches, 48.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (188 of 664 away matches, 28.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 31 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_rest_days |corr| = 0.0695 (n=2231 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.019: home 2.711, draw -1.074, away -3.308
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (12)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2377 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2377 |
| Average goals per match | 2.468 |
| Home win rate | 39.9% |
| Draw rate | 32.2% |
| Away win rate | 27.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Frosinone |
| Champion with most titles | Empoli |
| BTTS rate | 52.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 39.84 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 26.25 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.26 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 56.93 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.41 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 326.42 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 390 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 87 matches, expected 380
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **4.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021-2022 goalless share 7.1% vs overall 9.1% (deviation 2.0 pp)
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022-2023 goalless share 11.1% vs overall 9.1% (deviation 2.0 pp)
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2025-2026 home outcome share 44.9% vs overall 39.9%
- **7.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.4% vs overall 9.1% (deviation 5.7 pp)
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 27.6% vs overall 32.2%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 35.6% vs overall 27.9%
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 9 match(es) with >= 8 total goals (extreme scorelines)
- **11.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **12.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=362, fgte=362 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
