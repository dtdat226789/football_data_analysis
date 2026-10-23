# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:05:37+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Division 1 (Saudi Arabia)
- Scope: league `saudi2`

## 1. Scoreline frequency
- Matches analysed: **362** across **2** seasons.
- Distinct scorelines seen: **32**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 45 | 12.4% |
| 2-1 | 36 | 9.9% |
| 1-2 | 32 | 8.8% |
| 0-0 | 27 | 7.5% |
| 0-1 | 27 | 7.5% |
| 1-0 | 24 | 6.6% |
| 2-2 | 22 | 6.1% |
| 2-0 | 17 | 4.7% |
| 1-3 | 15 | 4.1% |
| 3-0 | 15 | 4.1% |
| 3-1 | 15 | 4.1% |
| 0-2 | 15 | 4.1% |
| 4-1 | 11 | 3.0% |
| 2-3 | 10 | 2.8% |
| 0-3 | 7 | 1.9% |
| 0-4 | 6 | 1.7% |
| 5-1 | 6 | 1.7% |
| 4-0 | 6 | 1.7% |
| 1-4 | 5 | 1.4% |
| 4-2 | 5 | 1.4% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 36 | 11.7% |
| 2-1 | 34 | 11.0% |
| 1-2 | 31 | 10.0% |
| 0-1 | 21 | 6.8% |
| 1-0 | 20 | 6.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-0 | 11 | 20.8% |
| 1-1 | 9 | 17.0% |
| 0-1 | 6 | 11.3% |
| 1-0 | 4 | 7.5% |
| 2-2 | 4 | 7.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 27 | 7.5% |
| 1 | 51 | 14.1% |
| 2 | 77 | 21.3% |
| 3 | 90 | 24.9% |
| 4 | 64 | 17.7% |
| 5 | 32 | 8.8% |
| 6 | 13 | 3.6% |
| 7 | 5 | 1.4% |
| 8 | 2 | 0.6% |
| 9 | 1 | 0.3% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **8**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-01-22 | 6-3 | 9 |
| 2025-2026 | 2025-09-12 | 4-4 | 8 |
| 2025-2026 | 2026-01-01 | 5-3 | 8 |
| 2025-2026 | 2025-12-31 | 5-2 | 7 |
| 2025-2026 | 2026-02-04 | 4-3 | 7 |
| 2025-2026 | 2026-03-02 | 1-6 | 7 |
| 2025-2026 | 2026-05-01 | 4-3 | 7 |
| 2026-2027 | 2026-08-26 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **266** (draws: **96**)
- Average winning margin: **1.83**

| margin | matches | pct |
|---|---|---|
| 1 | 135 | 50.8% |
| 2 | 68 | 25.6% |
| 3+ | 63 | 23.7% |

## 6. Margin by outcome

### Home wins
- Matches: **144** | avg margin: **1.93** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 65 | 45.1% |
| 2 | 38 | 26.4% |
| 3+ | 41 | 28.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **122** | avg margin: **1.71** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 70 | 57.4% |
| 2 | 30 | 24.6% |
| 3+ | 22 | 18.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 144 | 2-1 | 36 | 25.0% |
| draw | 96 | 1-1 | 45 | 46.9% |
| away | 122 | 1-2 | 32 | 26.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\saudi2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\saudi2\charts\scoreline_analysis_total_goals.png)

