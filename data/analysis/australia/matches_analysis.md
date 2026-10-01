# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:43:49+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: A-League (Australia)
- Scope: league `australia`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 332 |
| Home wins | 121 (36.4%) |
| Draws | 87 (26.2%) |
| Away wins | 124 (37.3%) |
| Total goals | 1018 |
| Average goals per match | 3.066 |
| Goalless matches | 17 (5.1%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2024-2025 | 169 | 59 (34.9%) | 44 (26.0%) | 66 (39.1%) | 556 | 3.29 | 8 (4.7%) |
| 2025-2026 | 163 | 62 (38.0%) | 43 (26.4%) | 58 (35.6%) | 462 | 2.834 | 9 (5.5%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 70 (66.7%) | 25 (23.8%) | 10 (9.5%) | 105 |
| HT draw | 41 (30.4%) | 42 (31.1%) | 52 (38.5%) | 135 |
| HT away lead | 10 (10.9%) | 20 (21.7%) | 62 (67.4%) | 92 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (3.0%)
- Away comebacks (trailing at HT, won at FT): **10** (3.0%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2024-2025 | WS Wanderers | Melbourne Victory | 1-2 | 4-2 |
| 2024-2025 | Melbourne City | Brisbane Roar | 0-1 | 3-2 |
| 2024-2025 | Sydney FC | Newcastle Jets | 1-2 | 3-2 |
| 2025-2026 | Wellington Phoenix | Brisbane Roar | 0-1 | 2-1 |
| 2025-2026 | Melbourne City | Auckland FC | 0-1 | 2-1 |
| 2025-2026 | Perth Glory | Auckland FC | 0-1 | 2-1 |
| 2025-2026 | Central Coast Mariners | WS Wanderers | 0-1 | 3-2 |
| 2025-2026 | Newcastle Jets | WS Wanderers | 0-1 | 2-1 |
| 2025-2026 | Melbourne Victory | Central Coast Mariners | 0-1 | 4-1 |
| 2025-2026 | Adelaide United | Macarthur FC | 0-1 | 3-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2024-2025 | Macarthur FC | Newcastle Jets | 1-0 | 1-2 |
| 2024-2025 | Brisbane Roar | Adelaide United | 2-1 | 2-3 |
| 2024-2025 | Sydney FC | Western United | 2-1 | 3-4 |
| 2024-2025 | Adelaide United | WS Wanderers | 2-1 | 2-3 |
| 2024-2025 | Melbourne Victory | Western United | 2-1 | 3-4 |
| 2024-2025 | Macarthur FC | Wellington Phoenix | 1-0 | 1-2 |
| 2024-2025 | Adelaide United | Macarthur FC | 3-2 | 4-5 |
| 2025-2026 | Brisbane Roar | Adelaide United | 1-0 | 2-3 |
| 2025-2026 | Brisbane Roar | Melbourne City | 1-0 | 2-3 |
| 2025-2026 | Melbourne City | Adelaide United | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 105 | 70 (66.7%) | 25 (23.8%) | 10 (9.5%) |
| Away lead | 92 | 62 (67.4%) | 20 (21.7%) | 10 (10.9%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 41 | 30.4% |
| Draw | 42 | 31.1% |
| Away win | 52 | 38.5% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `315` of `332` (94.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 128 | 38.6% | 46 (35.9%) | 29 (22.7%) | 53 (41.4%) |
| 16-30 | 63 | 19.0% | 24 (38.1%) | 18 (28.6%) | 21 (33.3%) |
| 31-45 | 47 | 14.2% | 20 (42.6%) | 10 (21.3%) | 17 (36.2%) |
| 46-60 | 42 | 12.7% | 20 (47.6%) | 7 (16.7%) | 15 (35.7%) |
| 61-75 | 20 | 6.0% | 5 (25.0%) | 5 (25.0%) | 10 (50.0%) |
| 76-90 | 9 | 2.7% | 3 (33.3%) | 1 (11.1%) | 5 (55.6%) |
| 91-120 | 6 | 1.8% | 3 (50.0%) | 0 (0.0%) | 3 (50.0%) |

## 7. Goalless matches
- Overall: **17** of `332` (5.1%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2024-2025 | 169 | 8 | 4.7% |
| 2025-2026 | 163 | 9 | 5.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\australia\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\australia\charts\matches_analysis_home_win_rate.png)

