# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:58:27+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Serie C - Group B (Italy)
- Scope: league `italy3b`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 426 |
| Home wins | 167 (39.2%) |
| Draws | 133 (31.2%) |
| Away wins | 126 (29.6%) |
| Total goals | 979 |
| Average goals per match | 2.298 |
| Goalless matches | 41 (9.6%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 357 | 134 (37.5%) | 113 (31.7%) | 110 (30.8%) | 802 | 2.246 | 35 (9.8%) |
| 2026-2027 | 69 | 33 (47.8%) | 20 (29.0%) | 16 (23.2%) | 177 | 2.565 | 6 (8.7%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 92 (70.2%) | 30 (22.9%) | 9 (6.9%) | 131 |
| HT draw | 66 (34.2%) | 80 (41.5%) | 47 (24.4%) | 193 |
| HT away lead | 9 (8.8%) | 23 (22.5%) | 70 (68.6%) | 102 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **9** (2.1%)
- Away comebacks (trailing at HT, won at FT): **9** (2.1%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Ravenna | Perugia | 1-2 | 3-2 |
| 2025-2026 | Vis Pesaro | Guidonia | 0-1 | 2-1 |
| 2025-2026 | Perugia | Vis Pesaro | 0-1 | 2-1 |
| 2025-2026 | Ravenna | Pontedera | 0-1 | 2-1 |
| 2025-2026 | Campobasso | Pontedera | 0-1 | 3-2 |
| 2025-2026 | Campobasso | Juventus U23 | 0-1 | 2-1 |
| 2025-2026 | Ascoli | Vis Pesaro | 0-1 | 2-1 |
| 2026-2027 | Torres | Ostiamare | 0-1 | 3-2 |
| 2026-2027 | Livorno | Vado | 1-2 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Guidonia | Ravenna | 1-0 | 1-2 |
| 2025-2026 | Juventus U23 | Arezzo | 2-1 | 2-3 |
| 2025-2026 | Pianese | Arezzo | 2-0 | 2-4 |
| 2025-2026 | Forli | Campobasso | 2-0 | 2-3 |
| 2025-2026 | Forli | Arezzo | 1-0 | 1-2 |
| 2025-2026 | Bra | Ascoli | 1-0 | 1-3 |
| 2025-2026 | Vis Pesaro | Campobasso | 1-0 | 1-2 |
| 2025-2026 | Ternana | Pianese | 1-0 | 1-3 |
| 2026-2027 | Sambenedettese | Spezia | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 131 | 92 (70.2%) | 30 (22.9%) | 9 (6.9%) |
| Away lead | 102 | 70 (68.6%) | 23 (22.5%) | 9 (8.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 66 | 34.2% |
| Draw | 80 | 41.5% |
| Away win | 47 | 24.4% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `385` of `426` (90.4%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 98 | 23.0% | 39 (39.8%) | 25 (25.5%) | 34 (34.7%) |
| 16-30 | 89 | 20.9% | 42 (47.2%) | 20 (22.5%) | 27 (30.3%) |
| 31-45 | 76 | 17.8% | 26 (34.2%) | 26 (34.2%) | 24 (31.6%) |
| 46-60 | 59 | 13.8% | 31 (52.5%) | 11 (18.6%) | 17 (28.8%) |
| 61-75 | 40 | 9.4% | 20 (50.0%) | 7 (17.5%) | 13 (32.5%) |
| 76-90 | 16 | 3.8% | 5 (31.2%) | 3 (18.8%) | 8 (50.0%) |
| 91-120 | 7 | 1.6% | 4 (57.1%) | 0 (0.0%) | 3 (42.9%) |

## 7. Goalless matches
- Overall: **41** of `426` (9.6%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 357 | 35 | 9.8% |
| 2026-2027 | 69 | 6 | 8.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\italy3b\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\italy3b\charts\matches_analysis_home_win_rate.png)

