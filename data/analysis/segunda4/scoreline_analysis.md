# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:46:24+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

## 1. Scoreline frequency
- Matches analysed: **350** across **2** seasons.
- Distinct scorelines seen: **24**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 60 | 17.1% |
| 1-1 | 50 | 14.3% |
| 2-1 | 40 | 11.4% |
| 0-0 | 31 | 8.9% |
| 1-2 | 27 | 7.7% |
| 0-1 | 27 | 7.7% |
| 2-0 | 22 | 6.3% |
| 3-2 | 13 | 3.7% |
| 3-1 | 13 | 3.7% |
| 0-2 | 11 | 3.1% |
| 3-0 | 11 | 3.1% |
| 1-3 | 10 | 2.9% |
| 2-2 | 10 | 2.9% |
| 0-3 | 5 | 1.4% |
| 4-0 | 4 | 1.1% |
| 2-3 | 3 | 0.9% |
| 4-2 | 3 | 0.9% |
| 2-4 | 2 | 0.6% |
| 5-0 | 2 | 0.6% |
| 4-1 | 2 | 0.6% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 59 | 18.3% |
| 1-1 | 47 | 14.6% |
| 2-1 | 38 | 11.8% |
| 0-0 | 28 | 8.7% |
| 1-2 | 24 | 7.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-1 | 4 | 14.8% |
| 0-0 | 3 | 11.1% |
| 1-1 | 3 | 11.1% |
| 1-2 | 3 | 11.1% |
| 2-1 | 2 | 7.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 31 | 8.9% |
| 1 | 87 | 24.9% |
| 2 | 83 | 23.7% |
| 3 | 83 | 23.7% |
| 4 | 37 | 10.6% |
| 5 | 21 | 6.0% |
| 6 | 7 | 2.0% |
| 7 | 1 | 0.3% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **1**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-04-26 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **258** (draws: **92**)
- Average winning margin: **1.47**

| margin | matches | pct |
|---|---|---|
| 1 | 171 | 66.3% |
| 2 | 61 | 23.6% |
| 3+ | 26 | 10.1% |

## 6. Margin by outcome

### Home wins
- Matches: **171** | avg margin: **1.51** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 113 | 66.1% |
| 2 | 38 | 22.2% |
| 3+ | 20 | 11.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **87** | avg margin: **1.4** | max margin: **3**
| margin | matches | pct |
|---|---|---|
| 1 | 58 | 66.7% |
| 2 | 23 | 26.4% |
| 3+ | 6 | 6.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 171 | 1-0 | 60 | 35.1% |
| draw | 92 | 1-1 | 50 | 54.3% |
| away | 87 | 1-2 | 27 | 31.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\segunda4\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\segunda4\charts\scoreline_analysis_total_goals.png)

