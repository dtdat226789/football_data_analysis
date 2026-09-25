# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:54:39+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: A-League (Australia)
- Scope: league `australia`

## 1. Scoreline frequency
- Matches analysed: **332** across **2** seasons.
- Distinct scorelines seen: **34**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 35 | 10.5% |
| 2-2 | 30 | 9.0% |
| 1-2 | 29 | 8.7% |
| 0-1 | 26 | 7.8% |
| 1-0 | 25 | 7.5% |
| 2-1 | 23 | 6.9% |
| 0-0 | 17 | 5.1% |
| 0-2 | 17 | 5.1% |
| 2-0 | 15 | 4.5% |
| 1-3 | 15 | 4.5% |
| 4-1 | 13 | 3.9% |
| 2-3 | 12 | 3.6% |
| 3-0 | 11 | 3.3% |
| 3-2 | 10 | 3.0% |
| 3-1 | 8 | 2.4% |
| 0-4 | 6 | 1.8% |
| 0-3 | 5 | 1.5% |
| 4-0 | 5 | 1.5% |
| 3-4 | 4 | 1.2% |
| 4-2 | 3 | 0.9% |

## 2. Scoreline frequency per season

### 2024-2025
| scoreline | count | pct |
|---|---|---|
| 2-2 | 16 | 9.5% |
| 1-1 | 15 | 8.9% |
| 1-2 | 13 | 7.7% |
| 1-0 | 13 | 7.7% |
| 0-1 | 11 | 6.5% |

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 20 | 12.3% |
| 1-2 | 16 | 9.8% |
| 2-1 | 15 | 9.2% |
| 0-1 | 15 | 9.2% |
| 2-2 | 14 | 8.6% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 17 | 5.1% |
| 1 | 51 | 15.4% |
| 2 | 67 | 20.2% |
| 3 | 68 | 20.5% |
| 4 | 64 | 19.3% |
| 5 | 40 | 12.0% |
| 6 | 11 | 3.3% |
| 7 | 7 | 2.1% |
| 8 | 5 | 1.5% |
| 9 | 2 | 0.6% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **14**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2024-2025 | 2025-03-14 | 4-5 | 9 |
| 2025-2026 | 2025-12-26 | 4-5 | 9 |
| 2024-2025 | 2024-11-30 | 4-4 | 8 |
| 2024-2025 | 2025-03-01 | 4-4 | 8 |
| 2024-2025 | 2025-03-16 | 2-6 | 8 |
| 2024-2025 | 2025-03-29 | 5-3 | 8 |
| 2025-2026 | 2026-01-24 | 6-2 | 8 |
| 2024-2025 | 2024-10-20 | 6-1 | 7 |
| 2024-2025 | 2024-11-02 | 3-4 | 7 |
| 2024-2025 | 2024-12-14 | 3-4 | 7 |
| 2024-2025 | 2025-01-10 | 3-4 | 7 |
| 2024-2025 | 2025-01-18 | 3-4 | 7 |
| 2024-2025 | 2025-02-22 | 6-1 | 7 |
| 2025-2026 | 2025-10-24 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **245** (draws: **87**)
- Average winning margin: **1.8**

| margin | matches | pct |
|---|---|---|
| 1 | 131 | 53.5% |
| 2 | 60 | 24.5% |
| 3+ | 54 | 22.0% |

## 6. Margin by outcome

### Home wins
- Matches: **121** | avg margin: **1.94** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 58 | 47.9% |
| 2 | 27 | 22.3% |
| 3+ | 36 | 29.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **124** | avg margin: **1.65** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 73 | 58.9% |
| 2 | 33 | 26.6% |
| 3+ | 18 | 14.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 121 | 1-0 | 25 | 20.7% |
| draw | 87 | 1-1 | 35 | 40.2% |
| away | 124 | 1-2 | 29 | 23.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\australia\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\australia\charts\scoreline_analysis_total_goals.png)

