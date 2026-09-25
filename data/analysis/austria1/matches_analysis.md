# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:54:44+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Bundesliga (Austria)
- Scope: league `austria1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 237 |
| Home wins | 106 (44.7%) |
| Draws | 59 (24.9%) |
| Away wins | 72 (30.4%) |
| Total goals | 656 |
| Average goals per match | 2.768 |
| Goalless matches | 13 (5.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 195 | 84 (43.1%) | 50 (25.6%) | 61 (31.3%) | 527 | 2.703 | 12 (6.2%) |
| 2026-2027 | 42 | 22 (52.4%) | 9 (21.4%) | 11 (26.2%) | 129 | 3.071 | 1 (2.4%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 66 (83.5%) | 8 (10.1%) | 5 (6.3%) | 79 |
| HT draw | 34 (38.2%) | 37 (41.6%) | 18 (20.2%) | 89 |
| HT away lead | 6 (8.7%) | 14 (20.3%) | 49 (71.0%) | 69 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **6** (2.5%)
- Away comebacks (trailing at HT, won at FT): **5** (2.1%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Austria Vienna | Ried | 0-2 | 3-2 |
| 2025-2026 | SK Rapid | Sturm Graz | 0-1 | 2-1 |
| 2025-2026 | BW Linz | Ried | 0-2 | 3-2 |
| 2025-2026 | Ried | Altach | 0-1 | 3-2 |
| 2025-2026 | Tirol | Wolfsberger AC | 0-1 | 3-1 |
| 2025-2026 | LASK | SK Rapid | 0-1 | 3-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Wolfsberger AC | Ried | 1-0 | 1-2 |
| 2025-2026 | Salzburg | Tirol | 2-0 | 2-3 |
| 2025-2026 | Sturm Graz | Tirol | 1-0 | 1-3 |
| 2025-2026 | Hartberg | Salzburg | 1-0 | 1-2 |
| 2026-2027 | Wolfsberger AC | LASK | 1-0 | 1-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 79 | 66 (83.5%) | 8 (10.1%) | 5 (6.3%) |
| Away lead | 69 | 49 (71.0%) | 14 (20.3%) | 6 (8.7%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 34 | 38.2% |
| Draw | 37 | 41.6% |
| Away win | 18 | 20.2% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `224` of `237` (94.5%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 80 | 33.8% | 33 (41.2%) | 16 (20.0%) | 31 (38.8%) |
| 16-30 | 47 | 19.8% | 22 (46.8%) | 12 (25.5%) | 13 (27.7%) |
| 31-45 | 40 | 16.9% | 20 (50.0%) | 8 (20.0%) | 12 (30.0%) |
| 46-60 | 27 | 11.4% | 12 (44.4%) | 8 (29.6%) | 7 (25.9%) |
| 61-75 | 12 | 5.1% | 6 (50.0%) | 1 (8.3%) | 5 (41.7%) |
| 76-90 | 16 | 6.8% | 11 (68.8%) | 1 (6.2%) | 4 (25.0%) |
| 91-120 | 2 | 0.8% | 2 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **13** of `237` (5.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 195 | 12 | 6.2% |
| 2026-2027 | 42 | 1 | 2.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\austria1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\austria1\charts\matches_analysis_home_win_rate.png)

