# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:43:48+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Saudi Professional League (Saudi Arabia)
- Scope: league `saudi1`

## 1. Scoreline frequency
- Matches analysed: **377** across **2** seasons.
- Distinct scorelines seen: **35**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 45 | 11.9% |
| 2-1 | 34 | 9.0% |
| 1-0 | 30 | 8.0% |
| 0-0 | 26 | 6.9% |
| 2-0 | 24 | 6.4% |
| 0-1 | 24 | 6.4% |
| 1-2 | 22 | 5.8% |
| 3-1 | 17 | 4.5% |
| 0-2 | 17 | 4.5% |
| 2-2 | 16 | 4.2% |
| 1-3 | 16 | 4.2% |
| 3-2 | 14 | 3.7% |
| 3-0 | 12 | 3.2% |
| 4-0 | 10 | 2.7% |
| 2-3 | 8 | 2.1% |
| 4-1 | 8 | 2.1% |
| 0-5 | 7 | 1.9% |
| 4-2 | 5 | 1.3% |
| 0-3 | 5 | 1.3% |
| 1-4 | 4 | 1.1% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 39 | 12.4% |
| 2-1 | 28 | 8.9% |
| 1-0 | 28 | 8.9% |
| 2-0 | 23 | 7.3% |
| 1-2 | 20 | 6.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-0 | 10 | 15.9% |
| 2-1 | 6 | 9.5% |
| 1-1 | 6 | 9.5% |
| 0-1 | 5 | 7.9% |
| 0-2 | 5 | 7.9% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 26 | 6.9% |
| 1 | 54 | 14.3% |
| 2 | 86 | 22.8% |
| 3 | 73 | 19.4% |
| 4 | 63 | 16.7% |
| 5 | 43 | 11.4% |
| 6 | 21 | 5.6% |
| 7 | 9 | 2.4% |
| 8 | 2 | 0.5% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **11**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-11-01 | 4-4 | 8 |
| 2025-2026 | 2026-02-27 | 3-5 | 8 |
| 2025-2026 | 2025-08-30 | 2-5 | 7 |
| 2025-2026 | 2025-10-19 | 6-1 | 7 |
| 2025-2026 | 2025-11-07 | 2-5 | 7 |
| 2025-2026 | 2026-01-08 | 3-4 | 7 |
| 2025-2026 | 2026-01-20 | 2-5 | 7 |
| 2025-2026 | 2026-02-13 | 2-5 | 7 |
| 2025-2026 | 2026-02-19 | 4-3 | 7 |
| 2025-2026 | 2026-04-03 | 5-2 | 7 |
| 2025-2026 | 2026-04-08 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **286** (draws: **91**)
- Average winning margin: **1.94**

| margin | matches | pct |
|---|---|---|
| 1 | 135 | 47.2% |
| 2 | 83 | 29.0% |
| 3+ | 68 | 23.8% |

## 6. Margin by outcome

### Home wins
- Matches: **163** | avg margin: **1.88** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 79 | 48.5% |
| 2 | 46 | 28.2% |
| 3+ | 38 | 23.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **123** | avg margin: **2.02** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 56 | 45.5% |
| 2 | 37 | 30.1% |
| 3+ | 30 | 24.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 163 | 2-1 | 34 | 20.9% |
| draw | 91 | 1-1 | 45 | 49.5% |
| away | 123 | 0-1 | 24 | 19.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\saudi1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\saudi1\charts\scoreline_analysis_total_goals.png)

