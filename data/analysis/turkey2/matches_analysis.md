# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:10:43+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: 1. Lig (Turkey)
- Scope: league `turkey2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 465 |
| Home wins | 203 (43.7%) |
| Draws | 123 (26.5%) |
| Away wins | 139 (29.9%) |
| Total goals | 1332 |
| Average goals per match | 2.865 |
| Goalless matches | 34 (7.3%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 385 | 175 (45.5%) | 95 (24.7%) | 115 (29.9%) | 1125 | 2.922 | 28 (7.3%) |
| 2026-2027 | 80 | 28 (35.0%) | 28 (35.0%) | 24 (30.0%) | 207 | 2.587 | 6 (7.5%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 119 (78.3%) | 22 (14.5%) | 11 (7.2%) | 152 |
| HT draw | 74 (37.4%) | 79 (39.9%) | 45 (22.7%) | 198 |
| HT away lead | 10 (8.8%) | 22 (19.3%) | 82 (71.9%) | 114 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (2.2%)
- Away comebacks (trailing at HT, won at FT): **11** (2.4%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Amedspor | Erokspor | 0-1 | 2-1 |
| 2025-2026 | Manisa FK | Vanspor FK | 0-1 | 2-1 |
| 2025-2026 | Istanbulspor AS | Sivasspor | 0-1 | 2-1 |
| 2025-2026 | Manisa FK | Bandirmaspor | 0-1 | 3-2 |
| 2025-2026 | Vanspor FK | Bodrumspor | 0-1 | 3-1 |
| 2025-2026 | Istanbulspor AS | Sariyer | 0-1 | 3-1 |
| 2025-2026 | Serik Spor | Hatayspor | 0-1 | 4-2 |
| 2025-2026 | Sivasspor | Igdir FK | 0-1 | 2-1 |
| 2025-2026 | Boluspor | Serik Spor | 0-1 | 3-1 |
| 2026-2027 | Batman Petrolspor | Sivasspor | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Hatayspor | Keciorengucu | 1-0 | 1-3 |
| 2025-2026 | Boluspor | Vanspor FK | 2-1 | 2-3 |
| 2025-2026 | Manisa FK | Erokspor | 2-1 | 3-4 |
| 2025-2026 | Sariyer | Istanbulspor AS | 1-0 | 1-2 |
| 2025-2026 | Keciorengucu | Erzurumspor | 1-0 | 1-2 |
| 2025-2026 | Serik Spor | Corum | 2-1 | 2-3 |
| 2025-2026 | Sakaryaspor | Erokspor | 1-0 | 1-2 |
| 2026-2027 | Antalyaspor | Sariyer | 1-0 | 1-2 |
| 2026-2027 | Kayserispor | Bursaspor | 1-0 | 1-2 |
| 2026-2027 | Umraniyespor | Antalyaspor | 1-0 | 1-2 |
| 2026-2027 | Batman Petrolspor | Bursaspor | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 152 | 119 (78.3%) | 22 (14.5%) | 11 (7.2%) |
| Away lead | 114 | 82 (71.9%) | 22 (19.3%) | 10 (8.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 74 | 37.4% |
| Draw | 79 | 39.9% |
| Away win | 45 | 22.7% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `430` of `465` (92.5%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 140 | 30.1% | 60 (42.9%) | 35 (25.0%) | 45 (32.1%) |
| 16-30 | 104 | 22.4% | 51 (49.0%) | 19 (18.3%) | 34 (32.7%) |
| 31-45 | 74 | 15.9% | 32 (43.2%) | 15 (20.3%) | 27 (36.5%) |
| 46-60 | 64 | 13.8% | 34 (53.1%) | 12 (18.8%) | 18 (28.1%) |
| 61-75 | 29 | 6.2% | 17 (58.6%) | 6 (20.7%) | 6 (20.7%) |
| 76-90 | 17 | 3.7% | 8 (47.1%) | 2 (11.8%) | 7 (41.2%) |
| 91-120 | 2 | 0.4% | 1 (50.0%) | 0 (0.0%) | 1 (50.0%) |

## 7. Goalless matches
- Overall: **34** of `465` (7.3%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 385 | 28 | 7.3% |
| 2026-2027 | 80 | 6 | 7.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\turkey2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\turkey2\charts\matches_analysis_home_win_rate.png)

