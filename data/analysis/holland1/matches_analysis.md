# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:52:28+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Eredivisie (Netherlands)
- Scope: league `holland1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 384 |
| Home wins | 162 (42.2%) |
| Draws | 100 (26.0%) |
| Away wins | 122 (31.8%) |
| Total goals | 1256 |
| Average goals per match | 3.271 |
| Goalless matches | 11 (2.9%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 321 | 143 (44.5%) | 83 (25.9%) | 95 (29.6%) | 1016 | 3.165 | 10 (3.1%) |
| 2026-2027 | 63 | 19 (30.2%) | 17 (27.0%) | 27 (42.9%) | 240 | 3.81 | 1 (1.6%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 114 (77.0%) | 25 (16.9%) | 9 (6.1%) | 148 |
| HT draw | 38 (28.4%) | 55 (41.0%) | 41 (30.6%) | 134 |
| HT away lead | 10 (9.8%) | 20 (19.6%) | 72 (70.6%) | 102 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (2.6%)
- Away comebacks (trailing at HT, won at FT): **9** (2.3%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | NAC Breda | Heracles | 0-1 | 2-1 |
| 2025-2026 | Heerenveen | Excelsior | 0-1 | 2-1 |
| 2025-2026 | Twente | Heracles | 0-1 | 2-1 |
| 2025-2026 | Utrecht | FC Volendam | 0-1 | 3-1 |
| 2025-2026 | FC Volendam | NAC Breda | 0-1 | 2-1 |
| 2025-2026 | Heracles | G.A. Eagles | 1-2 | 4-2 |
| 2025-2026 | Heerenveen | Zwolle | 1-2 | 4-2 |
| 2025-2026 | Feyenoord | Excelsior | 0-1 | 2-1 |
| 2025-2026 | PSV | Utrecht | 1-2 | 4-3 |
| 2026-2027 | Twente | PSV | 1-2 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Twente | Ajax | 1-0 | 2-3 |
| 2025-2026 | Excelsior | Heracles | 1-0 | 1-2 |
| 2025-2026 | FC Volendam | Nijmegen | 1-0 | 2-3 |
| 2025-2026 | Utrecht | PSV | 1-0 | 1-2 |
| 2025-2026 | Groningen | PSV | 1-0 | 1-2 |
| 2025-2026 | Excelsior | AZ Alkmaar | 1-0 | 1-2 |
| 2025-2026 | Sittard | Twente | 1-0 | 1-2 |
| 2025-2026 | Den Bosch | Almere City | 2-0 | 2-3 |
| 2026-2027 | Heerenveen | AZ Alkmaar | 2-1 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 148 | 114 (77.0%) | 25 (16.9%) | 9 (6.1%) |
| Away lead | 102 | 72 (70.6%) | 20 (19.6%) | 10 (9.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 38 | 28.4% |
| Draw | 55 | 41.0% |
| Away win | 41 | 30.6% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `373` of `384` (97.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 139 | 36.2% | 65 (46.8%) | 27 (19.4%) | 47 (33.8%) |
| 16-30 | 91 | 23.7% | 42 (46.2%) | 21 (23.1%) | 28 (30.8%) |
| 31-45 | 63 | 16.4% | 26 (41.3%) | 20 (31.7%) | 17 (27.0%) |
| 46-60 | 45 | 11.7% | 17 (37.8%) | 13 (28.9%) | 15 (33.3%) |
| 61-75 | 16 | 4.2% | 7 (43.8%) | 5 (31.2%) | 4 (25.0%) |
| 76-90 | 17 | 4.4% | 4 (23.5%) | 3 (17.6%) | 10 (58.8%) |
| 91-120 | 2 | 0.5% | 1 (50.0%) | 0 (0.0%) | 1 (50.0%) |

## 7. Goalless matches
- Overall: **11** of `384` (2.9%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 321 | 10 | 3.1% |
| 2026-2027 | 63 | 1 | 1.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\holland1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\holland1\charts\matches_analysis_home_win_rate.png)

