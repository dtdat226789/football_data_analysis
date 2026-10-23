# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:59:18+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: J1 League (Japan)
- Scope: league `japan1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\japan1\database_profile.json | yes | yes | 31.28 |
| matches_analysis | E:\football_data_analysis\data\analysis\japan1\matches_analysis.json | yes | yes | 10.07 |
| goals_analysis | E:\football_data_analysis\data\analysis\japan1\goals_analysis.json | yes | yes | 6.20 |
| teams_analysis | E:\football_data_analysis\data\analysis\japan1\teams_analysis.json | yes | yes | 39.37 |
| season_trends | E:\football_data_analysis\data\analysis\japan1\season_trends.json | yes | yes | 3.90 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\japan1\scoreline_analysis.json | yes | yes | 51.98 |
| relationships | E:\football_data_analysis\data\analysis\japan1\relationships.json | yes | yes | 13.76 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 241 matches: home wins 54.4%, draws 7.1%, away wins 38.6% (131H / 17D / 93A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 11 home and 10 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — level at HT -> home win occurred 61 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 241 matches produced 699 goals (avg 2.900 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.6% vs away 46.4% of 699 goals in total (home/away ratio 1.16)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 137 of 241 matches (56.8%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 66 scoring matches, 27.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.22, median 31.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — FC Tokyo leads with 53 points across 2 seasons (0 title(s), GD 20)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 20 teams present in every one of the 2 seasons (Avispa Fukuoka, Cerezo Osaka, Chiba, FC Tokyo, Gamba Osaka...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Verdy earns 15 more points at home than away (23 home vs 8 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Kashima Antlers won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Vissel Kobe beat Kashiwa Reysol by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.092 per match): first half 2.87 vs last half 2.962 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026 (luck view, avg abs position diff 13.889)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 2-1 in 39 matches (16.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (39 of 131 home matches, 29.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (10 of 17 draw matches, 58.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (30 of 93 away matches, 32.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 5 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_team_goals_conceded_last_5 |corr| = -0.0788 (n=161 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — position_difference spreads group means over 2.205: home -0.862, draw -, away 1.343
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (15)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 241 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 241 |
| Average goals per match | 2.9 |
| Home win rate | 54.4% |
| Draw rate | 7.1% |
| Away win rate | 38.6% |
| Most common scoreline | 2-1 |
| Dominant team (lifetime points) | FC Tokyo |
| Champion with most titles | Kashima Antlers |
| BTTS rate | 56.8% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.28 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 10.07 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.20 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.37 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.90 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 51.98 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.76 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 161 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 36 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 80 matches, expected 380
- **4.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 draw outcome share 0.0% vs overall 7.1%
- **6.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 3.8% vs overall 1.2% (deviation 2.6 pp)
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 46.2% vs overall 54.4%
- **8.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 21.2% vs overall 7.1%
- **9.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 away outcome share 32.5% vs overall 38.6%
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **11.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows)
- **12.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows)
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=36 positions=1..36 teams=36
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=36 positions=1..36 teams=36
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=36 positions=1..36 teams=36

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
