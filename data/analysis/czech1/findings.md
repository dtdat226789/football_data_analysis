# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:56:23+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Chance Liga (Czech Republic)
- Scope: league `czech1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\czech1\database_profile.json | yes | yes | 31.93 |
| matches_analysis | E:\football_data_analysis\data\analysis\czech1\matches_analysis.json | yes | yes | 8.42 |
| goals_analysis | E:\football_data_analysis\data\analysis\czech1\goals_analysis.json | yes | yes | 6.41 |
| teams_analysis | E:\football_data_analysis\data\analysis\czech1\teams_analysis.json | yes | yes | 28.49 |
| season_trends | E:\football_data_analysis\data\analysis\czech1\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\czech1\scoreline_analysis.json | yes | yes | 62.24 |
| relationships | E:\football_data_analysis\data\analysis\czech1\relationships.json | yes | yes | 14.35 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 351 matches: home wins 42.7%, draws 23.4%, away wins 33.9% (150H / 82D / 119A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 7 home and 5 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 98 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 351 matches produced 941 goals (avg 2.681 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.2% vs away 46.8% of 941 goals in total (home/away ratio 1.14)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 177 of 351 matches (50.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 104 scoring matches, 32.2% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.83, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Slavia Prague leads with 103 points across 2 seasons (2 title(s), GD 62)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 15 teams present in every one of the 2 seasons (Artis Brno, Bohemians, FK Pardubice, Hradec Kralove, Jablonec...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Hradec Kralove earns 18 more points at home than away (44 home vs 26 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Slavia Prague won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Slavia Prague beat Liberec by 3 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.188 per match): first half 2.643 vs last half 2.831 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 5.889)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.875)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 37 matches (10.5%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-0 (35 of 150 home matches, 23.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (37 of 82 draw matches, 45.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (28 of 119 away matches, 23.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 7 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_win_rate |corr| = -0.1197 (n=351 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.959: home 3.253, draw 1.256, away -4.706
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 351 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 351 |
| Average goals per match | 2.681 |
| Home win rate | 42.7% |
| Draw rate | 23.4% |
| Away win rate | 33.9% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Slavia Prague |
| Champion with most titles | Slavia Prague |
| BTTS rate | 50.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.93 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.42 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.41 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 28.49 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 62.24 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.35 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 280 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 71 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 5.6% vs overall 7.7% (deviation 2.1 pp)
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 3 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
