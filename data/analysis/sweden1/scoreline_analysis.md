# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:48:34+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Allsvenskan (Sweden)
- Scope: league `sweden1`

## 1. Scoreline frequency
- Matches analysed: **416** across **2** seasons.
- Distinct scorelines seen: **36**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 53 | 12.7% |
| 2-0 | 40 | 9.6% |
| 0-1 | 39 | 9.4% |
| 1-2 | 33 | 7.9% |
| 1-0 | 25 | 6.0% |
| 2-1 | 25 | 6.0% |
| 0-0 | 21 | 5.0% |
| 3-0 | 20 | 4.8% |
| 0-2 | 19 | 4.6% |
| 1-3 | 18 | 4.3% |
| 2-2 | 16 | 3.8% |
| 0-3 | 15 | 3.6% |
| 3-2 | 13 | 3.1% |
| 3-1 | 11 | 2.6% |
| 4-0 | 10 | 2.4% |
| 2-3 | 10 | 2.4% |
| 4-3 | 8 | 1.9% |
| 4-1 | 6 | 1.4% |
| 1-4 | 5 | 1.2% |
| 0-5 | 3 | 0.7% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-1 | 30 | 12.5% |
| 0-1 | 22 | 9.2% |
| 2-0 | 20 | 8.3% |
| 1-2 | 20 | 8.3% |
| 1-0 | 17 | 7.1% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 23 | 13.1% |
| 2-0 | 20 | 11.4% |
| 0-1 | 17 | 9.7% |
| 1-2 | 13 | 7.4% |
| 2-1 | 12 | 6.8% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 21 | 5.0% |
| 1 | 64 | 15.4% |
| 2 | 112 | 26.9% |
| 3 | 93 | 22.4% |
| 4 | 58 | 13.9% |
| 5 | 37 | 8.9% |
| 6 | 13 | 3.1% |
| 7 | 12 | 2.9% |
| 8 | 2 | 0.5% |
| 9 | 2 | 0.5% |
| 10+ | 2 | 0.5% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **18**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-08-02 | 6-4 | 10 |
| 2025 | 2025-09-29 | 8-2 | 10 |
| 2026 | 2026-04-18 | 8-1 | 9 |
| 2026 | 2026-05-31 | 4-5 | 9 |
| 2025 | 2025-10-25 | 6-2 | 8 |
| 2026 | 2026-07-03 | 4-4 | 8 |
| 2025 | 2025-03-30 | 4-3 | 7 |
| 2025 | 2025-04-06 | 4-3 | 7 |
| 2025 | 2025-04-23 | 3-4 | 7 |
| 2025 | 2025-04-23 | 4-3 | 7 |
| 2025 | 2025-05-15 | 4-3 | 7 |
| 2025 | 2025-07-27 | 1-6 | 7 |
| 2025 | 2025-07-28 | 4-3 | 7 |
| 2025 | 2025-09-14 | 4-3 | 7 |
| 2026 | 2026-05-30 | 5-2 | 7 |
| 2026 | 2026-07-11 | 4-3 | 7 |
| 2026 | 2026-08-08 | 3-4 | 7 |
| 2026 | 2026-08-15 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **322** (draws: **94**)
- Average winning margin: **1.86**

| margin | matches | pct |
|---|---|---|
| 1 | 156 | 48.4% |
| 2 | 93 | 28.9% |
| 3+ | 73 | 22.7% |

## 6. Margin by outcome

### Home wins
- Matches: **169** | avg margin: **2.01** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 71 | 42.0% |
| 2 | 53 | 31.4% |
| 3+ | 45 | 26.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **153** | avg margin: **1.71** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 85 | 55.6% |
| 2 | 40 | 26.1% |
| 3+ | 28 | 18.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 169 | 2-0 | 40 | 23.7% |
| draw | 94 | 1-1 | 53 | 56.4% |
| away | 153 | 0-1 | 39 | 25.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\sweden1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\sweden1\charts\scoreline_analysis_total_goals.png)

