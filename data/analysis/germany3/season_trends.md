# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:59:51+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: 3. Liga (Germany)
- Scope: league `germany3`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | VfL Osnabruck | 80 | Cottbus | 8 pts |
| 2026-2027 | Duisburg | 18 | Viktoria Koln | 3 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Duisburg beat Viktoria Koln by **3** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 8 pts |  |
| 2026-2027 | 3 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 80 | 72 | 68 | 64 | 35 | 21 |
| 2026-2027 | 18 | 15 | 13 | 12 | 6 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 35 | 18 | 34 | 1 pts |
| 2026-2027 | 17 | 6 | 18 | 5 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 1219 | 3.208 | 46.1% | 23.4% | 30.5% | 6.1% | 52.55 |
| 2026-2027 | 69 | 225 | 3.261 | 42.0% | 20.3% | 37.7% | 2.9% | 9.65 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 7.200)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.100 | 7.200 |
| 2026-2027 | 2.700 | 5.900 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\germany3\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\germany3\charts\season_trends_avg_goals.png)

