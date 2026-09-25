# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:00:15+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Super League 2 (Greece)
- Scope: league `greece2`

## 1. Scoreline frequency
- Matches analysed: **289** across **2** seasons.
- Distinct scorelines seen: **25**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 46 | 15.9% |
| 1-1 | 35 | 12.1% |
| 0-1 | 31 | 10.7% |
| 2-0 | 25 | 8.7% |
| 0-0 | 23 | 8.0% |
| 1-2 | 20 | 6.9% |
| 2-1 | 17 | 5.9% |
| 3-0 | 16 | 5.5% |
| 0-2 | 15 | 5.2% |
| 2-2 | 9 | 3.1% |
| 3-1 | 9 | 3.1% |
| 0-3 | 7 | 2.4% |
| 1-3 | 6 | 2.1% |
| 2-3 | 4 | 1.4% |
| 4-1 | 4 | 1.4% |
| 4-0 | 3 | 1.0% |
| 1-4 | 3 | 1.0% |
| 5-1 | 3 | 1.0% |
| 2-4 | 2 | 0.7% |
| 5-0 | 2 | 0.7% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 39 | 14.7% |
| 1-1 | 32 | 12.1% |
| 0-1 | 31 | 11.7% |
| 2-0 | 23 | 8.7% |
| 0-0 | 21 | 7.9% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 7 | 29.2% |
| 2-1 | 4 | 16.7% |
| 1-1 | 3 | 12.5% |
| 0-0 | 2 | 8.3% |
| 2-0 | 2 | 8.3% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 23 | 8.0% |
| 1 | 77 | 26.6% |
| 2 | 75 | 26.0% |
| 3 | 60 | 20.8% |
| 4 | 29 | 10.0% |
| 5 | 15 | 5.2% |
| 6 | 7 | 2.4% |
| 7 | 3 | 1.0% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-11-15 | 1-6 | 7 |
| 2025-2026 | 2026-04-18 | 4-3 | 7 |
| 2025-2026 | 2026-04-26 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **222** (draws: **67**)
- Average winning margin: **1.73**

| margin | matches | pct |
|---|---|---|
| 1 | 122 | 55.0% |
| 2 | 57 | 25.7% |
| 3+ | 43 | 19.4% |

## 6. Margin by outcome

### Home wins
- Matches: **131** | avg margin: **1.84** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 67 | 51.1% |
| 2 | 34 | 26.0% |
| 3+ | 30 | 22.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **91** | avg margin: **1.58** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 55 | 60.4% |
| 2 | 23 | 25.3% |
| 3+ | 13 | 14.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 131 | 1-0 | 46 | 35.1% |
| draw | 67 | 1-1 | 35 | 52.2% |
| away | 91 | 0-1 | 31 | 34.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\greece2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\greece2\charts\scoreline_analysis_total_goals.png)

