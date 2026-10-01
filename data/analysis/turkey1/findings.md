# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:10:39+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Super Lig (Turkey)
- Scope: league `turkey1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\turkey1\database_profile.json | yes | yes | 32.64 |
| matches_analysis | E:\football_data_analysis\data\analysis\turkey1\matches_analysis.json | yes | yes | 8.97 |
| goals_analysis | E:\football_data_analysis\data\analysis\turkey1\goals_analysis.json | yes | yes | 6.23 |
| teams_analysis | E:\football_data_analysis\data\analysis\turkey1\teams_analysis.json | yes | yes | 30.64 |
| season_trends | E:\football_data_analysis\data\analysis\turkey1\season_trends.json | yes | yes | 3.94 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\turkey1\scoreline_analysis.json | yes | yes | 60.41 |
| relationships | E:\football_data_analysis\data\analysis\turkey1\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 360 matches: home wins 43.1%, draws 27.8%, away wins 29.2% (155H / 100D / 105A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 6 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 97 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 360 matches produced 973 goals (avg 2.703 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 55.4% vs away 44.6% of 973 goals in total (home/away ratio 1.24)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 192 of 360 matches (53.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 108 scoring matches, 32.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.82, median 24.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Galatasaray leads with 90 points across 2 seasons (1 title(s), GD 50)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 15 teams present in every one of the 2 seasons (Alanyaspor, Basaksehir, Besiktas, Eyupspor, Fenerbahce...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Genclerbirligi earns 17 more points at home than away (29 home vs 12 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Galatasaray won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Amedspor beat Galatasaray by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.327 per match): first half 2.654 vs last half 2.981 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 5.333)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (goals view, avg abs position diff 3.556)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 47 matches (13.1%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (37 of 155 home matches, 23.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (47 of 100 draw matches, 47.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (28 of 105 away matches, 26.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 7 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_scored_last_5 |corr| = 0.1879 (n=306 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 10.561: home 3.163, draw 2.348, away -7.398
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (17)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 360 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 360 |
| Average goals per match | 2.703 |
| Home win rate | 43.1% |
| Draw rate | 27.8% |
| Away win rate | 29.2% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Galatasaray |
| Champion with most titles | Galatasaray |
| BTTS rate | 53.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.64 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.97 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.23 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 30.64 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.94 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 60.41 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 54 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.7% vs overall 8.3% (deviation 4.6 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 48.1% vs overall 43.1%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 20.4% vs overall 27.8%
- **9.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **10.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **11.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=30, fgte=30 rows)
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=18 positions=1..18 teams=18
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=18 positions=1..18 teams=18
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=18 positions=1..18 teams=18
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
