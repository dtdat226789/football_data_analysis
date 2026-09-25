# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:59:06+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

## 1. Scoreline frequency
- Matches analysed: **371** across **2** seasons.
- Distinct scorelines seen: **26**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 57 | 15.4% |
| 0-0 | 40 | 10.8% |
| 1-0 | 33 | 8.9% |
| 1-2 | 30 | 8.1% |
| 2-1 | 30 | 8.1% |
| 0-1 | 26 | 7.0% |
| 2-0 | 24 | 6.5% |
| 2-2 | 21 | 5.7% |
| 0-3 | 19 | 5.1% |
| 0-2 | 17 | 4.6% |
| 3-0 | 16 | 4.3% |
| 3-1 | 12 | 3.2% |
| 1-3 | 9 | 2.4% |
| 3-2 | 7 | 1.9% |
| 2-3 | 6 | 1.6% |
| 4-1 | 4 | 1.1% |
| 4-0 | 4 | 1.1% |
| 1-4 | 4 | 1.1% |
| 0-4 | 3 | 0.8% |
| 3-3 | 2 | 0.5% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 46 | 15.2% |
| 0-0 | 32 | 10.6% |
| 1-0 | 28 | 9.2% |
| 1-2 | 27 | 8.9% |
| 2-1 | 27 | 8.9% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 11 | 16.2% |
| 0-0 | 8 | 11.8% |
| 2-0 | 8 | 11.8% |
| 0-2 | 6 | 8.8% |
| 1-0 | 5 | 7.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 40 | 10.8% |
| 1 | 59 | 15.9% |
| 2 | 98 | 26.4% |
| 3 | 95 | 25.6% |
| 4 | 49 | 13.2% |
| 5 | 22 | 5.9% |
| 6 | 4 | 1.1% |
| 7 | 3 | 0.8% |
| 8 | 1 | 0.3% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **4**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-04-10 | 3-5 | 8 |
| 2026-2027 | 2026-08-14 | 4-3 | 7 |
| 2026-2027 | 2026-09-05 | 6-1 | 7 |
| 2026-2027 | 2026-09-05 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **251** (draws: **120**)
- Average winning margin: **1.73**

| margin | matches | pct |
|---|---|---|
| 1 | 133 | 53.0% |
| 2 | 65 | 25.9% |
| 3+ | 53 | 21.1% |

## 6. Margin by outcome

### Home wins
- Matches: **135** | avg margin: **1.75** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 71 | 52.6% |
| 2 | 37 | 27.4% |
| 3+ | 27 | 20.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **116** | avg margin: **1.72** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 62 | 53.4% |
| 2 | 28 | 24.1% |
| 3+ | 26 | 22.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 135 | 1-0 | 33 | 24.4% |
| draw | 120 | 1-1 | 57 | 47.5% |
| away | 116 | 1-2 | 30 | 25.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\france3\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\france3\charts\scoreline_analysis_total_goals.png)

