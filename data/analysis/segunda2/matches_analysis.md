# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:45:38+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Segunda RFEF - Group 2 (Spain)
- Scope: league `segunda2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 333 |
| Home wins | 142 (42.6%) |
| Draws | 96 (28.8%) |
| Away wins | 95 (28.5%) |
| Total goals | 842 |
| Average goals per match | 2.529 |
| Goalless matches | 31 (9.3%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 130 (42.5%) | 89 (29.1%) | 87 (28.4%) | 769 | 2.513 | 28 (9.2%) |
| 2026-2027 | 27 | 12 (44.4%) | 7 (25.9%) | 8 (29.6%) | 73 | 2.704 | 3 (11.1%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 86 (80.4%) | 17 (15.9%) | 4 (3.7%) | 107 |
| HT draw | 45 (31.2%) | 64 (44.4%) | 35 (24.3%) | 144 |
| HT away lead | 11 (13.4%) | 15 (18.3%) | 56 (68.3%) | 82 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **11** (3.3%)
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
| Home lead | 107 | 86 (80.4%) | 17 (15.9%) | 4 (3.7%) |
| Away lead | 82 | 56 (68.3%) | 15 (18.3%) | 11 (13.4%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 45 | 31.2% |
| Draw | 64 | 44.4% |
| Away win | 35 | 24.3% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `302` of `333` (90.7%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 95 | 28.5% | 46 (48.4%) | 16 (16.8%) | 33 (34.7%) |
| 16-30 | 67 | 20.1% | 33 (49.3%) | 17 (25.4%) | 17 (25.4%) |
| 31-45 | 57 | 17.1% | 27 (47.4%) | 12 (21.1%) | 18 (31.6%) |
| 46-60 | 38 | 11.4% | 18 (47.4%) | 9 (23.7%) | 11 (28.9%) |
| 61-75 | 25 | 7.5% | 10 (40.0%) | 8 (32.0%) | 7 (28.0%) |
| 76-90 | 14 | 4.2% | 5 (35.7%) | 2 (14.3%) | 7 (50.0%) |
| 91-120 | 6 | 1.8% | 3 (50.0%) | 1 (16.7%) | 2 (33.3%) |

## 7. Goalless matches
- Overall: **31** of `333` (9.3%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 306 | 28 | 9.2% |
| 2026-2027 | 27 | 3 | 11.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\segunda2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\segunda2\charts\matches_analysis_home_win_rate.png)

