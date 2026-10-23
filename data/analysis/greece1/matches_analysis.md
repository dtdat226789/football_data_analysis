# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:51:37+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Super League (Greece)
- Scope: league `greece1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 281 |
| Home wins | 116 (41.3%) |
| Draws | 77 (27.4%) |
| Away wins | 88 (31.3%) |
| Total goals | 712 |
| Average goals per match | 2.534 |
| Goalless matches | 24 (8.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 246 | 102 (41.5%) | 68 (27.6%) | 76 (30.9%) | 624 | 2.537 | 22 (8.9%) |
| 2026-2027 | 35 | 14 (40.0%) | 9 (25.7%) | 12 (34.3%) | 88 | 2.514 | 2 (5.7%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 79 (83.2%) | 11 (11.6%) | 5 (5.3%) | 95 |
| HT draw | 30 (27.5%) | 49 (45.0%) | 30 (27.5%) | 109 |
| HT away lead | 7 (9.1%) | 17 (22.1%) | 53 (68.8%) | 77 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (2.5%)
- Away comebacks (trailing at HT, won at FT): **5** (1.8%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | PAOK | Olympiacos Piraeus | 0-1 | 2-1 |
| 2025-2026 | AEK Athens | OFI Crete | 0-1 | 2-1 |
| 2025-2026 | Panserraikos | Kifisia | 0-1 | 2-1 |
| 2025-2026 | Volos | PAOK | 0-1 | 2-1 |
| 2025-2026 | Aris | Volos | 1-2 | 3-2 |
| 2025-2026 | Levadiakos | OFI Crete | 0-2 | 3-2 |
| 2026-2027 | Kalamata | Volos | 0-1 | 3-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Panetolikos | Panathinaikos | 1-0 | 1-2 |
| 2025-2026 | Kifisia | AEK Athens | 2-1 | 2-3 |
| 2025-2026 | Kifisia | AEK Athens FC | 2-1 | 2-3 |
| 2025-2026 | Panserraikos | Kifisia | 1-0 | 1-2 |
| 2025-2026 | Atromitos | Panetolikos | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 95 | 79 (83.2%) | 11 (11.6%) | 5 (5.3%) |
| Away lead | 77 | 53 (68.8%) | 17 (22.1%) | 7 (9.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 30 | 27.5% |
| Draw | 49 | 45.0% |
| Away win | 30 | 27.5% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `257` of `281` (91.5%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 75 | 26.7% | 39 (52.0%) | 11 (14.7%) | 25 (33.3%) |
| 16-30 | 66 | 23.5% | 32 (48.5%) | 17 (25.8%) | 17 (25.8%) |
| 31-45 | 51 | 18.1% | 20 (39.2%) | 9 (17.6%) | 22 (43.1%) |
| 46-60 | 31 | 11.0% | 13 (41.9%) | 10 (32.3%) | 8 (25.8%) |
| 61-75 | 23 | 8.2% | 7 (30.4%) | 5 (21.7%) | 11 (47.8%) |
| 76-90 | 7 | 2.5% | 2 (28.6%) | 1 (14.3%) | 4 (57.1%) |
| 91-120 | 4 | 1.4% | 3 (75.0%) | 0 (0.0%) | 1 (25.0%) |

## 7. Goalless matches
- Overall: **24** of `281` (8.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 246 | 22 | 8.9% |
| 2026-2027 | 35 | 2 | 5.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\greece1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\greece1\charts\matches_analysis_home_win_rate.png)

