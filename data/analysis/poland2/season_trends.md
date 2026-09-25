# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:41:17+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Division 1 (Poland)
- Scope: league `poland2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Wisla | 72 | Slask Wroclaw | 8 pts |
| 2026-2027 | Grodzisk M. | 18 | Termalica B-B. | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Grodzisk M. beat Termalica B-B. by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 8 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 72 | 64 | 55 | 55 | 36 | 28 |
| 2026-2027 | 18 | 16 | 15 | 14 | 9 | 6 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 36 | 16 | 30 | 6 pts |
| 2026-2027 | 15 | 9 | 16 | 9 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 328 | 991 | 3.021 | 41.5% | 27.1% | 31.4% | 4.6% | 46.95 |
| 2026-2027 | 80 | 220 | 2.75 | 42.5% | 28.8% | 28.8% | 5.0% | 12.06 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 6.526)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.474 | 6.526 |
| 2026-2027 | 2.222 | 6.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\poland2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\poland2\charts\season_trends_avg_goals.png)

