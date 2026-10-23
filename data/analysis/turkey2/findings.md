# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:10:53+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 1. Lig (Turkey)
- Scope: league `turkey2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\turkey2\database_profile.json | yes | yes | 29.95 |
| matches_analysis | E:\football_data_analysis\data\analysis\turkey2\matches_analysis.json | yes | yes | 10.11 |
| goals_analysis | E:\football_data_analysis\data\analysis\turkey2\goals_analysis.json | yes | yes | 6.32 |
| teams_analysis | E:\football_data_analysis\data\analysis\turkey2\teams_analysis.json | yes | yes | 36.69 |
| season_trends | E:\football_data_analysis\data\analysis\turkey2\season_trends.json | yes | yes | 3.93 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\turkey2\scoreline_analysis.json | yes | yes | 79.01 |
| relationships | E:\football_data_analysis\data\analysis\turkey2\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 465 matches: home wins 43.7%, draws 26.5%, away wins 29.9% (203H / 123D / 139A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 11 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 119 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 465 matches produced 1332 goals (avg 2.865 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.1% vs away 42.9% of 1332 goals in total (home/away ratio 1.33)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 235 of 465 matches (50.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 140 scoring matches, 32.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.48, median 26.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Erzurumspor leads with 81 points across 1 seasons (1 title(s), GD 55)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (Bandirmaspor, Bodrumspor, Boluspor, Erokspor, Igdir FK...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Amedspor earns 20 more points at home than away (47 home vs 27 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Erzurumspor won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Kayserispor beat Bursaspor by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.335 per match): first half 2.922 vs last half 2.587 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 7.300)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.700)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 66 matches (14.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-0 (38 of 203 home matches, 18.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (66 of 123 draw matches, 53.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (31 of 139 away matches, 22.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 18 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_conceded_avg |corr| = 0.2292 (n=385 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 14.09: home 5.577, draw -0.558, away -8.513
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (8)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 465 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 465 |
| Average goals per match | 2.865 |
| Home win rate | 43.7% |
| Draw rate | 26.5% |
| Away win rate | 29.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Erzurumspor |
| Champion with most titles | Erzurumspor |
| BTTS rate | 50.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 29.95 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 10.11 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.32 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 36.69 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.93 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 79.01 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 385 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 80 matches, expected 380
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **4.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 35.0% vs overall 43.7%
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 35.0% vs overall 26.5%
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=31, fgte=31 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
