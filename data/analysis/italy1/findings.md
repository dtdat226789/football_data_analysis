# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:56:47+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie A (Italy)
- Scope: league `italy1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\italy1\database_profile.json | yes | yes | 30.03 |
| matches_analysis | E:\football_data_analysis\data\analysis\italy1\matches_analysis.json | yes | yes | 8.49 |
| goals_analysis | E:\football_data_analysis\data\analysis\italy1\goals_analysis.json | yes | yes | 6.23 |
| teams_analysis | E:\football_data_analysis\data\analysis\italy1\teams_analysis.json | yes | yes | 32.23 |
| season_trends | E:\football_data_analysis\data\analysis\italy1\season_trends.json | yes | yes | 3.90 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\italy1\scoreline_analysis.json | yes | yes | 72.50 |
| relationships | E:\football_data_analysis\data\analysis\italy1\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 430 matches: home wins 39.5%, draws 25.1%, away wins 35.3% (170H / 108D / 152A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 7 home and 6 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 101 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 430 matches produced 1067 goals (avg 2.481 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.4% vs away 47.6% of 1067 goals in total (home/away ratio 1.10)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 201 of 430 matches (46.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 128 scoring matches, 32.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.47, median 26.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Inter leads with 100 points across 2 seasons (1 title(s), GD 61)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 17 teams present in every one of the 2 seasons (AC Milan, AS Roma, Atalanta, Bologna, Cagliari...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Sassuolo earns 14 more points at home than away (35 home vs 21 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Inter won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: AS Roma beat Inter by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.474 per match): first half 2.426 vs last half 2.9 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 6.500)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.800)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 45 matches (10.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (45 of 170 home matches, 26.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (43 of 108 draw matches, 39.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (42 of 152 away matches, 27.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 5 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_win_rate |corr| = 0.1177 (n=380 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 12.177: home 5.297, draw 0.505, away -6.880
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (9)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 430 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 430 |
| Average goals per match | 2.481 |
| Home win rate | 39.5% |
| Draw rate | 25.1% |
| Away win rate | 35.3% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Inter |
| Champion with most titles | Inter |
| BTTS rate | 46.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 30.03 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.49 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.23 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 32.23 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.90 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 72.50 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 50 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 2.9 vs overall 2.481 (deviation 0.419)
- **4.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 0.0% vs overall 8.4% (deviation 8.4 pp)
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 44.0% vs overall 39.5%
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 18.0% vs overall 25.1%
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=8, fgte=8 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
