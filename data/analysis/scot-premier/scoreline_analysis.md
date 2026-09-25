# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:44:38+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Premiership (Scotland)
- Scope: league `scot-premier`

## 1. Scoreline frequency
- Matches analysed: **276** across **2** seasons.
- Distinct scorelines seen: **29**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 31 | 11.2% |
| 1-0 | 29 | 10.5% |
| 2-0 | 24 | 8.7% |
| 1-2 | 23 | 8.3% |
| 0-0 | 19 | 6.9% |
| 2-1 | 19 | 6.9% |
| 2-2 | 18 | 6.5% |
| 0-1 | 17 | 6.2% |
| 3-1 | 13 | 4.7% |
| 3-0 | 13 | 4.7% |
| 0-2 | 12 | 4.3% |
| 4-0 | 8 | 2.9% |
| 0-3 | 8 | 2.9% |
| 2-3 | 7 | 2.5% |
| 1-3 | 7 | 2.5% |
| 3-2 | 6 | 2.2% |
| 3-3 | 5 | 1.8% |
| 4-1 | 2 | 0.7% |
| 5-1 | 2 | 0.7% |
| 4-3 | 2 | 0.7% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 25 | 10.7% |
| 1-0 | 25 | 10.7% |
| 2-0 | 23 | 9.8% |
| 2-2 | 18 | 7.7% |
| 1-2 | 18 | 7.7% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-1 | 7 | 16.7% |
| 1-1 | 6 | 14.3% |
| 1-2 | 5 | 11.9% |
| 0-1 | 5 | 11.9% |
| 1-0 | 4 | 9.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 19 | 6.9% |
| 1 | 46 | 16.7% |
| 2 | 67 | 24.3% |
| 3 | 63 | 22.8% |
| 4 | 48 | 17.4% |
| 5 | 17 | 6.2% |
| 6 | 11 | 4.0% |
| 7 | 3 | 1.1% |
| 8 | 1 | 0.4% |
| 9 | 1 | 0.4% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **5**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-04-12 | 3-6 | 9 |
| 2025-2026 | 2026-01-24 | 6-2 | 8 |
| 2025-2026 | 2026-02-11 | 4-3 | 7 |
| 2025-2026 | 2026-05-16 | 2-5 | 7 |
| 2026-2027 | 2026-08-02 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **203** (draws: **73**)
- Average winning margin: **1.77**

| margin | matches | pct |
|---|---|---|
| 1 | 103 | 50.7% |
| 2 | 59 | 29.1% |
| 3+ | 41 | 20.2% |

## 6. Margin by outcome

### Home wins
- Matches: **121** | avg margin: **1.84** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 56 | 46.3% |
| 2 | 39 | 32.2% |
| 3+ | 26 | 21.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **82** | avg margin: **1.67** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 47 | 57.3% |
| 2 | 20 | 24.4% |
| 3+ | 15 | 18.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 121 | 1-0 | 29 | 24.0% |
| draw | 73 | 1-1 | 31 | 42.5% |
| away | 82 | 1-2 | 23 | 28.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\scot-premier\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\scot-premier\charts\scoreline_analysis_total_goals.png)

