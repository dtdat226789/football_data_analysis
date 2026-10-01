# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:10:29+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Super Lig (Turkey)
- Scope: league `turkey1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 360 |
| Home wins | 155 (43.1%) |
| Draws | 100 (27.8%) |
| Away wins | 105 (29.2%) |
| Total goals | 973 |
| Average goals per match | 2.703 |
| Goalless matches | 30 (8.3%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 129 (42.2%) | 89 (29.1%) | 88 (28.8%) | 812 | 2.654 | 28 (9.2%) |
| 2026-2027 | 54 | 26 (48.1%) | 11 (20.4%) | 17 (31.5%) | 161 | 2.981 | 2 (3.7%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 97 (79.5%) | 16 (13.1%) | 9 (7.4%) | 122 |
| HT draw | 52 (34.4%) | 62 (41.1%) | 37 (24.5%) | 151 |
| HT away lead | 6 (6.9%) | 22 (25.3%) | 59 (67.8%) | 87 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **6** (1.7%)
- Away comebacks (trailing at HT, won at FT): **9** (2.5%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Samsunspor | Karagumruk | 0-1 | 3-2 |
| 2025-2026 | Galatasaray | Genclerbirligi | 0-1 | 3-2 |
| 2025-2026 | Fenerbahce | Samsunspor | 1-2 | 3-2 |
| 2025-2026 | Rizespor | Gaziantep | 0-1 | 2-1 |
| 2025-2026 | Galatasaray | Antalyaspor | 0-1 | 4-2 |
| 2025-2026 | Karagumruk | Alanyaspor | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Alanyaspor | Kasimpasa | 1-0 | 1-2 |
| 2025-2026 | Rizespor | Fenerbahce | 2-0 | 2-5 |
| 2025-2026 | Basaksehir | Trabzonspor | 2-1 | 3-4 |
| 2025-2026 | Antalyaspor | Goztepe | 1-0 | 1-2 |
| 2025-2026 | Alanyaspor | Fenerbahce | 2-1 | 2-3 |
| 2025-2026 | Alanyaspor | Eyupspor | 1-0 | 1-3 |
| 2025-2026 | Eyupspor | Samsunspor | 1-0 | 1-2 |
| 2026-2027 | Konyaspor | Kocaelispor | 1-0 | 1-2 |
| 2026-2027 | Genclerbirligi | Kasimpasa | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 122 | 97 (79.5%) | 16 (13.1%) | 9 (7.4%) |
| Away lead | 87 | 59 (67.8%) | 22 (25.3%) | 6 (6.9%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 52 | 34.4% |
| Draw | 62 | 41.1% |
| Away win | 37 | 24.5% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `330` of `360` (91.7%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 108 | 30.0% | 56 (51.9%) | 18 (16.7%) | 34 (31.5%) |
| 16-30 | 76 | 21.1% | 35 (46.1%) | 21 (27.6%) | 20 (26.3%) |
| 31-45 | 49 | 13.6% | 24 (49.0%) | 8 (16.3%) | 17 (34.7%) |
| 46-60 | 49 | 13.6% | 16 (32.7%) | 14 (28.6%) | 19 (38.8%) |
| 61-75 | 28 | 7.8% | 11 (39.3%) | 6 (21.4%) | 11 (39.3%) |
| 76-90 | 12 | 3.3% | 8 (66.7%) | 2 (16.7%) | 2 (16.7%) |
| 91-120 | 8 | 2.2% | 5 (62.5%) | 1 (12.5%) | 2 (25.0%) |

## 7. Goalless matches
- Overall: **30** of `360` (8.3%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 306 | 28 | 9.2% |
| 2026-2027 | 54 | 2 | 3.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\turkey1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\turkey1\charts\matches_analysis_home_win_rate.png)

