# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:55:32+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Serie A Betano (Brazil)
- Scope: league `brazil1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\brazil1\database_profile.json | yes | yes | 29.84 |
| matches_analysis | E:\football_data_analysis\data\analysis\brazil1\matches_analysis.json | yes | yes | 11.55 |
| goals_analysis | E:\football_data_analysis\data\analysis\brazil1\goals_analysis.json | yes | yes | 6.22 |
| teams_analysis | E:\football_data_analysis\data\analysis\brazil1\teams_analysis.json | yes | yes | 44.67 |
| season_trends | E:\football_data_analysis\data\analysis\brazil1\season_trends.json | yes | yes | 3.89 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\brazil1\scoreline_analysis.json | yes | yes | 101.77 |
| relationships | E:\football_data_analysis\data\analysis\brazil1\relationships.json | yes | yes | 14.37 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 657 matches: home wins 48.9%, draws 26.8%, away wins 24.4% (321H / 176D / 160A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 19 home and 11 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 203 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 657 matches produced 1698 goals (avg 2.584 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 59.0% vs away 41.0% of 1698 goals in total (home/away ratio 1.44)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 345 of 657 matches (52.5%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 184 scoring matches, 30.0% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 31.82, median 27.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Flamengo RJ leads with 139 points across 2 seasons (2 title(s), GD 83)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 16 teams present in every one of the 2 seasons (Atletico-MG, Bahia, Botafogo RJ, Bragantino, Corinthians...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Fluminense earns 46 more points at home than away (79 home vs 33 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Flamengo RJ won 2 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026: Flamengo RJ beat Palmeiras by 3 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.144 per match): first half 2.524 vs last half 2.668 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2025 (goals view, avg abs position diff 12.550)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026 (luck view, avg abs position diff 2.400)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 87 matches (13.2%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 1-0 (79 of 321 home matches, 24.6%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (87 of 176 draw matches, 49.4%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 0-1 (44 of 160 away matches, 27.5%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 3 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — home_points_before_match |corr| = 0.0755 (n=657 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.55: home 2.012, draw -1.295, away -4.537
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (9)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 657 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 657 |
| Average goals per match | 2.584 |
| Home win rate | 48.9% |
| Draw rate | 26.8% |
| Away win rate | 24.4% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Flamengo RJ |
| Champion with most titles | Flamengo RJ |
| BTTS rate | 52.5% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 29.84 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 11.55 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.22 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 44.67 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.89 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 101.77 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.37 |

## 5. Notable anomalies
- **1.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2025 has 40 teams, expected 20
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026 has 277 matches, expected 380
- **3.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026 has data but state is 'in_progress'
- **4.** `HIGH_SCORING_MATCHES` *(warning)* — 2 match(es) with >= 8 total goals (extreme scorelines)
- **5.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **6.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=2, fgte=2 rows)
- **7.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/classic rows=40 positions=1..40 teams=40
- **8.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/goals rows=40 positions=1..40 teams=40
- **9.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2025/luck rows=40 positions=1..40 teams=40

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
