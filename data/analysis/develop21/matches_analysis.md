# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:57:18+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 34 |
| Home wins | 14 (41.2%) |
| Draws | 9 (26.5%) |
| Away wins | 11 (32.4%) |
| Total goals | 140 |
| Average goals per match | 4.118 |
| Goalless matches | 1 (2.9%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2026-2027 | 34 | 14 (41.2%) | 9 (26.5%) | 11 (32.4%) | 140 | 4.118 | 1 (2.9%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 10 (76.9%) | 2 (15.4%) | 1 (7.7%) | 13 |
| HT draw | 2 (22.2%) | 4 (44.4%) | 3 (33.3%) | 9 |
| HT away lead | 2 (16.7%) | 3 (25.0%) | 7 (58.3%) | 12 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **2** (5.9%)
- Away comebacks (trailing at HT, won at FT): **1** (2.9%)

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
| Home lead | 13 | 10 (76.9%) | 2 (15.4%) | 1 (7.7%) |
| Away lead | 12 | 7 (58.3%) | 3 (25.0%) | 2 (16.7%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 2 | 22.2% |
| Draw | 4 | 44.4% |
| Away win | 3 | 33.3% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `33` of `34` (97.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 12 | 35.3% | 6 (50.0%) | 2 (16.7%) | 4 (33.3%) |
| 16-30 | 13 | 38.2% | 7 (53.8%) | 2 (15.4%) | 4 (30.8%) |
| 31-45 | 5 | 14.7% | 0 (0.0%) | 3 (60.0%) | 2 (40.0%) |
| 46-60 | 1 | 2.9% | 0 (0.0%) | 1 (100.0%) | 0 (0.0%) |
| 61-75 | 2 | 5.9% | 1 (50.0%) | 0 (0.0%) | 1 (50.0%) |
| 76-90 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |
| 91-120 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |

## 7. Goalless matches
- Overall: **1** of `34` (2.9%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2026-2027 | 34 | 1 | 2.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\develop21\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\develop21\charts\matches_analysis_home_win_rate.png)

