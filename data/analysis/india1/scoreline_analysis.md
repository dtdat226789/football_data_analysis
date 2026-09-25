# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:01:17+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: ISL (India)
- Scope: league `india1`

## 1. Scoreline frequency
- Matches analysed: **247** across **2** seasons.
- Distinct scorelines seen: **29**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 32 | 13.0% |
| 1-0 | 24 | 9.7% |
| 0-0 | 21 | 8.5% |
| 1-2 | 19 | 7.7% |
| 2-1 | 17 | 6.9% |
| 2-0 | 16 | 6.5% |
| 0-2 | 15 | 6.1% |
| 3-0 | 14 | 5.7% |
| 2-2 | 12 | 4.9% |
| 0-1 | 12 | 4.9% |
| 3-2 | 10 | 4.0% |
| 1-3 | 10 | 4.0% |
| 2-3 | 7 | 2.8% |
| 0-3 | 7 | 2.8% |
| 3-1 | 6 | 2.4% |
| 4-2 | 4 | 1.6% |
| 4-1 | 4 | 1.6% |
| 0-4 | 3 | 1.2% |
| 3-3 | 2 | 0.8% |
| 2-4 | 2 | 0.8% |

## 2. Scoreline frequency per season

### 2024-2025
| scoreline | count | pct |
|---|---|---|
| 1-1 | 16 | 10.3% |
| 1-0 | 15 | 9.6% |
| 2-1 | 12 | 7.7% |
| 3-0 | 11 | 7.1% |
| 0-0 | 11 | 7.1% |

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 16 | 17.6% |
| 0-0 | 10 | 11.0% |
| 1-2 | 10 | 11.0% |
| 1-0 | 9 | 9.9% |
| 2-0 | 8 | 8.8% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 21 | 8.5% |
| 1 | 36 | 14.6% |
| 2 | 63 | 25.5% |
| 3 | 57 | 23.1% |
| 4 | 32 | 13.0% |
| 5 | 23 | 9.3% |
| 6 | 12 | 4.9% |
| 7 | 3 | 1.2% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2024-2025 | 2024-12-23 | 2-5 | 7 |
| 2024-2025 | 2025-03-09 | 5-2 | 7 |
| 2025-2026 | 2026-03-23 | 7-0 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **180** (draws: **67**)
- Average winning margin: **1.81**

| margin | matches | pct |
|---|---|---|
| 1 | 89 | 49.4% |
| 2 | 53 | 29.4% |
| 3+ | 38 | 21.1% |

## 6. Margin by outcome

### Home wins
- Matches: **101** | avg margin: **1.82** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 51 | 50.5% |
| 2 | 26 | 25.7% |
| 3+ | 24 | 23.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **79** | avg margin: **1.78** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 38 | 48.1% |
| 2 | 27 | 34.2% |
| 3+ | 14 | 17.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 101 | 1-0 | 24 | 23.8% |
| draw | 67 | 1-1 | 32 | 47.8% |
| away | 79 | 1-2 | 19 | 24.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\india1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\india1\charts\scoreline_analysis_total_goals.png)

