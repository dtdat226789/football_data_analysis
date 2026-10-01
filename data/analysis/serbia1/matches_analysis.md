# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:08:01+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Mozzart Bet Super Liga (Serbia)
- Scope: league `serbia1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 365 |
| Home wins | 159 (43.6%) |
| Draws | 104 (28.5%) |
| Away wins | 102 (27.9%) |
| Total goals | 972 |
| Average goals per match | 2.663 |
| Goalless matches | 42 (11.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 297 | 124 (41.8%) | 86 (29.0%) | 87 (29.3%) | 790 | 2.66 | 36 (12.1%) |
| 2026-2027 | 68 | 35 (51.5%) | 18 (26.5%) | 15 (22.1%) | 182 | 2.676 | 6 (8.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 109 (75.2%) | 27 (18.6%) | 9 (6.2%) | 145 |
| HT draw | 43 (30.9%) | 64 (46.0%) | 32 (23.0%) | 139 |
| HT away lead | 7 (8.8%) | 13 (16.2%) | 60 (75.0%) | 80 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (1.9%)
- Away comebacks (trailing at HT, won at FT): **9** (2.5%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Partizan | Radnicki 1923 | 0-1 | 2-1 |
| 2025-2026 | Crvena zvezda | Radnicki 1923 | 0-1 | 2-1 |
| 2025-2026 | Javor | Radnik | 1-2 | 3-2 |
| 2025-2026 | Vojvodina | Crvena zvezda | 0-2 | 3-2 |
| 2025-2026 | Radnik | Napredak | 0-1 | 2-1 |
| 2026-2027 | Zeleznicar Pancevo | Radnik | 0-1 | 5-1 |
| 2026-2027 | Zeleznicar Pancevo | Cukaricki | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Radnicki Nis | Novi Pazar | 2-1 | 2-3 |
| 2025-2026 | TSC | OFK Beograd Mozzart Bet | 1-0 | 1-3 |
| 2025-2026 | Radnik | Radnicki 1923 | 2-0 | 2-3 |
| 2025-2026 | Javor | Partizan | 2-1 | 2-3 |
| 2025-2026 | Sp. Subotica | TSC | 1-0 | 1-2 |
| 2025-2026 | Javor | Vojvodina | 1-0 | 1-2 |
| 2025-2026 | Javor | Mladost | 1-0 | 2-4 |
| 2025-2026 | TSC | Radnicki Nis | 1-0 | 1-2 |
| 2026-2027 | Macva | Mladost | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 145 | 109 (75.2%) | 27 (18.6%) | 9 (6.2%) |
| Away lead | 80 | 60 (75.0%) | 13 (16.2%) | 7 (8.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 43 | 30.9% |
| Draw | 64 | 46.0% |
| Away win | 32 | 23.0% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `322` of `365` (88.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 95 | 26.0% | 49 (51.6%) | 17 (17.9%) | 29 (30.5%) |
| 16-30 | 90 | 24.7% | 34 (37.8%) | 26 (28.9%) | 30 (33.3%) |
| 31-45 | 63 | 17.3% | 35 (55.6%) | 8 (12.7%) | 20 (31.7%) |
| 46-60 | 41 | 11.2% | 19 (46.3%) | 7 (17.1%) | 15 (36.6%) |
| 61-75 | 20 | 5.5% | 15 (75.0%) | 3 (15.0%) | 2 (10.0%) |
| 76-90 | 6 | 1.6% | 3 (50.0%) | 1 (16.7%) | 2 (33.3%) |
| 91-120 | 7 | 1.9% | 4 (57.1%) | 0 (0.0%) | 3 (42.9%) |

## 7. Goalless matches
- Overall: **42** of `365` (11.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 297 | 36 | 12.1% |
| 2026-2027 | 68 | 6 | 8.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\serbia1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\serbia1\charts\matches_analysis_home_win_rate.png)

