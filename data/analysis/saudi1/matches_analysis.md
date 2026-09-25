# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:43:41+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Saudi Professional League (Saudi Arabia)
- Scope: league `saudi1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 377 |
| Home wins | 163 (43.2%) |
| Draws | 91 (24.1%) |
| Away wins | 123 (32.6%) |
| Total goals | 1117 |
| Average goals per match | 2.963 |
| Goalless matches | 26 (6.9%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 314 | 139 (44.3%) | 72 (22.9%) | 103 (32.8%) | 943 | 3.003 | 16 (5.1%) |
| 2026-2027 | 63 | 24 (38.1%) | 19 (30.2%) | 20 (31.7%) | 174 | 2.762 | 10 (15.9%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 102 (81.0%) | 19 (15.1%) | 5 (4.0%) | 126 |
| HT draw | 53 (35.8%) | 55 (37.2%) | 40 (27.0%) | 148 |
| HT away lead | 8 (7.8%) | 17 (16.5%) | 78 (75.7%) | 103 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (2.1%)
- Away comebacks (trailing at HT, won at FT): **5** (1.3%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Al Hazem | Al Najma | 0-2 | 3-2 |
| 2025-2026 | Al Hilal | Al Nassr | 0-1 | 3-1 |
| 2025-2026 | Al Ahli SC | Al Taawon | 0-1 | 2-1 |
| 2025-2026 | Al Ahli SC | Al Khaleej | 0-1 | 4-1 |
| 2025-2026 | Al Ahli SC | Al Najma | 0-1 | 4-1 |
| 2025-2026 | Al Riyadh | Al Ittihad | 0-1 | 3-1 |
| 2025-2026 | Al Qadsiah | Al Ahli SC | 0-2 | 3-2 |
| 2025-2026 | Al Hazem | Al Riyadh | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Neom SC | Al Hilal | 1-0 | 1-2 |
| 2025-2026 | Al Kholood | Al Ettifaq | 1-0 | 1-2 |
| 2025-2026 | Al Fayha | Al Nassr | 1-0 | 1-3 |
| 2025-2026 | Al Ettifaq | Al Riyadh | 2-1 | 2-3 |
| 2026-2027 | Al Ettifaq | Al Nassr | 2-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 126 | 102 (81.0%) | 19 (15.1%) | 5 (4.0%) |
| Away lead | 103 | 78 (75.7%) | 17 (16.5%) | 8 (7.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 53 | 35.8% |
| Draw | 55 | 37.2% |
| Away win | 40 | 27.0% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `351` of `377` (93.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 132 | 35.0% | 58 (43.9%) | 21 (15.9%) | 53 (40.2%) |
| 16-30 | 85 | 22.5% | 46 (54.1%) | 18 (21.2%) | 21 (24.7%) |
| 31-45 | 55 | 14.6% | 23 (41.8%) | 14 (25.5%) | 18 (32.7%) |
| 46-60 | 48 | 12.7% | 20 (41.7%) | 7 (14.6%) | 21 (43.8%) |
| 61-75 | 14 | 3.7% | 8 (57.1%) | 2 (14.3%) | 4 (28.6%) |
| 76-90 | 12 | 3.2% | 6 (50.0%) | 1 (8.3%) | 5 (41.7%) |
| 91-120 | 5 | 1.3% | 2 (40.0%) | 2 (40.0%) | 1 (20.0%) |

## 7. Goalless matches
- Overall: **26** of `377` (6.9%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 314 | 16 | 5.1% |
| 2026-2027 | 63 | 10 | 15.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\saudi1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\saudi1\charts\matches_analysis_home_win_rate.png)

