# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:45:46+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Segunda RFEF - Group 2 (Spain)
- Scope: league `segunda2`

## 1. Scoreline frequency
- Matches analysed: **333** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 49 | 14.7% |
| 1-0 | 32 | 9.6% |
| 0-1 | 31 | 9.3% |
| 0-0 | 31 | 9.3% |
| 2-0 | 26 | 7.8% |
| 1-2 | 26 | 7.8% |
| 2-1 | 21 | 6.3% |
| 3-1 | 17 | 5.1% |
| 2-2 | 14 | 4.2% |
| 0-2 | 11 | 3.3% |
| 3-2 | 11 | 3.3% |
| 1-3 | 11 | 3.3% |
| 3-0 | 9 | 2.7% |
| 4-0 | 9 | 2.7% |
| 4-1 | 7 | 2.1% |
| 2-3 | 4 | 1.2% |
| 0-3 | 4 | 1.2% |
| 0-4 | 4 | 1.2% |
| 5-1 | 3 | 0.9% |
| 5-0 | 3 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 47 | 15.4% |
| 1-0 | 30 | 9.8% |
| 0-0 | 28 | 9.2% |
| 0-1 | 27 | 8.8% |
| 2-0 | 24 | 7.8% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-1 | 4 | 14.8% |
| 1-2 | 3 | 11.1% |
| 0-0 | 3 | 11.1% |
| 2-2 | 2 | 7.4% |
| 1-1 | 2 | 7.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 31 | 9.3% |
| 1 | 63 | 18.9% |
| 2 | 86 | 25.8% |
| 3 | 60 | 18.0% |
| 4 | 55 | 16.5% |
| 5 | 27 | 8.1% |
| 6 | 8 | 2.4% |
| 7 | 2 | 0.6% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.3% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-03-29 | 6-4 | 10 |
| 2025-2026 | 2025-09-14 | 4-3 | 7 |
| 2026-2027 | 2026-09-06 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **237** (draws: **96**)
- Average winning margin: **1.76**

| margin | matches | pct |
|---|---|---|
| 1 | 127 | 53.6% |
| 2 | 67 | 28.3% |
| 3+ | 43 | 18.1% |

## 6. Margin by outcome

### Home wins
- Matches: **142** | avg margin: **1.91** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 66 | 46.5% |
| 2 | 44 | 31.0% |
| 3+ | 32 | 22.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **95** | avg margin: **1.53** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 61 | 64.2% |
| 2 | 23 | 24.2% |
| 3+ | 11 | 11.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 142 | 1-0 | 32 | 22.5% |
| draw | 96 | 1-1 | 49 | 51.0% |
| away | 95 | 0-1 | 31 | 32.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\segunda2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\segunda2\charts\scoreline_analysis_total_goals.png)

