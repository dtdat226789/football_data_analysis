# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:56:49+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: 3. CFL - Group B (Czech Republic)
- Scope: league `czech3b`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | FK Ceska Lipa | 88 | Zapy | 14 pts |
| 2026-2027 | Zapy | 17 | Jablonec B | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Zapy beat Jablonec B by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 14 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025-2026 | 88 | 74 | 61 | 44 | 34 | 25 |
| 2026-2027 | 17 | 15 | 13 | 12 | 6 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 13 | 34 | 14 | 31 | 3 pts |
| 2026-2027 | 13 | 6 | 14 | 5 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 272 | 912 | 3.353 | 44.1% | 22.1% | 33.8% | 2.6% | 44.47 |
| 2026-2027 | 54 | 167 | 3.093 | 37.0% | 29.6% | 33.3% | 9.3% | 9.12 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 5.529)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.235 | 5.529 |
| 2026-2027 | 2.125 | 4.250 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\czech3b\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\czech3b\charts\season_trends_avg_goals.png)

