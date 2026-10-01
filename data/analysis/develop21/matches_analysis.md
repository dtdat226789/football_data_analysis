# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:48:14+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 40 |
| Home wins | 18 (45.0%) |
| Draws | 10 (25.0%) |
| Away wins | 12 (30.0%) |
| Total goals | 164 |
| Average goals per match | 4.100 |
| Goalless matches | 1 (2.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2026-2027 | 40 | 18 (45.0%) | 10 (25.0%) | 12 (30.0%) | 164 | 4.1 | 1 (2.5%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 13 (81.2%) | 2 (12.5%) | 1 (6.2%) | 16 |
| HT draw | 3 (27.3%) | 5 (45.5%) | 3 (27.3%) | 11 |
| HT away lead | 2 (15.4%) | 3 (23.1%) | 8 (61.5%) | 13 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **2** (5.0%)
- Away comebacks (trailing at HT, won at FT): **1** (2.5%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2026-2027 | Bristol City U21 | Sheffield Utd U21 | 0-1 | 3-1 |
| 2026-2027 | Wigan U21 | Colchester U21 | 1-2 | 6-4 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2026-2027 | Millwall U21 | Huddersfield U21 | 2-0 | 2-4 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 16 | 13 (81.2%) | 2 (12.5%) | 1 (6.2%) |
| Away lead | 13 | 8 (61.5%) | 3 (23.1%) | 2 (15.4%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 3 | 27.3% |
| Draw | 5 | 45.5% |
| Away win | 3 | 27.3% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `39` of `40` (97.5%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 12 | 30.0% | 6 (50.0%) | 2 (16.7%) | 4 (33.3%) |
| 16-30 | 16 | 40.0% | 10 (62.5%) | 2 (12.5%) | 4 (25.0%) |
| 31-45 | 8 | 20.0% | 1 (12.5%) | 4 (50.0%) | 3 (37.5%) |
| 46-60 | 1 | 2.5% | 0 (0.0%) | 1 (100.0%) | 0 (0.0%) |
| 61-75 | 2 | 5.0% | 1 (50.0%) | 0 (0.0%) | 1 (50.0%) |
| 76-90 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |
| 91-120 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |

## 7. Goalless matches
- Overall: **1** of `40` (2.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2026-2027 | 40 | 1 | 2.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\develop21\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\develop21\charts\matches_analysis_home_win_rate.png)

