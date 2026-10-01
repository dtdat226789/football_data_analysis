# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:51:07+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: 2. Bundesliga (Germany)
- Scope: league `germany2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 364 |
| Home wins | 165 (45.3%) |
| Draws | 90 (24.7%) |
| Away wins | 109 (29.9%) |
| Total goals | 1082 |
| Average goals per match | 2.973 |
| Goalless matches | 19 (5.2%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 310 | 144 (46.5%) | 75 (24.2%) | 91 (29.4%) | 903 | 2.913 | 17 (5.5%) |
| 2026-2027 | 54 | 21 (38.9%) | 15 (27.8%) | 18 (33.3%) | 179 | 3.315 | 2 (3.7%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 89 (76.7%) | 23 (19.8%) | 4 (3.4%) | 116 |
| HT draw | 64 (43.0%) | 46 (30.9%) | 39 (26.2%) | 149 |
| HT away lead | 12 (12.1%) | 21 (21.2%) | 66 (66.7%) | 99 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **12** (3.3%)
- Away comebacks (trailing at HT, won at FT): **4** (1.1%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Darmstadt | Braunschweig | 0-1 | 2-1 |
| 2025-2026 | Hannover | Arminia Bielefeld | 0-1 | 3-1 |
| 2025-2026 | Paderborn | Arminia Bielefeld | 1-2 | 4-3 |
| 2025-2026 | Preussen Munster | Holstein Kiel | 0-1 | 2-1 |
| 2025-2026 | Nurnberg | Elversberg | 0-1 | 3-2 |
| 2025-2026 | Paderborn | Preussen Munster | 0-1 | 2-1 |
| 2025-2026 | Dusseldorf | Paderborn | 0-1 | 2-1 |
| 2025-2026 | Karlsruher SC | Greuther Furth | 0-1 | 3-1 |
| 2025-2026 | Paderborn | SG Dynamo Dresden | 0-1 | 2-1 |
| 2025-2026 | Arminia Bielefeld | Darmstadt | 0-1 | 2-1 |
| 2025-2026 | Arminia Bielefeld | Hertha Berlin | 0-1 | 6-1 |
| 2026-2027 | Heidenheim | SG Dynamo Dresden | 0-1 | 5-3 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Holstein Kiel | Hannover | 1-0 | 1-2 |
| 2025-2026 | Preussen Munster | Dusseldorf | 1-0 | 1-2 |
| 2025-2026 | Hannover | Darmstadt | 2-1 | 2-3 |
| 2025-2026 | SG Dynamo Dresden | Elversberg | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 116 | 89 (76.7%) | 23 (19.8%) | 4 (3.4%) |
| Away lead | 99 | 66 (66.7%) | 21 (21.2%) | 12 (12.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 64 | 43.0% |
| Draw | 46 | 30.9% |
| Away win | 39 | 26.2% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `345` of `364` (94.8%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 121 | 33.2% | 59 (48.8%) | 22 (18.2%) | 40 (33.1%) |
| 16-30 | 73 | 20.1% | 31 (42.5%) | 16 (21.9%) | 26 (35.6%) |
| 31-45 | 59 | 16.2% | 28 (47.5%) | 18 (30.5%) | 13 (22.0%) |
| 46-60 | 42 | 11.5% | 16 (38.1%) | 10 (23.8%) | 16 (38.1%) |
| 61-75 | 32 | 8.8% | 19 (59.4%) | 5 (15.6%) | 8 (25.0%) |
| 76-90 | 14 | 3.8% | 9 (64.3%) | 0 (0.0%) | 5 (35.7%) |
| 91-120 | 4 | 1.1% | 3 (75.0%) | 0 (0.0%) | 1 (25.0%) |

## 7. Goalless matches
- Overall: **19** of `364` (5.2%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 310 | 17 | 5.5% |
| 2026-2027 | 54 | 2 | 3.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\germany2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\germany2\charts\matches_analysis_home_win_rate.png)

