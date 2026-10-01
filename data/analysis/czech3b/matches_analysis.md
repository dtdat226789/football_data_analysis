# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:47:34+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: 3. CFL - Group B (Czech Republic)
- Scope: league `czech3b`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 333 |
| Home wins | 143 (42.9%) |
| Draws | 76 (22.8%) |
| Away wins | 114 (34.2%) |
| Total goals | 1104 |
| Average goals per match | 3.315 |
| Goalless matches | 12 (3.6%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 272 | 120 (44.1%) | 60 (22.1%) | 92 (33.8%) | 912 | 3.353 | 7 (2.6%) |
| 2026-2027 | 61 | 23 (37.7%) | 16 (26.2%) | 22 (36.1%) | 192 | 3.148 | 5 (8.2%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 104 (80.6%) | 17 (13.2%) | 8 (6.2%) | 129 |
| HT draw | 35 (32.4%) | 43 (39.8%) | 30 (27.8%) | 108 |
| HT away lead | 4 (4.2%) | 16 (16.7%) | 76 (79.2%) | 96 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **4** (1.2%)
- Away comebacks (trailing at HT, won at FT): **8** (2.4%)

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
| Home lead | 129 | 104 (80.6%) | 17 (13.2%) | 8 (6.2%) |
| Away lead | 96 | 76 (79.2%) | 16 (16.7%) | 4 (4.2%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 35 | 32.4% |
| Draw | 43 | 39.8% |
| Away win | 30 | 27.8% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `321` of `333` (96.4%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 123 | 36.9% | 54 (43.9%) | 23 (18.7%) | 46 (37.4%) |
| 16-30 | 88 | 26.4% | 43 (48.9%) | 16 (18.2%) | 29 (33.0%) |
| 31-45 | 57 | 17.1% | 24 (42.1%) | 13 (22.8%) | 20 (35.1%) |
| 46-60 | 33 | 9.9% | 13 (39.4%) | 9 (27.3%) | 11 (33.3%) |
| 61-75 | 8 | 2.4% | 3 (37.5%) | 3 (37.5%) | 2 (25.0%) |
| 76-90 | 11 | 3.3% | 5 (45.5%) | 0 (0.0%) | 6 (54.5%) |
| 91-120 | 1 | 0.3% | 1 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **12** of `333` (3.6%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 272 | 7 | 2.6% |
| 2026-2027 | 61 | 5 | 8.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\czech3b\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\czech3b\charts\matches_analysis_home_win_rate.png)

