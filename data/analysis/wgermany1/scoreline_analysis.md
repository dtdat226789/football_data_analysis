# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:51:16+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Bundesliga Women (Germany)
- Scope: league `wgermany1`

## 1. Scoreline frequency
- Matches analysed: **217** across **2** seasons.
- Distinct scorelines seen: **36**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 22 | 10.1% |
| 2-1 | 20 | 9.2% |
| 1-2 | 15 | 6.9% |
| 2-0 | 13 | 6.0% |
| 0-1 | 13 | 6.0% |
| 3-0 | 12 | 5.5% |
| 1-4 | 9 | 4.1% |
| 1-0 | 9 | 4.1% |
| 0-2 | 8 | 3.7% |
| 0-0 | 7 | 3.2% |
| 3-1 | 7 | 3.2% |
| 3-2 | 7 | 3.2% |
| 2-3 | 7 | 3.2% |
| 4-1 | 7 | 3.2% |
| 0-3 | 6 | 2.8% |
| 1-3 | 6 | 2.8% |
| 4-0 | 5 | 2.3% |
| 2-2 | 5 | 2.3% |
| 4-2 | 4 | 1.8% |
| 5-1 | 4 | 1.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 18 | 9.9% |
| 2-1 | 17 | 9.3% |
| 0-1 | 12 | 6.6% |
| 2-0 | 10 | 5.5% |
| 3-0 | 10 | 5.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-2 | 5 | 14.3% |
| 1-1 | 4 | 11.4% |
| 2-0 | 3 | 8.6% |
| 1-0 | 3 | 8.6% |
| 2-1 | 3 | 8.6% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 7 | 3.2% |
| 1 | 22 | 10.1% |
| 2 | 43 | 19.8% |
| 3 | 53 | 24.4% |
| 4 | 27 | 12.4% |
| 5 | 34 | 15.7% |
| 6 | 21 | 9.7% |
| 7 | 5 | 2.3% |
| 8 | 4 | 1.8% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.5% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **10**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-08-22 | 2-8 | 10 |
| 2025-2026 | 2025-09-19 | 6-2 | 8 |
| 2025-2026 | 2025-10-04 | 0-8 | 8 |
| 2025-2026 | 2025-12-10 | 5-3 | 8 |
| 2025-2026 | 2026-04-27 | 6-2 | 8 |
| 2025-2026 | 2025-09-22 | 4-3 | 7 |
| 2025-2026 | 2025-12-13 | 1-6 | 7 |
| 2025-2026 | 2026-04-25 | 4-3 | 7 |
| 2025-2026 | 2026-05-10 | 7-0 | 7 |
| 2026-2027 | 2026-09-19 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **180** (draws: **37**)
- Average winning margin: **2.22**

| margin | matches | pct |
|---|---|---|
| 1 | 73 | 40.6% |
| 2 | 43 | 23.9% |
| 3+ | 64 | 35.6% |

## 6. Margin by outcome

### Home wins
- Matches: **98** | avg margin: **2.19** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 38 | 38.8% |
| 2 | 25 | 25.5% |
| 3+ | 35 | 35.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **82** | avg margin: **2.26** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 35 | 42.7% |
| 2 | 18 | 22.0% |
| 3+ | 29 | 35.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 98 | 2-1 | 20 | 20.4% |
| draw | 37 | 1-1 | 22 | 59.5% |
| away | 82 | 1-2 | 15 | 18.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\wgermany1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\wgermany1\charts\scoreline_analysis_total_goals.png)

