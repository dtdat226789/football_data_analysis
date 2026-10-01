# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:50:16+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Ligue 2 (France)
- Scope: league `france2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Troyes | 67 | Le Mans | 5 pts |
| 2026-2027 | St Etienne | 16 | Red Star | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - St Etienne beat Red Star by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 5 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 67 | 62 | 60 | 56 | 36 | 24 |
| 2026-2027 | 16 | 14 | 12 | 10 | 7 | 5 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 36 | 16 | 36 | 0 pts |
| 2026-2027 | 15 | 7 | 16 | 6 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 310 | 784 | 2.529 | 37.7% | 30.6% | 31.6% | 10.6% | 43.79 |
| 2026-2027 | 63 | 162 | 2.571 | 33.3% | 36.5% | 30.2% | 11.1% | 9.22 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 5.778)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.474 | 4.737 |
| 2026-2027 | 1.667 | 5.778 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\france2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\france2\charts\season_trends_avg_goals.png)

