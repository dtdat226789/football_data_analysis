# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:00:47+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Tweede Divisie (Netherlands)
- Scope: league `holland3`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Quick Boys | 67 | De Treffers | 4 pts |
| 2026-2027 | Quick Boys | 15 | Kozakken Boys | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Quick Boys beat Kozakken Boys by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 4 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 67 | 63 | 56 | 56 | 42 | 30 |
| 2026-2027 | 15 | 13 | 11 | 10 | 5 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 42 | 16 | 39 | 3 pts |
| 2026-2027 | 15 | 5 | 16 | 5 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 322 | 1069 | 3.32 | 47.5% | 19.6% | 32.9% | 3.1% | 35.88 |
| 2026-2027 | 54 | 186 | 3.444 | 33.3% | 25.9% | 40.7% | 0.0% | 8.22 |

## 6. View divergence
- Largest divergence: **2025-2026** (luck view, avg abs position diff = 6.400)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 6.400 | 5.920 |
| 2026-2027 | 2.333 | 6.111 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\holland3\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\holland3\charts\season_trends_avg_goals.png)

