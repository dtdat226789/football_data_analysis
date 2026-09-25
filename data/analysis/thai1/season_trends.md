# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:49:46+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Thai League 1 (Thailand)
- Scope: league `thai1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Buriram | 70 | Port MTI FC | 10 pts |
| 2026-2027 | Buriram | 7 | Rayong FC | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Buriram beat Rayong FC by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 10 pts |  |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025-2026 | 70 | 60 | 52 | 45 | 28 | 23 |
| 2026-2027 | 7 | 7 | 6 | 6 | 3 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 13 | 28 | 14 | 26 | 2 pts |
| 2026-2027 | 13 | 3 | 14 | 1 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 240 | 642 | 2.675 | 43.3% | 31.2% | 25.4% | 7.1% | 40.31 |
| 2026-2027 | 24 | 62 | 2.583 | 41.7% | 16.7% | 41.7% | 4.2% | 4.25 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 4.875)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.125 | 4.625 |
| 2026-2027 | 3.250 | 4.875 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\thai1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\thai1\charts\season_trends_avg_goals.png)

