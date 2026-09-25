# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:54:23+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Ligue 1 (Algeria)
- Scope: league `algir1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 262 |
| Home wins | 130 (49.6%) |
| Draws | 77 (29.4%) |
| Away wins | 55 (21.0%) |
| Total goals | 600 |
| Average goals per match | 2.290 |
| Goalless matches | 21 (8.0%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 240 | 120 (50.0%) | 70 (29.2%) | 50 (20.8%) | 544 | 2.267 | 20 (8.3%) |
| 2026-2027 | 22 | 10 (45.5%) | 7 (31.8%) | 5 (22.7%) | 56 | 2.545 | 1 (4.5%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 73 (83.0%) | 13 (14.8%) | 2 (2.3%) | 88 |
| HT draw | 51 (39.2%) | 55 (42.3%) | 24 (18.5%) | 130 |
| HT away lead | 6 (13.6%) | 9 (20.5%) | 29 (65.9%) | 44 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **6** (2.3%)
- Away comebacks (trailing at HT, won at FT): **2** (0.8%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | ES Setif | Constantine | 0-1 | 2-1 |
| 2025-2026 | Oran | Paradou | 0-1 | 3-1 |
| 2025-2026 | Olympique Akbou | Paradou | 1-2 | 4-3 |
| 2025-2026 | Oran | Khenchela | 0-1 | 2-1 |
| 2025-2026 | MC Alger | Khenchela | 0-1 | 2-1 |
| 2025-2026 | Oran | Rouisset | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Ben Aknoun | MC Alger | 1-0 | 2-3 |
| 2025-2026 | Kabylie | Oran | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 88 | 73 (83.0%) | 13 (14.8%) | 2 (2.3%) |
| Away lead | 44 | 29 (65.9%) | 9 (20.5%) | 6 (13.6%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 51 | 39.2% |
| Draw | 55 | 42.3% |
| Away win | 24 | 18.5% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `241` of `262` (92.0%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 65 | 24.8% | 36 (55.4%) | 17 (26.2%) | 12 (18.5%) |
| 16-30 | 64 | 24.4% | 35 (54.7%) | 11 (17.2%) | 18 (28.1%) |
| 31-45 | 31 | 11.8% | 17 (54.8%) | 9 (29.0%) | 5 (16.1%) |
| 46-60 | 33 | 12.6% | 14 (42.4%) | 12 (36.4%) | 7 (21.2%) |
| 61-75 | 23 | 8.8% | 13 (56.5%) | 5 (21.7%) | 5 (21.7%) |
| 76-90 | 20 | 7.6% | 13 (65.0%) | 1 (5.0%) | 6 (30.0%) |
| 91-120 | 5 | 1.9% | 2 (40.0%) | 1 (20.0%) | 2 (40.0%) |

## 7. Goalless matches
- Overall: **21** of `262` (8.0%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 240 | 20 | 8.3% |
| 2026-2027 | 22 | 1 | 4.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\algir1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\algir1\charts\matches_analysis_home_win_rate.png)

