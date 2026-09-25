# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:46:04+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Segunda RFEF - Group 3 (Spain)
- Scope: league `segunda3`

## 1. Scoreline frequency
- Matches analysed: **337** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 57 | 16.9% |
| 1-1 | 48 | 14.2% |
| 0-0 | 35 | 10.4% |
| 2-1 | 28 | 8.3% |
| 1-2 | 27 | 8.0% |
| 0-1 | 23 | 6.8% |
| 2-0 | 20 | 5.9% |
| 2-2 | 19 | 5.6% |
| 3-1 | 11 | 3.3% |
| 3-0 | 10 | 3.0% |
| 0-2 | 9 | 2.7% |
| 3-2 | 8 | 2.4% |
| 1-3 | 6 | 1.8% |
| 4-1 | 5 | 1.5% |
| 4-0 | 4 | 1.2% |
| 4-2 | 4 | 1.2% |
| 5-1 | 4 | 1.2% |
| 2-4 | 3 | 0.9% |
| 3-3 | 3 | 0.9% |
| 1-4 | 3 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 49 | 16.0% |
| 1-1 | 43 | 14.1% |
| 0-0 | 33 | 10.8% |
| 2-1 | 26 | 8.5% |
| 0-1 | 21 | 6.9% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 8 | 25.8% |
| 1-2 | 6 | 19.4% |
| 1-1 | 5 | 16.1% |
| 2-1 | 2 | 6.5% |
| 2-2 | 2 | 6.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 35 | 10.4% |
| 1 | 80 | 23.7% |
| 2 | 77 | 22.8% |
| 3 | 67 | 19.9% |
| 4 | 41 | 12.2% |
| 5 | 19 | 5.6% |
| 6 | 15 | 4.5% |
| 7 | 0 | 0.0% |
| 8 | 2 | 0.6% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.3% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-12-14 | 7-3 | 10 |
| 2025-2026 | 2025-12-21 | 4-4 | 8 |
| 2025-2026 | 2026-04-05 | 5-3 | 8 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **231** (draws: **106**)
- Average winning margin: **1.55**

| margin | matches | pct |
|---|---|---|
| 1 | 146 | 63.2% |
| 2 | 54 | 23.4% |
| 3+ | 31 | 13.4% |

## 6. Margin by outcome

### Home wins
- Matches: **153** | avg margin: **1.61** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 93 | 60.8% |
| 2 | 36 | 23.5% |
| 3+ | 24 | 15.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **78** | avg margin: **1.44** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 53 | 67.9% |
| 2 | 18 | 23.1% |
| 3+ | 7 | 9.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 153 | 1-0 | 57 | 37.3% |
| draw | 106 | 1-1 | 48 | 45.3% |
| away | 78 | 1-2 | 27 | 34.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\segunda3\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\segunda3\charts\scoreline_analysis_total_goals.png)

