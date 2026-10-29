# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T02:10:50+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier League (England)
- Scope: league `premier`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/premier/database_profile.json | yes | yes | 41.64 |
| matches_analysis | data/analysis/premier/matches_analysis.json | yes | yes | 32.43 |
| goals_analysis | data/analysis/premier/goals_analysis.json | yes | yes | 12.37 |
| teams_analysis | data/analysis/premier/teams_analysis.json | yes | yes | 40.18 |
| season_trends | data/analysis/premier/season_trends.json | yes | yes | 10.51 |
| scoreline_analysis | data/analysis/premier/scoreline_analysis.json | yes | yes | 369.36 |
| relationships | data/analysis/premier/relationships.json | yes | yes | 13.80 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2360 matches: home wins 43.0%, draws 23.7%, away wins 33.3% (1014H / 560D / 786A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 70 home and 65 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 630 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2360 matches produced 6807 goals (avg 2.884 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.9% vs away 46.1% of 6807 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1277 of 2360 matches (54.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 763 scoring matches, 34.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.99, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Manchester City leads with 529 points across 7 seasons (5 title(s), GD 328)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 11 teams present in every one of the 7 seasons (Arsenal, Aston Villa, Brighton, Chelsea, Crystal Palace...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Newcastle earns 63 more points at home than away (207 home vs 144 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Manchester City won 5 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Manchester City beat Arsenal by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.031 per match): first half 2.789 vs last half 2.82 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 7.100)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.900)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 259 matches (11.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (194 of 1014 home matches, 19.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (259 of 560 draw matches, 46.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (176 of 786 away matches, 22.4%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 67 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.076 (n=2280 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 11.426: home 5.189, draw -1.125, away -6.237
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2360 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2360 |
| Average goals per match | 2.884 |
| Home win rate | 43.0% |
| Draw rate | 23.7% |
| Away win rate | 33.3% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Manchester City |
| Champion with most titles | Manchester City |
| BTTS rate | 54.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 41.64 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 32.43 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.37 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 40.18 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.51 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 369.36 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.80 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 80 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 7.9% vs overall 5.7% (deviation 2.2 pp)
- **4.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 37.9% vs overall 43.0%
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 40.3% vs overall 33.3%
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 home outcome share 48.4% vs overall 43.0%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 away outcome share 28.7% vs overall 33.3%
- **8.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2023-2024 avg goals 3.279 vs overall 2.884 (deviation 0.395)
- **9.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 2.9% vs overall 5.7% (deviation 2.8 pp)
- **10.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 7.5% vs overall 5.7% (deviation 1.8 pp)
- **11.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 38.8% vs overall 43.0%
- **12.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 28.8% vs overall 23.7%
- **13.** `HIGH_SCORING_MATCHES` *(warning)* — 18 match(es) with >= 8 total goals (extreme scorelines)
- **14.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **15.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=397, fgte=397 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
