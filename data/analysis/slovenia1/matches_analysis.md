# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:47:11+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Prva liga (Slovenia)
- Scope: league `slovenia1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 216 |
| Home wins | 99 (45.8%) |
| Draws | 46 (21.3%) |
| Away wins | 71 (32.9%) |
| Total goals | 635 |
| Average goals per match | 2.940 |
| Goalless matches | 14 (6.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 164 | 81 (49.4%) | 30 (18.3%) | 53 (32.3%) | 501 | 3.055 | 8 (4.9%) |
| 2026-2027 | 52 | 18 (34.6%) | 16 (30.8%) | 18 (34.6%) | 134 | 2.577 | 6 (11.5%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 70 (76.9%) | 11 (12.1%) | 10 (11.0%) | 91 |
| HT draw | 19 (34.5%) | 24 (43.6%) | 12 (21.8%) | 55 |
| HT away lead | 10 (14.5%) | 11 (15.9%) | 48 (69.6%) | 69 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (4.6%)
- Away comebacks (trailing at HT, won at FT): **10** (4.6%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Primorje | Domzale | 0-1 | 3-2 |
| 2025-2026 | Radomlje | O. Ljubljana | 0-2 | 3-2 |
| 2025-2026 | Aluminij | Celje | 0-1 | 2-1 |
| 2025-2026 | Bravo | Primorje | 0-1 | 2-1 |
| 2025-2026 | Bravo | Radomlje | 0-1 | 2-1 |
| 2025-2026 | Bravo | O. Ljubljana | 0-1 | 2-1 |
| 2026-2027 | Aluminij | Grosuplje | 1-2 | 4-2 |
| 2026-2027 | Maribor | Bravo | 0-1 | 3-1 |
| 2026-2027 | Bravo | Celje | 0-1 | 2-1 |
| 2026-2027 | Grosuplje | Radomlje | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Maribor | Celje | 1-0 | 1-2 |
| 2025-2026 | Bravo | Aluminij | 1-0 | 1-2 |
| 2025-2026 | Aluminij | Celje | 2-0 | 2-3 |
| 2025-2026 | O. Ljubljana | Koper | 1-0 | 1-3 |
| 2025-2026 | Primorje | Celje | 1-0 | 2-3 |
| 2025-2026 | Aluminij | Bravo | 1-0 | 1-3 |
| 2025-2026 | O. Ljubljana | Domzale | 1-0 | 1-2 |
| 2025-2026 | Maribor | Aluminij | 2-0 | 2-3 |
| 2025-2026 | Radomlje | O. Ljubljana | 1-0 | 1-2 |
| 2025-2026 | O. Ljubljana | Bravo | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 91 | 70 (76.9%) | 11 (12.1%) | 10 (11.0%) |
| Away lead | 69 | 48 (69.6%) | 11 (15.9%) | 10 (14.5%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 19 | 34.5% |
| Draw | 24 | 43.6% |
| Away win | 12 | 21.8% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `201` of `216` (93.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 77 | 35.6% | 35 (45.5%) | 9 (11.7%) | 33 (42.9%) |
| 16-30 | 63 | 29.2% | 33 (52.4%) | 10 (15.9%) | 20 (31.7%) |
| 31-45 | 32 | 14.8% | 18 (56.2%) | 6 (18.8%) | 8 (25.0%) |
| 46-60 | 15 | 6.9% | 4 (26.7%) | 6 (40.0%) | 5 (33.3%) |
| 61-75 | 8 | 3.7% | 6 (75.0%) | 1 (12.5%) | 1 (12.5%) |
| 76-90 | 2 | 0.9% | 1 (50.0%) | 0 (0.0%) | 1 (50.0%) |
| 91-120 | 4 | 1.9% | 2 (50.0%) | 0 (0.0%) | 2 (50.0%) |

## 7. Goalless matches
- Overall: **14** of `216` (6.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 164 | 8 | 4.9% |
| 2026-2027 | 52 | 6 | 11.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\slovenia1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\slovenia1\charts\matches_analysis_home_win_rate.png)

