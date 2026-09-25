# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:50:39+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Super League Women (Belgium)
- Scope: league `wbelgium1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Leuven W | 70 | RSC Anderlecht W | 15 pts |
| 2026-2027 | RSC Anderlecht W | 9 | Club Brugge W | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - RSC Anderlecht W beat Club Brugge W by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 15 pts |  |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 5 = last safe, 8 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 5 | pos 6 | pos 8 |
|---|---|---|---|---|---|---|
| 2025-2026 | 70 | 55 | 39 | 31 | 29 | 16 |
| 2026-2027 | 9 | 9 | 6 | 3 | 1 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 5 | 31 | 6 | 29 | 2 pts |
| 2026-2027 | 5 | 3 | 6 | 1 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 108 | 324 | 3.0 | 40.7% | 23.1% | 36.1% | 5.6% | 37.38 |
| 2026-2027 | 12 | 35 | 2.917 | 66.7% | 8.3% | 25.0% | 8.3% | 4.38 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 3.250)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 1.750 | 3.250 |
| 2026-2027 | 1.250 | 2.500 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\wbelgium1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\wbelgium1\charts\season_trends_avg_goals.png)

