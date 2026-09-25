# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:51:08+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Bundesliga Women (Germany)
- Scope: league `wgermany1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 217 |
| Home wins | 98 (45.2%) |
| Draws | 37 (17.1%) |
| Away wins | 82 (37.8%) |
| Total goals | 748 |
| Average goals per match | 3.447 |
| Goalless matches | 7 (3.2%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 182 | 81 (44.5%) | 32 (17.6%) | 69 (37.9%) | 627 | 3.445 | 7 (3.8%) |
| 2026-2027 | 35 | 17 (48.6%) | 5 (14.3%) | 13 (37.1%) | 121 | 3.457 | 0 (0.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 71 (80.7%) | 8 (9.1%) | 9 (10.2%) | 88 |
| HT draw | 22 (36.1%) | 18 (29.5%) | 21 (34.4%) | 61 |
| HT away lead | 5 (7.4%) | 11 (16.2%) | 52 (76.5%) | 68 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **5** (2.3%)
- Away comebacks (trailing at HT, won at FT): **9** (4.1%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Freiburg W | Eintracht Frankfurt W | 0-1 | 3-2 |
| 2025-2026 | Wolfsburg W | Freiburg W | 0-1 | 3-1 |
| 2025-2026 | Bayern Munich W | Wolfsburg W | 0-1 | 4-1 |
| 2025-2026 | Wolfsburg W | RB Leipzig W | 0-1 | 3-2 |
| 2026-2027 | Wolfsburg W | Werder Bremen W | 0-1 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Union Berlin W | Wolfsburg W | 1-0 | 1-4 |
| 2025-2026 | Hamburger SV W | 1.FC Nurnberg W | 1-0 | 1-2 |
| 2025-2026 | Union Berlin W | Bayer Leverkusen W | 1-0 | 1-2 |
| 2025-2026 | SGS Essen W | Union Berlin W | 2-1 | 2-4 |
| 2025-2026 | Koln W | Eintracht Frankfurt W | 1-0 | 1-2 |
| 2026-2027 | 1.FC Nurnberg W | Wolfsburg W | 2-0 | 2-8 |
| 2026-2027 | Bayer Leverkusen W | Bayern Munich W | 1-0 | 2-3 |
| 2026-2027 | Mainz W | Eintracht Frankfurt W | 2-0 | 2-3 |
| 2026-2027 | Freiburg W | Bayer Leverkusen W | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 88 | 71 (80.7%) | 8 (9.1%) | 9 (10.2%) |
| Away lead | 68 | 52 (76.5%) | 11 (16.2%) | 5 (7.4%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 22 | 36.1% |
| Draw | 18 | 29.5% |
| Away win | 21 | 34.4% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `210` of `217` (96.8%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 90 | 41.5% | 44 (48.9%) | 8 (8.9%) | 38 (42.2%) |
| 16-30 | 60 | 27.6% | 25 (41.7%) | 11 (18.3%) | 24 (40.0%) |
| 31-45 | 24 | 11.1% | 12 (50.0%) | 5 (20.8%) | 7 (29.2%) |
| 46-60 | 20 | 9.2% | 12 (60.0%) | 1 (5.0%) | 7 (35.0%) |
| 61-75 | 9 | 4.1% | 3 (33.3%) | 3 (33.3%) | 3 (33.3%) |
| 76-90 | 6 | 2.8% | 2 (33.3%) | 2 (33.3%) | 2 (33.3%) |
| 91-120 | 1 | 0.5% | 0 (0.0%) | 0 (0.0%) | 1 (100.0%) |

## 7. Goalless matches
- Overall: **7** of `217` (3.2%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 182 | 7 | 3.8% |
| 2026-2027 | 35 | 0 | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\wgermany1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\wgermany1\charts\matches_analysis_home_win_rate.png)

