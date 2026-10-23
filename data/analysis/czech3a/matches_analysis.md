# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:47:19+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: 3. CFL - Group A (Czech Republic)
- Scope: league `czech3a`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 337 |
| Home wins | 149 (44.2%) |
| Draws | 76 (22.6%) |
| Away wins | 112 (33.2%) |
| Total goals | 1085 |
| Average goals per match | 3.220 |
| Goalless matches | 24 (7.1%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 272 | 124 (45.6%) | 57 (21.0%) | 91 (33.5%) | 869 | 3.195 | 17 (6.2%) |
| 2026-2027 | 65 | 25 (38.5%) | 19 (29.2%) | 21 (32.3%) | 216 | 3.323 | 7 (10.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 87 (83.7%) | 13 (12.5%) | 4 (3.8%) | 104 |
| HT draw | 51 (37.8%) | 51 (37.8%) | 33 (24.4%) | 135 |
| HT away lead | 11 (11.3%) | 11 (11.3%) | 75 (77.3%) | 97 |
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
| Home lead | 104 | 87 (83.7%) | 13 (12.5%) | 4 (3.8%) |
| Away lead | 97 | 75 (77.3%) | 11 (11.3%) | 11 (11.3%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 51 | 37.8% |
| Draw | 51 | 37.8% |
| Away win | 33 | 24.4% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `313` of `337` (92.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 130 | 38.6% | 61 (46.9%) | 20 (15.4%) | 49 (37.7%) |
| 16-30 | 77 | 22.8% | 37 (48.1%) | 13 (16.9%) | 27 (35.1%) |
| 31-45 | 44 | 13.1% | 22 (50.0%) | 7 (15.9%) | 15 (34.1%) |
| 46-60 | 36 | 10.7% | 12 (33.3%) | 9 (25.0%) | 15 (41.7%) |
| 61-75 | 12 | 3.6% | 7 (58.3%) | 2 (16.7%) | 3 (25.0%) |
| 76-90 | 13 | 3.9% | 9 (69.2%) | 1 (7.7%) | 3 (23.1%) |
| 91-120 | 1 | 0.3% | 1 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **24** of `337` (7.1%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 272 | 17 | 6.2% |
| 2026-2027 | 65 | 7 | 10.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\czech3a\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\czech3a\charts\matches_analysis_home_win_rate.png)

