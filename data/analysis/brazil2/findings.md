# Consolidated Findings
- Report: `findings`
- Generated: 2026-10-29T01:55:00+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie B (Brazil)
- Scope: league `brazil2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | data/analysis/brazil2/database_profile.json | yes | yes | 45.18 |
| matches_analysis | data/analysis/brazil2/matches_analysis.json | yes | yes | 26.39 |
| goals_analysis | data/analysis/brazil2/goals_analysis.json | yes | yes | 12.19 |
| teams_analysis | data/analysis/brazil2/teams_analysis.json | yes | yes | 58.20 |
| season_trends | data/analysis/brazil2/season_trends.json | yes | yes | 10.29 |
| scoreline_analysis | data/analysis/brazil2/scoreline_analysis.json | yes | yes | 362.87 |
| relationships | data/analysis/brazil2/relationships.json | yes | yes | 13.78 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 2623 matches: home wins 46.9%, draws 28.9%, away wins 24.2% (1229H / 758D / 636A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 66 home and 39 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 704 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 2623 matches produced 5687 goals (avg 2.168 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 59.3% vs away 40.7% of 5687 goals in total (home/away ratio 1.46)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 1180 of 2623 matches (45.0%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 647 scoring matches, 27.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 35.18, median 30.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — CRB leads with 373 points across 7 seasons (0 title(s), GD 11)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 1 teams present in every one of the 7 seasons (CRB)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — CRB earns 117 more points at home than away (245 home vs 128 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — America MG won 1 of 7 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026: Novorizontino beat Juventude by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.126 per match): first half 2.119 vs last half 2.246 across 7 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025 (luck view, avg abs position diff 23.100)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026 (luck view, avg abs position diff 1.600)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 404 matches (15.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (404 of 1229 home matches, 32.9%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (359 of 758 draw matches, 47.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (255 of 636 away matches, 40.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 13 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.0878 (n=2273 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 3.764: home 1.012, draw -0.684, away -2.752
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (31)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 7 of 7 registered seasons populated (100.0%); 2623 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 2623 |
| Average goals per match | 2.168 |
| Home win rate | 46.9% |
| Draw rate | 28.9% |
| Away win rate | 24.2% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | CRB |
| Champion with most titles | America MG |
| BTTS rate | 45.0% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 45.18 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 26.39 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 12.19 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 58.20 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 10.29 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 362.87 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 13.78 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2024 has 373 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 350 matches, expected 380
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **4.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2021 goalless share 12.4% vs overall 10.8% (deviation 1.6 pp)
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2022 goalless share 12.9% vs overall 10.8% (deviation 2.1 pp)
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2022 away outcome share 18.4% vs overall 24.2%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2024 home outcome share 52.3% vs overall 46.9%
- **8.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2025 goalless share 8.7% vs overall 10.8% (deviation 2.1 pp)
- **9.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026 goalless share 8.3% vs overall 10.8% (deviation 2.5 pp)
- **10.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026 away outcome share 28.6% vs overall 24.2%
- **11.** `HIGH_SCORING_MATCHES` *(warning)* — 3 match(es) with >= 8 total goals (extreme scorelines)
- **12.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **13.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=294, fgte=294 rows)
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/classic rows=20 positions=1..22 teams=20
- **15.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/goals rows=20 positions=11..40 teams=20
- **16.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2020/luck rows=20 positions=1..58 teams=20
- **17.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/classic rows=20 positions=1..21 teams=20
- **18.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/goals rows=20 positions=10..34 teams=20
- **19.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2021/luck rows=20 positions=1..40 teams=20
- **20.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/classic rows=20 positions=1..22 teams=20
- **21.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/goals rows=20 positions=15..42 teams=20
- **22.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2022/luck rows=20 positions=1..58 teams=20
- **23.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/classic rows=20 positions=1..21 teams=20
- **24.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/goals rows=20 positions=5..32 teams=20
- **25.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2023/luck rows=20 positions=1..40 teams=20
- **26.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/classic rows=20 positions=1..22 teams=20
- **27.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/goals rows=20 positions=13..43 teams=20
- **28.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2024/luck rows=20 positions=1..56 teams=20
- **29.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=20 positions=1..23 teams=20
- **30.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=20 positions=13..48 teams=20
- **31.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=20 positions=1..57 teams=20

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
