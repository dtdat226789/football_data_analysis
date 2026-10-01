# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:05:51+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Championship (Scotland)
- Scope: league `scot-champ`

## 1. Scoreline frequency
- Matches analysed: **231** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 33 | 14.3% |
| 0-0 | 29 | 12.6% |
| 1-0 | 22 | 9.5% |
| 0-1 | 20 | 8.7% |
| 2-1 | 20 | 8.7% |
| 2-0 | 18 | 7.8% |
| 0-2 | 14 | 6.1% |
| 1-2 | 13 | 5.6% |
| 2-2 | 11 | 4.8% |
| 3-0 | 7 | 3.0% |
| 3-2 | 7 | 3.0% |
| 3-1 | 7 | 3.0% |
| 1-3 | 4 | 1.7% |
| 0-3 | 4 | 1.7% |
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
| 2-0 | 8 | 19.5% |
| 1-0 | 6 | 14.6% |
| 1-1 | 5 | 12.2% |
| 0-0 | 4 | 9.8% |
| 0-1 | 4 | 9.8% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 29 | 12.6% |
| 1 | 42 | 18.2% |
| 2 | 65 | 28.1% |
| 3 | 44 | 19.0% |
| 4 | 28 | 12.1% |
| 5 | 15 | 6.5% |
| 6 | 7 | 3.0% |
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
- Decided matches: **157** (draws: **74**)
- Average winning margin: **1.72**

| margin | matches | pct |
|---|---|---|
| 1 | 85 | 54.1% |
| 2 | 47 | 29.9% |
| 3+ | 25 | 15.9% |

## 6. Margin by outcome

### Home wins
- Matches: **93** | avg margin: **1.75** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 50 | 53.8% |
| 2 | 27 | 29.0% |
| 3+ | 16 | 17.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **64** | avg margin: **1.67** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 35 | 54.7% |
| 2 | 20 | 31.2% |
| 3+ | 9 | 14.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 93 | 1-0 | 22 | 23.7% |
| draw | 74 | 1-1 | 33 | 44.6% |
| away | 64 | 0-1 | 20 | 31.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\scot-champ\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\scot-champ\charts\scoreline_analysis_total_goals.png)

