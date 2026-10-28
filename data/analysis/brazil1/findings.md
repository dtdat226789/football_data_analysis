# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-27T01:41:34+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie A Betano (Brazil)
- Scope: league `brazil1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/brazil1/database_profile.json | yes | yes | 43.79 |
| matches_analysis | data/analysis/brazil1/matches_analysis.json | yes | yes | 23.66 |
| goals_analysis | data/analysis/brazil1/goals_analysis.json | yes | yes | 12.26 |
| teams_analysis | data/analysis/brazil1/teams_analysis.json | yes | yes | 39.93 |
| season_trends | data/analysis/brazil1/season_trends.json | yes | yes | 10.30 |
| scoreline_analysis | data/analysis/brazil1/scoreline_analysis.json | yes | yes | 364.80 |
| relationships | data/analysis/brazil1/relationships.json | yes | yes | 13.80 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2571 matches: home wins 46.7%, draws 27.6%, away wins 25.7% (1201H / 709D / 661A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 46 home and 43 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 624 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2571 matches produced 6296 goals (avg 2.449 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 58.0% vs away 42.0% of 6296 goals in total (home/away ratio 1.38)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1296 of 2571 matches (50.4%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 616 scoring matches, 29.5% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 33.79, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Palmeiras leads with 484 points across 7 seasons (2 title(s), GD 188)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 8 teams present in every one of the 7 seasons (Atletico-MG, Bragantino, Corinthians, Flamengo RJ, Fluminense...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Fluminense earns 133 more points at home than away (269 home vs 136 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Flamengo RJ won 4 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2023: Palmeiras beat Gremio by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.182 per match): first half 2.361 vs last half 2.543 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2021 (goals view, avg abs position diff 31.900)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026 (luck view, avg abs position diff 3.000)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 352 matches (13.7%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (331 of 1201 home matches, 27.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (352 of 709 draw matches, 49.6%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (204 of 661 away matches, 30.9%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 27 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_position_before_match |corr| = -0.0686 (n=2275 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 5.985: home 2.209, draw -1.383, away -3.776
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (26)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2571 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2571 |
| Average goals per match | 2.449 |
| Home win rate | 46.7% |
| Draw rate | 27.6% |
| Away win rate | 25.7% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Palmeiras |
| Champion with most titles | Flamengo RJ |
| BTTS rate | 50.4% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 43.79 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 23.66 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.26 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 39.93 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.30 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 364.80 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.80 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2023 has 375 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 296 matches, expected 380
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **4.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021 goalless share 11.6% vs overall 7.9% (deviation 3.7 pp)
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 5.7% vs overall 7.9% (deviation 2.2 pp)
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 10 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=294, fgte=294 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=20 positions=1..22 teams=20
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=20 positions=7..37 teams=20
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=20 positions=1..58 teams=20
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=20 positions=1..22 teams=20
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=20 positions=30..59 teams=20
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=20 positions=2..74 teams=20
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=20 positions=1..22 teams=20
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=20 positions=15..47 teams=20
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=20 positions=1..58 teams=20
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=20 positions=1..22 teams=20
- **19.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=20 positions=8..50 teams=20
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=20 positions=1..58 teams=20
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=20 positions=1..22 teams=20
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=20 positions=20..54 teams=20
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=20 positions=1..58 teams=20
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=20 positions=1..21 teams=20
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=20 positions=10..34 teams=20
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=20 positions=1..40 teams=20

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
