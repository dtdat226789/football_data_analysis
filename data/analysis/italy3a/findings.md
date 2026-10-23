# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:58:19+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie C - Group A (Italy)
- Scope: league `italy3a`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\italy3a\database_profile.json | yes | yes | 29.53 |
| matches_analysis | E:\football_data_analysis\data\analysis\italy3a\matches_analysis.json | yes | yes | 9.37 |
| goals_analysis | E:\football_data_analysis\data\analysis\italy3a\goals_analysis.json | yes | yes | 6.26 |
| teams_analysis | E:\football_data_analysis\data\analysis\italy3a\teams_analysis.json | yes | yes | 34.65 |
| season_trends | E:\football_data_analysis\data\analysis\italy3a\season_trends.json | yes | yes | 3.94 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\italy3a\scoreline_analysis.json | yes | yes | 69.13 |
| relationships | E:\football_data_analysis\data\analysis\italy3a\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 450 matches: home wins 36.7%, draws 31.8%, away wins 31.6% (165H / 143D / 142A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 8 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 101 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 450 matches produced 1044 goals (avg 2.320 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.1% vs away 46.9% of 1044 goals in total (home/away ratio 1.13)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 223 of 450 matches (49.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 113 scoring matches, 28.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.83, median 27.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — L.R. Vicenza leads with 89 points across 1 seasons (1 title(s), GD 43)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 15 teams present in every one of the 2 seasons (AlbinoLeffe, Alcione Milano, Arzignano, Brescia, Cittadella...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Triestina earns 20 more points at home than away (28 home vs 8 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — L.R. Vicenza won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Cittadella beat Brescia by 6 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.125 per match): first half 2.339 vs last half 2.214 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 8.100)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.900)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 60 matches (13.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (51 of 165 home matches, 30.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (60 of 143 draw matches, 42.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (49 of 142 away matches, 34.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_wins_last_5 |corr| = -0.1057 (n=380 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.687: home 3.083, draw 0.357, away -4.603
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (8)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 450 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 450 |
| Average goals per match | 2.32 |
| Home win rate | 36.7% |
| Draw rate | 31.8% |
| Away win rate | 31.6% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | L.R. Vicenza |
| Champion with most titles | L.R. Vicenza |
| BTTS rate | 49.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 29.53 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.37 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.26 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 34.65 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.94 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 69.13 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 70 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 18.6% vs overall 11.1% (deviation 7.5 pp)
- **4.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 30.0% vs overall 36.7%
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 40.0% vs overall 31.8%
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
