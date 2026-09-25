# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:58:25+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Ykkosliiga (Finland)
- Scope: league `finland2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 255 |
| Home wins | 108 (42.4%) |
| Draws | 61 (23.9%) |
| Away wins | 86 (33.7%) |
| Total goals | 752 |
| Average goals per match | 2.949 |
| Goalless matches | 13 (5.1%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 135 | 58 (43.0%) | 35 (25.9%) | 42 (31.1%) | 443 | 3.281 | 5 (3.7%) |
| 2026 | 120 | 50 (41.7%) | 26 (21.7%) | 44 (36.7%) | 309 | 2.575 | 8 (6.7%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 69 (77.5%) | 12 (13.5%) | 8 (9.0%) | 89 |
| HT draw | 32 (33.3%) | 36 (37.5%) | 28 (29.2%) | 96 |
| HT away lead | 7 (10.0%) | 13 (18.6%) | 50 (71.4%) | 70 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (2.7%)
- Away comebacks (trailing at HT, won at FT): **8** (3.1%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | KaPa | SalPa | 0-1 | 3-1 |
| 2025 | TPS | SJK Akatemia | 1-2 | 3-2 |
| 2025 | Lahti | Jippo | 1-2 | 3-2 |
| 2025 | Jippo | Ekenas | 1-2 | 3-2 |
| 2026 | Haka | Jippo | 0-1 | 2-1 |
| 2026 | KTP | JaPS | 0-1 | 4-1 |
| 2026 | Jippo | Klubi 04 | 0-1 | 3-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Klubi 04 | JaPS | 2-1 | 4-6 |
| 2025 | TPS | PK-35 | 1-0 | 1-2 |
| 2025 | TPS | PK-35 | 1-0 | 1-3 |
| 2025 | Ekenas | SJK Akatemia | 1-0 | 2-3 |
| 2025 | Klubi 04 | TPS | 1-0 | 2-3 |
| 2026 | Ekenas | Jippo | 1-0 | 1-2 |
| 2026 | Mikkeli | Jippo | 1-0 | 1-3 |
| 2026 | SJK Akatemia | JaPS | 1-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 89 | 69 (77.5%) | 12 (13.5%) | 8 (9.0%) |
| Away lead | 70 | 50 (71.4%) | 13 (18.6%) | 7 (10.0%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 32 | 33.3% |
| Draw | 36 | 37.5% |
| Away win | 28 | 29.2% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `242` of `255` (94.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 92 | 36.1% | 42 (45.7%) | 15 (16.3%) | 35 (38.0%) |
| 16-30 | 56 | 22.0% | 28 (50.0%) | 8 (14.3%) | 20 (35.7%) |
| 31-45 | 32 | 12.5% | 15 (46.9%) | 8 (25.0%) | 9 (28.1%) |
| 46-60 | 32 | 12.5% | 12 (37.5%) | 7 (21.9%) | 13 (40.6%) |
| 61-75 | 19 | 7.5% | 5 (26.3%) | 8 (42.1%) | 6 (31.6%) |
| 76-90 | 7 | 2.7% | 3 (42.9%) | 2 (28.6%) | 2 (28.6%) |
| 91-120 | 4 | 1.6% | 3 (75.0%) | 0 (0.0%) | 1 (25.0%) |

## 7. Goalless matches
- Overall: **13** of `255` (5.1%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 135 | 5 | 3.7% |
| 2026 | 120 | 8 | 6.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\finland2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\finland2\charts\matches_analysis_home_win_rate.png)

