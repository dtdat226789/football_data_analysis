# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:46:15+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 350 |
| Home wins | 171 (48.9%) |
| Draws | 92 (26.3%) |
| Away wins | 87 (24.9%) |
| Total goals | 804 |
| Average goals per match | 2.297 |
| Goalless matches | 31 (8.9%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 323 | 162 (50.2%) | 84 (26.0%) | 77 (23.8%) | 738 | 2.285 | 28 (8.7%) |
| 2026-2027 | 27 | 9 (33.3%) | 8 (29.6%) | 10 (37.0%) | 66 | 2.444 | 3 (11.1%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 95 (81.2%) | 15 (12.8%) | 7 (6.0%) | 117 |
| HT draw | 66 (40.2%) | 60 (36.6%) | 38 (23.2%) | 164 |
| HT away lead | 10 (14.5%) | 17 (24.6%) | 42 (60.9%) | 69 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (2.9%)
- Away comebacks (trailing at HT, won at FT): **7** (2.0%)

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
| Home lead | 117 | 95 (81.2%) | 15 (12.8%) | 7 (6.0%) |
| Away lead | 69 | 42 (60.9%) | 17 (24.6%) | 10 (14.5%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 66 | 40.2% |
| Draw | 60 | 36.6% |
| Away win | 38 | 23.2% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `319` of `350` (91.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 86 | 24.6% | 56 (65.1%) | 12 (14.0%) | 18 (20.9%) |
| 16-30 | 78 | 22.3% | 40 (51.3%) | 14 (17.9%) | 24 (30.8%) |
| 31-45 | 55 | 15.7% | 25 (45.5%) | 16 (29.1%) | 14 (25.5%) |
| 46-60 | 47 | 13.4% | 22 (46.8%) | 10 (21.3%) | 15 (31.9%) |
| 61-75 | 22 | 6.3% | 11 (50.0%) | 5 (22.7%) | 6 (27.3%) |
| 76-90 | 24 | 6.9% | 14 (58.3%) | 4 (16.7%) | 6 (25.0%) |
| 91-120 | 7 | 2.0% | 3 (42.9%) | 0 (0.0%) | 4 (57.1%) |

## 7. Goalless matches
- Overall: **31** of `350` (8.9%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 323 | 28 | 8.7% |
| 2026-2027 | 27 | 3 | 11.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\segunda4\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\segunda4\charts\matches_analysis_home_win_rate.png)

