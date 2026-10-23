# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-29T16:09:41+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Superettan (Sweden)
- Scope: league `sweden2`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\sweden2\database_profile.json | yes | yes | 31.52 |
| matches_analysis | E:\football_data_analysis\data\analysis\sweden2\matches_analysis.json | yes | yes | 11.88 |
| goals_analysis | E:\football_data_analysis\data\analysis\sweden2\goals_analysis.json | yes | yes | 6.28 |
| teams_analysis | E:\football_data_analysis\data\analysis\sweden2\teams_analysis.json | yes | yes | 31.16 |
| season_trends | E:\football_data_analysis\data\analysis\sweden2\season_trends.json | yes | yes | 3.88 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\sweden2\scoreline_analysis.json | yes | yes | 70.90 |
| relationships | E:\football_data_analysis\data\analysis\sweden2\relationships.json | yes | yes | 14.33 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 440 matches: home wins 40.5%, draws 27.0%, away wins 32.5% (178H / 119D / 143A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 21 home and 11 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 100 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 440 matches produced 1266 goals (avg 2.877 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 53.9% vs away 46.1% of 1266 goals in total (home/away ratio 1.17)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 253 of 440 matches (57.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 154 scoring matches, 37.7% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 29.18, median 23.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Falkenberg leads with 91 points across 2 seasons (0 title(s), GD 30)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 10 teams present in every one of the 2 seasons (Brage, Falkenberg, Helsingborg, Landskrona, Oddevold...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Ostersund earns 21 more points at home than away (50 home vs 29 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Vasteras SK won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2025: Vasteras SK beat Kalmar by 1 pt
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — stable (+0.042 per match): first half 2.858 vs last half 2.9 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026 (goals view, avg abs position diff 5.250)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026 (luck view, avg abs position diff 0.875)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 45 matches (10.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (37 of 178 home matches, 20.8%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (45 of 119 draw matches, 37.8%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (33 of 143 away matches, 23.1%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 6 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — points_difference |corr| = 0.1676 (n=240 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 7.307: home 3.604, draw -2.677, away -3.703
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (14)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 440 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 440 |
| Average goals per match | 2.877 |
| Home win rate | 40.5% |
| Draw rate | 27.0% |
| Away win rate | 32.5% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Falkenberg |
| Champion with most titles | Vasteras SK |
| BTTS rate | 57.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.52 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 11.88 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.28 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 31.16 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.88 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 70.90 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.33 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 240 matches, expected 380
- **2.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 16 teams, expected 20
- **3.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 200 matches, expected 380
- **4.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 16 teams, expected 20
- **5.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **6.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **7.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows)
- **8.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=30, fgte=30 rows)
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=16 positions=1..16 teams=16
- **10.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=16 positions=1..16 teams=16
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=16 positions=1..16 teams=16
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/classic rows=16 positions=1..16 teams=16
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/goals rows=16 positions=1..16 teams=16
- **14.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026/luck rows=16 positions=1..16 teams=16

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
