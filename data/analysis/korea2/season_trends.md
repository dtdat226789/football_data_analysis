# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:02:59+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: K League 2 (South Korea)
- Scope: league `korea2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Incheon | 76 | Suwon Bluewings | 7 pts |
| 2026 | Suwon Bluewings | 56 | Suwon FC | 7 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2025** - Incheon beat Suwon Bluewings by **7** pts

| season | margin | tight |
|---|---|---|
| 2025 | 7 pts |  |
| 2026 | 7 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 14 = last safe, 17 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 14 | pos 17 |
|---|---|---|---|---|---|---|
| 2025 | 76 | 69 | 61 | 54 | 28 | 3 |
| 2026 | 56 | 49 | 46 | 41 | 24 | 14 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 14 | 28 | 15 | 26 | 2 pts |
| 2026 | 14 | 24 | 15 | 22 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 273 | 686 | 2.513 | 35.2% | 29.3% | 35.5% | 9.5% | 26.39 |
| 2026 | 220 | 588 | 2.673 | 35.0% | 33.2% | 31.8% | 7.3% | 34.53 |

## 6. View divergence
- Largest divergence: **2025** (goals view, avg abs position diff = 10.000)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 7.857 | 10.000 |
| 2026 | 2.706 | 5.412 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\korea2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\korea2\charts\season_trends_avg_goals.png)

