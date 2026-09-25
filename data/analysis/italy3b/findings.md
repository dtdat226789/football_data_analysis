# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:02:25+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie C - Group B (Italy)
- Scope: league `italy3b`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\italy3b\database_profile.json | yes | yes | 29.44 |
| matches_analysis | E:\football_data_analysis\data\analysis\italy3b\matches_analysis.json | yes | yes | 9.47 |
| goals_analysis | E:\football_data_analysis\data\analysis\italy3b\goals_analysis.json | yes | yes | 6.33 |
| teams_analysis | E:\football_data_analysis\data\analysis\italy3b\teams_analysis.json | yes | yes | 36.99 |
| season_trends | E:\football_data_analysis\data\analysis\italy3b\season_trends.json | yes | yes | 3.92 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\italy3b\scoreline_analysis.json | yes | yes | 64.52 |
| relationships | E:\football_data_analysis\data\analysis\italy3b\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 417 matches: home wins 39.1%, draws 31.4%, away wins 29.5% (163H / 131D / 123A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 9 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 88 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 417 matches produced 956 goals (avg 2.293 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.9% vs away 47.1% of 956 goals in total (home/away ratio 1.12)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 207 of 417 matches (49.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 94 scoring matches, 24.9% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.51, median 31.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Ravenna leads with 87 points across 2 seasons (0 title(s), GD 28)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (Campobasso, Forli, Gubbio, Guidonia, Livorno...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Livorno earns 20 more points at home than away (37 home vs 17 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Arezzo won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Spezia beat Ravenna by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.321 per match): first half 2.246 vs last half 2.567 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.600)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.300)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 64 matches (15.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (51 of 163 home matches, 31.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (64 of 131 draw matches, 48.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (41 of 123 away matches, 33.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 1 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.0695 (n=417 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.941: home 3.258, draw -0.267, away -4.683
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (8)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 417 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 417 |
| Average goals per match | 2.293 |
| Home win rate | 39.1% |
| Draw rate | 31.4% |
| Away win rate | 29.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Ravenna |
| Champion with most titles | Arezzo |
| BTTS rate | 49.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 29.44 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.47 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.33 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 36.99 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.92 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 64.52 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 357 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 60 matches, expected 380
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **4.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 48.3% vs overall 39.1%
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 21.7% vs overall 29.5%
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
