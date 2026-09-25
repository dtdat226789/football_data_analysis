# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:03:14+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Virsliga (Latvia)
- Scope: league `latvia`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 336 |
| Home wins | 147 (43.8%) |
| Draws | 80 (23.8%) |
| Away wins | 109 (32.4%) |
| Total goals | 973 |
| Average goals per match | 2.896 |
| Goalless matches | 19 (5.7%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 182 | 83 (45.6%) | 43 (23.6%) | 56 (30.8%) | 535 | 2.94 | 11 (6.0%) |
| 2026 | 154 | 64 (41.6%) | 37 (24.0%) | 53 (34.4%) | 438 | 2.844 | 8 (5.2%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 97 (80.8%) | 18 (15.0%) | 5 (4.2%) | 120 |
| HT draw | 41 (33.3%) | 42 (34.1%) | 40 (32.5%) | 123 |
| HT away lead | 9 (9.7%) | 20 (21.5%) | 64 (68.8%) | 93 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **9** (2.7%)
- Away comebacks (trailing at HT, won at FT): **5** (1.5%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Grobina | BFC Daugavpils | 0-1 | 3-2 |
| 2025 | Metta | Tukums 2000 | 1-2 | 3-2 |
| 2025 | RFS | FK Liepaja | 0-1 | 4-1 |
| 2025 | Jelgava | Tukums 2000 | 0-1 | 2-1 |
| 2025 | BFC Daugavpils | Grobina | 1-2 | 3-2 |
| 2025 | Tukums 2000 | Super Nova | 0-1 | 2-1 |
| 2026 | Ogre United | Tukums 2000 | 1-2 | 3-2 |
| 2026 | Riga FC | Tukums 2000 | 0-1 | 3-1 |
| 2026 | Tukums 2000 | Ogre United | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2026 | Jelgava | Auda | 2-1 | 2-3 |
| 2026 | Ogre United | RFS | 3-2 | 3-4 |
| 2026 | Super Nova | FK Liepaja | 1-0 | 1-2 |
| 2026 | Ogre United | Jelgava | 2-1 | 2-3 |
| 2026 | BFC Daugavpils | RFS | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 120 | 97 (80.8%) | 18 (15.0%) | 5 (4.2%) |
| Away lead | 93 | 64 (68.8%) | 20 (21.5%) | 9 (9.7%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 41 | 33.3% |
| Draw | 42 | 34.1% |
| Away win | 40 | 32.5% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `317` of `336` (94.3%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 104 | 31.0% | 51 (49.0%) | 14 (13.5%) | 39 (37.5%) |
| 16-30 | 85 | 25.3% | 42 (49.4%) | 19 (22.4%) | 24 (28.2%) |
| 31-45 | 45 | 13.4% | 18 (40.0%) | 12 (26.7%) | 15 (33.3%) |
| 46-60 | 43 | 12.8% | 21 (48.8%) | 8 (18.6%) | 14 (32.6%) |
| 61-75 | 17 | 5.1% | 7 (41.2%) | 7 (41.2%) | 3 (17.6%) |
| 76-90 | 19 | 5.7% | 7 (36.8%) | 1 (5.3%) | 11 (57.9%) |
| 91-120 | 4 | 1.2% | 1 (25.0%) | 0 (0.0%) | 3 (75.0%) |

## 7. Goalless matches
- Overall: **19** of `336` (5.7%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 182 | 11 | 6.0% |
| 2026 | 154 | 8 | 5.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\latvia\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\latvia\charts\matches_analysis_home_win_rate.png)

