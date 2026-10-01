# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:04:36+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

## 1. Scoreline frequency
- Matches analysed: **429** across **2** seasons.
- Distinct scorelines seen: **28**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 58 | 13.5% |
| 0-0 | 50 | 11.7% |
| 1-1 | 48 | 11.2% |
| 2-0 | 43 | 10.0% |
| 0-1 | 39 | 9.1% |
| 2-1 | 37 | 8.6% |
| 2-2 | 25 | 5.8% |
| 1-2 | 24 | 5.6% |
| 0-2 | 17 | 4.0% |
| 3-0 | 17 | 4.0% |
| 3-1 | 14 | 3.3% |
| 3-2 | 9 | 2.1% |
| 1-3 | 9 | 2.1% |
| 0-3 | 7 | 1.6% |
| 4-0 | 6 | 1.4% |
| 2-3 | 5 | 1.2% |
| 1-4 | 5 | 1.2% |
| 3-3 | 3 | 0.7% |
| 4-1 | 3 | 0.7% |
| 4-2 | 2 | 0.5% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 52 | 13.7% |
| 0-0 | 46 | 12.1% |
| 1-1 | 43 | 11.3% |
| 0-1 | 37 | 9.7% |
| 2-0 | 37 | 9.7% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 6 | 12.2% |
| 1-2 | 6 | 12.2% |
| 2-0 | 6 | 12.2% |
| 1-1 | 5 | 10.2% |
| 2-2 | 4 | 8.2% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 50 | 11.7% |
| 1 | 97 | 22.6% |
| 2 | 108 | 25.2% |
| 3 | 85 | 19.8% |
| 4 | 54 | 12.6% |
| 5 | 23 | 5.4% |
| 6 | 7 | 1.6% |
| 7 | 3 | 0.7% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **5**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-04-10 | 5-4 | 9 |
| 2025-2026 | 2026-05-16 | 6-2 | 8 |
| 2025-2026 | 2026-03-14 | 5-2 | 7 |
| 2025-2026 | 2026-05-08 | 4-3 | 7 |
| 2026-2027 | 2026-09-13 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **303** (draws: **126**)
- Average winning margin: **1.59**

| margin | matches | pct |
|---|---|---|
| 1 | 175 | 57.8% |
| 2 | 86 | 28.4% |
| 3+ | 42 | 13.9% |

## 6. Margin by outcome

### Home wins
- Matches: **194** | avg margin: **1.65** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 106 | 54.6% |
| 2 | 59 | 30.4% |
| 3+ | 29 | 14.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **109** | avg margin: **1.5** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 69 | 63.3% |
| 2 | 27 | 24.8% |
| 3+ | 13 | 11.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 194 | 1-0 | 58 | 29.9% |
| draw | 126 | 0-0 | 50 | 39.7% |
| away | 109 | 0-1 | 39 | 35.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\primera2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\primera2\charts\scoreline_analysis_total_goals.png)

