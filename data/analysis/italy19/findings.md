# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:57:19+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Primavera 1 (Italy)
- Scope: league `italy19`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\italy19\database_profile.json | yes | yes | 31.13 |
| matches_analysis | E:\football_data_analysis\data\analysis\italy19\matches_analysis.json | yes | yes | 9.75 |
| goals_analysis | E:\football_data_analysis\data\analysis\italy19\goals_analysis.json | yes | yes | 6.31 |
| teams_analysis | E:\football_data_analysis\data\analysis\italy19\teams_analysis.json | yes | yes | 32.87 |
| season_trends | E:\football_data_analysis\data\analysis\italy19\season_trends.json | yes | yes | 3.94 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\italy19\scoreline_analysis.json | yes | yes | 69.60 |
| relationships | E:\football_data_analysis\data\analysis\italy19\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 432 matches: home wins 38.4%, draws 30.8%, away wins 30.8% (166H / 133D / 133A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 7 home and 12 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 90 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 432 matches produced 1212 goals (avg 2.806 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.9% vs away 46.1% of 1212 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 257 of 432 matches (59.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 158 scoring matches, 40.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.06, median 21.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Parma U20 leads with 79 points across 2 seasons (0 title(s), GD 27)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 17 teams present in every one of the 2 seasons (AC Milan U20, AS Roma U20, Atalanta U20, Bologna U20, Cagliari U20...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Fiorentina U20 earns 15 more points at home than away (43 home vs 28 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Cesena U20 won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Cesena U20 beat Fiorentina U20 by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.469 per match): first half 2.751 vs last half 3.22 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 6.600)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.200)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 58 matches (13.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (37 of 166 home matches, 22.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (58 of 133 draw matches, 43.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (37 of 133 away matches, 27.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 14 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.1205 (n=382 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 3.852: home 1.276, draw -0.120, away -2.575
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (10)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 432 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 432 |
| Average goals per match | 2.806 |
| Home win rate | 38.4% |
| Draw rate | 30.8% |
| Away win rate | 30.8% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Parma U20 |
| Champion with most titles | Cesena U20 |
| BTTS rate | 59.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.13 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.75 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.31 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 32.87 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.94 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 69.60 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 382 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 50 matches, expected 380
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **4.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 3.22 vs overall 2.806 (deviation 0.414)
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.0% vs overall 7.2% (deviation 3.2 pp)
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 28.0% vs overall 38.4%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 40.0% vs overall 30.8%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 7 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
