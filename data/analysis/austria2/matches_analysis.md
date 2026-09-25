# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:54:54+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: 2. Liga (Austria)
- Scope: league `austria2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 279 |
| Home wins | 121 (43.4%) |
| Draws | 66 (23.7%) |
| Away wins | 92 (33.0%) |
| Total goals | 784 |
| Average goals per match | 2.810 |
| Goalless matches | 19 (6.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 223 | 92 (41.3%) | 58 (26.0%) | 73 (32.7%) | 599 | 2.686 | 18 (8.1%) |
| 2026-2027 | 56 | 29 (51.8%) | 8 (14.3%) | 19 (33.9%) | 185 | 3.304 | 1 (1.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 80 (79.2%) | 17 (16.8%) | 4 (4.0%) | 101 |
| HT draw | 33 (33.0%) | 35 (35.0%) | 32 (32.0%) | 100 |
| HT away lead | 7 (9.1%) | 14 (18.2%) | 56 (72.7%) | 77 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (2.5%)
- Away comebacks (trailing at HT, won at FT): **4** (1.4%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | St. Polten | First Vienna | 0-1 | 2-1 |
| 2025-2026 | Liefering | A. Salzburg | 1-2 | 3-2 |
| 2025-2026 | Hertha Wels | SK Rapid II | 1-2 | 3-2 |
| 2025-2026 | St. Polten | A. Salzburg | 0-1 | 2-1 |
| 2025-2026 | A. Klagenfurt | SK Rapid II | 0-1 | 2-1 |
| 2026-2027 | BW Linz | Hertha Wels | 0-1 | 4-1 |
| 2026-2027 | St. Polten | Bregenz | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | A. Klagenfurt | St. Polten | 1-0 | 1-2 |
| 2025-2026 | SK Rapid II | A. Lustenau | 1-0 | 1-2 |
| 2025-2026 | A. Salzburg | Sturm Graz II | 1-0 | 1-2 |
| 2025-2026 | Liefering | Hertha Wels | 2-1 | 2-5 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 101 | 80 (79.2%) | 17 (16.8%) | 4 (4.0%) |
| Away lead | 77 | 56 (72.7%) | 14 (18.2%) | 7 (9.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 33 | 33.0% |
| Draw | 35 | 35.0% |
| Away win | 32 | 32.0% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `259` of `279` (92.8%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 95 | 34.1% | 42 (44.2%) | 20 (21.1%) | 33 (34.7%) |
| 16-30 | 68 | 24.4% | 36 (52.9%) | 9 (13.2%) | 23 (33.8%) |
| 31-45 | 41 | 14.7% | 20 (48.8%) | 10 (24.4%) | 11 (26.8%) |
| 46-60 | 26 | 9.3% | 8 (30.8%) | 6 (23.1%) | 12 (46.2%) |
| 61-75 | 13 | 4.7% | 4 (30.8%) | 2 (15.4%) | 7 (53.8%) |
| 76-90 | 11 | 3.9% | 8 (72.7%) | 0 (0.0%) | 3 (27.3%) |
| 91-120 | 5 | 1.8% | 2 (40.0%) | 0 (0.0%) | 3 (60.0%) |

## 7. Goalless matches
- Overall: **19** of `279` (6.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 223 | 18 | 8.1% |
| 2026-2027 | 56 | 1 | 1.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\austria2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\austria2\charts\matches_analysis_home_win_rate.png)

