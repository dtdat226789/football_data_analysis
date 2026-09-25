# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:55:40+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Serie B (Brazil)
- Scope: league `brazil2`

## 1. Scoreline frequency
- Matches analysed: **669** across **2** seasons.
- Distinct scorelines seen: **28**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 98 | 14.6% |
| 1-1 | 97 | 14.5% |
| 2-1 | 81 | 12.1% |
| 0-1 | 59 | 8.8% |
| 2-0 | 59 | 8.8% |
| 0-0 | 58 | 8.7% |
| 1-2 | 49 | 7.3% |
| 2-2 | 35 | 5.2% |
| 3-0 | 23 | 3.4% |
| 0-2 | 22 | 3.3% |
| 1-3 | 16 | 2.4% |
| 3-1 | 15 | 2.2% |
| 4-0 | 8 | 1.2% |
| 0-3 | 7 | 1.0% |
| 3-2 | 7 | 1.0% |
| 4-2 | 6 | 0.9% |
| 2-3 | 6 | 0.9% |
| 1-4 | 5 | 0.7% |
| 3-3 | 5 | 0.7% |
| 5-0 | 3 | 0.4% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-0 | 60 | 15.8% |
| 1-1 | 57 | 15.0% |
| 2-1 | 44 | 11.6% |
| 2-0 | 37 | 9.7% |
| 0-0 | 33 | 8.7% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 40 | 13.8% |
| 1-0 | 38 | 13.1% |
| 2-1 | 37 | 12.8% |
| 0-1 | 27 | 9.3% |
| 0-0 | 25 | 8.7% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 58 | 8.7% |
| 1 | 157 | 23.5% |
| 2 | 178 | 26.6% |
| 3 | 160 | 23.9% |
| 4 | 76 | 11.4% |
| 5 | 22 | 3.3% |
| 6 | 14 | 2.1% |
| 7 | 3 | 0.4% |
| 8 | 1 | 0.1% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **4**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026 | 2026-05-16 | 2-6 | 8 |
| 2025 | 2025-07-19 | 2-5 | 7 |
| 2026 | 2026-06-20 | 4-3 | 7 |
| 2026 | 2026-07-26 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **474** (draws: **195**)
- Average winning margin: **1.52**

| margin | matches | pct |
|---|---|---|
| 1 | 302 | 63.7% |
| 2 | 119 | 25.1% |
| 3+ | 53 | 11.2% |

## 6. Margin by outcome

### Home wins
- Matches: **304** | avg margin: **1.57** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 187 | 61.5% |
| 2 | 80 | 26.3% |
| 3+ | 37 | 12.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **170** | avg margin: **1.44** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 115 | 67.6% |
| 2 | 39 | 22.9% |
| 3+ | 16 | 9.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 304 | 1-0 | 98 | 32.2% |
| draw | 195 | 1-1 | 97 | 49.7% |
| away | 170 | 0-1 | 59 | 34.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\brazil2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\brazil2\charts\scoreline_analysis_total_goals.png)

