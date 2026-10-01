# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:43:45+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Ligue 1 (Algeria)
- Scope: league `algir1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\algir1\database_profile.json | yes | yes | 31.69 |
| matches_analysis | E:\football_data_analysis\data\analysis\algir1\matches_analysis.json | yes | yes | 7.61 |
| goals_analysis | E:\football_data_analysis\data\analysis\algir1\goals_analysis.json | yes | yes | 6.22 |
| teams_analysis | E:\football_data_analysis\data\analysis\algir1\teams_analysis.json | yes | yes | 28.00 |
| season_trends | E:\football_data_analysis\data\analysis\algir1\season_trends.json | yes | yes | 3.92 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\algir1\scoreline_analysis.json | yes | yes | 44.74 |
| relationships | E:\football_data_analysis\data\analysis\algir1\relationships.json | yes | yes | 14.30 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 263 matches: home wins 49.4%, draws 29.7%, away wins 20.9% (130H / 78D / 55A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 6 home and 2 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 73 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 263 matches produced 600 goals (avg 2.281 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 60.2% vs away 39.8% of 600 goals in total (home/away ratio 1.51)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 125 of 263 matches (47.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 65 scoring matches, 27.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 35.51, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — MC Alger leads with 68 points across 2 seasons (1 title(s), GD 25)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 2 seasons (ASO Chlef, Ben Aknoun, CR Belouizdad, Constantine, ES Setif...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Rouisset earns 25 more points at home than away (32 home vs 7 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — MC Alger won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: CR Belouizdad beat USM Alger by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.168 per match): first half 2.267 vs last half 2.435 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025-2026 (goals view, avg abs position diff 4.625)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2025-2026 (luck view, avg abs position diff 1.500)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 49 matches (18.6%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (49 of 130 home matches, 37.7%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (38 of 78 draw matches, 48.7%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (22 of 55 away matches, 40.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 4 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_rest_days |corr| = 0.2701 (n=232 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.925: home 1.825, draw -1.243, away -5.100
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 263 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 263 |
| Average goals per match | 2.281 |
| Home win rate | 49.4% |
| Draw rate | 29.7% |
| Away win rate | 20.9% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | MC Alger |
| Champion with most titles | MC Alger |
| BTTS rate | 47.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.69 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 7.61 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.22 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 28.00 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.92 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 44.74 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.30 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 23 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 43.5% vs overall 49.4%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 34.8% vs overall 29.7%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/classic rows=16 positions=1..16 teams=16
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/goals rows=16 positions=1..16 teams=16
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025-2026/luck rows=16 positions=1..16 teams=16
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=16 positions=1..16 teams=16
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=16 positions=1..16 teams=16
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
