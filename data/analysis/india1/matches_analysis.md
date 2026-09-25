# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:01:13+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: ISL (India)
- Scope: league `india1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 247 |
| Home wins | 101 (40.9%) |
| Draws | 67 (27.1%) |
| Away wins | 79 (32.0%) |
| Total goals | 669 |
| Average goals per match | 2.709 |
| Goalless matches | 21 (8.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2024-2025 | 156 | 66 (42.3%) | 38 (24.4%) | 52 (33.3%) | 448 | 2.872 | 11 (7.1%) |
| 2025-2026 | 91 | 35 (38.5%) | 29 (31.9%) | 27 (29.7%) | 221 | 2.429 | 10 (11.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 58 (70.7%) | 14 (17.1%) | 10 (12.2%) | 82 |
| HT draw | 35 (36.5%) | 41 (42.7%) | 20 (20.8%) | 96 |
| HT away lead | 8 (11.6%) | 12 (17.4%) | 49 (71.0%) | 69 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (3.2%)
- Away comebacks (trailing at HT, won at FT): **10** (4.0%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2024-2025 | Mohun Bagan | North East Utd | 1-2 | 3-2 |
| 2024-2025 | Punjab | Chennaiyin | 0-1 | 3-2 |
| 2024-2025 | East Bengal | Punjab | 0-2 | 4-2 |
| 2024-2025 | Jamshedpur | Bengaluru FC | 0-1 | 2-1 |
| 2024-2025 | Kerala Blasters | Odisha FC | 0-1 | 3-2 |
| 2024-2025 | Hyderabad | Jamshedpur | 1-2 | 3-2 |
| 2024-2025 | Odisha FC | Hyderabad | 0-1 | 3-1 |
| 2025-2026 | Punjab | Mohammedan | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2024-2025 | Odisha FC | Chennaiyin | 1-0 | 2-3 |
| 2024-2025 | Goa | Jamshedpur | 1-0 | 1-2 |
| 2024-2025 | Mohammedan | Kerala Blasters | 1-0 | 1-2 |
| 2024-2025 | Mohammedan | Bengaluru FC | 1-0 | 1-2 |
| 2024-2025 | Hyderabad | North East Utd | 2-1 | 2-5 |
| 2024-2025 | Punjab | Mohun Bagan | 1-0 | 1-3 |
| 2025-2026 | East Bengal | Jamshedpur | 1-0 | 1-2 |
| 2025-2026 | Bengaluru FC | Kerala Blasters | 1-0 | 1-2 |
| 2025-2026 | Mumbai City | East Bengal | 1-0 | 1-2 |
| 2025-2026 | Inter Kashi | East Bengal | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 82 | 58 (70.7%) | 14 (17.1%) | 10 (12.2%) |
| Away lead | 69 | 49 (71.0%) | 12 (17.4%) | 8 (11.6%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 35 | 36.5% |
| Draw | 41 | 42.7% |
| Away win | 20 | 20.8% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `226` of `247` (91.5%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 82 | 33.2% | 33 (40.2%) | 15 (18.3%) | 34 (41.5%) |
| 16-30 | 43 | 17.4% | 22 (51.2%) | 8 (18.6%) | 13 (30.2%) |
| 31-45 | 34 | 13.8% | 12 (35.3%) | 6 (17.6%) | 16 (47.1%) |
| 46-60 | 38 | 15.4% | 18 (47.4%) | 12 (31.6%) | 8 (21.1%) |
| 61-75 | 18 | 7.3% | 10 (55.6%) | 4 (22.2%) | 4 (22.2%) |
| 76-90 | 9 | 3.6% | 5 (55.6%) | 1 (11.1%) | 3 (33.3%) |
| 91-120 | 2 | 0.8% | 1 (50.0%) | 0 (0.0%) | 1 (50.0%) |

## 7. Goalless matches
- Overall: **21** of `247` (8.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2024-2025 | 156 | 11 | 7.1% |
| 2025-2026 | 91 | 10 | 11.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\india1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\india1\charts\matches_analysis_home_win_rate.png)

