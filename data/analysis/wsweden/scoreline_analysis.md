# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:24:38+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Allsvenskan Women (Sweden)
- Scope: league `wsweden`

## 1. Scoreline frequency
- Matches analysed: **322** across **2** seasons.
- Distinct scorelines seen: **34**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 29 | 9.0% |
| 2-1 | 29 | 9.0% |
| 1-2 | 27 | 8.4% |
| 1-1 | 25 | 7.8% |
| 0-1 | 25 | 7.8% |
| 2-0 | 21 | 6.5% |
| 3-0 | 18 | 5.6% |
| 2-2 | 15 | 4.7% |
| 0-3 | 12 | 3.7% |
| 0-2 | 11 | 3.4% |
| 3-1 | 10 | 3.1% |
| 2-3 | 9 | 2.8% |
| 1-4 | 9 | 2.8% |
| 3-2 | 9 | 2.8% |
| 0-4 | 8 | 2.5% |
| 0-0 | 8 | 2.5% |
| 4-1 | 7 | 2.2% |
| 4-0 | 7 | 2.2% |
| 0-5 | 6 | 1.9% |
| 0-6 | 5 | 1.6% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 2-1 | 19 | 10.4% |
| 1-2 | 17 | 9.3% |
| 1-0 | 16 | 8.8% |
| 2-0 | 13 | 7.1% |
| 1-1 | 10 | 5.5% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 15 | 10.7% |
| 0-1 | 15 | 10.7% |
| 1-0 | 13 | 9.3% |
| 3-0 | 12 | 8.6% |
| 2-1 | 10 | 7.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 8 | 2.5% |
| 1 | 54 | 16.8% |
| 2 | 57 | 17.7% |
| 3 | 86 | 26.7% |
| 4 | 43 | 13.4% |
| 5 | 43 | 13.4% |
| 6 | 21 | 6.5% |
| 7 | 7 | 2.2% |
| 8 | 2 | 0.6% |
| 9 | 1 | 0.3% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **10**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-10-11 | 6-3 | 9 |
| 2025 | 2025-11-16 | 7-1 | 8 |
| 2026 | 2026-08-08 | 8-0 | 8 |
| 2025 | 2025-05-11 | 6-1 | 7 |
| 2025 | 2025-05-16 | 6-1 | 7 |
| 2025 | 2025-08-08 | 7-0 | 7 |
| 2025 | 2025-08-23 | 2-5 | 7 |
| 2025 | 2025-09-27 | 2-5 | 7 |
| 2025 | 2025-09-28 | 2-5 | 7 |
| 2025 | 2025-09-28 | 0-7 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **270** (draws: **52**)
- Average winning margin: **2.18**

| margin | matches | pct |
|---|---|---|
| 1 | 128 | 47.4% |
| 2 | 49 | 18.1% |
| 3+ | 93 | 34.4% |

## 6. Margin by outcome

### Home wins
- Matches: **149** | avg margin: **2.18** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 67 | 45.0% |
| 2 | 33 | 22.1% |
| 3+ | 49 | 32.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **121** | avg margin: **2.18** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 61 | 50.4% |
| 2 | 16 | 13.2% |
| 3+ | 44 | 36.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 149 | 1-0 | 29 | 19.5% |
| draw | 52 | 1-1 | 25 | 48.1% |
| away | 121 | 1-2 | 27 | 22.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\wsweden\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\wsweden\charts\scoreline_analysis_total_goals.png)

