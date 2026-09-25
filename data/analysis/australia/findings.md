# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:54:41+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: A-League (Australia)
- Scope: league `australia`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\australia\database_profile.json | yes | yes | 31.46 |
| matches_analysis | E:\football_data_analysis\data\analysis\australia\matches_analysis.json | yes | yes | 10.08 |
| goals_analysis | E:\football_data_analysis\data\analysis\australia\goals_analysis.json | yes | yes | 6.33 |
| teams_analysis | E:\football_data_analysis\data\analysis\australia\teams_analysis.json | yes | yes | 22.58 |
| season_trends | E:\football_data_analysis\data\analysis\australia\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\australia\scoreline_analysis.json | yes | yes | 58.74 |
| relationships | E:\football_data_analysis\data\analysis\australia\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 332 matches: home wins 36.4%, draws 26.2%, away wins 37.3% (121H / 87D / 124A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 10 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 70 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 332 matches produced 1018 goals (avg 3.066 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 51.5% vs away 48.5% of 1018 goals in total (home/away ratio 1.06)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 202 of 332 matches (60.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 128 scoring matches, 40.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.58, median 20.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Auckland FC leads with 105 points across 2 seasons (2 title(s), GD 40)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (Adelaide United, Auckland FC, Brisbane Roar, Central Coast Mariners, Macarthur FC...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Melbourne Victory earns 11 more points at home than away (47 home vs 36 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Auckland FC won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025-2026: Auckland FC beat Newcastle Jets by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.456 per match): first half 3.29 vs last half 2.834 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 4.154)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2024-2025 (luck view, avg abs position diff 1.846)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 35 matches (10.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (25 of 121 home matches, 20.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (35 of 87 draw matches, 40.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (29 of 124 away matches, 23.4%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 14 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1893 (n=332 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 4.084: home 18.612, draw 19.931, away 15.847
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (12)** — Anomaly codes: DUPLICATE_ROWS, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 332 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 332 |
| Average goals per match | 3.066 |
| Home win rate | 36.4% |
| Draw rate | 26.2% |
| Away win rate | 37.3% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Auckland FC |
| Champion with most titles | Auckland FC |
| BTTS rate | 60.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.46 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 10.08 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.33 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 22.58 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 58.74 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 169 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2024-2025 has 13 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 163 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 12 teams, expected 20
- **5.** `HIGH_SCORING_MATCHES` *(warning)* — 7 match(es) with >= 8 total goals (extreme scorelines)
- **6.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **7.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/classic rows=13 positions=1..13 teams=13
- **8.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/goals rows=13 positions=1..13 teams=13
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024-2025/luck rows=13 positions=1..13 teams=13
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=12 positions=1..12 teams=12
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=12 positions=1..12 teams=12
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
