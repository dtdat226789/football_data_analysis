# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:02:03+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: National League (England)
- Scope: league `national`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Rochdale | 112 | York City | 4 pts |
| 2026-2027 | Boreham Wood | 26 | Southend | 6 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2025-2026** - Rochdale beat York City by **4** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 4 pts |  |
| 2026-2027 | 6 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 21 = last safe, 24 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 21 | pos 24 |
|---|---|---|---|---|---|---|
| 2025-2026 | 112 | 108 | 90 | 81 | 42 | 34 |
| 2026-2027 | 26 | 20 | 19 | 18 | 9 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 21 | 42 | 22 | 38 | 4 pts |
| 2026-2027 | 21 | 9 | 22 | 8 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 557 | 1626 | 2.919 | 43.4% | 23.0% | 33.6% | 5.0% | 63.92 |
| 2026-2027 | 120 | 375 | 3.125 | 47.5% | 18.3% | 34.2% | 0.8% | 14.08 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 7.083)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.833 | 7.083 |
| 2026-2027 | 2.500 | 6.667 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\national\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\national\charts\season_trends_avg_goals.png)

