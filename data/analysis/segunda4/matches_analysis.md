# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:07:31+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 359 |
| Home wins | 177 (49.3%) |
| Draws | 94 (26.2%) |
| Away wins | 88 (24.5%) |
| Total goals | 826 |
| Average goals per match | 2.301 |
| Goalless matches | 33 (9.2%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 323 | 162 (50.2%) | 84 (26.0%) | 77 (23.8%) | 738 | 2.285 | 28 (8.7%) |
| 2026-2027 | 36 | 15 (41.7%) | 10 (27.8%) | 11 (30.6%) | 88 | 2.444 | 5 (13.9%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 99 (81.8%) | 15 (12.4%) | 7 (5.8%) | 121 |
| HT draw | 68 (40.5%) | 62 (36.9%) | 38 (22.6%) | 168 |
| HT away lead | 10 (14.3%) | 17 (24.3%) | 43 (61.4%) | 70 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (2.8%)
- Away comebacks (trailing at HT, won at FT): **7** (1.9%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | CD Extremadura | Malaga B | 0-2 | 3-2 |
| 2025-2026 | CD Extremadura | Malagueno | 0-2 | 3-2 |
| 2025-2026 | La Union | CD Extremadura | 0-1 | 2-1 |
| 2025-2026 | Malaga B | Xerez D.F.C. | 0-1 | 2-1 |
| 2025-2026 | Puente Genil | Antoniano | 0-1 | 2-1 |
| 2025-2026 | Xerez CD | La Union | 0-1 | 2-1 |
| 2025-2026 | CD Extremadura | Recreativo Huelva | 0-1 | 2-1 |
| 2025-2026 | Malaga B | Antoniano | 0-1 | 3-2 |
| 2025-2026 | CD Extremadura | La Union | 0-1 | 4-2 |
| 2025-2026 | CD Estepona | Aguilas FC | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | CD Estepona | Lorca Deportiva | 1-0 | 1-3 |
| 2025-2026 | Antoniano | Linares | 1-0 | 1-2 |
| 2025-2026 | Almeria B | Xerez CD | 1-0 | 1-2 |
| 2025-2026 | Linares | CD Estepona | 2-1 | 2-3 |
| 2025-2026 | Almeria B | Deportiva Minera | 2-1 | 3-4 |
| 2026-2027 | Antoniano | Don Benito | 1-0 | 1-2 |
| 2026-2027 | Tamaraceite | Recreativo Huelva | 1-0 | 1-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 121 | 99 (81.8%) | 15 (12.4%) | 7 (5.8%) |
| Away lead | 70 | 43 (61.4%) | 17 (24.3%) | 10 (14.3%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 68 | 40.5% |
| Draw | 62 | 36.9% |
| Away win | 38 | 22.6% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `326` of `359` (90.8%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 91 | 25.3% | 60 (65.9%) | 12 (13.2%) | 19 (20.9%) |
| 16-30 | 79 | 22.0% | 41 (51.9%) | 14 (17.7%) | 24 (30.4%) |
| 31-45 | 54 | 15.0% | 25 (46.3%) | 16 (29.6%) | 13 (24.1%) |
| 46-60 | 47 | 13.1% | 22 (46.8%) | 10 (21.3%) | 15 (31.9%) |
| 61-75 | 23 | 6.4% | 12 (52.2%) | 5 (21.7%) | 6 (26.1%) |
| 76-90 | 24 | 6.7% | 14 (58.3%) | 4 (16.7%) | 6 (25.0%) |
| 91-120 | 8 | 2.2% | 3 (37.5%) | 0 (0.0%) | 5 (62.5%) |

## 7. Goalless matches
- Overall: **33** of `359` (9.2%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 323 | 28 | 8.7% |
| 2026-2027 | 36 | 5 | 13.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\segunda4\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\segunda4\charts\matches_analysis_home_win_rate.png)

