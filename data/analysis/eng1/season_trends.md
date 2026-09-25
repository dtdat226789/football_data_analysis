# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:57:42+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: League One (England)
- Scope: league `eng1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Lincoln | 103 | Cardiff | 12 pts |
| 2026-2027 | Bradford City | 15 | Sheffield Wed | 1 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Bradford City beat Sheffield Wed by **1** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 12 pts |  |
| 2026-2027 | 1 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 21 = last safe, 24 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 21 | pos 24 |
|---|---|---|---|---|---|---|
| 2025-2026 | 103 | 91 | 83 | 75 | 49 | 35 |
| 2026-2027 | 15 | 14 | 12 | 11 | 6 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 21 | 49 | 22 | 42 | 7 pts |
| 2026-2027 | 21 | 6 | 22 | 6 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 557 | 1462 | 2.625 | 46.1% | 25.0% | 28.9% | 5.9% | 63.83 |
| 2026-2027 | 83 | 243 | 2.928 | 34.9% | 32.5% | 32.5% | 9.6% | 9.25 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 7.083)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.917 | 6.333 |
| 2026-2027 | 2.833 | 7.083 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\eng1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\eng1\charts\season_trends_avg_goals.png)

