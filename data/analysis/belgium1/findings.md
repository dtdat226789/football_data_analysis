# Consolidated Findings
- Report: `findings`
- Generated: 2026-09-23T10:55:21+00:00
- Script: `backend/scripts/compile_findings.py` v1.0.0
- League: Jupiler Pro League (Belgium)
- Scope: league `belgium1`

## 1. Sources
| report | path | exists | loaded | size (KB) |
|---|---|---|---|---|
| database_profile | E:\football_data_analysis\data\analysis\belgium1\database_profile.json | yes | yes | 31.35 |
| matches_analysis | E:\football_data_analysis\data\analysis\belgium1\matches_analysis.json | yes | yes | 9.73 |
| goals_analysis | E:\football_data_analysis\data\analysis\belgium1\goals_analysis.json | yes | yes | 6.42 |
| teams_analysis | E:\football_data_analysis\data\analysis\belgium1\teams_analysis.json | yes | yes | 31.48 |
| season_trends | E:\football_data_analysis\data\analysis\belgium1\season_trends.json | yes | yes | 3.96 |
| scoreline_analysis | E:\football_data_analysis\data\analysis\belgium1\scoreline_analysis.json | yes | yes | 66.86 |
| relationships | E:\football_data_analysis\data\analysis\belgium1\relationships.json | yes | yes | 14.36 |
- Coverage: **7** of **7** module reports found (all reports present)

## 2. Key findings
- **F1** · `matches_analysis` · *[medium]* — **Outcome split across all seasons** — 384 matches: home wins 42.7%, draws 24.2%, away wins 33.1% (164H / 93D / 127A)
- **F2** · `matches_analysis` · *[medium]* — **Comeback wins** — 9 home and 10 away comebacks (trailing at HT but winning at FT)
- **F3** · `matches_analysis` · *[low]* — **Most common HT/FT flow** — home lead at HT -> home win occurred 99 times
- **F4** · `goals_analysis` · *[medium]* — **Average goals per match** — 384 matches produced 1049 goals (avg 2.732 per match)
- **F5** · `goals_analysis` · *[medium]* — **Home goal share** — home 54.5% vs away 45.5% of 1049 goals in total (home/away ratio 1.20)
- **F6** · `goals_analysis` · *[medium]* — **Both teams to score** — 200 of 384 matches (52.1%)
- **F7** · `goals_analysis` · *[low]* — **Most common first-goal bucket** — minute 1-15 (first goal in 123 scoring matches, 34.6% of scoring)
- **F8** · `goals_analysis` · *[low]* — **Average first goal minute** — mean 30.46, median 24.0
- **F9** · `teams_analysis` · *[high]* — **Dominant team by lifetime points** — Club Brugge KV leads with 106 points across 2 seasons (1 title(s), GD 58)
- **F10** · `teams_analysis` · *[medium]* — **Team consistency** — 16 teams present in every one of the 2 seasons (Anderlecht, Antwerp, Cercle Brugge KSV, Charleroi, Club Brugge KV...)
- **F11** · `teams_analysis` · *[medium]* — **Biggest home advantage** — Anderlecht earns 22 more points at home than away (45 home vs 23 away)
- **F12** · `season_trends` · *[high]* — **Champion with most titles** — Club Brugge KV won 1 of 2 championship(s) on record
- **F13** · `season_trends` · *[medium]* — **Tightest title race** — 2026-2027: Royale Union SG beat Gent by 0 pts
- **F14** · `season_trends` · *[medium]* — **Average-goals trend** — up (+0.245 per match): first half 2.692 vs last half 2.937 across 2 seasons
- **F15** · `season_trends` · *[low]* — **Largest view divergence** — 2026-2027 (goals view, avg abs position diff 6.222)
- **F16** · `season_trends` · *[low]* — **Smallest view divergence** — 2026-2027 (luck view, avg abs position diff 1.889)
- **F17** · `scoreline_analysis` · *[medium]* — **Most common scoreline** — 1-1 in 42 matches (10.9%)
- **F18** · `scoreline_analysis` · *[low]* — **Most common home-win scoreline** — 2-1 (35 of 164 home matches, 21.3%)
- **F19** · `scoreline_analysis` · *[low]* — **Most common draw scoreline** — 1-1 (42 of 93 draw matches, 45.2%)
- **F20** · `scoreline_analysis` · *[low]* — **Most common away-win scoreline** — 1-2 (32 of 127 away matches, 25.2%)
- **F21** · `scoreline_analysis` · *[low]* — **Extreme scorelines** — 8 match(es) with >= 7 total goals
- **F22** · `relationships` · *[medium]* — **Strongest correlation with total goals** — away_team_wins_last_5 |corr| = -0.0976 (n=384 leakage-safe rows)
- **F23** · `relationships` · *[medium]* — **Most outcome-separating feature** — points_difference spreads group means over 6.091: home 2.823, draw -1.022, away -3.268
- **F24** · `database_profile` · *[high]* — **Data-quality warnings (13)** — Anomaly codes: DUPLICATE_ROWS, FIRST_GOAL_NULL_INCONSISTENCY, GOALLESS_SHARE_OUTLIER, HIGH_SCORING_MATCHES, MATCH_COUNT_UNEXPECTED, OUTCOME_SHARE_OUTLIER, SEASON_STATE_NOT_COMPLETE, STANDINGS_INCOMPLETE, TEAM_COUNT_UNEXPECTED
- **F25** · `database_profile` · *[medium]* — **Data coverage** — 2 of 2 registered seasons populated (100.0%); 384 matches observed

## 3. Cross-module headline stats
| stat | value |
|---|---|
| Matches analysed | 384 |
| Average goals per match | 2.732 |
| Home win rate | 42.7% |
| Draw rate | 24.2% |
| Away win rate | 33.1% |
| Most common scoreline | 1-1 |
| Dominant team (lifetime points) | Club Brugge KV |
| Champion with most titles | Club Brugge KV |
| BTTS rate | 52.1% |

## 4. Module comparison
| module | report_name | sections present | size (KB) |
|---|---|---|---|
| database_profile | database_profile | observed, calculated, warnings | 31.35 |
| matches_analysis | matches_analysis | overall, per_season, ht_ft_matrix, comebacks, ht_lead_conversion, first_goal_timing, goalless | 9.73 |
| goals_analysis | goals_analysis | goals_distribution, goals_per_season, goal_share, btts, clean_sheets, scoring_intensity, first_goal_timing | 6.42 |
| teams_analysis | teams_analysis | teams, home_away, top_performers, consistent_teams, head_to_head, position_table | 31.48 |
| season_trends | season_trends | champions, title_race, points_thresholds, relegation_battle, league_trends, view_divergence | 3.96 |
| scoreline_analysis | scoreline_analysis | scoreline_frequency, scoreline_per_season, total_goal_histogram, extreme_scorelines, margin_distribution, margin_by_outcome, common_scorelines | 66.86 |
| relationships | relationships | n_matches, feature_count, correlation_matrix, form_vs_outcome, position_vs_outcome, rest_advantage, home_quality, feature_by_result | 14.36 |

## 5. Notable anomalies
- **1.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2025-2026 has 321 matches, expected 380
- **2.** `MATCH_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 63 matches, expected 380
- **3.** `TEAM_COUNT_UNEXPECTED` *(warning)* — Season 2026-2027 has 18 teams, expected 20
- **4.** `SEASON_STATE_NOT_COMPLETE` *(warning)* — Season 2026-2027 has data but state is 'in_progress'
- **5.** `GOALLESS_SHARE_OUTLIER` *(warning)* — Season 2026-2027 goalless share 4.8% vs overall 7.3% (deviation 2.5 pp)
- **6.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 home outcome share 50.8% vs overall 42.7%
- **7.** `OUTCOME_SHARE_OUTLIER` *(warning)* — Season 2026-2027 draw outcome share 19.0% vs overall 24.2%
- **8.** `HIGH_SCORING_MATCHES` *(warning)* — 4 match(es) with >= 8 total goals (extreme scorelines)
- **9.** `DUPLICATE_ROWS` *(warning)* — Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows)
- **10.** `FIRST_GOAL_NULL_INCONSISTENCY` *(warning)* — first_goal_time/first_goal_time_extra NULL semantics broken (fgt=2, fgte=2 rows)
- **11.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/classic rows=18 positions=1..18 teams=18
- **12.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/goals rows=18 positions=1..18 teams=18
- **13.** `STANDINGS_INCOMPLETE` *(warning)* — Standings 2026-2027/luck rows=18 positions=1..18 teams=18

## 6. Methodology
- Exploratory-data-analysis only: SQL + Python over the analytics database; relationship statistics use leakage-safe pre-match features and imply no predictive power.

---
*Aggregates `database_profile.json` and the module reports (modules 1-6). Run `python backend/scripts/compile_findings.py` after regenerating the module reports to refresh.*
