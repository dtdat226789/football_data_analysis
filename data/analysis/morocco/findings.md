# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:03:40+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Botola Pro (Morocco)
- Scope: league `morocco`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\morocco\database_profile.json | yes | yes | 30.70 |
| matches_analysis | E:\football_data_analysis\data\analysis\morocco\matches_analysis.json | yes | yes | 9.48 |
| goals_analysis | E:\football_data_analysis\data\analysis\morocco\goals_analysis.json | yes | yes | 6.18 |
| teams_analysis | E:\football_data_analysis\data\analysis\morocco\teams_analysis.json | yes | yes | 29.88 |
| season_trends | E:\football_data_analysis\data\analysis\morocco\season_trends.json | yes | yes | 3.97 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\morocco\scoreline_analysis.json | yes | yes | 74.76 |
| relationships | E:\football_data_analysis\data\analysis\morocco\relationships.json | yes | yes | 14.37 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 488 matches: home wins 40.6%, draws 31.4%, away wins 28.1% (198H / 153D / 137A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 7 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 105 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 488 matches produced 1094 goals (avg 2.242 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.3% vs away 46.7% of 1094 goals in total (home/away ratio 1.14)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 236 of 488 matches (48.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 106 scoring matches, 24.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 36.07, median 33.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Berkane leads with 127 points across 2 seasons (1 title(s), GD 52)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (Berkane, COD Meknes, Difaa El Jadidi, FAR Rabat, FUS Rabat...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — COD Meknes earns 32 more points at home than away (52 home vs 20 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Berkane won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Maghreb Fez beat Raja Casablanca by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.139 per match): first half 2.312 vs last half 2.173 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 6.706)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2024-2025 (luck view, avg abs position diff 2.625)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 81 matches (16.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (62 of 198 home matches, 31.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (81 of 153 draw matches, 52.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (38 of 137 away matches, 27.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.0975 (n=488 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 8.542: home 3.323, draw -0.150, away -5.219
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (12)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, MATCH_COUNT_UNEXPECTED, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 488 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 488 |
| Average goals per match | 2.242 |
| Home win rate | 40.6% |
| Draw rate | 31.4% |
| Away win rate | 28.1% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Berkane |
| Champion with most titles | Berkane |
| BTTS rate | 48.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 30.70 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.48 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.18 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 29.88 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.97 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 74.76 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.37 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 248 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 17 teams, expected 20
- **5.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **6.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=18, fgte=18 rows)
- **7.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=16 positions=1..16 teams=16
- **8.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=16 positions=1..16 teams=16
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=16 positions=1..16 teams=16
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=17 positions=1..17 teams=17
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=17 positions=1..17 teams=17
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=17 positions=1..17 teams=17

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
