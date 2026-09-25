# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:44:22+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Championship (Scotland)
- Scope: league `scot-champ`

## 1. Scoreline frequency
- Matches analysed: **227** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 33 | 14.5% |
| 0-0 | 29 | 12.8% |
| 1-0 | 22 | 9.7% |
| 0-1 | 19 | 8.4% |
| 2-1 | 19 | 8.4% |
| 2-0 | 17 | 7.5% |
| 1-2 | 13 | 5.7% |
| 0-2 | 13 | 5.7% |
| 2-2 | 11 | 4.8% |
| 3-0 | 7 | 3.1% |
| 3-2 | 7 | 3.1% |
| 3-1 | 7 | 3.1% |
| 1-3 | 4 | 1.8% |
| 0-3 | 4 | 1.8% |
| 0-4 | 3 | 1.3% |
| 4-0 | 3 | 1.3% |
| 4-2 | 2 | 0.9% |
| 4-1 | 2 | 0.9% |
| 5-0 | 2 | 0.9% |
| 2-4 | 2 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 28 | 14.7% |
| 0-0 | 25 | 13.2% |
| 2-1 | 17 | 8.9% |
| 0-1 | 16 | 8.4% |
| 1-0 | 16 | 8.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-0 | 7 | 18.9% |
| 1-0 | 6 | 16.2% |
| 1-1 | 5 | 13.5% |
| 0-0 | 4 | 10.8% |
| 0-1 | 3 | 8.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 29 | 12.8% |
| 1 | 41 | 18.1% |
| 2 | 63 | 27.8% |
| 3 | 43 | 18.9% |
| 4 | 28 | 12.3% |
| 5 | 15 | 6.6% |
| 6 | 7 | 3.1% |
| 7 | 1 | 0.4% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **1**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-11-15 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **153** (draws: **74**)
- Average winning margin: **1.73**

| margin | matches | pct |
|---|---|---|
| 1 | 83 | 54.2% |
| 2 | 45 | 29.4% |
| 3+ | 25 | 16.3% |

## 6. Margin by outcome

### Home wins
- Matches: **91** | avg margin: **1.76** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 49 | 53.8% |
| 2 | 26 | 28.6% |
| 3+ | 16 | 17.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **62** | avg margin: **1.68** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 34 | 54.8% |
| 2 | 19 | 30.6% |
| 3+ | 9 | 14.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 91 | 1-0 | 22 | 24.2% |
| draw | 74 | 1-1 | 33 | 44.6% |
| away | 62 | 0-1 | 19 | 30.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\scot-champ\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\scot-champ\charts\scoreline_analysis_total_goals.png)

