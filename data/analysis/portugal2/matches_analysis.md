# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:41:48+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Liga Portugal 2 (Portugal)
- Scope: league `portugal2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 363 |
| Home wins | 153 (42.1%) |
| Draws | 88 (24.2%) |
| Away wins | 122 (33.6%) |
| Total goals | 874 |
| Average goals per match | 2.408 |
| Goalless matches | 37 (10.2%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 310 | 131 (42.3%) | 76 (24.5%) | 103 (33.2%) | 751 | 2.423 | 33 (10.6%) |
| 2026-2027 | 53 | 22 (41.5%) | 12 (22.6%) | 19 (35.8%) | 123 | 2.321 | 4 (7.5%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 90 (76.3%) | 16 (13.6%) | 12 (10.2%) | 118 |
| HT draw | 54 (34.0%) | 58 (36.5%) | 47 (29.6%) | 159 |
| HT away lead | 9 (10.5%) | 14 (16.3%) | 63 (73.3%) | 86 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **9** (2.5%)
- Away comebacks (trailing at HT, won at FT): **12** (3.3%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Torreense | Academico Viseu | 0-1 | 2-1 |
| 2025-2026 | Torreense | Oliveirense | 0-1 | 3-2 |
| 2025-2026 | SC Farense | Benfica B | 0-3 | 4-3 |
| 2025-2026 | Leiria | Chaves | 0-1 | 2-1 |
| 2025-2026 | Academico Viseu | Lusitania FC | 1-2 | 3-2 |
| 2025-2026 | FC Porto B | Sporting CP B | 0-1 | 2-1 |
| 2025-2026 | Lusitania FC | Felgueiras | 0-1 | 2-1 |
| 2025-2026 | Sporting CP B | Portimonense | 1-2 | 4-3 |
| 2025-2026 | Leixoes | Pacos Ferreira | 1-2 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Pacos Ferreira | Vizela | 1-0 | 1-2 |
| 2025-2026 | Portimonense | Sporting CP B | 1-0 | 1-2 |
| 2025-2026 | FC Porto B | Torreense | 2-0 | 2-3 |
| 2025-2026 | Maritimo | Leiria | 1-0 | 1-3 |
| 2025-2026 | Leiria | Felgueiras | 2-1 | 2-3 |
| 2025-2026 | Portimonense | Leixoes | 1-0 | 1-2 |
| 2025-2026 | Chaves | Maritimo | 2-1 | 2-3 |
| 2025-2026 | Oliveirense | Feirense | 2-1 | 3-4 |
| 2025-2026 | Portimonense | Pacos Ferreira | 2-0 | 2-3 |
| 2025-2026 | Sporting CP B | Penafiel | 1-0 | 1-2 |
| 2025-2026 | Feirense | Oliveirense | 1-0 | 1-2 |
| 2025-2026 | Lusitania FC | Torreense | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 118 | 90 (76.3%) | 16 (13.6%) | 12 (10.2%) |
| Away lead | 86 | 63 (73.3%) | 14 (16.3%) | 9 (10.5%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 54 | 34.0% |
| Draw | 58 | 36.5% |
| Away win | 47 | 29.6% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `326` of `363` (89.8%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 86 | 23.7% | 37 (43.0%) | 15 (17.4%) | 34 (39.5%) |
| 16-30 | 77 | 21.2% | 33 (42.9%) | 8 (10.4%) | 36 (46.8%) |
| 31-45 | 65 | 17.9% | 39 (60.0%) | 12 (18.5%) | 14 (21.5%) |
| 46-60 | 48 | 13.2% | 23 (47.9%) | 10 (20.8%) | 15 (31.2%) |
| 61-75 | 27 | 7.4% | 10 (37.0%) | 6 (22.2%) | 11 (40.7%) |
| 76-90 | 13 | 3.6% | 4 (30.8%) | 0 (0.0%) | 9 (69.2%) |
| 91-120 | 10 | 2.8% | 7 (70.0%) | 0 (0.0%) | 3 (30.0%) |

## 7. Goalless matches
- Overall: **37** of `363` (10.2%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 310 | 33 | 10.6% |
| 2026-2027 | 53 | 4 | 7.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\portugal2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\portugal2\charts\matches_analysis_home_win_rate.png)

