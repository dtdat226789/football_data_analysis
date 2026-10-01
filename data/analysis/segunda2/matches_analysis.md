# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:07:00+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Segunda RFEF - Group 2 (Spain)
- Scope: league `segunda2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 342 |
| Home wins | 146 (42.7%) |
| Draws | 97 (28.4%) |
| Away wins | 99 (28.9%) |
| Total goals | 864 |
| Average goals per match | 2.526 |
| Goalless matches | 32 (9.4%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 130 (42.5%) | 89 (29.1%) | 87 (28.4%) | 769 | 2.513 | 28 (9.2%) |
| 2026-2027 | 36 | 16 (44.4%) | 8 (22.2%) | 12 (33.3%) | 95 | 2.639 | 4 (11.1%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 89 (80.9%) | 17 (15.5%) | 4 (3.6%) | 110 |
| HT draw | 45 (30.6%) | 65 (44.2%) | 37 (25.2%) | 147 |
| HT away lead | 12 (14.1%) | 15 (17.6%) | 58 (68.2%) | 85 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **12** (3.5%)
- Away comebacks (trailing at HT, won at FT): **4** (1.2%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Tudelano | Beasain | 0-1 | 3-1 |
| 2025-2026 | UD Logrones | Naxara | 0-1 | 2-1 |
| 2025-2026 | UD Logrones | Beasain | 0-1 | 2-1 |
| 2025-2026 | Tudelano | Naxara | 0-1 | 2-1 |
| 2025-2026 | Ejea | Amorebieta | 0-1 | 2-1 |
| 2025-2026 | SD Logrones | Ebro | 0-1 | 2-1 |
| 2025-2026 | Naxara | UD Logrones | 0-1 | 2-1 |
| 2025-2026 | Zaragoza B | Mutilvera | 0-2 | 3-2 |
| 2025-2026 | Beasain | Mutilvera | 1-2 | 3-2 |
| 2025-2026 | Ejea | R. Union | 1-2 | 3-2 |
| 2026-2027 | Girona B | Tudelano | 0-1 | 3-1 |
| 2026-2027 | Girona B | Osasuna B | 1-2 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Tudelano | Basconia | 1-0 | 1-2 |
| 2025-2026 | Amorebieta | Ebro | 1-0 | 1-2 |
| 2025-2026 | Amorebieta | Gernika | 1-0 | 1-2 |
| 2025-2026 | Mutilvera | Utebo FC | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 110 | 89 (80.9%) | 17 (15.5%) | 4 (3.6%) |
| Away lead | 85 | 58 (68.2%) | 15 (17.6%) | 12 (14.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 45 | 30.6% |
| Draw | 65 | 44.2% |
| Away win | 37 | 25.2% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `310` of `342` (90.6%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 98 | 28.7% | 48 (49.0%) | 16 (16.3%) | 34 (34.7%) |
| 16-30 | 70 | 20.5% | 35 (50.0%) | 17 (24.3%) | 18 (25.7%) |
| 31-45 | 57 | 16.7% | 27 (47.4%) | 12 (21.1%) | 18 (31.6%) |
| 46-60 | 38 | 11.1% | 18 (47.4%) | 9 (23.7%) | 11 (28.9%) |
| 61-75 | 26 | 7.6% | 10 (38.5%) | 8 (30.8%) | 8 (30.8%) |
| 76-90 | 14 | 4.1% | 5 (35.7%) | 2 (14.3%) | 7 (50.0%) |
| 91-120 | 7 | 2.0% | 3 (42.9%) | 1 (14.3%) | 3 (42.9%) |

## 7. Goalless matches
- Overall: **32** of `342` (9.4%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 306 | 28 | 9.2% |
| 2026-2027 | 36 | 4 | 11.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\segunda2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\segunda2\charts\matches_analysis_home_win_rate.png)

