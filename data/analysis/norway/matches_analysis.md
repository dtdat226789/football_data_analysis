# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:04:04+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Eliteserien (Norway)
- Scope: league `norway`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 408 |
| Home wins | 204 (50.0%) |
| Draws | 78 (19.1%) |
| Away wins | 126 (30.9%) |
| Total goals | 1293 |
| Average goals per match | 3.169 |
| Goalless matches | 17 (4.2%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 240 | 118 (49.2%) | 45 (18.8%) | 77 (32.1%) | 762 | 3.175 | 11 (4.6%) |
| 2026 | 168 | 86 (51.2%) | 33 (19.6%) | 49 (29.2%) | 531 | 3.161 | 6 (3.6%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 143 (88.3%) | 10 (6.2%) | 9 (5.6%) | 162 |
| HT draw | 49 (37.7%) | 48 (36.9%) | 33 (25.4%) | 130 |
| HT away lead | 11 (9.6%) | 20 (17.4%) | 84 (73.0%) | 115 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **11** (2.7%)
- Away comebacks (trailing at HT, won at FT): **9** (2.2%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Brann | Tromso | 0-1 | 3-1 |
| 2025 | Viking | Kristiansund | 0-1 | 3-1 |
| 2025 | Brann | Bryne | 0-2 | 3-2 |
| 2025 | Tromso | Bodo/Glimt | 0-1 | 2-1 |
| 2025 | Sarpsborg 08 | Haugesund | 0-1 | 3-1 |
| 2025 | Fredrikstad | Molde | 0-1 | 4-2 |
| 2025 | Kristiansund | Molde | 0-1 | 2-1 |
| 2025 | Valerenga | Stromsgodset | 0-1 | 2-1 |
| 2026 | Viking | Start | 1-3 | 6-3 |
| 2026 | Fredrikstad | Start | 0-1 | 2-1 |
| 2026 | Viking | Aalesund | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Tromso | Kristiansund | 1-0 | 2-3 |
| 2025 | Stromsgodset | Brann | 1-0 | 1-2 |
| 2025 | Stromsgodset | Kristiansund | 1-0 | 1-2 |
| 2025 | Bodo/Glimt | Viking | 2-1 | 2-4 |
| 2025 | Valerenga | Molde | 2-1 | 2-3 |
| 2025 | Sandefjord | Viking | 1-0 | 1-2 |
| 2025 | Tromso | Brann | 1-0 | 1-2 |
| 2025 | HamKam | Stromsgodset | 1-0 | 1-2 |
| 2025 | Brann | Bodo/Glimt | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 162 | 143 (88.3%) | 10 (6.2%) | 9 (5.6%) |
| Away lead | 115 | 84 (73.0%) | 20 (17.4%) | 11 (9.6%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 49 | 37.7% |
| Draw | 48 | 36.9% |
| Away win | 33 | 25.4% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `390` of `408` (95.6%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 160 | 39.2% | 86 (53.8%) | 21 (13.1%) | 53 (33.1%) |
| 16-30 | 89 | 21.8% | 49 (55.1%) | 13 (14.6%) | 27 (30.3%) |
| 31-45 | 64 | 15.7% | 34 (53.1%) | 8 (12.5%) | 22 (34.4%) |
| 46-60 | 43 | 10.5% | 20 (46.5%) | 10 (23.3%) | 13 (30.2%) |
| 61-75 | 20 | 4.9% | 4 (20.0%) | 7 (35.0%) | 9 (45.0%) |
| 76-90 | 13 | 3.2% | 10 (76.9%) | 1 (7.7%) | 2 (15.4%) |
| 91-120 | 1 | 0.2% | 0 (0.0%) | 1 (100.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **17** of `408` (4.2%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 240 | 11 | 4.6% |
| 2026 | 168 | 6 | 3.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\norway\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\norway\charts\matches_analysis_home_win_rate.png)

