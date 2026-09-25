# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:56:45+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: 3. CFL - Group B (Czech Republic)
- Scope: league `czech3b`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 326 |
| Home wins | 140 (42.9%) |
| Draws | 76 (23.3%) |
| Away wins | 110 (33.7%) |
| Total goals | 1079 |
| Average goals per match | 3.310 |
| Goalless matches | 12 (3.7%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 272 | 120 (44.1%) | 60 (22.1%) | 92 (33.8%) | 912 | 3.353 | 7 (2.6%) |
| 2026-2027 | 54 | 20 (37.0%) | 16 (29.6%) | 18 (33.3%) | 167 | 3.093 | 5 (9.3%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 103 (80.5%) | 17 (13.3%) | 8 (6.2%) | 128 |
| HT draw | 33 (31.7%) | 43 (41.3%) | 28 (26.9%) | 104 |
| HT away lead | 4 (4.3%) | 16 (17.0%) | 74 (78.7%) | 94 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **4** (1.2%)
- Away comebacks (trailing at HT, won at FT): **8** (2.5%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Zapy | FK Ceska Lipa | 1-2 | 3-2 |
| 2025-2026 | Hradec Kralove B | Varnsdorf | 1-2 | 3-2 |
| 2025-2026 | Hradec Kralove B | Usti nad Orlici | 0-1 | 3-1 |
| 2025-2026 | Zapy | Kolin | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Liberec B | Jablonec B | 1-0 | 1-3 |
| 2025-2026 | Benatky n. Jiz. | Banik Most-Sous | 1-0 | 1-2 |
| 2025-2026 | Kolin | Zapy | 2-0 | 2-3 |
| 2025-2026 | Liberec B | Banik Most-Sous | 1-0 | 1-2 |
| 2025-2026 | Varnsdorf | Jablonec B | 1-0 | 1-2 |
| 2025-2026 | Usti nad Orlici | Jablonec B | 1-0 | 1-3 |
| 2025-2026 | Velke Hamry | FK Ceska Lipa | 1-0 | 1-2 |
| 2025-2026 | Jablonec B | FK Ceska Lipa | 1-0 | 1-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 128 | 103 (80.5%) | 17 (13.3%) | 8 (6.2%) |
| Away lead | 94 | 74 (78.7%) | 16 (17.0%) | 4 (4.3%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 33 | 31.7% |
| Draw | 43 | 41.3% |
| Away win | 28 | 26.9% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `314` of `326` (96.3%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 121 | 37.1% | 52 (43.0%) | 23 (19.0%) | 46 (38.0%) |
| 16-30 | 86 | 26.4% | 42 (48.8%) | 16 (18.6%) | 28 (32.6%) |
| 31-45 | 56 | 17.2% | 24 (42.9%) | 13 (23.2%) | 19 (33.9%) |
| 46-60 | 33 | 10.1% | 13 (39.4%) | 9 (27.3%) | 11 (33.3%) |
| 61-75 | 8 | 2.5% | 3 (37.5%) | 3 (37.5%) | 2 (25.0%) |
| 76-90 | 9 | 2.8% | 5 (55.6%) | 0 (0.0%) | 4 (44.4%) |
| 91-120 | 1 | 0.3% | 1 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **12** of `326` (3.7%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 272 | 7 | 2.6% |
| 2026-2027 | 54 | 5 | 9.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\czech3b\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\czech3b\charts\matches_analysis_home_win_rate.png)

