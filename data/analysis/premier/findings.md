# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T13:42:19+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier League (England)
- Scope: league `premier`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\premier\database_profile.json | yes | yes | 42.83 |
| matches_analysis | E:\football_data_analysis\data\analysis\premier\matches_analysis.json | yes | yes | 33.62 |
| goals_analysis | E:\football_data_analysis\data\analysis\premier\goals_analysis.json | yes | yes | 12.93 |
| teams_analysis | E:\football_data_analysis\data\analysis\premier\teams_analysis.json | yes | yes | 42.22 |
| season_trends | E:\football_data_analysis\data\analysis\premier\season_trends.json | yes | yes | 11.07 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\premier\scoreline_analysis.json | yes | yes | 379.86 |
| relationships | E:\football_data_analysis\data\analysis\premier\relationships.json | yes | yes | 14.46 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2330 matches: home wins 43.0%, draws 23.7%, away wins 33.3% (1001H / 553D / 776A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 70 home and 64 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 619 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2330 matches produced 6726 goals (avg 2.887 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.9% vs away 46.1% of 6726 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1262 of 2330 matches (54.2%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 753 scoring matches, 34.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.93, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Manchester City leads with 523 points across 7 seasons (5 title(s), GD 325)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 11 teams present in every one of the 7 seasons (Arsenal, Aston Villa, Brighton, Chelsea, Crystal Palace...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Newcastle earns 66 more points at home than away (207 home vs 141 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Manchester City won 5 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2021-2022: Manchester City beat Liverpool by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.046 per match): first half 2.789 vs last half 2.835 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 7.100)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 2.200)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 255 matches (10.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (192 of 1001 home matches, 19.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (255 of 553 draw matches, 46.1%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (173 of 776 away matches, 22.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 67 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.074 (n=2330 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 11.233: home 5.098, draw -1.078, away -6.135
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (16)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_STATE_NOT_COMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2330 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2330 |
| Average goals per match | 2.887 |
| Home win rate | 43.0% |
| Draw rate | 23.7% |
| Away win rate | 33.3% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Manchester City |
| Champion with most titles | Manchester City |
| BTTS rate | 54.2% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 42.83 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 33.62 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.93 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 42.22 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 11.07 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 379.86 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.46 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 50 matches, expected 380
- **2.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **3.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 7.9% vs overall 5.8% (deviation 2.1 pp)
- **4.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 37.9% vs overall 43.0%
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 40.3% vs overall 33.3%
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 home outcome share 48.4% vs overall 43.0%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 away outcome share 28.7% vs overall 33.3%
- **8.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2023-2024 avg goals 3.279 vs overall 2.887 (deviation 0.392)
- **9.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 2.9% vs overall 5.8% (deviation 2.9 pp)
- **10.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2024-2025 goalless share 4.2% vs overall 5.8% (deviation 1.6 pp)
- **11.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 10.0% vs overall 5.8% (deviation 4.2 pp)
- **12.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 36.0% vs overall 43.0%
- **13.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 32.0% vs overall 23.7%
- **14.** `HIGH_SCORING_MATCHES` *(warning)* — 18 match(es) with >= 8 total goals (extreme scorelines)
- **15.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows)
- **16.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
