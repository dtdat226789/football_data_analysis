# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:55:41+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Premier Division (Ireland)
- Scope: league `ireland1`

## 1. Scoreline frequency
- Matches analysed: **339** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 47 | 13.9% |
| 1-0 | 35 | 10.3% |
| 2-1 | 33 | 9.7% |
| 0-0 | 30 | 8.8% |
| 1-2 | 30 | 8.8% |
| 0-1 | 26 | 7.7% |
| 2-0 | 26 | 7.7% |
| 2-2 | 24 | 7.1% |
| 2-3 | 12 | 3.5% |
| 0-2 | 11 | 3.2% |
| 3-0 | 10 | 2.9% |
| 3-2 | 8 | 2.4% |
| 3-1 | 7 | 2.1% |
| 1-3 | 7 | 2.1% |
| 4-1 | 7 | 2.1% |
| 4-0 | 4 | 1.2% |
| 0-4 | 3 | 0.9% |
| 2-4 | 3 | 0.9% |
| 3-3 | 3 | 0.9% |
| 4-3 | 2 | 0.6% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-1 | 25 | 13.9% |
| 1-0 | 22 | 12.2% |
| 2-1 | 20 | 11.1% |
| 0-1 | 17 | 9.4% |
| 1-2 | 17 | 9.4% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 22 | 13.8% |
| 0-0 | 15 | 9.4% |
| 2-1 | 13 | 8.2% |
| 2-0 | 13 | 8.2% |
| 1-2 | 13 | 8.2% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 30 | 8.8% |
| 1 | 61 | 18.0% |
| 2 | 84 | 24.8% |
| 3 | 75 | 22.1% |
| 4 | 45 | 13.3% |
| 5 | 30 | 8.8% |
| 6 | 8 | 2.4% |
| 7 | 4 | 1.2% |
| 8 | 1 | 0.3% |
| 9 | 1 | 0.3% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **6**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-07-04 | 7-2 | 9 |
| 2026 | 2026-08-21 | 5-3 | 8 |
| 2025 | 2025-02-28 | 4-3 | 7 |
| 2025 | 2025-09-12 | 3-4 | 7 |
| 2026 | 2026-03-16 | 4-3 | 7 |
| 2026 | 2026-04-24 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **235** (draws: **104**)
- Average winning margin: **1.54**

| margin | matches | pct |
|---|---|---|
| 1 | 148 | 63.0% |
| 2 | 57 | 24.3% |
| 3+ | 30 | 12.8% |

## 6. Margin by outcome

### Home wins
- Matches: **137** | avg margin: **1.66** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 78 | 56.9% |
| 2 | 36 | 26.3% |
| 3+ | 23 | 16.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **98** | avg margin: **1.39** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 70 | 71.4% |
| 2 | 21 | 21.4% |
| 3+ | 7 | 7.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 137 | 1-0 | 35 | 25.5% |
| draw | 104 | 1-1 | 47 | 45.2% |
| away | 98 | 1-2 | 30 | 30.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\ireland1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\ireland1\charts\scoreline_analysis_total_goals.png)

