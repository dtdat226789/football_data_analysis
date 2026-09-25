# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:02:09+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Serie C - Group A (Italy)
- Scope: league `italy3a`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 440 |
| Home wins | 164 (37.3%) |
| Draws | 138 (31.4%) |
| Away wins | 138 (31.4%) |
| Total goals | 1026 |
| Average goals per match | 2.332 |
| Goalless matches | 48 (10.9%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 144 (37.9%) | 115 (30.3%) | 121 (31.8%) | 889 | 2.339 | 37 (9.7%) |
| 2026-2027 | 60 | 20 (33.3%) | 23 (38.3%) | 17 (28.3%) | 137 | 2.283 | 11 (18.3%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 101 (75.4%) | 24 (17.9%) | 9 (6.7%) | 134 |
| HT draw | 55 (27.9%) | 88 (44.7%) | 54 (27.4%) | 197 |
| HT away lead | 8 (7.3%) | 26 (23.9%) | 75 (68.8%) | 109 |

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
| Away lead | 109 | 75 (68.8%) | 26 (23.9%) | 8 (7.3%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 55 | 27.9% |
| Draw | 88 | 44.7% |
| Away win | 54 | 27.4% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `392` of `440` (89.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 112 | 25.5% | 53 (47.3%) | 27 (24.1%) | 32 (28.6%) |
| 16-30 | 100 | 22.7% | 44 (44.0%) | 24 (24.0%) | 32 (32.0%) |
| 31-45 | 65 | 14.8% | 24 (36.9%) | 16 (24.6%) | 25 (38.5%) |
| 46-60 | 49 | 11.1% | 19 (38.8%) | 10 (20.4%) | 20 (40.8%) |
| 61-75 | 38 | 8.6% | 13 (34.2%) | 8 (21.1%) | 17 (44.7%) |
| 76-90 | 21 | 4.8% | 7 (33.3%) | 5 (23.8%) | 9 (42.9%) |
| 91-120 | 7 | 1.6% | 4 (57.1%) | 0 (0.0%) | 3 (42.9%) |

## 7. Goalless matches
- Overall: **48** of `440` (10.9%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 380 | 37 | 9.7% |
| 2026-2027 | 60 | 11 | 18.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\italy3a\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\italy3a\charts\matches_analysis_home_win_rate.png)

