# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:03:52+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Liga Portugal 2 (Portugal)
- Scope: league `portugal2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\portugal2\database_profile.json | yes | yes | 30.01 |
| matches_analysis | E:\football_data_analysis\data\analysis\portugal2\matches_analysis.json | yes | yes | 10.13 |
| goals_analysis | E:\football_data_analysis\data\analysis\portugal2\goals_analysis.json | yes | yes | 6.18 |
| teams_analysis | E:\football_data_analysis\data\analysis\portugal2\teams_analysis.json | yes | yes | 33.54 |
| season_trends | E:\football_data_analysis\data\analysis\portugal2\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\portugal2\scoreline_analysis.json | yes | yes | 63.26 |
| relationships | E:\football_data_analysis\data\analysis\portugal2\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 363 matches: home wins 42.1%, draws 24.2%, away wins 33.6% (153H / 88D / 122A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 9 home and 12 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 90 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 363 matches produced 874 goals (avg 2.408 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.1% vs away 47.9% of 874 goals in total (home/away ratio 1.09)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 164 of 363 matches (45.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 86 scoring matches, 26.4% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.61, median 30.5
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Maritimo leads with 66 points across 1 seasons (1 title(s), GD 21)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 14 teams present in every one of the 2 seasons (Benfica B, Chaves, FC Porto B, Feirense, Felgueiras...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Academico Viseu earns 13 more points at home than away (36 home vs 23 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Maritimo won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Lusitania FC beat Penafiel by 3 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — down (-0.102 per match): first half 2.423 vs last half 2.321 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (luck view, avg abs position diff 5.600)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 51 matches (14.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (51 of 153 home matches, 33.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 0-0 (37 of 88 draw matches, 42.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (33 of 122 away matches, 27.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 6 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.0901 (n=310 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — away_points_before_match spreads group means over 4.504: home 24.412, draw 19.908, away 22.340
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (10)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 363 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 363 |
| Average goals per match | 2.408 |
| Home win rate | 42.1% |
| Draw rate | 24.2% |
| Away win rate | 33.6% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Maritimo |
| Champion with most titles | Maritimo |
| BTTS rate | 45.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 30.01 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 10.13 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.18 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 33.54 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 63.26 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 310 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 53 matches, expected 380
- **3.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **4.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 7.5% vs overall 10.2% (deviation 2.7 pp)
- **6.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **7.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows)
- **8.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
