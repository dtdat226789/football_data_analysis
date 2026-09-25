# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:43:30+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Premier League (Russia)
- Scope: league `russia`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Zenit | 68 | Krasnodar | 2 pts |
| 2026-2027 | CSKA Moscow | 22 | Krasnodar | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026-2027** - CSKA Moscow beat Krasnodar by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 2 pts | yes |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025-2026 | 68 | 66 | 52 | 46 | 30 | 22 |
| 2026-2027 | 22 | 22 | 19 | 12 | 9 | 3 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 13 | 30 | 14 | 29 | 1 pts |
| 2026-2027 | 13 | 9 | 14 | 7 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 244 | 615 | 2.52 | 45.1% | 27.5% | 27.5% | 6.1% | 36.94 |
| 2026-2027 | 76 | 212 | 2.789 | 35.5% | 34.2% | 30.3% | 7.9% | 12.62 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 5.500)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.556 | 4.667 |
| 2026-2027 | 1.750 | 5.500 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\russia\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\russia\charts\season_trends_avg_goals.png)

