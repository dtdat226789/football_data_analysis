# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:03:08+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Division 1 (Poland)
- Scope: league `poland2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 408 |
| Home wins | 170 (41.7%) |
| Draws | 112 (27.5%) |
| Away wins | 126 (30.9%) |
| Total goals | 1211 |
| Average goals per match | 2.968 |
| Goalless matches | 19 (4.7%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 328 | 136 (41.5%) | 89 (27.1%) | 103 (31.4%) | 991 | 3.021 | 15 (4.6%) |
| 2026-2027 | 80 | 34 (42.5%) | 23 (28.8%) | 23 (28.8%) | 220 | 2.75 | 4 (5.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 107 (72.3%) | 28 (18.9%) | 13 (8.8%) | 148 |
| HT draw | 55 (35.5%) | 60 (38.7%) | 40 (25.8%) | 155 |
| HT away lead | 7 (6.7%) | 24 (23.1%) | 73 (70.2%) | 104 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (1.7%)
- Away comebacks (trailing at HT, won at FT): **13** (3.2%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Pogon Siedlce | Ruch Chorzow | 0-1 | 2-1 |
| 2025-2026 | Grodzisk M. | Polonia Bytom | 0-1 | 2-1 |
| 2025-2026 | Puszcza | Polonia Warszawa | 0-1 | 2-1 |
| 2025-2026 | Wieczysta Krakow | Polonia Bytom | 0-2 | 4-3 |
| 2025-2026 | LKS Lodz | Leczna | 0-1 | 3-1 |
| 2026-2027 | Polonia Warszawa | Skierniewice | 0-1 | 3-1 |
| 2026-2027 | Skierniewice | Grodzisk M. | 0-1 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Puszcza | Tychy | 1-0 | 1-2 |
| 2025-2026 | Pogon Siedlce | Slask Wroclaw | 2-1 | 2-3 |
| 2025-2026 | Leczna | Wisla | 1-0 | 1-2 |
| 2025-2026 | Stal Mielec | Legnica | 1-0 | 1-2 |
| 2025-2026 | Wieczysta Krakow | Grodzisk M. | 2-1 | 2-3 |
| 2025-2026 | KS Wieczysta Krakow | Grodzisk M. | 2-1 | 2-3 |
| 2025-2026 | Polonia Bytom | LKS Lodz | 1-0 | 2-3 |
| 2025-2026 | Stal Mielec | LKS Lodz | 1-0 | 1-2 |
| 2025-2026 | Pruszkow | Odra Opole | 2-0 | 2-3 |
| 2025-2026 | S. Rzeszow | Wisla | 1-0 | 1-2 |
| 2025-2026 | Polonia Bytom | Slask Wroclaw | 1-0 | 1-3 |
| 2025-2026 | Odra Opole | Polonia Warszawa | 1-0 | 1-2 |
| 2026-2027 | Pogon Siedlce | Termalica B-B. | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 148 | 107 (72.3%) | 28 (18.9%) | 13 (8.8%) |
| Away lead | 104 | 73 (70.2%) | 24 (23.1%) | 7 (6.7%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 55 | 35.5% |
| Draw | 60 | 38.7% |
| Away win | 40 | 25.8% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `388` of `408` (95.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 131 | 32.1% | 60 (45.8%) | 33 (25.2%) | 38 (29.0%) |
| 16-30 | 93 | 22.8% | 40 (43.0%) | 19 (20.4%) | 34 (36.6%) |
| 31-45 | 68 | 16.7% | 31 (45.6%) | 15 (22.1%) | 22 (32.4%) |
| 46-60 | 53 | 13.0% | 23 (43.4%) | 17 (32.1%) | 13 (24.5%) |
| 61-75 | 26 | 6.4% | 9 (34.6%) | 4 (15.4%) | 13 (50.0%) |
| 76-90 | 15 | 3.7% | 5 (33.3%) | 4 (26.7%) | 6 (40.0%) |
| 91-120 | 2 | 0.5% | 1 (50.0%) | 1 (50.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **19** of `408` (4.7%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 328 | 15 | 4.6% |
| 2026-2027 | 80 | 4 | 5.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\poland2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\poland2\charts\matches_analysis_home_win_rate.png)

