# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T11:03:21+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Virsliga (Latvia)
- Scope: league `latvia`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\latvia\database_profile.json | yes | yes | 31.86 |
| matches_analysis | E:\football_data_analysis\data\analysis\latvia\matches_analysis.json | yes | yes | 8.66 |
| goals_analysis | E:\football_data_analysis\data\analysis\latvia\goals_analysis.json | yes | yes | 6.18 |
| teams_analysis | E:\football_data_analysis\data\analysis\latvia\teams_analysis.json | yes | yes | 20.88 |
| season_trends | E:\football_data_analysis\data\analysis\latvia\season_trends.json | yes | yes | 3.83 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\latvia\scoreline_analysis.json | yes | yes | 59.06 |
| relationships | E:\football_data_analysis\data\analysis\latvia\relationships.json | yes | yes | 14.32 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 336 matches: home wins 43.8%, draws 23.8%, away wins 32.4% (147H / 80D / 109A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 9 home and 5 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 97 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 336 matches produced 973 goals (avg 2.896 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.3% vs away 43.7% of 973 goals in total (home/away ratio 1.29)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 182 of 336 matches (54.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 104 scoring matches, 32.8% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.70, median 26.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Riga FC leads with 161 points across 2 seasons (1 title(s), GD 115)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 2 seasons (Auda, BFC Daugavpils, FK Liepaja, Grobina, Jelgava...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — BFC Daugavpils earns 29 more points at home than away (58 home vs 29 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Riga FC won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025: Riga FC beat RFS by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.096 per match): first half 2.94 vs last half 2.844 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026 (goals view, avg abs position diff 3.200)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026 (luck view, avg abs position diff 1.800)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 40 matches (11.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (28 of 147 home matches, 19.0%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (40 of 80 draw matches, 50.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (36 of 109 away matches, 33.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 11 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_home_win_rate |corr| = 0.148 (n=336 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 18.106: home 7.565, draw -0.225, away -10.541
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 336 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 336 |
| Average goals per match | 2.896 |
| Home win rate | 43.8% |
| Draw rate | 23.8% |
| Away win rate | 32.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Riga FC |
| Champion with most titles | Riga FC |
| BTTS rate | 54.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.86 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.66 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.18 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 20.88 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.83 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 59.06 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.32 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 182 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 11 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 154 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=11 positions=1..11 teams=11
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=11 positions=1..11 teams=11
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=11 positions=1..11 teams=11
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
