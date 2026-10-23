# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:03:30+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Liga Portugal (Portugal)
- Scope: league `portugal1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | FC Porto | 88 | Sporting CP | 6 pts |
| 2026-2027 | FC Porto | 21 | Benfica | 5 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2026-2027** - FC Porto beat Benfica by **5** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 6 pts |  |
| 2026-2027 | 5 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 88 | 82 | 59 | 50 | 34 | 21 |
| 2026-2027 | 21 | 16 | 15 | 11 | 4 | 2 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 34 | 16 | 30 | 4 pts |
| 2026-2027 | 15 | 4 | 16 | 4 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 308 | 823 | 2.672 | 41.2% | 27.3% | 31.5% | 6.8% | 44.21 |
| 2026-2027 | 62 | 170 | 2.742 | 38.7% | 29.0% | 32.3% | 6.5% | 9.33 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 5.111)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.368 | 4.737 |
| 2026-2027 | 3.333 | 5.111 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\portugal1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\portugal1\charts\season_trends_avg_goals.png)

