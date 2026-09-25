# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:50:21+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: 1. Lig (Turkey)
- Scope: league `turkey2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Erzurumspor | 81 | Corum | 4 pts |
| 2026-2027 | Kayserispor | 19 | Bursaspor | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Kayserispor beat Bursaspor by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 4 pts |  |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 81 | 77 | 74 | 63 | 39 | 6 |
| 2026-2027 | 19 | 19 | 16 | 13 | 6 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 39 | 18 | 34 | 5 pts |
| 2026-2027 | 17 | 6 | 18 | 5 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 385 | 1125 | 2.922 | 45.5% | 24.7% | 29.9% | 7.3% | 52.85 |
| 2026-2027 | 80 | 207 | 2.587 | 35.0% | 35.0% | 30.0% | 7.5% | 10.6 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 7.300)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 4.300 | 7.300 |
| 2026-2027 | 1.700 | 6.300 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\turkey2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\turkey2\charts\season_trends_avg_goals.png)

