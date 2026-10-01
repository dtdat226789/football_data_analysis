# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:01:47+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Botola Pro (Morocco)
- Scope: league `morocco`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2024-2025 | Berkane | 70 | FAR Rabat | 13 pts |
| 2025-2026 | Maghreb Fez | 59 | Raja Casablanca | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2025-2026** - Maghreb Fez beat Raja Casablanca by **2** pts

| season | margin | tight |
|---|---|---|
| 2024-2025 | 13 pts |  |
| 2025-2026 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 14 = last safe, 17 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 14 | pos 17 |
|---|---|---|---|---|---|---|
| 2024-2025 | 70 | 57 | 53 | 47 | 25 | - |
| 2025-2026 | 59 | 57 | 55 | 40 | 31 | 20 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2024-2025 | 14 | 25 | 15 | 23 | 2 pts |
| 2025-2026 | 14 | 31 | 15 | 30 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2024-2025 | 240 | 555 | 2.312 | 43.3% | 28.3% | 28.3% | 9.2% | 40.75 |
| 2025-2026 | 248 | 539 | 2.173 | 37.9% | 34.3% | 27.8% | 11.7% | 38.76 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 6.706)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2024-2025 | 2.625 | 5.000 |
| 2025-2026 | 3.882 | 6.706 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\morocco\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\morocco\charts\season_trends_avg_goals.png)

