# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:41:55+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Liga Portugal 2 (Portugal)
- Scope: league `portugal2`

## 1. Scoreline frequency
- Matches analysed: **363** across **2** seasons.
- Distinct scorelines seen: **25**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 51 | 14.0% |
| 0-0 | 37 | 10.2% |
| 0-1 | 33 | 9.1% |
| 1-1 | 31 | 8.5% |
| 1-2 | 30 | 8.3% |
| 2-0 | 30 | 8.3% |
| 2-1 | 26 | 7.2% |
| 0-2 | 20 | 5.5% |
| 2-2 | 19 | 5.2% |
| 3-2 | 12 | 3.3% |
| 0-3 | 12 | 3.3% |
| 3-0 | 11 | 3.0% |
| 3-1 | 9 | 2.5% |
| 2-3 | 8 | 2.2% |
| 1-3 | 7 | 1.9% |
| 4-3 | 5 | 1.4% |
| 4-1 | 4 | 1.1% |
| 4-0 | 3 | 0.8% |
| 1-5 | 3 | 0.8% |
| 2-4 | 3 | 0.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 42 | 13.5% |
| 0-0 | 33 | 10.6% |
| 0-1 | 29 | 9.4% |
| 1-1 | 28 | 9.0% |
| 1-2 | 27 | 8.7% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 9 | 17.0% |
| 2-1 | 5 | 9.4% |
| 2-0 | 5 | 9.4% |
| 2-2 | 5 | 9.4% |
| 0-2 | 5 | 9.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 37 | 10.2% |
| 1 | 84 | 23.1% |
| 2 | 81 | 22.3% |
| 3 | 79 | 21.8% |
| 4 | 40 | 11.0% |
| 5 | 27 | 7.4% |
| 6 | 9 | 2.5% |
| 7 | 6 | 1.7% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **6**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-11-02 | 4-3 | 7 |
| 2025-2026 | 2026-01-11 | 3-4 | 7 |
| 2025-2026 | 2026-02-15 | 4-3 | 7 |
| 2025-2026 | 2026-03-15 | 4-3 | 7 |
| 2025-2026 | 2026-04-11 | 4-3 | 7 |
| 2025-2026 | 2026-04-18 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **275** (draws: **88**)
- Average winning margin: **1.56**

| margin | matches | pct |
|---|---|---|
| 1 | 166 | 60.4% |
| 2 | 71 | 25.8% |
| 3+ | 38 | 13.8% |

## 6. Margin by outcome

### Home wins
- Matches: **153** | avg margin: **1.52** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 94 | 61.4% |
| 2 | 41 | 26.8% |
| 3+ | 18 | 11.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **122** | avg margin: **1.61** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 72 | 59.0% |
| 2 | 30 | 24.6% |
| 3+ | 20 | 16.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 153 | 1-0 | 51 | 33.3% |
| draw | 88 | 0-0 | 37 | 42.0% |
| away | 122 | 0-1 | 33 | 27.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\portugal2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\portugal2\charts\scoreline_analysis_total_goals.png)

