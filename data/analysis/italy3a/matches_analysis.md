# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:57:56+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Serie C - Group A (Italy)
- Scope: league `italy3a`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 450 |
| Home wins | 165 (36.7%) |
| Draws | 143 (31.8%) |
| Away wins | 142 (31.6%) |
| Total goals | 1044 |
| Average goals per match | 2.320 |
| Goalless matches | 50 (11.1%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 144 (37.9%) | 115 (30.3%) | 121 (31.8%) | 889 | 2.339 | 37 (9.7%) |
| 2026-2027 | 70 | 21 (30.0%) | 28 (40.0%) | 21 (30.0%) | 155 | 2.214 | 13 (18.6%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 101 (75.4%) | 24 (17.9%) | 9 (6.7%) | 134 |
| HT draw | 56 (27.5%) | 93 (45.6%) | 55 (27.0%) | 204 |
| HT away lead | 8 (7.1%) | 26 (23.2%) | 78 (69.6%) | 112 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (1.8%)
- Away comebacks (trailing at HT, won at FT): **9** (2.0%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | L.R. Vicenza | Arzignano | 0-1 | 2-1 |
| 2025-2026 | Triestina | Arzignano | 0-1 | 2-1 |
| 2025-2026 | AlbinoLeffe | Novara | 1-2 | 3-2 |
| 2025-2026 | Giana Erminio | Lumezzane | 0-1 | 2-1 |
| 2025-2026 | AlbinoLeffe | Pro Vercelli | 0-1 | 2-1 |
| 2025-2026 | Giana Erminio | Arzignano | 0-1 | 2-1 |
| 2025-2026 | Cittadella | Dolomiti Bellunesi | 0-1 | 2-1 |
| 2025-2026 | Cittadella | Lecco | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Brescia | Arzignano | 1-0 | 1-2 |
| 2025-2026 | Renate | Brescia | 1-0 | 1-3 |
| 2025-2026 | Lumezzane | Triestina | 1-0 | 1-2 |
| 2025-2026 | Dolomiti Bellunesi | Pro Vercelli | 1-0 | 1-2 |
| 2025-2026 | Arzignano | Ospitaletto | 1-0 | 1-2 |
| 2025-2026 | Renate | L.R. Vicenza | 1-0 | 1-3 |
| 2025-2026 | Dolomiti Bellunesi | Arzignano | 1-0 | 1-2 |
| 2026-2027 | Carpi | Cittadella | 1-0 | 1-2 |
| 2026-2027 | AlbinoLeffe | Arzignano | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 134 | 101 (75.4%) | 24 (17.9%) | 9 (6.7%) |
| Away lead | 112 | 78 (69.6%) | 26 (23.2%) | 8 (7.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 56 | 27.5% |
| Draw | 93 | 45.6% |
| Away win | 55 | 27.0% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `400` of `450` (88.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 113 | 25.1% | 53 (46.9%) | 27 (23.9%) | 33 (29.2%) |
| 16-30 | 100 | 22.2% | 44 (44.0%) | 24 (24.0%) | 32 (32.0%) |
| 31-45 | 67 | 14.9% | 24 (35.8%) | 16 (23.9%) | 27 (40.3%) |
| 46-60 | 51 | 11.3% | 19 (37.3%) | 12 (23.5%) | 20 (39.2%) |
| 61-75 | 40 | 8.9% | 14 (35.0%) | 9 (22.5%) | 17 (42.5%) |
| 76-90 | 22 | 4.9% | 7 (31.8%) | 5 (22.7%) | 10 (45.5%) |
| 91-120 | 7 | 1.6% | 4 (57.1%) | 0 (0.0%) | 3 (42.9%) |

## 7. Goalless matches
- Overall: **50** of `450` (11.1%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 380 | 37 | 9.7% |
| 2026-2027 | 70 | 13 | 18.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\italy3a\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\italy3a\charts\matches_analysis_home_win_rate.png)

