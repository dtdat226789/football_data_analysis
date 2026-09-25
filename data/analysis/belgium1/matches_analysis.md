# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:55:14+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Jupiler Pro League (Belgium)
- Scope: league `belgium1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 384 |
| Home wins | 164 (42.7%) |
| Draws | 93 (24.2%) |
| Away wins | 127 (33.1%) |
| Total goals | 1049 |
| Average goals per match | 2.732 |
| Goalless matches | 28 (7.3%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 321 | 132 (41.1%) | 81 (25.2%) | 108 (33.6%) | 864 | 2.692 | 25 (7.8%) |
| 2026-2027 | 63 | 32 (50.8%) | 12 (19.0%) | 19 (30.2%) | 185 | 2.937 | 3 (4.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 99 (79.2%) | 16 (12.8%) | 10 (8.0%) | 125 |
| HT draw | 56 (35.4%) | 56 (35.4%) | 46 (29.1%) | 158 |
| HT away lead | 9 (8.9%) | 21 (20.8%) | 71 (70.3%) | 101 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **9** (2.3%)
- Away comebacks (trailing at HT, won at FT): **10** (2.6%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Club Brugge KV | Genk | 0-1 | 2-1 |
| 2025-2026 | Gent | Anderlecht | 1-2 | 4-2 |
| 2025-2026 | Club Brugge KV | Waregem | 1-2 | 4-3 |
| 2025-2026 | Anderlecht | Gent | 0-1 | 3-1 |
| 2025-2026 | St. Liege | Leuven | 0-1 | 2-1 |
| 2025-2026 | RAAL La Louviere | Cercle Brugge KSV | 0-1 | 4-1 |
| 2025-2026 | Lommel SK | Dender | 0-1 | 3-2 |
| 2026-2027 | Waregem | Genk | 0-1 | 2-1 |
| 2026-2027 | Antwerp | Beveren | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Charleroi | Waregem | 1-0 | 1-2 |
| 2025-2026 | St. Truiden | Genk | 1-0 | 1-2 |
| 2025-2026 | KV Mechelen | St. Truiden | 1-0 | 1-3 |
| 2025-2026 | Cercle Brugge KSV | Leuven | 1-0 | 1-2 |
| 2025-2026 | Gent | St. Truiden | 1-0 | 1-2 |
| 2025-2026 | Club Brugge KV | RAAL La Louviere | 2-0 | 2-3 |
| 2025-2026 | Charleroi | Club Brugge KV | 1-0 | 1-2 |
| 2025-2026 | St. Truiden | Club Brugge KV | 1-0 | 1-2 |
| 2025-2026 | KV Mechelen | Anderlecht | 1-0 | 1-2 |
| 2025-2026 | Cercle Brugge KSV | Waregem | 1-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 125 | 99 (79.2%) | 16 (12.8%) | 10 (8.0%) |
| Away lead | 101 | 71 (70.3%) | 21 (20.8%) | 9 (8.9%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 56 | 35.4% |
| Draw | 56 | 35.4% |
| Away win | 46 | 29.1% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `356` of `384` (92.7%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 123 | 32.0% | 54 (43.9%) | 27 (22.0%) | 42 (34.1%) |
| 16-30 | 84 | 21.9% | 37 (44.0%) | 20 (23.8%) | 27 (32.1%) |
| 31-45 | 64 | 16.7% | 34 (53.1%) | 8 (12.5%) | 22 (34.4%) |
| 46-60 | 37 | 9.6% | 18 (48.6%) | 5 (13.5%) | 14 (37.8%) |
| 61-75 | 27 | 7.0% | 11 (40.7%) | 3 (11.1%) | 13 (48.1%) |
| 76-90 | 17 | 4.4% | 9 (52.9%) | 2 (11.8%) | 6 (35.3%) |
| 91-120 | 4 | 1.0% | 1 (25.0%) | 0 (0.0%) | 3 (75.0%) |

## 7. Goalless matches
- Overall: **28** of `384` (7.3%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 321 | 25 | 7.8% |
| 2026-2027 | 63 | 3 | 4.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\belgium1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\belgium1\charts\matches_analysis_home_win_rate.png)

