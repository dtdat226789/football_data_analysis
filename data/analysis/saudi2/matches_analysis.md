# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:05:30+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Division 1 (Saudi Arabia)
- Scope: league `saudi2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 362 |
| Home wins | 144 (39.8%) |
| Draws | 96 (26.5%) |
| Away wins | 122 (33.7%) |
| Total goals | 1029 |
| Average goals per match | 2.843 |
| Goalless matches | 27 (7.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 309 | 128 (41.4%) | 72 (23.3%) | 109 (35.3%) | 917 | 2.968 | 16 (5.2%) |
| 2026-2027 | 53 | 16 (30.2%) | 24 (45.3%) | 13 (24.5%) | 112 | 2.113 | 11 (20.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 82 (73.2%) | 19 (17.0%) | 11 (9.8%) | 112 |
| HT draw | 53 (37.6%) | 49 (34.8%) | 39 (27.7%) | 141 |
| HT away lead | 8 (7.5%) | 28 (26.2%) | 71 (66.4%) | 107 |
- *2 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (2.2%)
- Away comebacks (trailing at HT, won at FT): **11** (3.0%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Al Jandal | Al Batin | 0-1 | 2-1 |
| 2025-2026 | Al Raed | Al Wehda | 0-1 | 2-1 |
| 2025-2026 | Al Raed | Al-Ula | 0-1 | 3-2 |
| 2025-2026 | Al Jabalain | Al Batin | 0-1 | 4-1 |
| 2025-2026 | Al Raed | Al Adalah | 2-3 | 6-3 |
| 2025-2026 | Al Jabalain | Al Bukiryah | 0-1 | 2-1 |
| 2025-2026 | Al Arabi | Al Jubail | 1-2 | 4-3 |
| 2025-2026 | Al Diriyah | Al-Ula | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Abha | Al Orubah | 1-0 | 2-3 |
| 2025-2026 | Al Batin | Al Zulfi | 1-0 | 1-2 |
| 2025-2026 | Al Wehda | Abha | 1-0 | 2-3 |
| 2025-2026 | Al Batin | Al Diriyah | 1-0 | 1-2 |
| 2025-2026 | Al Bukiryah | Al Taee | 1-0 | 1-2 |
| 2025-2026 | Al Zulfi | Al Orubah | 1-0 | 1-2 |
| 2025-2026 | Al Zulfi | Jeddah | 1-0 | 1-2 |
| 2025-2026 | Al Orubah | Abha | 1-0 | 1-2 |
| 2025-2026 | Al Jandal | Al-Ula | 1-0 | 1-2 |
| 2025-2026 | Al Raed | Al-Faisaly | 1-0 | 1-2 |
| 2025-2026 | Al Jabalain | Al Adalah | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 112 | 82 (73.2%) | 19 (17.0%) | 11 (9.8%) |
| Away lead | 107 | 71 (66.4%) | 28 (26.2%) | 8 (7.5%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 53 | 37.6% |
| Draw | 49 | 34.8% |
| Away win | 39 | 27.7% |
- *2 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `333` of `362` (92.0%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 101 | 27.9% | 52 (51.5%) | 17 (16.8%) | 32 (31.7%) |
| 16-30 | 80 | 22.1% | 31 (38.8%) | 19 (23.8%) | 30 (37.5%) |
| 31-45 | 65 | 18.0% | 24 (36.9%) | 15 (23.1%) | 26 (40.0%) |
| 46-60 | 48 | 13.3% | 18 (37.5%) | 13 (27.1%) | 17 (35.4%) |
| 61-75 | 18 | 5.0% | 8 (44.4%) | 3 (16.7%) | 7 (38.9%) |
| 76-90 | 16 | 4.4% | 6 (37.5%) | 2 (12.5%) | 8 (50.0%) |
| 91-120 | 5 | 1.4% | 4 (80.0%) | 0 (0.0%) | 1 (20.0%) |

## 7. Goalless matches
- Overall: **27** of `362` (7.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 309 | 16 | 5.2% |
| 2026-2027 | 53 | 11 | 20.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\saudi2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\saudi2\charts\matches_analysis_home_win_rate.png)

