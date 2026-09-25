# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:02:18+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Serie C - Group B (Italy)
- Scope: league `italy3b`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 417 |
| Home wins | 163 (39.1%) |
| Draws | 131 (31.4%) |
| Away wins | 123 (29.5%) |
| Total goals | 956 |
| Average goals per match | 2.293 |
| Goalless matches | 40 (9.6%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 357 | 134 (37.5%) | 113 (31.7%) | 110 (30.8%) | 802 | 2.246 | 35 (9.8%) |
| 2026-2027 | 60 | 29 (48.3%) | 18 (30.0%) | 13 (21.7%) | 154 | 2.567 | 5 (8.3%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 88 (69.3%) | 30 (23.6%) | 9 (7.1%) | 127 |
| HT draw | 66 (34.7%) | 78 (41.1%) | 46 (24.2%) | 190 |
| HT away lead | 9 (9.0%) | 23 (23.0%) | 68 (68.0%) | 100 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **9** (2.2%)
- Away comebacks (trailing at HT, won at FT): **9** (2.2%)

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
| Home lead | 127 | 88 (69.3%) | 30 (23.6%) | 9 (7.1%) |
| Away lead | 100 | 68 (68.0%) | 23 (23.0%) | 9 (9.0%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 66 | 34.7% |
| Draw | 78 | 41.1% |
| Away win | 46 | 24.2% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `377` of `417` (90.4%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 94 | 22.5% | 36 (38.3%) | 25 (26.6%) | 33 (35.1%) |
| 16-30 | 88 | 21.1% | 41 (46.6%) | 20 (22.7%) | 27 (30.7%) |
| 31-45 | 76 | 18.2% | 26 (34.2%) | 26 (34.2%) | 24 (31.6%) |
| 46-60 | 57 | 13.7% | 31 (54.4%) | 11 (19.3%) | 15 (26.3%) |
| 61-75 | 39 | 9.4% | 20 (51.3%) | 6 (15.4%) | 13 (33.3%) |
| 76-90 | 16 | 3.8% | 5 (31.2%) | 3 (18.8%) | 8 (50.0%) |
| 91-120 | 7 | 1.7% | 4 (57.1%) | 0 (0.0%) | 3 (42.9%) |

## 7. Goalless matches
- Overall: **40** of `417` (9.6%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 357 | 35 | 9.8% |
| 2026-2027 | 60 | 5 | 8.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\italy3b\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\italy3b\charts\matches_analysis_home_win_rate.png)

