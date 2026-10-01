# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:51:17+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: 2. Bundesliga (Germany)
- Scope: league `germany2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\germany2\database_profile.json | yes | yes | 30.89 |
| matches_analysis | E:\football_data_analysis\data\analysis\germany2\matches_analysis.json | yes | yes | 9.24 |
| goals_analysis | E:\football_data_analysis\data\analysis\germany2\goals_analysis.json | yes | yes | 6.32 |
| teams_analysis | E:\football_data_analysis\data\analysis\germany2\teams_analysis.json | yes | yes | 33.66 |
| season_trends | E:\football_data_analysis\data\analysis\germany2\season_trends.json | yes | yes | 3.94 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\germany2\scoreline_analysis.json | yes | yes | 64.77 |
| relationships | E:\football_data_analysis\data\analysis\germany2\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 364 matches: home wins 45.3%, draws 24.7%, away wins 29.9% (165H / 90D / 109A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 12 home and 4 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 89 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 364 matches produced 1082 goals (avg 2.973 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.3% vs away 44.7% of 1082 goals in total (home/away ratio 1.24)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 217 of 364 matches (59.6%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 121 scoring matches, 35.1% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.92, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Schalke leads with 70 points across 1 seasons (1 title(s), GD 19)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 14 teams present in every one of the 2 seasons (Arminia Bielefeld, Bochum, Braunschweig, Darmstadt, Greuther Furth...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Darmstadt earns 22 more points at home than away (39 home vs 17 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Schalke won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Hertha Berlin beat Nurnberg by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.402 per match): first half 2.913 vs last half 3.315 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 5.400)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.778)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 41 matches (11.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (41 of 165 home matches, 24.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (36 of 90 draw matches, 40.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (29 of 109 away matches, 26.6%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 15 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_goals_avg |corr| = 0.0908 (n=310 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — away_points_before_match spreads group means over 5.425: home 21.944, draw 27.040, away 21.615
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (11)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 364 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 364 |
| Average goals per match | 2.973 |
| Home win rate | 45.3% |
| Draw rate | 24.7% |
| Away win rate | 29.9% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | Schalke |
| Champion with most titles | Schalke |
| BTTS rate | 59.6% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 30.89 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.24 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.32 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 33.66 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.94 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 64.77 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 310 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 54 matches, expected 380
- **3.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **4.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 38.9% vs overall 45.3%
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 6 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
