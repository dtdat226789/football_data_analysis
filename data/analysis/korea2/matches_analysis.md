# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:00:27+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: K League 2 (South Korea)
- Scope: league `korea2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 493 |
| Home wins | 173 (35.1%) |
| Draws | 153 (31.0%) |
| Away wins | 167 (33.9%) |
| Total goals | 1274 |
| Average goals per match | 2.584 |
| Goalless matches | 42 (8.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 273 | 96 (35.2%) | 80 (29.3%) | 97 (35.5%) | 686 | 2.513 | 26 (9.5%) |
| 2026 | 220 | 77 (35.0%) | 73 (33.2%) | 70 (31.8%) | 588 | 2.673 | 16 (7.3%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 93 (67.4%) | 32 (23.2%) | 13 (9.4%) | 138 |
| HT draw | 69 (30.0%) | 96 (41.7%) | 65 (28.3%) | 230 |
| HT away lead | 11 (8.8%) | 25 (20.0%) | 89 (71.2%) | 125 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **11** (2.2%)
- Away comebacks (trailing at HT, won at FT): **13** (2.6%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Suwon Bluewings | Jeonnam | 0-1 | 2-1 |
| 2025 | Incheon | Cheongju | 0-1 | 2-1 |
| 2025 | Suwon Bluewings | Bucheon FC 1995 | 0-1 | 4-1 |
| 2025 | Cheongju | Seoul E-Land | 0-1 | 2-1 |
| 2025 | Jeonnam | Cheonan City | 0-1 | 4-1 |
| 2025 | Bucheon FC 1995 | Cheonan City | 0-1 | 2-1 |
| 2026 | Ansan Greeners | Jeonnam | 0-1 | 2-1 |
| 2026 | Suwon FC | Suwon Bluewings | 0-1 | 3-1 |
| 2026 | Gyeongnam | Suwon FC | 1-2 | 3-2 |
| 2026 | Ansan Greeners | Suwon Bluewings | 0-1 | 2-1 |
| 2026 | Paju Frontier | Seongnam | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Cheongju | Gyeongnam | 1-0 | 1-2 |
| 2025 | Gyeongnam | Jeonnam | 1-0 | 2-3 |
| 2025 | Hwaseong | Suwon Bluewings | 1-0 | 2-3 |
| 2026 | Gimhae | Ansan Greeners | 1-0 | 1-4 |
| 2026 | Seoul E-Land | Busan | 1-0 | 2-3 |
| 2026 | Ansan Greeners | Asan | 1-0 | 1-3 |
| 2026 | Daegu | Cheonan City | 1-0 | 1-2 |
| 2026 | Paju Frontier | Gyeongnam | 2-1 | 2-3 |
| 2026 | Hwaseong | Suwon Bluewings | 1-0 | 1-2 |
| 2026 | Seoul E-Land | Cheongju | 1-0 | 1-2 |
| 2026 | Ansan Greeners | Suwon FC | 1-0 | 1-3 |
| 2026 | Ansan Greeners | Seongnam | 1-0 | 1-2 |
| 2026 | Ansan Greeners | Daegu | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 138 | 93 (67.4%) | 32 (23.2%) | 13 (9.4%) |
| Away lead | 125 | 89 (71.2%) | 25 (20.0%) | 11 (8.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 69 | 30.0% |
| Draw | 96 | 41.7% |
| Away win | 65 | 28.3% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `451` of `493` (91.5%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 134 | 27.2% | 46 (34.3%) | 39 (29.1%) | 49 (36.6%) |
| 16-30 | 92 | 18.7% | 41 (44.6%) | 21 (22.8%) | 30 (32.6%) |
| 31-45 | 83 | 16.8% | 34 (41.0%) | 16 (19.3%) | 33 (39.8%) |
| 46-60 | 65 | 13.2% | 23 (35.4%) | 22 (33.8%) | 20 (30.8%) |
| 61-75 | 38 | 7.7% | 17 (44.7%) | 6 (15.8%) | 15 (39.5%) |
| 76-90 | 30 | 6.1% | 9 (30.0%) | 6 (20.0%) | 15 (50.0%) |
| 91-120 | 9 | 1.8% | 3 (33.3%) | 1 (11.1%) | 5 (55.6%) |

## 7. Goalless matches
- Overall: **42** of `493` (8.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 273 | 26 | 9.5% |
| 2026 | 220 | 16 | 7.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\korea2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\korea2\charts\matches_analysis_home_win_rate.png)

