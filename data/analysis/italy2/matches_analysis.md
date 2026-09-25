# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:01:59+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Serie B (Italy)
- Scope: league `italy2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 440 |
| Home wins | 196 (44.5%) |
| Draws | 134 (30.5%) |
| Away wins | 110 (25.0%) |
| Total goals | 1125 |
| Average goals per match | 2.557 |
| Goalless matches | 31 (7.0%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 390 | 175 (44.9%) | 121 (31.0%) | 94 (24.1%) | 993 | 2.546 | 30 (7.7%) |
| 2026-2027 | 50 | 21 (42.0%) | 13 (26.0%) | 16 (32.0%) | 132 | 2.64 | 1 (2.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 105 (75.0%) | 23 (16.4%) | 12 (8.6%) | 140 |
| HT draw | 79 (40.5%) | 80 (41.0%) | 36 (18.5%) | 195 |
| HT away lead | 12 (11.4%) | 31 (29.5%) | 62 (59.0%) | 105 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **12** (2.7%)
- Away comebacks (trailing at HT, won at FT): **12** (2.7%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Padova | Entella | 0-1 | 2-1 |
| 2025-2026 | Modena | Pescara | 0-1 | 2-1 |
| 2025-2026 | Sampdoria | Pescara | 0-1 | 4-1 |
| 2025-2026 | Cesena | Mantova | 1-2 | 3-2 |
| 2025-2026 | Monza | Juve Stabia | 0-1 | 2-1 |
| 2025-2026 | Mantova | Sampdoria | 0-1 | 2-1 |
| 2025-2026 | Catanzaro | Empoli | 0-2 | 3-2 |
| 2025-2026 | Cesena | Catanzaro | 0-1 | 3-1 |
| 2025-2026 | Palermo | Catanzaro | 1-2 | 3-2 |
| 2026-2027 | Sampdoria | Catanzaro | 0-1 | 2-1 |
| 2026-2027 | Ascoli | Avellino | 0-1 | 3-1 |
| 2026-2027 | Modena | Empoli | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Sudtirol | Empoli | 1-0 | 1-2 |
| 2025-2026 | Mantova | Catanzaro | 1-0 | 1-3 |
| 2025-2026 | Modena | Catanzaro | 1-0 | 1-2 |
| 2025-2026 | Modena | Monza | 1-0 | 1-2 |
| 2025-2026 | Frosinone | Venezia | 1-0 | 1-2 |
| 2025-2026 | Empoli | Juve Stabia | 1-0 | 1-2 |
| 2025-2026 | Pescara | Sampdoria | 1-0 | 1-2 |
| 2025-2026 | Modena | Frosinone | 1-0 | 1-2 |
| 2026-2027 | Benevento | Modena | 1-0 | 1-2 |
| 2026-2027 | Avellino | Arezzo | 1-0 | 1-2 |
| 2026-2027 | Verona | Ascoli | 1-0 | 1-2 |
| 2026-2027 | Sampdoria | Juve Stabia | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 140 | 105 (75.0%) | 23 (16.4%) | 12 (8.6%) |
| Away lead | 105 | 62 (59.0%) | 31 (29.5%) | 12 (11.4%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 79 | 40.5% |
| Draw | 80 | 41.0% |
| Away win | 36 | 18.5% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `409` of `440` (93.0%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 113 | 25.7% | 59 (52.2%) | 29 (25.7%) | 25 (22.1%) |
| 16-30 | 101 | 23.0% | 46 (45.5%) | 30 (29.7%) | 25 (24.8%) |
| 31-45 | 79 | 18.0% | 32 (40.5%) | 19 (24.1%) | 28 (35.4%) |
| 46-60 | 65 | 14.8% | 33 (50.8%) | 16 (24.6%) | 16 (24.6%) |
| 61-75 | 23 | 5.2% | 7 (30.4%) | 6 (26.1%) | 10 (43.5%) |
| 76-90 | 25 | 5.7% | 17 (68.0%) | 3 (12.0%) | 5 (20.0%) |
| 91-120 | 3 | 0.7% | 2 (66.7%) | 0 (0.0%) | 1 (33.3%) |

## 7. Goalless matches
- Overall: **31** of `440` (7.0%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 390 | 30 | 7.7% |
| 2026-2027 | 50 | 1 | 2.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\italy2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\italy2\charts\matches_analysis_home_win_rate.png)

