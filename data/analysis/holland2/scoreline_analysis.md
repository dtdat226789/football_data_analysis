# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:53:13+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Eerste Divisie (Netherlands)
- Scope: league `holland2`

## 1. Scoreline frequency
- Matches analysed: **474** across **2** seasons.
- Distinct scorelines seen: **35**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 43 | 9.1% |
| 2-1 | 41 | 8.6% |
| 1-2 | 38 | 8.0% |
| 1-0 | 36 | 7.6% |
| 2-2 | 31 | 6.5% |
| 0-1 | 30 | 6.3% |
| 2-0 | 29 | 6.1% |
| 3-1 | 23 | 4.9% |
| 3-2 | 22 | 4.6% |
| 1-3 | 20 | 4.2% |
| 2-3 | 17 | 3.6% |
| 0-0 | 16 | 3.4% |
| 0-2 | 15 | 3.2% |
| 4-0 | 14 | 3.0% |
| 3-0 | 12 | 2.5% |
| 0-3 | 11 | 2.3% |
| 4-2 | 9 | 1.9% |
| 1-4 | 8 | 1.7% |
| 2-4 | 8 | 1.7% |
| 3-3 | 7 | 1.5% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 36 | 9.2% |
| 1-2 | 34 | 8.7% |
| 2-1 | 32 | 8.2% |
| 1-0 | 29 | 7.4% |
| 2-2 | 28 | 7.1% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-1 | 9 | 11.0% |
| 1-1 | 7 | 8.5% |
| 1-0 | 7 | 8.5% |
| 3-2 | 7 | 8.5% |
| 3-1 | 7 | 8.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 16 | 3.4% |
| 1 | 66 | 13.9% |
| 2 | 87 | 18.4% |
| 3 | 102 | 21.5% |
| 4 | 92 | 19.4% |
| 5 | 59 | 12.4% |
| 6 | 30 | 6.3% |
| 7 | 17 | 3.6% |
| 8 | 3 | 0.6% |
| 9 | 1 | 0.2% |
| 10+ | 1 | 0.2% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **22**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-08-17 | 4-6 | 10 |
| 2026-2027 | 2026-09-05 | 3-6 | 9 |
| 2025-2026 | 2025-09-26 | 5-3 | 8 |
| 2025-2026 | 2026-01-19 | 5-3 | 8 |
| 2026-2027 | 2026-09-04 | 5-3 | 8 |
| 2025-2026 | 2025-08-24 | 5-2 | 7 |
| 2025-2026 | 2025-08-25 | 4-3 | 7 |
| 2025-2026 | 2025-09-19 | 3-4 | 7 |
| 2025-2026 | 2025-11-02 | 3-4 | 7 |
| 2025-2026 | 2025-11-21 | 5-2 | 7 |
| 2025-2026 | 2025-12-12 | 3-4 | 7 |
| 2025-2026 | 2025-12-12 | 3-4 | 7 |
| 2025-2026 | 2026-01-26 | 3-4 | 7 |
| 2025-2026 | 2026-03-20 | 3-4 | 7 |
| 2025-2026 | 2026-04-06 | 6-1 | 7 |
| 2026-2027 | 2026-08-07 | 3-4 | 7 |
| 2026-2027 | 2026-08-17 | 2-5 | 7 |
| 2026-2027 | 2026-08-21 | 5-2 | 7 |
| 2026-2027 | 2026-08-24 | 1-6 | 7 |
| 2026-2027 | 2026-08-28 | 6-1 | 7 |
| 2026-2027 | 2026-09-14 | 6-1 | 7 |
| 2026-2027 | 2026-09-18 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **377** (draws: **97**)
- Average winning margin: **1.83**

| margin | matches | pct |
|---|---|---|
| 1 | 192 | 50.9% |
| 2 | 108 | 28.6% |
| 3+ | 77 | 20.4% |

## 6. Margin by outcome

### Home wins
- Matches: **214** | avg margin: **1.96** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 100 | 46.7% |
| 2 | 64 | 29.9% |
| 3+ | 50 | 23.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **163** | avg margin: **1.65** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 92 | 56.4% |
| 2 | 44 | 27.0% |
| 3+ | 27 | 16.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 214 | 2-1 | 41 | 19.2% |
| draw | 97 | 1-1 | 43 | 44.3% |
| away | 163 | 1-2 | 38 | 23.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\holland2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\holland2\charts\scoreline_analysis_total_goals.png)

