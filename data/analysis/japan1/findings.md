# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:59:00+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: J1 League (Japan)
- Scope: league `japan1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/japan1/database_profile.json | yes | yes | 49.77 |
| matches_analysis | data/analysis/japan1/matches_analysis.json | yes | yes | 29.76 |
| goals_analysis | data/analysis/japan1/goals_analysis.json | yes | yes | 13.43 |
| teams_analysis | data/analysis/japan1/teams_analysis.json | yes | yes | 40.23 |
| season_trends | data/analysis/japan1/season_trends.json | yes | yes | 11.71 |
| scoreline_analysis | data/analysis/japan1/scoreline_analysis.json | yes | yes | 353.07 |
| relationships | data/analysis/japan1/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2339 matches: home wins 42.3%, draws 24.2%, away wins 33.4% (990H / 567D / 782A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 64 home and 52 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 538 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2339 matches produced 6077 goals (avg 2.598 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.7% vs away 46.3% of 6077 goals in total (home/away ratio 1.16)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1193 of 2339 matches (51.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 653 scoring matches, 30.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.63, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Kawasaki Frontale leads with 446 points across 8 seasons (2 title(s), GD 160)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 11 teams present in every one of the 8 seasons (Cerezo Osaka, FC Tokyo, Gamba Osaka, Kashima Antlers, Kashiwa Reysol...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Nagoya Grampus earns 72 more points at home than away (218 home vs 146 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Kawasaki Frontale won 2 of 8 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Machida beat FC Tokyo by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.149 per match): first half 2.578 vs last half 2.727 across 8 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2020 (goals view, avg abs position diff 14.500)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.200)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 257 matches (11.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (248 of 990 home matches, 25.1%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (257 of 567 draw matches, 45.3%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (225 of 782 away matches, 28.8%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 51 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_conceded_avg |corr| = 0.0597 (n=2219 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.241: home 2.631, draw -1.390, away -2.610
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (39)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 8 of 8 registered seasons populated (100.0%); 2339 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2339 |
| Average goals per match | 2.598 |
| Home win rate | 42.3% |
| Draw rate | 24.2% |
| Away win rate | 33.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Kawasaki Frontale |
| Champion with most titles | Kawasaki Frontale |
| BTTS rate | 51.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 49.77 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 29.76 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 13.43 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 40.23 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 11.71 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 353.07 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 306 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2020 has 18 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 306 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2022 has 18 teams, expected 20
- **5.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 306 matches, expected 380
- **6.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 18 teams, expected 20
- **7.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 161 matches, expected 380
- **8.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 120 matches, expected 380
- **9.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **10.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020 away outcome share 39.2% vs overall 33.4%
- **11.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022 goalless share 11.8% vs overall 8.0% (deviation 3.8 pp)
- **12.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022 draw outcome share 31.7% vs overall 24.2%
- **13.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022 away outcome share 28.4% vs overall 33.4%
- **14.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 0.0% vs overall 8.0% (deviation 8.0 pp)
- **15.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 home outcome share 58.4% vs overall 42.3%
- **16.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 draw outcome share 0.0% vs overall 24.2%
- **17.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 away outcome share 41.6% vs overall 33.4%
- **18.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2026-2027 avg goals 2.975 vs overall 2.598 (deviation 0.377)
- **19.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 5.8% vs overall 8.0% (deviation 2.2 pp)
- **20.** `HIGH_SCORING_MATCHES` *(warning)* — 21 match(es) with >= 8 total goals (extreme scorelines)
- **21.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **22.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=366, fgte=366 rows)
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=18 positions=1..19 teams=18
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=18 positions=12..34 teams=18
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=18 positions=1..36 teams=18
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=20 positions=5..35 teams=20
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=20 positions=1..40 teams=20
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=18 positions=1..18 teams=18
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=18 positions=6..33 teams=18
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=18 positions=1..35 teams=18
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=18 positions=1..18 teams=18
- **32.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=18 positions=1..18 teams=18
- **33.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=18 positions=1..18 teams=18
- **34.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=20 positions=1..21 teams=20
- **35.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=20 positions=6..37 teams=20
- **36.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=20 positions=1..40 teams=20
- **37.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=20 positions=1..22 teams=20
- **38.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=20 positions=3..27 teams=20
- **39.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=20 positions=1..36 teams=20

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
