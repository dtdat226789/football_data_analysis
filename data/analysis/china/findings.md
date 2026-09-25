# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:56:13+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Super League (China)
- Scope: league `china`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\china\database_profile.json | yes | yes | 31.53 |
| matches_analysis | E:\football_data_analysis\data\analysis\china\matches_analysis.json | yes | yes | 12.80 |
| goals_analysis | E:\football_data_analysis\data\analysis\china\goals_analysis.json | yes | yes | 6.28 |
| teams_analysis | E:\football_data_analysis\data\analysis\china\teams_analysis.json | yes | yes | 28.36 |
| season_trends | E:\football_data_analysis\data\analysis\china\season_trends.json | yes | yes | 3.90 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\china\scoreline_analysis.json | yes | yes | 74.71 |
| relationships | E:\football_data_analysis\data\analysis\china\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 448 matches: home wins 46.2%, draws 26.3%, away wins 27.5% (207H / 118D / 123A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 18 home and 16 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 130 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 448 matches produced 1414 goals (avg 3.156 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 56.7% vs away 43.3% of 1414 goals in total (home/away ratio 1.31)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 284 of 448 matches (63.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 149 scoring matches, 34.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 28.95, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Chengdu Rongcheng leads with 112 points across 2 seasons (1 title(s), GD 53)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 14 teams present in every one of the 2 seasons (Beijing Guoan, Chengdu Rongcheng, Dalian Yingbo, Henan Songshan Longmen, Qingdao Hainiu...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Dalian Yingbo earns 32 more points at home than away (54 home vs 22 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Shanghai Port won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025: Shanghai Port beat Shanghai Shenhua by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.121 per match): first half 3.212 vs last half 3.091 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026 (goals view, avg abs position diff 5.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025 (luck view, avg abs position diff 2.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 55 matches (12.3%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (43 of 207 home matches, 20.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (55 of 118 draw matches, 46.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (32 of 123 away matches, 26.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 17 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_scored_last_5 |corr| = 0.1135 (n=448 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.701: home 1.986, draw -0.364, away -4.715
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 448 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 448 |
| Average goals per match | 3.156 |
| Home win rate | 46.2% |
| Draw rate | 26.3% |
| Away win rate | 27.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Chengdu Rongcheng |
| Champion with most titles | Shanghai Port |
| BTTS rate | 63.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.53 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 12.80 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.28 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 28.36 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.90 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 74.71 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 208 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=4, fgte=4 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=16 positions=1..16 teams=16
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=16 positions=1..16 teams=16
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=16 positions=1..16 teams=16
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=16 positions=1..16 teams=16
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=16 positions=1..16 teams=16
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
