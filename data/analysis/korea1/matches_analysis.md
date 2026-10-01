# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:59:57+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: K League 1 (South Korea)
- Scope: league `korea1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 378 |
| Home wins | 137 (36.2%) |
| Draws | 113 (29.9%) |
| Away wins | 128 (33.9%) |
| Total goals | 952 |
| Average goals per match | 2.519 |
| Goalless matches | 37 (9.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 198 | 83 (41.9%) | 52 (26.3%) | 63 (31.8%) | 512 | 2.586 | 16 (8.1%) |
| 2026 | 180 | 54 (30.0%) | 61 (33.9%) | 65 (36.1%) | 440 | 2.444 | 21 (11.7%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 72 (79.1%) | 15 (16.5%) | 4 (4.4%) | 91 |
| HT draw | 53 (29.1%) | 75 (41.2%) | 54 (29.7%) | 182 |
| HT away lead | 12 (11.4%) | 23 (21.9%) | 70 (66.7%) | 105 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **12** (3.2%)
- Away comebacks (trailing at HT, won at FT): **4** (1.1%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Daegu | Gangwon | 0-1 | 2-1 |
| 2025 | Gangwon | Pohang | 0-1 | 2-1 |
| 2025 | Gwangju FC | Anyang | 0-1 | 2-1 |
| 2025 | Pohang | Anyang | 0-1 | 2-1 |
| 2025 | Ulsan HD | Gimcheon Sangmu | 0-1 | 3-2 |
| 2025 | Jeju SK | Daegu | 0-1 | 2-1 |
| 2025 | Jeonbuk | Suwon FC | 0-2 | 3-2 |
| 2025 | Daejeon | Suwon FC | 1-2 | 3-2 |
| 2025 | Daegu | Suwon FC | 0-1 | 3-1 |
| 2026 | Jeju SK | Pohang | 0-1 | 2-1 |
| 2026 | Seoul | Daejeon | 0-1 | 4-2 |
| 2026 | Daejeon | Anyang | 0-1 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Jeju SK | Gimcheon Sangmu | 1-0 | 2-3 |
| 2025 | Suwon FC | Anyang | 1-0 | 1-2 |
| 2025 | Daegu | Gimcheon Sangmu | 2-1 | 2-3 |
| 2025 | Pohang | Jeonbuk | 2-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 91 | 72 (79.1%) | 15 (16.5%) | 4 (4.4%) |
| Away lead | 105 | 70 (66.7%) | 23 (21.9%) | 12 (11.4%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 53 | 29.1% |
| Draw | 75 | 41.2% |
| Away win | 54 | 29.7% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `341` of `378` (90.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 92 | 24.3% | 36 (39.1%) | 22 (23.9%) | 34 (37.0%) |
| 16-30 | 75 | 19.8% | 34 (45.3%) | 10 (13.3%) | 31 (41.3%) |
| 31-45 | 67 | 17.7% | 25 (37.3%) | 17 (25.4%) | 25 (37.3%) |
| 46-60 | 46 | 12.2% | 15 (32.6%) | 15 (32.6%) | 16 (34.8%) |
| 61-75 | 33 | 8.7% | 13 (39.4%) | 7 (21.2%) | 13 (39.4%) |
| 76-90 | 21 | 5.6% | 12 (57.1%) | 5 (23.8%) | 4 (19.0%) |
| 91-120 | 7 | 1.9% | 2 (28.6%) | 0 (0.0%) | 5 (71.4%) |

## 7. Goalless matches
- Overall: **37** of `378` (9.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 198 | 16 | 8.1% |
| 2026 | 180 | 21 | 11.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\korea1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\korea1\charts\matches_analysis_home_win_rate.png)

