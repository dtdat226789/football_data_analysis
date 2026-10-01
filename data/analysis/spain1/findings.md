# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:08:57+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: LaLiga (Spain)
- Scope: league `spain1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\spain1\database_profile.json | yes | yes | 29.18 |
| matches_analysis | E:\football_data_analysis\data\analysis\spain1\matches_analysis.json | yes | yes | 10.58 |
| goals_analysis | E:\football_data_analysis\data\analysis\spain1\goals_analysis.json | yes | yes | 6.31 |
| teams_analysis | E:\football_data_analysis\data\analysis\spain1\teams_analysis.json | yes | yes | 32.72 |
| season_trends | E:\football_data_analysis\data\analysis\spain1\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\spain1\scoreline_analysis.json | yes | yes | 76.69 |
| relationships | E:\football_data_analysis\data\analysis\spain1\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 449 matches: home wins 48.3%, draws 24.5%, away wins 27.2% (217H / 110D / 122A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 9 home and 15 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 122 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 449 matches produced 1234 goals (avg 2.748 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 58.0% vs away 42.0% of 1234 goals in total (home/away ratio 1.38)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 255 of 449 matches (56.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 123 scoring matches, 28.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.82, median 30.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Barcelona leads with 115 points across 2 seasons (2 title(s), GD 83)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 17 teams present in every one of the 2 seasons (Alaves, Ath Bilbao, Atl. Madrid, Barcelona, Betis...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Atl. Madrid earns 27 more points at home than away (56 home vs 29 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Barcelona won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Barcelona beat Atl. Madrid by 5 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.348 per match): first half 2.695 vs last half 3.043 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 6.200)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 3.400)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 68 matches (15.1%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (52 of 217 home matches, 24.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (68 of 110 draw matches, 61.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (30 of 122 away matches, 24.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 9 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.2264 (n=380 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 8.022: home 3.339, draw -3.022, away -4.683
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (6)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 449 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 449 |
| Average goals per match | 2.748 |
| Home win rate | 48.3% |
| Draw rate | 24.5% |
| Away win rate | 27.2% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Barcelona |
| Champion with most titles | Barcelona |
| BTTS rate | 56.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 29.18 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 10.58 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.31 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 32.72 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 76.69 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 69 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 7.2% vs overall 4.5% (deviation 2.7 pp)
- **4.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **5.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **6.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=29, fgte=29 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
