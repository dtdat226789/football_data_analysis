# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:03:28+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: TOPLYGA (Lithuania)
- Scope: league `lithuania`

## 1. Scoreline frequency
- Matches analysed: **324** across **2** seasons.
- Distinct scorelines seen: **30**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 34 | 10.5% |
| 0-0 | 29 | 9.0% |
| 2-1 | 27 | 8.3% |
| 0-1 | 27 | 8.3% |
| 1-0 | 25 | 7.7% |
| 1-2 | 22 | 6.8% |
| 2-0 | 20 | 6.2% |
| 2-2 | 19 | 5.9% |
| 0-2 | 19 | 5.9% |
| 3-0 | 16 | 4.9% |
| 1-3 | 14 | 4.3% |
| 3-1 | 13 | 4.0% |
| 0-3 | 11 | 3.4% |
| 3-2 | 8 | 2.5% |
| 2-3 | 6 | 1.9% |
| 4-0 | 6 | 1.9% |
| 5-0 | 5 | 1.5% |
| 4-1 | 4 | 1.2% |
| 0-5 | 3 | 0.9% |
| 3-4 | 2 | 0.6% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 0-1 | 20 | 11.1% |
| 2-1 | 19 | 10.6% |
| 1-1 | 16 | 8.9% |
| 2-2 | 13 | 7.2% |
| 1-0 | 13 | 7.2% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 18 | 12.5% |
| 0-0 | 16 | 11.1% |
| 1-2 | 12 | 8.3% |
| 1-0 | 12 | 8.3% |
| 2-0 | 8 | 5.6% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 29 | 9.0% |
| 1 | 52 | 16.0% |
| 2 | 73 | 22.5% |
| 3 | 76 | 23.5% |
| 4 | 54 | 16.7% |
| 5 | 27 | 8.3% |
| 6 | 8 | 2.5% |
| 7 | 5 | 1.5% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **5**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-03-01 | 3-4 | 7 |
| 2025 | 2025-07-05 | 5-2 | 7 |
| 2025 | 2025-09-14 | 6-1 | 7 |
| 2026 | 2026-06-12 | 4-3 | 7 |
| 2026 | 2026-08-09 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **240** (draws: **84**)
- Average winning margin: **1.87**

| margin | matches | pct |
|---|---|---|
| 1 | 118 | 49.2% |
| 2 | 68 | 28.3% |
| 3+ | 54 | 22.5% |

## 6. Margin by outcome

### Home wins
- Matches: **130** | avg margin: **1.98** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 61 | 46.9% |
| 2 | 33 | 25.4% |
| 3+ | 36 | 27.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **110** | avg margin: **1.73** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 57 | 51.8% |
| 2 | 35 | 31.8% |
| 3+ | 18 | 16.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 130 | 2-1 | 27 | 20.8% |
| draw | 84 | 1-1 | 34 | 40.5% |
| away | 110 | 0-1 | 27 | 24.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\lithuania\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\lithuania\charts\scoreline_analysis_total_goals.png)

