# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:58:29+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Ykkosliiga (Finland)
- Scope: league `finland2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Lahti | 57 | TPS | 7 pts |
| 2026 | KTP | 57 | PK-35 | 9 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2025** - Lahti beat TPS by **7** pts

| season | margin | tight |
|---|---|---|
| 2025 | 7 pts |  |
| 2026 | 9 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 7 = last safe, 10 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 7 | pos 10 |
|---|---|---|---|---|---|---|
| 2025 | 57 | 50 | 37 | 31 | 29 | 19 |
| 2026 | 57 | 48 | 40 | 28 | 28 | 13 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 7 | 29 | 8 | 22 | 7 pts |
| 2026 | 7 | 28 | 8 | 21 | 7 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 135 | 443 | 3.281 | 43.0% | 25.9% | 31.1% | 3.7% | 18.5 |
| 2026 | 120 | 309 | 2.575 | 41.7% | 21.7% | 36.7% | 6.7% | 33.4 |

## 6. View divergence
- Largest divergence: **2025** (luck view, avg abs position diff = 5.700)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 5.700 | 5.400 |
| 2026 | 1.000 | 3.200 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\finland2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\finland2\charts\season_trends_avg_goals.png)

