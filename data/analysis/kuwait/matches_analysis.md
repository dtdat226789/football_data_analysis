# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:00:51+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Premier League (Kuwait)
- Scope: league `kuwait`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 116 |
| Home wins | 48 (41.4%) |
| Draws | 29 (25.0%) |
| Away wins | 39 (33.6%) |
| Total goals | 311 |
| Average goals per match | 2.681 |
| Goalless matches | 8 (6.9%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 98 | 40 (40.8%) | 25 (25.5%) | 33 (33.7%) | 257 | 2.622 | 7 (7.1%) |
| 2026-2027 | 18 | 8 (44.4%) | 4 (22.2%) | 6 (33.3%) | 54 | 3.0 | 1 (5.6%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 33 (82.5%) | 7 (17.5%) | 0 (0.0%) | 40 |
| HT draw | 13 (30.2%) | 15 (34.9%) | 15 (34.9%) | 43 |
| HT away lead | 2 (6.1%) | 7 (21.2%) | 24 (72.7%) | 33 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **2** (1.7%)
- Away comebacks (trailing at HT, won at FT): **0** (0.0%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Kazma SC | Al Qadisiya | 1-2 | 4-2 |
| 2026-2027 | Al Jahra | Al Arabi | 0-1 | 2-1 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 40 | 33 (82.5%) | 7 (17.5%) | 0 (0.0%) |
| Away lead | 33 | 24 (72.7%) | 7 (21.2%) | 2 (6.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 13 | 30.2% |
| Draw | 15 | 34.9% |
| Away win | 15 | 34.9% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `108` of `116` (93.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 30 | 25.9% | 19 (63.3%) | 5 (16.7%) | 6 (20.0%) |
| 16-30 | 26 | 22.4% | 10 (38.5%) | 6 (23.1%) | 10 (38.5%) |
| 31-45 | 21 | 18.1% | 6 (28.6%) | 5 (23.8%) | 10 (47.6%) |
| 46-60 | 19 | 16.4% | 7 (36.8%) | 4 (21.1%) | 8 (42.1%) |
| 61-75 | 7 | 6.0% | 3 (42.9%) | 1 (14.3%) | 3 (42.9%) |
| 76-90 | 4 | 3.4% | 2 (50.0%) | 0 (0.0%) | 2 (50.0%) |
| 91-120 | 1 | 0.9% | 1 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **8** of `116` (6.9%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 98 | 7 | 7.1% |
| 2026-2027 | 18 | 1 | 5.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\kuwait\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\kuwait\charts\matches_analysis_home_win_rate.png)

