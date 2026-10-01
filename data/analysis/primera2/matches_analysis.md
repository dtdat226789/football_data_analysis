# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:04:30+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 429 |
| Home wins | 194 (45.2%) |
| Draws | 126 (29.4%) |
| Away wins | 109 (25.4%) |
| Total goals | 979 |
| Average goals per match | 2.282 |
| Goalless matches | 50 (11.7%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 173 (45.5%) | 113 (29.7%) | 94 (24.7%) | 856 | 2.253 | 46 (12.1%) |
| 2026-2027 | 49 | 21 (42.9%) | 13 (26.5%) | 15 (30.6%) | 123 | 2.51 | 4 (8.2%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 120 (87.0%) | 16 (11.6%) | 2 (1.4%) | 138 |
| HT draw | 64 (32.5%) | 87 (44.2%) | 46 (23.4%) | 197 |
| HT away lead | 10 (10.6%) | 23 (24.5%) | 61 (64.9%) | 94 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (2.3%)
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
| Home lead | 138 | 120 (87.0%) | 16 (11.6%) | 2 (1.4%) |
| Away lead | 94 | 61 (64.9%) | 23 (24.5%) | 10 (10.6%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 64 | 32.5% |
| Draw | 87 | 44.2% |
| Away win | 46 | 23.4% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `379` of `429` (88.3%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 114 | 26.6% | 62 (54.4%) | 27 (23.7%) | 25 (21.9%) |
| 16-30 | 87 | 20.3% | 43 (49.4%) | 19 (21.8%) | 25 (28.7%) |
| 31-45 | 68 | 15.9% | 34 (50.0%) | 15 (22.1%) | 19 (27.9%) |
| 46-60 | 52 | 12.1% | 26 (50.0%) | 7 (13.5%) | 19 (36.5%) |
| 61-75 | 34 | 7.9% | 14 (41.2%) | 6 (17.6%) | 14 (41.2%) |
| 76-90 | 17 | 4.0% | 9 (52.9%) | 2 (11.8%) | 6 (35.3%) |
| 91-120 | 7 | 1.6% | 6 (85.7%) | 0 (0.0%) | 1 (14.3%) |

## 7. Goalless matches
- Overall: **50** of `429` (11.7%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 380 | 46 | 12.1% |
| 2026-2027 | 49 | 4 | 8.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\primera2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\primera2\charts\matches_analysis_home_win_rate.png)

