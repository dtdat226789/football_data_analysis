# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:59:50+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: J2 League (Japan)
- Scope: league `japan2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\japan2\database_profile.json | yes | yes | 28.12 |
| matches_analysis | E:\football_data_analysis\data\analysis\japan2\matches_analysis.json | yes | yes | 14.22 |
| goals_analysis | E:\football_data_analysis\data\analysis\japan2\goals_analysis.json | yes | yes | 6.21 |
| teams_analysis | E:\football_data_analysis\data\analysis\japan2\teams_analysis.json | yes | yes | 35.74 |
| season_trends | E:\football_data_analysis\data\analysis\japan2\season_trends.json | yes | yes | 3.88 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\japan2\scoreline_analysis.json | yes | yes | 119.34 |
| relationships | E:\football_data_analysis\data\analysis\japan2\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 760 matches: home wins 39.2%, draws 25.9%, away wins 34.9% (298H / 197D / 265A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 15 home and 29 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 169 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 760 matches produced 1880 goals (avg 2.474 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.6% vs away 46.4% of 1880 goals in total (home/away ratio 1.15)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 378 of 760 matches (49.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 206 scoring matches, 30.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 32.32, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — V-Varen Nagasaki leads with 145 points across 2 seasons (0 title(s), GD 54)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 14 teams present in every one of the 2 seasons (Blaublitz, Chiba, Ehime, Fujieda MYFC, Iwaki...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Kagoshima Utd earns 18 more points at home than away (24 home vs 6 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Shimizu S-Pulse won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025: Mito beat V-Varen Nagasaki by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (-0.031 per match): first half 2.489 vs last half 2.458 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024 (goals view, avg abs position diff 6.400)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 1.400)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 89 matches (11.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (89 of 298 home matches, 29.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (79 of 197 draw matches, 40.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (77 of 265 away matches, 29.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 11 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_wins_last_5 |corr| = 0.0992 (n=760 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.104: home 3.587, draw -0.604, away -3.517
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (3)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 760 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 760 |
| Average goals per match | 2.474 |
| Home win rate | 39.2% |
| Draw rate | 25.9% |
| Away win rate | 34.9% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | V-Varen Nagasaki |
| Champion with most titles | Shimizu S-Pulse |
| BTTS rate | 49.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 28.12 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 14.22 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.21 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 35.74 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.88 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 119.34 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **2.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **3.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
