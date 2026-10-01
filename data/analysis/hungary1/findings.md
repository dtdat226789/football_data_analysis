# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:54:19+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: NB I. (Hungary)
- Scope: league `hungary1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\hungary1\database_profile.json | yes | yes | 32.07 |
| matches_analysis | E:\football_data_analysis\data\analysis\hungary1\matches_analysis.json | yes | yes | 8.92 |
| goals_analysis | E:\football_data_analysis\data\analysis\hungary1\goals_analysis.json | yes | yes | 6.30 |
| teams_analysis | E:\football_data_analysis\data\analysis\hungary1\teams_analysis.json | yes | yes | 22.88 |
| season_trends | E:\football_data_analysis\data\analysis\hungary1\season_trends.json | yes | yes | 3.92 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\hungary1\scoreline_analysis.json | yes | yes | 45.10 |
| relationships | E:\football_data_analysis\data\analysis\hungary1\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 245 matches: home wins 40.0%, draws 25.3%, away wins 34.7% (98H / 62D / 85A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 10 home and 5 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 55 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 245 matches produced 747 goals (avg 3.049 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 52.6% vs away 47.4% of 747 goals in total (home/away ratio 1.11)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 150 of 245 matches (61.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 74 scoring matches, 31.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.78, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Gyor leads with 84 points across 2 seasons (2 title(s), GD 41)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 10 teams present in every one of the 2 seasons (Debrecen, Ferencvaros, Gyor, Kisvarda, MTK Budapest...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — MTK Budapest earns 15 more points at home than away (31 home vs 16 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Gyor won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Gyor beat Puskas Academy by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.255 per match): first half 3.0 vs last half 3.255 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 5.000)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.333)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 31 matches (12.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (24 of 98 home matches, 24.5%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (31 of 62 draw matches, 50.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (21 of 85 away matches, 24.7%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 8 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_away_win_rate |corr| = -0.1807 (n=198 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — home_points_before_match spreads group means over 6.537: home 25.551, draw 19.837, away 19.014
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 245 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 245 |
| Average goals per match | 3.049 |
| Home win rate | 40.0% |
| Draw rate | 25.3% |
| Away win rate | 34.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Gyor |
| Champion with most titles | Gyor |
| BTTS rate | 61.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 32.07 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 8.92 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.30 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 22.88 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.92 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 45.10 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 198 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 12 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 47 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 12 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 29.8% vs overall 34.7%
- **7.** `HIGH_SCORING_MATCHES` *(warning)* — 3 match(es) with >= 8 total goals (extreme scorelines)
- **8.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **9.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=7, fgte=7 rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=12 positions=1..12 teams=12
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=12 positions=1..12 teams=12
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=12 positions=1..12 teams=12
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=12 positions=1..12 teams=12
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=12 positions=1..12 teams=12
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=12 positions=1..12 teams=12

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
