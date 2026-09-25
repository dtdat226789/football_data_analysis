# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:01:03+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: NB II. (Hungary)
- Scope: league `hungary2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 301 |
| Home wins | 137 (45.5%) |
| Draws | 74 (24.6%) |
| Away wins | 90 (29.9%) |
| Total goals | 774 |
| Average goals per match | 2.571 |
| Goalless matches | 17 (5.6%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 240 | 105 (43.8%) | 60 (25.0%) | 75 (31.2%) | 602 | 2.508 | 15 (6.2%) |
| 2026-2027 | 61 | 32 (52.5%) | 14 (23.0%) | 15 (24.6%) | 172 | 2.82 | 2 (3.3%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 80 (80.0%) | 18 (18.0%) | 2 (2.0%) | 100 |
| HT draw | 51 (39.5%) | 36 (27.9%) | 42 (32.6%) | 129 |
| HT away lead | 6 (8.3%) | 20 (27.8%) | 46 (63.9%) | 72 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **6** (2.0%)
- Away comebacks (trailing at HT, won at FT): **2** (0.7%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | BVSC-Zuglo | Szentlorinc | 0-1 | 2-1 |
| 2025-2026 | Karcagi | Bekescsaba 1912 | 0-1 | 4-2 |
| 2025-2026 | Karcagi | Budafoki | 0-1 | 3-2 |
| 2025-2026 | Szentlorinc | Videoton | 0-1 | 2-1 |
| 2025-2026 | Kozarmisleny SE | Karcagi | 0-1 | 2-1 |
| 2026-2027 | Videoton | DVTK | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Szentlorinc | Kecskemeti TE | 2-1 | 3-4 |
| 2026-2027 | Kozarmisleny SE | Szeged | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 100 | 80 (80.0%) | 18 (18.0%) | 2 (2.0%) |
| Away lead | 72 | 46 (63.9%) | 20 (27.8%) | 6 (8.3%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 51 | 39.5% |
| Draw | 36 | 27.9% |
| Away win | 42 | 32.6% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `284` of `301` (94.4%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 95 | 31.6% | 44 (46.3%) | 24 (25.3%) | 27 (28.4%) |
| 16-30 | 62 | 20.6% | 34 (54.8%) | 12 (19.4%) | 16 (25.8%) |
| 31-45 | 55 | 18.3% | 28 (50.9%) | 13 (23.6%) | 14 (25.5%) |
| 46-60 | 34 | 11.3% | 14 (41.2%) | 6 (17.6%) | 14 (41.2%) |
| 61-75 | 16 | 5.3% | 7 (43.8%) | 1 (6.2%) | 8 (50.0%) |
| 76-90 | 20 | 6.6% | 9 (45.0%) | 1 (5.0%) | 10 (50.0%) |
| 91-120 | 2 | 0.7% | 1 (50.0%) | 0 (0.0%) | 1 (50.0%) |

## 7. Goalless matches
- Overall: **17** of `301` (5.6%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 240 | 15 | 6.2% |
| 2026-2027 | 61 | 2 | 3.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\hungary2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\hungary2\charts\matches_analysis_home_win_rate.png)

