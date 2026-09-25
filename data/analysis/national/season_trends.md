# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:03:46+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: National League (England)
- Scope: league `national`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Rochdale | 112 | York City | 4 pts |
| 2026-2027 | Boreham Wood | 23 | Southend | 3 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Boreham Wood beat Southend by **3** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 4 pts |  |
| 2026-2027 | 3 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 21 = last safe, 24 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 21 | pos 24 |
|---|---|---|---|---|---|---|
| 2025-2026 | 112 | 108 | 90 | 81 | 42 | 34 |
| 2026-2027 | 23 | 20 | 17 | 16 | 8 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 21 | 42 | 22 | 38 | 4 pts |
| 2026-2027 | 21 | 8 | 22 | 7 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 557 | 1626 | 2.919 | 43.4% | 23.0% | 33.6% | 5.0% | 63.92 |
| 2026-2027 | 108 | 325 | 3.009 | 47.2% | 19.4% | 33.3% | 0.9% | 12.62 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 7.083)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.833 | 7.083 |
| 2026-2027 | 2.833 | 6.667 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\national\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\national\charts\season_trends_avg_goals.png)

