# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:54:28+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Ligue 1 (Algeria)
- Scope: league `algir1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | MC Alger | 65 | Saoura | 10 pts |
| 2026-2027 | CR Belouizdad | 8 | USM Alger | 1 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - CR Belouizdad beat USM Alger by **1** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 10 pts |  |
| 2026-2027 | 1 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 11 = last safe, 14 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 11 | pos 14 |
|---|---|---|---|---|---|---|
| 2025-2026 | 65 | 55 | 49 | 45 | 39 | 24 |
| 2026-2027 | 8 | 7 | 5 | 5 | 3 | 2 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 11 | 39 | 12 | 36 | 3 pts |
| 2026-2027 | 11 | 3 | 12 | 3 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 240 | 544 | 2.267 | 50.0% | 29.2% | 20.8% | 8.3% | 40.62 |
| 2026-2027 | 22 | 56 | 2.545 | 45.5% | 31.8% | 22.7% | 4.5% | 3.69 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 5.500)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 1.500 | 4.625 |
| 2026-2027 | 2.375 | 5.500 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\algir1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\algir1\charts\season_trends_avg_goals.png)

