# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:02:32+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: J1 League (Japan)
- Scope: league `japan1`

## 1. Scoreline frequency
- Matches analysed: **241** across **2** seasons.
- Distinct scorelines seen: **29**.

| scoreline | count | pct |
|---|---|---|
| 2-1 | 39 | 16.2% |
| 1-2 | 30 | 12.4% |
| 1-0 | 27 | 11.2% |
| 2-0 | 22 | 9.1% |
| 0-1 | 20 | 8.3% |
| 3-2 | 17 | 7.1% |
| 0-2 | 12 | 5.0% |
| 3-0 | 10 | 4.1% |
| 1-1 | 10 | 4.1% |
| 2-3 | 8 | 3.3% |
| 1-3 | 7 | 2.9% |
| 3-1 | 7 | 2.9% |
| 0-3 | 7 | 2.9% |
| 1-4 | 3 | 1.2% |
| 2-2 | 3 | 1.2% |
| 4-2 | 3 | 1.2% |
| 0-0 | 3 | 1.2% |
| 1-5 | 2 | 0.8% |
| 5-3 | 1 | 0.4% |
| 0-5 | 1 | 0.4% |

## 2. Scoreline frequency per season

### 2026
| scoreline | count | pct |
|---|---|---|
| 2-1 | 30 | 18.6% |
| 1-2 | 27 | 16.8% |
| 1-0 | 21 | 13.0% |
| 2-0 | 16 | 9.9% |
| 3-2 | 14 | 8.7% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 10 | 12.5% |
| 2-1 | 9 | 11.2% |
| 0-1 | 8 | 10.0% |
| 1-0 | 6 | 7.5% |
| 2-0 | 6 | 7.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 3 | 1.2% |
| 1 | 47 | 19.5% |
| 2 | 44 | 18.3% |
| 3 | 86 | 35.7% |
| 4 | 18 | 7.5% |
| 5 | 30 | 12.4% |
| 6 | 8 | 3.3% |
| 7 | 4 | 1.7% |
| 8 | 1 | 0.4% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **5**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026 | 2026-02-08 | 5-3 | 8 |
| 2026 | 2026-04-24 | 5-2 | 7 |
| 2026-2027 | 2026-08-07 | 3-4 | 7 |
| 2026-2027 | 2026-08-07 | 4-3 | 7 |
| 2026-2027 | 2026-09-12 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **224** (draws: **17**)
- Average winning margin: **1.53**

| margin | matches | pct |
|---|---|---|
| 1 | 143 | 63.8% |
| 2 | 53 | 23.7% |
| 3+ | 28 | 12.5% |

## 6. Margin by outcome

### Home wins
- Matches: **131** | avg margin: **1.5** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 84 | 64.1% |
| 2 | 33 | 25.2% |
| 3+ | 14 | 10.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **93** | avg margin: **1.57** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 59 | 63.4% |
| 2 | 20 | 21.5% |
| 3+ | 14 | 15.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 131 | 2-1 | 39 | 29.8% |
| draw | 17 | 1-1 | 10 | 58.8% |
| away | 93 | 1-2 | 30 | 32.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\japan1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\japan1\charts\scoreline_analysis_total_goals.png)

