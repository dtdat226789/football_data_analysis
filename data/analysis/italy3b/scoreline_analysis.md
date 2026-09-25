# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:02:22+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Serie C - Group B (Italy)
- Scope: league `italy3b`

## 1. Scoreline frequency
- Matches analysed: **417** across **2** seasons.
- Distinct scorelines seen: **25**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 64 | 15.3% |
| 1-0 | 51 | 12.2% |
| 2-1 | 43 | 10.3% |
| 0-1 | 41 | 9.8% |
| 0-0 | 40 | 9.6% |
| 2-0 | 31 | 7.4% |
| 1-2 | 26 | 6.2% |
| 2-2 | 24 | 5.8% |
| 0-2 | 22 | 5.3% |
| 3-1 | 11 | 2.6% |
| 3-0 | 11 | 2.6% |
| 0-3 | 10 | 2.4% |
| 1-3 | 8 | 1.9% |
| 3-2 | 7 | 1.7% |
| 2-3 | 7 | 1.7% |
| 2-4 | 4 | 1.0% |
| 4-2 | 4 | 1.0% |
| 1-4 | 3 | 0.7% |
| 3-3 | 3 | 0.7% |
| 0-4 | 2 | 0.5% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 55 | 15.4% |
| 1-0 | 45 | 12.6% |
| 0-1 | 38 | 10.6% |
| 2-1 | 36 | 10.1% |
| 0-0 | 35 | 9.8% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 9 | 15.0% |
| 2-0 | 7 | 11.7% |
| 2-1 | 7 | 11.7% |
| 1-0 | 6 | 10.0% |
| 0-0 | 5 | 8.3% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 40 | 9.6% |
| 1 | 92 | 22.1% |
| 2 | 117 | 28.1% |
| 3 | 90 | 21.6% |
| 4 | 46 | 11.0% |
| 5 | 19 | 4.6% |
| 6 | 12 | 2.9% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **1**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-08-29 | 6-3 | 9 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **286** (draws: **131**)
- Average winning margin: **1.52**

| margin | matches | pct |
|---|---|---|
| 1 | 175 | 61.2% |
| 2 | 80 | 28.0% |
| 3+ | 31 | 10.8% |

## 6. Margin by outcome

### Home wins
- Matches: **163** | avg margin: **1.5** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 101 | 62.0% |
| 2 | 46 | 28.2% |
| 3+ | 16 | 9.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **123** | avg margin: **1.54** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 74 | 60.2% |
| 2 | 34 | 27.6% |
| 3+ | 15 | 12.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 163 | 1-0 | 51 | 31.3% |
| draw | 131 | 1-1 | 64 | 48.9% |
| away | 123 | 0-1 | 41 | 33.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\italy3b\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\italy3b\charts\scoreline_analysis_total_goals.png)

