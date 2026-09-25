# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:56:36+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: 3. CFL - Group A (Czech Republic)
- Scope: league `czech3a`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 330 |
| Home wins | 147 (44.5%) |
| Draws | 74 (22.4%) |
| Away wins | 109 (33.0%) |
| Total goals | 1056 |
| Average goals per match | 3.200 |
| Goalless matches | 24 (7.3%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 272 | 124 (45.6%) | 57 (21.0%) | 91 (33.5%) | 869 | 3.195 | 17 (6.2%) |
| 2026-2027 | 58 | 23 (39.7%) | 17 (29.3%) | 18 (31.0%) | 187 | 3.224 | 7 (12.1%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 85 (83.3%) | 13 (12.7%) | 4 (3.9%) | 102 |
| HT draw | 51 (38.1%) | 51 (38.1%) | 32 (23.9%) | 134 |
| HT away lead | 11 (11.8%) | 9 (9.7%) | 73 (78.5%) | 93 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **11** (3.3%)
- Away comebacks (trailing at HT, won at FT): **4** (1.2%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | SK Kladno | Pribram B | 1-2 | 5-2 |
| 2025-2026 | Pisek | Domazlice | 0-1 | 3-1 |
| 2025-2026 | Pribram B | Aritma Prague | 0-1 | 3-2 |
| 2025-2026 | Plzen B | Domazlice | 0-1 | 2-1 |
| 2025-2026 | Slavia Prague U20 | SK Kladno | 0-1 | 2-1 |
| 2025-2026 | Aritma Prague | Loko Praha | 0-1 | 3-1 |
| 2025-2026 | Aritma Prague | Dukla Prague B | 0-1 | 2-1 |
| 2025-2026 | Domazlice | Pisek | 1-2 | 3-2 |
| 2025-2026 | Domazlice | Slavia Prague U20 | 1-2 | 4-3 |
| 2025-2026 | Pisek | Kraluv Dvur | 0-1 | 3-1 |
| 2026-2027 | Domazlice | Motorlet Prague | 0-1 | 5-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Petrin Plzen | Plzen B | 3-0 | 3-4 |
| 2025-2026 | Taborsko akademie | Dukla Prague B | 1-0 | 1-2 |
| 2025-2026 | Loko Praha | Bohemians 1905 B | 1-0 | 1-2 |
| 2025-2026 | Dukla Prague B | Taborsko akademie | 1-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 102 | 85 (83.3%) | 13 (12.7%) | 4 (3.9%) |
| Away lead | 93 | 73 (78.5%) | 9 (9.7%) | 11 (11.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 51 | 38.1% |
| Draw | 51 | 38.1% |
| Away win | 32 | 23.9% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `306` of `330` (92.7%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 127 | 38.5% | 61 (48.0%) | 19 (15.0%) | 47 (37.0%) |
| 16-30 | 73 | 22.1% | 35 (47.9%) | 12 (16.4%) | 26 (35.6%) |
| 31-45 | 44 | 13.3% | 22 (50.0%) | 7 (15.9%) | 15 (34.1%) |
| 46-60 | 36 | 10.9% | 12 (33.3%) | 9 (25.0%) | 15 (41.7%) |
| 61-75 | 12 | 3.6% | 7 (58.3%) | 2 (16.7%) | 3 (25.0%) |
| 76-90 | 13 | 3.9% | 9 (69.2%) | 1 (7.7%) | 3 (23.1%) |
| 91-120 | 1 | 0.3% | 1 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **24** of `330` (7.3%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 272 | 17 | 6.2% |
| 2026-2027 | 58 | 7 | 12.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\czech3a\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\czech3a\charts\matches_analysis_home_win_rate.png)

