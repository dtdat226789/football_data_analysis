# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:24:26+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Bundesliga Women (Germany)
- Scope: league `wgermany1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\wgermany1\database_profile.json | yes | yes | 32.42 |
| matches_analysis | E:\football_data_analysis\data\analysis\wgermany1\matches_analysis.json | yes | yes | 8.88 |
| goals_analysis | E:\football_data_analysis\data\analysis\wgermany1\goals_analysis.json | yes | yes | 6.40 |
| teams_analysis | E:\football_data_analysis\data\analysis\wgermany1\teams_analysis.json | yes | yes | 25.74 |
| season_trends | E:\football_data_analysis\data\analysis\wgermany1\season_trends.json | yes | yes | 4.00 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\wgermany1\scoreline_analysis.json | yes | yes | 44.90 |
| relationships | E:\football_data_analysis\data\analysis\wgermany1\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 217 matches: home wins 45.2%, draws 17.1%, away wins 37.8% (98H / 37D / 82A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 5 home and 9 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 71 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 217 matches produced 748 goals (avg 3.447 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.0% vs away 48.0% of 748 goals in total (home/away ratio 1.08)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 131 of 217 matches (60.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 90 scoring matches, 42.9% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 24.43, median 19.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Bayern Munich W leads with 89 points across 2 seasons (2 title(s), GD 93)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (1.FC Nurnberg W, Bayer Leverkusen W, Bayern Munich W, Eintracht Frankfurt W, Freiburg W...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Eintracht Frankfurt W earns 18 more points at home than away (41 home vs 23 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Bayern Munich W won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Bayern Munich W beat Eintracht Frankfurt W by 2 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.012 per match): first half 3.445 vs last half 3.457 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.286)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 22 matches (10.1%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (20 of 98 home matches, 20.4%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (22 of 37 draw matches, 59.5%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (15 of 82 away matches, 18.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 10 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_goals_scored_last_5 |corr| = 0.1658 (n=182 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 14.473: home 5.778, draw 1.656, away -8.696
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 217 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 217 |
| Average goals per match | 3.447 |
| Home win rate | 45.2% |
| Draw rate | 17.1% |
| Away win rate | 37.8% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Bayern Munich W |
| Champion with most titles | Bayern Munich W |
| BTTS rate | 60.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.42 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.88 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.40 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 25.74 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 4.00 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 44.90 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 182 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 14 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 35 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 14 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 0.0% vs overall 3.2% (deviation 3.2 pp)
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 5 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=35, fgte=35 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=14 positions=1..14 teams=14
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=14 positions=1..14 teams=14
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=14 positions=1..14 teams=14
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=14 positions=1..14 teams=14
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=14 positions=1..14 teams=14
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=14 positions=1..14 teams=14

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
