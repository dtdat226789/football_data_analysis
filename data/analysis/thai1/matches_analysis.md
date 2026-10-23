# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:10:14+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Thai League 1 (Thailand)
- Scope: league `thai1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 264 |
| Home wins | 114 (43.2%) |
| Draws | 79 (29.9%) |
| Away wins | 71 (26.9%) |
| Total goals | 704 |
| Average goals per match | 2.667 |
| Goalless matches | 18 (6.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 240 | 104 (43.3%) | 75 (31.2%) | 61 (25.4%) | 642 | 2.675 | 17 (7.1%) |
| 2026-2027 | 24 | 10 (41.7%) | 4 (16.7%) | 10 (41.7%) | 62 | 2.583 | 1 (4.2%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 70 (72.9%) | 18 (18.8%) | 8 (8.3%) | 96 |
| HT draw | 36 (34.3%) | 41 (39.0%) | 28 (26.7%) | 105 |
| HT away lead | 8 (12.7%) | 20 (31.7%) | 35 (55.6%) | 63 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (3.0%)
- Away comebacks (trailing at HT, won at FT): **8** (3.0%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Pathum United | Lamphun Warrior | 0-1 | 2-1 |
| 2025-2026 | Buriram | Nakhon Ratchasima FC | 0-1 | 2-1 |
| 2025-2026 | Ayutthaya Utd | Bangkok Utd | 0-1 | 3-1 |
| 2025-2026 | Prachuap | Chiangrai Utd | 0-2 | 3-2 |
| 2025-2026 | Chonburi | Port MTI FC | 1-2 | 3-2 |
| 2025-2026 | Uthai Thani | Kanchanaburi | 0-1 | 2-1 |
| 2025-2026 | Sukhothai | Rayong FC | 0-1 | 2-1 |
| 2025-2026 | Muang Thong Utd | Chiangrai Utd | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Lamphun Warrior | Buriram | 2-1 | 2-3 |
| 2025-2026 | Kanchanaburi | Ayutthaya Utd | 1-0 | 1-2 |
| 2025-2026 | Bangkok Utd | Uthai Thani | 1-0 | 1-2 |
| 2025-2026 | Chonburi | Pathum United | 1-0 | 1-2 |
| 2025-2026 | Ratchaburi | Chiangrai Utd | 1-0 | 1-2 |
| 2025-2026 | Sukhothai | Ratchaburi | 1-0 | 1-2 |
| 2025-2026 | Kanchanaburi | Buriram | 1-0 | 1-3 |
| 2025-2026 | Ayutthaya Utd | Prachuap | 1-0 | 1-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 96 | 70 (72.9%) | 18 (18.8%) | 8 (8.3%) |
| Away lead | 63 | 35 (55.6%) | 20 (31.7%) | 8 (12.7%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 36 | 34.3% |
| Draw | 41 | 39.0% |
| Away win | 28 | 26.7% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `246` of `264` (93.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 81 | 30.7% | 46 (56.8%) | 14 (17.3%) | 21 (25.9%) |
| 16-30 | 51 | 19.3% | 22 (43.1%) | 12 (23.5%) | 17 (33.3%) |
| 31-45 | 42 | 15.9% | 16 (38.1%) | 14 (33.3%) | 12 (28.6%) |
| 46-60 | 34 | 12.9% | 12 (35.3%) | 13 (38.2%) | 9 (26.5%) |
| 61-75 | 18 | 6.8% | 9 (50.0%) | 3 (16.7%) | 6 (33.3%) |
| 76-90 | 15 | 5.7% | 7 (46.7%) | 5 (33.3%) | 3 (20.0%) |
| 91-120 | 5 | 1.9% | 2 (40.0%) | 0 (0.0%) | 3 (60.0%) |

## 7. Goalless matches
- Overall: **18** of `264` (6.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 240 | 17 | 7.1% |
| 2026-2027 | 24 | 1 | 4.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\thai1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\thai1\charts\matches_analysis_home_win_rate.png)

