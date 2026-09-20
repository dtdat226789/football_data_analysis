# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-19T08:55:07+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Premier League (England)
- Scope: league `premier`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | /mnt/e/football_data_analysis/data/analysis/database_profile.json | yes | yes | 37.48 |
| matches_analysis | /mnt/e/football_data_analysis/data/analysis/matches_analysis.json | yes | yes | 31.44 |
| goals_analysis | /mnt/e/football_data_analysis/data/analysis/goals_analysis.json | yes | yes | 11.14 |
| teams_analysis | /mnt/e/football_data_analysis/data/analysis/teams_analysis.json | yes | yes | 37.56 |
| season_trends | /mnt/e/football_data_analysis/data/analysis/season_trends.json | yes | yes | 9.16 |
| scoreline_analysis | /mnt/e/football_data_analysis/data/analysis/scoreline_analysis.json | yes | yes | 357.29 |
| relationships | /mnt/e/football_data_analysis/data/analysis/relationships.json | yes | yes | 13.82 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2280 matches: home wins 43.1%, draws 23.6%, away wins 33.3% (983H / 537D / 760A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 69 home and 63 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 607 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2280 matches produced 6585 goals (avg 2.888 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.9% vs away 46.1% of 6585 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1237 of 2280 matches (54.3%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 737 scoring matches, 34.3% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.88, median 25.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Manchester City leads with 508 points across 6 seasons (4 title(s), GD 317)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 13 teams present in every one of the 6 seasons (Arsenal, Aston Villa, Brighton, Chelsea, Crystal Palace...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Newcastle earns 64 more points at home than away (202 home vs 138 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Manchester City won 4 of 6 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2021-2022: Manchester City beat Liverpool by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.199 per match): first half 2.789 vs last half 2.988 across 6 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2024-2025 (goals view, avg abs position diff 7.100)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2023-2024 (luck view, avg abs position diff 3.600)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 250 matches (11.0%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (189 of 983 home matches, 19.2%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (250 of 537 draw matches, 46.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (167 of 760 away matches, 22.0%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 64 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.076 (n=2280 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 11.426: home 5.189, draw -1.125, away -6.237
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (10)** — Anomaly codes: GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_AVG_GOALS_OUTLIER, SEASON_REGISTERED_NO_DATA
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 6 of 7 registered seasons populated (85.7%); 2280 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2280 |
| Average goals per match | 2.888 |
| Home win rate | 43.1% |
| Draw rate | 23.6% |
| Away win rate | 33.3% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Manchester City |
| Champion with most titles | Manchester City |
| BTTS rate | 54.3% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 37.48 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 31.44 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 11.14 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 37.56 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 9.16 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 357.29 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.82 |

## 5. Notable anomalies
- **1.** `SEASON_REGISTERED_NO_DATA` *(warning)* — Season 2026-2027 is registered but has no match data (declared_by_api=True, state=unknown)
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 0 matches, expected 380
- **3.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2020-2021 goalless share 7.9% vs overall 5.7% (deviation 2.2 pp)
- **4.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 home outcome share 37.9% vs overall 43.1%
- **5.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2020-2021 away outcome share 40.3% vs overall 33.3%
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 home outcome share 48.4% vs overall 43.1%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022-2023 away outcome share 28.7% vs overall 33.3%
- **8.** `SEASON_AVG_GOALS_OUTLIER` *(warning)* — Season 2023-2024 avg goals 3.279 vs overall 2.888 (deviation 0.391)
- **9.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2023-2024 goalless share 2.9% vs overall 5.7% (deviation 2.8 pp)
- **10.** `HIGH_SCORING_MATCHES` *(warning)* — 17 match(es) with >= 8 total goals (extreme scorelines)

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
