# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:00:36+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Eerste Divisie (Netherlands)
- Scope: league `holland2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Den Haag | 89 | Cambuur | 11 pts |
| 2026-2027 | Heracles | 18 | Almere City | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Heracles beat Almere City by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 11 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 89 | 78 | 68 | 60 | 40 | 35 |
| 2026-2027 | 18 | 16 | 13 | 13 | 7 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 40 | 18 | 39 | 1 pts |
| 2026-2027 | 17 | 7 | 18 | 6 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 392 | 1248 | 3.184 | 42.6% | 21.7% | 35.7% | 3.6% | 51.67 |
| 2026-2027 | 74 | 279 | 3.77 | 52.7% | 16.2% | 31.1% | 2.7% | 10.5 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 6.500)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 5.429 | 5.905 |
| 2026-2027 | 2.500 | 6.500 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\holland2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\holland2\charts\season_trends_avg_goals.png)

