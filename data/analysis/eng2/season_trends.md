# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:57:54+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: League Two (England)
- Scope: league `eng2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Notts Co | 87 | Bromley | 0 pts |
| 2026-2027 | Barnet | 15 | Walsall | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Notts Co beat Bromley by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 0 pts | yes |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 21 = last safe, 24 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 21 | pos 24 |
|---|---|---|---|---|---|---|
| 2025-2026 | 87 | 87 | 84 | 80 | 41 | 36 |
| 2026-2027 | 15 | 13 | 12 | 12 | 6 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 21 | 41 | 22 | 40 | 1 pts |
| 2026-2027 | 21 | 6 | 22 | 6 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 557 | 1434 | 2.575 | 41.8% | 25.0% | 33.2% | 6.6% | 63.75 |
| 2026-2027 | 84 | 212 | 2.524 | 51.2% | 35.7% | 13.1% | 9.5% | 9.25 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 7.333)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.500 | 7.333 |
| 2026-2027 | 3.167 | 6.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\eng2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\eng2\charts\season_trends_avg_goals.png)

