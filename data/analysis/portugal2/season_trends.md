# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:41:54+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Liga Portugal 2 (Portugal)
- Scope: league `portugal2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Maritimo | 66 | Torreense | 6 pts |
| 2026-2027 | Lusitania FC | 16 | Penafiel | 3 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Lusitania FC beat Penafiel by **3** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 6 pts |  |
| 2026-2027 | 3 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 66 | 60 | 51 | 50 | 41 | 34 |
| 2026-2027 | 16 | 13 | 11 | 10 | 5 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 41 | 16 | 40 | 1 pts |
| 2026-2027 | 15 | 5 | 16 | 4 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 310 | 751 | 2.423 | 42.3% | 24.5% | 33.2% | 10.6% | 42.7 |
| 2026-2027 | 53 | 123 | 2.321 | 41.5% | 22.6% | 35.8% | 7.5% | 8.17 |

## 6. View divergence
- Largest divergence: **2025-2026** (luck view, avg abs position diff = 5.600)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 5.600 | 5.200 |
| 2026-2027 | 1.444 | 5.222 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\portugal2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\portugal2\charts\season_trends_avg_goals.png)

