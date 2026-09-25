# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:42:45+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 419 |
| Home wins | 192 (45.8%) |
| Draws | 124 (29.6%) |
| Away wins | 103 (24.6%) |
| Total goals | 956 |
| Average goals per match | 2.282 |
| Goalless matches | 50 (11.9%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 173 (45.5%) | 113 (29.7%) | 94 (24.7%) | 856 | 2.253 | 46 (12.1%) |
| 2026-2027 | 39 | 19 (48.7%) | 11 (28.2%) | 9 (23.1%) | 100 | 2.564 | 4 (10.3%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 120 (87.6%) | 15 (10.9%) | 2 (1.5%) | 137 |
| HT draw | 62 (32.6%) | 86 (45.3%) | 42 (22.1%) | 190 |
| HT away lead | 10 (10.9%) | 23 (25.0%) | 59 (64.1%) | 92 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (2.4%)
- Away comebacks (trailing at HT, won at FT): **2** (0.5%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Tarazona | Villarreal B | 0-1 | 2-1 |
| 2025-2026 | Betis B | Alcorcon | 0-1 | 2-1 |
| 2025-2026 | Tarazona | Teruel | 1-2 | 3-2 |
| 2025-2026 | Sevilla FC B | Sanluqueno | 0-1 | 2-1 |
| 2025-2026 | Sabadell | Algeciras | 0-1 | 3-1 |
| 2025-2026 | Atl. Madrid B | Antequera | 0-1 | 3-2 |
| 2025-2026 | Atl. Madrid B | Marbella | 1-2 | 5-4 |
| 2025-2026 | Eldense | FC Cartagena SAD | 0-1 | 2-1 |
| 2025-2026 | Torremolinos | Atl. Madrid B | 0-1 | 3-1 |
| 2026-2027 | Murcia | CE Europa | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Tarazona | Atl. Madrid B | 1-0 | 1-4 |
| 2025-2026 | Teruel | Alcorcon | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 137 | 120 (87.6%) | 15 (10.9%) | 2 (1.5%) |
| Away lead | 92 | 59 (64.1%) | 23 (25.0%) | 10 (10.9%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 62 | 32.6% |
| Draw | 86 | 45.3% |
| Away win | 42 | 22.1% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `369` of `419` (88.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 112 | 26.7% | 62 (55.4%) | 27 (24.1%) | 23 (20.5%) |
| 16-30 | 85 | 20.3% | 43 (50.6%) | 18 (21.2%) | 24 (28.2%) |
| 31-45 | 67 | 16.0% | 34 (50.7%) | 14 (20.9%) | 19 (28.4%) |
| 46-60 | 49 | 11.7% | 26 (53.1%) | 7 (14.3%) | 16 (32.7%) |
| 61-75 | 33 | 7.9% | 13 (39.4%) | 6 (18.2%) | 14 (42.4%) |
| 76-90 | 17 | 4.1% | 9 (52.9%) | 2 (11.8%) | 6 (35.3%) |
| 91-120 | 6 | 1.4% | 5 (83.3%) | 0 (0.0%) | 1 (16.7%) |

## 7. Goalless matches
- Overall: **50** of `419` (11.9%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 380 | 46 | 12.1% |
| 2026-2027 | 39 | 4 | 10.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\primera2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\primera2\charts\matches_analysis_home_win_rate.png)

