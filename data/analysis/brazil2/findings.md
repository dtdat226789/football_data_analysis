# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T15:45:49+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie B (Brazil)
- Scope: league `brazil2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\brazil2\database_profile.json | yes | yes | 29.64 |
| matches_analysis | E:\football_data_analysis\data\analysis\brazil2\matches_analysis.json | yes | yes | 12.15 |
| goals_analysis | E:\football_data_analysis\data\analysis\brazil2\goals_analysis.json | yes | yes | 6.21 |
| teams_analysis | E:\football_data_analysis\data\analysis\brazil2\teams_analysis.json | yes | yes | 57.87 |
| season_trends | E:\football_data_analysis\data\analysis\brazil2\season_trends.json | yes | yes | 3.87 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\brazil2\scoreline_analysis.json | yes | yes | 101.93 |
| relationships | E:\football_data_analysis\data\analysis\brazil2\relationships.json | yes | yes | 14.34 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 679 matches: home wins 45.4%, draws 29.2%, away wins 25.5% (308H / 198D / 173A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 21 home and 12 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 173 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 679 matches produced 1544 goals (avg 2.274 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 57.8% vs away 42.2% of 1544 goals in total (home/away ratio 1.37)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 331 of 679 matches (48.7%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 170 scoring matches, 27.4% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 34.81, median 29.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Novorizontino leads with 111 points across 2 seasons (0 title(s), GD 33)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 12 teams present in every one of the 2 seasons (America MG, Athletic Club, Atletico GO, Avai, Botafogo SP...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Vila Nova FC earns 39 more points at home than away (70 home vs 31 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Coritiba won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025: Coritiba beat Criciuma by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.126 per match): first half 2.218 vs last half 2.344 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025 (goals view, avg abs position diff 19.333)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026 (luck view, avg abs position diff 2.100)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-0 in 98 matches (14.4%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (98 of 308 home matches, 31.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (97 of 198 draw matches, 49.0%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (61 of 173 away matches, 35.3%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 4 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_position_before_match |corr| = 0.1414 (n=380 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — away_points_before_match spreads group means over 3.687: home 23.305, draw 26.991, away 26.822
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (9)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 679 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 679 |
| Average goals per match | 2.274 |
| Home win rate | 45.4% |
| Draw rate | 29.2% |
| Away win rate | 25.5% |
| Most common scoreline | 1-0 |
| Dominant team (lifetime points) | Novorizontino |
| Champion with most titles | Coritiba |
| BTTS rate | 48.7% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 29.64 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 12.15 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.21 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 57.87 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.87 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 101.93 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.34 |

## 5. Notable anomalies
- **1.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 57 teams, expected 20
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 299 matches, expected 380
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **4.** `HIGH_SCORING_MATCHES` *(warning)* — 1 match(es) with >= 8 total goals (extreme scorelines)
- **5.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **6.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=2, fgte=2 rows)
- **7.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=57 positions=1..57 teams=57
- **8.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=57 positions=1..57 teams=57
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=57 positions=1..57 teams=57

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
