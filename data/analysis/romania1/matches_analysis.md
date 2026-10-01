# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:04:44+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Superliga (Romania)
- Scope: league `romania1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 429 |
| Home wins | 199 (46.4%) |
| Draws | 117 (27.3%) |
| Away wins | 113 (26.3%) |
| Total goals | 1095 |
| Average goals per match | 2.552 |
| Goalless matches | 32 (7.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 350 | 155 (44.3%) | 96 (27.4%) | 99 (28.3%) | 887 | 2.534 | 25 (7.1%) |
| 2026-2027 | 79 | 44 (55.7%) | 21 (26.6%) | 14 (17.7%) | 208 | 2.633 | 7 (8.9%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 123 (82.0%) | 23 (15.3%) | 4 (2.7%) | 150 |
| HT draw | 65 (34.6%) | 73 (38.8%) | 50 (26.6%) | 188 |
| HT away lead | 11 (12.1%) | 21 (23.1%) | 59 (64.8%) | 91 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **11** (2.6%)
- Away comebacks (trailing at HT, won at FT): **4** (0.9%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Univ. Craiova | U. Cluj | 0-1 | 2-1 |
| 2025-2026 | Unirea Slobozia | Metaloglobus Bucharest | 0-1 | 2-1 |
| 2025-2026 | Metaloglobus Bucharest | FCSB | 0-1 | 2-1 |
| 2025-2026 | Petrolul | FC Arges | 0-1 | 2-1 |
| 2025-2026 | Univ. Craiova | Metaloglobus Bucharest | 0-1 | 2-1 |
| 2025-2026 | FC Botosani | Unirea Slobozia | 1-2 | 3-2 |
| 2025-2026 | FC Botosani | FCSB | 1-2 | 3-2 |
| 2025-2026 | Farul Constanta | Chindia Targoviste | 0-1 | 2-1 |
| 2026-2027 | U. Cluj | FC Botosani | 0-1 | 2-1 |
| 2026-2027 | Sepsi Sf. Gheorghe | CFR Cluj | 0-1 | 3-1 |
| 2026-2027 | FC Rapid Bucuresti | FC Voluntari | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | FCSB | Farul Constanta | 1-0 | 1-2 |
| 2025-2026 | FC Rapid Bucuresti | U. Cluj | 1-0 | 1-2 |
| 2025-2026 | Unirea Slobozia | Petrolul | 1-0 | 1-2 |
| 2025-2026 | Farul Constanta | FCSB | 1-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 150 | 123 (82.0%) | 23 (15.3%) | 4 (2.7%) |
| Away lead | 91 | 59 (64.8%) | 21 (23.1%) | 11 (12.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 65 | 34.6% |
| Draw | 73 | 38.8% |
| Away win | 50 | 26.6% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `397` of `429` (92.5%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 112 | 26.1% | 59 (52.7%) | 21 (18.8%) | 32 (28.6%) |
| 16-30 | 97 | 22.6% | 50 (51.5%) | 21 (21.6%) | 26 (26.8%) |
| 31-45 | 70 | 16.3% | 37 (52.9%) | 19 (27.1%) | 14 (20.0%) |
| 46-60 | 50 | 11.7% | 21 (42.0%) | 15 (30.0%) | 14 (28.0%) |
| 61-75 | 46 | 10.7% | 18 (39.1%) | 7 (15.2%) | 21 (45.7%) |
| 76-90 | 15 | 3.5% | 9 (60.0%) | 2 (13.3%) | 4 (26.7%) |
| 91-120 | 7 | 1.6% | 5 (71.4%) | 0 (0.0%) | 2 (28.6%) |

## 7. Goalless matches
- Overall: **32** of `429` (7.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 350 | 25 | 7.1% |
| 2026-2027 | 79 | 7 | 8.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\romania1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\romania1\charts\matches_analysis_home_win_rate.png)

