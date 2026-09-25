# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:00:14+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Super League 2 (Greece)
- Scope: league `greece2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Kalamata | 66 | Iraklis 1908 | 6 pts |
| 2026-2027 | Marko | 9 | Ellas Syrou | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Marko beat Ellas Syrou by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 6 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025-2026 | 66 | 60 | 48 | 45 | 35 | 23 |
| 2026-2027 | 9 | 7 | 7 | 6 | 1 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 13 | 35 | 14 | 31 | 4 pts |
| 2026-2027 | 13 | 1 | 14 | 1 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 265 | 607 | 2.291 | 44.2% | 23.0% | 32.8% | 7.9% | 36.7 |
| 2026-2027 | 24 | 54 | 2.25 | 58.3% | 25.0% | 16.7% | 8.3% | 4.12 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 7.500)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.700 | 7.500 |
| 2026-2027 | 1.625 | 4.125 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\greece2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\greece2\charts\season_trends_avg_goals.png)

