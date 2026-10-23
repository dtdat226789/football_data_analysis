# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:49:43+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Ykkosliiga (Finland)
- Scope: league `finland2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 260 |
| Home wins | 110 (42.3%) |
| Draws | 64 (24.6%) |
| Away wins | 86 (33.1%) |
| Total goals | 764 |
| Average goals per match | 2.938 |
| Goalless matches | 14 (5.4%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 135 | 58 (43.0%) | 35 (25.9%) | 42 (31.1%) | 443 | 3.281 | 5 (3.7%) |
| 2026 | 125 | 52 (41.6%) | 29 (23.2%) | 44 (35.2%) | 321 | 2.568 | 9 (7.2%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 70 (76.9%) | 13 (14.3%) | 8 (8.8%) | 91 |
| HT draw | 32 (33.0%) | 37 (38.1%) | 28 (28.9%) | 97 |
| HT away lead | 8 (11.1%) | 14 (19.4%) | 50 (69.4%) | 72 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (3.1%)
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
| 2026 | KaPa | Haka | 0-2 | 3-2 |

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
| Home lead | 91 | 70 (76.9%) | 13 (14.3%) | 8 (8.8%) |
| Away lead | 72 | 50 (69.4%) | 14 (19.4%) | 8 (11.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 32 | 33.0% |
| Draw | 37 | 38.1% |
| Away win | 28 | 28.9% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `246` of `260` (94.6%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 93 | 35.8% | 42 (45.2%) | 16 (17.2%) | 35 (37.6%) |
| 16-30 | 59 | 22.7% | 30 (50.8%) | 9 (15.3%) | 20 (33.9%) |
| 31-45 | 32 | 12.3% | 15 (46.9%) | 8 (25.0%) | 9 (28.1%) |
| 46-60 | 32 | 12.3% | 12 (37.5%) | 7 (21.9%) | 13 (40.6%) |
| 61-75 | 19 | 7.3% | 5 (26.3%) | 8 (42.1%) | 6 (31.6%) |
| 76-90 | 7 | 2.7% | 3 (42.9%) | 2 (28.6%) | 2 (28.6%) |
| 91-120 | 4 | 1.5% | 3 (75.0%) | 0 (0.0%) | 1 (25.0%) |

## 7. Goalless matches
- Overall: **14** of `260` (5.4%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 135 | 5 | 3.7% |
| 2026 | 125 | 9 | 7.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\finland2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\finland2\charts\matches_analysis_home_win_rate.png)

