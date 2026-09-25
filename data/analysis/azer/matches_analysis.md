# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:55:04+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Premier League (Azerbaijan)
- Scope: league `azer`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 234 |
| Home wins | 93 (39.7%) |
| Draws | 56 (23.9%) |
| Away wins | 85 (36.3%) |
| Total goals | 600 |
| Average goals per match | 2.564 |
| Goalless matches | 21 (9.0%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 200 | 75 (37.5%) | 49 (24.5%) | 76 (38.0%) | 515 | 2.575 | 18 (9.0%) |
| 2026-2027 | 34 | 18 (52.9%) | 7 (20.6%) | 9 (26.5%) | 85 | 2.5 | 3 (8.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 57 (81.4%) | 10 (14.3%) | 3 (4.3%) | 70 |
| HT draw | 32 (30.5%) | 38 (36.2%) | 35 (33.3%) | 105 |
| HT away lead | 4 (7.0%) | 7 (12.3%) | 46 (80.7%) | 57 |
- *2 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **4** (1.7%)
- Away comebacks (trailing at HT, won at FT): **3** (1.3%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Zira | Shamakhi | 0-1 | 2-1 |
| 2025-2026 | Araz | Karvan | 0-1 | 2-1 |
| 2025-2026 | Shamakhi | Zira | 0-1 | 2-1 |
| 2025-2026 | Sabah Baku | Qarabag | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Turan Tovuz | Qarabag | 1-0 | 1-2 |
| 2025-2026 | Karvan | Zira | 1-0 | 2-3 |
| 2025-2026 | Karvan | Neftci Baku | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 70 | 57 (81.4%) | 10 (14.3%) | 3 (4.3%) |
| Away lead | 57 | 46 (80.7%) | 7 (12.3%) | 4 (7.0%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 32 | 30.5% |
| Draw | 38 | 36.2% |
| Away win | 35 | 33.3% |
- *2 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `212` of `234` (90.6%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 58 | 24.8% | 29 (50.0%) | 4 (6.9%) | 25 (43.1%) |
| 16-30 | 42 | 17.9% | 14 (33.3%) | 14 (33.3%) | 14 (33.3%) |
| 31-45 | 43 | 18.4% | 21 (48.8%) | 6 (14.0%) | 16 (37.2%) |
| 46-60 | 38 | 16.2% | 18 (47.4%) | 7 (18.4%) | 13 (34.2%) |
| 61-75 | 20 | 8.5% | 5 (25.0%) | 4 (20.0%) | 11 (55.0%) |
| 76-90 | 9 | 3.8% | 5 (55.6%) | 0 (0.0%) | 4 (44.4%) |
| 91-120 | 2 | 0.9% | 1 (50.0%) | 0 (0.0%) | 1 (50.0%) |

## 7. Goalless matches
- Overall: **21** of `234` (9.0%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 200 | 18 | 9.0% |
| 2026-2027 | 34 | 3 | 8.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\azer\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\azer\charts\matches_analysis_home_win_rate.png)

