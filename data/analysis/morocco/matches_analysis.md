# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:03:34+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Botola Pro (Morocco)
- Scope: league `morocco`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 488 |
| Home wins | 198 (40.6%) |
| Draws | 153 (31.4%) |
| Away wins | 137 (28.1%) |
| Total goals | 1094 |
| Average goals per match | 2.242 |
| Goalless matches | 51 (10.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2024-2025 | 240 | 104 (43.3%) | 68 (28.3%) | 68 (28.3%) | 555 | 2.312 | 22 (9.2%) |
| 2025-2026 | 248 | 94 (37.9%) | 85 (34.3%) | 69 (27.8%) | 539 | 2.173 | 29 (11.7%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 105 (71.9%) | 34 (23.3%) | 7 (4.8%) | 146 |
| HT draw | 83 (36.6%) | 95 (41.9%) | 49 (21.6%) | 227 |
| HT away lead | 10 (8.7%) | 24 (20.9%) | 81 (70.4%) | 115 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (2.0%)
- Away comebacks (trailing at HT, won at FT): **7** (1.4%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2024-2025 | Hassania Agadir | Union Touarga | 0-1 | 2-1 |
| 2024-2025 | Jeunesse Sportive Soualem | IR Tanger | 0-1 | 2-1 |
| 2024-2025 | Raja Casablanca | Union Touarga | 0-1 | 2-1 |
| 2024-2025 | FUS Rabat | Raja Casablanca | 0-1 | 2-1 |
| 2024-2025 | Difaa El Jadidi | COD Meknes | 0-1 | 2-1 |
| 2024-2025 | Difaa El Jadidi | IR Tanger | 0-1 | 2-1 |
| 2025-2026 | Dcheira | Kawkab Marrakech | 0-1 | 2-1 |
| 2025-2026 | FAR Rabat | Dcheira | 1-2 | 3-2 |
| 2025-2026 | Hassania Agadir | Olympique de Safi | 0-1 | 2-1 |
| 2025-2026 | Maghreb Fez | Difaa El Jadidi | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2024-2025 | Olympique de Safi | Raja Casablanca | 2-1 | 2-3 |
| 2024-2025 | Moghreb Tetouan | Difaa El Jadidi | 1-0 | 1-3 |
| 2025-2026 | FUS Rabat | Hassania Agadir | 1-0 | 1-2 |
| 2025-2026 | Union Touarga | Wydad AC | 2-1 | 3-4 |
| 2025-2026 | Olympique de Safi | IR Tanger | 1-0 | 1-2 |
| 2025-2026 | Wydad AC | Yacoub El Mansour | 1-0 | 1-2 |
| 2025-2026 | Kawkab Marrakech | Renaissance Zemamra | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 146 | 105 (71.9%) | 34 (23.3%) | 7 (4.8%) |
| Away lead | 115 | 81 (70.4%) | 24 (20.9%) | 10 (8.7%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 83 | 36.6% |
| Draw | 95 | 41.9% |
| Away win | 49 | 21.6% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `437` of `488` (89.5%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 106 | 21.7% | 48 (45.3%) | 24 (22.6%) | 34 (32.1%) |
| 16-30 | 100 | 20.5% | 38 (38.0%) | 27 (27.0%) | 35 (35.0%) |
| 31-45 | 76 | 15.6% | 33 (43.4%) | 23 (30.3%) | 20 (26.3%) |
| 46-60 | 82 | 16.8% | 36 (43.9%) | 16 (19.5%) | 30 (36.6%) |
| 61-75 | 36 | 7.4% | 21 (58.3%) | 7 (19.4%) | 8 (22.2%) |
| 76-90 | 25 | 5.1% | 14 (56.0%) | 5 (20.0%) | 6 (24.0%) |
| 91-120 | 12 | 2.5% | 8 (66.7%) | 0 (0.0%) | 4 (33.3%) |

## 7. Goalless matches
- Overall: **51** of `488` (10.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2024-2025 | 240 | 22 | 9.2% |
| 2025-2026 | 248 | 29 | 11.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\morocco\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\morocco\charts\matches_analysis_home_win_rate.png)

