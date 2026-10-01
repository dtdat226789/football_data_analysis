# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:49:24+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Meistriliiga (Estonia)
- Scope: league `estonia`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\estonia\database_profile.json | yes | yes | 31.76 |
| matches_analysis | E:\football_data_analysis\data\analysis\estonia\matches_analysis.json | yes | yes | 9.89 |
| goals_analysis | E:\football_data_analysis\data\analysis\estonia\goals_analysis.json | yes | yes | 6.27 |
| teams_analysis | E:\football_data_analysis\data\analysis\estonia\teams_analysis.json | yes | yes | 19.83 |
| season_trends | E:\football_data_analysis\data\analysis\estonia\season_trends.json | yes | yes | 3.85 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\estonia\scoreline_analysis.json | yes | yes | 64.55 |
| relationships | E:\football_data_analysis\data\analysis\estonia\relationships.json | yes | yes | 14.32 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 325 matches: home wins 46.5%, draws 12.9%, away wins 40.6% (151H / 42D / 132A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 12 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 95 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 325 matches produced 1028 goals (avg 3.163 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.6% vs away 44.4% of 1028 goals in total (home/away ratio 1.25)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 184 of 325 matches (56.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 111 scoring matches, 35.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 27.47, median 22.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Levadia leads with 151 points across 2 seasons (1 title(s), GD 113)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 9 teams present in every one of the 2 seasons (Flora, Harju JK Laagri, Kalju, Kuressaare, Levadia...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Narva earns 14 more points at home than away (42 home vs 28 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Flora won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025: Flora beat Levadia by 3 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (-0.033 per match): first half 3.178 vs last half 3.145 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025 (goals view, avg abs position diff 3.600)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 1.400)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-2 in 43 matches (13.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (29 of 151 home matches, 19.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (18 of 42 draw matches, 42.9%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (43 of 132 away matches, 32.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 12 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_position_before_match |corr| = 0.1692 (n=180 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 18.675: home 8.869, draw -3.917, away -9.806
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 325 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 325 |
| Average goals per match | 3.163 |
| Home win rate | 46.5% |
| Draw rate | 12.9% |
| Away win rate | 40.6% |
| Most common scoreline | 1-2 |
| Dominant team (lifetime points) | Levadia |
| Champion with most titles | Flora |
| BTTS rate | 56.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.76 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.89 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.27 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 19.83 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.85 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 64.55 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.32 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 180 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 10 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 145 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 10 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=10 positions=1..10 teams=10
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=10 positions=1..10 teams=10
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=10 positions=1..10 teams=10
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=10 positions=1..10 teams=10
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=10 positions=1..10 teams=10
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=10 positions=1..10 teams=10

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
